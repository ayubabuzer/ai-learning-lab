# Lesson 06 — Build and Deploy Your AI Digital Twin (English only)

This final lesson uses **one real English-language chatbot**, not an illustrative rule-based app. The model reads an editable fictional profile in `about-me.txt`, recent conversation history and the visitor's question, and generates an answer. The app shows a *possible matching source line* separately from the model's response.

On the [Lesson 06 page](./) choose **Windows** (default) or **Mac** for a short, guided setup. Git, Python 3.12, `uv`, the profile editor, local testing, Hugging Face login and `uv run gradio deploy` are all covered.

## Clone only Lesson 06 (new checkout)

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
git sparse-checkout set lessons/06-digital-twin
cd lessons/06-digital-twin/gradio-app
```

Sparse checkout checks out Lesson 06 plus a few repository-root files. Git still keeps its repository metadata; it does **not** create an independent repository for Lesson 06. If you already have AI Learning Lab cloned, simply open its `lessons/06-digital-twin/gradio-app` folder instead.

## Run and deploy

```bash
uv python install 3.12
uv run app.py
uvx hf auth login
uv run gradio deploy
```

Local inference can be slow and initially downloads model weights; local testing is optional on low-powered computers. On Hugging Face, choose **ZeroGPU (`zero-a10g`)** if your account is eligible. Check the Space settings if the deployment prompt does not offer hardware selection. No paid external model API key is needed, but GPU queues and free usage limits apply.

Read the [full English project guide](gradio-app/README.md). Use only fictional information; a public Space's files are publicly accessible. The model can be wrong, and a possible source line is not proof of an accurate answer.

[← Lesson 05](../05-ai-retrieval/) · [All lessons](../../)
