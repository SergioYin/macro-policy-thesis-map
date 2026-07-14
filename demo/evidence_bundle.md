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
| README.md | 20613 | 71f5f2542b3a7bc9 |
| demo/api_reference.html | 15320 | d10c6848559b3806 |
| demo/api_reference.json | 48075 | 9abbaa7e95e8ef92 |
| demo/api_reference.md | 21476 | 759349ae803b2065 |
| demo/artifact_index.json | 27781 | af1407dccdf01b73 |
| demo/artifact_index.md | 10180 | 5155586fe7b55035 |
| demo/assumption_registry.json | 2500 | 8c9211fd74cc7585 |
| demo/assumption_registry.md | 1980 | 92e9c23a163dbb27 |
| demo/benchmark_suite.json | 3043 | fecc433c113c786f |
| demo/benchmark_suite.md | 1916 | 5f684baf6651cb7c |
| demo/boundary_attestation.json | 2101 | 32d1ff7a15c7debe |
| demo/boundary_attestation.md | 1485 | b16cadf6f0b49043 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/case_gallery.md | 1776 | 22a9ea47c93c5df5 |
| demo/citation_map.json | 5936 | 1c3b7eff9d04cd1d |
| demo/citation_map.md | 2132 | dc131b38b464e117 |
| demo/cli_help.json | 22661 | 39e89a7e1135aff2 |
| demo/cli_help.md | 15920 | a5633de330e238d6 |
| demo/cold_start_walkthrough.json | 4825 | 7b3233c8a2ac3343 |
| demo/cold_start_walkthrough.md | 3810 | 0d646cc4c4b95db0 |
| demo/command_matrix.json | 23850 | 5e97ff48b0bb0929 |
| demo/command_matrix.md | 16099 | 69d54545dd436bd4 |
| demo/compatibility_report.json | 2400 | 56be342014d705ad |
| demo/compatibility_report.md | 1634 | b07159a2749e0791 |
| demo/data_dictionary_diff.json | 3472 | bfd4b231f59dc583 |
| demo/data_dictionary_diff.md | 2177 | 0ef439b29e4ab000 |
| demo/docs_export.json | 9415 | 17f2fe2a942b558a |
| demo/docs_export.md | 4948 | 5b345bc0994b00c6 |
| demo/evaluator_scorecard.json | 2257 | e87c0940fbff005d |
| demo/evaluator_scorecard.md | 1757 | c193e2b0a29abbfa |
| demo/example_pack.html | 2945 | 594ec32edc81f6a7 |
| demo/example_pack.json | 3795 | 80c1af31fba09765 |
| demo/example_pack.md | 2132 | 9f7a9594b951d5fa |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/exposure_map.md | 1722 | 78bb263d749d469a |
| demo/fixture_doctor.json | 985 | 56410778254836de |
| demo/fixture_doctor.md | 534 | 6c06972b77c0882a |
| demo/golden_fixtures.json | 4685 | acea7ebf0a09c9d1 |
| demo/golden_fixtures.md | 1287 | 2b21512fc548f4c5 |
| demo/history_comparison.json | 1197 | 999b0f50d04e7fa9 |
| demo/history_comparison.md | 635 | aaa45f9f26551651 |
| demo/input_schema.json | 2845 | 19a2195c2cca5011 |
| demo/input_schema.md | 1997 | abda2e77f30468e7 |
| demo/integration_cookbook.json | 3546 | 4cc09db548a7c957 |
| demo/integration_cookbook.md | 2480 | 0a323ed74290b7e4 |
| demo/landing_page.html | 3860 | 120a784348fd24fe |
| demo/landing_page.json | 6046 | 99596e5e7fb494f2 |
| demo/landing_page.md | 3222 | 0d8df38c7eb0b574 |
| demo/maintainer_guide.json | 2623 | b448c5bdd76bec62 |
| demo/maintainer_guide.md | 2367 | a4b9ca5fbc9d28d3 |
| demo/maintainer_handoff.json | 3508 | 3679cbe6be3393d4 |
| demo/maintainer_handoff.md | 2429 | ba048068413333d7 |
| demo/maturity_report.json | 1685 | 7c6686ce06ac79b2 |
| demo/maturity_report.md | 874 | d635e979d3cc455d |
| demo/onboarding_checklist.json | 2593 | 0b0183d29083835a |
| demo/onboarding_checklist.md | 2209 | 78e2bb39032145d1 |
| demo/provenance_ledger.json | 27062 | ec5015ff728ecde2 |
| demo/provenance_ledger.md | 10209 | 0d1ce951440bd816 |
| demo/public_readiness.json | 2610 | 8b91002e3689db66 |
| demo/public_readiness.md | 1865 | 504769b1ffdbaaab |
| demo/quickstart_check.json | 11135 | a5a46f94ea40db7d |
| demo/quickstart_check.md | 7048 | 75e068d228e7e1f3 |
| demo/readme_snippet.json | 6230 | 238a74942c1c2adb |
| demo/readme_snippet.md | 3503 | 4bd11cc1348c2438 |
| demo/regression_summary.json | 3662 | 7585f3c1dc78ba14 |
| demo/regression_summary.md | 2843 | f738f4411d07d5eb |
| demo/release_faq.json | 2887 | 0f235c2a8d40f672 |
| demo/release_faq.md | 1951 | f0950c960ebe8349 |
| demo/release_notes_draft.json | 2248 | e14d99fc40369c0f |
| demo/release_notes_draft.md | 2185 | f6775912d1f48829 |
| demo/reproducibility_recipe.json | 10807 | 7fe88eeb7faedd9c |
| demo/reproducibility_recipe.md | 7738 | c8dfdd37e1f233f1 |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/review_ledger.md | 367 | c19af376680eae28 |
| demo/roadmap_next.html | 2785 | 9d18903ea0673853 |
| demo/roadmap_next.json | 2452 | 629518ec9ea03f23 |
| demo/roadmap_next.md | 1954 | 74a9ca8278d4e62e |
| demo/scenario_library.json | 2903 | a8c13fa73022fd96 |
| demo/scenario_library.md | 1936 | f9f19dcc7f58cfbd |
| demo/static_dashboard.html | 2398 | 07515c531d20fbfe |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/thesis_impact_brief.md | 2240 | 36867e04943f1a4a |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/thesis_packet.md | 1401 | 03769420c7f83604 |
| demo/troubleshoot.json | 3174 | f2577b71f0b54928 |
| demo/troubleshoot.md | 2357 | 5a6675bf160aafa7 |
| demo/trust_report.json | 5130 | 902eafc01db72132 |
| demo/trust_report.md | 3128 | 62f8f18e4bfa9b90 |
| demo/visual_receipt.html | 3104 | a7e0dd3e0f994b76 |
| demo/visual_receipt.json | 3350 | 4144cd27dd4a07e0 |
| demo/visual_receipt.svg | 2519 | c099d5375752c582 |
| demo/workflow_protocol.html | 2971 | cf4b17983e3dc52e |
| demo/workflow_protocol.json | 3557 | dfa240e52ed0ec75 |
| demo/workflow_protocol.md | 2397 | 600a27b91f4d887e |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| pyproject.toml | 832 | 76e96e006cdb2620 |
| skills/agent/macro-policy-thesis-map/SKILL.md | 4869 | 5f0c177b4e3ec83e |
| tests/test_build_backend.py | 1615 | eb712723fe64465d |
| tests/test_cli.py | 26456 | 0461a69d708e22f2 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
