# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.6.0

Slide count: 5

## 1. Release Surface

- Version 0.6.0
- 28 zero-dependency CLI commands documented
- Static Markdown, JSON, HTML, and SVG artifacts only
## 2. Evidence And Hashes

- 58 release manifest artifacts tracked
- Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests
- diff-check verifies saved hashes against current local files
## 3. Reviewer Rubric

- Scorecard status: ready
- Score: 5 / 5
- Maturity mapping covers static inputs, review controls, package evidence, verification, and readiness
## 4. Cold User Path

- Run the quickstart commands from a clean checkout.
- Review demo/reviewer_scorecard.md for any maturity item marked review.
- Confirm demo/public_readiness.json remains ready after local edits.
- Run public-scan and diff-check before sharing the bundle.
## 5. Safety Boundaries

- No workflow files are required for public evaluation
- No private references or credential-shaped terms are allowed by public-scan
- No live data, broker connections, orders, recommendations, predictions, or personalized advice
- Public readiness status: ready

## Artifact Hashes

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/adoption_notes.json | 3683 | 7aa9621cd8f222ac |
| demo/command_matrix.json | 11650 | 1eb66dbe9204a2fa |
| demo/public_readiness.json | 1355 | 26e502baf3e00996 |
| demo/release_manifest.json | 9745 | 5e498ecb61fc230f |
| demo/reviewer_scorecard.json | 3849 | 43ddcac602b834e0 |
