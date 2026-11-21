# AI Learning Lab — Version 5 validation report

The release was checked against the updated lesson designs.

- **21 dependency-free structural tests:** passed (`python -m unittest discover -s tests -v`).
- **Playwright/Chromium interaction smoke checks:** passed on 1280px desktop and 390px mobile (`python tests/browser_smoke.py` in the validation environment). These verified page errors, horizontal overflow, Lesson 1 editability, Lesson 2 selected pair and score changes, Lesson 4 fact recall and clear-context behaviour, Lesson 5 `5 x 2`, two agent scenarios and reset.
- **Language audit:** English pages had no visible Arabic text apart from intentionally Arabic language-toggle labels. English and Arabic Lesson 2 controls were checked for consistent map scores.
- **Hugging Face Space deployment:** not executed in a real account; `deploy.py` continues using the safe five-file allowlist and requests ZeroGPU. Account eligibility and remote build behaviour remain external dependencies.

The word map in Lesson 2 is a **curated 2D teaching illustration**, not measured pretrained embeddings. The guided Lesson 4 chat is rule-based and does not run an LLM. Lesson 5 weather/search data and agent plans are explicitly illustrative. Lesson 3 retains its browser-only prediction experiment.

Automated tests and screenshots do not establish full usability or accessibility certification on every device; classroom testing remains recommended.
