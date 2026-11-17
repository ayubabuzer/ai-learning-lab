# AI Learning Lab — Teacher's Guide

[العربية](TEACHERS.ar.md) · [Lesson 01](lessons/01-how-ai-reads-words/)

## Lesson 01: How Does AI Read Our Words? (25 minutes)

**Audience:** Mixed-age groups, pair work, no prior coding or mathematical knowledge.
**Learning goal:** Pupils can explain a token, a token ID, and why tokenisation can differ between tokenizers.

**Before class:** Open Lesson 01 on the projector. Click **Reveal real tokens** once to check that the Hugging Face tokenizer files load over your school network; first download requires internet. If blocked, use **Explore byte tokens (offline)** and explain clearly that byte tokenisation is different. Do not enter pupil names, contact details or other personal information.

| Minutes | Activity | Teacher prompt |
|---|---|---|
| 0–5 | Explore | Change one letter in a sample and ask pupils to describe the difference. |
| 5–12 | Token detectives | Pairs type English or Arabic sentences and choose **Reveal real tokens**; click pieces to see IDs. |
| 12–19 | Surprise challenge | Teams try punctuation, spaces, emojis or invented words; share the most surprising difference. |
| 19–23 | Compare | Switch the *same text* to byte mode. Ask why numbers and token counts change. |
| 23–25 | Exit ticket | Each pair explains: “A token is …; a token ID is …; an ID does not tell us …” |

### Common misconceptions

- **A token is always a whole word:** False. Some tokenizers use subwords, punctuation and other pieces.
- **A token ID is a meaning score:** False. It is an identifier in a particular tokenizer vocabulary.
- **This model understands our sentence:** Not in this activity. We load a pretrained **tokenizer**, not a language model that predicts or generates.
- **Byte mode is a backup Qwen model:** False. It shows how UTF‑8 bytes can be used as real token units without downloading a model.

### Class play ideas

**Token Detectives:** Teams change one letter, punctuation mark or emoji, then explain what changed in the real token IDs. Award points for explanations, not guesses. **Two-language detectives:** Give groups semantically similar English and Arabic sentences and compare different splits, without suggesting the languages must produce the same number of pieces. **Emoji challenge:** Explore why one visible emoji can correspond to multiple bytes.

**Assessment:** Ask pupils to explain an unexpected result and identify something they cannot infer from token IDs.

**Next lesson (planned):** How Does AI Connect Words? — embeddings and similarity, not just identifiers.


**Arabic display fix:** Real Qwen byte-level BPE token IDs are preserved. Adjacent token IDs may be grouped into readable Unicode spans, so a displayed piece is not necessarily a single token. The inspector shows every original ID. Arabic layouts use RTL, and byte mode decodes valid UTF-8 sequences for display.
