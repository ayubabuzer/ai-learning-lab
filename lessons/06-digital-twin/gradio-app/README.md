---
title: AI Learning Lab Digital Twin
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.5.1
app_file: app.py
pinned: false
---

# Digital Twin — Gradio starter (Lesson 06)

This is a **lightweight, extractive retrieval demonstration**, not a generative Qwen model. It quotes a matching line from an editable fictional knowledge file and cites its line number; if the question lacks sufficient word overlap, it says **I don’t know**. The matching is simple and limited: a close paraphrase can be missed, and a matching line is not guaranteed to answer the question.

## Run locally (teacher/developer computer)

1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. `python -m pip install -r requirements.txt`
4. `python app.py`
5. Open the local address printed by Gradio.

This installation step requires network access, but pupils using the static GitHub Pages lesson do **not** install Python or a model. Local Gradio use has no model download or per-question API charge.

## Make it yours

Edit `about-me.txt` to describe an **imaginary** person, character, robot or planet. Each fact should be on its own line. In the Gradio app, you can edit the knowledge textbox or upload your own `.txt` file. Try a question with an answer and one with missing information. Confirm the source line is shown.

## Optional Hugging Face Spaces publishing

Create a Gradio Space (subject to current account eligibility, hardware and quota policies), and add `app.py`, `requirements.txt` and `about-me.txt` at the root of that Space. Hosting is **optional** and may change in cost or availability. Uploading real pupil details is not appropriate. If deployed, the text submitted by visitors is processed by the host; don't promise server-side privacy based on the browser-only version.

## Important distinction

This is an early retrieval-grounded foundation. A future extension could use a hosted open-source Qwen model to *write* answers using the retrieved evidence, while still showing the sources and testing unsupported questions. That extension is **not included** and should never be described as already working.
