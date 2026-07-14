# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.3.0

Slide count: 5

## 1. Release Surface

- Version 1.3.0
- 51 zero-dependency CLI commands documented
- Static Markdown, JSON, HTML, and SVG artifacts only
## 2. Evidence And Hashes

- 109 release manifest artifacts tracked
- Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests
- Golden fixtures record static fixture hashes, schemas, and expected output keys
- diff-check verifies saved hashes against current local files
## 3. Reviewer Rubric

- Scorecard status: needs-review
- Score: 8 / 9
- Maturity mapping covers static inputs, review controls, package evidence, verification, and readiness
- Public hardening covers benchmark, integration, compatibility, maintainer, fixture, and regression surfaces
- Protocol layer covers public landing, API contracts, agent protocol, example recipes, and roadmap constraints
- Governance layer covers boundary attestation, provenance, reproducibility, and release notes draft
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
| demo/adoption_notes.json | 8176 | 3d0e67cdfe090f33 |
| demo/api_reference.json | 45374 | 9babdb9e89dfc5ee |
| demo/artifact_index.json | 26413 | 934fe0fd1b8ce7a2 |
| demo/benchmark_suite.json | 3043 | 4a16814969e6dd12 |
| demo/boundary_attestation.json | 2101 | 521ff58189d124c5 |
| demo/citation_map.json | 5681 | 84ae750e57985800 |
| demo/command_matrix.json | 22248 | 7f61d38fdb211d10 |
| demo/compatibility_report.json | 2099 | fbf928894bc1ca24 |
| demo/evaluator_scorecard.json | 2214 | 79c7961fbc7b64f0 |
| demo/example_pack.json | 3795 | b2704c9a6deba147 |
| demo/golden_fixtures.json | 4685 | 6918a9dc69858c85 |
| demo/integration_cookbook.json | 3546 | 25d215e91152aa50 |
| demo/landing_page.json | 6046 | 23e0a951b8946771 |
| demo/maintainer_guide.json | 2540 | 6713131f87a78e8c |
| demo/provenance_ledger.json | 25808 | b41da876e3c9d36b |
| demo/public_readiness.json | 2301 | b2e51d04d172c6ca |
| demo/regression_summary.json | 2966 | 75a04ffefd4176b1 |
| demo/release_faq.json | 2778 | e1d0a5c2660c6411 |
| demo/release_manifest.json | 17914 | e209ffc1f60d18a8 |
| demo/release_notes_draft.json | 1922 | c1819fef3ab960e5 |
| demo/reproducibility_recipe.json | 10241 | c171be145870f412 |
| demo/reviewer_scorecard.json | 8950 | 7bf5681c80f5dfc4 |
| demo/roadmap_next.json | 2452 | 6a5aec3071917e7e |
| demo/trust_report.json | 5130 | edf2cf57246dad6e |
| demo/workflow_protocol.json | 3557 | 01116e3fb6b402c8 |
