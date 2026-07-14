# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.6.0

Maturity: ready (13 / 13)

Public readiness: ready

Release manifest artifacts: 58

## Release Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . |
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
| README.md | 10220 | eaa234fbd5b55e4b |
| demo/cli_help.json | 11169 | fe922417f2a1ede9 |
| demo/cold_start_walkthrough.json | 3025 | f4ad9938520ac395 |
| demo/command_matrix.json | 11650 | 1eb66dbe9204a2fa |
| demo/docs_export.json | 2521 | 27404a3954d073b7 |
| demo/evidence_bundle.json | 8900 | 8a4daf5c8c2f5c00 |
| demo/maturity_report.json | 1157 | 96cf4d616ecea361 |
| demo/public_readiness.json | 1355 | 26e502baf3e00996 |
| demo/readme_snippet.json | 1253 | ecb716a85d3e4108 |
| demo/release_manifest.json | 9745 | 5e498ecb61fc230f |
| demo/troubleshoot.json | 2732 | 7cf26ad10b287905 |
