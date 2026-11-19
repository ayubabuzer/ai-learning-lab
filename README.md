# AI Learning Lab | مختبر تعلم الذكاء الاصطناعي

**[English](README.md) · [العربية](README.ar.md) · [Website](https://ayubabuzer.github.io/ai-learning-lab/)**

A free, bilingual, hands-on learning website for ordinary school computers. Lessons 01–05 work in a normal browser without a learner account, API key, GPU or large-model download. Lesson 06 guides learners to **one real generative AI app** using uv, Gradio and ZeroGPU. The lesson pages have **Previous / Next** navigation. Lessons 01–05 have Arabic RTL modes and language-specific examples. Lesson 06 and its chatbot are English-only.

## Explore the six lessons

| Lesson | What students do | Important distinction |
|---|---|---|
| [01 · How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) | Type text, explore pieces and classroom number labels | Simplified text segmentation; labels are not real LLM token IDs |
| [02 · How Does AI Connect Words?](lessons/02-word-embeddings/) | Compare context vectors and visualise a word map; explore king–queen arithmetic | Calculated co-occurrences; overlapping map positions are visually separated **only** for readability; king/queen coordinates are invented |
| [03 · How Does AI Predict What Comes Next?](lessons/03-next-word-prediction/) | Teach a tiny predictor with sentences, then see real count-based next-word probabilities | Example-based pattern counts, not generation by a pretrained model |
| [04 · Does AI Really Remember?](lessons/04-ai-context-memory/) | Provide temporary context, ask questions, toggle the context and start a new session | Context in a request is not model training or permanent memory |
| [05 · How Does AI Know Which Words to Look At?](lessons/05-ai-retrieval/) | Type English or Arabic text; click words, follow attention links and see percentages change | Real calculations from a **fixed classroom attention algorithm**, not pretrained model attention |
| [06 · Build Your Own AI Digital Twin](lessons/06-digital-twin/) | Follow the uv + Gradio guide, personalise a fictional knowledge file and publish one real-model AI chatbot | Real pretrained language model on eligible Hugging Face ZeroGPU hosting; no paid inference API |

**Learning path:** Text pieces → Word relationships → Pattern prediction → Context → Attention → Build and publish a real-model Digital Twin.

Large real language models learn patterns from many examples of words and sentences found in books, websites, stories, articles and other text. Our small classroom algorithms teach selected ideas transparently. Results never claim to be pretrained-model output.

## Build and share your own Digital Twin

The homepage and Lesson 06 now include **Windows / Mac tabs (Windows by default)** for Ed Donner's uv + Gradio workflow, adapted to an open model on Hugging Face ZeroGPU. The on-page course guide explicitly covers Git, Python 3.12, uv, cloning, editing, login, deployment and sharing:

1. **Check/install Git** (Windows: winget; Mac: Command Line Tools).
2. **Install uv** (Windows: winget; Mac: Homebrew or official installer), then **install Python 3.12** using `uv python install 3.12`.
3. **Clone the full repository** using Git, enter `lessons/06-digital-twin/gradio-app` and edit the fictional `about-me.txt`.
4. **Optional local test:** `uv run app.py` (downloads a large model).
5. **Create and verify a Hugging Face account**, then run `uvx hf auth login`.
6. **Deploy:** `uv run gradio deploy`; choose **`zero-a10g`**, not `cpu-basic`, when hardware choice is offered. Verify the Space hardware in Settings and share the tested link.

Follow the [complete English deployment guide](lessons/06-digital-twin/gradio-app/README.md) (English-only final project). **Free hosting is conditional:** a personal account must meet ZeroGPU eligibility rules (verified email, older than 30 days, in good standing; maximum two Spaces). Free shared GPUs have queues and daily quotas. No paid model API key is needed. **Never publish private personal information.**

## For teachers

[English teacher guide](TEACHERS.md) · [دليل المعلم](TEACHERS.ar.md). Lessons 01–05 have English and Arabic READMEs; Lesson 06 is English only.

## Publishing the website

Review the files in this release before uploading. Preserve your `LICENSE` and any unrelated work; do not delete unknown folders without checking links. Each lesson has exactly one canonical folder. Publish from the repository root with GitHub Pages and check the live lessons after uploading.

The first five browser lessons remain lightweight. Lesson 06 is the guide to **one real AI Digital Twin** at `lessons/06-digital-twin/gradio-app/`, running a pretrained model directly on ZeroGPU after deployment. No external inference service is used by Lessons 01–05.

### Latest learning improvements

- **Lesson 01:** A one-click **Change punctuation** experiment automatically shows what changes in the classroom text pieces and IDs.
- **Lesson 05:** An interactive **small/big** word-connection comparison shows computed classroom weights for *it → ball* and *it → bag*. Teachers may input other sentences and get recalculated numerical patterns; they are not pretrained attention values or guaranteed meaning.
