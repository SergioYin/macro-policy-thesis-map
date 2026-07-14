# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.1.0

Status: ready

Documents: 21

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 16096 | 14c1a4e5d37ae040 | Primary operator and evaluator documentation. |
| API reference | demo/api_reference.md | 16800 | bb9e2f53d48fd5f7 | Command, artifact, and data-contract reference. |
| Assumption registry | demo/assumption_registry.md | 1980 | 792c443afe9f7ecd | Bounded public assumptions and validation controls. |
| Benchmark suite | demo/benchmark_suite.md | 1916 | b7889665139c122e | Static synthetic evaluator benchmark matrix. |
| CLI help | demo/cli_help.md | 12005 | 0fcb37ae7a358d34 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 11981 | 23bf912e47074965 | Command inputs, outputs, and safety posture. |
| Compatibility report | demo/compatibility_report.md | 1284 | cc210d7c639f0880 | Package and artifact compatibility gates. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | dd9c3757259a51dc | Base and optional CSV dictionary comparison. |
| Example pack | demo/example_pack.md | 2132 | fdc5ab342f2245a1 | Stable public command recipes and expected artifacts. |
| Golden fixtures | demo/golden_fixtures.md | 1287 | 5e86fdeee147fa2f | Fixture hashes, schemas, and expected output counts. |
| Input schema | demo/input_schema.md | 1997 | a88689cafca69b55 | Static CSV schema and data dictionary. |
| Integration cookbook | demo/integration_cookbook.md | 2480 | fec4ebfd9689c624 | Public-safe local integration recipes. |
| Landing page | demo/landing_page.md | 3222 | b9002f9f5b39d840 | Public first-screen story and start-here commands. |
| Maintainer guide | demo/maintainer_guide.md | 2042 | e904cce568728ce3 | Release duties, order, and safety invariants. |
| README snippet | demo/readme_snippet.md | 2299 | c73c7ee8e2560178 | Compact copyable quickstart snippet. |
| Regression summary | demo/regression_summary.md | 1501 | 9b7d79db41f8e948 | Static regression gate summary. |
| Roadmap next | demo/roadmap_next.md | 1954 | 8c3739fe64ecc21c | Bounded public next steps and exclusions. |
| Scenario library | demo/scenario_library.md | 1936 | fcc943eeeb242bcd | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | 2bf46306d6b84ace | Operator diagnostics and recovery steps. |
| Workflow protocol | demo/workflow_protocol.md | 2397 | 65164a579b085da1 | Agent-ready local protocol and stop conditions. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 3856 | c9ef317e9fb11217 | Agent protocol and finance boundaries. |

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
