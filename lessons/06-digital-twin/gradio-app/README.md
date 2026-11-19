# Your AI Digital Twin — Python + uv + Gradio + Hugging Face ZeroGPU

This is **one English-only generative AI chatbot**. The same `app.py` runs on your computer or in a Hugging Face Space. It uses an editable `about-me.txt`, conversation history and an open language model (the model name is documented in `app.py`). Visitors don't need an API key. Real model inference and a real Hugging Face deployment still require live verification.

**Privacy:** use an imaginary character and never publish private personal information. A public Space makes the default knowledge file publicly available.

## Windows setup

1. Open **PowerShell**.
2. Check Git: `git --version`. If missing: `winget install --id Git.Git -e` (then reopen PowerShell).
3. Install uv: `winget install --id astral-sh.uv -e`, reopen PowerShell, check `uv --version`.
4. Install Python: `uv python install 3.12`.
5. Clone only Lesson 06 in a **fresh folder**:

```powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
git sparse-checkout set lessons/06-digital-twin
cd lessons/06-digital-twin/gradio-app
```

6. Edit `about-me.txt` (`notepad about-me.txt`).
7. Test on a capable computer: `uv run app.py`. Open `http://127.0.0.1:7860`; stop with Ctrl+C.
8. Create/verify a Hugging Face account at https://huggingface.co/join.
9. Run `uvx hf auth login` and `uvx hf auth whoami`.
10. Deploy from the folder containing `app.py`: `uv run gradio deploy`. Choose `zero-a10g` when possible.
11. Check Space settings and test the public link in English.

## Mac setup

1. Open **Terminal**.
2. Check Git: `git --version`. If missing, install Command Line Tools: `xcode-select --install`.
3. Install `uv` with `brew install uv` (if Homebrew is installed), **or** `curl -LsSf https://astral.sh/uv/install.sh | sh`. Reopen Terminal and check `uv --version`.
4. Install Python: `uv python install 3.12`.
5. Clone only Lesson 06 in a **fresh folder**:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
git sparse-checkout set lessons/06-digital-twin
cd lessons/06-digital-twin/gradio-app
```

6. Edit your fictional facts: `open -e about-me.txt`.
7. Optionally test locally: `uv run app.py`; stop with Ctrl+C.
8. Create and verify your Hugging Face account.
9. Log in: `uvx hf auth login`; verify `uvx hf auth whoami`.
10. Publish: `uv run gradio deploy`; select `zero-a10g` if available.
11. Check Space settings, test and share your public link.

**Already cloned?** Don't clone again; simply change into your existing `lessons/06-digital-twin/gradio-app` directory. Sparse checkout is for a fresh clone, and Git still needs some repository metadata/root files.

## About hosting and speed

- Local inference first downloads model files and can be very slow on a Mac without suitable acceleration. You can skip the local model test on a weak laptop.
- Hugging Face ZeroGPU requires an eligible account; it has queues and usage limits. The default `cpu-basic` hardware is generally not available for newly created free-account Gradio Spaces; choose `zero-a10g` if offered, or check the Space's Settings → Hardware.
- Gradio's deploy tool may change prompts between releases. The command alone does not guarantee ZeroGPU was selected.
- Never paste your Hugging Face write token into project files.
- Re-deploy or push updated files to your Space to publish changes to `about-me.txt`.

## What the Digital Twin actually does

The app creates a system instruction from the fictional facts, sends recent chat messages and the new question to a real text-generation model, and shows its freshly generated reply. Separately, it suggests a potentially related line from the profile. This is **not proof** the answer is correct. Unknown facts should produce “I don't know”, though real language models can still hallucinate.

## Files

- `app.py` — English-only Gradio chatbot with real model inference and ZeroGPU decorator
- `twin_core.py` — prompt, conversation handling, source hints, error messages
- `about-me.txt` — editable default fictional knowledge file
- `pyproject.toml`, `.python-version`, `requirements.txt` — dependencies
- `tests/` — quick tests without model downloads

Official docs: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Git sparse checkout](https://git-scm.com/docs/git-sparse-checkout), [Gradio](https://www.gradio.app/guides/sharing-your-app), [ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu).
