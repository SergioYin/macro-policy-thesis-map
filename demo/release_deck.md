# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.0.0

Slide count: 5

## 1. Release Surface

- Version 1.0.0
- 37 zero-dependency CLI commands documented
- Static Markdown, JSON, HTML, and SVG artifacts only
## 2. Evidence And Hashes

- 76 release manifest artifacts tracked
- Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests
- Golden fixtures record static fixture hashes, schemas, and expected output keys
- diff-check verifies saved hashes against current local files
## 3. Reviewer Rubric

- Scorecard status: ready
- Score: 6 / 6
- Maturity mapping covers static inputs, review controls, package evidence, verification, and readiness
- Public hardening covers benchmark, integration, compatibility, maintainer, fixture, and regression surfaces
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
| demo/adoption_notes.json | 5938 | 67a2f9c23b0a880e |
| demo/benchmark_suite.json | 3043 | 3f8b9be2e11158d9 |
| demo/command_matrix.json | 15540 | 5467cce33f686c5a |
| demo/compatibility_report.json | 1688 | 737f1a2d1377e5e4 |
| demo/golden_fixtures.json | 4685 | 43567374f2468e4a |
| demo/integration_cookbook.json | 3546 | 4412ef0248807d31 |
| demo/maintainer_guide.json | 2216 | 66aeb9ddf7d23998 |
| demo/public_readiness.json | 1732 | 4dd6c11f67f4d2c1 |
| demo/regression_summary.json | 1984 | d76fb5661bd590f4 |
| demo/release_manifest.json | 12659 | 8ff93441a6d2c1a4 |
| demo/reviewer_scorecard.json | 5738 | 188e8c32928cf4b8 |
