# Public Integration Cookbook

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Recipe count: 4

## Recipes

| Recipe | Name | Goal | Commands | Inputs | Outputs | Guardrails |
| --- | --- | --- | --- | --- | --- | --- |
| recipe-001 | Local CSV Evaluation | Evaluate a static event CSV from a clean checkout. | fixture-doctor --root . --events examples/macro_events.csv, build-packet --root ., review-ledger --root . | static event CSV with base event columns | demo/fixture_doctor.json, demo/thesis_packet.json, demo/review_ledger.json | No network calls, No broker access, No trade or allocation language |
| recipe-002 | Schema Adapter Review | Decide whether optional public fixture columns should be adopted. | schema-export --root ., scenario-library --root ., assumption-registry --root ., data-dictionary-diff --root . | built-in schema metadata | demo/input_schema.json, demo/scenario_library.json, demo/assumption_registry.json, demo/data_dictionary_diff.json | Keep optional columns additive, Keep scores bounded from 0 to 1, Do not add recommendation fields |
| recipe-003 | Public Artifact Review | Share deterministic local evidence with a public evaluator. | command-matrix --root ., evidence-bundle --root ., public-readiness --root ., visual-receipt --root . | demo artifacts and local source files | demo/command_matrix.json, demo/evidence_bundle.json, demo/public_readiness.json, demo/visual_receipt.json | Use hashes instead of private storage links, Do not add workflow files, Run public-scan before sharing |
| recipe-004 | Maintainer Release Check | Regenerate release owner surfaces before cutting a static public package. | maintainer-guide --root ., golden-fixtures --root ., regression-summary --root ., release-manifest --root ., diff-check --root . | repository files and synthetic fixtures | demo/maintainer_guide.json, demo/golden_fixtures.json, demo/regression_summary.json, demo/release_manifest.json | Keep zero runtime dependencies, Keep version metadata synchronized, Do not include private references |

## Integration Boundaries

| Boundary |
| --- |
| Recipes are command sequences for local static files. |
| Recipes do not describe private tools, CI workflows, upload destinations, live market feeds, or investment actions. |
