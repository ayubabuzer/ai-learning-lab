# Lesson 01 clarity update — test report

Local tests: 2026-11-17.

## Verified

- JavaScript syntax of homepage and Lesson 01 scripts (`node --check`).
- Interactive browser tests in headless Chromium at 1280 × 900 and 375 × 812, injecting the exact HTML as a document (direct navigation was blocked in this environment).
- English-mode example buttons contain only English text; switching to Arabic shows Arabic-only example sentences and challenges, and switches the input default.
- Arabic interface `lang=ar`, `dir=rtl`, RTL token row, correct reconstruction of custom Arabic plus emoji input.
- Click-to-inspect displays classroom ID and explanation, with no piece-type, UTF-8 byte or hexadecimal output.
- Editing an English sentence and an Arabic sentence, example button selection, no JavaScript errors, no mobile horizontal overflow.
- Only one Lesson 01 folder exists within this release.

## Limitations

- This is a **classroom text splitter** with locally assigned IDs. It is not a real Qwen tokenizer or LLM, and the displayed IDs are not real Qwen IDs.
- Actual GitHub Pages deployment has not been verified in this test.
- School-managed browsers, accessibility assistive technologies and other devices may differ from our local Chromium checks.
- The ZIP must be reviewed before replacing any customized repository files.
