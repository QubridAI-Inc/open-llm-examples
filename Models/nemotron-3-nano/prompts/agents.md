# Agent & Tool-Use Prompts

These prompts evaluate agent-style reasoning,
planning, and tool awareness.

---

## Prompt 1: Agent Planning with Tools

### Prompt
You are an AI agent with access to the following tools:
- Web search
- Calculator
- Database query tool

Explain step by step how you would answer the question:

"What was the average revenue growth of top SaaS companies in 2023?"

Do not make up numbers.
Clearly state when a tool would be used and why.

### Model
NVIDIA Nemotron 3 Nano 30B-A3B

### Settings
- Temperature: 0.2
- Max Tokens: 1200

### Expected Behavior
- Explicit planning
- Correct tool usage decisions
- No hallucinated facts