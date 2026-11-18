# Release tests

Run `python -m unittest discover -s tests -v` from the repository root to check the canonical folder structure, documentation, static links, Python source validity and model-honesty statements. Python 3.10+ is sufficient for these structure checks; no Gradio installation is needed.

The fuller local browser checks described in `../TEST-REPORT.md` were run separately in Chromium. They included English/Arabic input, probabilities, context toggling, search results, source citations, abstentions and mobile width. Those live browser checks are not covered by this dependency-free structural suite.

Always confirm the six live GitHub Pages links after uploading.
