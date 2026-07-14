# Static Scenario Library

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.7.0

Fixture type: synthetic public evaluator scenarios

Scenario count: 4

## Scenarios

| Scenario | Name | Region | Area | Horizon | Axis | Direction | Schema fields | Adaptation note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scenario-001 | Policy Path Repricing | US | monetary-policy | near-term | rate-path | more-restrictive | date, policy_area, channel, direction, confidence, thesis_link | Use direction and confidence to describe a static policy-path interpretation without adding forecast probabilities. |
| scenario-002 | Fiscal Implementation Lag | EU | fiscal-policy | medium-term | implementation-timing | delayed-transmission | date, source, policy_area, channel, evidence | Keep source labels and evidence summaries separate so public reviewers can trace static assumptions. |
| scenario-003 | Labor Supply Normalization | US | labor-market | medium-term | participation | normalizing | event_type, policy_area, channel, direction, confidence | Represent labor channels as descriptive categories, not market return forecasts. |
| scenario-004 | External Demand Rotation | Asia | trade-policy | cross-cycle | demand-mix | rotating | region, policy_area, channel, route, command | Optional region and route fields can support public galleries while preserving base event compatibility. |

## Schema Adaptation Rules

| Rule |
| --- |
| Treat every scenario as a deterministic example, not a forecast. |
| Keep optional fields additive so the base event CSV remains valid. |
| Use confidence as a bounded evidence-mapping score from 0 to 1. |
| Do not add allocation, trade, price-target, or return-prediction columns. |
