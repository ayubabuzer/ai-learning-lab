"""AI Learning Lab Lesson 06 — source-based, EXTRACTIVE digital twin.

No generative language model; quotes a matching line or refuses. For education.
All examples fictional. Never publish a child's real personal information.
"""
from pathlib import Path
import re
import unicodedata
import gradio as gr

HERE = Path(__file__).resolve().parent
DEFAULT = (HERE / "about-me.txt").read_text(encoding="utf-8")
EN_STOP = set("what where when why how which who is are was were the a an my your you i me does do did have has about of in for to can please tell".split())
AR_STOP = set("ما ماذا من اين متى كيف لماذا هو هي هل في من عن على اسم".split())


def normalise(word):
    word = unicodedata.normalize("NFKC", word.lower())
    word = re.sub("[\u064b-\u065f\u0670]", "", word)
    word = re.sub("[إأآ]", "ا", word).replace("ى", "ي")
    return word


def words(text, language):
    terms = [normalise(w) for w in re.findall(r"[^\W_]+", text, re.UNICODE)]
    stop = {normalise(x) for x in (AR_STOP if language == "العربية" else EN_STOP)}
    return set(w for w in terms if len(w) > 1 and w not in stop)


def retrieve(question, knowledge, language):
    qterms = words(question, language)
    if not qterms:
        return None
    candidates = []
    for idx, raw in enumerate(knowledge.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        matches = len(qterms & words(line, language))
        candidates.append((matches, -idx, idx, line))
    if not candidates:
        return None
    matches, _, idx, line = max(candidates)
    minimum = 2 if len(qterms) >= 2 else 1
    return (idx, line) if matches >= minimum else None


def answer_question(question, knowledge, language):
    arabic = language == "العربية"
    if not question.strip():
        return ("اكتب سؤالاً أولاً." if arabic else "Write a question first.", "—")
    result = retrieve(question, knowledge, language)
    if result is None:
        return ("لا أعرف من المعلومات المتاحة." if arabic else
                "I don't know from the information supplied.", "—")
    idx, text = result
    intro = "هذه معلومة مرتبطة من ملف المعرفة:" if arabic else "Relevant information from the knowledge file:"
    source = f"السطر {idx}: {text}" if arabic else f"Line {idx}: {text}"
    return f"{intro}\n“{text}”", source


def load_text(file_path):
    if not file_path:
        return DEFAULT
    path = Path(file_path)
    if path.suffix.lower() != ".txt" or path.stat().st_size > 250_000:
        raise gr.Error("Use a .txt file smaller than 250 KB.")
    return path.read_text(encoding="utf-8")

with gr.Blocks(title="AI Learning Lab — Fictional Digital Twin") as demo:
    gr.Markdown("# AI Learning Lab · Lesson 06\n### Fictional, evidence-first digital twin / توأم رقمي خيالي مع مصادر")
    gr.Markdown("This is **retrieval**, not a generative Qwen model. Use fictional information only. If hosted publicly, user text is processed on the host.")
    language = gr.Radio(["English", "العربية"], value="English", label="Language / اللغة")
    with gr.Row():
        with gr.Column():
            knowledge = gr.Textbox(value=DEFAULT, label="Knowledge / المعلومات", lines=12)
            file_input = gr.File(label="Load a .txt file / تحميل ملف", file_types=[".txt"], type="filepath")
        with gr.Column():
            question = gr.Textbox(label="Question / السؤال", lines=2)
            ask_button = gr.Button("Find evidence / ابحث عن الدليل", variant="primary")
            response = gr.Textbox(label="Answer / الإجابة", lines=5, interactive=False)
            citation = gr.Textbox(label="Source / المصدر", lines=3, interactive=False)
    file_input.change(fn=load_text, inputs=file_input, outputs=knowledge)
    ask_button.click(fn=answer_question, inputs=[question, knowledge, language], outputs=[response, citation])

if __name__ == "__main__":
    demo.launch()
