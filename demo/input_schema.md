# Input Schema

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Schema version: 0.7.0

Format: csv

Required columns: date, event_type, source, policy_area, channel, direction, confidence, evidence, thesis_link

## Data Dictionary

| Column | Type | Required | Format | Min | Max | Allowed values | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| date | date | yes | YYYY-MM-DD |  |  |  | Publication or observation date for the static source row. |
| event_type | string | yes |  |  |  | macro_observation, market_context, policy_signal, thesis_note | Classification of the supplied macro or policy evidence. |
| source | string | yes |  |  |  |  | Short static source label, such as a release, calendar, or research note identifier. |
| policy_area | string | yes |  |  |  |  | Policy or macro area being mapped, for example monetary-policy or labor-market. |
| channel | string | yes |  |  |  |  | Transmission channel or metric represented by the row. |
| direction | string | yes |  |  |  |  | Neutral analyst label for the supplied evidence direction. |
| confidence | number | yes |  | 0 | 1 |  | Static analyst confidence in the row's evidence mapping, bounded from 0 to 1. |
| evidence | string | yes |  |  |  |  | Concise neutral evidence summary. Advice-like terms are treated as doctor blockers. |
| thesis_link | string | yes |  |  |  |  | Stable local thesis identifier used to group evidence. |

## Quality Controls

| Control |
| --- |
| CSV header must contain every required column. |
| event_type must be one of the allowed values. |
| confidence must parse as a number from 0 to 1 inclusive. |
| date must parse as ISO YYYY-MM-DD and should not be stale relative to the configured as-of date. |
| evidence and thesis_link should not contain advice-like terms. |
