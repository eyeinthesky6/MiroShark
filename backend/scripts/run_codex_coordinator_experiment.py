#!/usr/bin/env python3
"""Run the Codex Coordinator open-source decision experiment through MiroShark."""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import test_e2e_api as e2e  # noqa: E402

backend_dir = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
repo_root = os.path.abspath(os.path.join(backend_dir, ".."))

e2e.PDF_PATH = os.environ.get(
    "EXPERIMENT_INPUT",
    os.path.join(repo_root, "tasks", "codex-coordinator-decision-packet.md"),
)
e2e.SIMULATION_REQUIREMENT = (
    "Simulate a diverse, adversarial public and developer-community reaction to the "
    "decision to open-source Codex Coordinator. Compare the observed open-source "
    "strategy against closed-source, delayed-release, selective-source, and open-core "
    "counterfactuals over 12–24 months. Represent the stakeholder groups in the packet; "
    "surface second-order effects, disagreements, failure modes, and conditions for "
    "success. Do not assume that open or closed is inherently preferable. The final "
    "report must give a directional verdict (correct, incorrect, or too early to tell), "
    "a confidence level, the strongest evidence on both sides, concrete mitigations, "
    "and measurable signals that would falsify the verdict. Clearly label all findings "
    "as synthetic simulation output rather than observed market evidence."
)
e2e.MAX_SIM_ROUNDS = int(os.environ.get("EXPERIMENT_ROUNDS", "2"))
e2e.ENABLE_POLYMARKET = False
e2e.OUT_DIR = os.path.abspath(
    os.environ.get("EXPERIMENT_OUTPUT", os.path.join(repo_root, "experiment_output"))
)
os.makedirs(e2e.OUT_DIR, exist_ok=True)

if __name__ == "__main__":
    e2e.main()
