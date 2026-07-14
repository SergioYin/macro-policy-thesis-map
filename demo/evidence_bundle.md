# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 50

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
| README.md | 10220 | eaa234fbd5b55e4b |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/cli_help.json | 11169 | fe922417f2a1ede9 |
| demo/cli_help.md | 7728 | 8a67e4481f613301 |
| demo/cold_start_walkthrough.json | 3025 | f4ad9938520ac395 |
| demo/cold_start_walkthrough.md | 2342 | af4c5c761e9da9be |
| demo/command_matrix.json | 11650 | 1eb66dbe9204a2fa |
| demo/command_matrix.md | 7693 | 3a370f34dc533f51 |
| demo/docs_export.json | 2521 | 27404a3954d073b7 |
| demo/docs_export.md | 1642 | 7207dfa6d9e2e791 |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | 3973fd83bc3b59e7 |
| demo/input_schema.md | 1997 | 3cf4632070a11834 |
| demo/maturity_report.json | 1157 | 96cf4d616ecea361 |
| demo/maturity_report.md | 626 | d9da010a8013055d |
| demo/public_readiness.json | 1355 | 26e502baf3e00996 |
| demo/public_readiness.md | 1009 | c248789cc8208e76 |
| demo/quickstart_check.json | 5631 | 21cd7bbf5b86f0d1 |
| demo/quickstart_check.md | 3586 | 1f9ba0e532cb4150 |
| demo/readme_snippet.json | 1253 | ecb716a85d3e4108 |
| demo/readme_snippet.md | 785 | d47dd5186caf62b6 |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 2732 | 7cf26ad10b287905 |
| demo/troubleshoot.md | 2053 | ab8727285b47c4ac |
| demo/visual_receipt.html | 2636 | 0fc79ca76b1ef233 |
| demo/visual_receipt.json | 2682 | 3da4ec60def90c7e |
| demo/visual_receipt.svg | 2530 | 329ecc447a69c7ab |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 819 | ee15e3f8b5d693b1 |
| skills/agent/macro-policy-thesis-map/SKILL.md | 2782 | b60e5d1ad66a7639 |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 14315 | 1086bc049a77329d |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
