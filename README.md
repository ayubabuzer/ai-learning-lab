# AI Learning Lab | مختبر تعلم الذكاء الاصطناعي

**[English](README.md) · [العربية](README.ar.md) · [Visit website](https://ayubabuzer.github.io/ai-learning-lab/)**

**Learn how AI works by playing with real experiments — no advanced maths or programming needed.**

AI Learning Lab is a free, open-source, bilingual learning journey for learners of all ages. Every lesson includes a pupil playground, a simple explanation, hands-on challenges and a teacher-led activity. The site uses the existing dark visual design and works on GitHub Pages.

## Start with Lesson 01

### [How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) — Published

**What happens to a sentence before an AI model can process it?** Learners type any English or Arabic text, run the **real Qwen3 0.6B tokenizer**, click colourful tokens to inspect their **actual numerical IDs**, and compare the result with a clearly labelled offline UTF‑8 byte tokenizer. They experiment with emojis, punctuation, different languages and spelling, and explain surprises.

Real model-tokeniser mode requires an internet connection initially for free tokenizer files. Offline byte mode is not a pretrained model vocabulary. No text-generation model runs in this lesson. Token IDs are not embeddings; this is introduced in Lesson 02.

## Learning path

| Lesson | Discovery | Status |
|---|---|---|
| [01 — How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) | Tokens, token IDs and text puzzles | **Published** |
| 02 — How Does AI Connect Words? | Enter words, view pretrained embeddings and compare similarity | Planned |
| 03 — How Does AI Predict What Comes Next? | Change context; see real next-token predictions and generation | Planned |
| 04 — Does AI Really Remember? | Write any text context and question; compare with/without context | Planned |
| 05 — How Does AI Find Information? | Keyword search versus semantic retrieval from text | Planned |
| 06 — Build Your Own AI Digital Twin | Grounded retrieval chatbot with Gradio and optional Hugging Face publishing | Planned capstone |

## For teachers

Read [TEACHERS.md](TEACHERS.md) for a projector-friendly 25-minute classroom game, group challenges, preparation and key misconceptions. [دليل المعلم بالعربية](TEACHERS.ar.md). The lesson itself also contains a collapsible guide.

## Principles

- No paid APIs, subscription or account required to use the browser lesson.
- The site is bilingual, with meaningful Arabic examples and RTL layout.
- Distinguish **real tokenizer/model results** from educational explanations.
- Each lesson: predict → run → change → explain → challenge.
- Avoid collecting pupil personal information. Use invented examples by default.
- The final Gradio project will run locally at no cost; Hugging Face hosting availability and requirements may change, so hosting is optional rather than guaranteed.

## Existing experiments

Earlier experimental pages are retained as archives for compatibility: [Inside AI overview](lessons/01-inside-ai/), [Tokens prototype](lessons/01-tokens/), and [Next-word predictor](lessons/01-next-word/). The historical folder names do not represent the current curriculum. These are **not** part of the new six-lesson published sequence.

## Contribute and license

Report ideas and issues in the repository. Respect the existing repository licence. Changes to lessons should update this file, [README.ar.md](README.ar.md), homepage, teacher guidance and [CHANGELOG.md](CHANGELOG.md) together.

## Why Qwen tokenisation?

Lesson 01 uses the tokenizer files of the actual Qwen3 0.6B model, but **does not load Qwen model weights or generate answers**. These are two separate stages: tokenisation is lightweight; language generation is introduced in Lesson 03. A small first-time download of tokenizer files is needed. The classroom byte mode remains available without model downloads.


**Arabic display fix:** Real Qwen byte-level BPE token IDs are preserved. Adjacent token IDs may be grouped into readable Unicode spans, so a displayed piece is not necessarily a single token. The inspector shows every original ID. Arabic layouts use RTL, and byte mode decodes valid UTF-8 sequences for display.
