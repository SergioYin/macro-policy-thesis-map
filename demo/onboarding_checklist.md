# Evaluator Onboarding Checklist

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Status: ready

Passed: 5 / 5

Missing: 0

## Checks

| Check | Result | Artifact | Action |
| --- | --- | --- | --- |
| read_boundaries | pass | README.md | Confirm the evaluator understands this is static research tooling, not investment advice. |
| inspect_command_matrix | pass | demo/command_matrix.json | Review command inputs, outputs, and safety posture before running generators. |
| review_evidence_bundle | pass | demo/evidence_bundle.json | Use local hashes and fixture records as the starting evidence set. |
| confirm_public_readiness | pass | demo/public_readiness.json | Treat readiness blockers as stop conditions before sharing artifacts. |
| confirm_boundary_attestation | pass | demo/boundary_attestation.json | Verify no live data, workflows, private references, broker actions, or advice are in scope. |

## Onboarding Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli fixture-doctor --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli command-matrix --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli evidence-bundle --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli onboarding-checklist --root . |

## Stop Conditions

| Condition |
| --- |
| public-readiness is not ready |
| boundary-attestation is not attested |
| fixture-doctor reports blockers |
| public-scan reports private or credential-shaped text |
| requested output requires live data, broker access, trading instructions, or personalized financial advice |

## Handoff Artifacts

| Path |
| --- |
| demo/onboarding_checklist.md |
| demo/onboarding_checklist.json |
| demo/maintainer_handoff.md |
| demo/maintainer_handoff.json |

## Missing Artifacts

| Path |
| --- |
| none |
