# Lesson 05 — How Does AI Know Which Words to Look At?

[العربية](README.ar.md) · [Open attention explorer](index.html)

## What the lesson teaches

Real Transformers learn numbers during training that help tokens exchange information. This lightweight browser experiment illustrates *how numerical matching scores become weights* without pretending to show real trained attention weights. The weights share 100% across the displayed text pieces. **They are not confidence scores or proof of meaning.**

## Main experiment: small vs big

1. Open **Try too small** and click **Explore attention** (the word “it” is selected automatically).
2. Inspect its computed classroom weights to **ball** and **bag**.
3. Select **Change to too big**. The classroom rule deliberately flips which object is favoured.
4. Compare the two columns showing both calculations and click any other word to see its general numerical pattern.
5. Type **any short English or Arabic sentence**. The calculator still recomputes numerical weights and links; it **does not guarantee meaningful referents for arbitrary text**. The small/big result comes from an intentionally written teaching rule for sentences about an item fitting in a container, not from a trained model.

The Arabic interface has its own natural ball/bag example. Other settings show similar-looking and nearby word patterns. No network, accounts, API keys or large model downloads are needed.

## Classroom discussion

What changed when “small” became “big”? Did a program invent the weights, calculate them, or learn its rules from training? Compare with a real model, whose numerical transformations are learned and far more complex.

[← Lesson 04](../04-ai-context-memory/) · [Lesson 06 →](../06-digital-twin/)
