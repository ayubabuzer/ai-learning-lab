# Lesson 06 — Build Your Own AI Digital Twin

**[English](README.md) · [العربية](README.ar.md)**

Build a **fictional assistant** from a `.txt` file with one fact per line. The student-facing interface separates **⚙️ knowledge/settings**, **✍️ question**, **🤖 answer**, and **📖 exact source**. The answer is initially blank. A short animated robot icon appears when asking a question.

Try **What is your name?**: with the sample file the assistant replies **My name is Alex.**, while the source panel displays the full original line. Try **How old are you?**: with no supporting age fact it should say **I don't know**.

This is a small rule-based extraction / matching algorithm. Some questions can return an exact sentence instead of a polished answer; not all free-text questions are understood. The source is not automatically verified as correct. Use fictional characters, not personal information about pupils.

## Run and deploy your Gradio project

The included [`gradio-app/`](gradio-app/) is a standalone Python + Gradio version. The [full setup guide](gradio-app/README.md) covers `git clone`, `python -m venv`, `pip install -r requirements.txt`, running `python app.py`, creating a Hugging Face account and optionally deploying.

**Hosting reminder:** Public Python/Gradio hosting on Hugging Face may require a paid plan or qualifying hosting access. A free Static Space cannot run the Gradio application; running locally remains a complete learning activity.

[← Lesson 05](../05-ai-retrieval/) · [All lessons](../../)
