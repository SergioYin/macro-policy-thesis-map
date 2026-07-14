# Roadmap Next

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Roadmap items: 4

## Items

| ID | Theme | Item | Acceptance | Excluded |
| --- | --- | --- | --- | --- |
| next-001 | Public docs | Keep the landing page aligned with README and command-matrix as commands evolve. | landing-page, api-reference, and command-matrix agree on command count and output paths. | marketing claims, private references |
| next-002 | Agent reuse | Stabilize protocol JSON field names before adding optional adapters. | workflow_protocol.json remains backwards-readable by agents using protocol_id macro-policy-thesis-map.v1.3. | remote orchestration, repository workflow files |
| next-003 | Data contracts | Add optional contract examples only when they remain synthetic, static, and additive. | api-reference and data-dictionary-diff list the new optional fields without changing base_event_csv. | live feeds, broker data, prediction fields |
| next-004 | Verification | Continue treating public-readiness, public-scan, selfcheck, diff-check, pytest, and wheel build as release gates. | regression-summary records gate names and no required gate depends on network access. | CI-only validation, timing benchmarks |

## Release Principles

| Principle |
| --- |
| Prefer deterministic local artifacts over hosted or live references. |
| Keep the base CSV contract stable and make optional layers additive. |
| Preserve zero runtime dependencies. |
| Keep finance boundaries explicit in every public surface. |

## Not Planned

| Surface |
| --- |
| Live macro or market data fetching. |
| Broker connections or order routing. |
| Personalized financial advice. |
| Repository workflow automation. |
| Private storage or private document references. |
