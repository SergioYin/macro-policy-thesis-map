# Assumption Registry

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.1.0

Assumption count: 4

## Assumptions

| Assumption | Category | Statement | Owner | Validation | Schema impact | Status |
| --- | --- | --- | --- | --- | --- | --- |
| assumption-001 | data | Input rows are static CSV records supplied by the evaluator. | public evaluator | fixture-doctor checks required columns, confidence bounds, dates, and advice-like terms. | Base event columns remain required for build-packet. | active |
| assumption-002 | safety | Outputs must stay descriptive and research-only. | release owner | public-scan, review-ledger, public-readiness, and selfcheck fail closed on unsafe text or missing boundaries. | Do not add recommendation, allocation, target, order, or prediction fields. | active |
| assumption-003 | packaging | The package has zero runtime dependencies and bundled example CSVs for installed default commands. | maintainer | pytest and build backend tests verify version, wheel package data, and reproducible archives. | New default commands should use built-in metadata or bundled fixtures. | active |
| assumption-004 | adaptation | Schema extensions are optional public-evaluator layers rather than replacements for the base event schema. | public evaluator | data-dictionary-diff lists additive, shared, and omitted fields deterministically. | Adapters should preserve date, event_type, policy_area, confidence, evidence, and thesis_link where possible. | active |

## Review Controls

| Control |
| --- |
| Regenerate assumption-registry after changing schema or release boundaries. |
| Treat assumptions marked active as evaluator-facing constraints. |
| Escalate any need for live data, broker access, or investment advice outside this package. |
