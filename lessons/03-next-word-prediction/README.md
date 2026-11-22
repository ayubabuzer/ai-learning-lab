# Lesson 03 — How Does AI Learn to Predict?

[العربية](README.ar.md) · [Open lesson](index.html)

**Start with training, not misinformation.** Learners type arbitrary example sentences and click **Teach the mini AI**. The classroom model counts which next words follow matching sequences. This is a real, explainable calculation, but not training a neural network.

**Learn → test → change → train again:** Type a sentence starter, press **Predict**, and inspect calculated percentages and the exact supporting training examples. Change the sentences and press **Teach** again; editing by itself does not update the model. The program uses the longest matching ending of up to four words, falling back to shorter ones.

**Optional final challenge — misleading training data:** First try “The moon is made of” with the original training text, which includes one rock example. Next add repeated, deliberately false cheese examples using the editable challenge box, press **Teach**, and predict again. The resulting distribution is calculated from the actual data and demonstrates that a frequent pattern is **not a guarantee of truth**. Learners can replace every example with their own.

Real large language models learn patterns from extensive text including books, websites, articles and stories; this mini-model only counts patterns on this page.

**Next:** Lesson 04 explains how a conversation's history can be sent to a model as temporary memory.

### Where real models learn

After the mini-model experiment, a book-icon comparison explains that real language models learn patterns from very large collections of text, potentially including books, websites, articles and other writing. Training occurs before chat; the model does not ordinarily reopen those sources when answering, and learned patterns can be inaccurate.
