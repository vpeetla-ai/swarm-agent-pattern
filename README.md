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

The default demo uses deterministic swarm agents, so it runs without external API keys.

For local setup, environment variables, LLM API keys, database configuration, and production adapter guidance, see [docs/LOCAL_DEVELOPMENT.md](docs/LOCAL_DEVELOPMENT.md).

Create your local secret file from:

```bash
cp .env.example .env
```
