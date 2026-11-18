# Lesson 04 — Does AI Really Remember?

[Open lesson](index.html) · [العربية](README.ar.md) · [Homepage](../../)

**Concept:** A model's trained weights, temporary conversation context, and information saved by an app are three different things.

**Try it:** Write arbitrary facts and ask any question. Toggle **Include this text with my question**; look at the exact text shown in the received-input panel. Click **Start a fresh session** to clear the demo history and reset the example.

**Model honesty:** This version is an **extractive mini-reader**, not a language model. It searches the context for sentences sharing important words with the question and quotes a matching sentence, or reports insufficient information. It does not learn the context into permanent model weights, or automatically store it online. Exact matches are not proof that a full answer was found.

## Classroom tasks

1. Predict the output before clicking the experiment button.
2. Change one input at a time and record what changes.
3. Explain what the miniature model computes and what it cannot do.

**Technical requirement:** Modern browser with JavaScript. No API keys, full-model downloads or student accounts.
