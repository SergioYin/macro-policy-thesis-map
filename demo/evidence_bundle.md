# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 101

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
| README.md | 19492 | 7cd2fe9dcb70f4ae |
| demo/api_reference.html | 14498 | cc1aa66e9fe4c257 |
| demo/api_reference.json | 45374 | 9babdb9e89dfc5ee |
| demo/api_reference.md | 20311 | 37910cc4f52c4724 |
| demo/artifact_index.json | 26413 | fcbabc7d8e4f3cf0 |
| demo/artifact_index.md | 9685 | f39a25556ee0957a |
| demo/assumption_registry.json | 2500 | 496daa362b79b90a |
| demo/assumption_registry.md | 1980 | 3321107de459893a |
| demo/benchmark_suite.json | 3043 | 4a16814969e6dd12 |
| demo/benchmark_suite.md | 1916 | 9037acb0cc47a879 |
| demo/boundary_attestation.json | 2101 | 521ff58189d124c5 |
| demo/boundary_attestation.md | 1485 | 488105fdb8470163 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/citation_map.json | 5681 | 038e10ece93cd22e |
| demo/citation_map.md | 2016 | 8edcea066457d94c |
| demo/cli_help.json | 21217 | 020c43e13a343233 |
| demo/cli_help.md | 14851 | 13cbcfa1d3053508 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/cold_start_walkthrough.md | 3810 | 0d646cc4c4b95db0 |
| demo/command_matrix.json | 22248 | 7f61d38fdb211d10 |
| demo/command_matrix.md | 14929 | 87185ae268bfd471 |
| demo/compatibility_report.json | 2099 | fbf928894bc1ca24 |
| demo/compatibility_report.md | 1447 | e6914baf5ca32fd4 |
| demo/data_dictionary_diff.json | 3472 | 510e5713493d6f3d |
| demo/data_dictionary_diff.md | 2177 | a64ba918055b0779 |
| demo/docs_export.json | 8541 | 6c5cb1021151e8ec |
| demo/docs_export.md | 4488 | e3dc7a80a686f85f |
| demo/evaluator_scorecard.json | 2214 | 79c7961fbc7b64f0 |
| demo/evaluator_scorecard.md | 1715 | b5a82ced9745cbaf |
| demo/example_pack.html | 2945 | 6f32417150ffa6a7 |
| demo/example_pack.json | 3795 | b2704c9a6deba147 |
| demo/example_pack.md | 2132 | 8b6c0b536f95affb |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/golden_fixtures.json | 4685 | 6918a9dc69858c85 |
| demo/golden_fixtures.md | 1287 | 82b2d1c321ff99c4 |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | b2cbdb9101393a75 |
| demo/input_schema.md | 1997 | 375a25ed52497363 |
| demo/integration_cookbook.json | 3546 | 25d215e91152aa50 |
| demo/integration_cookbook.md | 2480 | f62ac0e3e755c8be |
| demo/landing_page.html | 3860 | 07cb9a57d8c08c24 |
| demo/landing_page.json | 6046 | 23e0a951b8946771 |
| demo/landing_page.md | 3222 | 0e6eb500c7da3765 |
| demo/maintainer_guide.json | 2540 | 6713131f87a78e8c |
| demo/maintainer_guide.md | 2278 | 7547ea596e8676b8 |
| demo/maturity_report.json | 1544 | 16497ee75188fbd0 |
| demo/maturity_report.md | 814 | 506b76e3b333931b |
| demo/provenance_ledger.json | 25808 | 6aac8308e447ef46 |
| demo/provenance_ledger.md | 9743 | 6853de8d53cfdfd5 |
| demo/public_readiness.json | 2301 | b2e51d04d172c6ca |
| demo/public_readiness.md | 1670 | e5868de7e7b0f263 |
| demo/quickstart_check.json | 10899 | 9b100b1f36a95f56 |
| demo/quickstart_check.md | 6895 | 101410efb29af736 |
| demo/readme_snippet.json | 5816 | ce0ab69a9191c53c |
| demo/readme_snippet.md | 3275 | a55a5c3027c81672 |
| demo/regression_summary.json | 2966 | 75a04ffefd4176b1 |
| demo/regression_summary.md | 2312 | 54f5fe8515bb49b9 |
| demo/release_faq.json | 2778 | e1d0a5c2660c6411 |
| demo/release_faq.md | 1852 | ad7ac666d3b4ac69 |
| demo/release_notes_draft.json | 1922 | c1819fef3ab960e5 |
| demo/release_notes_draft.md | 1880 | ebab1c802f5e5710 |
| demo/reproducibility_recipe.json | 10241 | c171be145870f412 |
| demo/reproducibility_recipe.md | 7352 | 6056669713187aee |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/roadmap_next.html | 2785 | 60e1592f07e31b4c |
| demo/roadmap_next.json | 2452 | 6a5aec3071917e7e |
| demo/roadmap_next.md | 1954 | 15e06375f6dcb59d |
| demo/scenario_library.json | 2903 | 8997f1e9baaefcfa |
| demo/scenario_library.md | 1936 | bf179298255b14bd |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 3174 | f03de8b53641563b |
| demo/troubleshoot.md | 2357 | ca95a276ea8f7efe |
| demo/trust_report.json | 5130 | 2ff715389b8cd046 |
| demo/trust_report.md | 3128 | 577846a827973a1d |
| demo/visual_receipt.html | 3104 | ef267e6e134e7fcb |
| demo/visual_receipt.json | 3350 | d0da08d915f68d64 |
| demo/visual_receipt.svg | 2519 | 47341e2473ff675c |
| demo/workflow_protocol.html | 2971 | 63f520952f7c3eed |
| demo/workflow_protocol.json | 3557 | 01116e3fb6b402c8 |
| demo/workflow_protocol.md | 2397 | bf183dd8ad9a4577 |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 832 | 4849cdc7abe57512 |
| skills/agent/macro-policy-thesis-map/SKILL.md | 4591 | 07299c071a787ed4 |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 25101 | ca215821917b8b36 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
