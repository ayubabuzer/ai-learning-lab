# Lesson 05 — How Does AI Use Tools and Work Towards a Goal?

[Arabic guide](README.ar.md) · [Open lesson](index.html)

**Simple question:** How does an AI assistant know which tool to use, and how can an agent take several steps toward a goal?

**Try it:** The developer supplies the names, descriptions and inputs for weather, calculator and search tools. Enable or disable them, then ask a question. The page shows the proposed tool call, the tool result and the assistant's reply. The arithmetic calculator handles inputs such as `5 x 2`, `5 × 2`, `5 * 2` and `12 + 8`. Search and weather results are intentionally fictional.

**Agent experiment:** Choose either the picnic-with-backup scenario or the budget-headphones scenario. Click **Run agent** to watch the simulated steps appear automatically. **Start again** resets the example. The agent pattern is goal → decide → act → observe → repeat or stop.

**Technical honesty:** Tool routing is rule-based on this page; it does not invoke a live LLM, real weather API or product search. The agent executions are scripted to teach the sequence, not autonomous work. Real systems must validate permissions and know when to stop or ask for human approval.

**Next:** Lesson 06 builds a real Digital Twin chatbot, not an autonomous agent.
