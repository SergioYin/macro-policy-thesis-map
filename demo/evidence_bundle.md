# Evidence Bundle

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Artifact count: 105

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
| README.md | 20213 | bd9e1705b4ad4609 |
| demo/api_reference.html | 15029 | 774471c303c4088d |
| demo/api_reference.json | 47299 | b82a42e9cbf67437 |
| demo/api_reference.md | 21138 | e765a0f16dea6f5e |
| demo/artifact_index.json | 27463 | b21862414972e9e5 |
| demo/artifact_index.md | 10075 | cc42ab634dad4582 |
| demo/assumption_registry.json | 2500 | 24f1cb2faaf193e6 |
| demo/assumption_registry.md | 1980 | b0f851a867a3216d |
| demo/benchmark_suite.json | 3043 | 287d3fd6ac67014f |
| demo/benchmark_suite.md | 1916 | 86a7f8561a279961 |
| demo/boundary_attestation.json | 2101 | 3aaf0a1cff28aa03 |
| demo/boundary_attestation.md | 1485 | 7d8b8c99e7410411 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/citation_map.json | 5723 | f2743cdeed60b6b3 |
| demo/citation_map.md | 2058 | b4d857fab09d9bf6 |
| demo/cli_help.json | 22174 | 49979ac371db2feb |
| demo/cli_help.md | 15558 | 27377a4cfac85de1 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/cold_start_walkthrough.md | 3810 | 0d646cc4c4b95db0 |
| demo/command_matrix.json | 23315 | 6655681f7e419648 |
| demo/command_matrix.md | 15708 | f6599d5a8f001d3e |
| demo/compatibility_report.json | 2257 | 0a222de323e14ab6 |
| demo/compatibility_report.md | 1548 | 010e133a6e655915 |
| demo/data_dictionary_diff.json | 3472 | b1c9f49c0cbf3f3d |
| demo/data_dictionary_diff.md | 2177 | cfd3eb09350f1e49 |
| demo/docs_export.json | 9113 | 46712218e15cb9ea |
| demo/docs_export.md | 4784 | 4fcb9ca68476f384 |
| demo/evaluator_scorecard.json | 2250 | 4e534075cd200132 |
| demo/evaluator_scorecard.md | 1751 | 8d0d9e4c6069919a |
| demo/example_pack.html | 2945 | 8c221a2fe609c985 |
| demo/example_pack.json | 3795 | 935a6dab9ce220cf |
| demo/example_pack.md | 2132 | b06724bf250cfc33 |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/golden_fixtures.json | 4685 | 99a3213b8530a9a4 |
| demo/golden_fixtures.md | 1287 | a8d4b690ee52dd7e |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | 02f643407959d64c |
| demo/input_schema.md | 1997 | 421c6402eea9862e |
| demo/integration_cookbook.json | 3546 | a4c794f009d7bede |
| demo/integration_cookbook.md | 2480 | dc5b28704653220f |
| demo/landing_page.html | 3860 | 2e0c917e4863319d |
| demo/landing_page.json | 6046 | 9ff1501b33a0058f |
| demo/landing_page.md | 3222 | 680a264ce0740f73 |
| demo/maintainer_guide.json | 2594 | 23c3bcd8b3958d2a |
| demo/maintainer_guide.md | 2336 | 1d9901d4b3a63a35 |
| demo/maintainer_handoff.json | 3508 | a5a1daf57bf987d0 |
| demo/maintainer_handoff.md | 2429 | 6bead6e0c9098ec6 |
| demo/maturity_report.json | 1622 | 02f3a3edd8df91a3 |
| demo/maturity_report.md | 852 | 622bd663f4fc2576 |
| demo/onboarding_checklist.json | 2593 | e3944b057ecfcc8b |
| demo/onboarding_checklist.md | 2209 | 29e572d330eb545e |
| demo/provenance_ledger.json | 26766 | 1d9db255031ae0b9 |
| demo/provenance_ledger.md | 10109 | 1e26fe977d7f2641 |
| demo/public_readiness.json | 2471 | d45135eba9e8effb |
| demo/public_readiness.md | 1783 | 2573dcbb3707aee8 |
| demo/quickstart_check.json | 10899 | 9b100b1f36a95f56 |
| demo/quickstart_check.md | 6895 | 101410efb29af736 |
| demo/readme_snippet.json | 6230 | 99265ac326496199 |
| demo/readme_snippet.md | 3503 | 798d4ed518b2c24e |
| demo/regression_summary.json | 3389 | 55721620ea052ddc |
| demo/regression_summary.md | 2651 | 01303ace7d520486 |
| demo/release_faq.json | 2820 | b62bd3e5721b08ca |
| demo/release_faq.md | 1894 | 9fae7126efe177af |
| demo/release_notes_draft.json | 2124 | f62415c15621be64 |
| demo/release_notes_draft.md | 2068 | 824520c2570ec470 |
| demo/reproducibility_recipe.json | 10617 | 5031cf7d6615be3b |
| demo/reproducibility_recipe.md | 7608 | e718e5f02c0a34cb |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/roadmap_next.html | 2785 | 7143a953adc3e8de |
| demo/roadmap_next.json | 2452 | 394394f2afe8618f |
| demo/roadmap_next.md | 1954 | 0f979db08f83a7ff |
| demo/scenario_library.json | 2903 | cc502c7edcf25d4d |
| demo/scenario_library.md | 1936 | 231589f27b600c11 |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 3174 | b986a9d03a2293b7 |
| demo/troubleshoot.md | 2357 | ae74fa8998c303f0 |
| demo/trust_report.json | 5130 | 036222b32c7e7a4f |
| demo/trust_report.md | 3128 | 54d891a58b6984be |
| demo/visual_receipt.html | 3104 | ef267e6e134e7fcb |
| demo/visual_receipt.json | 3350 | 588f2f479e94550a |
| demo/visual_receipt.svg | 2519 | 4fafd5e3bf33d7af |
| demo/workflow_protocol.html | 2971 | 8222cb0092381551 |
| demo/workflow_protocol.json | 3557 | 26555f1efd6289b6 |
| demo/workflow_protocol.md | 2397 | 33bcfea129ebdfc7 |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 832 | e2eccdcc2248f66d |
| skills/agent/macro-policy-thesis-map/SKILL.md | 4775 | 6414e2bbb4630894 |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 25925 | d1fe1bd81232c338 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
