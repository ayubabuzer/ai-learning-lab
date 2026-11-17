# Lesson 02 — Local validation report

**Date:** 2026-11-17  
**Test environment:** Local Linux Chromium (`/usr/bin/chromium`) controlled through Playwright, desktop viewport 1280 × 900 and mobile viewport 375 × 820.  
**Result:** 30 / 30 automated checks passed.  
**Not tested:** The deployed GitHub Pages site and specific pupils' school computers.

## Checks completed

- English `cat/dog` yields a calculated shared-context score of **67%** for the included English examples; `cat/banana` initially yields **0%**.
- Adding two English example sentences linking `cat` and `banana`, then rebuilding, changes that score to **30%**.
- Clicking preset pairs, editing the corpus, rebuilding, resetting, inspecting the numeric vector table and displaying the word map work in Chromium.
- An unknown input (`unicorn`) receives clear guidance to add examples, rather than an invented score.
- Arabic switches the whole page to `lang=ar` and `dir=rtl`; the Arabic examples are in Arabic only. The included `القطة/الكلب` example scores **78%** with the supplied Arabic corpus.
- Unknown Arabic words receive Arabic guidance. The king/queen analogy labels switch to Arabic.
- The Arabic mobile view does not overflow horizontally at 375 px width.
- The homepage displays a working Lesson 02 link in both English and Arabic, with no captured JavaScript errors.
- The incremental package includes only the new permanent `lessons/02-word-embeddings/` folder. Lesson 01 is **not modified**.
- Root English and Arabic READMEs, teacher guides, and changelog were synchronised.

## Model disclosure

The lesson runs a **real local co-occurrence calculation** over its editable example sentences and computes cosine similarity from numeric vectors. The graph is a 2D approximate projection. This is **not** a pretrained neural embedding model, Qwen, or live LLM inference. The king–queen arithmetic uses invented teaching coordinates, explicitly marked as such.

## Deployment checklist (still to do)

1. Review root file changes against the current GitHub repository before uploading.
2. Upload the new lesson directory and root documentation/homepage updates, preserving all Lesson 01 files and your `LICENSE`.
3. After GitHub Pages deploys, open `https://ayubabuzer.github.io/ai-learning-lab/lessons/02-word-embeddings/` and check both languages, mobile behaviour, inputs, vectors, similarity and data editing.
4. Test on at least one ordinary school computer and resolve any environmental differences before declaring the lesson classroom-ready.
