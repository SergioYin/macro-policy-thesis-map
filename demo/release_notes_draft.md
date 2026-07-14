# Release Notes Draft

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Release: v1.4.0 evaluator onboarding and maintainer handoff layer

Status: ready

## Highlights

| Highlight |
| --- |
| Added onboarding-checklist for final evaluator start-here gates, stop conditions, and artifact route checks. |
| Added maintainer-handoff for custody, release gates, version duties, and public static finance boundaries. |
| Kept governance artifacts, provenance, reproducibility, and release notes tied to deterministic local evidence. |
| Preserved zero runtime dependencies, static bundled fixtures, and no workflow automation. |

## Governance Artifacts

| Path |
| --- |
| demo/boundary_attestation.md |
| demo/provenance_ledger.md |
| demo/reproducibility_recipe.md |
| demo/release_notes_draft.md |
| demo/onboarding_checklist.md |
| demo/maintainer_handoff.md |

## Gate Summary

| Gate | Value |
| --- | --- |
| public_readiness_status | ready |
| regression_status | needs-review |
| boundary_status | attested |
| provenance_present_artifacts | 105 |
| reproducibility_steps | 50 |
| onboarding_status | ready |
| handoff_status | ready |

## Verification Commands

| Command |
| --- |
| PYTHONPATH=src python -m pytest |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
| python -c "import build_backend; build_backend.build_wheel('dist')" |

## Upgrade Notes

| Note |
| --- |
| Runtime dependencies remain empty. |
| Default finance fixtures remain static and synthetic. |
| No workflow files, private references, live data, broker actions, or finance advice were added. |
