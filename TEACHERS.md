# AI Learning Lab — Teacher guide (English)

Six connected lessons for pupils, including beginners and younger learners. Use fictional text. Each page is bilingual, browser-based and designed for ordinary school computers. Lessons 01–06 use **small teaching algorithms**, not pretrained Qwen. For deeper explanations see each lesson's README.

## Lesson 01 — Text pieces (20 minutes)

Pupils type and change English words, punctuation and emojis. Click pieces and inspect classroom IDs. Ask whether those local IDs are genuine Qwen tokenizer IDs (**no**). In Arabic mode, use the corresponding Arabic examples. Leave UTF-8 byte/hex representations out of the beginner activity.

## Lesson 02 — Context vectors (25 minutes)

Compare `cat`/`dog` and `cat`/`banana`; edit the example sentences and rebuild. Ask why a similarity score changed. Point to the **separate illustrative** king/man/woman/queen axes map and perform `[3,1] − [1,1] + [1,3] = [3,3]`. Explain that the numbers are invented, and real embeddings are more complex.

## Lesson 03 — Prediction detectives (25 minutes)

Ask pupils what might follow `The cat drinks`. Show the example sentences, predict the bars, then add `The cat drinks water` and click **Teach**. Explain *learned patterns* using books, websites, stories, articles and other written material as examples of large training corpora. Our classroom counts are not an LLM. Ask why a new sentence starter changes the result and show the matching evidence sentences.

## Lesson 04 — Context versus memory (20 minutes)

Invent a planet, character or robot in the context box; ask any question. Toggle **Include context** off, then on. Discuss what is visible in the received-input panel, and what happens when a fresh session starts. The mini reader quotes a likely related sentence, **not a generated answer**. Distinguish permanent model weights, temporary input and app storage.

## Lesson 05 — Finding evidence (20–25 minutes)

Show a sentence using `researcher` and ask about a `scientist`. Compare keyword search against small concept-aware vector matching. Change a document and see if the retrieved source changes. Explain that this is a transparent **mini vocabulary bridge**, not a neural semantic model. Retrieval is not the same as prediction or proof of truth.

## Lesson 06 — Fictional digital twin (30–40 minutes)

Each team invents a robot/planet/persona and writes one fact per line. They ask supported and unsupported questions, check line-number citations and get the text file ready for the optional Gradio project. Never publish pupils' real names, addresses, personal stories or contact details. Hosting outside the browser processes visitor input remotely; treat it differently from local browser input.

## Group discussion

After each experiment, ask: What changed? What calculation did the app really perform? What could it **not** know? How would a fully trained language model differ?

## Device and access notes

The browser lessons need only a modern browser with JavaScript. No account, full-model download, GPU or API service. Gradio is a separate **optional developer activity** requiring Python and the package installation. Test the website on school computers and check the live Pages links after deployment.
