# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.7.0

Status: ready

Documents: 10

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 11457 | c3f6dcc9a6f908ce | Primary operator and evaluator documentation. |
| Assumption registry | demo/assumption_registry.md | 1980 | 04fe2e3e4e6d56c7 | Bounded public assumptions and validation controls. |
| CLI help | demo/cli_help.md | 8653 | ee93ddaf0b9436ec | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 8556 | c85741c8d658518f | Command inputs, outputs, and safety posture. |
| Data dictionary diff | demo/data_dictionary_diff.md | 2177 | 86f1198eb0785c72 | Base and optional CSV dictionary comparison. |
| Input schema | demo/input_schema.md | 1997 | 3a6c9b953a7de268 | Static CSV schema and data dictionary. |
| README snippet | demo/readme_snippet.md | 1123 | 7e2cd08dda5284ff | Compact copyable quickstart snippet. |
| Scenario library | demo/scenario_library.md | 1936 | 02371cfe666cccda | Synthetic scenarios for public schema adaptation review. |
| Troubleshooting | demo/troubleshoot.md | 2357 | 1de5bb412b1b2059 | Operator diagnostics and recovery steps. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 3062 | 3e2ac9bf3e85192a | Agent protocol and finance boundaries. |

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
