# Upload Lesson 01 fix

1. Back up your current repository.
2. Extract the ZIP into the root of `ai-learning-lab`, preserving folders.
3. Upload only the relevant updated files (the lesson page, root `index.html`, bilingual READMEs, teacher guides, changelog and lesson READMEs). Keep your LICENSE and existing experiments.
4. Commit: `fix(lesson-01): make Qwen Arabic tokens readable and RTL`
5. Open `https://ayubabuzer.github.io/ai-learning-lab/lessons/01-how-ai-reads-words/`. Select Arabic, try `أنا أحب تعلم الذكاء الاصطناعي! 🤖`, click Run and verify text is readable, chips flow RTL, and clicking a chip shows original IDs. Test mixed Arabic-English, punctuation, emoji and editing the input.

**Important:** The live Qwen tokenizer network load cannot be confirmed in this package build environment. Source-level and offline rendering tests are provided; verify online inference after upload.
