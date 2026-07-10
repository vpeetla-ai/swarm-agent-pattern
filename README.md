# Swarm Agent Pattern


<!-- vpeetla-tech-stack:start -->
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square)]() [![Curriculum stub](https://img.shields.io/badge/Curriculum-stub-0EA5E9?style=flat-square)]() [![asyncio](https://img.shields.io/badge/asyncio-3776AB?style=flat-square)]() [![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square)]()
<!-- vpeetla-tech-stack:end -->
**Curriculum teaching stub for Swarm parallelism** — parallel specialist exploration. Pattern used in **VAP parallel asyncio bundles**.

[▶ Live demo](https://swarm-agent-pattern.vercel.app) · [Architecture](docs/ARCHITECTURE.md) · [Portfolio](https://venkat-ai.com/work) · [VAP case study](https://github.com/vpeetla-ai/ai-architecture-portfolio/blob/main/case-studies/venkat-ai-platform.md)

## What this is

Parallel autonomous agents with handoff-friendly boundaries — explore breadth before merge.

## How we solve it

Async specialist fan-out with orchestrator merge and live trace visualization.

## Case study & tradeoffs

[venkat-ai.com/work](https://venkat-ai.com/work) · [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

Org skills: [vpeetla-ai-skills](https://github.com/vpeetla-ai/vpeetla-ai-skills). This repo includes `.cursor/skills/`, `AGENTS.md`, and `CONTEXT.md`.

```bash
git clone https://github.com/vpeetla-ai/vpeetla-ai-skills.git
./vpeetla-ai-skills/scripts/install.sh --cursor --codex --project .
```

---


> **Scope:** Curriculum stub with deterministic tests and a live trace viewer — not a production agent fleet. Compose into [Venkat AI Platform](https://github.com/vpeetla-ai/venkat-ai-platform) for governed graphs.

## Implementation status

| Component | Status | Notes |
|-----------|--------|-------|
| Pattern demo + trace UI | ✅ | Live Vercel demo |
| Core agent loop | ✅ | Reference implementation |
| LangGraph production graph | 🟡 | Teaching scope — compose into VAP for fleet use |
| MCP tool bridge | ❌ | See LoopForge / VAP MCP docs |
| AegisAI gateway | ❌ | No side effects in pattern demo |
| Pytest regression | ✅ | `pytest -q` in repo |


[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://swarm-agent-pattern.vercel.app)
[![Part of Curriculum Agent Patterns](https://img.shields.io/badge/series-Curriculum%20Agent%20Patterns-purple)](https://github.com/vpeetla-ai/swarm-agent-pattern)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Part 5 of 5** in the [Curriculum Agent Patterns](https://github.com/vpeetla-ai/react-agent-pattern) series.

Curriculum teaching stub (compose into VAP for production graphs) of the **Swarm** pattern — parallel autonomous agents with coordination, aggregation, and conflict resolution.

| # | Pattern | Repository | Use when |
|---|---------|------------|----------|
| 1 | ReAct | [react-agent-pattern](https://github.com/vpeetla-ai/react-agent-pattern) | Tool use + reasoning loops |
| 2 | Reflection | [reflection-agent-pattern](https://github.com/vpeetla-ai/reflection-agent-pattern) | Self-critique and improve output |
| 3 | Plan-Execute | [plan-execute-agent-pattern](https://github.com/vpeetla-ai/plan-execute-agent-pattern) | Decompose goals into steps |
| 4 | Multi-Agent | [multi-agent-system-pattern](https://github.com/vpeetla-ai/multi-agent-system-pattern) | Specialized role delegation |
| 5 | **Swarm** | **this repo** | Parallel autonomous agents |

[▶ Live demo](https://swarm-agent-pattern.vercel.app) · [📖 Full series roadmap](https://github.com/vpeetla-ai/ai-content-factory/blob/main/docs/agent-patterns/ROADMAP.md) · [Compose in production — AI Content Factory (separate repo)](https://ai-content-factory-iota.vercel.app)

---

## What you'll learn

- Spawn **parallel workers** on subtasks
- Coordinate results without central bottleneck
- Handle duplicate/conflicting outputs
- Cost and concurrency guardrails for production

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m swarm_agent_pattern
pytest
```

Runs without external API keys using deterministic stubs.

```bash
cp .env.example .env
```

See [docs/LOCAL_DEVELOPMENT.md](docs/LOCAL_DEVELOPMENT.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Series complete?

You now have all five curriculum stubs. Compose them in the **separate** **[AI Content Factory](https://github.com/vpeetla-ai/ai-content-factory)** repo — research RAG, parallel enrich, HITL gate, multi-platform publish.

[▶ Live demo](https://ai-content-factory-iota.vercel.app)

## Related

- **Previous:** [Multi-Agent System Pattern](https://github.com/vpeetla-ai/multi-agent-system-pattern)
- **Enterprise RAG:** [enterprise_rag_platform](https://github.com/vpeetla-ai/enterprise_rag_platform)

⭐ Star the repo — and the full [series](https://github.com/vpeetla-ai) — if this helped.
