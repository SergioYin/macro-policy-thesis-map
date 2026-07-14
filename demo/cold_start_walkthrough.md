# Cold Start Walkthrough

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Step count: 11

## Steps

| Step | Title | Command | Expected result |
| --- | --- | --- | --- |
| 1 | Inspect available commands | macro-policy-thesis-map command-matrix | Markdown and JSON command matrix are written under demo/. |
| 2 | Build the packet from static examples | macro-policy-thesis-map build-packet | A neutral thesis packet is written as Markdown and JSON. |
| 3 | Review evidence safety | macro-policy-thesis-map review-ledger | A review ledger flags low-confidence or advice-like input text. |
| 4 | Render static sensitivity and exposure layers | macro-policy-thesis-map thesis-impact-brief && macro-policy-thesis-map exposure-map && macro-policy-thesis-map scenario-library | Synthetic sensitivity, exposure, and scenario maps are written as Markdown and JSON. |
| 5 | Review schema adaptation surfaces | macro-policy-thesis-map assumption-registry && macro-policy-thesis-map data-dictionary-diff | Bounded assumptions and CSV dictionary differences are written as Markdown and JSON. |
| 6 | Read operator support surfaces | macro-policy-thesis-map troubleshoot && macro-policy-thesis-map docs-export && macro-policy-thesis-map cli-help | Operator troubleshooting, docs export, and CLI help surfaces are written as Markdown and JSON. |
| 7 | Read release-owner promotion notes | macro-policy-thesis-map adoption-notes && macro-policy-thesis-map reviewer-scorecard && macro-policy-thesis-map release-deck | Release-owner notes, scorecard, and deck are written as Markdown and JSON. |
| 8 | Generate public evaluator hardening surfaces | macro-policy-thesis-map benchmark-suite && macro-policy-thesis-map integration-cookbook && macro-policy-thesis-map compatibility-report && macro-policy-thesis-map maintainer-guide && macro-policy-thesis-map golden-fixtures && macro-policy-thesis-map regression-summary | Benchmark, integration, compatibility, maintainer, golden fixture, and regression artifacts are written as Markdown and JSON. |
| 9 | Export the public promotion bundle manifest | macro-policy-thesis-map bundle-export | A deterministic bundle manifest is written under demo/bundle_export/. |
| 10 | Check public readiness | macro-policy-thesis-map public-readiness | A public readiness report lists pass/fail gates. |
| 11 | Run final local checks | macro-policy-thesis-map selfcheck && macro-policy-thesis-map public-scan && macro-policy-thesis-map diff-check | All commands exit successfully before sharing artifacts. |

## Safety Notes

| Note |
| --- |
| Use static CSV files only. |
| Run local static commands only; no network access or broker connection is part of the walkthrough. |
| Do not add live market data, broker actions, trading recommendations, or personalized advice. |
| Treat review-ledger blockers as release blockers until the input text is revised. |
