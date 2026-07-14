# Release Owner Adoption Notes

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.5.0

Maturity: ready (12 / 12)

Public readiness: ready

Release manifest artifacts: 50

## Release Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |

## Cold User Next Actions

| Action |
| --- |
| Run the quickstart commands from a clean checkout. |
| Review demo/reviewer_scorecard.md for any maturity item marked review. |
| Confirm demo/public_readiness.json remains ready after local edits. |
| Run public-scan and diff-check before sharing the bundle. |

## Safety Boundaries

| Boundary |
| --- |
| Use static files only. |
| Do not add workflow files, upload steps, or private references. |
| Do not fetch live data, connect to brokers, place orders, or provide financial advice. |
| Treat public-readiness blockers and reviewer-scorecard review items as release-owner follow-up. |

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| README.md | 8838 | f7a8424248d470ec |
| demo/cold_start_walkthrough.json | 2692 | c5944698c87f48f7 |
| demo/command_matrix.json | 10065 | 7b08a63b9e1de027 |
| demo/evidence_bundle.json | 7493 | dfdedc681fb28659 |
| demo/maturity_report.json | 1088 | ebda2801902de5c0 |
| demo/public_readiness.json | 1176 | 6c77e1bbdc99d8e9 |
| demo/release_manifest.json | 8501 | 58f8c0a362e01524 |
