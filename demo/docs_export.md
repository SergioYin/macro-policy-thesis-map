# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Status: ready

Documents: 33

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 20613 | 71f5f2542b3a7bc9 | Primary operator and evaluator documentation. |
| API reference | demo/api_reference.md | 21476 | 759349ae803b2065 | Command, artifact, and data-contract reference. |
| Artifact index | demo/artifact_index.md | 10180 | 11235ef9284f074f | Demo artifact producers, formats, sizes, and hashes. |
| Assumption registry | demo/assumption_registry.md | 1980 | 92e9c23a163dbb27 | Bounded public assumptions and validation controls. |
| Benchmark suite | demo/benchmark_suite.md | 1916 | 5f684baf6651cb7c | Static synthetic evaluator benchmark matrix. |
| Boundary attestation | demo/boundary_attestation.md | 1485 | b16cadf6f0b49043 | Static finance boundary and public release attestation. |
| Citation map | demo/citation_map.md | 2132 | e72db447edb12052 | Public claim citations to local paths and hashes. |
| CLI help | demo/cli_help.md | 15920 | a5633de330e238d6 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 16099 | 69d54545dd436bd4 | Command inputs, outputs, and safety posture. |
| Compatibility report | demo/compatibility_report.md | 1634 | b07159a2749e0791 | Package and artifact compatibility gates. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | 0ef439b29e4ab000 | Base and optional CSV dictionary comparison. |
| Evaluator scorecard | demo/evaluator_scorecard.md | 1757 | c193e2b0a29abbfa | Public evaluator readiness scorecard. |
| Example pack | demo/example_pack.md | 2132 | 9f7a9594b951d5fa | Stable public command recipes and expected artifacts. |
| Golden fixtures | demo/golden_fixtures.md | 1287 | 2b21512fc548f4c5 | Fixture hashes, schemas, and expected output counts. |
| Input schema | demo/input_schema.md | 1997 | abda2e77f30468e7 | Static CSV schema and data dictionary. |
| Integration cookbook | demo/integration_cookbook.md | 2480 | 0a323ed74290b7e4 | Public-safe local integration recipes. |
| Landing page | demo/landing_page.md | 3222 | 0d8df38c7eb0b574 | Public first-screen story and start-here commands. |
| Maintainer guide | demo/maintainer_guide.md | 2367 | a4b9ca5fbc9d28d3 | Release duties, order, and safety invariants. |
| Maintainer handoff | demo/maintainer_handoff.md | 2429 | ba048068413333d7 | Maintainer artifact custody, release gates, and boundary duties. |
| Evaluator onboarding checklist | demo/onboarding_checklist.md | 2209 | 78e2bb39032145d1 | Final evaluator onboarding checks and stop conditions. |
| Provenance ledger | demo/provenance_ledger.md | 10209 | 0d1ce951440bd816 | Local source and artifact hash provenance. |
| README snippet | demo/readme_snippet.md | 3503 | 4bd11cc1348c2438 | Compact copyable quickstart snippet. |
| Regression summary | demo/regression_summary.md | 2843 | f738f4411d07d5eb | Static regression gate summary. |
| Release audit summary | demo/release_audit_summary.md | 3056 | ca36ea1f8b9e892d | Final release, verification, public safety, and promotion readiness evidence. |
| Release FAQ | demo/release_faq.md | 1951 | f0950c960ebe8349 | First-time evaluator questions with local citations. |
| Release notes draft | demo/release_notes_draft.md | 2185 | f6775912d1f48829 | v1.5.0 public release notes draft. |
| Reproducibility recipe | demo/reproducibility_recipe.md | 7738 | c8dfdd37e1f233f1 | Deterministic regeneration order and release gates. |
| Roadmap next | demo/roadmap_next.md | 1954 | 74a9ca8278d4e62e | Bounded public next steps and exclusions. |
| Scenario library | demo/scenario_library.md | 1936 | f9f19dcc7f58cfbd | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | 5a6675bf160aafa7 | Operator diagnostics and recovery steps. |
| Trust report | demo/trust_report.md | 3128 | 90b0cb897bc3633a | GitHub stranger trust evidence from local artifacts. |
| Workflow protocol | demo/workflow_protocol.md | 2397 | 600a27b91f4d887e | Agent-ready local protocol and stop conditions. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 4869 | 5f0c177b4e3ec83e | Agent protocol and finance boundaries. |

## Missing

| Title | Path | Purpose |
| --- | --- | --- |
| none | none | none |

## Validation Commands

| Command |
| --- |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli readme-snippet --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root . |
