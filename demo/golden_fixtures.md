# Golden Fixtures

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Status: ready

Fixture count: 5

## Fixtures

| Fixture | Path | Rows | Schema | Bytes | SHA-256 prefix |
| --- | --- | --- | --- | --- | --- |
| event_current | examples/macro_events.csv | 5 | pass | 906 | b7410919d62dd4e3 |
| event_prior | examples/prior_macro_events.csv | 4 | pass | 715 | 95f9b30ce6f88581 |
| case_gallery | examples/public_macro_cases.csv | 6 | pass | 1471 | ee511dd457dd7aab |
| thesis_sensitivity | examples/thesis_sensitivities.csv | 6 | pass | 1016 | ab0a6a3d0a7f0bc9 |
| portfolio_exposure | examples/portfolio_exposures.csv | 5 | pass | 835 | f9ea6de8ccd82b4d |

## Expected Outputs

| Command | JSON path | Key | Observed value | Status |
| --- | --- | --- | --- | --- |
| build-packet | demo/thesis_packet.json | event_count | 5 | recorded |
| case-gallery | demo/case_gallery.json | case_count | 6 | recorded |
| thesis-impact-brief | demo/thesis_impact_brief.json | sensitivity_count | 6 | recorded |
| exposure-map | demo/exposure_map.json | exposure_count | 5 | recorded |
