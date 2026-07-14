# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Status: ready

Documents: 30

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 19492 | 7cd2fe9dcb70f4ae | Primary operator and evaluator documentation. |
| API reference | demo/api_reference.md | 20311 | 37910cc4f52c4724 | Command, artifact, and data-contract reference. |
| Artifact index | demo/artifact_index.md | 9685 | a2201ada7f3d20bb | Demo artifact producers, formats, sizes, and hashes. |
| Assumption registry | demo/assumption_registry.md | 1980 | 3321107de459893a | Bounded public assumptions and validation controls. |
| Benchmark suite | demo/benchmark_suite.md | 1916 | 9037acb0cc47a879 | Static synthetic evaluator benchmark matrix. |
| Boundary attestation | demo/boundary_attestation.md | 1485 | 488105fdb8470163 | Static finance boundary and public release attestation. |
| Citation map | demo/citation_map.md | 2016 | eef84eac5b04c46c | Public claim citations to local paths and hashes. |
| CLI help | demo/cli_help.md | 14851 | 13cbcfa1d3053508 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 14929 | 87185ae268bfd471 | Command inputs, outputs, and safety posture. |
| Compatibility report | demo/compatibility_report.md | 1447 | e6914baf5ca32fd4 | Package and artifact compatibility gates. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | a64ba918055b0779 | Base and optional CSV dictionary comparison. |
| Evaluator scorecard | demo/evaluator_scorecard.md | 1715 | b5a82ced9745cbaf | Public evaluator readiness scorecard. |
| Example pack | demo/example_pack.md | 2132 | 8b6c0b536f95affb | Stable public command recipes and expected artifacts. |
| Golden fixtures | demo/golden_fixtures.md | 1287 | 82b2d1c321ff99c4 | Fixture hashes, schemas, and expected output counts. |
| Input schema | demo/input_schema.md | 1997 | 375a25ed52497363 | Static CSV schema and data dictionary. |
| Integration cookbook | demo/integration_cookbook.md | 2480 | f62ac0e3e755c8be | Public-safe local integration recipes. |
| Landing page | demo/landing_page.md | 3222 | 0e6eb500c7da3765 | Public first-screen story and start-here commands. |
| Maintainer guide | demo/maintainer_guide.md | 2278 | 7547ea596e8676b8 | Release duties, order, and safety invariants. |
| Provenance ledger | demo/provenance_ledger.md | 9743 | 2fccd87b38b1ff54 | Local source and artifact hash provenance. |
| README snippet | demo/readme_snippet.md | 3275 | a55a5c3027c81672 | Compact copyable quickstart snippet. |
| Regression summary | demo/regression_summary.md | 2312 | 54f5fe8515bb49b9 | Static regression gate summary. |
| Release FAQ | demo/release_faq.md | 1852 | ad7ac666d3b4ac69 | First-time evaluator questions with local citations. |
| Release notes draft | demo/release_notes_draft.md | 1880 | ebab1c802f5e5710 | v1.3.0 public release notes draft. |
| Reproducibility recipe | demo/reproducibility_recipe.md | 7352 | 6056669713187aee | Deterministic regeneration order and release gates. |
| Roadmap next | demo/roadmap_next.md | 1954 | 15e06375f6dcb59d | Bounded public next steps and exclusions. |
| Scenario library | demo/scenario_library.md | 1936 | bf179298255b14bd | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | ca95a276ea8f7efe | Operator diagnostics and recovery steps. |
| Trust report | demo/trust_report.md | 3128 | 795a095cfcc4f35a | GitHub stranger trust evidence from local artifacts. |
| Workflow protocol | demo/workflow_protocol.md | 2397 | bf183dd8ad9a4577 | Agent-ready local protocol and stop conditions. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 4591 | 07299c071a787ed4 | Agent protocol and finance boundaries. |

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
