# Macro Policy Visual Receipt

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Format: svg

Artifacts: 7

Routes: 6

Commands: 4

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| README.md | 6426 | a2b7c4b9bdbce51e |
| examples/macro_events.csv | 906 | b7410919d62dd4e3 |
| examples/public_macro_cases.csv | 1471 | ee511dd457dd7aab |
| demo/thesis_packet.json | 3659 | 21afd1a6478ca243 |
| demo/case_gallery.json | 4180 | 526e837ce331afd0 |
| demo/review_ledger.json | 432 | d4f558b50d9e8366 |
| demo/public_readiness.json | 1176 | 6c77e1bbdc99d8e9 |

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
| macro-policy-thesis-map visual-receipt --root . --format svg |
| macro-policy-thesis-map public-readiness --root . |
| macro-policy-thesis-map diff-check --root . |
