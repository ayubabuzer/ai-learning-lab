# 🤖 Build and deploy your real AI Digital Twin with `uv` + Gradio + Hugging Face ZeroGPU

**English · [العربية](README.ar.md)**

This is the **real-model** Digital Twin from AI Learning Lab, following Ed Donner's **workflow**: edit a fictional profile, `uv run app.py`, sign in to Hugging Face, and `uv run gradio deploy`. Unlike Ed's paid-model API example, our model runs **directly on Hugging Face ZeroGPU**, so you do not need an OpenAI or Groq API key.

**No student information:** use an invented character. Do not publish a real child's name, school, email, address, phone number, or personal story.

## Before you start

- Git, [uv](https://docs.astral.sh/uv/getting-started/installation/), an internet connection, and a computer able to install Python.
- For **local inference**, the default `Qwen/Qwen3-1.7B` model downloads several GB of weights and needs substantial RAM; local CPU answers can be slow. **The shared Space is the intended classroom experience after deployment.** No pupil needs to download a model merely to visit the published URL.
- To **host ZeroGPU for free**, your Hugging Face personal account must have a verified email, be older than 30 days, be in good standing, and have fewer than two ZeroGPU Spaces. Hardware and quota rules can change: <https://huggingface.co/docs/hub/spaces-zerogpu>.
- Free visitors can encounter queues and daily GPU limits. The page shows friendly retry advice; some queue/quota failures may still be shown by Hugging Face itself.

## 1. Clone and open the project

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab/lessons/06-digital-twin/gradio-app
```

Or unpack the course ZIP and open this **exact** `gradio-app` folder in a terminal. **Deploy from this folder, not from the repository root.** There is only one Digital Twin project.

## 2. Install `uv`

Follow the official instructions at <https://docs.astral.sh/uv/getting-started/installation/>. For example:

**Windows PowerShell:**
```powershell
winget install --id=astral-sh.uv -e
```

**macOS with Homebrew:**
```bash
brew install uv
```

On other systems, use the official uv installer. Verify it:

```bash
uv --version
```

## 3. Personalise your Digital Twin

Edit **`about-me.txt`**. By default it's about *Alex*, a fictional robot. Write simple fictional facts, such as the character's name, hobbies, likes and goals. This file becomes the default profile. Visitors may edit a temporary copy in their own chat session, but those edits do **not** change the published file.

## 4. Run locally (like Ed)

```bash
uv run app.py
```

`uv` prepares a Python 3.12 environment and installs the dependencies. At first launch, the pretrained model downloads; **this is not instant**, especially on a school laptop without a GPU. Open the local URL printed by Gradio (usually <http://127.0.0.1:7860>). Ask *What is your name?* or *ما اسمك؟*.

> If the local computer cannot run the model, use a suitable teacher computer for testing and publish to ZeroGPU. The browser lessons (01–05) remain lightweight; the published Digital Twin runs the model remotely.

## 5. Create your free Hugging Face account

Open <https://huggingface.co/join>, verify your email, and check [ZeroGPU eligibility](https://huggingface.co/docs/hub/spaces-zerogpu). Create a **write** token in <https://huggingface.co/settings/tokens> (scope permitting Space creation).

Authenticate from the **same terminal**:

```bash
uvx hf auth login
uvx hf auth whoami
```

Paste your access token only into the official login prompt. **Never put it in `app.py`, `about-me.txt`, a public repo or chat message.** No model API key is needed.

## 6. Deploy using the same command as Ed

From the `gradio-app` folder run:

```bash
uv run gradio deploy
```

Answer the Gradio prompts:

| Prompt | What to enter |
|---|---|
| Space title | Your choice, e.g. `my-learning-lab-twin` |
| App file | `app.py` |
| **Hardware** | **`zero-a10g` (ZeroGPU)** — **DO NOT accept `cpu-basic`** |
| Secrets | `n` (none required for this model) |
| GitHub Action | `n` (optional later) |

**Important:** Ed's recorded course accepts **CPU Basic** by default. On today's free Hugging Face accounts, an ordinary CPU Basic Gradio Space generally cannot be created. The free exception for eligible accounts is **ZeroGPU**. Enter `zero-a10g` explicitly when prompted; its name in the API remains this even when the underlying GPU changes. If `uv run gradio deploy` skips the hardware question, check the Space **Settings → Hardware** and ensure **ZeroGPU** is selected before testing. You may need to remove previously saved Space frontmatter in `README.md` if redeploying with incorrect settings.

The command will upload the files, create the Space and print its public link. On first launch, Hugging Face downloads the model weights for the Space. Wait for the build to finish, then test English and Arabic questions and share the URL.

**If the Space cannot be created:** verify account age, email, ZeroGPU eligibility and remaining Space allowance. We cannot bypass Hugging Face's hosting rules. Your local project and code still work; a shared free deployment is conditional on your account.

## 7. Test it and share it

- Ask for a fact from `about-me.txt`: the answer should be newly generated text, not a copied line.
- Try a different phrasing or ask in Arabic.
- Ask something not covered, e.g. *How old are you?* — the assistant is instructed to say **I don't know**. **Language models can still make mistakes**, so check answers.
- Compare the **AI reply** with the **possible supporting line** displayed separately. A matching line is not proof that the answer is correct.
- If the GPU is busy or the visitor's allowance is exhausted, **try again later**.

## How this works

The app loads a real multilingual open model from <https://huggingface.co/Qwen/Qwen3-1.7B> into ZeroGPU using the `@spaces.GPU` decorator. The model receives the edited profile, the current question and recent chat history as **temporary context**, then generates a reply. We do **not** fine-tune it, change its weights or save conversations permanently. This example has **no external paid AI API**; model computation is done on the shared Hugging Face hardware.

The app **does not guarantee factuality**, nor does it perform a general web search. Supporting lines are suggested by lightweight keyword matching, then shown separately so pupils can inspect them. Anyone using a **public** Space can interact with it; do not insert private facts.

## Files

- `app.py` — bilingual Gradio user interface and real text generation on ZeroGPU
- `twin_core.py` — safe context assembly, history handling and source hints
- `about-me.txt` — fictional profile to personalise
- `pyproject.toml`, `.python-version` — uv's local Python environment
- `requirements.txt` — model dependencies for Hugging Face Spaces (Gradio and `spaces` are managed by the Space SDK)
- `tests/` — fast checks without downloading the model

**Note for developers:** The `README.md` intentionally begins without Hugging Face Space YAML metadata so **the first** `uv run gradio deploy` asks for the hardware. The CLI then inserts metadata automatically. If you re-run deployment after the metadata has been generated, verify hardware in Space Settings; changing the README metadata alone does not resize hardware.

## Useful official documentation

- [uv installation](https://docs.astral.sh/uv/getting-started/installation/)
- [Gradio deploy CLI](https://gradio.app/guides/sharing-your-app)
- [Hugging Face ZeroGPU](https://huggingface.co/docs/hub/spaces-zerogpu)
- [Hugging Face Spaces account / hardware eligibility](https://huggingface.co/docs/hub/spaces-overview)
