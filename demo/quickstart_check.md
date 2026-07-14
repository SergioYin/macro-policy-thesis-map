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
| PYTHONPATH=src python -m macro_policy_thesis_map.cli quickstart-check --root . | demo/quickstart_check.md, demo/quickstart_check.json |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli command-matrix --root . | demo/command_matrix.md, demo/command_matrix.json |
