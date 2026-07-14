# Boundary Attestation

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Status: attested

Passed: 6 / 6

## Checks

| Check | Result | Evidence | Attestation |
| --- | --- | --- | --- |
| static_research_boundaries | pass | README.md | README states the finance boundary before command usage. |
| agent_skill_boundaries | pass | skills/agent/macro-policy-thesis-map/SKILL.md | Agent protocol preserves static, research-only behavior. |
| zero_runtime_dependencies | pass | pyproject.toml | Runtime dependency list is empty. |
| public_scan_clean | pass | public-scan | No private term or credential-shaped finding was detected in public text. |
| no_workflow_files | pass | .github/workflows | Release verification is local and does not rely on repository workflow files. |
| synthetic_static_fixtures | pass | examples/macro_events.csv, examples/public_macro_cases.csv, examples/thesis_sensitivities.csv, examples/portfolio_exposures.csv | Default finance examples are committed static fixtures. |

## Public Scan Findings

| Finding |
| --- |
| none |

## Unsupported

| Surface |
| --- |
| live data fetching |
| broker connections |
| orders |
| recommendations |
| return predictions |
| personalized financial advice |
| workflow automation |
| private references |
