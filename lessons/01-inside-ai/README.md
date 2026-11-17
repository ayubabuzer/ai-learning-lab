# Lesson 01 — Inside AI: From Words to Predictions

[Open the lesson](index.html) · [العربية](README.ar.md)

**Goal:** Understand, by playing, how text can become tokens and IDs, how numerical embeddings can represent relationships, and how a language model uses context to predict what comes next.

## Explore the four stages

1. **Your sentence:** type something different, or try the cat and king buttons.
2. **Tokens and numbers:** view the pieces, their classroom IDs and illustrative number pairs.
3. **Word map:** click words, see neighbours, and explore `king − man + woman ≈ queen` on an illustrative two-dimensional map.
4. **Prediction:** edit training sentences, add an example and watch the empirical next-word probabilities change.

### Challenges

- **Explorer:** Add punctuation. Do the tokens change?
- **Builder:** Repeat one example. How does that change the probabilities?
- **Innovator:** Why should we not treat a hand-drawn word map as a real embedding?

## Accuracy and limits

The tokenizer here splits words and punctuation for teaching; genuine model tokenizers may use subwords. Token IDs in this page are assigned locally to the distinct tokens in your sentence. The two-component vectors are **illustrative numbers**, not pretrained embeddings. The word map is **hand-designed**, and the analogy is a classic *approximate* property of some word embeddings, not a universal law. The next-word algorithm counts completions after one or two words; **it is not an LLM**. Real language models compute contextual representations and probability distributions using learned network parameters.

No accounts, APIs, downloads or fees are needed. Runs entirely in the browser. The Arabic version uses its own examples and right-to-left layout. Avoid entering personal information.
