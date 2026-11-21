# AI Learning Lab — Connected Learning Journey: Test Report

**Release date:** 21 November 2026

## What changed

- Lesson 01: first-step text → actual Unicode character numbers, honest simplified splitting and meaningful before/after punctuation comparison; no fake classroom IDs displayed.
- Lesson 02: existing editable word-vector model retained; added a separate guided ball/bag attention explanation, no manufactured attention weights.
- Lesson 03: teaching a real editable count-based next-word predictor is the main activity; test, change corpus, retrain, then optional misleading-data challenge. Example baseline *The moon is made of* predicts **rock 100%**; after appending three false cheese examples and retraining, calculated **cheese 75%, rock 25%**. Additional arbitrary learner-generated sentence tests passed.
- Lesson 04: editable growing conversation history, role-tagged messages, actual assembled-input preview, toggle and remove controls, and illustrative word budget. No live model.
- Lesson 05: guided tool call and workflow/agent decision-loop stories. No live tool call, weather forecast or autonomous agent claimed.
- Lesson 06: unchanged English-only Gradio model app; one explanatory bridge, full-project git clone commands retained.

## Checks executed locally

- **16 Python website/repository structural tests passed** using `python -m unittest discover -s tests -v`.
- **4 Python Digital Twin helper tests passed** using `python -m unittest discover -s lessons/06-digital-twin/gradio-app/tests -v`.
- **46 Chromium browser checks passed**, covering all seven HTML pages, click controls, bilingual toggles, custom training inputs, changing predictions, attention example changes, history assembly, tool/agent story steps, and **390 px mobile overflow**. No JavaScript page errors occurred. The checks loaded HTML with Playwright's `set_content`, since browser navigation to local URLs was blocked in the environment.
- `node --check` passed for all inline JavaScript scripts on the seven pages.
- The website test suite verifies exactly six canonical folders and valid on-disk internal links.

## Not tested / limits

- No live Hugging Face authentication, ZeroGPU Space deployment or actual Qwen model inference was performed.
- Browser screenshot verification was performed via injected HTML; a static visual browser run did **not** verify loading remote services or the original lesson 06 image over HTTP. The image file is present and checked by structural tests.
- The word-context vectors in Lesson 02 and count-based predictions in Lesson 03 are small teaching algorithms. They accept editable learner input but cannot replicate arbitrary language understanding by a pretrained model.
- The attention example in Lesson 02 and the tools/workflow/agent stories in Lesson 05 are openly labelled **guided illustrations**, not AI-executed decisions.
- The Lesson 04 practice limit counts whitespace-delimited words for clarity; actual LLM context budgets are measured in model-specific tokens.
- **The project files have not been uploaded to GitHub or published to GitHub Pages by this test run.**
