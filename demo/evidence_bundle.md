# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 42

Missing count: 0

## Evaluation Commands

| Command |
| --- |
| PYTHONPATH=src python -m pytest tests/test_cli.py tests/test_safety.py |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |

## Missing

| Path |
| --- |
| none |

## Artifacts

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| LICENSE | 1066 | b13dc350cd48500c |
| README.md | 7691 | d1494a28d5d6a2bd |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/cold_start_walkthrough.json | 2115 | e40ad7fa1fa238cb |
| demo/cold_start_walkthrough.md | 1681 | 585045d1e2f59963 |
| demo/command_matrix.json | 8357 | 41a25718ab752b0a |
| demo/command_matrix.md | 5552 | 3713ac63c04be2f5 |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | a4baac3557dc1a45 |
| demo/input_schema.md | 1997 | cbe126ddf4ad6d3a |
| demo/maturity_report.json | 1018 | 88e6f0b098611bc8 |
| demo/maturity_report.md | 567 | d89f4f7bf9d60471 |
| demo/public_readiness.json | 1176 | 6c77e1bbdc99d8e9 |
| demo/public_readiness.md | 887 | 19f9e31fcf6d66b5 |
| demo/quickstart_check.json | 3923 | e5354ed50f6ef346 |
| demo/quickstart_check.md | 2542 | d6e1560e7a0bbad5 |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/visual_receipt.html | 2636 | b2c0ba972caca39c |
| demo/visual_receipt.json | 2683 | f605163af78543b0 |
| demo/visual_receipt.svg | 2530 | a15c3efc9217822a |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 819 | f60845993d627abf |
| skills/agent/macro-policy-thesis-map/SKILL.md | 2269 | dc469400e1dbf309 |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 10690 | 54c643cde31d359d |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
