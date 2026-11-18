# Lesson 06 — Build and Deploy Your Own AI Digital Twin

**[English](README.md) · [العربية](README.ar.md)**

In Lessons 01–05, we explored text, word relationships, prediction, context and checking evidence. **Now build one real, generative AI chatbot.** The model reads fictional facts from `about-me.txt`, uses recent conversation history and creates a new answer in English or Arabic.

**Follow Ed Donner's deployment workflow:** clone → install `uv` → edit profile → `uv run app.py` → `uvx hf auth login` → `uv run gradio deploy` → share your Hugging Face Space link. Choose **ZeroGPU (`zero-a10g`)**, not the older CPU Basic default.

Open the [step-by-step English guide](gradio-app/README.md) or [Arabic guide](gradio-app/README.ar.md). The **same** `gradio-app/` project is used for local testing and publication—there are no separate levels or replacement apps.

**What pupils discover:** the profile is temporary context, not permanent model training. The model generates natural words, but it can make mistakes or invent facts. The UI keeps the AI's answer separate from a possible supporting line so pupils can check what the source actually says.

**Hosting requirement:** Hugging Face currently lets eligible free personal accounts (verified email, more than 30 days old and in good standing) host up to two ZeroGPU Spaces. Daily GPU limits and queues apply. The app does not need a paid LLM API key. Local use downloads multiple GB of model files and may be slow on basic school PCs. **Use only imaginary pupil-safe information.**

[← Lesson 05](../05-ai-retrieval/) · [All lessons](../../)
