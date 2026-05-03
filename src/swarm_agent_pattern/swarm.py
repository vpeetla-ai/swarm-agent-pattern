from dataclasses import dataclass

from .agents import SwarmAgent
from .blackboard import Blackboard


@dataclass(frozen=True)
class SwarmResult:
    answer: str
    blackboard: Blackboard
    rounds: int


class SwarmRuntime:
    def __init__(
        self,
        agents: list[SwarmAgent],
        acceptance_threshold: float = 0.8,
        max_rounds: int = 4,
        convergence_target: int = 3,
    ) -> None:
        if max_rounds < 1:
            raise ValueError("max_rounds must be positive")
        self.agents = agents
        self.acceptance_threshold = acceptance_threshold
        self.max_rounds = max_rounds
        self.convergence_target = convergence_target

    def run(self, goal: str) -> SwarmResult:
        blackboard = Blackboard(goal=goal)
        for round_number in range(1, self.max_rounds + 1):
            for agent in self.agents:
                proposal = agent.propose(blackboard)
                blackboard.publish(proposal, self.acceptance_threshold)
            unique_agents = {proposal.agent_id for proposal in blackboard.accepted}
            if len(unique_agents) >= self.convergence_target:
                return SwarmResult(self._final_answer(blackboard), blackboard, round_number)
        return SwarmResult(self._final_answer(blackboard), blackboard, self.max_rounds)

    def _final_answer(self, blackboard: Blackboard) -> str:
        accepted = "; ".join(proposal.content for proposal in blackboard.accepted)
        return f"Swarm consensus for '{blackboard.goal}': {accepted}"

