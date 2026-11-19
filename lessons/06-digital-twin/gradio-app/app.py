"""AI Learning Lab · Real-model Digital Twin · Gradio + Hugging Face ZeroGPU.

Run locally: uv run app.py
Deploy from THIS folder: uv run gradio deploy (choose hardware zero-a10g)

There is no model API key: the model runs inside this Space on a shared GPU.
The model is loaded once at module import, as required for ZeroGPU.
"""
from __future__ import annotations

import os
from pathlib import Path

# Import spaces before torch: on ZeroGPU it installs CUDA offload hooks.
import spaces
import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from twin_core import (
    MAX_PROFILE_CHARS, MAX_QUESTION_CHARS, build_messages,
    candidate_source, friendly_error,
)

MODEL_ID = os.environ.get("MODEL_ID", "Qwen/Qwen3-1.7B")
PROFILE_FILE = Path(__file__).with_name("about-me.txt")
DEFAULT_PROFILE = PROFILE_FILE.read_text(encoding="utf-8")

# In ZeroGPU, spaces makes .to('cuda') work at startup without holding a GPU;
# the real GPU arrives only inside the @spaces.GPU function.
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


@spaces.GPU(duration=35)
def infer(messages: list[dict[str, str]]) -> str:
    """Use the actual pretrained model; never fabricate AI model output."""
    ids = TOKENIZER.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        enable_thinking=False,
        return_tensors="pt",
    ).to(DEVICE)
    # Avoid unbounded resource usage and very long histories.
    if ids.shape[-1] > 3000:
        ids = ids[:, -3000:]
    with torch.inference_mode():
        output = MODEL.generate(
            ids,
            max_new_tokens=160,
            do_sample=False,
            pad_token_id=TOKENIZER.eos_token_id,
            eos_token_id=TOKENIZER.eos_token_id,
        )
    generated = output[0, ids.shape[-1]:]
    reply = TOKENIZER.decode(generated, skip_special_tokens=True).strip()
    # If the model emitted a thinking block unexpectedly, don't show it to learners.
    if "</think>" in reply:
        reply = reply.split("</think>", 1)[-1].strip()
    return reply


def chat(question: str, history: list[dict] | None, profile: str):
    """Chat history is per Gradio session. Profile edits are not written to disk."""
    history = list(history or [])
    question = (question or "").strip()
    profile = (profile or "").strip()
    if not question:
        return history, "", ""
    question = question[:MAX_QUESTION_CHARS]
    if not profile:
        reply = "Please add a fictional profile first."
        source = ""
    else:
        try:
            reply = infer(build_messages(question, history, profile[:MAX_PROFILE_CHARS]))
            if not reply:
                reply = "I couldn't generate a reply. Try again."
            source = candidate_source(profile, question)
        except Exception as exc:
            reply, source = friendly_error(exc), ""
    history.extend([{"role": "user", "content": question}, {"role": "assistant", "content": reply}])
    return history, source, ""


CSS = """
.gradio-container {max-width: 1110px !important; margin: auto !important}
#profile-area {border:2px solid #b6915e; border-radius:14px; padding:5px}
#chat-area {border:2px solid #44b7aa; border-radius:14px; padding:5px}
#source-area {border:1px dashed #8586c5; border-radius:12px; padding:5px}
"""

with gr.Blocks(title="AI Learning Lab · My Digital Twin") as demo:
    gr.Markdown("# 🤖 My AI Digital Twin")
    gr.Markdown(
        "**Ask about your fictional character in English.** "
        "The AI reads your character's text and generates a new reply. "
        "It does not learn the text permanently. "
        "**Do not enter private personal information.** "
        "On Hugging Face ZeroGPU, shared queues and usage limits may apply."
    )
    with gr.Row():
        with gr.Column(scale=4, min_width=285):
            gr.Markdown("### ⚙️ Character information")
            profile = gr.Textbox(
                value=DEFAULT_PROFILE,
                label="Fictional facts",
                lines=13,
                max_lines=18,
                max_length=MAX_PROFILE_CHARS,
                elem_id="profile-area",
            )
            gr.Markdown(
                "Edit the facts, then ask a question. Changes apply to **this chat session only**; "
                "to publish different default facts, edit `about-me.txt` in your project."
            )
        with gr.Column(scale=6, min_width=310):
            gr.Markdown("### 🤖 AI reply")
            conversation = gr.Chatbot(value=[], height=375, elem_id="chat-area")
            question = gr.Textbox(
                label="✍️ Your question",
                placeholder="What is your name?",
                max_lines=3,
                max_length=MAX_QUESTION_CHARS,
            )
            with gr.Row():
                ask_button = gr.Button("Ask AI", variant="primary")
                reset_button = gr.Button("New conversation")
            gr.Markdown("### 📖 Possible supporting text")
            source = gr.Textbox(
                interactive=False, lines=3,
                label="From your character information",
                elem_id="source-area",
                placeholder="A possible related line will appear here after a question.",
            )
            gr.Markdown(
                "A matching line is **not proof** the reply is correct. "
                "Check the AI answer against the character's facts."
            )
    ask_button.click(chat, [question, conversation, profile], [conversation, source, question], show_progress="full")
    question.submit(chat, [question, conversation, profile], [conversation, source, question], show_progress="full")
    reset_button.click(lambda: ([], "", ""), outputs=[conversation, source, question])

if __name__ == "__main__":
    # The same app works locally and on Hugging Face Spaces.
    demo.queue(default_concurrency_limit=1, max_size=16).launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", "7860")),
        show_error=False,
        css=CSS,
    )
