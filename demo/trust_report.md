# Public Trust Report

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

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
| README.md | 20613 | 71f5f2542b3a7bc9 |
| demo/boundary_attestation.json | 2101 | 32d1ff7a15c7debe |
| demo/command_matrix.json | 23850 | 5e97ff48b0bb0929 |
| demo/evidence_bundle.json | 19080 | b0bd94074e5f9486 |
| demo/provenance_ledger.json | 27062 | ec5015ff728ecde2 |
| demo/public_readiness.json | 2610 | 8b91002e3689db66 |
| demo/release_manifest.json | 18568 | dc52cccb72090ed5 |
| demo/release_notes_draft.json | 2248 | e14d99fc40369c0f |
| demo/reproducibility_recipe.json | 10807 | 7fe88eeb7faedd9c |
| pyproject.toml | 832 | 76e96e006cdb2620 |
| tests/test_cli.py | 26456 | 0461a69d708e22f2 |
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
