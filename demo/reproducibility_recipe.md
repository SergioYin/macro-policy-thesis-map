# Reproducibility Recipe

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Policy: Run from a source checkout with static files only; commands do not require network access.

Steps: 51

## Regeneration Steps

| Step | Command | Expected |
| --- | --- | --- |
| 1 | PYTHONPATH=src python -m macro_policy_thesis_map.cli build-packet --root . | deterministic demo artifact update |
| 2 | PYTHONPATH=src python -m macro_policy_thesis_map.cli compare-history --root . | deterministic demo artifact update |
| 3 | PYTHONPATH=src python -m macro_policy_thesis_map.cli review-ledger --root . | deterministic demo artifact update |
| 4 | PYTHONPATH=src python -m macro_policy_thesis_map.cli static-dashboard --root . | deterministic demo artifact update |
| 5 | PYTHONPATH=src python -m macro_policy_thesis_map.cli thesis-impact-brief --root . | deterministic demo artifact update |
| 6 | PYTHONPATH=src python -m macro_policy_thesis_map.cli exposure-map --root . | deterministic demo artifact update |
| 7 | PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root . | deterministic demo artifact update |
| 8 | PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root . | deterministic demo artifact update |
| 9 | PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root . | deterministic demo artifact update |
| 10 | PYTHONPATH=src python -m macro_policy_thesis_map.cli case-gallery --root . | deterministic demo artifact update |
| 11 | PYTHONPATH=src python -m macro_policy_thesis_map.cli visual-receipt --root . | deterministic demo artifact update |
| 12 | PYTHONPATH=src python -m macro_policy_thesis_map.cli fixture-doctor --root . | deterministic demo artifact update |
| 13 | PYTHONPATH=src python -m macro_policy_thesis_map.cli schema-export --root . | deterministic demo artifact update |
| 14 | PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . | deterministic demo artifact update |
| 15 | PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . | deterministic demo artifact update |
| 16 | PYTHONPATH=src python -m macro_policy_thesis_map.cli readme-snippet --root . | deterministic demo artifact update |
| 17 | PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root . | deterministic demo artifact update |
| 18 | PYTHONPATH=src python -m macro_policy_thesis_map.cli maturity-report --root . | deterministic demo artifact update |
| 19 | PYTHONPATH=src python -m macro_policy_thesis_map.cli quickstart-check --root . | deterministic demo artifact update |
| 20 | PYTHONPATH=src python -m macro_policy_thesis_map.cli command-matrix --root . | deterministic demo artifact update |
| 21 | PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root . | deterministic demo artifact update |
| 22 | PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root . | deterministic demo artifact update |
| 23 | PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root . | deterministic demo artifact update |
| 24 | PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root . | deterministic demo artifact update |
| 25 | PYTHONPATH=src python -m macro_policy_thesis_map.cli evidence-bundle --root . | deterministic demo artifact update |
| 26 | PYTHONPATH=src python -m macro_policy_thesis_map.cli public-readiness --root . | deterministic demo artifact update |
| 27 | PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root . | deterministic demo artifact update |
| 28 | PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root . | deterministic demo artifact update |
| 29 | PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root . | deterministic demo artifact update |
| 30 | PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root . | deterministic demo artifact update |
| 31 | PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root . | deterministic demo artifact update |
| 32 | PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root . | deterministic demo artifact update |
| 33 | PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root . | deterministic demo artifact update |
| 34 | PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root . | deterministic demo artifact update |
| 35 | PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root . | deterministic demo artifact update |
| 36 | PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root . | deterministic demo artifact update |
| 37 | PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root . | deterministic demo artifact update |
| 38 | PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root . | deterministic demo artifact update |
| 39 | PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root . | deterministic demo artifact update |
| 40 | PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root . | deterministic demo artifact update |
| 41 | PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root . | deterministic demo artifact update |
| 42 | PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root . | deterministic demo artifact update |
| 43 | PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root . | deterministic demo artifact update |
| 44 | PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root . | deterministic demo artifact update |
| 45 | PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root . | deterministic demo artifact update |
| 46 | PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root . | deterministic demo artifact update |
| 47 | PYTHONPATH=src python -m macro_policy_thesis_map.cli onboarding-checklist --root . | deterministic demo artifact update |
| 48 | PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-handoff --root . | deterministic demo artifact update |
| 49 | PYTHONPATH=src python -m macro_policy_thesis_map.cli release-audit-summary --root . | deterministic demo artifact update |
| 50 | PYTHONPATH=src python -m macro_policy_thesis_map.cli cold-start-walkthrough --root . | deterministic demo artifact update |
| 51 | PYTHONPATH=src python -m macro_policy_thesis_map.cli release-manifest --root . | release manifest records settled hashes |

## Release Gates

| Command |
| --- |
| PYTHONPATH=src python -m pytest |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
| python -c "import build_backend; build_backend.build_wheel('dist')" |

## Determinism Controls

| Control |
| --- |
| JSON writer sorts keys. |
| Markdown tables are generated from sorted command metadata and local file records. |
| Release manifest is written after generated governance artifacts settle. |
| diff-check compares SHA-256 values from the saved release manifest. |

## Unsupported

| Surface |
| --- |
| live data refresh |
| private storage |
| workflow automation |
| broker access |
| investment advice |
