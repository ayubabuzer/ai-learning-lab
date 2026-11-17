# AI Learning Lab | مختبر تعلم الذكاء الاصطناعي

**[English](README.md) · [العربية](README.ar.md) · [Website](https://ayubabuzer.github.io/ai-learning-lab/)**

Free, bilingual, hands-on AI education for all ages. No programming, advanced mathematics or paid API keys are required for the introductory lessons.

## Start with Lesson 01 — How Does AI Read Our Words?

**[Open the interactive lesson](lessons/01-how-ai-reads-words/)**

Type an English sentence or choose an English example, split it into readable pieces, click a piece to see its classroom ID, then change the text and compare the results. In Arabic mode, pupils see Arabic examples and a full right-to-left interface. The lesson includes three pupil missions and a 20-minute teacher activity.

**Important model explanation:** This first lightweight release is a **classroom simulation of tokenisation**, not a Qwen model or a genuine Qwen tokenizer. Its numeric IDs are assigned locally to pieces created by a simple Unicode splitting rule. They are classroom labels, not genuine model token IDs. It does not produce embeddings, trained predictions or LLM responses. We deliberately chose a small, instant and fully offline learning experience for ordinary school computers. The difference between classroom pieces and real model tokens is explained in the lesson.

## Learning path

| Lesson | Concept | Status |
|---|---|---|
| **[01 — How Does AI Read Our Words?](lessons/01-how-ai-reads-words/)** | Text pieces and local classroom IDs | **Lightweight version ready** |
| **[02 — How Does AI Connect Words?](lessons/02-word-embeddings/)** | Editable context vectors, numerical similarity and interactive word map | **Lightweight version ready** |
| 03 — How Does AI Predict What Comes Next? | Context and next-token generation | Planned |
| 04 — Does AI Really Remember? | Editable context, open-ended questions, temporary memory | Planned |
| 05 — How Does AI Find Information? | Keyword and semantic retrieval | Planned |
| 06 — Build Your Own AI Digital Twin | Gradio, `.txt` retrieval, grounded answers | Planned capstone |

## Lesson 02 — How Does AI Connect Words?

**[Open the interactive word playground](lessons/02-word-embeddings/)** · [Lesson guide](lessons/02-word-embeddings/README.md)

Enter any two words **present in the editable examples**, compare their numerical context vectors, see their shared-context similarity score and explore a calculated 2D word map. Add or change sentences and rebuild to see the result change. English mode uses English examples; Arabic mode uses Arabic examples and RTL layout. A short, **static and explicitly illustrative** king − man + woman ≈ queen example is included.

**Model honesty:** This is a real calculation from learner-editable sentences using word co-occurrence counts and cosine similarity. It is **not a pretrained embedding model or Qwen** and does not predict the next token. It works offline on ordinary school computers. Arbitrary typed words must be present in the example text; otherwise pupils are invited to add examples and rebuild.

## For teachers

[English classroom guide](TEACHERS.md) · [دليل المعلم بالعربية](TEACHERS.ar.md). Activities include practical tests, suggested questions and misconceptions to address.

## Project principles

- All learner-facing explanations and activities work in English and Arabic, with right-to-left Arabic layout.
- One lesson = one permanent folder. Updates change files in place, and Git preserves history.
- Never label teaching numbers, illustrative graphs or stored examples as live model output.
- Future real-model features must be measured and tested on normal school computers before release.
- Keep the current website design; update the homepage, both READMEs, teacher guides and [CHANGELOG.md](CHANGELOG.md) together.
- Prefer fictional examples rather than pupils' personal data.

## Contributing

You can review, adapt and improve the lessons in this repository, subject to its existing `LICENSE`.
