# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Status: ready

Score: 9 / 9

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
| governance_attestation_layer | pass | Boundary, provenance, reproducibility, and release-note artifacts are present. | governance_attestation_layer |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/api_reference.json | 47299 | b82a42e9cbf67437 |
| demo/artifact_index.json | 27463 | 6e767512e0bcd303 |
| demo/assumption_registry.json | 2500 | 24f1cb2faaf193e6 |
| demo/benchmark_suite.json | 3043 | 287d3fd6ac67014f |
| demo/boundary_attestation.json | 2101 | 3aaf0a1cff28aa03 |
| demo/citation_map.json | 5723 | 1efa53e66056991d |
| demo/cli_help.json | 22174 | 49979ac371db2feb |
| demo/command_matrix.json | 23315 | 6655681f7e419648 |
| demo/compatibility_report.json | 2257 | 0a222de323e14ab6 |
| demo/data_dictionary_diff.json | 3472 | b1c9f49c0cbf3f3d |
| demo/docs_export.json | 9113 | 7abe99a8aeda92bf |
| demo/evaluator_scorecard.json | 2250 | 4e534075cd200132 |
| demo/evidence_bundle.json | 19080 | c2985ca1793291c8 |
| demo/example_pack.json | 3795 | 935a6dab9ce220cf |
| demo/golden_fixtures.json | 4685 | 99a3213b8530a9a4 |
| demo/integration_cookbook.json | 3546 | a4c794f009d7bede |
| demo/landing_page.json | 6046 | 9ff1501b33a0058f |
| demo/maintainer_guide.json | 2594 | 23c3bcd8b3958d2a |
| demo/maturity_report.json | 1622 | 02f3a3edd8df91a3 |
| demo/provenance_ledger.json | 26766 | 16af0d34681e26e4 |
| demo/public_readiness.json | 2471 | d45135eba9e8effb |
| demo/readme_snippet.json | 6230 | 99265ac326496199 |
| demo/regression_summary.json | 3389 | 55721620ea052ddc |
| demo/release_faq.json | 2820 | b62bd3e5721b08ca |
| demo/release_manifest.json | 18568 | 365a3a8944e17c4a |
| demo/release_notes_draft.json | 2124 | f62415c15621be64 |
| demo/reproducibility_recipe.json | 10617 | 5031cf7d6615be3b |
| demo/roadmap_next.json | 2452 | 394394f2afe8618f |
| demo/scenario_library.json | 2903 | cc502c7edcf25d4d |
| demo/troubleshoot.json | 3174 | b986a9d03a2293b7 |
| demo/trust_report.json | 5130 | 212ac784fdce5843 |
| demo/workflow_protocol.json | 3557 | 26555f1efd6289b6 |
| tests/test_cli.py | 25925 | d1fe1bd81232c338 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
