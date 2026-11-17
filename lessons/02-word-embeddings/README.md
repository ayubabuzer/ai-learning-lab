# Lesson 02 — How Does AI Connect Words?

[العربية](README.ar.md) · [Interactive lesson](index.html) · [Learning path](../../index.html)

## The question

How can numbers help a computer notice that words may be related?

## Short explanation for learners

Words that appear in similar situations may have something in common. In this lesson, the computer reads your example sentences and counts the other words each word appears beside. For every word it makes a **vector** — a list of numbers. We can compare those lists and show the results on a map.

This is a small **word co-occurrence classroom model**, not a pretrained language model or Qwen embeddings. Its numerical results are calculated from your examples, and they can change when you edit those examples. It doesn't prove the words have the same meaning.

## Input → experiment → output

- **Input:** Any two words that appear in your editable sentences; the starter pairs are `cat/dog`, `cat/banana`, and `apple/banana`.
- **Run:** Click **Compare words**, inspect the actual counts for context-clue words, and explore the calculated map and nearest neighbours.
- **Change:** Edit or add a sentence in the **Example sentences** box, click **Rebuild word map**, and compare the score before and after.
- **Output:** A numerical shared-context similarity score, sample dimensions from each context vector, a two-dimensional approximate projection and closest words from the available vocabulary.
- **Unknown input:** If your word does not appear in the examples, the page explains that you need to add a sentence using it. The model does not invent results.

For a memorable example, the page includes a **static** calculation: `king [3,3] − man [1,3] + woman [1,1] = queen [3,1]`. These numbers are **invented only for teaching**; not output from Qwen or a pretrained embedding model. An LLM's next-token prediction is not simply finding the closest word vector.

## Three challenges

1. Compare `cat/dog` and `cat/banana`. Why do the scores differ?
2. Add a sentence containing `cat` and `banana`, rebuild the map and inspect the new result.
3. Enter `unicorn` or another absent word. Add two useful sentences containing it and rebuild.

## Teachers

A 25-minute classroom game with preparation, discussion questions and misconceptions appears in [TEACHERS.md](../../TEACHERS.md). The Arabic guide provides Arabic activities, not translated English-only examples.

## Technical and privacy notes

This page is self-contained HTML/CSS/JavaScript, works without external scripts or API keys, and runs offline after download. It creates bag-of-context co-occurrence vectors from each line of learner-supplied text, compares them with cosine similarity, and displays an approximate two-dimensional projection. It does **not** run the Qwen model, retrieve pretrained embeddings, or process prompts through a chatbot. Avoid entering pupils' personal data. The next lesson covers context and next-token prediction.
