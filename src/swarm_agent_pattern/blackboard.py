from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Proposal:
    agent_id: str
    content: str
    score: float


@dataclass
class Blackboard:
    goal: str
    board_id: str = field(default_factory=lambda: str(uuid4()))
    accepted: list[Proposal] = field(default_factory=list)
    rejected: list[Proposal] = field(default_factory=list)

    def publish(self, proposal: Proposal, threshold: float) -> None:
        if proposal.score >= threshold:
            self.accepted.append(proposal)
        else:
            self.rejected.append(proposal)

