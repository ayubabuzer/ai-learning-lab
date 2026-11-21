# Tests

Run the dependency-free structural suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

Optional desktop/mobile browser smoke tests use Playwright and Chromium:

```bash
python -m pip install playwright
playwright install chromium
python tests/browser_smoke.py
```

The browser suite checks critical lesson interactions and responsive overflow. These tests do not need a Hugging Face account or an API key. Browser results may vary across devices; the educational examples are not pretrained model inference.
