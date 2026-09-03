"""Real merge gate: runs the shared `swarm_agent_pattern.fanout_v1` suite
from vpeetla-ai/golden-eval-registry against this repo's real, executed
`scripts/benchmark_fanout_vs_serial.py` results.

Skips locally when the sibling registry repo isn't checked out; CI always
checks it out first (see .github/workflows/ci.yml). Mirrors the
`GOLDEN_EVAL_REGISTRY_PATH` convention used across the vpeetla-ai org (see
e.g. aegisloop-agentops-workbench/services/api/tests/test_golden_eval_gate.py
and react-agent-pattern's equivalent).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from benchmark_fanout_vs_serial import SCENARIOS, run_scenario  # noqa: E402

try:
    from golden_eval_registry.runner import score_suite
    from golden_eval_registry.schema import parse_manifest
    from golden_eval_registry.validate import load_jsonl

    GOLDEN_EVAL_REGISTRY_AVAILABLE = True
except ImportError:
    GOLDEN_EVAL_REGISTRY_AVAILABLE = False

REGISTRY_PATH = Path(os.getenv("GOLDEN_EVAL_REGISTRY_PATH", "../golden-eval-registry")).resolve()
SUITE_DIR = REGISTRY_PATH / "suites" / "swarm_agent_fanout_v1"


def _actual_for_case(case: dict) -> dict:
    """Run the real benchmark scenario named by this case and shape the
    result the way the suite's `expect.equals` block expects it."""
    scenario_id = case["input"]["scenario_id"]
    scenario = next((s for s in SCENARIOS if s.name == scenario_id), None)
    if scenario is None:
        raise ValueError(f"unknown scenario_id in golden-eval case {case['id']!r}: {scenario_id!r}")

    result = run_scenario(scenario)
    return {
        "fanout_converged": result.fanout.converged,
        "fanout_rounds": result.fanout.rounds,
        "serial_matched_converged": result.serial_matched.converged,
        "serial_matched_rounds": result.serial_matched.rounds,
        "serial_extended_converged": result.serial_extended.converged,
        "serial_extended_rounds": result.serial_extended.rounds,
    }


@pytest.mark.skipif(
    not (GOLDEN_EVAL_REGISTRY_AVAILABLE and SUITE_DIR.exists()),
    reason="golden-eval-registry not available -- set GOLDEN_EVAL_REGISTRY_PATH or run in CI",
)
def test_swarm_agent_fanout_v1_suite_passes() -> None:
    manifest = parse_manifest(SUITE_DIR / "manifest.json")
    cases = load_jsonl(manifest.cases_path)

    actual_by_id = {str(case["id"]): _actual_for_case(case) for case in cases}

    result = score_suite(manifest, cases, actual_by_id)
    failures = "\n".join(f"{failure.case_id}: {failure.detail}" for failure in result.failures)
    assert result.passed, f"golden eval regressions:\n{failures}"
