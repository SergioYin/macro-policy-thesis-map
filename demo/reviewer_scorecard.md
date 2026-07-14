# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Status: ready

Score: 8 / 8

## Rubric Mapping

| Rubric | Result | Description | Evidence mapping |
| --- | --- | --- | --- |
| static_inputs | pass | Static fixtures and synthetic public examples are present. | examples, case_gallery, sensitivity_layer, exposure_layer, schema_adaptation_surfaces |
| review_controls | pass | Review artifacts, operator docs, hashes, and owner pack are present. | visual_receipt, operator_surfaces, release_owner_pack |
| public_evaluator_hardening | pass | Benchmark, integration, compatibility, maintainer, golden fixture, and regression artifacts are present. | public_evaluator_hardening |
| public_protocol_layer | pass | Landing, API reference, workflow protocol, example pack, and roadmap artifacts are present. | public_protocol_layer |
| public_trust_layer | pass | Trust report, citation map, release FAQ, artifact index, and evaluator scorecard are present. | public_trust_layer |
| public_package | pass | Package metadata, docs, license, and agent skill are present. | package, readme, license, skill |
| verification | pass | Tests exist and no workflow files are required. | tests, no_workflows |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/api_reference.json | 41652 | 459ceec67aa61f46 |
| demo/artifact_index.json | 24304 | 1fe20b2960e171da |
| demo/assumption_registry.json | 2500 | de075c9b3fb8f456 |
| demo/benchmark_suite.json | 3043 | 6ee09b77f1d4f5aa |
| demo/citation_map.json | 4645 | cb3e09d776b4e334 |
| demo/cli_help.json | 19327 | 632452d87990f5f1 |
| demo/command_matrix.json | 20252 | 0eedc17d3bea61f2 |
| demo/compatibility_report.json | 1952 | 6c3056202895e6f5 |
| demo/data_dictionary_diff.json | 3472 | 41ecef87918921c8 |
| demo/docs_export.json | 7471 | 71935492ff33c6e4 |
| demo/evaluator_scorecard.json | 1762 | a9406e7b779c266d |
| demo/evidence_bundle.json | 17114 | 8d272626babf708f |
| demo/example_pack.json | 3795 | 7cb7f9c3f2b0fc25 |
| demo/golden_fixtures.json | 4685 | f6c5648518f62a1b |
| demo/integration_cookbook.json | 3546 | 8a9ed4d4f1bc0b6f |
| demo/landing_page.json | 6046 | 1d5dd327d5deed49 |
| demo/maintainer_guide.json | 2430 | de0a35b7e0901089 |
| demo/maturity_report.json | 1456 | 73c8213cb4b0c095 |
| demo/public_readiness.json | 2116 | ea95c96e19cefec9 |
| demo/readme_snippet.json | 4982 | 1b317fea0dfb9a9f |
| demo/regression_summary.json | 2275 | 784262d381778f1f |
| demo/release_faq.json | 2295 | 5aafef8f95cd0962 |
| demo/release_manifest.json | 16603 | 50d89640ff5572c5 |
| demo/roadmap_next.json | 2452 | 3928f2c8b8502c9a |
| demo/scenario_library.json | 2903 | a10db1111ec03d96 |
| demo/troubleshoot.json | 3174 | dbbbecdae18d1dc9 |
| demo/trust_report.json | 3747 | 90e576c5b6525744 |
| demo/workflow_protocol.json | 3557 | d9e8eb649bda291f |
| tests/test_cli.py | 23575 | e4e74cefb38973a1 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
