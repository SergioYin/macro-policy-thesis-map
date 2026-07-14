# Macro Policy Visual Receipt

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Format: svg

Artifacts: 14

Routes: 6

Commands: 9

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| README.md | 16096 | 14c1a4e5d37ae040 |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| examples/thesis_sensitivities.csv | 1016 | ab0a6a3d0a7f0bc9 |
| examples/portfolio_exposures.csv | 835 | f9ea6de8ccd82b4d |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/thesis_impact_brief.json | 4389 | 941fcf40523e63ae |
| demo/exposure_map.json | 3334 | e99f1a3387a9baa5 |
| demo/scenario_library.json | 2903 | 62d405892fb64c52 |
| demo/assumption_registry.json | 2500 | 7170c7639ab9e790 |
| demo/data_dictionary_diff.json | 3472 | 3d2592dd48b9de32 |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/public_readiness.json | 1923 | 15d96adf743682be |

## Routes

| Route |
| --- |
| /cases/asia-001 |
| /cases/asia-002 |
| /cases/eu-001 |
| /cases/eu-002 |
| /cases/us-001 |
| /cases/us-002 |

## Commands

| Command |
| --- |
| macro-policy-thesis-map case-gallery --root . |
| macro-policy-thesis-map thesis-impact-brief --root . |
| macro-policy-thesis-map exposure-map --root . |
| macro-policy-thesis-map scenario-library --root . |
| macro-policy-thesis-map assumption-registry --root . |
| macro-policy-thesis-map data-dictionary-diff --root . |
| macro-policy-thesis-map visual-receipt --root . --format svg |
| macro-policy-thesis-map public-readiness --root . |
| macro-policy-thesis-map diff-check --root . |
