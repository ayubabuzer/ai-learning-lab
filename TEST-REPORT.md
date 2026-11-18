# Test report — Lessons 03–06 combined release

**Tested locally on 2026-11-17.** This report covers a static offline browser package and the optional Gradio source project. It does **not** verify that your public GitHub Pages deployment has been updated.

## Verified

- **78 checks passed**, using headless Chromium with page content loaded locally, plus static link/file tests and direct Python checks for the optional Gradio app.
- Homepage shows six interactive lesson cards, links to all six canonical folders and switches to Arabic RTL.
- Existing Lesson 01 present; no new or duplicate Lesson 01 folder.
- Lesson 02 includes the revised static 2D king/man/woman/queen axes map, shown arithmetic with invented coordinates, English/Arabic labels and the honesty note. Main existing vector comparison left in place.
- Lesson 03: genuine 66.7%/33.3% sample counts, recalculation after training changes, source lines, no-match behavior and Arabic RTL.
- Lesson 04: evidence extraction from user context, context on/off, exact input display, fresh-session clearing, Arabic RTL.
- Lesson 05: distinct results for keyword versus tiny concept-aware vector matching, arbitrary document editing, Arabic output.
- Lesson 06: quoted evidence and source line, correct refusal when an unsupported fact is asked about, Arabic example response and mobile horizontal-overflow check.
- Optional Python Gradio app: imported successfully with Gradio 6.5.1; confirmed supported, unsupported and Arabic question outputs.
- A further **6 dependency-free Python unittest structural checks passed** (`python -m unittest discover -s tests -v`). The test source is included in `tests/`.
- Node.js `node --check` verified syntax of the seven JavaScript scripts (homepage plus Lessons 01–06).
- Link targets checked for each HTML page. Exactly one directory for each of Lessons 01–06.

## Design choices and limitations

- No pretrained Qwen tokenizer, embedding model or generative LLM is running in this lightweight release. No generated percentages have been attributed to a pretrained model.
- The first five lessons use tiny illustrative or calculated algorithms; Lesson 06 uses extractive document matching. Their limitations are stated prominently in pupil and teacher content.
- Tests used the local HTML content in Chromium; real school computers and deployed GitHub Pages may behave differently. The public website still needs post-deployment checking.
- Gradio was tested as an importable app and with its answer function; no public Hugging Face Space was created or tested.
- Network behavior and platform quotas are not involved in the browser lessons.
- The root `LICENSE` isn't bundled (previous partial packages did not include it). **Keep the existing LICENSE and any unrelated repository files.**

## Reproduce

Open each `lessons/NN-.../index.html` in a modern browser or serve the folder using a basic local static HTTP server. Switch between English and Arabic and try the sample challenges. For Gradio, follow `lessons/06-digital-twin/gradio-app/README.md`.
