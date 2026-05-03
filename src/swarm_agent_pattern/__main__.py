from .agents import ExplorationAgent, RiskAgent, SynthesisAgent
from .swarm import SwarmRuntime


def main() -> None:
    result = SwarmRuntime([ExplorationAgent(), RiskAgent(), SynthesisAgent()]).run(
        "Coordinate real-time AI operations"
    )
    print(result.answer)
    print(f"rounds={result.rounds}")


if __name__ == "__main__":
    main()

