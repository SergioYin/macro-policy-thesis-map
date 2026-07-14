# Example Pack

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Fixture policy: Bundled and top-level examples are synthetic static fixtures for deterministic local evaluation.

Recipes: 4

## Recipes

| Recipe | Name | Commands | Outputs | Expected JSON keys |
| --- | --- | --- | --- | --- |
| example-001 | Visitor Landing Preview | landing-page --root . | demo/landing_page.md, demo/landing_page.json, demo/landing_page.html | first_screen, featured_commands, boundaries |
| example-002 | Agent Protocol Reuse | workflow-protocol --root ., api-reference --root . | demo/workflow_protocol.json, demo/api_reference.json | phases, agent_contract, data_contracts |
| example-003 | Static Thesis Packet | fixture-doctor --root ., build-packet --root ., review-ledger --root . | demo/fixture_doctor.json, demo/thesis_packet.json, demo/review_ledger.json | status, policy_areas, findings |
| example-004 | Public Release Gates | public-readiness --root ., release-manifest --root ., diff-check --root . | demo/public_readiness.json, demo/release_manifest.json, stdout pass/fail | checks, artifacts, status |

## Fixtures

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| examples/prior_macro_events.csv | 715 | 95f9b30ce6f88581 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |

## Stable Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root . |
