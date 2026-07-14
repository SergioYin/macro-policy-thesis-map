# Data Dictionary Diff

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Base dictionary: base_event

Dictionary count: 4

## Dictionary Comparison

| Dictionary | Columns | Shared with base | Additive columns | Base columns not present | Adaptation posture |
| --- | --- | --- | --- | --- | --- |
| base_event | 9 | date, event_type, source, policy_area, channel, direction, confidence, evidence, thesis_link | none | none | base |
| case_gallery | 11 | date, policy_area, channel, direction, confidence, evidence | case_id, region, case_title, route, command | event_type, source, thesis_link | optional additive layer |
| thesis_sensitivity | 8 | policy_area, confidence | thesis_id, sensitivity_axis, shock_label, impact_direction, impact_score, rationale | date, event_type, source, channel, direction, evidence, thesis_link | optional additive layer |
| portfolio_exposure | 8 | policy_area | portfolio_id, sleeve, exposure_id, thesis_id, exposure_direction, exposure_score, rationale | date, event_type, source, channel, direction, confidence, evidence, thesis_link | optional additive layer |

## Recommendations

| Decision | Rationale |
| --- | --- |
| Keep base event columns for packet generation. | build-packet, compare-history, review-ledger, fixture-doctor, and static-dashboard rely on the base event schema. |
| Add region, route, and command only for public case gallery workflows. | Those fields support deterministic public routes and receipts but are not needed for core event evidence. |
| Use sensitivity and exposure fields as separate optional tables. | Separate CSVs keep scenario scores synthetic and avoid mixing descriptive mappings with event evidence. |

## Finance Safety Constraints

| Constraint |
| --- |
| No allocation target, order, recommendation, price target, or return prediction fields. |
| Scores must remain bounded descriptive values from 0 to 1. |
| Scenario and assumption fields must remain synthetic and static. |
