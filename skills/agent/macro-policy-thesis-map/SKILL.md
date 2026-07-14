# macro-policy-thesis-map

Use this skill when an agent needs to turn static macro policy notes into a neutral thesis evidence packet without live data, trading actions, or predictions.

## Protocol

1. Confirm the input is static CSV data with the columns documented in `README.md`.
2. Run `macro-policy-thesis-map fixture-doctor --root .` to validate required columns, event types, confidence bounds, stale source dates, and advice-like terms.
3. Run `macro-policy-thesis-map schema-export --root .` when a machine-readable input schema or data dictionary is needed.
4. Run `macro-policy-thesis-map troubleshoot --root .`, `macro-policy-thesis-map docs-export --root .`, `macro-policy-thesis-map readme-snippet --root .`, and `macro-policy-thesis-map cli-help --root .` when operator support surfaces are needed.
5. Run `macro-policy-thesis-map build-packet --root .` to create the primary evidence packet.
6. Run `macro-policy-thesis-map review-ledger --root .` to surface low-confidence or advice-like text for human review.
7. Run `macro-policy-thesis-map compare-history --root .` when a prior static event file is available.
8. Run `macro-policy-thesis-map thesis-impact-brief --root .` and `macro-policy-thesis-map exposure-map --root .` when static synthetic sensitivity and exposure summaries are needed.
9. Run `macro-policy-thesis-map scenario-library --root .`, `macro-policy-thesis-map assumption-registry --root .`, and `macro-policy-thesis-map data-dictionary-diff --root .` when public evaluators need static schema adaptation guidance.
10. Run `macro-policy-thesis-map case-gallery --root .` when public-safe US, EU, and Asia fixture examples are needed.
11. Run `macro-policy-thesis-map visual-receipt --root .` to create a static SVG receipt with hashes, routes, and commands. Use `--format html` when an HTML receipt is preferred.
12. Run `macro-policy-thesis-map quickstart-check --root .` and `macro-policy-thesis-map command-matrix --root .` to publish first-evaluator command evidence.
13. Run `macro-policy-thesis-map adoption-notes --root .`, `macro-policy-thesis-map reviewer-scorecard --root .`, `macro-policy-thesis-map release-deck --root .`, and `macro-policy-thesis-map bundle-export --root .` to build the release-owner public promotion pack.
14. Run `macro-policy-thesis-map evidence-bundle --root .`, `macro-policy-thesis-map cold-start-walkthrough --root .`, and `macro-policy-thesis-map public-readiness --root .` for release-readiness review.
15. Run `macro-policy-thesis-map benchmark-suite --root .`, `macro-policy-thesis-map integration-cookbook --root .`, `macro-policy-thesis-map compatibility-report --root .`, `macro-policy-thesis-map maintainer-guide --root .`, `macro-policy-thesis-map golden-fixtures --root .`, and `macro-policy-thesis-map regression-summary --root .` for the public evaluator hardening pack.
16. Run `macro-policy-thesis-map landing-page --root .`, `macro-policy-thesis-map api-reference --root .`, `macro-policy-thesis-map workflow-protocol --root .`, `macro-policy-thesis-map example-pack --root .`, and `macro-policy-thesis-map roadmap-next --root .` for the public landing and reusable protocol layer.
17. Run `macro-policy-thesis-map trust-report --root .`, `macro-policy-thesis-map citation-map --root .`, `macro-policy-thesis-map release-faq --root .`, `macro-policy-thesis-map artifact-index --root .`, and `macro-policy-thesis-map evaluator-scorecard --root .` for the public trust layer.
18. Run `macro-policy-thesis-map boundary-attestation --root .`, `macro-policy-thesis-map provenance-ledger --root .`, `macro-policy-thesis-map reproducibility-recipe --root .`, `macro-policy-thesis-map release-notes-draft --root .`, `macro-policy-thesis-map onboarding-checklist --root .`, `macro-policy-thesis-map maintainer-handoff --root .`, and `macro-policy-thesis-map release-audit-summary --root .` for the v1.5.0 governance, evaluator onboarding, maintainer handoff, and final audit layer.
19. Run `macro-policy-thesis-map public-scan --root .` and `macro-policy-thesis-map diff-check --root .` before sharing generated files outside the working environment.

## Boundaries

Keep outputs neutral and evidence-focused. Do not add buy, sell, hold, allocation, price target, return forecast, live market data, broker, order, or personalized advice language. Sensitivity, exposure, scenario, assumption, dictionary-diff, landing, API reference, workflow protocol, example pack, roadmap, trust report, citation map, release FAQ, artifact index, evaluator scorecard, boundary attestation, provenance ledger, reproducibility recipe, release notes draft, onboarding checklist, maintainer handoff, and release audit summary outputs must stay synthetic, descriptive, public-safe, and deterministic. If the input contains advice-like terms, preserve the review finding and ask for a safer static fixture.
