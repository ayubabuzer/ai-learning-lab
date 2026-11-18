# AI Learning Lab — Teacher guide

A six-lesson bilingual classroom journey for beginners. Only lightweight, explicit teaching algorithms run in pupils' browsers. The pupil UI distinguishes **✍️ input**, **⚙️ examples/settings**, **🤖 mini-robot reply**, and **📖 evidence/source**. Output starts blank until pupils take an action; a short robot animation signals the calculation.

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

## Lesson 05 · How Can We Check an AI Answer? (20–25 min)

Use the new **Fact Detectives** game. For each fictional case, pupils select the relevant source (or no source) and decide whether a claim is **supported**, **contradicted** or **not answered**. Discuss that a cited sentence can still be false; it is not automatic verification. Ask pupils to make a claim the evidence does not support. This lesson prepares them to evaluate the Digital Twin, not build another search interface.

## Lesson 06 · Build Your Own AI Digital Twin (30–40 min)

Write one imaginary fact per line. Ask **What is your name?**: the simple source-based assistant now replies **My name is Alex.** and displays the full matching `about-me.txt` line in a separate **Evidence** panel. Ask **How old are you?**: it should say **I don't know**. Other questions may return a matching sentence because this is not a generative model. Download the text file and optionally use the Gradio starter locally. Hosting to Hugging Face may require paid or specially eligible compute access.

## Safety and accessibility

Switch to Arabic for Arabic cases and RTL. Use fictional data only. A public Hugging Face Space publishes its source files and receives visitor input remotely; never upload personal information about pupils. Preview the actual GitHub Pages deployment on a school computer before class.
