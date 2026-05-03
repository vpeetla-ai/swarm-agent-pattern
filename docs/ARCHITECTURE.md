# Architecture Decision Record: Swarm Agent Pattern

## Context

Swarm architectures are useful when a system needs adaptive coordination rather than a fixed central plan. This appears in real-time operations, simulations, open-ended optimization, autonomous monitoring, and environments where useful work can emerge from many agents proposing, scoring, and reacting to shared state.

Swarm systems are powerful but risky. They should not be the default enterprise pattern. They require stronger observability, budgets, convergence rules, and safety boundaries than centralized orchestration.

## Decision

This repo implements a decentralized swarm with:

1. `SwarmAgent` instances that independently publish proposals.
2. `Blackboard` shared state that accepts or rejects proposals.
3. Peer-style proposal scoring represented as a score on each proposal.
4. `SwarmRuntime` that advances rounds and stops on convergence.

The runtime manages mechanical safety boundaries such as maximum rounds. It does not prescribe a central task plan. That distinction matters: in a swarm, agents adapt to the board and each other rather than executing a fixed sequence from an orchestrator.

## When To Use

Use this pattern for dynamic autonomous coordination:

- Real-time operations.
- Adaptive simulation.
- Incident exploration.
- Complex optimization.
- Open-ended problem solving.
- Multi-agent environments where no single coordinator has complete context.

Avoid it for regulated linear workflows, simple tool use, or tasks requiring deterministic approval chains.

## Runtime Flow

```text
Goal
  -> agents inspect blackboard
  -> agents publish proposals
  -> proposals are accepted or rejected
  -> agents adapt next round based on shared state
  -> runtime stops at convergence or round budget
```

## State Model

The blackboard is the primary coordination primitive. Production blackboards should include:

- Goal and operating constraints.
- Accepted and rejected proposals.
- Proposal lineage.
- Agent identity and permissions.
- Evidence, citations, and tool results.
- Environment observations.
- Safety policy decisions.

Use append-only event storage for audit. Agents can subscribe to board updates through pub/sub or consume snapshots at round boundaries.

## Guardrails

- Maximum round budget.
- Proposal acceptance threshold.
- Convergence target.
- Explicit accepted and rejected proposal stores.

Recommended production additions:

- Agent admission control.
- Rate limits per agent.
- Safety monitor agents with veto power.
- Environment sandboxing.
- Cost budget shared across the swarm.
- Drift detection when proposals stop improving.
- Human interruption controls.

## Failure Modes

- Emergent instability: agents amplify weak or unsafe ideas. Mitigation: safety monitors, acceptance thresholds, and veto policies.
- Non-convergence: agents continue proposing without useful progress. Mitigation: round budgets and improvement thresholds.
- Coordination opacity: behavior is hard to explain. Mitigation: event-sourced blackboard and proposal lineage.
- Cost runaway: many agents multiply calls. Mitigation: swarm-level budgets and adaptive throttling.
- Adversarial agents: one compromised agent pollutes shared state. Mitigation: identity, permissions, reputation, and quarantine.

## Scaling Strategy

Start with round-based synchronous coordination. Move to asynchronous pub/sub only when the environment requires real-time behavior. Use partitions for large swarms: local boards for subproblems and a higher-level board for cross-swarm synthesis.

## Success Metrics

- Convergence rate.
- Proposal acceptance ratio.
- Unique useful contributors.
- Improvement per round.
- Cost per consensus.
- Safety veto frequency.
- Human override rate.

