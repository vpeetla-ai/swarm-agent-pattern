# Swarm Agent Pattern

Production-grade reference implementation of a decentralized swarm architecture using agent proposals, peer scoring, shared blackboard state, and convergence rules.

## Highlights

- No central planner decides every action.
- Agents publish proposals to a shared blackboard.
- Peer scoring selects the most useful contributions.
- Convergence policy prevents endless autonomous chatter.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m swarm_agent_pattern
pytest
```

