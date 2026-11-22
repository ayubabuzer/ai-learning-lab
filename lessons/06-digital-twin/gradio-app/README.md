# Your AI Digital Twin — Python + uv + Gradio + Hugging Face ZeroGPU

This is **one English-only generative AI chatbot**. The same `app.py` runs on your computer or in a Hugging Face Space. It uses an editable `about-me.txt`, conversation history and an open language model (the model name is documented in `app.py`). Visitors don't need an API key. Real model inference and a real Hugging Face deployment still require live verification.

**Privacy:** use an imaginary character and never publish private personal information. A public Space makes the default knowledge file publicly available.

## Deploy your Digital Twin

After creating a Hugging Face **Write** access token and connecting with `uvx hf auth login`, run this command **from this `gradio-app` folder**. It installs only the small Hub client, not the model or PyTorch:

```bash
uv run deploy.py
```

First you may check locally without uploading by running `uv run deploy.py --check`. The script asks for your Space name once, remembers it locally in `.space-deploy.json`, creates or updates your Space, and uploads **only** `app.py`, `twin_core.py`, `about-me.txt`, `requirements.txt`, and a generated Hugging Face Space `README.md`. It excludes your 747 MB `.venv`, caches, test files, Git history, and credentials by construction. The local Space name file is excluded from Git and uploads. Subsequent deployments use the same command. **If an older Space already contains too many tracked files, deploy under a NEW Space name** rather than trying to upload to the oversized repository. The script does not delete old files.

Open the URL printed by the script. Wait for **Running**, open **App**, and test the chatbot. If it fails, inspect **Logs** and **Settings → Hardware**. The script requests ZeroGPU when creating the Space. Hugging Face must still approve account eligibility and start the app; uploading code does not guarantee GPU availability. Only use fictional profile information in `about-me.txt` because Space files may be public.

The interactive prompts shown later in this guide are for the *optional, older Gradio CLI deployment method*, not this recommended script. Students using `deploy.py` do not need to answer GitHub Actions, Space app file, or git credential prompts during deployment.


**Windows deployment is lightweight:** `deploy.py` includes uv inline script metadata, so `uv run deploy.py` creates a dedicated environment with only `huggingface_hub`. It does not run Qwen or download the 4 GB model on the student's PC. Local testing (`uv run python app.py`) is a separate, optional heavyweight step. A Windows user can complete the online deployment without running the AI locally.

## Why we test versions before deployment

Hugging Face provides **Gradio, the `spaces` runtime and `huggingface_hub`** in its Space image. Our Space's `requirements.txt` installs only the app's model libraries. The generated Space `README.md` pins Python 3.12 and Gradio 6.32.0, and `transformers==5.23.0` is compatible with Gradio's Hub dependencies. The deploy script rejects incompatible changes before uploading.

For contributors, run `python space_compat.py` and the GitHub Actions dependency-resolution check. The latter resolves the actual Hugging Face SDK dependencies using `uv` on Linux. No offline check can guarantee future service uptime or a successful GPU build: consult the Space's first build error if it fails.

## Create your Hugging Face access token **before** logging in

1. Visit [huggingface.co/join](https://huggingface.co/join), create an account, confirm the email, and sign in.
2. Open [Settings → Access Tokens](https://huggingface.co/settings/tokens), then choose **Create new token**.
3. Name the token `ai-course`, select the **Write** role, and create it. This course uses Write because deployment may upload or update your own Space. **Write is broad but is not unrestricted access** to other users’ private or gated resources. For production work, prefer a fine-grained token scoped to the specific Space or repository.
4. Copy the token privately. It may only be displayed once; if you lose it, generate a new token. **Never paste it into your source code, Git history, public screenshots, or `about-me.txt`.**
5. In the project terminal, use `uvx hf auth login`. This uses `uv` to run the CLI without adding a separate project dependency. If offered a browser or token method, choose **access-token login**, paste the token at the hidden prompt, and press Enter. If the terminal asks `Add token as git credential? (Y/n)`, choose `n` for this CLI deployment, or `Y` if you also plan to push changes using Git from this computer. Git-credential storage is optional for Gradio deployment.
6. Verify with `uvx hf auth whoami`. Your Hugging Face username should appear. If authentication fails, recheck your token, its role, and whether it has been revoked.
7. Continue to `uv run deploy.py` only after authentication succeeds. If you already have `huggingface_hub` in your project dependencies, `uv run hf auth login` and `uv run hf auth whoami` are valid alternatives; **do not install it twice**.

A public model download alone cannot verify the Write role. You can confirm the token role on the token settings page. ZeroGPU hosting also requires separate account eligibility and does not follow automatically from token permissions.

## Windows setup (PowerShell, Windows 10/11)

1. Open **PowerShell**.
2. Check Git: `git --version`. If missing: `winget install --id Git.Git -e` (then reopen PowerShell). If `winget` is missing, use the [Git for Windows installer](https://git-scm.com/install/windows).
3. Install uv: `winget install --id astral-sh.uv -e`, reopen PowerShell, then verify `uv --version`. If `winget` is missing, follow the [official uv Windows installer](https://docs.astral.sh/uv/getting-started/installation/). Do not use the macOS `curl | sh` command in PowerShell.
4. Install Python: `uv python install 3.12`.
5. Clone the full project in a **fresh folder**, then navigate to it:

```powershell
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
cd lessons/06-digital-twin/gradio-app
```

6. Edit `about-me.txt` (`notepad about-me.txt`).
7. **Optional local model test:** only on a computer with sufficient memory, run `uv run python app.py`. This downloads the model and heavy packages. Windows students without suitable hardware can **skip** it and deploy directly. If you do run it, open `http://127.0.0.1:7860` and stop with Ctrl+C.
8. Create/verify a Hugging Face account at https://huggingface.co/join.
9. **First create the Write token using the guide above**, then run `uvx hf auth login`, paste the token when prompted, and verify with `uvx hf auth whoami`.
10. Verify deployment files with `uv run deploy.py --check` (optional), then publish from the folder containing `app.py` using `uv run deploy.py`. The script requests `zero-a10g` automatically; no manual hardware selection or GitHub Action prompts are required.
11. Check Space settings and test the public link in English.

## Mac setup

1. Open **Terminal**.
2. Check Git: `git --version`. If missing, install Command Line Tools: `xcode-select --install`.
3. Install `uv` with `brew install uv` (if Homebrew is installed), **or** `curl -LsSf https://astral.sh/uv/install.sh | sh`. Reopen Terminal and check `uv --version`.
4. Install Python: `uv python install 3.12`.
5. Clone the full project in a **fresh folder**, then navigate to it:

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
cd lessons/06-digital-twin/gradio-app
```

6. Edit your fictional facts: `open -e about-me.txt`.
7. Optionally test locally on a capable computer: `uv run python app.py`; stop with Ctrl+C.
8. Create and verify your Hugging Face account.
9. **First create the Write token using the guide above**, then log in with `uvx hf auth login` and verify with `uvx hf auth whoami`.
10. Publish: `uv run deploy.py`; the script requests `zero-a10g` automatically for eligible accounts.
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

1. **Find your Space link.** When `uv run deploy.py` finishes successfully, open the URL printed by the terminal, usually `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE`. Replace both placeholders; do not copy them literally. If you lost the URL, log in to [Hugging Face Spaces](https://huggingface.co/spaces), open your profile and find the Space you own.
2. **Check its state.** Open the **App** tab. The page may say *Building* or *Starting* while dependencies and model files are prepared. If it fails, open the Space's **Logs** (build and runtime) to see why. Check **Settings → Hardware** for the expected eligible `zero-a10g` configuration.
3. **Run a chat.** Once the app is Running, type an English question into the Gradio chat input such as `What is your name?`, then press **Enter** or **Send**. Ask another question about a fact in your fictional `about-me.txt`. Test one unknown fact too; the model may still hallucinate.
4. **Share or return later.** Copy the Space page URL and open it in another browser tab to verify public access. You **do not have to keep your laptop, terminal, or `uv run python app.py` running** after successful deployment: Hugging Face hosts it. On free/shared resources the Space may sleep, wait in a GPU queue or exhaust a quota. Return to the Space URL and check logs if it does not respond.
5. **When you edit the profile or code:** Save the local changes and redeploy with `uv run deploy.py` (or use a configured Space/Git sync). Local file edits do not automatically update the hosted Space; use the same script to redeploy after changing files.

## If a chat still fails after deployment

1. Open your Space → **Logs** → **Runtime** (not just Build logs). Send a question in the chat while viewing the log.
2. If the answer contains a code such as `Reference: a1b2c3d4`, search the runtime logs for that code. The original Python exception and traceback are logged there; the public chat never reveals the traceback.
3. Confirm **Settings → Hardware** shows the eligible **ZeroGPU** hardware. If the log mentions `No @spaces.GPU function detected`, verify that the updated `app.py` was uploaded, not the old version.
4. For `ZeroGPU quota exceeded`, the visitor's GPU allowance needs to reset. For `CUDA` or worker errors, use the runtime traceback to investigate the actual failure. Repeatedly redeploying without reading logs will not fix a quota or infrastructure error.
5. The app uses one request at a time to reduce shared-GPU contention. A cold GPU or model load can still be slow. Don't claim a request succeeded until a real model reply appears.

To republish the corrected code from this folder, use `uv run deploy.py`, then open the existing Space URL and test **What is your name?** and **Where do you live?**.

## About hosting and speed

- Local inference first downloads model files and can be very slow on a Mac without suitable acceleration. You can skip the local model test on a weak laptop.
- Hugging Face ZeroGPU requires an eligible account; it has queues and usage limits. The default `cpu-basic` hardware is generally not available for newly created free-account Gradio Spaces; our deployment script requests `zero-a10g` at creation; check your eligibility and Space Settings → Hardware if creation fails.
- The course uses `deploy.py` rather than the interactive `gradio deploy` command; `deploy.py` explicitly requests ZeroGPU.
- Never paste your Hugging Face write token into project files.
- Re-deploy or push updated files to your Space to publish changes to `about-me.txt`.

## What the Digital Twin actually does

The public app is **chat only**: a conversation, one message composer, and suggested starter questions. It reads the fictional facts from `about-me.txt` on the server, combines them with recent chat messages, and asks the real Qwen model to generate its next response. Visitors cannot edit or view the profile *through the chat interface*. Remember that `about-me.txt` is still a file in a public Space repository — **never put private information in it**. Unknown facts should produce “I don't know”, although real language models can still make mistakes.

**Why the previous version always replied with a generic error:** the GPU decoration was on an internal inference helper, not on Gradio's registered event handler, and a blanket exception handler hid the actual traceback. The new `respond()` function is both `@spaces.GPU`-decorated and directly registered in `gr.ChatInterface`. Each caught error now includes a short reference code; search for it in the Space **Logs → Runtime** to see the real underlying exception. This is a diagnosed code issue, not confirmation that the remote Space has been repaired until you redeploy and test it.

## Files

- `app.py` — English-only Gradio chatbot with real model inference and ZeroGPU decorator
- `twin_core.py` — profile grounding, conversation history and error messages
- `about-me.txt` — editable default fictional knowledge file
- `pyproject.toml`, `.python-version`, `requirements.txt` — dependencies
- `tests/` — quick tests without model downloads

Official docs: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Git](https://git-scm.com/doc), [Gradio](https://www.gradio.app/guides/sharing-your-app), [ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu).

### Free ZeroGPU deployment (current hosting requirements)

`uv run deploy.py` explicitly requests `space_hardware="zero-a10g"` when creating the Gradio Space. This avoids the default CPU Basic creation request, which may return HTTP 402 for free accounts. Hugging Face currently permits up to two free ZeroGPU Spaces for eligible personal accounts (verified email, account older than 30 days). No new Space or successful build is guaranteed: account restrictions, queues, and runtime limits still apply. Existing Spaces are never switched to a different hardware type silently. The file allowlist excludes `.venv`.
