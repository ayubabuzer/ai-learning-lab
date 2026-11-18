"""AI Learning Lab · A small, source-based educational digital twin.

This is a deterministic text-matching and extraction app, NOT a pretrained LLM.
It deliberately does not invent responses when evidence cannot be located.
Never upload real children's personal details to a public Space.
"""
from pathlib import Path
import re
import unicodedata
import gradio as gr

BASE = Path(__file__).resolve().parent
DEFAULT_EN = (BASE / "about-me.txt").read_text(encoding="utf-8")
DEFAULT_AR = """اسمي نور وأنا روبوت خيالي لطيف.
أسكن على كوكب خيالي اسمه لونا.
طعامي المفضل هو المعكرونة على شكل نجوم.
أحب رسم صور للكواكب.
لدي تنين أليف اسمه برق.
لوني المفضل هو الفيروزي."""
EN_STOP = set("what where when why how which who is are was were the a an my your you i me does do did have has about of in for to can please tell".split())
AR_STOP = set("ما ماذا من اين متى كيف لماذا هو هي هل في من عن على اسم اسمي اسمك".split())


def normalise(word: str) -> str:
    word = unicodedata.normalize("NFKC", word.casefold())
    word = re.sub(r"[\u064b-\u065f\u0670]", "", word)
    return re.sub(r"[إأآ]", "ا", word).replace("ى", "ي")


def words(text: str, language: str) -> set[str]:
    stop = EN_STOP if language == "English" else AR_STOP
    tokens = re.findall(r"[^\W_]+", text, flags=re.UNICODE)
    return {normalise(t) for t in tokens if len(t) > 1 and normalise(t) not in stop}


def find_evidence(question: str, knowledge: str, language: str):
    """Return a supporting line only when question words overlap sufficiently."""
    query = words(question, language)
    if not query:
        return None
    hits = []
    for row, raw in enumerate(knowledge.splitlines(), 1):
        sentence = raw.strip()
        if not sentence:
            continue
        shared = len(query & words(sentence, language))
        hits.append((shared, -row, row, sentence))
    if not hits:
        return None
    shared, _, row, sentence = max(hits)
    needed = 2 if len(query) >= 2 else 1
    return (row, sentence) if shared >= needed else None


def direct_answer(question: str, knowledge: str, language: str):
    """Return answer, line number, source text. No unrestricted generation."""
    lines = [(row, line.strip()) for row, line in enumerate(knowledge.splitlines(), 1) if line.strip()]
    q = normalise(question)
    if language == "English" and re.search(r"\b(name|called)\b", q):
        for row, line in lines:
            m = re.search(r"\bmy name is\s+([^\s,.!?]+)", line, re.I)
            if m:
                return f"My name is {m.group(1)}.", row, line
        return None
    if language == "العربية" and ("اسم" in q or "من انت" in q):
        for row, line in lines:
            m = re.search(r"اسمي\s+([^\s،.!؟]+)", line)
            if m:
                return f"اسمي {m.group(1)}.", row, line
        return None
    if language == "English" and re.search(r"\b(age|how old)\b", q):
        for row, line in lines:
            if re.search(r"\b\d+\s+years? old\b", line, re.I):
                return line, row, line
        return None
    if language == "العربية" and ("عمرك" in q or "عمر" in q):
        for row, line in lines:
            if re.search(r"(?:عمري|عمره|عمرها)\s*\d+", line):
                return line, row, line
        return None
    found = find_evidence(question, knowledge, language)
    if found:
        row, line = found
        return line, row, line
    return None


def answer_question(question, knowledge, language):
    """Shown response is separate from the exact supporting source."""
    arabic = language == "العربية"
    if not (question or "").strip():
        return ("اكتب سؤالاً أولاً." if arabic else "Write a question first.", "—")
    if not (knowledge or "").strip():
        return ("أضف معلومات خيالية أولاً." if arabic else "Add some fictional facts first.", "—")
    result = direct_answer(question, knowledge, language)
    if result is None:
        return ("لا أعرف من المعلومات المتاحة." if arabic else "I don't know from the supplied information.", "—")
    answer, line_number, source = result
    reference = f"السطر {line_number}: {source}" if arabic else f"Line {line_number}: {source}"
    return answer, reference


def load_text(filepath):
    if not filepath:
        return DEFAULT_EN
    target = Path(filepath)
    if target.suffix.lower() != ".txt" or target.stat().st_size > 250_000:
        raise gr.Error("Please use a UTF-8 .txt file smaller than 250 KB.")
    try:
        return target.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise gr.Error("Please save the text file using UTF-8 encoding.")


def example_for_language(language):
    return DEFAULT_AR if language == "العربية" else DEFAULT_EN


with gr.Blocks(title="AI Learning Lab — Fictional Digital Twin") as demo:
    gr.Markdown("# 🤖 My Digital Twin · توأمي الرقمي\nLearn how a question-answering assistant uses a knowledge file.")
    gr.Markdown("**Classroom project:** This is rule-based retrieval and text extraction, **not a generative language model**. Use fictional information only. Public Space source files can be read by others.")
    language = gr.Radio(["English", "العربية"], value="English", label="Language / اللغة")
    with gr.Row():
        with gr.Column():
            gr.Markdown("### ⚙️ Knowledge & settings · المعلومات والإعدادات")
            knowledge = gr.Textbox(value=DEFAULT_EN, label="Fictional knowledge (one fact per line) / معلومات خيالية", lines=10)
            file_input = gr.File(label="Load a UTF-8 .txt file / تحميل ملف", file_types=[".txt"], type="filepath")
            example_button = gr.Button("Load example for selected language / تحميل مثال باللغة المختارة")
        with gr.Column():
            gr.Markdown("### ✍️ Ask something · اطرح سؤالاً")
            question = gr.Textbox(label="Your question / سؤالك", lines=2, placeholder="What is your name? / ما اسمك؟")
            ask_button = gr.Button("🤖 Ask my digital twin / اسأل توأمي الرقمي", variant="primary")
            gr.Markdown("### 🤖 Twin's answer · إجابة التوأم")
            response = gr.Textbox(label="Answer / الإجابة", interactive=False, lines=3, value="")
            gr.Markdown("### 📖 Where it found the information · مصدر المعلومات")
            citation = gr.Textbox(label="Evidence / الدليل", interactive=False, lines=3, value="")
    file_input.change(fn=load_text, inputs=[file_input], outputs=[knowledge])
    example_button.click(fn=example_for_language, inputs=[language], outputs=[knowledge])
    ask_button.click(fn=answer_question, inputs=[question, knowledge, language], outputs=[response, citation])

if __name__ == "__main__":
    demo.launch()
