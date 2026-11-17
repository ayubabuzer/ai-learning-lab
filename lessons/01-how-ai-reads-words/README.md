# Lesson 01 — How Does AI Read Our Words?

[العربية](README.ar.md) · [Open playground](index.html) · [Teacher guide](../../TEACHERS.md)

## What is this lesson about?

Text can be separated into pieces and represented by numbers so computers can process it. This page uses a **simple classroom tokenizer** that groups letters, numbers, whitespace and symbols. The page makes local piece IDs and shows the **actual UTF-8 bytes** of each piece.

The activity **does not load or run Qwen** or any other pretrained tokenizer/LLM. Local IDs are not Qwen IDs and these are not embeddings or next-token predictions. Real AI tokenizers can use different, more sophisticated boundaries.

## Input → Output → Task

- **Input:** Any English or Arabic text, including emojis and punctuation.
- **Output:** Clickable text pieces, stable local IDs during the page session, real decimal and hex UTF-8 byte values, reconstructed original text, and before/after piece counts.
- **Task:** Change one word, try Arabic, then inspect an emoji. Explain why the numbers change.

This runs instantly in a normal browser, without internet requests, installation, API keys or model downloads. It works on GitHub Pages or as a local HTML file.

## What comes next?

Lesson 02 will explain real pretrained embeddings, word relationships and similarity on a graph. Numbers that represent characters are not the same as numerical vectors that a model learns.
