# Lesson 01 — How Does AI Read Our Words?

[Open lesson](index.html) · [العربية](README.ar.md) · [Teacher guide](../../TEACHERS.md)

## Discover

AI language systems do not directly work with written sentences. Their tokenizer turns text into pieces called **tokens**, and each token has an **ID**. Try English, Arabic, punctuation and emoji. Explore what changes when you edit your sentence.

## Try it yourself

1. Enter any sentence (avoid private information).
2. Click **Reveal real tokens** and examine the readable pieces.
3. Choose **Explore byte tokens (offline)** to compare a different method, if useful.
4. Click a coloured piece to see one or more original token IDs.
5. Change one letter, a space, or the language; run again and explain the difference.

## What is real?

- The pretrained mode loads the *actual* tokenizer for `Qwen/Qwen3-0.6B` in your browser through Transformers.js. It loads tokenizer files; **it does not run a language model or predict text**. Internet is needed initially.
- The offline mode genuinely encodes UTF‑8 bytes (IDs 0–255). It is an educational alternative, **not** an LLM vocabulary or embedding.
- Token IDs are vocabulary indexes, **not embeddings or distances**. Lesson 02 will cover numerical vectors and similarity.

## Challenge and reflection

**Explorer:** find text that has more tokens than words. **Builder:** compare equivalent English and Arabic texts. **Innovator:** compare Qwen and byte tokenisation and explain the difference. Discuss what surprised you.

## Classroom

Open the **Teacher’s guide** panel in the page or read [TEACHERS.md](../../TEACHERS.md) for a 25-minute group activity.

## Technical notes

Static GitHub Pages HTML, JavaScript and CSS. No account, paid inference, API key or personal data upload. External CDN and pretrained tokenizer files require network access; offline byte mode works without those dependencies. User input is processed locally and not uploaded by our code. External dependencies are subject to their own licensing and hosting terms.


**Arabic display fix:** Real Qwen byte-level BPE token IDs are preserved. Adjacent token IDs may be grouped into readable Unicode spans, so a displayed piece is not necessarily a single token. The inspector shows every original ID. Arabic layouts use RTL, and byte mode decodes valid UTF-8 sequences for display.
