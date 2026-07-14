# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Maturity: needs-review (17 / 18)

Public readiness: ready

Release manifest artifacts: 109

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
| README.md | 19492 | 7cd2fe9dcb70f4ae |
| demo/artifact_index.json | 26413 | 934fe0fd1b8ce7a2 |
| demo/assumption_registry.json | 2500 | 496daa362b79b90a |
| demo/benchmark_suite.json | 3043 | 4a16814969e6dd12 |
| demo/boundary_attestation.json | 2101 | 521ff58189d124c5 |
| demo/citation_map.json | 5681 | 84ae750e57985800 |
| demo/cli_help.json | 21217 | 020c43e13a343233 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/command_matrix.json | 22248 | 7f61d38fdb211d10 |
| demo/compatibility_report.json | 2099 | fbf928894bc1ca24 |
| demo/data_dictionary_diff.json | 3472 | 510e5713493d6f3d |
| demo/docs_export.json | 8541 | 1e0994200d487257 |
| demo/evaluator_scorecard.json | 2214 | 79c7961fbc7b64f0 |
| demo/evidence_bundle.json | 18426 | a3c4962c0db96247 |
| demo/golden_fixtures.json | 4685 | 6918a9dc69858c85 |
| demo/integration_cookbook.json | 3546 | 25d215e91152aa50 |
| demo/maintainer_guide.json | 2540 | 6713131f87a78e8c |
| demo/maturity_report.json | 1544 | 16497ee75188fbd0 |
| demo/provenance_ledger.json | 25808 | b41da876e3c9d36b |
| demo/public_readiness.json | 2301 | b2e51d04d172c6ca |
| demo/readme_snippet.json | 5816 | ce0ab69a9191c53c |
| demo/regression_summary.json | 2966 | 75a04ffefd4176b1 |
| demo/release_faq.json | 2778 | e1d0a5c2660c6411 |
| demo/release_manifest.json | 17914 | e209ffc1f60d18a8 |
| demo/release_notes_draft.json | 1922 | c1819fef3ab960e5 |
| demo/reproducibility_recipe.json | 10241 | c171be145870f412 |
| demo/scenario_library.json | 2903 | 8997f1e9baaefcfa |
| demo/troubleshoot.json | 3174 | f03de8b53641563b |
| demo/trust_report.json | 5130 | edf2cf57246dad6e |
