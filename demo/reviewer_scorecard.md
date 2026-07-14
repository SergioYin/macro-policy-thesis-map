# Reviewer Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

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
| demo/api_reference.json | 48075 | 9abbaa7e95e8ef92 |
| demo/artifact_index.json | 27781 | 9b636f1a40213802 |
| demo/assumption_registry.json | 2500 | 8c9211fd74cc7585 |
| demo/benchmark_suite.json | 3043 | fecc433c113c786f |
| demo/boundary_attestation.json | 2101 | 32d1ff7a15c7debe |
| demo/citation_map.json | 5936 | 25e37ca20e0c62c1 |
| demo/cli_help.json | 22661 | 39e89a7e1135aff2 |
| demo/command_matrix.json | 23850 | 5e97ff48b0bb0929 |
| demo/compatibility_report.json | 2400 | 56be342014d705ad |
| demo/data_dictionary_diff.json | 3472 | bfd4b231f59dc583 |
| demo/docs_export.json | 9415 | bb2d6fe136439981 |
| demo/evaluator_scorecard.json | 2257 | e87c0940fbff005d |
| demo/evidence_bundle.json | 19080 | b0bd94074e5f9486 |
| demo/example_pack.json | 3795 | 80c1af31fba09765 |
| demo/golden_fixtures.json | 4685 | acea7ebf0a09c9d1 |
| demo/integration_cookbook.json | 3546 | 4cc09db548a7c957 |
| demo/landing_page.json | 6046 | 99596e5e7fb494f2 |
| demo/maintainer_guide.json | 2623 | b448c5bdd76bec62 |
| demo/maturity_report.json | 1685 | 7c6686ce06ac79b2 |
| demo/provenance_ledger.json | 27062 | ec5015ff728ecde2 |
| demo/public_readiness.json | 2610 | 8b91002e3689db66 |
| demo/readme_snippet.json | 6230 | 238a74942c1c2adb |
| demo/regression_summary.json | 3662 | 7585f3c1dc78ba14 |
| demo/release_faq.json | 2887 | 0f235c2a8d40f672 |
| demo/release_manifest.json | 18568 | dc52cccb72090ed5 |
| demo/release_notes_draft.json | 2248 | e14d99fc40369c0f |
| demo/reproducibility_recipe.json | 10807 | 7fe88eeb7faedd9c |
| demo/roadmap_next.json | 2452 | 629518ec9ea03f23 |
| demo/scenario_library.json | 2903 | a8c13fa73022fd96 |
| demo/troubleshoot.json | 3174 | f2577b71f0b54928 |
| demo/trust_report.json | 5130 | f6249b9e4c8d4171 |
| demo/workflow_protocol.json | 3557 | dfa240e52ed0ec75 |
| tests/test_cli.py | 26456 | 0461a69d708e22f2 |
| tests/test_safety.py | 1388 | d50fc2a2e87e8002 |
