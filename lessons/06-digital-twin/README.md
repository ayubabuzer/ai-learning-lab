# Lesson 06 — Build and Deploy Your AI Digital Twin (English only)

This final lesson uses **one real English-language chatbot**, not an illustrative rule-based app. The model reads an editable fictional profile in `about-me.txt`, recent conversation history and the visitor's question, and generates an answer. Visitors see a single modern chat screen; the character facts stay in the app file `about-me.txt` and are not displayed or editable in the public chat. The public Space repository may still expose that file, so use fictional facts only.

On the [Lesson 06 page](./) choose **Windows** (default) or **Mac** for a short, guided setup. Git, Python 3.12, `uv`, the profile editor, local testing, Hugging Face login and `uv run python deploy.py` are all covered.

## Clone the full project (new checkout)

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab
cd lessons/06-digital-twin/gradio-app
```

This clones all six lessons into one repository, as in the course. If you already have AI Learning Lab cloned, simply open its `lessons/06-digital-twin/gradio-app` folder instead.

## Run and deploy

```bash
uv python install 3.12
uv run app.py
uvx hf auth login
uv run python deploy.py
```

Local inference can be slow and initially downloads model weights; local testing is optional on low-powered computers. On Hugging Face, choose **ZeroGPU (`zero-a10g`)** if your account is eligible. Check the Space settings if the deployment prompt does not offer hardware selection. No paid external model API key is needed, but GPU queues and free usage limits apply.

Read the [full English project guide](gradio-app/README.md). Use only fictional information; a public Space's files are publicly accessible. The model can still make mistakes; check replies against the facts in `about-me.txt`.

[← Lesson 05](../05-ai-retrieval/) · [All lessons](../../)

**Important:** Before `uvx hf auth login`, create an access token with the **Write** role from [Hugging Face token settings](https://huggingface.co/settings/tokens), copy it privately, then paste it when prompted. See the [complete step-by-step guide](gradio-app/README.md#create-your-hugging-face-access-token-before-logging-in).

## Run your deployed Space

After `uv run python deploy.py` completes, open the Space URL shown in the terminal or find the Space under your Hugging Face profile. On its **App** tab, wait for the app to finish Building/Starting, then ask a question in the English chat interface. You do not need to keep the local terminal running. For problems, check the Space **Logs** and **Settings → Hardware**. Answer `n` (Enter) to the optional GitHub Actions prompt for manual deployment; a large-folder message is a warning, not necessarily an error. The [full deployment guide](gradio-app/README.md#after-deployment-open-and-run-your-app) covers these steps.


## Safe deployment / النشر الآمن

Use `uv run python deploy.py` from `lessons/06-digital-twin/gradio-app`. It sends only the required app source files, not `.venv` or secrets. Create a Hugging Face Write token first, authenticate using `uvx hf auth login`, then open the Space URL printed by the script. The first run asks for a Space name; subsequent runs update it. An existing oversized Space may require a clean new Space name.
