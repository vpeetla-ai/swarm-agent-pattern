# Local Development Guide

## Current Runtime Behavior

This repo runs locally without LLM, database, or event-stream credentials. The default swarm uses deterministic agents:

- `ExplorationAgent`
- `RiskAgent`
- `SynthesisAgent`

Agents publish proposals to a shared `Blackboard`. The runtime accepts or rejects proposals and stops when convergence is reached or the round budget is exhausted.

## 1. Setup

```bash
cd /Users/lakshmipraveenabodempudi/swarm-agent-pattern
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 2. Run Locally

```bash
python -m swarm_agent_pattern
```

No-key smoke run:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m swarm_agent_pattern
```

Expected behavior:

- Agents inspect the blackboard.
- Agents publish proposals.
- Proposals above threshold are accepted.
- Runtime reaches convergence.
- A swarm consensus answer is printed.

## 3. Run Tests

```bash
pytest
```

## 4. Environment Variables

Create a local `.env`:

```bash
cp .env.example .env
```

Important variables:

| Variable | Purpose |
| --- | --- |
| `EXPLORATION_AGENT_MODEL` | Model for exploration proposals |
| `RISK_AGENT_MODEL` | Model for risk proposals |
| `SYNTHESIS_AGENT_MODEL` | Model for final consensus |
| `SAFETY_MONITOR_MODEL` | Optional safety veto model |
| `BLACKBOARD_STORE_URL` | Durable blackboard state |
| `EVENT_STREAM_URL` | Pub/sub or event bus for async swarms |
| `SWARM_ACCEPTANCE_THRESHOLD` | Minimum proposal score |
| `SWARM_MAX_ROUNDS` | Hard autonomy budget |
| `SWARM_CONVERGENCE_TARGET` | Number of distinct accepted agents required |
| `ENABLE_SAFETY_VETO` | Allow safety monitor to reject proposals |

## 5. Where To Add Real LLM Support

Add model-backed swarm agents in:

```text
src/swarm_agent_pattern/agents.py
```

Each production swarm agent should:

- Have a stable identity.
- Read from the blackboard.
- Publish structured proposals.
- Include evidence and confidence.
- Respect cost and rate limits.

The runtime control plane is:

```text
src/swarm_agent_pattern/swarm.py
```

Keep convergence, round limits, cost budgets, and safety interrupts there.

## 6. Where To Add Database or Event Stream Support

The blackboard is defined in:

```text
src/swarm_agent_pattern/blackboard.py
```

Recommended persisted entities:

- `swarm_boards`
- `swarm_proposals`
- `proposal_scores`
- `safety_vetoes`
- `round_events`
- `agent_reputation`

For real-time systems, store every blackboard update as an event and let agents subscribe through an event stream.

## 7. Production Readiness Checks

- Hard round, time, and cost budgets exist.
- Safety veto can interrupt unsafe convergence.
- Blackboard is append-only and auditable.
- Non-convergence has a fallback.
- Agent identities and permissions are enforced.
- Proposal quality improves or the swarm stops.

