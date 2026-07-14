# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Slide count: 5

## 1. Release Surface

- Version 1.2.0
- 47 zero-dependency CLI commands documented
- Static Markdown, JSON, HTML, and SVG artifacts only
## 2. Evidence And Hashes

- 101 release manifest artifacts tracked
- Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests
- Golden fixtures record static fixture hashes, schemas, and expected output keys
- diff-check verifies saved hashes against current local files
## 3. Reviewer Rubric

- Scorecard status: ready
- Score: 8 / 8
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
| demo/adoption_notes.json | 7151 | aff676f77aee44d0 |
| demo/api_reference.json | 41652 | 459ceec67aa61f46 |
| demo/artifact_index.json | 24304 | 1fe20b2960e171da |
| demo/benchmark_suite.json | 3043 | 6ee09b77f1d4f5aa |
| demo/citation_map.json | 4645 | cb3e09d776b4e334 |
| demo/command_matrix.json | 20252 | 0eedc17d3bea61f2 |
| demo/compatibility_report.json | 1952 | 6c3056202895e6f5 |
| demo/evaluator_scorecard.json | 1762 | a9406e7b779c266d |
| demo/example_pack.json | 3795 | 7cb7f9c3f2b0fc25 |
| demo/golden_fixtures.json | 4685 | f6c5648518f62a1b |
| demo/integration_cookbook.json | 3546 | 8a9ed4d4f1bc0b6f |
| demo/landing_page.json | 6046 | 1d5dd327d5deed49 |
| demo/maintainer_guide.json | 2430 | de0a35b7e0901089 |
| demo/public_readiness.json | 2116 | ea95c96e19cefec9 |
| demo/regression_summary.json | 2275 | 784262d381778f1f |
| demo/release_faq.json | 2295 | 5aafef8f95cd0962 |
| demo/release_manifest.json | 16603 | 50d89640ff5572c5 |
| demo/reviewer_scorecard.json | 7955 | 8c95b1f77db408b1 |
| demo/roadmap_next.json | 2452 | 3928f2c8b8502c9a |
| demo/trust_report.json | 3747 | 90e576c5b6525744 |
| demo/workflow_protocol.json | 3557 | d9e8eb649bda291f |
