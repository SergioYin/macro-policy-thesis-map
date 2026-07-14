# Quickstart Check

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Status: ready

Passed: 8 / 8

## Checks

| Check | Result | Path |
| --- | --- | --- |
| readme_available | pass | README.md |
| package_metadata_available | pass | pyproject.toml |
| example_events_available | pass | examples/macro_events.csv |
| bundled_events_available | pass | src/macro_policy_thesis_map/examples/macro_events.csv |
| example_sensitivities_available | pass | examples/thesis_sensitivities.csv |
| example_exposures_available | pass | examples/portfolio_exposures.csv |
| skill_available | pass | skills/agent/macro-policy-thesis-map/SKILL.md |
| tests_available | pass | tests/test_*.py |

## Starter Commands

| Command | Expected outputs |
| --- | --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli build-packet --root . | demo/thesis_packet.md, demo/thesis_packet.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli compare-history --root . | demo/history_comparison.md, demo/history_comparison.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli review-ledger --root . | demo/review_ledger.md, demo/review_ledger.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli static-dashboard --root . | demo/static_dashboard.html |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli thesis-impact-brief --root . | demo/thesis_impact_brief.md, demo/thesis_impact_brief.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli exposure-map --root . | demo/exposure_map.md, demo/exposure_map.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root . | demo/scenario_library.md, demo/scenario_library.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root . | demo/assumption_registry.md, demo/assumption_registry.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root . | demo/data_dictionary_diff.md, demo/data_dictionary_diff.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli case-gallery --root . | demo/case_gallery.md, demo/case_gallery.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli visual-receipt --root . | demo/visual_receipt.svg or demo/visual_receipt.html, demo/visual_receipt.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli fixture-doctor --root . | demo/fixture_doctor.md, demo/fixture_doctor.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli schema-export --root . | demo/input_schema.md, demo/input_schema.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . | demo/troubleshoot.md, demo/troubleshoot.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . | demo/docs_export.md, demo/docs_export.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli readme-snippet --root . | demo/readme_snippet.md, demo/readme_snippet.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root . | demo/cli_help.md, demo/cli_help.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli quickstart-check --root . | demo/quickstart_check.md, demo/quickstart_check.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli command-matrix --root . | demo/command_matrix.md, demo/command_matrix.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root . | demo/adoption_notes.md, demo/adoption_notes.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root . | demo/reviewer_scorecard.md, demo/reviewer_scorecard.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root . | demo/release_deck.md, demo/release_deck.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root . | demo/bundle_export/manifest.md, demo/bundle_export/manifest.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root . | demo/benchmark_suite.md, demo/benchmark_suite.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root . | demo/integration_cookbook.md, demo/integration_cookbook.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root . | demo/compatibility_report.md, demo/compatibility_report.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root . | demo/maintainer_guide.md, demo/maintainer_guide.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root . | demo/golden_fixtures.md, demo/golden_fixtures.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root . | demo/regression_summary.md, demo/regression_summary.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root . | demo/landing_page.md, demo/landing_page.json, demo/landing_page.html |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root . | demo/api_reference.md, demo/api_reference.json, demo/api_reference.html |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root . | demo/workflow_protocol.md, demo/workflow_protocol.json, demo/workflow_protocol.html |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root . | demo/example_pack.md, demo/example_pack.json, demo/example_pack.html |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root . | demo/roadmap_next.md, demo/roadmap_next.json, demo/roadmap_next.html |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root . | demo/trust_report.md, demo/trust_report.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root . | demo/citation_map.md, demo/citation_map.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root . | demo/release_faq.md, demo/release_faq.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root . | demo/artifact_index.md, demo/artifact_index.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root . | demo/evaluator_scorecard.md, demo/evaluator_scorecard.json |
