# Compatibility Report

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Status: ready

Passed: 11 / 11

## Checks

| Check | Result | Detail |
| --- | --- | --- |
| python_requires | pass | Package declares Python 3.11 or newer. |
| zero_runtime_dependencies | pass | Package declares zero runtime dependencies. |
| console_script | pass | Console script is declared. |
| version_sync | pass | pyproject version matches package version. |
| bundled_event_fixture | pass | Bundled default event fixture is present. |
| bundled_case_fixture | pass | Bundled public case fixture is present. |
| public_artifacts | pass | Public evaluator artifacts are present. |
| protocol_artifacts | pass | Public protocol layer artifacts are present. |
| trust_artifacts | pass | Public trust layer artifacts are present. |
| governance_artifacts | pass | Governance and attestation layer artifacts are present. |
| no_workflows | pass | No workflow files are required. |

## Supported Surfaces

| Surface |
| --- |
| source checkout |
| installed console script |
| offline wheel |
| offline sdist |

## Unsupported Surfaces

| Surface |
| --- |
| live data connector |
| broker integration |
| workflow automation |
| personalized finance advice |
