# AI Learning Lab — Version 6.1 validation

- Structural/unit tests: 25 course checks + 4 Digital Twin core tests passed.
- Browser smoke: Playwright/Chromium passed at desktop 1280px and mobile 390px. Checked interactive word cards, word-map updates, drag/drop and click-to-add memory facts, context clearing, prepared tool questions, 31 calculator parser cases, 240 seeded arithmetic comparisons, both agent scenarios (desktop), agent reset and mobile overflow.
- Seven lesson/homepage embedded JavaScript syntax checks passed using Node `--check`.
- Deployment script and offline compatibility preflight passed `py_compile` / `space_compat.py`. Preflight also passes with `.python-version` absent, and rejects explicit 3.11 mismatches.
- Deployment allowlist remains five files; staged Space README now pins Python 3.12 and Gradio 6.32.0.
- **Not verified:** live Hugging Face build/inference, remote package resolver (`uv pip compile` runs in GitHub Actions), classroom-device accessibility and all possible browsers. Do not claim these are certified without a real release deployment.

Lesson 2 map and percentage are illustrative teaching examples, not pretrained model measurements. Lesson 4 and Lesson 5 interactions are guided simulations, not a real hosted LLM.
