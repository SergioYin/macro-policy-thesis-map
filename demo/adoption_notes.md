# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Maturity: needs-review (18 / 19)

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
| README.md | 20213 | bd9e1705b4ad4609 |
| demo/artifact_index.json | 27463 | 6e767512e0bcd303 |
| demo/assumption_registry.json | 2500 | 24f1cb2faaf193e6 |
| demo/benchmark_suite.json | 3043 | 287d3fd6ac67014f |
| demo/boundary_attestation.json | 2101 | 3aaf0a1cff28aa03 |
| demo/citation_map.json | 5723 | 1efa53e66056991d |
| demo/cli_help.json | 22174 | 49979ac371db2feb |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/command_matrix.json | 23315 | 6655681f7e419648 |
| demo/compatibility_report.json | 2257 | 0a222de323e14ab6 |
| demo/data_dictionary_diff.json | 3472 | b1c9f49c0cbf3f3d |
| demo/docs_export.json | 9113 | 7abe99a8aeda92bf |
| demo/evaluator_scorecard.json | 2250 | 4e534075cd200132 |
| demo/evidence_bundle.json | 19080 | c2985ca1793291c8 |
| demo/golden_fixtures.json | 4685 | 99a3213b8530a9a4 |
| demo/integration_cookbook.json | 3546 | a4c794f009d7bede |
| demo/maintainer_guide.json | 2594 | 23c3bcd8b3958d2a |
| demo/maturity_report.json | 1622 | 02f3a3edd8df91a3 |
| demo/provenance_ledger.json | 26766 | 16af0d34681e26e4 |
| demo/public_readiness.json | 2471 | d45135eba9e8effb |
| demo/readme_snippet.json | 6230 | 99265ac326496199 |
| demo/regression_summary.json | 3389 | 55721620ea052ddc |
| demo/release_faq.json | 2820 | b62bd3e5721b08ca |
| demo/release_manifest.json | 18568 | 365a3a8944e17c4a |
| demo/release_notes_draft.json | 2124 | f62415c15621be64 |
| demo/reproducibility_recipe.json | 10617 | 5031cf7d6615be3b |
| demo/scenario_library.json | 2903 | cc502c7edcf25d4d |
| demo/troubleshoot.json | 3174 | b986a9d03a2293b7 |
| demo/trust_report.json | 5130 | 212ac784fdce5843 |
