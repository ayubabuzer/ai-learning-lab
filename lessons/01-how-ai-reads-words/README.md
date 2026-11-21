# Lesson 01 — How Does AI Read Our Words?

[العربية](README.ar.md) · [Open lesson](index.html) · [Teacher guide](../../TEACHERS.md)

**Simple question:** What happens after you send a message to AI?

**Short explanation:** Computers work with numbers. Every written character has a standard Unicode number. Language models take a further step: a *tokenizer* makes text pieces with model-specific IDs, which are turned into numerical representations. A trained language model then processes those representations to predict tokens for its answer.

**Try it:** Type **any English or Arabic text**. Explore how this classroom word splitter divides it. Click a piece to see **actual Unicode numbers** for its individual characters, not invented classroom IDs. Change punctuation to compare the pieces and inspect the difference.

**Discovery:** The same letter keeps its Unicode number, even when the sentence changes. But Unicode numbers are **not** a language model's token IDs, and neither number is a word's meaning. The colourful splitter is simplified; it is **not a pretrained AI tokenizer**.

**Next:** Lesson 02 explains how numerical patterns can capture some relationships between words and gives a guided attention example.

No internet or API key is required. This experiment does not run an LLM.
