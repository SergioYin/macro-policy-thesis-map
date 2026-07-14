# Public Trust Report

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Audience: GitHub visitor with no prior project context

Status: ready

Score: 7 / 7

## Trust Checks

| Check | Result | Evidence | Reason |
| --- | --- | --- | --- |
| zero_runtime_dependencies | pass | pyproject.toml | A stranger can inspect and install without pulling runtime packages. |
| local_static_inputs | pass | examples/macro_events.csv, examples/prior_macro_events.csv, examples/public_macro_cases.csv | Default examples are committed static CSV files. |
| deterministic_demo_outputs | pass | demo/command_matrix.json, demo/public_readiness.json, demo/release_manifest.json | Public command, readiness, and hash manifests are available under demo/. |
| test_and_scan_surfaces | pass | tests/test_cli.py, tests/test_safety.py, demo/public_readiness.json | Tests and public scan support local verification without network access. |
| finance_boundaries | pass | README.md, skills/agent/macro-policy-thesis-map/SKILL.md | Research-only limitations are visible before running the CLI. |
| no_workflow_files | pass | .github/workflows | Evaluation does not depend on hidden CI or repository automation. |
| governance_attestation_layer | pass | demo/boundary_attestation.json, demo/provenance_ledger.json, demo/reproducibility_recipe.json, demo/release_notes_draft.json | Governance evidence is recorded as local deterministic artifacts. |

## Local Evidence Artifacts

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| README.md | 20213 | bd9e1705b4ad4609 |
| demo/boundary_attestation.json | 2101 | 3aaf0a1cff28aa03 |
| demo/command_matrix.json | 23315 | 6655681f7e419648 |
| demo/evidence_bundle.json | 19080 | c2985ca1793291c8 |
| demo/provenance_ledger.json | 26766 | 16af0d34681e26e4 |
| demo/public_readiness.json | 2471 | d45135eba9e8effb |
| demo/release_manifest.json | 18568 | 365a3a8944e17c4a |
| demo/release_notes_draft.json | 2124 | f62415c15621be64 |
| demo/reproducibility_recipe.json | 10617 | 5031cf7d6615be3b |
| pyproject.toml | 832 | e2eccdcc2248f66d |
| tests/test_cli.py | 25925 | d1fe1bd81232c338 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |

## Verification Commands

| Command |
| --- |
| PYTHONPATH=src python -m pytest |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root . |
