from swarm_agent_pattern import ExplorationAgent, RiskAgent, SwarmRuntime, SynthesisAgent


def test_swarm_reaches_consensus_through_blackboard() -> None:
    result = SwarmRuntime([ExplorationAgent(), RiskAgent(), SynthesisAgent()]).run(
        "Optimize incident response"
    )

    accepted_agents = {proposal.agent_id for proposal in result.blackboard.accepted}
    assert {"exploration", "risk", "synthesis"} <= accepted_agents
    assert result.rounds <= 2
    assert "Swarm consensus" in result.answer

