# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.0.0

Status: ready

Score: 6 / 6

## Rubric Mapping

| Rubric | Result | Description | Evidence mapping |
| --- | --- | --- | --- |
| static_inputs | pass | Static fixtures and synthetic public examples are present. | examples, case_gallery, sensitivity_layer, exposure_layer, schema_adaptation_surfaces |
| review_controls | pass | Review artifacts, operator docs, hashes, and owner pack are present. | visual_receipt, operator_surfaces, release_owner_pack |
| public_evaluator_hardening | pass | Benchmark, integration, compatibility, maintainer, golden fixture, and regression artifacts are present. | public_evaluator_hardening |
| public_package | pass | Package metadata, docs, license, and agent skill are present. | package, readme, license, skill |
| verification | pass | Tests exist and no workflow files are required. | tests, no_workflows |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/assumption_registry.json | 2500 | 70aecc7f328a8430 |
| demo/benchmark_suite.json | 3043 | 3f8b9be2e11158d9 |
| demo/cli_help.json | 14939 | 2e0d1c169d268305 |
| demo/command_matrix.json | 15540 | 5467cce33f686c5a |
| demo/compatibility_report.json | 1688 | 737f1a2d1377e5e4 |
| demo/data_dictionary_diff.json | 3472 | 894c3a7c3f46c635 |
| demo/docs_export.json | 4892 | 07f7d1874faaec4c |
| demo/evidence_bundle.json | 12337 | 50f995f62cd84c64 |
| demo/golden_fixtures.json | 4685 | 43567374f2468e4a |
| demo/integration_cookbook.json | 3546 | 4412ef0248807d31 |
| demo/maintainer_guide.json | 2216 | 66aeb9ddf7d23998 |
| demo/maturity_report.json | 1313 | 4b0c137ae12f6b3a |
| demo/public_readiness.json | 1732 | 4dd6c11f67f4d2c1 |
| demo/readme_snippet.json | 3080 | 94d243c825b24666 |
| demo/regression_summary.json | 1984 | d76fb5661bd590f4 |
| demo/release_manifest.json | 12659 | 8ff93441a6d2c1a4 |
| demo/scenario_library.json | 2903 | 6a6dfba6bf9c54a4 |
| demo/troubleshoot.json | 3174 | 623fae46fea5fc9e |
| tests/test_cli.py | 18727 | 803740be53d67ae8 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
