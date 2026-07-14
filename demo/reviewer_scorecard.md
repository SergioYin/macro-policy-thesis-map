# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Status: needs-review

Score: 8 / 9

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
| governance_attestation_layer | review | Boundary, provenance, reproducibility, and release-note artifacts are present. | governance_attestation_layer |
| public_readiness | pass | Public readiness command reports ready. | demo/public_readiness.json |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/api_reference.json | 45374 | 9babdb9e89dfc5ee |
| demo/artifact_index.json | 26413 | 934fe0fd1b8ce7a2 |
| demo/assumption_registry.json | 2500 | 496daa362b79b90a |
| demo/benchmark_suite.json | 3043 | 4a16814969e6dd12 |
| demo/boundary_attestation.json | 2101 | 521ff58189d124c5 |
| demo/citation_map.json | 5681 | 84ae750e57985800 |
| demo/cli_help.json | 21217 | 020c43e13a343233 |
| demo/command_matrix.json | 22248 | 7f61d38fdb211d10 |
| demo/compatibility_report.json | 2099 | fbf928894bc1ca24 |
| demo/data_dictionary_diff.json | 3472 | 510e5713493d6f3d |
| demo/docs_export.json | 8541 | 1e0994200d487257 |
| demo/evaluator_scorecard.json | 2214 | 79c7961fbc7b64f0 |
| demo/evidence_bundle.json | 18426 | a3c4962c0db96247 |
| demo/example_pack.json | 3795 | b2704c9a6deba147 |
| demo/golden_fixtures.json | 4685 | 6918a9dc69858c85 |
| demo/integration_cookbook.json | 3546 | 25d215e91152aa50 |
| demo/landing_page.json | 6046 | 23e0a951b8946771 |
| demo/maintainer_guide.json | 2540 | 6713131f87a78e8c |
| demo/maturity_report.json | 1544 | 16497ee75188fbd0 |
| demo/provenance_ledger.json | 25808 | b41da876e3c9d36b |
| demo/public_readiness.json | 2301 | b2e51d04d172c6ca |
| demo/readme_snippet.json | 5816 | ce0ab69a9191c53c |
| demo/regression_summary.json | 2966 | 75a04ffefd4176b1 |
| demo/release_faq.json | 2778 | e1d0a5c2660c6411 |
| demo/release_manifest.json | 17914 | e209ffc1f60d18a8 |
| demo/release_notes_draft.json | 1922 | c1819fef3ab960e5 |
| demo/reproducibility_recipe.json | 10241 | c171be145870f412 |
| demo/roadmap_next.json | 2452 | 6a5aec3071917e7e |
| demo/scenario_library.json | 2903 | 8997f1e9baaefcfa |
| demo/troubleshoot.json | 3174 | f03de8b53641563b |
| demo/trust_report.json | 5130 | edf2cf57246dad6e |
| demo/workflow_protocol.json | 3557 | 01116e3fb6b402c8 |
| tests/test_cli.py | 25101 | dc9f2c894fc63c8d |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
