# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.0.0

Status: ready

Documents: 16

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 13515 | 4366c0540cdd883c | Primary operator and evaluator documentation. |
| Assumption registry | demo/assumption_registry.md | 1980 | 2b961c66ef2d33cc | Bounded public assumptions and validation controls. |
| Benchmark suite | demo/benchmark_suite.md | 1916 | 18115fdb4f1ca70f | Static synthetic evaluator benchmark matrix. |
| CLI help | demo/cli_help.md | 10373 | 6d51f91a2bb2b6e9 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 10287 | 94c79f2821d3b898 | Command inputs, outputs, and safety posture. |
| Compatibility report | demo/compatibility_report.md | 1207 | e140522e762b8cfc | Package and artifact compatibility gates. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | 6af63ab579f72a45 | Base and optional CSV dictionary comparison. |
| Golden fixtures | demo/golden_fixtures.md | 1287 | 0787d7af95d65426 | Fixture hashes, schemas, and expected output counts. |
| Input schema | demo/input_schema.md | 1997 | 754ab856318b5154 | Static CSV schema and data dictionary. |
| Integration cookbook | demo/integration_cookbook.md | 2480 | bb099ed382e45608 | Public-safe local integration recipes. |
| Maintainer guide | demo/maintainer_guide.md | 1926 | a5c3b705b6a3865c | Release duties, order, and safety invariants. |
| README snippet | demo/readme_snippet.md | 1787 | 46296fe71995bdb3 | Compact copyable quickstart snippet. |
| Regression summary | demo/regression_summary.md | 1501 | d049beb5ad27eab2 | Static regression gate summary. |
| Scenario library | demo/scenario_library.md | 1936 | 422c35b095ebd318 | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | 46dc6e206ba46b5b | Operator diagnostics and recovery steps. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 3447 | ad2a3aa446657766 | Agent protocol and finance boundaries. |

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
