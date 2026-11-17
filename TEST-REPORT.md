# Lesson 01 lightweight release — verification report

**Tested locally on 2026-11-17.**

## Verified
- Browser JavaScript syntax for homepage and lesson.
- English text splitting and click-to-inspect local IDs.
- Decimal UTF-8 bytes for emoji text and readable Unicode output.
- Arabic interface direction (`dir=rtl`), readable Arabic, RTL piece ordering and reconstructed Arabic text.
- Changing a sentence and comparing piece counts.
- Mobile viewport 375 px without horizontal overflow.
- Homepage English/Arabic language switching and lesson description.
- No JavaScript exceptions during the automated interaction tests.

## Not claimed
- This lightweight lesson **does not run Qwen** or another pretrained LLM/tokenizer; results are from an educational text splitter and genuine UTF-8 encoding.
- No live GitHub Pages deployment has been checked in this release.
- Actual pupil device performance, screen readers and all possible browser versions have not been exhaustively tested.

## Structure verification
Only one lesson folder is included: `lessons/01-how-ai-reads-words/`. Other prototype folders are neither bundled nor removed.
