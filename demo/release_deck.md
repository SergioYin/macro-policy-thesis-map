# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Slide count: 5

## 1. Release Surface

- Version 1.4.0
- 53 zero-dependency CLI commands documented
- Static Markdown, JSON, HTML, and SVG artifacts only
## 2. Evidence And Hashes

- 113 release manifest artifacts tracked
- Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests
- Golden fixtures record static fixture hashes, schemas, and expected output keys
- diff-check verifies saved hashes against current local files
## 3. Reviewer Rubric

- Scorecard status: ready
- Score: 9 / 9
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
| demo/adoption_notes.json | 8176 | ffd44ddaf8d88dbc |
| demo/api_reference.json | 47299 | b82a42e9cbf67437 |
| demo/artifact_index.json | 27463 | 6e767512e0bcd303 |
| demo/benchmark_suite.json | 3043 | 287d3fd6ac67014f |
| demo/boundary_attestation.json | 2101 | 3aaf0a1cff28aa03 |
| demo/citation_map.json | 5723 | 1efa53e66056991d |
| demo/command_matrix.json | 23315 | 6655681f7e419648 |
| demo/compatibility_report.json | 2257 | 0a222de323e14ab6 |
| demo/evaluator_scorecard.json | 2250 | 4e534075cd200132 |
| demo/example_pack.json | 3795 | 935a6dab9ce220cf |
| demo/golden_fixtures.json | 4685 | 99a3213b8530a9a4 |
| demo/integration_cookbook.json | 3546 | a4c794f009d7bede |
| demo/landing_page.json | 6046 | 9ff1501b33a0058f |
| demo/maintainer_guide.json | 2594 | 23c3bcd8b3958d2a |
| demo/provenance_ledger.json | 26766 | 16af0d34681e26e4 |
| demo/public_readiness.json | 2471 | d45135eba9e8effb |
| demo/regression_summary.json | 3389 | 55721620ea052ddc |
| demo/release_faq.json | 2820 | b62bd3e5721b08ca |
| demo/release_manifest.json | 18568 | 365a3a8944e17c4a |
| demo/release_notes_draft.json | 2124 | f62415c15621be64 |
| demo/reproducibility_recipe.json | 10617 | 5031cf7d6615be3b |
| demo/reviewer_scorecard.json | 8942 | 60034f732a1c4238 |
| demo/roadmap_next.json | 2452 | 394394f2afe8618f |
| demo/trust_report.json | 5130 | 212ac784fdce5843 |
| demo/workflow_protocol.json | 3557 | 26555f1efd6289b6 |
