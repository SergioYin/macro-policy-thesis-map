# Release Owner Promotion Deck

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Slide count: 5

## 1. Release Surface

- Version 1.5.0
- 54 zero-dependency CLI commands documented
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
| demo/adoption_notes.json | 8260 | 914c6001a16039b9 |
| demo/api_reference.json | 48075 | 9abbaa7e95e8ef92 |
| demo/artifact_index.json | 27781 | 9b636f1a40213802 |
| demo/benchmark_suite.json | 3043 | fecc433c113c786f |
| demo/boundary_attestation.json | 2101 | 32d1ff7a15c7debe |
| demo/citation_map.json | 5936 | 25e37ca20e0c62c1 |
| demo/command_matrix.json | 23850 | 5e97ff48b0bb0929 |
| demo/compatibility_report.json | 2400 | 56be342014d705ad |
| demo/evaluator_scorecard.json | 2257 | e87c0940fbff005d |
| demo/example_pack.json | 3795 | 80c1af31fba09765 |
| demo/golden_fixtures.json | 4685 | acea7ebf0a09c9d1 |
| demo/integration_cookbook.json | 3546 | 4cc09db548a7c957 |
| demo/landing_page.json | 6046 | 99596e5e7fb494f2 |
| demo/maintainer_guide.json | 2623 | b448c5bdd76bec62 |
| demo/provenance_ledger.json | 27062 | ec5015ff728ecde2 |
| demo/public_readiness.json | 2610 | 8b91002e3689db66 |
| demo/regression_summary.json | 3662 | 7585f3c1dc78ba14 |
| demo/release_faq.json | 2887 | 0f235c2a8d40f672 |
| demo/release_manifest.json | 18568 | dc52cccb72090ed5 |
| demo/release_notes_draft.json | 2248 | e14d99fc40369c0f |
| demo/reproducibility_recipe.json | 10807 | 7fe88eeb7faedd9c |
| demo/reviewer_scorecard.json | 8942 | 249bccb3df196683 |
| demo/roadmap_next.json | 2452 | 629518ec9ea03f23 |
| demo/trust_report.json | 5130 | f6249b9e4c8d4171 |
| demo/workflow_protocol.json | 3557 | dfa240e52ed0ec75 |
