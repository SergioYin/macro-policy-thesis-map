# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 68

Missing count: 0

## Evaluation Commands

| Command |
| --- |
| PYTHONPATH=src python -m pytest tests/test_cli.py tests/test_safety.py |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root . |
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
| README.md | 13515 | 4366c0540cdd883c |
| demo/assumption_registry.json | 2500 | 70aecc7f328a8430 |
| demo/assumption_registry.md | 1980 | 2b961c66ef2d33cc |
| demo/benchmark_suite.json | 3043 | 3f8b9be2e11158d9 |
| demo/benchmark_suite.md | 1916 | 18115fdb4f1ca70f |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/cli_help.json | 14939 | 2e0d1c169d268305 |
| demo/cli_help.md | 10373 | 6d51f91a2bb2b6e9 |
| demo/cold_start_walkthrough.json | 3924 | 08c65a8acc7216b8 |
| demo/cold_start_walkthrough.md | 3075 | c181fff48c192faf |
| demo/command_matrix.json | 15540 | 5467cce33f686c5a |
| demo/command_matrix.md | 10287 | 94c79f2821d3b898 |
| demo/compatibility_report.json | 1688 | 737f1a2d1377e5e4 |
| demo/compatibility_report.md | 1207 | e140522e762b8cfc |
| demo/data_dictionary_diff.json | 3472 | 894c3a7c3f46c635 |
| demo/data_dictionary_diff.md | 2177 | 6af63ab579f72a45 |
| demo/docs_export.json | 4892 | 07f7d1874faaec4c |
| demo/docs_export.md | 2771 | e3beea885245dab7 |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/golden_fixtures.json | 4685 | 43567374f2468e4a |
| demo/golden_fixtures.md | 1287 | 0787d7af95d65426 |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | e3fcb549370dd31e |
| demo/input_schema.md | 1997 | 754ab856318b5154 |
| demo/integration_cookbook.json | 3546 | 4412ef0248807d31 |
| demo/integration_cookbook.md | 2480 | bb099ed382e45608 |
| demo/maintainer_guide.json | 2216 | 66aeb9ddf7d23998 |
| demo/maintainer_guide.md | 1926 | a5c3b705b6a3865c |
| demo/maturity_report.json | 1313 | 4b0c137ae12f6b3a |
| demo/maturity_report.md | 702 | e25f6b612827b7b5 |
| demo/public_readiness.json | 1732 | 4dd6c11f67f4d2c1 |
| demo/public_readiness.md | 1272 | bc2c339a94e5519a |
| demo/quickstart_check.json | 7665 | 3505abdb1875999a |
| demo/quickstart_check.md | 4873 | f7264bf8fa7386c6 |
| demo/readme_snippet.json | 3080 | 94d243c825b24666 |
| demo/readme_snippet.md | 1787 | 46296fe71995bdb3 |
| demo/regression_summary.json | 1984 | d76fb5661bd590f4 |
| demo/regression_summary.md | 1501 | d049beb5ad27eab2 |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/scenario_library.json | 2903 | 6a6dfba6bf9c54a4 |
| demo/scenario_library.md | 1936 | 422c35b095ebd318 |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 3174 | 623fae46fea5fc9e |
| demo/troubleshoot.md | 2357 | 46dc6e206ba46b5b |
| demo/visual_receipt.html | 3104 | fcc332f19244de6c |
| demo/visual_receipt.json | 3352 | c404724fce22219d |
| demo/visual_receipt.svg | 2519 | 3f7700e482b573d6 |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 832 | 6b41fc65064e38fd |
| skills/agent/macro-policy-thesis-map/SKILL.md | 3447 | ad2a3aa446657766 |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 18727 | 803740be53d67ae8 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
