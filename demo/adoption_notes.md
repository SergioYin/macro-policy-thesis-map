# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Maturity: ready (20 / 20)

Public readiness: ready

Release manifest artifacts: 113

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
| PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-audit-summary --root . |
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
| README.md | 20613 | 71f5f2542b3a7bc9 |
| demo/artifact_index.json | 27781 | 9b636f1a40213802 |
| demo/assumption_registry.json | 2500 | 8c9211fd74cc7585 |
| demo/benchmark_suite.json | 3043 | fecc433c113c786f |
| demo/boundary_attestation.json | 2101 | 32d1ff7a15c7debe |
| demo/citation_map.json | 5936 | 25e37ca20e0c62c1 |
| demo/cli_help.json | 22661 | 39e89a7e1135aff2 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/command_matrix.json | 23850 | 5e97ff48b0bb0929 |
| demo/compatibility_report.json | 2400 | 56be342014d705ad |
| demo/data_dictionary_diff.json | 3472 | bfd4b231f59dc583 |
| demo/docs_export.json | 9415 | bb2d6fe136439981 |
| demo/evaluator_scorecard.json | 2257 | e87c0940fbff005d |
| demo/evidence_bundle.json | 19080 | b0bd94074e5f9486 |
| demo/golden_fixtures.json | 4685 | acea7ebf0a09c9d1 |
| demo/integration_cookbook.json | 3546 | 4cc09db548a7c957 |
| demo/maintainer_guide.json | 2623 | b448c5bdd76bec62 |
| demo/maturity_report.json | 1685 | 7c6686ce06ac79b2 |
| demo/provenance_ledger.json | 27062 | ec5015ff728ecde2 |
| demo/public_readiness.json | 2610 | 8b91002e3689db66 |
| demo/readme_snippet.json | 6230 | 238a74942c1c2adb |
| demo/regression_summary.json | 3662 | 7585f3c1dc78ba14 |
| demo/release_faq.json | 2887 | 0f235c2a8d40f672 |
| demo/release_manifest.json | 18568 | dc52cccb72090ed5 |
| demo/release_notes_draft.json | 2248 | e14d99fc40369c0f |
| demo/reproducibility_recipe.json | 10807 | 7fe88eeb7faedd9c |
| demo/scenario_library.json | 2903 | a8c13fa73022fd96 |
| demo/troubleshoot.json | 3174 | f2577b71f0b54928 |
| demo/trust_report.json | 5130 | f6249b9e4c8d4171 |
