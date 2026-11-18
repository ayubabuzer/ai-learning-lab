# AI Learning Lab | مختبر تعلم الذكاء الاصطناعي

**[English](README.md) · [العربية](README.ar.md) · [Website](https://ayubabuzer.github.io/ai-learning-lab/)**

A free, bilingual, hands-on learning website for ordinary school computers. The six browser lessons work without a pupil account, API key, GPU or large-model download. Each lesson has **Previous / Next** buttons. Arabic mode has right-to-left layouts and its own example texts.

## Explore the six lessons

| Lesson | What students do | Important distinction |
|---|---|---|
| [01 · How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) | Type text, explore pieces and classroom number labels | Simplified text segmentation; labels are not real LLM token IDs |
| [02 · How Does AI Connect Words?](lessons/02-word-embeddings/) | Compare context vectors and visualise a word map; explore king–queen arithmetic | Calculated co-occurrences; overlapping map positions are visually separated **only** for readability; king/queen coordinates are invented |
| [03 · How Does AI Predict What Comes Next?](lessons/03-next-word-prediction/) | Teach a tiny predictor with sentences, then see real count-based next-word probabilities | Example-based pattern counts, not generation by a pretrained model |
| [04 · Does AI Really Remember?](lessons/04-ai-context-memory/) | Provide temporary context, ask questions, toggle the context and start a new session | Context in a request is not model training or permanent memory |
| [05 · How Can We Check an AI Answer?](lessons/05-ai-retrieval/) | Play Fact Detectives: decide if sources support, contradict, or do not address a claim | Evidence-reading exercise, not an automated truth checker |
| [06 · Build Your Own AI Digital Twin](lessons/06-digital-twin/) | Create a fictional assistant that replies from a knowledge file and shows evidence separately | Rules-based, extractive assistant, not a general generative chatbot |

**Learning path:** Text pieces → Word relationships → Pattern prediction → Context → Checking evidence → Your own source-based assistant.

Large real language models learn patterns from many examples of words and sentences found in books, websites, stories, articles and other text. Our small classroom algorithms teach selected ideas transparently. Results never claim to be pretrained-model output.

## Build and share your own Digital Twin

The homepage now includes a five-step deployment roadmap:

1. **Clone** the repository.
2. **Install** Python and the Gradio requirements.
3. **Personalise and run** the fictional knowledge file locally.
4. **Create** a Hugging Face account and check hosting eligibility.
5. **Deploy and share** a public link, if suitable hosting is available.

Follow the [full English Gradio guide](lessons/06-digital-twin/gradio-app/README.md) or [Arabic setup guide](lessons/06-digital-twin/gradio-app/README.ar.md). **Free Static Spaces cannot run Python Gradio**, and Gradio compute hosting may require a paid subscription or qualifying access. The project works locally even when hosting is unavailable. **Never upload private pupil information.**

## For teachers

[English teacher guide](TEACHERS.md) · [دليل المعلم](TEACHERS.ar.md). Each lesson also has an English and Arabic README.

## Publishing the website

Review the files in this release before uploading. Preserve your `LICENSE` and any unrelated work; do not delete unknown folders without checking links. Each lesson has exactly one canonical folder. Publish from the repository root with GitHub Pages and check the live lessons after uploading.

The website includes all six lessons and one optional `lessons/06-digital-twin/gradio-app/` project. No external inference service is used by the browser lessons.
