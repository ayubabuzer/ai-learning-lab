# AI Learning Lab — Teacher guide

**Approach:** Explain with familiar words before introducing terms such as token, attention, training, context, tool calling and agent. Each lesson has **a simple question → one example or genuine experiment → a meaningful change → a discovery → a link forward**. Not every visual needs to execute a model; explicitly distinguish real calculations from guided illustrations. Lessons 01–05 are bilingual. The real Digital Twin remains English-only.

## Lesson 01 — Text, tokens and patterns (15–20 min)

Type a short message. The page illustrates small text pieces, stable teaching IDs and one example vector; finish with the related-word map preview. Ask: *is a token ID the meaning of a word?* (No.) These are simplified representations, not a real model tokenizer. No Unicode detour is needed.

## Lesson 02 — Word relationships and context (20 min)

Choose cat/dog, cat/car and car/bus. Learners observe the line and example percentage change together, or click map dots to compare other prepared words. The score is a **distance on an invented 2D classroom map**, not model-derived semantic similarity. Then use the bank experiment to compare a riverbank with a financial bank; ask which surrounding words provide the clues. Finish with the side-by-side ball/bag examples to show how one adjective changes the likely reference. The king/queen vector equation is taught once in Lesson 01. Do not call the illustrations real attention weights.

## Lesson 03 — Teach, test, retrain, then challenge (25 min)

**Training comes first.** Learners write sentences; click **Teach the mini AI**; predict the next word; inspect the actual matching examples and computed frequencies. Then edit the corpus, teach again, and compare. Finally, optionally try the moon example: start with one *rock* continuation, add repeated *cheese* examples, retrain, and see how misleading data affects the prediction. Make explicit: this is an accurate **counting model**, not neural-network training, and frequency is not truth. Let learners substitute any examples.

## Lesson 04 — How does AI remember? (20 min)

Students choose a fact type and type any value, then add it to the guided chat. They select a supported question and see the simulated reply. They clear the context without clearing the visible transcript and ask the *same* question again; now the local demonstration responds that the fact is unknown. Explain that the browser uses a restricted, rule-based teaching example, not a live LLM or permanent memory.

## Lesson 05 — Tools and agents (20–25 min)

Show that developers describe available tools and their expected inputs. Ask a weather question, a search question and `what is 5 x 2`; enable or disable tools to show the difference. The calculator evaluates the arithmetic input; weather and search responses are hypothetical. Play **both** automatic agent scenarios (picnic and budget headphones) and reset them. Teach the decision loop: goal → decide → use tool → observe → continue or stop. This is a scripted visualisation, not live autonomy. Tools need permissions and appropriate human oversight.

## Lesson 06 — Real Digital Twin (30–45 min plus optional setup)

Edit fictional `about-me.txt`, then `uv run app.py` on suitable hardware or publish using eligible Hugging Face ZeroGPU (model downloads and quotas apply). Use the complete [English-only setup, account, token and Gradio deployment guide](lessons/06-digital-twin/gradio-app/README.md); clone **the whole repository** with ordinary `git clone`. Students test supported and unsupported facts, note possible hallucinations and discuss why this is a chatbot rather than an autonomous agent. Never include private learner details or publish access tokens.

**Classroom safety:** Keep personal information fictional, distinguish actual computations from illustrative stories, and check internet and hardware limitations before teaching. All website files remain in the same six canonical lesson folders.

**Version 6:** Lesson 4 uses draggable or clickable prepared fact cards; Lesson 5 uses prepared tool questions and a simulated agent that pauses between steps. Do not describe these as live AI in the browser.
