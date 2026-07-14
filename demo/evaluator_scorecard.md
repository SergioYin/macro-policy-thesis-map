# Evaluator Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Status: needs-review

Score: 6 / 7

## Checks

| Check | Result | Evidence | Detail |
| --- | --- | --- | --- |
| trust_report_ready | pass | demo/trust_report.json | Trust report scores local evidence for a first-time GitHub visitor. |
| citation_map_complete | pass | demo/citation_map.json | Public claims cite local artifacts with paths and hashes. |
| artifact_index_complete | review | demo/artifact_index.json | Demo artifacts have producer commands, formats, and hashes. |
| public_readiness_ready | pass | demo/public_readiness.json | Readiness gates pass for local public release evidence. |
| tests_present | pass | tests/test_*.py | Local pytest suite is present for evaluator reruns. |
| boundaries_visible | pass | README.md, skills/agent/macro-policy-thesis-map/SKILL.md, demo/release_faq.json, demo/boundary_attestation.json | Research-only boundaries are documented in human and agent surfaces. |
| governance_layer_present | pass | demo/boundary_attestation.json, demo/provenance_ledger.json, demo/reproducibility_recipe.json, demo/release_notes_draft.json | v1.3.0 governance artifacts are available for public release review. |

## Recommended Order

| Step | Command |
| --- | --- |
| 1 | trust-report |
| 2 | citation-map |
| 3 | release-faq |
| 4 | artifact-index |
| 5 | evaluator-scorecard |
| 6 | boundary-attestation |
| 7 | provenance-ledger |
| 8 | reproducibility-recipe |
| 9 | release-notes-draft |
