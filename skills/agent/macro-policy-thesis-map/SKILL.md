# macro-policy-thesis-map

Use this skill when an agent needs to turn static macro policy notes into a neutral thesis evidence packet without live data, trading actions, or predictions.

## Protocol

1. Confirm the input is static CSV data with the columns documented in `README.md`.
2. Run `macro-policy-thesis-map fixture-doctor --root .` to validate required columns, event types, confidence bounds, stale source dates, and advice-like terms.
3. Run `macro-policy-thesis-map schema-export --root .` when a machine-readable input schema or data dictionary is needed.
4. Run `macro-policy-thesis-map build-packet --root .` to create the primary evidence packet.
5. Run `macro-policy-thesis-map review-ledger --root .` to surface low-confidence or advice-like text for human review.
6. Run `macro-policy-thesis-map compare-history --root .` when a prior static event file is available.
7. Run `macro-policy-thesis-map quickstart-check --root .` and `macro-policy-thesis-map command-matrix --root .` to publish first-evaluator command evidence.
8. Run `macro-policy-thesis-map evidence-bundle --root .`, `macro-policy-thesis-map cold-start-walkthrough --root .`, and `macro-policy-thesis-map public-readiness --root .` for release-readiness review.
9. Run `macro-policy-thesis-map public-scan --root .` before sharing generated files outside the working environment.

## Boundaries

Keep outputs neutral and evidence-focused. Do not add buy, sell, hold, allocation, price target, return forecast, live market data, broker, order, or personalized advice language. If the input contains those terms, preserve the review finding and ask for a safer static fixture.
