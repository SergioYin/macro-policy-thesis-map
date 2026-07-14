# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 56

Missing count: 0

## Evaluation Commands

| Command |
| --- |
| PYTHONPATH=src python -m pytest tests/test_cli.py tests/test_safety.py |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |

## Missing

| Path |
| --- |
| none |

## Artifacts

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| LICENSE | 1066 | b13dc350cd48500c |
| README.md | 11457 | c3f6dcc9a6f908ce |
| demo/assumption_registry.json | 2500 | eaef6265dd5bc388 |
| demo/assumption_registry.md | 1980 | 04fe2e3e4e6d56c7 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/cli_help.json | 12469 | 194440fbdd3c0193 |
| demo/cli_help.md | 8653 | ee93ddaf0b9436ec |
| demo/cold_start_walkthrough.json | 3025 | f4ad9938520ac395 |
| demo/cold_start_walkthrough.md | 2342 | af4c5c761e9da9be |
| demo/command_matrix.json | 12945 | 9cd774a589d103c9 |
| demo/command_matrix.md | 8556 | c85741c8d658518f |
| demo/data_dictionary_diff.json | 3472 | dfa75a46af746035 |
| demo/data_dictionary_diff.md | 2177 | 86f1198eb0785c72 |
| demo/docs_export.json | 3332 | 038ed466803af18f |
| demo/docs_export.md | 2039 | 75afcf8677488e06 |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | 2bfee681498b0812 |
| demo/input_schema.md | 1997 | 3a6c9b953a7de268 |
| demo/maturity_report.json | 1235 | c07499edebed7b3e |
| demo/maturity_report.md | 664 | 015cdcf15b0dfb20 |
| demo/public_readiness.json | 1522 | 9dccc86d5ebed1d5 |
| demo/public_readiness.md | 1119 | a6af529cae3491c5 |
| demo/quickstart_check.json | 6315 | 5e37fd03c619d316 |
| demo/quickstart_check.md | 4021 | b85d52086e60e5a4 |
| demo/readme_snippet.json | 1868 | a47fbc7eee8ad796 |
| demo/readme_snippet.md | 1123 | 7e2cd08dda5284ff |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/scenario_library.json | 2903 | 44d3f23eafdadeb3 |
| demo/scenario_library.md | 1936 | 02371cfe666cccda |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 3174 | fbd09082b63e674a |
| demo/troubleshoot.md | 2357 | 1de5bb412b1b2059 |
| demo/visual_receipt.html | 3104 | 88f5c30a46eb8f63 |
| demo/visual_receipt.json | 3352 | a4ee83d628c6b1d3 |
| demo/visual_receipt.svg | 2519 | 48993870c4cc3b0f |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 819 | db9d1c7b0d96e6bf |
| skills/agent/macro-policy-thesis-map/SKILL.md | 3062 | 3e2ac9bf3e85192a |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 15692 | dabaea10614c2404 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
