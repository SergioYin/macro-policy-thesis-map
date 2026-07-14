# Static Portfolio Exposure Map

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Fixture type: synthetic static exposure examples

Portfolio count: 2

Exposure count: 5

Matched exposure count: 5

## Portfolio Summary

| Portfolio | Sleeves | Exposures | Matched | Avg exposure | Policy areas |
| --- | --- | --- | --- | --- | --- |
| synthetic-core | 3 | 3 | 3 | 0.560 | fiscal-policy, labor-market, monetary-policy |
| synthetic-income | 2 | 2 | 2 | 0.505 | inflation, labor-market |

## Exposure Rows

| Portfolio | Sleeve | Exposure | Area | Thesis | Direction | Score | Sensitivity match | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| synthetic-core | duration-context | exp-003 | fiscal-policy | thesis-gamma | term-premium-linked | 0.490 | yes | Synthetic exposure score for duration supply context |
| synthetic-core | macro-cycle | exp-002 | labor-market | thesis-beta | demand-linked | 0.520 | yes | Synthetic exposure score for cyclical demand-channel monitoring |
| synthetic-core | rates-context | exp-001 | monetary-policy | thesis-alpha | rate-sensitive | 0.670 | yes | Synthetic exposure score for instruments described as rate-path sensitive |
| synthetic-income | inflation-context | exp-004 | inflation | thesis-delta | price-level-linked | 0.570 | yes | Synthetic exposure score for inflation breadth context |
| synthetic-income | macro-cycle | exp-005 | labor-market | thesis-beta | wage-cost-linked | 0.440 | yes | Synthetic exposure score for labor cost sensitivity context |
