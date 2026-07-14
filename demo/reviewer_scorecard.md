# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.7.0

Status: ready

Score: 5 / 5

## Rubric Mapping

| Rubric | Result | Description | Evidence mapping |
| --- | --- | --- | --- |
| static_inputs | pass | Static fixtures and synthetic public examples are present. | examples, case_gallery, sensitivity_layer, exposure_layer, schema_adaptation_surfaces |
| review_controls | pass | Review artifacts, operator docs, hashes, and owner pack are present. | visual_receipt, operator_surfaces, release_owner_pack |
| public_package | pass | Package metadata, docs, license, and agent skill are present. | package, readme, license, skill |
| verification | pass | Tests exist and no workflow files are required. | tests, no_workflows |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/assumption_registry.json | 2500 | eaef6265dd5bc388 |
| demo/cli_help.json | 12469 | 194440fbdd3c0193 |
| demo/command_matrix.json | 12945 | 9cd774a589d103c9 |
| demo/data_dictionary_diff.json | 3472 | dfa75a46af746035 |
| demo/docs_export.json | 3333 | e58db956e3fbd5d8 |
| demo/evidence_bundle.json | 9875 | fa03db93b320d05b |
| demo/maturity_report.json | 1235 | c07499edebed7b3e |
| demo/public_readiness.json | 1522 | 9dccc86d5ebed1d5 |
| demo/readme_snippet.json | 1868 | a47fbc7eee8ad796 |
| demo/release_manifest.json | 10720 | 4b602d8cc944613e |
| demo/scenario_library.json | 2903 | 44d3f23eafdadeb3 |
| demo/troubleshoot.json | 3174 | fbd09082b63e674a |
| tests/test_cli.py | 15692 | dabaea10614c2404 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
