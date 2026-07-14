# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Maturity: ready (17 / 17)

Public readiness: ready

Release manifest artifacts: 101

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
| PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root . |
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
| README.md | 17804 | 2544bbba66b1aa8f |
| demo/artifact_index.json | 24304 | 1fe20b2960e171da |
| demo/assumption_registry.json | 2500 | de075c9b3fb8f456 |
| demo/benchmark_suite.json | 3043 | 6ee09b77f1d4f5aa |
| demo/citation_map.json | 4645 | cb3e09d776b4e334 |
| demo/cli_help.json | 19327 | 632452d87990f5f1 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/command_matrix.json | 20252 | 0eedc17d3bea61f2 |
| demo/compatibility_report.json | 1952 | 6c3056202895e6f5 |
| demo/data_dictionary_diff.json | 3472 | 41ecef87918921c8 |
| demo/docs_export.json | 7471 | 71935492ff33c6e4 |
| demo/evaluator_scorecard.json | 1762 | a9406e7b779c266d |
| demo/evidence_bundle.json | 17114 | 8d272626babf708f |
| demo/golden_fixtures.json | 4685 | f6c5648518f62a1b |
| demo/integration_cookbook.json | 3546 | 8a9ed4d4f1bc0b6f |
| demo/maintainer_guide.json | 2430 | de0a35b7e0901089 |
| demo/maturity_report.json | 1456 | 73c8213cb4b0c095 |
| demo/public_readiness.json | 2116 | ea95c96e19cefec9 |
| demo/readme_snippet.json | 4982 | 1b317fea0dfb9a9f |
| demo/regression_summary.json | 2275 | 784262d381778f1f |
| demo/release_faq.json | 2295 | 5aafef8f95cd0962 |
| demo/release_manifest.json | 16603 | 50d89640ff5572c5 |
| demo/scenario_library.json | 2903 | a10db1111ec03d96 |
| demo/troubleshoot.json | 3174 | dbbbecdae18d1dc9 |
| demo/trust_report.json | 3747 | 90e576c5b6525744 |
