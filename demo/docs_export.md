# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Status: ready

Documents: 32

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 20213 | bd9e1705b4ad4609 | Primary operator and evaluator documentation. |
| API reference | demo/api_reference.md | 21138 | e765a0f16dea6f5e | Command, artifact, and data-contract reference. |
| Artifact index | demo/artifact_index.md | 10075 | a7e3d8ff9c7c8520 | Demo artifact producers, formats, sizes, and hashes. |
| Assumption registry | demo/assumption_registry.md | 1980 | b0f851a867a3216d | Bounded public assumptions and validation controls. |
| Benchmark suite | demo/benchmark_suite.md | 1916 | 86a7f8561a279961 | Static synthetic evaluator benchmark matrix. |
| Boundary attestation | demo/boundary_attestation.md | 1485 | 7d8b8c99e7410411 | Static finance boundary and public release attestation. |
| Citation map | demo/citation_map.md | 2058 | 0b833d20792bce5d | Public claim citations to local paths and hashes. |
| CLI help | demo/cli_help.md | 15558 | 27377a4cfac85de1 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 15708 | f6599d5a8f001d3e | Command inputs, outputs, and safety posture. |
| Compatibility report | demo/compatibility_report.md | 1548 | 010e133a6e655915 | Package and artifact compatibility gates. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | cfd3eb09350f1e49 | Base and optional CSV dictionary comparison. |
| Evaluator scorecard | demo/evaluator_scorecard.md | 1751 | 8d0d9e4c6069919a | Public evaluator readiness scorecard. |
| Example pack | demo/example_pack.md | 2132 | b06724bf250cfc33 | Stable public command recipes and expected artifacts. |
| Golden fixtures | demo/golden_fixtures.md | 1287 | a8d4b690ee52dd7e | Fixture hashes, schemas, and expected output counts. |
| Input schema | demo/input_schema.md | 1997 | 421c6402eea9862e | Static CSV schema and data dictionary. |
| Integration cookbook | demo/integration_cookbook.md | 2480 | dc5b28704653220f | Public-safe local integration recipes. |
| Landing page | demo/landing_page.md | 3222 | 680a264ce0740f73 | Public first-screen story and start-here commands. |
| Maintainer guide | demo/maintainer_guide.md | 2336 | 1d9901d4b3a63a35 | Release duties, order, and safety invariants. |
| Maintainer handoff | demo/maintainer_handoff.md | 2429 | 6bead6e0c9098ec6 | Maintainer artifact custody, release gates, and boundary duties. |
| Evaluator onboarding checklist | demo/onboarding_checklist.md | 2209 | 29e572d330eb545e | Final evaluator onboarding checks and stop conditions. |
| Provenance ledger | demo/provenance_ledger.md | 10109 | 83cf3b41216bee65 | Local source and artifact hash provenance. |
| README snippet | demo/readme_snippet.md | 3503 | 798d4ed518b2c24e | Compact copyable quickstart snippet. |
| Regression summary | demo/regression_summary.md | 2651 | 01303ace7d520486 | Static regression gate summary. |
| Release FAQ | demo/release_faq.md | 1894 | 9fae7126efe177af | First-time evaluator questions with local citations. |
| Release notes draft | demo/release_notes_draft.md | 2068 | 824520c2570ec470 | v1.4.0 public release notes draft. |
| Reproducibility recipe | demo/reproducibility_recipe.md | 7608 | e718e5f02c0a34cb | Deterministic regeneration order and release gates. |
| Roadmap next | demo/roadmap_next.md | 1954 | 0f979db08f83a7ff | Bounded public next steps and exclusions. |
| Scenario library | demo/scenario_library.md | 1936 | 231589f27b600c11 | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | ae74fa8998c303f0 | Operator diagnostics and recovery steps. |
| Trust report | demo/trust_report.md | 3128 | 844f8ac0e34502f3 | GitHub stranger trust evidence from local artifacts. |
| Workflow protocol | demo/workflow_protocol.md | 2397 | 33bcfea129ebdfc7 | Agent-ready local protocol and stop conditions. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 4775 | 6414e2bbb4630894 | Agent protocol and finance boundaries. |

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
