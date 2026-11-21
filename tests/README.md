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

The browser suite checks critical lesson interactions and responsive overflow. It also includes a regression matrix of 31 calculator, error-handling, and tool-routing cases (including Eastern Arabic digits), run on desktop and mobile. An additional 240 deterministic randomized calculations compare the browser parser with expected arithmetic. Unsupported natural-language phrasing is handled with an explicit explanation rather than partial arithmetic. These tests do not need a Hugging Face account or an API key. Browser results may vary across devices; the educational examples are not pretrained model inference.
