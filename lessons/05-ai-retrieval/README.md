# Lesson 05 — How Does AI Know Which Words to Look At?

**[English](README.md) · [العربية](README.ar.md)**

## The idea, in simple words

During training, a real AI model learns numerical settings to help its tokens exchange information. Attention scores tell its computation how much information comes from different positions. They do not directly show a word's meaning or prove an answer is correct.

## Try the interactive explorer (20 minutes)

1. Type any short English or Arabic sentence, or use the example in your selected language.
2. Click **Explore attention**. The blank output now shows clickable word pieces, connection lines and percentages.
3. Click a word. Compare the bar for each other word; all percentages add to 100%.
4. Change or repeat a word: the numbers and line thicknesses recalculate.
5. Switch the setting from **Similar-looking words** to **Nearby words** and compare.

**Important accuracy note:** This is a faithful demonstration of turning numerical match scores into attention weights using a **fixed, transparent teaching algorithm**. It is not running a pretrained Transformer, and the graph is not actual pretrained model attention. It uses simple character features and positions; it cannot infer which person or object a pronoun refers to. No large download, account, API key or network access is required. The output begins empty.

## Teacher activity

Ask pupils to predict which bar will change when they repeat a word. Discuss why different attention patterns can produce different links and why a strong link alone does not explain the AI's final answer.

[← Lesson 04](../04-ai-context-memory/) · [Lesson 06 →](../06-digital-twin/)
