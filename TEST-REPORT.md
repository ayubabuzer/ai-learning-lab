## Version 7 validation

- 26/26 structural and documentation tests passed.
- JavaScript syntax checks passed for the homepage and all six lesson pages.
- Targeted Chromium desktop (1280 px) and mobile (390 px) checks passed for the homepage, Lesson 01, Lesson 03 (including Arabic translation), Lesson 04 context clearing and Lesson 05 calculator tool activity.
- A static screenshot of the new Lesson 03 explanatory panel was visually reviewed.
- Direct browser navigation to local HTTP URLs was blocked in this environment; cross-page language persistence was checked in source but must also be verified on the hosted site.
- This release did not perform a live Hugging Face deployment or GPU inference run.

# AI Learning Lab — Version 6.3 regression validation

- Diagnosed the reported live Space exception at `app.py:_inputs`: Transformers 5 returns `BatchEncoding`, not a bare tensor. Confirmed in the official Transformers v5 migration guide.
- Changed token preparation to use `return_dict=True` and `encoded["input_ids"]`, passing all supported model inputs as named arguments.
- **25/25** course structure tests passed.
- **11/11** Digital Twin tests passed (including a Transformers 5 `BatchEncoding`-shaped mock, an attention-mask assertion, and an AST contract test that runs on lighter CI runners).
- `app.py`, `deploy.py`, `space_compat.py`, and `twin_core.py` compile; the offline Space dependency compatibility check passed.
- **Not verified:** a full model inference request on an actual Hugging Face ZeroGPU device, and the Space UI after uploading this fix.

---

# AI Learning Lab — Version 6.2 validation

- **25/25** course structure/unit tests passed.
- **9/9** Digital Twin unit tests passed, including a fast mocked-model Gradio integration check. If Gradio/PyTorch are missing on CI, the dependency-free AST registration check still runs and the heavyweight UI tests skip.
- Real Gradio 6.x `/chat` API response verified with a mocked model; model weights were not downloaded.
- `app.py`, `deploy.py`, `twin_core.py` and `space_compat.py` pass Python compilation, and the compatibility matrix passes the offline configuration check.
- Strict Space deployment allowlist remains five files; `.venv`, private data and tests are excluded.
- **Unverified:** live ZeroGPU inference in the owner's Hugging Face Space, on-device desktop/mobile visual screenshots (browser policy blocks opening localhost), external build/package resolution and service quotas. Ask for the actual Space Runtime Logs if the new deploy still fails.

---

# AI Learning Lab — Version 6.1 validation

- Structural/unit tests: 25 course checks + 4 Digital Twin core tests passed.
- Browser smoke: Playwright/Chromium passed at desktop 1280px and mobile 390px. Checked interactive word cards, word-map updates, drag/drop and click-to-add memory facts, context clearing, prepared tool questions, 31 calculator parser cases, 240 seeded arithmetic comparisons, both agent scenarios (desktop), agent reset and mobile overflow.
- Seven lesson/homepage embedded JavaScript syntax checks passed using Node `--check`.
- Deployment script and offline compatibility preflight passed `py_compile` / `space_compat.py`. Preflight also passes with `.python-version` absent, and rejects explicit 3.11 mismatches.
- Deployment allowlist remains five files; staged Space README now pins Python 3.12 and Gradio 6.32.0.
- **Not verified:** live Hugging Face build/inference, remote package resolver (`uv pip compile` runs in GitHub Actions), classroom-device accessibility and all possible browsers. Do not claim these are certified without a real release deployment.

Lesson 2 map and percentage are illustrative teaching examples, not pretrained model measurements. Lesson 4 and Lesson 5 interactions are guided simulations, not a real hosted LLM.
