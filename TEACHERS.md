# AI Learning Lab — Teacher guide

**Approach:** Explain with familiar words before introducing terms such as token, attention, training, context, tool calling and agent. Each lesson has **a simple question → one example or genuine experiment → a meaningful change → a discovery → a link forward**. Not every visual needs to execute a model; explicitly distinguish real calculations from guided illustrations. Lessons 01–05 are bilingual. The real Digital Twin remains English-only.

## Lesson 01 — Words become numbers (15–20 min)

Ask what a computer receives when someone types a message. Learners type **any text**, explore the simplified text pieces, then click a piece to see its **real Unicode character numbers**. Try punctuation and Arabic/English characters. A repeated character has the same Unicode number. These are not pretrained model token IDs. Briefly show the full journey: text → model-specific tokens → learned numerical representations → generated response. No bytes or formulas required.

## Lesson 02 — Word relationships and attention (20–25 min)

Compare two words appearing in the editable example text; the numerical word-context calculation is real but very limited. Add examples and rebuild the map. Then use the *ball didn't fit in the bag / too small–too big* switch to discuss changing interpretations. Only **after** discussing the idea, introduce **attention** as a learned information-mixing mechanism. The guided pronoun story contains **no** model-derived percentages or real inference. The king–queen axes example uses invented values, clearly marked.

## Lesson 03 — Teach, test, retrain, then challenge (25 min)

**Training comes first.** Learners write sentences; click **Teach the mini AI**; predict the next word; inspect the actual matching examples and computed frequencies. Then edit the corpus, teach again, and compare. Finally, optionally try the moon example: start with one *rock* continuation, add repeated *cheese* examples, retrain, and see how misleading data affects the prediction. Make explicit: this is an accurate **counting model**, not neural-network training, and frequency is not truth. Let learners substitute any examples.

## Lesson 04 — How does AI remember? (20 min)

Add a fictional fact to the message history and then a follow-up question. Observe the **real assembled input**. Add any messages, delete the earlier fact, switch off history, or reduce the practice word limit. Ask what information would reach a future model call. The page does **not** run an LLM or generate arbitrary answers. Conversation history is temporary input, not permanent model training. A real LLM context window is based on tokens, not the lesson's teaching word limit.

## Lesson 05 — Tools, workflows and agents (20–25 min)

Use the guided outdoors-day or library story. Step through request → tool descriptions → model requests tool → application executes → result returned → answer. Ask **who actually runs the tool** (the application). Compare **Workflow** (predefined paths, potentially with branches) and **Agent** (model can choose further actions and repeat *decide → act → check* until a goal, limit or human approval). Nothing here contacts a live service or executes a model. A workflow may be preferable; agency also introduces permission and safety requirements. Sources: [Anthropic — Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), [OpenAI — Function calling](https://developers.openai.com/api/docs/guides/function-calling).

## Lesson 06 — Real Digital Twin (30–45 min plus optional setup)

Edit fictional `about-me.txt`, then `uv run app.py` on suitable hardware or publish using eligible Hugging Face ZeroGPU (model downloads and quotas apply). Use the complete [English-only setup, account, token and Gradio deployment guide](lessons/06-digital-twin/gradio-app/README.md); clone **the whole repository** with ordinary `git clone`. Students test supported and unsupported facts, note possible hallucinations and discuss why this is a chatbot rather than an autonomous agent. Never include private learner details or publish access tokens.

**Classroom safety:** Keep personal information fictional, distinguish actual computations from illustrative stories, and check internet and hardware limitations before teaching. All website files remain in the same six canonical lesson folders.
