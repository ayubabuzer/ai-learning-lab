# AI Learning Lab

**[English](README.md) · [Arabic](README.ar.md) · [Website](https://ayubabuzer.github.io/ai-learning-lab/)**

AI Learning Lab is a free, open-source learning website for people of all ages. It uses everyday language first and introduces technical words only after the idea makes sense. Lessons 01–05 are bilingual (English/Arabic), browser-based, and require no learner account, model download or API token. Lesson 06 is an English-only real-model Digital Twin project.

## Six connected lessons

| Lesson | Simple question | What is real and what is illustrative? |
|---|---|---|
| [01 · How Does AI Read Our Words?](lessons/01-how-ai-reads-words/) | How does a message become numbers? | Illustrative text pieces, token IDs and number patterns, followed by a conceptual word map |
| [02 · How Does AI Connect Words?](lessons/02-word-embeddings/) | How can numbers relate words? | Interactive example map with curated word comparisons; a bank/river-versus-money context experiment and ball/bag illustrations, **not** measured pretrained embeddings |
| [03 · How Does AI Learn to Predict?](lessons/03-next-word-prediction/) | How do examples change predictions? | A genuine count-based mini predictor: **teach → test → change → teach again**, a brief explanation of how large models learn from text, then an optional misleading-data challenge |
| [04 · How Does AI Remember?](lessons/04-ai-context-memory/) | Where does its memory come from? | Guided chat: tap or drag prepared fact cards into context, ask a supported question, clear the context and ask again; **not a live LLM** |
| [05 · How Does AI Use Tools and Work Towards a Goal?](lessons/05-ai-retrieval/) | How do tools and goal-seeking agents work? | Offline tool-call activity trace with real arithmetic and two replayable agent scenarios; illustrative external data |
| [06 · Build Your Own Digital Twin](lessons/06-digital-twin/) | How can I create and share a real chatbot? | Real Qwen-based Gradio app (English-only), with fictional-profile context and optional Hugging Face ZeroGPU deployment |

Each lesson follows **short explanation → meaningful experiment or illustrated example → change something → discovery → connection to the next lesson**. A lesson may be interactive without pretending that every illustration is a trained model. The first lesson introduces words and numbers; later lessons introduce context, prediction, memory, tools and agents.

## Run the Digital Twin

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab/lessons/06-digital-twin/gradio-app
uv run app.py
```

Local model inference can be slow and requires a capable computer. For optional Hugging Face deployment, read [the full account, token and deployment guide](lessons/06-digital-twin/gradio-app/README.md). Use `uvx hf auth login` followed by `uv run python deploy.py` when eligible; never put tokens or private personal data into public project files. The Digital Twin is a conversational chatbot, **not an autonomous agent**. ZeroGPU account eligibility, quotas and availability must be checked before deployment; successful public deployment has **not** been verified as part of this release.

**Repo layout:** Keep exactly the six existing lesson directories. The `05-ai-retrieval` directory retains its name to preserve URLs; its lesson now teaches tool selection and agents. Do not create a duplicate Lesson 05 folder. Lesson 06 remains English-only.

### Hugging Face access token checklist

Before `uvx hf auth login`, open [Hugging Face tokens](https://huggingface.co/settings/tokens), **Create new token**, name it `ai-course`, select **Write**, copy it privately, and paste it at the login prompt. Verify with `uvx hf auth whoami`. See the [complete setup guide](lessons/06-digital-twin/gradio-app/README.md#create-your-hugging-face-access-token-before-logging-in). Tokens are secrets; never commit them.


## Safe deployment

Use `uv run python deploy.py` from `lessons/06-digital-twin/gradio-app`. It sends only the required app source files, not `.venv` or secrets. Create a Hugging Face Write token first, authenticate using `uvx hf auth login`, then open the Space URL printed by the script. The first run asks for a Space name; subsequent runs update it. An existing oversized Space may require a clean new Space name.

> Deployment update: the supplied `deploy.py` explicitly requests ZeroGPU (`zero-a10g`) rather than the default CPU Basic hardware when creating a new Space. Hosting eligibility is controlled by Hugging Face; no live deployment has been verified.

## Maintainer quality checks

Tests are kept in the GitHub repository (not in Hugging Face Space uploads). [Space version and compatibility policy](MAINTAINERS-SPACE-COMPATIBILITY.md) documents the pinned Python, Gradio, Transformers and ZeroGPU versions and the online GitHub Actions resolver. Live deployments must still be tested separately.
