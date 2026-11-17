# Lesson 01 — Next Word Predictor

**English** | [العربية](README.ar.md) · [Try the lesson](https://ayubabuzer.github.io/ai-learning-lab/lessons/01-next-word/) · [Back to the lab](../../README.md)

## Goal
Understand how a tiny program predicts the next word by counting examples. This is **not** a large language model or a trained neural network.

## Start
1. Open the [interactive lesson](https://ayubabuzer.github.io/ai-learning-lab/lessons/01-next-word/).
2. Read the example sentences and guess the next word before clicking **Predict**.
3. Add or remove repeated sentences; predict again.
4. Click **Surprise me** several times and compare the outcomes.
5. Switch to **العربية** and explore the Arabic examples.

## Challenges
- **Explorer:** Predict before clicking. Change three examples and describe what happens.
- **Builder:** Make a different word the most likely next word. Explain the counts.
- **Innovator:** Test unseen prompts, punctuation and ties. Describe two limitations.

## How it works
The app finds exact sequences of words in the editable sentences. It counts the word immediately after each match, then divides each count by the total. **Surprise me** randomly samples using these frequencies. Unknown prompts return **I don’t know yet**.

## Learn and reflect
- Does repeating an example change its probability? Why?
- Does the model understand your sentence? What evidence supports your answer?
- How is this different from a modern language model that predicts tokens?

## Privacy and accessibility
Everything runs in your browser. No account, API key or personal information is needed. Use fictional examples; do not enter private data.

## Remix
Use GitHub **Use this template** if the repository is configured as a template, or fork/clone the repository. Edit `lessons/01-next-word/index.html` and publish through GitHub Pages.
