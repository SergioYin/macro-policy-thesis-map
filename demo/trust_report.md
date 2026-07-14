# Public Trust Report

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Audience: GitHub visitor with no prior project context

Status: ready

Score: 6 / 6

## Trust Checks

| Check | Result | Evidence | Reason |
| --- | --- | --- | --- |
| zero_runtime_dependencies | pass | pyproject.toml | A stranger can inspect and install without pulling runtime packages. |
| local_static_inputs | pass | examples/macro_events.csv, examples/prior_macro_events.csv, examples/public_macro_cases.csv | Default examples are committed static CSV files. |
| deterministic_demo_outputs | pass | demo/command_matrix.json, demo/public_readiness.json, demo/release_manifest.json | Public command, readiness, and hash manifests are available under demo/. |
| test_and_scan_surfaces | pass | tests/test_cli.py, tests/test_safety.py, demo/public_readiness.json | Tests and public scan support local verification without network access. |
| finance_boundaries | pass | README.md, skills/agent/macro-policy-thesis-map/SKILL.md | Research-only limitations are visible before running the CLI. |
| no_workflow_files | pass | .github/workflows | Evaluation does not depend on hidden CI or repository automation. |

## Local Evidence Artifacts

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| README.md | 17804 | 2544bbba66b1aa8f |
| demo/command_matrix.json | 20252 | 0eedc17d3bea61f2 |
| demo/evidence_bundle.json | 17114 | 8d272626babf708f |
| demo/public_readiness.json | 2116 | ea95c96e19cefec9 |
| demo/release_manifest.json | 16603 | 50d89640ff5572c5 |
| pyproject.toml | 832 | d1f5f350cfc9b332 |
| tests/test_cli.py | 23575 | e4e74cefb38973a1 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |

## Verification Commands

| Command |
| --- |
| PYTHONPATH=src python -m pytest |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
