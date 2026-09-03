"""Fast, real invariant checks over (a subset of) the fan-out vs. serial
benchmark scenarios defined in scripts/benchmark_fanout_vs_serial.py.

These are not hand-computed expected numbers -- every assertion below runs
the real SwarmRuntime / SerialSwarmRuntime objects (via run_scenario) and
checks structural invariants that must hold given how SwarmRuntime and the
deterministic stub agents are actually implemented.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from benchmark_fanout_vs_serial import SCENARIOS, run_all, run_scenario  # noqa: E402


def test_all_scenarios_run_without_error() -> None:
    results = run_all()
    assert len(results) == len(SCENARIOS) == 9


def test_fanout_never_needs_more_rounds_than_serial_matched_when_both_converge() -> None:
    """Fan-out's whole premise is fewer sequential rounds for the same
    convergence target. When both conditions converge within the same
    round budget, fan-out must not need MORE rounds than serial."""
    for scenario in SCENARIOS:
        result = run_scenario(scenario)
        if result.fanout.converged and result.serial_matched.converged:
            assert result.fanout.rounds <= result.serial_matched.rounds, (
                f"{scenario.name}: fanout took {result.fanout.rounds} rounds, "
                f"serial_matched took {result.serial_matched.rounds}"
            )


def test_serial_matched_never_beats_fanout_on_convergence_under_equal_round_budget() -> None:
    """Under the SAME max_rounds, serial can accept at most one proposal
    per round, so it can never reach convergence in a scenario where
    fan-out cannot (both share the same acceptance rule and roster)."""
    for scenario in SCENARIOS:
        result = run_scenario(scenario)
        if result.serial_matched.converged:
            assert result.fanout.converged, (
                f"{scenario.name}: serial_matched converged but fanout (same round "
                "budget, strictly more proposals per round) did not"
            )


def test_serial_extended_reaches_every_target_fanout_reaches() -> None:
    """Given an equal total-invocation budget (max_rounds * roster size),
    serial should be able to reach any convergence_target fan-out reaches
    -- the difference between the strategies is round-count, not raw
    reachability, given the same threshold/roster/target."""
    for scenario in SCENARIOS:
        result = run_scenario(scenario)
        if result.fanout.converged:
            assert result.serial_extended.converged, (
                f"{scenario.name}: fanout converged but serial_extended "
                "(equal total invocation budget) did not"
            )


def test_structurally_unreachable_scenarios_never_converge() -> None:
    """roster_too_small_for_target and acceptance_threshold_unreachable are
    deliberately built so NEITHER condition can converge under any round
    budget -- verify that stays true (and is reported honestly, not hidden)."""
    unreachable = {s.name for s in SCENARIOS if not s.expect_convergence}
    assert unreachable == {"roster_too_small_for_target", "acceptance_threshold_unreachable"}

    for scenario in SCENARIOS:
        if scenario.name in unreachable:
            result = run_scenario(scenario)
            assert not result.fanout.converged
            assert not result.serial_matched.converged
            assert not result.serial_extended.converged


def test_invocation_counts_match_rounds_times_roster_or_less() -> None:
    """Fan-out invocations must equal rounds_used * roster_size exactly
    (every agent proposes every round, including the converging round).
    Serial invocations must equal rounds_used exactly (one agent/round)."""
    for scenario in SCENARIOS:
        roster_size = len(scenario.roster_factory())
        result = run_scenario(scenario)
        assert result.fanout.invocations == result.fanout.rounds * roster_size
        assert result.serial_matched.invocations == result.serial_matched.rounds
        assert result.serial_extended.invocations == result.serial_extended.rounds


def test_wall_clock_is_measured_and_non_negative() -> None:
    for scenario in SCENARIOS[:3]:
        result = run_scenario(scenario)
        for condition in (result.fanout, result.serial_matched, result.serial_extended):
            assert condition.wall_clock_seconds >= 0.0
