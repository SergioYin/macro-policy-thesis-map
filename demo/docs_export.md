# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Status: ready

Documents: 26

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 17804 | 2544bbba66b1aa8f | Primary operator and evaluator documentation. |
| API reference | demo/api_reference.md | 18635 | 96426334358080c1 | Command, artifact, and data-contract reference. |
| Artifact index | demo/artifact_index.md | 8896 | fc183b4389f29d28 | Demo artifact producers, formats, sizes, and hashes. |
| Assumption registry | demo/assumption_registry.md | 1980 | 0300d98f2f5eecaf | Bounded public assumptions and validation controls. |
| Benchmark suite | demo/benchmark_suite.md | 1916 | 28305b62f844c032 | Static synthetic evaluator benchmark matrix. |
| Citation map | demo/citation_map.md | 1690 | d3e655c739c17fc5 | Public claim citations to local paths and hashes. |
| CLI help | demo/cli_help.md | 13461 | 02d4a0db172d9293 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 13509 | b2a1218e98d1247f | Command inputs, outputs, and safety posture. |
| Compatibility report | demo/compatibility_report.md | 1357 | 0cc97f2bfa740961 | Package and artifact compatibility gates. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | 43080d5bc3d487d0 | Base and optional CSV dictionary comparison. |
| Evaluator scorecard | demo/evaluator_scorecard.md | 1335 | 743673aa00d75e1c | Public evaluator readiness scorecard. |
| Example pack | demo/example_pack.md | 2132 | e5b600b5a1f1a446 | Stable public command recipes and expected artifacts. |
| Golden fixtures | demo/golden_fixtures.md | 1287 | e3b9cc07f8f7402c | Fixture hashes, schemas, and expected output counts. |
| Input schema | demo/input_schema.md | 1997 | c62f5d75f7fa35cd | Static CSV schema and data dictionary. |
| Integration cookbook | demo/integration_cookbook.md | 2480 | 64d584a9f491472a | Public-safe local integration recipes. |
| Landing page | demo/landing_page.md | 3222 | 08ae9bad5f9805c9 | Public first-screen story and start-here commands. |
| Maintainer guide | demo/maintainer_guide.md | 2160 | 5c6bcce3dfeca5f2 | Release duties, order, and safety invariants. |
| README snippet | demo/readme_snippet.md | 2815 | c19125c5c9f7d486 | Compact copyable quickstart snippet. |
| Regression summary | demo/regression_summary.md | 1711 | 8d15612225ea8c07 | Static regression gate summary. |
| Release FAQ | demo/release_faq.md | 1537 | ed5a3bf8f0daa89e | First-time evaluator questions with local citations. |
| Roadmap next | demo/roadmap_next.md | 1954 | e20df3db1b243b32 | Bounded public next steps and exclusions. |
| Scenario library | demo/scenario_library.md | 1936 | 0402d234f5250f31 | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | 994fc517414a6d56 | Operator diagnostics and recovery steps. |
| Trust report | demo/trust_report.md | 2303 | ab9572cb36631edc | GitHub stranger trust evidence from local artifacts. |
| Workflow protocol | demo/workflow_protocol.md | 2397 | 9511beb364af7159 | Agent-ready local protocol and stop conditions. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 4226 | 482b63068e523668 | Agent protocol and finance boundaries. |

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
