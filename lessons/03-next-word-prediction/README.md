# Lesson 03 — How Does AI Predict What Comes Next?

[Open lesson](index.html) · [العربية](README.ar.md) · [Homepage](../../)

**Concept:** Real language models learn patterns from many words and sentences in books, websites, stories, articles and other written material. This lesson implements an *explainable, small counting model* trained on editable examples.

**Try it:** Edit the training sentences, click **Teach the mini AI**, enter a sentence starter, click **Predict** and inspect calculated percentages. Click **Add top prediction** to continue a sentence. A list of matching examples makes the calculations traceable.

**What is calculated:** For the longest matching suffix (up to four words), the app counts next words seen within the entered example lines, without crossing line boundaries. Each displayed probability is `count(next word) / total matching next words × 100`. The model does not browse books or the web and is not Qwen. If the suffix is unknown, it tries shorter suffixes. If all are unknown, it reports no match. Punctuation is omitted in this miniature *word* predictor, not a real LLM tokenizer.

## Classroom tasks

1. Predict the output before clicking the experiment button.
2. Change one input at a time and record what changes.
3. Explain what the miniature model computes and what it cannot do.

**Technical requirement:** Modern browser with JavaScript. No API keys, full-model downloads or student accounts.
