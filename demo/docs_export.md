# Operator Documentation Export

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.6.0

Status: ready

Documents: 7

Missing: 0

## Documents

| Title | Path | Bytes | SHA-256 prefix | Purpose |
| --- | --- | --- | --- | --- |
| README | README.md | 10220 | eaa234fbd5b55e4b | Primary operator and evaluator documentation. |
| CLI help | demo/cli_help.md | 7728 | 8a67e4481f613301 | Deterministic command usage lines. |
| Command matrix | demo/command_matrix.md | 7693 | 3a370f34dc533f51 | Command inputs, outputs, and safety posture. |
| Input schema | demo/input_schema.md | 1997 | 3cf4632070a11834 | Static CSV schema and data dictionary. |
| README snippet | demo/readme_snippet.md | 785 | d47dd5186caf62b6 | Compact copyable quickstart snippet. |
| Troubleshooting | demo/troubleshoot.md | 2053 | ab8727285b47c4ac | Operator diagnostics and recovery steps. |
| Agent skill | skills/agent/macro-policy-thesis-map/SKILL.md | 2782 | b60e5d1ad66a7639 | Agent protocol and finance boundaries. |

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
