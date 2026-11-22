"""AI Learning Lab Digital Twin — chat-only Gradio app using Qwen on ZeroGPU.

The public interface is deliberately just a conversation. Character facts are
loaded from about-me.txt when the Space starts and are never shown as an editable
textbox to visitors. Inference uses the *same* @spaces.GPU-decorated handler that
Gradio registers, which ZeroGPU needs to allocate a GPU for each request.
"""
from __future__ import annotations

import logging
import os
import uuid
from pathlib import Path

# ZeroGPU must patch PyTorch before anything touches CUDA.
import spaces
import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from twin_core import MAX_PROFILE_CHARS, MAX_QUESTION_CHARS, build_messages, friendly_error

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("ai_learning_lab.digital_twin")

MODEL_ID = os.environ.get("MODEL_ID", "Qwen/Qwen3-1.7B")
PROFILE = Path(__file__).with_name("about-me.txt").read_text(encoding="utf-8").strip()
if not PROFILE:
    raise RuntimeError("about-me.txt is empty. Add fictional character facts before deploying.")

# On ZeroGPU, spaces emulates CUDA at module scope and handles GPU offloading.
# Do not move the model to CUDA inside the per-message handler.
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.bfloat16 if DEVICE == "cuda" else torch.float32
TOKENIZER = AutoTokenizer.from_pretrained(MODEL_ID)
MODEL = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=DTYPE,
    low_cpu_mem_usage=True,
    attn_implementation="sdpa",
).to(DEVICE)
MODEL.eval()
logger.info("Model initialised on %s", DEVICE)

MAX_CONTEXT_TOKENS = 3000


def _inputs(message: str, history: list[dict]) -> dict[str, torch.Tensor]:
    """Build model inputs; trim old messages while preserving profile and question.

    Transformers 5 returns a BatchEncoding (a mapping with ``input_ids`` and
    ``attention_mask``), NOT a tensor, from ``apply_chat_template``. Access the
    tensor by key and pass the complete mapping to ``generate``.
    """
    messages = build_messages(message, history, PROFILE[:MAX_PROFILE_CHARS])
    while True:
        encoded = TOKENIZER.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            enable_thinking=False,
            return_tensors="pt",
            return_dict=True,
        )
        input_ids = encoded["input_ids"]
        if input_ids.shape[-1] <= MAX_CONTEXT_TOKENS:
            # BatchEncoding.to() returns the mapping with all tensors moved;
            # using a normal dict also makes the model's inputs explicit.
            return {key: value.to(DEVICE) for key, value in encoded.items()
                    if isinstance(value, torch.Tensor)}
        if len(messages) <= 2:
            raise ValueError("The character profile is too long for this chat. Shorten about-me.txt.")
        # Keep the system message and the latest user question intact.
        messages.pop(1)


@spaces.GPU(duration=35)
def respond(message: str, history: list[dict] | None) -> str:
    """Gradio's registered ChatInterface handler — also ZeroGPU's GPU entrypoint."""
    question = (message or "").strip()
    if not question:
        return "Please enter a question."
    question = question[:MAX_QUESTION_CHARS]
    try:
        inputs = _inputs(question, list(history or []))
        with torch.inference_mode():
            output = MODEL.generate(
                **inputs,
                max_new_tokens=160,
                do_sample=False,
                pad_token_id=TOKENIZER.eos_token_id,
                eos_token_id=TOKENIZER.eos_token_id,
            )
        generated = output[0, inputs["input_ids"].shape[-1]:]
        answer = TOKENIZER.decode(generated, skip_special_tokens=True).strip()
        if "</think>" in answer:
            answer = answer.split("</think>", 1)[-1].strip()
        return answer or "I couldn't find a reply to that question. Please try rephrasing it."
    except Exception as exc:
        # Previous versions hid every failure behind the same message. The
        # reference makes the actual traceback discoverable in Space Logs.
        reference = uuid.uuid4().hex[:8]
        logger.exception("Chat inference failed (reference %s)", reference)
        return f"{friendly_error(exc)}  (Reference: {reference}; check Space Logs.)"


CSS = """
:root { color-scheme: light dark; }
.gradio-container { max-width: 920px !important; margin-inline: auto !important; padding: 18px 22px !important; }
#twin-brand { display:flex; align-items:center; gap:13px; padding: 4px 4px 18px; }
#twin-brand .brand-mark { display:grid; place-items:center; width:42px; height:42px; flex-shrink:0;
    border-radius:15px; color:white; background:linear-gradient(135deg,#6257db,#9b69ef); font-size:22px;
    box-shadow:0 7px 20px rgba(99,87,219,.23); }
#twin-brand .brand-title {font-size:18px; font-weight:730; line-height:1.3; letter-spacing:-.35px;}
#twin-brand .brand-subtitle {font-size:12px; opacity:.68; margin-top:2px;}
#twin-brand .brand-status {margin-left:auto; font-size:12px; opacity:.74; white-space:nowrap;}
#twin-brand .brand-status::before {content:'•'; color:#29ac78; font-size:20px; vertical-align:-2px; margin-right:5px;}
#twin-chat {border:1px solid var(--border-color-primary) !important; border-radius:22px !important;
    overflow:hidden; box-shadow:0 5px 28px rgba(30,35,70,.05);}
#twin-input {border-radius:15px !important;}
#twin-chat .message {line-height:1.55;}
#twin-chat .message.user {border-radius:17px 17px 5px 17px !important;}
#twin-chat .message.bot {border-radius:17px 17px 17px 5px !important;}
#twin-chat .bubble-wrap {max-width:88%;}
#twin-footer {text-align:center; opacity:.62; font-size:11px; padding-top:8px;}
@media (max-width:640px) {
  .gradio-container {padding:10px !important;}
  #twin-brand {gap:10px; padding:5px 2px 12px;}
  #twin-brand .brand-mark {width:36px; height:36px; border-radius:12px; font-size:18px;}
  #twin-brand .brand-title {font-size:16px;}
  #twin-brand .brand-status {font-size:10px;}
  #twin-chat {border-radius:16px !important;}
}
"""

with gr.Blocks(
    title="Digital Twin | AI Learning Lab",
    fill_height=True,
) as demo:
    gr.HTML(
        '<header id="twin-brand" aria-label="Digital Twin">'
        '<div class="brand-mark" aria-hidden="true">✦</div>'
        '<div><div class="brand-title">Digital Twin</div>'
        '<div class="brand-subtitle">AI Learning Lab · Powered by Qwen</div></div>'
        '<span class="brand-status">AI chat</span></header>'
    )
    chatbot = gr.Chatbot(
        height=530,
        show_label=False,
        elem_id="twin-chat",
        layout="bubble",
        allow_tags=False,
        placeholder=(
            '<div style="text-align:center;padding:30px 12px">'
            '<div style="font-size:30px;margin-bottom:8px">✦</div>'
            '<strong style="font-size:19px">Say hello to your Digital Twin</strong>'
            '<p style="opacity:.68;margin-top:9px">Ask about the fictional character and explore its story.</p>'
            '</div>'
        ),
    )
    gr.ChatInterface(
        fn=respond,
        chatbot=chatbot,
        textbox=gr.Textbox(
            placeholder="Message your Digital Twin…",
            show_label=False,
            max_lines=4,
            max_length=MAX_QUESTION_CHARS,
            elem_id="twin-input",
        ),
        examples=["What is your name?", "Where do you live?", "What do you enjoy?"],
        run_examples_on_click=False,
        cache_examples=False,
        submit_btn=True,
        stop_btn=True,
        show_progress="minimal",
        fill_width=True,
        fill_height=True,
        api_name="chat",
    )
    gr.HTML('<div id="twin-footer">AI can make mistakes · Fictional character demo · Do not share private information</div>')

if __name__ == "__main__":
    demo.queue(default_concurrency_limit=1, max_size=16).launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", "7860")),
        show_error=False,  # Internal tracebacks belong in Space Logs, not in the public UI.
        theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="slate"),
        css=CSS,
    )
