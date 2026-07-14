# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.5.0

Status: ready

Score: 5 / 5

## Rubric Mapping

| Rubric | Result | Description | Evidence mapping |
| --- | --- | --- | --- |
| static_inputs | pass | Static fixtures and synthetic public examples are present. | examples, case_gallery, sensitivity_layer, exposure_layer |
| review_controls | pass | Review artifacts, hashes, and owner pack are present. | visual_receipt, release_owner_pack |
| public_package | pass | Package metadata, docs, license, and agent skill are present. | package, readme, license, skill |
| verification | pass | Tests exist and no workflow files are required. | tests, no_workflows |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/command_matrix.json | 10065 | 7b08a63b9e1de027 |
| demo/evidence_bundle.json | 7493 | dfdedc681fb28659 |
| demo/maturity_report.json | 1088 | ebda2801902de5c0 |
| demo/public_readiness.json | 1176 | 6c77e1bbdc99d8e9 |
| demo/release_manifest.json | 8501 | 58f8c0a362e01524 |
| tests/test_cli.py | 12490 | fb13045aef6b55b9 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
