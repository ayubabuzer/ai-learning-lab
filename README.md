# AI Learning Lab | مختبر تعلم الذكاء الاصطناعي

**[English](README.md) · [العربية](README.ar.md) · [Website](https://ayubabuzer.github.io/ai-learning-lab/)**

A free, bilingual, hands-on learning website for ordinary school computers. Lessons 01–05 work in a normal browser without a pupil account, API key, GPU or large-model download. Lesson 06 guides pupils to **one real generative AI app** using uv, Gradio and ZeroGPU. The lesson pages have **Previous / Next** navigation. Arabic mode has right-to-left layouts and its own example texts.

## Explore the six lessons

| Lesson | What students do | Important distinction |
|---|---|---|
| [01 · How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) | Type text, explore pieces and classroom number labels | Simplified text segmentation; labels are not real LLM token IDs |
| [02 · How Does AI Connect Words?](lessons/02-word-embeddings/) | Compare context vectors and visualise a word map; explore king–queen arithmetic | Calculated co-occurrences; overlapping map positions are visually separated **only** for readability; king/queen coordinates are invented |
| [03 · How Does AI Predict What Comes Next?](lessons/03-next-word-prediction/) | Teach a tiny predictor with sentences, then see real count-based next-word probabilities | Example-based pattern counts, not generation by a pretrained model |
| [04 · Does AI Really Remember?](lessons/04-ai-context-memory/) | Provide temporary context, ask questions, toggle the context and start a new session | Context in a request is not model training or permanent memory |
| [05 · Can We Always Trust an AI Answer?](lessons/05-ai-retrieval/) | Play Fact Detectives: decide if sources support, contradict, or do not address a claim | Evidence-reading exercise, not an automated truth checker |
| [06 · Build Your Own AI Digital Twin](lessons/06-digital-twin/) | Follow the uv + Gradio guide, personalise a fictional knowledge file and publish one real-model AI chatbot | Real pretrained language model on eligible Hugging Face ZeroGPU hosting; no paid inference API |

**Learning path:** Text pieces → Word relationships → Pattern prediction → Context → Checking evidence → Build and publish a real-model Digital Twin.

Large real language models learn patterns from many examples of words and sentences found in books, websites, stories, articles and other text. Our small classroom algorithms teach selected ideas transparently. Results never claim to be pretrained-model output.

## Build and share your own Digital Twin

The homepage and Lesson 06 now explain **Ed Donner's uv + Gradio deployment workflow**, adapted to an open language model on Hugging Face ZeroGPU:

1. **Clone** the repository and open `lessons/06-digital-twin/gradio-app`.
2. **Install uv** and edit the fictional `about-me.txt` profile.
3. **Run locally:** `uv run app.py` (downloads the model; a capable computer is needed).
4. **Sign into Hugging Face:** `uvx hf auth login`, then `uvx hf auth whoami`.
5. **Deploy:** `uv run gradio deploy` and select **`zero-a10g`**, not the old `cpu-basic` default.

Follow the [complete English deployment guide](lessons/06-digital-twin/gradio-app/README.md) or [Arabic guide](lessons/06-digital-twin/gradio-app/README.ar.md). **Free hosting is conditional:** a personal account must meet ZeroGPU eligibility rules (verified email, older than 30 days, in good standing; maximum two Spaces). Free shared GPUs have queues and daily quotas. No paid model API key is needed. **Never publish real pupil personal information.**

## For teachers

[English teacher guide](TEACHERS.md) · [دليل المعلم](TEACHERS.ar.md). Each lesson also has an English and Arabic README.

## Publishing the website

Review the files in this release before uploading. Preserve your `LICENSE` and any unrelated work; do not delete unknown folders without checking links. Each lesson has exactly one canonical folder. Publish from the repository root with GitHub Pages and check the live lessons after uploading.

The first five browser lessons remain lightweight. Lesson 06 is the guide to **one real AI Digital Twin** at `lessons/06-digital-twin/gradio-app/`, running a pretrained model directly on ZeroGPU after deployment. No external inference service is used by Lessons 01–05.
