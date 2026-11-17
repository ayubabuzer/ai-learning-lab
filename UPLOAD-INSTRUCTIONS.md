# Upload Lesson 01 to GitHub Pages

1. Back up your existing GitHub repository before replacing files. This package was built from the previous AI Learning Lab release files, **not** from a verified snapshot of the latest live repository; preserve any newer changes you made.
2. Upload the **contents** of this ZIP to the repository root on `main`. Keep the existing `LICENSE` and any other files you added yourself.
3. Retain the folder structure exactly, especially `lessons/01-how-ai-reads-words/index.html`, `README.md` and `README.ar.md`. Existing experiments are included only to avoid breaking previous links.
4. Commit: `feat(lesson-01): launch bilingual real-tokenizer playground and teacher guide`.
5. Wait for GitHub Pages deployment, then visit `https://ayubabuzer.github.io/ai-learning-lab/lessons/01-how-ai-reads-words/`.
6. Test English/Arabic switching, free input, guess, model tokenizer, byte mode, clickable IDs, teacher guide, and phone width. The real-model option needs network/CDN access on the learner device for first load.

The initial download of tokenizer libraries/files is free but can fail on filtered school networks. In that case use the offline byte mode, clearly marked as a different tokenizer.


For this revision, the real tokenizer was changed to **Qwen3 0.6B**. Test it on the deployed page with one English example and one Arabic example before classroom use. The first visit needs internet access to download tokenizer files. Do not upload API keys.
