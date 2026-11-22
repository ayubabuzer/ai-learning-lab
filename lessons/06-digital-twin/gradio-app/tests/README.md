# Fast Digital Twin tests

Run from the `gradio-app` folder without downloading model weights:

```bash
python -m unittest discover -s tests -v
```

The suite tests helper functions, the GPU-decorated Gradio handler with a mocked model, and the Transformers 5 `BatchEncoding` return contract. It does **not** download Qwen weights or execute a live ZeroGPU request. Test the deployed Space after publishing changes.
