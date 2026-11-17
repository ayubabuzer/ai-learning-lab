# AI Learning Lab — Teacher's Guide

[العربية](TEACHERS.ar.md) · [Lesson 01](lessons/01-how-ai-reads-words/) · [Lesson 02](lessons/02-word-embeddings/)

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

---

## Lesson 02: How Does AI Connect Words?

**Length:** 25 minutes. **Audience:** All ages, pairs/groups. **Equipment:** Normal web browser; projector optional. **Account/network:** None required for the downloaded lesson.

**Objective:** Pupils see that words can be represented by lists of numbers describing the words that appeared around them in examples. They can compare the numerical patterns and explain how adding examples changes the outcome.

| Time | Classroom game | Teacher actions |
|---|---|---|
| 0–5 min | Which words belong together? | Ask pupils to predict whether `cat/dog` or `cat/banana` will have more context in common. Show each result. |
| 5–12 min | Find a close pair | Pairs enter words **from the example sentences**, click Compare, inspect the number table, and explore a dot on the map. |
| 12–20 min | Change the evidence | Each pair adds a sentence featuring a target word, clicks Rebuild word map and compares before/after scores. |
| 20–25 min | Explain the surprise | Invite pairs to share one result and explain which shared clue words produced it. |

**Teaching prompt:** "Why might *cat* and *dog* have similar context counts? What would happen if we only supplied sentences about cats?"

**Common misconceptions:** Similarity is **not** a probability that two words mean the same thing. This simple experiment computes co-occurrence context vectors from short editable examples; it is not Qwen and not a pretrained neural embedding model. The 2D graph is an approximate projection; the similarity score uses all context clues. The **king − man + woman ≈ queen** numbers are invented for illustration, not model output; vector arithmetic is not how a language model directly predicts its next token.

**Safeguarding:** Use fictional and classroom-safe sentences, not personal data. For Arabic, switch the interface so Arabic examples and proper RTL ordering appear.

**Exit question:** "If I add new example sentences, can the numbers change? Why?" Expected answer: yes, because the numbers are calculated from the words found together in the current examples.

---
