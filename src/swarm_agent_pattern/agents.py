from dataclasses import dataclass
from typing import Protocol

from .blackboard import Blackboard, Proposal


class SwarmAgent(Protocol):
    agent_id: str

    def propose(self, blackboard: Blackboard) -> Proposal:
        """Publish a candidate contribution based on shared state."""


@dataclass
class ExplorationAgent:
    agent_id: str = "exploration"

    def propose(self, blackboard: Blackboard) -> Proposal:
        score = 0.88 if not blackboard.accepted else 0.72
        return Proposal(self.agent_id, f"Explore options for {blackboard.goal}", score)


@dataclass
class RiskAgent:
    agent_id: str = "risk"

    def propose(self, blackboard: Blackboard) -> Proposal:
        return Proposal(self.agent_id, "Identify safety, cost, and reliability risks", 0.91)


@dataclass
class SynthesisAgent:
    agent_id: str = "synthesis"

    def propose(self, blackboard: Blackboard) -> Proposal:
        readiness = len({proposal.agent_id for proposal in blackboard.accepted})
        score = 0.95 if readiness >= 2 else 0.6
        return Proposal(self.agent_id, "Synthesize accepted swarm proposals", score)

