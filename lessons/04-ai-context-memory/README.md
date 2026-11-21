# Lesson 04 — How Does AI Remember?

[العربية](README.ar.md) · [Open lesson](index.html)

**Simple question:** Why can a chatbot appear to remember something from earlier in a conversation?

**Main experiment:** Add any messages as **You** or as a sample **Assistant** reply. Watch the actual ordered conversation history accumulate. The right-hand panel displays exactly which messages would be prepared for the next model request. Turn off **Include previous messages**, remove a message, clear the chat, or reduce the small practice word limit. Observe the preview change immediately.

**Technical honesty:** The messages are actually assembled in the browser. There is **no language model** running here and the app does not generate a reply. The practice limit is in **words for clarity**, not actual model tokens. Modern chat applications often submit prior user and assistant messages as temporary context; some products may also have separate persistent memory features. The history in this page is neither model training nor permanent storage.

**Discovery:** A chatbot may appear to remember because old messages are included again. If the application omits them, the current request lacks that information.

**Next:** Lesson 05 explains how assistants can access tools beyond the conversation.
