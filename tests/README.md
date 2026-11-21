# Checks for the AI Learning Lab release

From the project root:

```bash
python -m unittest discover -s tests -v
python -m unittest discover -s lessons/06-digital-twin/gradio-app/tests -v
```

The first suite verifies the six canonical lesson folders, English/Arabic learner guides for Lessons 01–05, the English-only real-model Digital Twin, internal links, word-vector illustration, real Lesson 01 punctuation control, Lesson 03 training-then-challenge structure, Lesson 04 growing-memory UI, Lesson 05 tool/workflow/agent story, full-project clone commands, and deployment guidance. The second suite tests small Digital Twin helper functions without downloading a model.

JavaScript syntax and browser interaction tests were executed separately. Browser testing uses in-memory HTML because local URL navigation was blocked in the test environment. The full outcomes and limitations are in [the release test report](../TEST-REPORT.md).
