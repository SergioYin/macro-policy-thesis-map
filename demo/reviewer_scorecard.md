# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.6.0

Status: ready

Score: 5 / 5

## Rubric Mapping

| Rubric | Result | Description | Evidence mapping |
| --- | --- | --- | --- |
| static_inputs | pass | Static fixtures and synthetic public examples are present. | examples, case_gallery, sensitivity_layer, exposure_layer |
| review_controls | pass | Review artifacts, operator docs, hashes, and owner pack are present. | visual_receipt, operator_surfaces, release_owner_pack |
| public_package | pass | Package metadata, docs, license, and agent skill are present. | package, readme, license, skill |
| verification | pass | Tests exist and no workflow files are required. | tests, no_workflows |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/cli_help.json | 11169 | fe922417f2a1ede9 |
| demo/command_matrix.json | 11650 | 1eb66dbe9204a2fa |
| demo/docs_export.json | 2521 | 27404a3954d073b7 |
| demo/evidence_bundle.json | 8900 | 8a4daf5c8c2f5c00 |
| demo/maturity_report.json | 1157 | 96cf4d616ecea361 |
| demo/public_readiness.json | 1355 | 26e502baf3e00996 |
| demo/readme_snippet.json | 1253 | ecb716a85d3e4108 |
| demo/release_manifest.json | 9745 | 5e498ecb61fc230f |
| demo/troubleshoot.json | 2732 | 7cf26ad10b287905 |
| tests/test_cli.py | 14315 | 1086bc049a77329d |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
