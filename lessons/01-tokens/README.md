# Lesson 01 — How AI Reads Text: Tokens

[العربية](README.ar.md) · [Open interactive lesson](index.html)

**Goal:** See how text can be divided into pieces called tokens, without mathematics or programming.

## A simple explanation

When you type a sentence, a language model first separates the text into smaller pieces called **tokens**. These pieces can be entire words, word fragments, or punctuation. For instance, “I love AI!” can be shown as `I | love | AI | !` in our classroom demonstration. Different models may divide that sentence differently.

The point is to **see** the pieces, not memorize technical terms. You can learn by experimenting, without maths or programming.

## Try it

1. Type an English sentence.
2. Compare **Words + punctuation**, **Characters**, and **Spaces only**.
3. Predict which mode produces more pieces, then test.
4. Switch to Arabic and repeat with an Arabic sentence.

## Challenges

- **Explorer:** Include an emoji and notice what changes.
- **Builder:** Compare the same sentence using all three rules.
- **Innovator:** Explain why a real tokenizer may break an unfamiliar word into subword pieces.

## Important distinction

This is an educational text splitter, **not** a production LLM tokenizer. Actual tokenization depends on the model and may produce subword tokens, special tokens, or different handling of spaces. No data is sent to a server; the lesson runs in your browser.

Next concept (planned): token IDs. An [earlier next-word prediction experiment](../01-next-word/) is also available as an optional bonus, not a numbered lesson.
