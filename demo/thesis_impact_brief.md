# Static Thesis Impact Brief

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Fixture type: synthetic static thesis sensitivity examples

Sensitivity count: 6

Thesis count: 4

Policy area count: 4

Fixture hash: ab0a6a3d0a7f0bc9

## Thesis Summary

| Thesis | Policy areas | Axes | Avg impact | Avg confidence | Directions |
| --- | --- | --- | --- | --- | --- |
| thesis-alpha | monetary-policy | 1 | 0.650 | 0.720 | pressure, relief |
| thesis-beta | labor-market | 2 | 0.590 | 0.685 | moderation, pressure |
| thesis-delta | inflation | 1 | 0.690 | 0.740 | pressure |
| thesis-gamma | fiscal-policy | 1 | 0.610 | 0.640 | pressure |

## Policy Area Summary

| Area | Theses | Axes | Avg impact |
| --- | --- | --- | --- |
| fiscal-policy | 1 | 1 | 0.610 |
| inflation | 1 | 1 | 0.690 |
| labor-market | 1 | 2 | 0.590 |
| monetary-policy | 1 | 1 | 0.650 |

## Sensitivity Rows

| Thesis | Area | Axis | Shock | Direction | Impact | Confidence | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |
| thesis-alpha | monetary-policy | rate-path | faster-easing | relief | 0.580 | 0.680 | Synthetic row maps easier rate path language to reduced discount-rate pressure |
| thesis-alpha | monetary-policy | rate-path | higher-for-longer | pressure | 0.720 | 0.760 | Synthetic row maps tighter rate path language to valuation pressure in rate-sensitive thesis notes |
| thesis-beta | labor-market | employment-momentum | cooling-labor | moderation | 0.630 | 0.710 | Synthetic row links slower labor momentum to softer demand-channel framing |
| thesis-beta | labor-market | wage-pressure | firm-wage-costs | pressure | 0.550 | 0.660 | Synthetic row maps wage pressure to margin-channel monitoring |
| thesis-delta | inflation | inflation-breadth | sticky-services | pressure | 0.690 | 0.740 | Synthetic row maps services breadth to inflation persistence monitoring |
| thesis-gamma | fiscal-policy | issuance-mix | long-duration-supply | pressure | 0.610 | 0.640 | Synthetic row links duration supply context to term-premium monitoring |
