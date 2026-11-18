---
title: AI Learning Lab Digital Twin
emoji: 🤖
colorFrom: blue
colorTo: teal
sdk: gradio
app_file: app.py
pinned: false
---

# Build, run and share your Digital Twin 🤖

Create a **fictional, source-based question-answering assistant**. It reads `about-me.txt`, replies using information it can find, and displays the exact supporting line separately. The model is a lightweight, rule-based classroom demonstration, not a pretrained generative AI model. It is not guaranteed to understand arbitrary questions.

## 1. What you need

- Git (for cloning), Python **3.11 or newer**, and an internet connection for installing dependencies.
- No AI API key or large language-model download.
- **Never publish a real child’s name, address, email, school details or other private data.** All sample facts describe fictional characters.

## 2. Clone the GitHub project

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab/lessons/06-digital-twin/gradio-app
```

Alternatively, download the complete AI Learning Lab ZIP and open its `lessons/06-digital-twin/gradio-app` folder in a terminal.

## 3. Install Gradio

Create an isolated environment (recommended):

```bash
python -m venv .venv
```

Activate it on **Windows (PowerShell)**:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on **macOS / Linux**:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

On machines where `python` means Python 2, use `python3` instead. If school security policies prevent installation, ask your teacher or IT administrator.

## 4. Run it locally

```bash
python app.py
```

Open the local URL Gradio prints (commonly `http://127.0.0.1:7860`). Ask **What is your name?** and see a concise answer plus its supporting `about-me.txt` line. Ask something missing, such as **How old are you?**, and watch it say **I don't know**.

Edit `about-me.txt` to add imaginary facts; restart the app to load changed defaults, or paste new facts into its knowledge box. For Arabic, switch to `العربية` and click **Load example for selected language**.

## 5. Optional: deploy to Hugging Face Spaces

1. Sign up at <https://huggingface.co/join> and verify your account.
2. Check the current hosting requirements and your account’s eligibility at <https://huggingface.co/docs/hub/spaces-overview>. **Static Spaces are free, but they cannot run this Python/Gradio app. A Gradio Space may require a paid plan, or qualifying free-hosting eligibility and quotas. Do not assume deployment is free.**
3. If you have eligible compute hosting, open <https://huggingface.co/new-space>, give the Space a name such as `my-fictional-digital-twin`, select **Gradio**, and choose **Public** only if the text file contains no private information.
4. Upload **four files from this `gradio-app` folder to the root of the new Space**: `app.py`, `requirements.txt`, `about-me.txt`, and this `README.md`. Do **not** upload the whole GitHub repository as a nested folder. The YAML at the top of this README tells Spaces to launch `app.py`.
5. Wait for the Space build to succeed. Test an answer and its evidence, then share the public Space link with friends or the class.

A public Space's availability depends on the host's policies, quotas and uptime. Publishing is optional: the local app is a complete learning project on its own. This version requires **no GPU or generative model**.

## What it can and cannot do

- ✅ Give a concise name reply when the knowledge file contains `My name is Alex` (or `اسمي نور`).
- ✅ Show the **original source line** underneath its reply.
- ✅ Return the closest matching sentence for some other questions.
- ✅ Say **I don't know** when no sufficient match exists.
- ❌ It does **not** automatically establish whether a source is factually true.
- ❌ It does **not** generate creative answers or understand all possible grammar.

For the teaching sequence, see the Lesson 06 guide one directory above and Lesson 05 on checking evidence.
