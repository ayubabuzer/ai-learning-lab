# Lesson 01 — How Does AI Read Our Words?

[العربية](README.ar.md) · [Open playground](index.html) · [Teacher guide](../../TEACHERS.md)

## What is this lesson about?

Text can be separated into pieces and represented by numbers so computers can process it. This page uses a **simple classroom tokenizer** that groups letters, numbers, whitespace and symbols. The page makes local classroom IDs for each piece. We omit low-level byte and hexadecimal details so learners can concentrate on the basic idea.

The activity **does not load or run a pretrained model** or any other pretrained tokenizer/LLM. Local IDs are not a pretrained model IDs and these are not embeddings or next-token predictions. Real AI tokenizers can use different, more sophisticated boundaries.

## Input → Output → Task

- **Input:** Any text, including emojis and punctuation. Suggested examples follow the chosen interface language: English in English mode and Arabic in Arabic mode.
- **Output:** Clickable text pieces, local classroom IDs for the current visit, reconstructed original text, and before/after piece counts.
- **Task:** Change one word, try another sentence in the selected language, then inspect an emoji or punctuation mark. Explain what changed.

This runs instantly in a normal browser, without internet requests, installation, API keys or model downloads. It works on GitHub Pages or as a local HTML file.

## What comes next?

Lesson 02 will explain real pretrained embeddings, word relationships and similarity on a graph. Numbers that represent characters are not the same as numerical vectors that a model learns.
