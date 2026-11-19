# AI Learning Lab — Teacher guide

A six-lesson bilingual classroom journey for beginners. Lessons 01–05 use lightweight, explicit teaching algorithms in pupils' browsers. The Lesson 06 project uses a real model hosted on ZeroGPU after deployment. The pupil UI distinguishes **✍️ input**, **⚙️ examples/settings**, **🤖 mini-robot reply**, and **📖 evidence/source**. Output starts blank until pupils take an action; a short robot animation signals the calculation.

## Lesson 01 · How Does AI Read Our Words? (20 min)

Type, change and inspect a sentence. Compare English punctuation or Arabic word forms. Click pieces to see **classroom IDs** — not actual LLM token IDs. Avoid unnecessary byte and hexadecimal jargon. The output remains unfilled until pupils click Explore.

## Lesson 02 · How Does AI Connect Words? (25 min)

Compare `cat`/`dog` and `cat`/`banana`. Edit the sample text and rebuild. Ask why unrelated words can sometimes have equal co-occurrence vectors: the map places their **display dots** next to each other with dashed lines, while preserving the same calculated coordinates. Explain why this is not a claim of identical meanings. Use the separate, invented axes diagram:

- **king − man:** `[3,1] − [1,1] = [2,0]`
- **king − man + woman:** `[2,0] + [1,3] = [3,3] = queen`

Invented coordinates do not represent pretrained embeddings.

## Lesson 03 · How Does AI Predict What Comes Next? (25 min)

Ask what might follow `The cat drinks`. Students view example sentences, predict the probabilities, then add another `The cat drinks water` line and **Teach the mini AI**. Large models learn patterns from many **words, sentences, books, websites, articles and stories**. Our small predictor counts next words in editable text. Pupils press Predict to see results; examples alone do not cause a generated answer to appear.

## Lesson 04 · Does AI Really Remember? (20 min)

Invent facts about a robot or planet, ask open-ended questions, toggle Include context and view the exact received text. Start a new session. Contrast temporary request context, model parameters and app persistence. The classroom reader quotes related evidence rather than composing arbitrary new answers.

## Lesson 05 · How Does AI Know Which Words to Look At? (20–25 min)

Use the new bilingual **Attention Explorer**. Pupils enter any short sentence, press Explore, click a word and watch its calculated connections and percentages. Then change one word and switch between **Similar-looking words** and **Nearby words**. Ask whether a high attention weight proves meaning or truth (it does not).

**Teach simply:** a real Transformer learns numerical settings during training, uses them to compare token representations, and shares attention across tokens. The lesson's attention percentages are **calculated live by an untrained classroom algorithm with fixed numerical settings**, not measured from a pretrained LLM. No model download, accounts or hidden API. The output begins empty until Explore is clicked. Use the separate English/Arabic sample sentences and check RTL.

## Lesson 06 · Build Your Own AI Digital Twin (30–45 min)

This lesson now guides pupils through **one real-model Gradio application** (not a rule-based chatbot). Learners choose fictional facts for `about-me.txt`; a capable teacher computer can test locally with `uv run app.py`, then an eligible account publishes with `uv run gradio deploy` and **ZeroGPU `zero-a10g`**. Compare natural generated replies with the possible supporting line displayed outside the robot answer. Ask an unsupported age question to discuss why language models may invent facts despite clear instructions. The website includes a self-reported, printable participation certificate. Read [the complete deployment guide](lessons/06-digital-twin/gradio-app/README.md).

## Safety and accessibility

Use Arabic mode for Lessons 01–05; Lesson 06 is English-only. Use fictional data only. A public Hugging Face Space publishes its source files and receives visitor input remotely; never upload personal information about pupils. Preview the actual GitHub Pages deployment on a school computer before class.

## Updated capstone: real language model with uv + ZeroGPU

Follow the [real-model Digital Twin guide](lessons/06-digital-twin/gradio-app/README.md). Pupils customise a **fictional** profile, then a teacher or eligible pupil uses `uv run app.py`, `uvx hf auth login` and `uv run gradio deploy` with hardware `zero-a10g` (not CPU Basic). The hosted model produces fresh replies; pupils compare answers with the separate possible source line and test unknown facts. Remind pupils that context does not retrain model weights. Personal free ZeroGPU hosting requires eligibility and has queue/daily quotas; local model downloads need a capable computer. Do not encourage public sharing of private personal information.

The Lesson 06 app and deployment guide are now **English-only**. Clone the entire repository with the standard `git clone` command; see the full guide.

### Lesson 01 and 05 activity update

**Lesson 01:** Click **Change punctuation** after the first exploration. Ask which classroom piece changed and whether the original sentence can be reconstructed. No token-count guessing.

**Lesson 05:** Show the ball/bag sentence. Select **too small** then **too big** and read the actual calculated percentages for the two objects. The classroom size rule is deliberately programmed, not learned. Next, let teachers enter any short sentence and explore its computed numerical patterns; do not interpret the largest bar as proof of meaning.
