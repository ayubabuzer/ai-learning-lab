"""Fast UI/handler tests: deliberately no model download, GPU, or HF account."""
from __future__ import annotations

import importlib.util
import ast
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))


class DummyBatchEncoding(dict):
    """Transformers 5-style tokenizer return object: mapping, not tensor."""


class DummyTokenizer:
    eos_token_id = 0

    @classmethod
    def from_pretrained(cls, _model_id):
        return cls()

    def apply_chat_template(self, messages, **kwargs):
        import torch
        # v5 returns a BatchEncoding mapping by default. Deliberately do not
        # expose .shape or .to so tests catch treating it as a Tensor.
        assert kwargs["return_dict"] is True
        ids = torch.tensor([[1, 2, 3]])
        return DummyBatchEncoding(input_ids=ids, attention_mask=torch.ones_like(ids))

    def decode(self, tokens, **_kwargs):
        return "Hello! I'm Alex, an imaginary robot."


class DummyModel:
    @classmethod
    def from_pretrained(cls, *_args, **_kwargs):
        return cls()

    def to(self, _device):
        return self

    def eval(self):
        return self

    def generate(self, *, input_ids, attention_mask, **_kwargs):
        import torch
        assert torch.equal(attention_mask, torch.ones_like(input_ids))
        return torch.cat([input_ids, torch.tensor([[4]])], dim=1)


def load_app():
    import functools
    import torch  # Must precede Gradio for the local mocked run.
    import gradio  # Loaded before temporary sys.modules patch is restored.
    fake_spaces = types.ModuleType("spaces")

    def gpu(*_args, **_kwargs):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapped(*args, **kwargs):
                return fn(*args, **kwargs)
            wrapped._is_gpu = True
            return wrapped
        return decorator

    fake_spaces.GPU = gpu
    fake_transformers = types.ModuleType("transformers")
    fake_transformers.AutoTokenizer = DummyTokenizer
    fake_transformers.AutoModelForCausalLM = DummyModel

    with patch.dict(sys.modules, {"spaces": fake_spaces, "transformers": fake_transformers}):
        spec = importlib.util.spec_from_file_location("digital_twin_app_under_test", HERE / "app.py")
        app = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app)
    return app


class StaticHandlerTest(unittest.TestCase):
    """These release-critical checks run without torch, gradio or model downloads."""

    def test_gpu_decorator_on_registered_chat_handler(self):
        tree = ast.parse((HERE / "app.py").read_text(encoding="utf-8"))
        functions = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        responder = next(n for n in functions if n.name == "respond")
        self.assertTrue(any(isinstance(d, ast.Call) and isinstance(d.func, ast.Attribute)
                            and d.func.attr == "GPU" for d in responder.decorator_list))
        interfaces = [n for n in ast.walk(tree) if isinstance(n, ast.Call)
                      and isinstance(n.func, ast.Attribute) and n.func.attr == "ChatInterface"]
        self.assertEqual(len(interfaces), 1)
        self.assertTrue(any(k.arg == "fn" and isinstance(k.value, ast.Name) and k.value.id == "respond"
                            for k in interfaces[0].keywords))


    def test_transformers5_tokenizer_contract_is_explicit_in_source(self):
        """Run on CI even if the heavyweight UI dependencies aren't installed."""
        tree = ast.parse((HERE / "app.py").read_text(encoding="utf-8"))
        calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
        template_calls = [n for n in calls if isinstance(n.func, ast.Attribute)
                          and n.func.attr == "apply_chat_template"]
        self.assertEqual(len(template_calls), 1)
        self.assertTrue(any(k.arg == "return_dict" and isinstance(k.value, ast.Constant)
                            and k.value.value is True for k in template_calls[0].keywords))
        model_generate = [n for n in calls if isinstance(n.func, ast.Attribute)
                          and n.func.attr == "generate"]
        self.assertEqual(len(model_generate), 1)
        self.assertTrue(any(k.arg is None for k in model_generate[0].keywords),
                        "Generation must unpack named model inputs, not pass BatchEncoding as one tensor")
        source = (HERE / "app.py").read_text(encoding="utf-8")
        self.assertIn('encoded["input_ids"]', source)


class ChatAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from importlib.util import find_spec
        if not find_spec("torch") or not find_spec("gradio"):
            raise unittest.SkipTest("Live UI dependencies are not installed on this CI runner; static handler tests run instead")
        cls.app = load_app()

    def test_chat_only_no_profile_editor_or_source_panel(self):
        config = self.app.demo.get_config_file()
        types_in_ui = [c["type"] for c in config["components"]]
        self.assertIn("chatbot", types_in_ui)
        self.assertIn("textbox", types_in_ui)
        self.assertNotIn("accordion", types_in_ui)
        self.assertEqual(types_in_ui.count("textbox"), 1)  # Only the chat composer.
        self.assertEqual(types_in_ui.count("chatbot"), 1)
        html = " ".join(str(c.get("props", {}).get("value", "")) for c in config["components"])
        self.assertNotIn("Character information", html)
        self.assertNotIn("Possible supporting text", html)

    def test_gpu_handler_is_registered_directly_with_gradio(self):
        self.assertTrue(self.app.respond._is_gpu)
        config = self.app.demo.get_config_file()
        names = [d.get("api_name") for d in config["dependencies"]]
        self.assertIn("chat", names)

    def test_transformers5_batchencoding_model_inputs(self):
        import torch
        model_inputs = self.app._inputs("Hello", [])
        self.assertEqual(set(model_inputs), {"input_ids", "attention_mask"})
        self.assertTrue(torch.equal(model_inputs["input_ids"], torch.tensor([[1, 2, 3]])))
        self.assertEqual(model_inputs["input_ids"].shape, model_inputs["attention_mask"].shape)

    def test_genuine_model_response_and_context(self):
        answer = self.app.respond("What is your name?", [])
        self.assertEqual(answer, "Hello! I'm Alex, an imaginary robot.")
        self.assertEqual(self.app.respond("Where do you live?", [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi"},
        ]), answer)

    def test_failures_have_reference_for_space_logs(self):
        with patch.object(self.app.MODEL, "generate", side_effect=RuntimeError("CUDA unavailable")):
            with self.assertLogs("ai_learning_lab.digital_twin", level="ERROR") as logs:
                result = self.app.respond("Hello", [])
            self.assertIn("Reference:", result)
            self.assertTrue(any("CUDA unavailable" in line for line in logs.output))
            self.assertNotIn("CUDA unavailable", result)  # Keep internal details out of public chat.


if __name__ == "__main__":
    unittest.main()
