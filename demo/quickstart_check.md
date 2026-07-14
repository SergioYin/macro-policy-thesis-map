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
