# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.7.0

Maturity: ready (14 / 14)

Public readiness: ready

Release manifest artifacts: 64

## Release Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root . |
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
| README.md | 11457 | c3f6dcc9a6f908ce |
| demo/assumption_registry.json | 2500 | eaef6265dd5bc388 |
| demo/cli_help.json | 12469 | 194440fbdd3c0193 |
| demo/cold_start_walkthrough.json | 3388 | 45482ee14454e821 |
| demo/command_matrix.json | 12945 | 9cd774a589d103c9 |
| demo/data_dictionary_diff.json | 3472 | dfa75a46af746035 |
| demo/docs_export.json | 3333 | e58db956e3fbd5d8 |
| demo/evidence_bundle.json | 9875 | fa03db93b320d05b |
| demo/maturity_report.json | 1235 | c07499edebed7b3e |
| demo/public_readiness.json | 1522 | 9dccc86d5ebed1d5 |
| demo/readme_snippet.json | 1868 | a47fbc7eee8ad796 |
| demo/release_manifest.json | 10720 | 4b602d8cc944613e |
| demo/scenario_library.json | 2903 | 44d3f23eafdadeb3 |
| demo/troubleshoot.json | 3174 | fbd09082b63e674a |
