# AI Learning Lab | مختبر تعلم الذكاء الاصطناعي

**[English](README.md) · [العربية](README.ar.md) · [Website](https://ayubabuzer.github.io/ai-learning-lab/)**

Free, bilingual, beginner-friendly AI education with working interactive experiments. The current lightweight mode is designed for ordinary school computers: **no pupil account, API key, large AI download or inference server**.

## Learning path

| Lesson | Playground | Technology honesty |
|---|---|---|
| [01 — How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) | Text pieces and classroom IDs | Simplified segmentation; not a Qwen tokenizer |
| [02 — How Does AI Connect Words?](lessons/02-word-embeddings/) | Editable word-context vectors, similarity map and illustrative king/queen axes | Word co-occurrence counts; invented axes numbers clearly labelled |
| [03 — How Does AI Predict What Comes Next?](lessons/03-next-word-prediction/) | Editable training examples, calculated probabilities, source examples | Small n-gram word-count model; not LLM generation |
| [04 — Does AI Really Remember?](lessons/04-ai-context-memory/) | Context on/off, any question, visible input, fresh session | Mini context reader, not model training or permanent memory |
| [05 — How Does AI Find Information?](lessons/05-ai-retrieval/) | Keyword search versus concept-aware vector matching | Lightweight word-count vectors + small fixed synonym groups; not pretrained embeddings |
| [06 — Build Your Own AI Digital Twin](lessons/06-digital-twin/) | Editable/uploadable fictional `.txt` knowledge, evidence and abstention | Extractive retrieval; optional Python/Gradio starter, not a generative LLM |

## How the lessons fit together

**Words and IDs → Context vectors → Prediction patterns → Temporary context → Retrieval → Source-based assistant.**

Real LLMs learn from huge collections of books, websites, articles, stories and other text. Our lightweight classroom activities provide transparent experiments for understanding *selected ideas*; they do not reproduce the capabilities of pretrained AI. Pupils can freely edit the examples and see the actual calculations, but the miniature algorithms have limited vocabulary and understanding.

The four new lessons are **instant, offline-friendly browser demonstrations**; none claims to use a pretrained Qwen model. Lesson 02 uses computed co-occurrence vectors; Lesson 03 uses n-gram counts; Lesson 04 retrieves matching sentences from temporary context; Lesson 05 compares literal keywords with small-dictionary concept vectors; Lesson 06 builds a source-quoting digital twin plus an optional Gradio starter.

## Teachers

[Teacher guide (English)](TEACHERS.md) · [دليل المعلم](TEACHERS.ar.md). Each lesson has an additional bilingual guide in its own folder.

## Website and deployment

1. Keep the repository's existing `LICENSE` and any unrelated files.
2. Extract this release over the repository **without deleting existing folders**. It contains one canonical folder for each lesson.
3. Check the changes, especially README links and the existing Lesson 01 files, then commit.
4. Enable GitHub Pages for the root folder and check the deployed lesson links after Pages finishes publishing.

The separate [Gradio capstone project](lessons/06-digital-twin/gradio-app/README.md) requires Python and Gradio to run on a developer/teacher machine. Hosting on Hugging Face Spaces is optional, not required for pupils.

## Principles

- English mode suggests only English examples; Arabic mode suggests only Arabic examples and has RTL layout.
- Results described as model predictions are only the numerical results from that *specified* classroom algorithm.
- Never label illustrative king/queen coordinates or small vectors as pretrained Qwen embeddings.
- No real pupil personal information is needed. Use fictional examples for the digital twin.
- Each lesson lives in **one** directory and gets updated in place. The root website, documents and changelog should remain consistent.
