# AI Learning Lab release checks

From the repository root run:

```bash
python -m unittest discover -s tests -v
```

This dependency-free suite checks the folder structure, bilingual docs, Previous/Next navigation, important interaction code markers, local links, Lesson 02 math/map handling, the distinct Lesson 05 evidence activity, and the Gradio app source syntax.

For optional full local development checks, install the Gradio dependencies then test its answer/source behaviour. **A real browser and device test is still necessary**: the current production package was structurally and JavaScript-syntax checked, but automated Chromium navigation was blocked by the execution environment's browser policy.

Before publishing, open all lessons in English and Arabic, try answer and unknown cases, inspect the word map on a laptop/mobile screen, and verify the live GitHub Pages site after upload.
