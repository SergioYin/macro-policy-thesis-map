# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.1.0

Slide count: 5

## 1. Release Surface

- Version 1.1.0
- 42 zero-dependency CLI commands documented
- Static Markdown, JSON, HTML, and SVG artifacts only
## 2. Evidence And Hashes

- 91 release manifest artifacts tracked
- Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests
- Golden fixtures record static fixture hashes, schemas, and expected output keys
- diff-check verifies saved hashes against current local files
## 3. Reviewer Rubric

- Scorecard status: ready
- Score: 7 / 7
- Maturity mapping covers static inputs, review controls, package evidence, verification, and readiness
- Public hardening covers benchmark, integration, compatibility, maintainer, fixture, and regression surfaces
- Protocol layer covers public landing, API contracts, agent protocol, example recipes, and roadmap constraints
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
| demo/adoption_notes.json | 5938 | 4f24357bd142f6ab |
| demo/api_reference.json | 37394 | 7b89c11e4d5e9b45 |
| demo/benchmark_suite.json | 3043 | b491a34778eb237d |
| demo/command_matrix.json | 18004 | 482bdb26f8278978 |
| demo/compatibility_report.json | 1822 | d2653a328dc17a98 |
| demo/example_pack.json | 3795 | 2a5f299bb12a9fe6 |
| demo/golden_fixtures.json | 4685 | 6e7b7638818afdf7 |
| demo/integration_cookbook.json | 3546 | 71823c83d849c943 |
| demo/landing_page.json | 6046 | 9001d5d562723f1c |
| demo/maintainer_guide.json | 2322 | c54064f0c7b0ab21 |
| demo/public_readiness.json | 1923 | 15d96adf743682be |
| demo/regression_summary.json | 1984 | 5919c7ab743c5893 |
| demo/release_manifest.json | 15025 | f2564a94855db679 |
| demo/reviewer_scorecard.json | 6849 | 8a00abc46ce472d3 |
| demo/roadmap_next.json | 2452 | 5df60fe48a35e8be |
| demo/workflow_protocol.json | 3557 | 8a210ce7d2934354 |
