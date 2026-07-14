# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.0.0

Maturity: ready (15 / 15)

Public readiness: ready

Release manifest artifacts: 76

## Release Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |

## Cold User Next Actions

| Action |
| --- |
| Run the quickstart commands from a clean checkout. |
| Review demo/reviewer_scorecard.md for any maturity item marked review. |
| Confirm demo/public_readiness.json remains ready after local edits. |
| Run public-scan and diff-check before sharing the bundle. |

## Safety Boundaries

| Boundary |
| --- |
| Use static files only. |
| Do not add workflow files, upload steps, or private references. |
| Do not fetch live data, connect to brokers, place orders, or provide financial advice. |
| Treat public-readiness blockers and reviewer-scorecard review items as release-owner follow-up. |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| README.md | 13515 | 4366c0540cdd883c |
| demo/assumption_registry.json | 2500 | 70aecc7f328a8430 |
| demo/benchmark_suite.json | 3043 | 3f8b9be2e11158d9 |
| demo/cli_help.json | 14939 | 2e0d1c169d268305 |
| demo/cold_start_walkthrough.json | 3924 | 08c65a8acc7216b8 |
| demo/command_matrix.json | 15540 | 5467cce33f686c5a |
| demo/compatibility_report.json | 1688 | 737f1a2d1377e5e4 |
| demo/data_dictionary_diff.json | 3472 | 894c3a7c3f46c635 |
| demo/docs_export.json | 4892 | 07f7d1874faaec4c |
| demo/evidence_bundle.json | 12337 | 50f995f62cd84c64 |
| demo/golden_fixtures.json | 4685 | 43567374f2468e4a |
| demo/integration_cookbook.json | 3546 | 4412ef0248807d31 |
| demo/maintainer_guide.json | 2216 | 66aeb9ddf7d23998 |
| demo/maturity_report.json | 1313 | 4b0c137ae12f6b3a |
| demo/public_readiness.json | 1732 | 4dd6c11f67f4d2c1 |
| demo/readme_snippet.json | 3080 | 94d243c825b24666 |
| demo/regression_summary.json | 1984 | d76fb5661bd590f4 |
| demo/release_manifest.json | 12659 | 8ff93441a6d2c1a4 |
| demo/scenario_library.json | 2903 | 6a6dfba6bf9c54a4 |
| demo/troubleshoot.json | 3174 | 623fae46fea5fc9e |
