# Fast Digital Twin tests

Run from the `gradio-app` folder without downloading model weights:

```bash
python -m unittest discover -s tests -v
```

These test only the deterministic helper functions. Real GPU inference and account eligibility must be tested after deployment.
