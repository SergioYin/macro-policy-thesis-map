# Release Audit Summary

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Status: ready

Evidence: 17

Missing: 0

Blockers: 0

## Sections

| Section | Present | Evidence |
| --- | --- | --- |
| release | 4 | 4 |
| verification | 4 | 4 |
| public_safety | 4 | 4 |
| promotion_readiness | 5 | 5 |

## Evidence

| Section | Name | Status | Path | Field | Value | SHA-256 prefix |
| --- | --- | --- | --- | --- | --- | --- |
| release | release_manifest | present | demo/release_manifest.json | artifact_count | 113 | 70bc1fb99bb5eabd |
| release | release_notes | present | demo/release_notes_draft.json | status | ready | e14d99fc40369c0f |
| release | provenance | present | demo/provenance_ledger.json | present_artifact_count | 107 | ec5015ff728ecde2 |
| release | reproducibility | present | demo/reproducibility_recipe.json | step_count | 51 | 7fe88eeb7faedd9c |
| verification | regression | present | demo/regression_summary.json | status | ready | 7585f3c1dc78ba14 |
| verification | public_readiness | present | demo/public_readiness.json | status | ready | 8b91002e3689db66 |
| verification | golden_fixtures | present | demo/golden_fixtures.json | status | ready | acea7ebf0a09c9d1 |
| verification | compatibility | present | demo/compatibility_report.json | status | ready | 56be342014d705ad |
| public_safety | boundary_attestation | present | demo/boundary_attestation.json | status | attested | 32d1ff7a15c7debe |
| public_safety | trust_report | present | demo/trust_report.json | status | ready | 902eafc01db72132 |
| public_safety | citation_map | present | demo/citation_map.json | missing_count | 0 | 1c3b7eff9d04cd1d |
| public_safety | evaluator_scorecard | present | demo/evaluator_scorecard.json | status | ready | e87c0940fbff005d |
| promotion_readiness | adoption_notes | present | demo/adoption_notes.json | public_readiness_status | ready | 7440970ffd5317e1 |
| promotion_readiness | reviewer_scorecard | present | demo/reviewer_scorecard.json | status | ready | 99477329b486f41b |
| promotion_readiness | release_deck | present | demo/release_deck.json | slide_count | 5 | a97490a0e4c3565f |
| promotion_readiness | bundle_export | present | demo/bundle_export/manifest.json | status | ready | 8d6ae90c9ea2b3d0 |
| promotion_readiness | evidence_bundle | present | demo/evidence_bundle.json | status | ready | b0bd94074e5f9486 |

## Reviewer Focus

| Focus |
| --- |
| Release evidence: manifest, notes, provenance, and reproducibility recipe. |
| Verification evidence: regression summary, readiness, golden fixtures, and compatibility report. |
| Public safety evidence: boundary attestation, trust report, citation map, and evaluator scorecard. |
| Promotion readiness evidence: adoption notes, reviewer scorecard, release deck, bundle export, and evidence bundle. |

## Blockers

| Blocker |
| --- |
| none |
