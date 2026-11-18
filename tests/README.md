# Tests

From the site root, run:

```bash
python -m unittest discover -s tests -v
```

To test the **Digital Twin's pure-Python message/source helpers** without downloading the model:

```bash
python -m unittest discover -s lessons/06-digital-twin/gradio-app/tests -v
```

For a full local run from `lessons/06-digital-twin/gradio-app/`, use `uv run app.py`; this downloads the open model and needs adequate memory. To publish, use `uv run gradio deploy` and enter `zero-a10g` when prompted for hardware. The full guide is in that folder.

These tests do not verify live Hugging Face Space creation or GPU inference. See the root `TEST-REPORT.md`.
