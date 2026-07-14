# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 93

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
| PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root . |
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
| README.md | 17804 | 2544bbba66b1aa8f |
| demo/api_reference.html | 13422 | d2dc00f8b6a91f2c |
| demo/api_reference.json | 41652 | 459ceec67aa61f46 |
| demo/api_reference.md | 18635 | 96426334358080c1 |
| demo/artifact_index.json | 24304 | 6178755dca37c641 |
| demo/artifact_index.md | 8896 | 384d8b60e7f4424e |
| demo/assumption_registry.json | 2500 | de075c9b3fb8f456 |
| demo/assumption_registry.md | 1980 | 0300d98f2f5eecaf |
| demo/benchmark_suite.json | 3043 | 6ee09b77f1d4f5aa |
| demo/benchmark_suite.md | 1916 | 28305b62f844c032 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/citation_map.json | 4645 | 5c87565d3146b53d |
| demo/citation_map.md | 1690 | e733c68aa2f99289 |
| demo/cli_help.json | 19327 | 632452d87990f5f1 |
| demo/cli_help.md | 13461 | 02d4a0db172d9293 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/cold_start_walkthrough.md | 3810 | 0d646cc4c4b95db0 |
| demo/command_matrix.json | 20252 | 0eedc17d3bea61f2 |
| demo/command_matrix.md | 13509 | b2a1218e98d1247f |
| demo/compatibility_report.json | 1952 | 6c3056202895e6f5 |
| demo/compatibility_report.md | 1357 | 0cc97f2bfa740961 |
| demo/data_dictionary_diff.json | 3472 | 41ecef87918921c8 |
| demo/data_dictionary_diff.md | 2177 | 43080d5bc3d487d0 |
| demo/docs_export.json | 7471 | 021bf20feecf2d6e |
| demo/docs_export.md | 3970 | f8b251a2a5538af3 |
| demo/evaluator_scorecard.json | 1762 | a9406e7b779c266d |
| demo/evaluator_scorecard.md | 1335 | 743673aa00d75e1c |
| demo/example_pack.html | 2945 | 5d6bc3fe906edec4 |
| demo/example_pack.json | 3795 | 7cb7f9c3f2b0fc25 |
| demo/example_pack.md | 2132 | e5b600b5a1f1a446 |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/golden_fixtures.json | 4685 | f6c5648518f62a1b |
| demo/golden_fixtures.md | 1287 | e3b9cc07f8f7402c |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | daba44295c239710 |
| demo/input_schema.md | 1997 | c62f5d75f7fa35cd |
| demo/integration_cookbook.json | 3546 | 8a9ed4d4f1bc0b6f |
| demo/integration_cookbook.md | 2480 | 64d584a9f491472a |
| demo/landing_page.html | 3860 | 178a338dc19a2efd |
| demo/landing_page.json | 6046 | 1d5dd327d5deed49 |
| demo/landing_page.md | 3222 | 08ae9bad5f9805c9 |
| demo/maintainer_guide.json | 2430 | de0a35b7e0901089 |
| demo/maintainer_guide.md | 2160 | 5c6bcce3dfeca5f2 |
| demo/maturity_report.json | 1456 | 73c8213cb4b0c095 |
| demo/maturity_report.md | 765 | 00e1d5ed1876aacd |
| demo/public_readiness.json | 2116 | ea95c96e19cefec9 |
| demo/public_readiness.md | 1542 | c63bce85990b63aa |
| demo/quickstart_check.json | 9973 | 9f484679160c3e56 |
| demo/quickstart_check.md | 6301 | 28e066f153edc8ef |
| demo/readme_snippet.json | 4982 | 1b317fea0dfb9a9f |
| demo/readme_snippet.md | 2815 | c19125c5c9f7d486 |
| demo/regression_summary.json | 2275 | 784262d381778f1f |
| demo/regression_summary.md | 1711 | 8d15612225ea8c07 |
| demo/release_faq.json | 2295 | 5aafef8f95cd0962 |
| demo/release_faq.md | 1537 | ed5a3bf8f0daa89e |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/roadmap_next.html | 2785 | 22fec239e7beb50f |
| demo/roadmap_next.json | 2452 | 3928f2c8b8502c9a |
| demo/roadmap_next.md | 1954 | e20df3db1b243b32 |
| demo/scenario_library.json | 2903 | a10db1111ec03d96 |
| demo/scenario_library.md | 1936 | 0402d234f5250f31 |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 3174 | dbbbecdae18d1dc9 |
| demo/troubleshoot.md | 2357 | 994fc517414a6d56 |
| demo/trust_report.json | 3747 | 17bef81b0c89890d |
| demo/trust_report.md | 2303 | 9babb344f36637ba |
| demo/visual_receipt.html | 3104 | 3936c9ab772be878 |
| demo/visual_receipt.json | 3352 | a9dd7a01cd5aa45b |
| demo/visual_receipt.svg | 2519 | 45965b0b90fbdd2d |
| demo/workflow_protocol.html | 2971 | b981e3bbeb799bc4 |
| demo/workflow_protocol.json | 3557 | d9e8eb649bda291f |
| demo/workflow_protocol.md | 2397 | 9511beb364af7159 |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 832 | d1f5f350cfc9b332 |
| skills/agent/macro-policy-thesis-map/SKILL.md | 4226 | 482b63068e523668 |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 23575 | e4e74cefb38973a1 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
