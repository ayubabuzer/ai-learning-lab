# AI Learning Lab — Teacher's Guide

[العربية](TEACHERS.ar.md) · [Lesson 01](lessons/01-how-ai-reads-words/)

## Lesson 01: How Does AI Read Our Words?

**Length:** 20 minutes. **Audience:** Mixed ages, pairs or small groups. **Equipment:** An ordinary browser, projector optional. **Internet and account:** Not required once the HTML is available.

**Learning objective:** Pupils can explain that text can be split into pieces and represented numerically, and distinguish classroom IDs from the token IDs of a real LLM.

| Time | Activity | Teacher instructions |
|---|---|---|
| 0–4 min | Show it | Enter “The cat drinks milk!” and click a piece. Ask what the local ID means. |
| 4–10 min | Change it | In pairs, change “cat” to “elephant”; compare the pieces and numbers. |
| 10–16 min | Investigate | Try English punctuation, spaces and emoji; discuss which pieces change. |
| 16–20 min | Explain it | Ask pupils to explain what a text piece is, what its classroom ID means, and why real model tokens may be different. |

### Suggested challenges

- **Change one thing:** Which IDs stay the same if a single word is replaced?
- **Sentence detectives:** Try `I love building robots!` and change one word.
- **Emoji detectives:** Add `🤖` and see whether it becomes a separate piece.

### Essential teacher notes

This lesson is **not running Qwen**. It is a lightweight teaching tokenizer using a Unicode-aware splitting rule. The lesson assigns local classroom IDs to pieces. It deliberately hides low-level byte and hexadecimal details. A real LLM uses a model-specific tokenizer and a fixed vocabulary, and may split words differently. Classroom IDs are not learned embeddings and are not Qwen token IDs. Lesson 02 will explore vectors; Lesson 03 covers prediction.

**Safeguarding:** Ask pupils to use imaginary stories, animals or fictional characters instead of personal details.

**Exit question:** “Can the numbers alone tell us the meaning of a sentence?” Expected answer: no — numerical encoding is a first step, not understanding.
