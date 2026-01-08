# NVIDIA Nemotron 3 Nano 30B-A3B

This directory contains **real-world prompts, outputs, and API examples**
for **NVIDIA Nemotron 3 Nano 30B-A3B**, tested on **Qubrid AI**.

Nemotron 3 Nano is an open, high-performance large language model designed
for **long-context reasoning, coding, and agent workflows**.

---

## 📌 Table of Contents

- [Why Nemotron 3 Nano](#why-nemotron-3-nano)
- [Model Overview](#model-overview)
- [Folder Structure](#folder-structure)
- [How to Use These Prompts](#how-to-use-these-prompts)
- [Prompt Categories](#prompt-categories)
- [API Examples](#api-examples)
- [Comparisons](#comparisons)
- [Recommended Settings](#recommended-settings)
- [Notes & Limitations](#notes--limitations)
- [License & Disclaimer](#license--disclaimer)

---

## Why Nemotron 3 Nano

Nemotron 3 Nano 30B-A3B stands out among open LLMs because it combines:

- 🚀 **High inference speed** via Mixture-of-Experts (MoE)
- 📚 **Ultra-long context support** (up to 1M tokens)
- 🧠 **Strong reasoning and coding performance**
- 🤖 **Agent-ready architecture**
- 🔓 **Open weights suitable for commercial use**

It is particularly well-suited for:
- Retrieval-Augmented Generation (RAG)
- AI agents and tool-using systems
- Developer copilots
- Large document analysis

---

## Model Overview

| Attribute | Details |
|--------|--------|
| Model Name | NVIDIA Nemotron 3 Nano 30B-A3B |
| Architecture | Hybrid MoE + Mamba |
| Total Parameters | ~30B |
| Active Params / Token | ~3.5B |
| Max Context Length | Up to 1,000,000 tokens |
| Strengths | Reasoning, Coding, Long Context |
| Tested On | Qubrid AI |

---

## Folder Structure

nemotron-3-nano/
│
├── README.md ← You are here
│
├── prompts/
│ ├── long_context.md
│ ├── reasoning.md
│ ├── coding.md
│ └── agents.md
│
├── outputs/
│ ├── nemotron.md
│ └── qwen3.md
│
└── api/
├── python.py
└── curl.sh


---

## How to Use These Prompts

1. Open **Qubrid AI → Model Studio**
2. Select **NVIDIA Nemotron 3 Nano 30B-A3B**
3. Copy a prompt from the `prompts/` directory
4. Run it in the Playground or via API
5. Compare your results with the outputs provided

These prompts are designed to be:
- Reproducible
- Model-agnostic
- Easy to extend

---

## Prompt Categories

### 📚 Long Context
**File:** `prompts/long_context.md`  
Tests document understanding, RAG design, and memory handling.

### 🧠 Reasoning
**File:** `prompts/reasoning.md`  
Evaluates multi-step logic, decision-making, and structured thinking.

### 💻 Coding
**File:** `prompts/coding.md`  
Focuses on real-world backend and system design problems.

### 🤖 Agents
**File:** `prompts/agents.md`  
Tests planning, tool usage, and agent-style reasoning.

---

## API Examples

API examples demonstrate how to run Nemotron 3 Nano programmatically
using **Qubrid AI APIs**.

- `api/python.py` – Python inference example
- `api/curl.sh` – cURL-based API request

These examples can be adapted for:
- Backend services
- AI agents
- Internal tools

---

## Comparisons

Where relevant, outputs are compared against other models
(e.g. Qwen3 30B-A3B) to highlight strengths and limitations.

Comparison outputs live in:

outputs/
├── nemotron.md
└── qwen3.md


---

## Recommended Settings

Based on testing, we recommend:

| Use Case | Temperature | Max Tokens |
|------|-----------|------------|
| Reasoning | 0.1 – 0.3 | 1024 – 2048 |
| Coding | 0.1 | 1500+ |
| Long Context | 0.2 | 2048+ |
| Agents | 0.2 | 1200+ |

---

## Notes & Limitations

- Very long context usage may increase latency and cost
- Reasoning quality depends on sufficient token budget
- Always validate outputs in production systems

---

## License & Disclaimer

This repository is licensed under **Apache License 2.0**.

This directory contains **examples, prompts, and outputs only**.
Model weights and usage rights are governed by their respective owners
(e.g., NVIDIA). Please refer to the official model license before
production use.

---

**Maintained by Qubrid AI**  
Open models. Fast inference. Zero infrastructure.