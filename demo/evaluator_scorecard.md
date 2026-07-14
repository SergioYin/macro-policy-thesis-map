# Evaluator Scorecard

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Status: needs-review

Score: 5 / 6

## Checks

| Check | Result | Evidence | Detail |
| --- | --- | --- | --- |
| trust_report_ready | pass | demo/trust_report.json | Trust report scores local evidence for a first-time GitHub visitor. |
| citation_map_complete | pass | demo/citation_map.json | Public claims cite local artifacts with paths and hashes. |
| artifact_index_complete | review | demo/artifact_index.json | Demo artifacts have producer commands, formats, and hashes. |
| public_readiness_ready | pass | demo/public_readiness.json | Readiness gates pass for local public release evidence. |
| tests_present | pass | tests/test_*.py | Local pytest suite is present for evaluator reruns. |
| boundaries_visible | pass | README.md, skills/agent/macro-policy-thesis-map/SKILL.md, demo/release_faq.json | Research-only boundaries are documented in human and agent surfaces. |

## Recommended Order

| Step | Command |
| --- | --- |
| 1 | trust-report |
| 2 | citation-map |
| 3 | release-faq |
| 4 | artifact-index |
| 5 | evaluator-scorecard |
