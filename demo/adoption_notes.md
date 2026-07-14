# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.1.0

Maturity: ready (16 / 16)

Public readiness: ready

Release manifest artifacts: 91

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
| README.md | 16096 | 14c1a4e5d37ae040 |
| demo/assumption_registry.json | 2500 | 7170c7639ab9e790 |
| demo/benchmark_suite.json | 3043 | b491a34778eb237d |
| demo/cli_help.json | 17246 | 035477d512f32cb2 |
| demo/cold_start_walkthrough.json | 4389 | 544e7dc160b71aa3 |
| demo/command_matrix.json | 18004 | 482bdb26f8278978 |
| demo/compatibility_report.json | 1822 | d2653a328dc17a98 |
| demo/data_dictionary_diff.json | 3472 | 3d2592dd48b9de32 |
| demo/docs_export.json | 6178 | 2689d46f2138c12c |
| demo/evidence_bundle.json | 15119 | 92a1e46d33c41910 |
| demo/golden_fixtures.json | 4685 | 6e7b7638818afdf7 |
| demo/integration_cookbook.json | 3546 | 71823c83d849c943 |
| demo/maintainer_guide.json | 2322 | c54064f0c7b0ab21 |
| demo/maturity_report.json | 1386 | 701cd3be902cb617 |
| demo/public_readiness.json | 1923 | 15d96adf743682be |
| demo/readme_snippet.json | 4028 | 2265ee4e3406200e |
| demo/regression_summary.json | 1984 | 5919c7ab743c5893 |
| demo/release_manifest.json | 15025 | f2564a94855db679 |
| demo/scenario_library.json | 2903 | 62d405892fb64c52 |
| demo/troubleshoot.json | 3174 | 9b2d5f00d46734a2 |
