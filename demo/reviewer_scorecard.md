# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.1.0

Status: ready

Score: 7 / 7

## Rubric Mapping

| Rubric | Result | Description | Evidence mapping |
| --- | --- | --- | --- |
| static_inputs | pass | Static fixtures and synthetic public examples are present. | examples, case_gallery, sensitivity_layer, exposure_layer, schema_adaptation_surfaces |
| review_controls | pass | Review artifacts, operator docs, hashes, and owner pack are present. | visual_receipt, operator_surfaces, release_owner_pack |
| public_evaluator_hardening | pass | Benchmark, integration, compatibility, maintainer, golden fixture, and regression artifacts are present. | public_evaluator_hardening |
| public_protocol_layer | pass | Landing, API reference, workflow protocol, example pack, and roadmap artifacts are present. | public_protocol_layer |
| public_package | pass | Package metadata, docs, license, and agent skill are present. | package, readme, license, skill |
| verification | pass | Tests exist and no workflow files are required. | tests, no_workflows |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/api_reference.json | 37394 | 7b89c11e4d5e9b45 |
| demo/assumption_registry.json | 2500 | 7170c7639ab9e790 |
| demo/benchmark_suite.json | 3043 | b491a34778eb237d |
| demo/cli_help.json | 17246 | 035477d512f32cb2 |
| demo/command_matrix.json | 18004 | 482bdb26f8278978 |
| demo/compatibility_report.json | 1822 | d2653a328dc17a98 |
| demo/data_dictionary_diff.json | 3472 | 3d2592dd48b9de32 |
| demo/docs_export.json | 6178 | 2689d46f2138c12c |
| demo/evidence_bundle.json | 15119 | 92a1e46d33c41910 |
| demo/example_pack.json | 3795 | 2a5f299bb12a9fe6 |
| demo/golden_fixtures.json | 4685 | 6e7b7638818afdf7 |
| demo/integration_cookbook.json | 3546 | 71823c83d849c943 |
| demo/landing_page.json | 6046 | 9001d5d562723f1c |
| demo/maintainer_guide.json | 2322 | c54064f0c7b0ab21 |
| demo/maturity_report.json | 1386 | 701cd3be902cb617 |
| demo/public_readiness.json | 1923 | 15d96adf743682be |
| demo/readme_snippet.json | 4028 | 2265ee4e3406200e |
| demo/regression_summary.json | 1984 | 5919c7ab743c5893 |
| demo/release_manifest.json | 15025 | f2564a94855db679 |
| demo/roadmap_next.json | 2452 | 5df60fe48a35e8be |
| demo/scenario_library.json | 2903 | 62d405892fb64c52 |
| demo/troubleshoot.json | 3174 | 9b2d5f00d46734a2 |
| demo/workflow_protocol.json | 3557 | 8a210ce7d2934354 |
| tests/test_cli.py | 21480 | 8e805ded13136580 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
