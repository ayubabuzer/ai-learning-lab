# Your AI Digital Twin — Python + uv + Gradio + Hugging Face ZeroGPU

This is **one English-only generative AI chatbot**. The same `app.py` runs on your computer or in a Hugging Face Space. It uses an editable `about-me.txt`, conversation history and an open language model (the model name is documented in `app.py`). Visitors don't need an API key. Real model inference and a real Hugging Face deployment still require live verification.

**Privacy:** use an imaginary character and never publish private personal information. A public Space makes the default knowledge file publicly available.

## Recommended deployment: only the five required files

After creating a Hugging Face **Write** access token and connecting with `uvx hf auth login`, run this command **from this `gradio-app` folder**:

```bash
uv run python deploy.py
```

The script asks for your Space name once, remembers it locally in `.space-deploy.json`, creates or updates your Space, and uploads **only** `app.py`, `twin_core.py`, `about-me.txt`, `requirements.txt`, and a generated Hugging Face Space `README.md`. It excludes your 747 MB `.venv`, caches, test files, Git history, and credentials by construction. The local Space name file is excluded from Git and uploads. Subsequent deployments use the same command. **If an older Space already contains too many tracked files, deploy under a NEW Space name** rather than trying to upload to the oversized repository. The script does not delete old files.

Open the URL printed by the script. Wait for **Running**, open **App**, and test the chatbot. If it fails, inspect **Logs** and **Settings → Hardware**. ZeroGPU requires eligibility and may need selecting appropriate hardware in your Space; uploading code does not guarantee GPU availability. Only use fictional profile information in `about-me.txt` because Space files may be public.

The interactive prompts shown later in this guide are for the *optional, older Gradio CLI deployment method*, not this recommended script. Students using `deploy.py` do not need to answer GitHub Actions, Space app file, or git credential prompts during deployment.

## Create your Hugging Face access token **before** logging in

1. Visit [huggingface.co/join](https://huggingface.co/join), create an account, confirm the email, and sign in.
2. Open [Settings → Access Tokens](https://huggingface.co/settings/tokens), then choose **Create new token**.
3. Name the token `ai-course`, select the **Write** role, and create it. This course uses Write because deployment may upload or update your own Space. **Write is broad but is not unrestricted access** to other users’ private or gated resources. For production work, prefer a fine-grained token scoped to the specific Space or repository.
4. Copy the token privately. It may only be displayed once; if you lose it, generate a new token. **Never paste it into your source code, Git history, public screenshots, or `about-me.txt`.**
5. In the project terminal, use `uvx hf auth login`. This uses `uv` to run the CLI without adding a separate project dependency. If offered a browser or token method, choose **access-token login**, paste the token at the hidden prompt, and press Enter. If the terminal asks `Add token as git credential? (Y/n)`, choose `n` for this CLI deployment, or `Y` if you also plan to push changes using Git from this computer. Git-credential storage is optional for Gradio deployment.
6. Verify with `uvx hf auth whoami`. Your Hugging Face username should appear. If authentication fails, recheck your token, its role, and whether it has been revoked.
7. Continue to `uv run python deploy.py` only after authentication succeeds. If you already have `huggingface_hub` in your project dependencies, `uv run hf auth login` and `uv run hf auth whoami` are valid alternatives; **do not install it twice**.

A public model download alone cannot verify the Write role. You can confirm the token role on the token settings page. ZeroGPU hosting also requires separate account eligibility and does not follow automatically from token permissions.

## Windows setup

1. Open **PowerShell**.
2. Check Git: `git --version`. If missing: `winget install --id Git.Git -e` (then reopen PowerShell).
3. Install uv: `winget install --id astral-sh.uv -e`, reopen PowerShell, check `uv --version`.
4. Install Python: `uv python install 3.12`.
5. Clone the full project in a **fresh folder**:

```powershell
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
cd lessons/06-digital-twin/gradio-app
```

6. Edit `about-me.txt` (`notepad about-me.txt`).
7. Test on a capable computer: `uv run app.py`. Open `http://127.0.0.1:7860`; stop with Ctrl+C.
8. Create/verify a Hugging Face account at https://huggingface.co/join.
9. **First create the Write token using the guide above**, then run `uvx hf auth login`, paste the token when prompted, and verify with `uvx hf auth whoami`.
10. Deploy from the folder containing `app.py`: `uv run python deploy.py`. Choose `zero-a10g` when possible.
11. Check Space settings and test the public link in English.

## Mac setup

1. Open **Terminal**.
2. Check Git: `git --version`. If missing, install Command Line Tools: `xcode-select --install`.
3. Install `uv` with `brew install uv` (if Homebrew is installed), **or** `curl -LsSf https://astral.sh/uv/install.sh | sh`. Reopen Terminal and check `uv --version`.
4. Install Python: `uv python install 3.12`.
5. Clone the full project in a **fresh folder**:

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
cd lessons/06-digital-twin/gradio-app
```

6. Edit your fictional facts: `open -e about-me.txt`.
7. Optionally test locally: `uv run app.py`; stop with Ctrl+C.
8. Create and verify your Hugging Face account.
9. **First create the Write token using the guide above**, then log in with `uvx hf auth login` and verify with `uvx hf auth whoami`.
10. Publish: `uv run python deploy.py`; select `zero-a10g` if available.
11. Check Space settings, test and share your public link.

**Already cloned?** Don't clone again; simply open the `lessons/06-digital-twin/gradio-app` folder of your existing repository.


## Optional reference: prompts from the older Gradio CLI method

If you use the older `uv run gradio deploy` command rather than our safe script, Gradio may ask for metadata. These questions are expected, not errors. Wording and order depend on the installed version.

| Terminal asks | Recommended learner response | Why |
| --- | --- | --- |
| `Add token as git credential? (Y/n)` | `n` for Gradio CLI deployment; `Y` only if you will also use Git to push directly to your Hugging Face Space | Optional Git credential storage is not needed for the deploy command |
| `Enter Spaces app title [gradio-app]:` | Type `my-ai-digital-twin`, or press **Enter** | Sets the Space title; the default is acceptable, but a descriptive name is easier to recognise |
| `Enter Gradio app file [app.py]:` | Press **Enter** | Our entry point is `app.py` |
| `Create Github Action to automatically update Space on 'git push'? [n]:` | Press **Enter** (`n`) | Keep deployment manual for this beginner course. `Y` requires configuring a GitHub Action and GitHub secrets securely |
| Space owner / account, if asked | Choose your own account | Deploy to the account you control |
| Space visibility, if asked | **Public** only for fictional, non-private facts | Visitors can view public files; never deploy real personal information |
| Hardware choice, if offered | `zero-a10g` if eligible | This project uses `@spaces.GPU`; check **Space Settings → Hardware** after deployment |
| Other questions | Read the prompt; accept the default only if it matches the course and your intended publishing settings | Prompts can change across Gradio versions |

The CLI may show `Creating new Spaces Repo ... Collecting metadata, press Enter to accept default value.` This indicates a new Space is being configured and your local project will be uploaded. It does **not** mean authentication failed. The token must already have Write permission, but **the Space is created at deployment time**, not when the token is generated. If deployment errors, copy the error *without copying any secrets* and review the Space build logs.

## If you see the large-folder warning

The CLI may display: `It seems you are trying to upload a large folder at once...`. **This is a warning, not proof that deployment failed.** Let the command finish and open the Space to check whether it built successfully. Make sure you are inside `lessons/06-digital-twin/gradio-app`, not at the root of the entire course. Do not commit/upload `.venv/`, `__pycache__/`, downloaded model weights, cache folders, local `.env` files or access tokens. The Hugging Face Space will download its dependencies and public model when it runs; do not bundle local weights into the repo.

If the upload actually fails because the folder is too large, consult the [official large-folder upload instructions](https://huggingface.co/docs/huggingface_hub/main/en/guides/upload#upload-a-large-folder) for the existing Space. Do not blindly upload the entire course folder or create a second Space.

## After deployment: open and run your app

1. **Find your Space link.** When `uv run python deploy.py` finishes successfully, open the URL printed by the terminal, usually `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE`. Replace both placeholders; do not copy them literally. If you lost the URL, log in to [Hugging Face Spaces](https://huggingface.co/spaces), open your profile and find the Space you own.
2. **Check its state.** Open the **App** tab. The page may say *Building* or *Starting* while dependencies and model files are prepared. If it fails, open the Space's **Logs** (build and runtime) to see why. Check **Settings → Hardware** for the expected eligible `zero-a10g` configuration.
3. **Run a chat.** Once the app is Running, type an English question into the Gradio chat input such as `What is your name?`, then press **Enter** or **Send**. Ask another question about a fact in your fictional `about-me.txt`. Test one unknown fact too; the model may still hallucinate.
4. **Share or return later.** Copy the Space page URL and open it in another browser tab to verify public access. You **do not have to keep your laptop, terminal, or `uv run app.py` running** after successful deployment: Hugging Face hosts it. On free/shared resources the Space may sleep, wait in a GPU queue or exhaust a quota. Return to the Space URL and check logs if it does not respond.
5. **When you edit the profile or code:** Save the local changes and redeploy with `uv run python deploy.py` (or use a configured Space/Git sync). Local file edits do not automatically update an existing Space when you answered `n` to the GitHub Action question.

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

Official docs: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Git](https://git-scm.com/doc), [Gradio](https://www.gradio.app/guides/sharing-your-app), [ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu).
