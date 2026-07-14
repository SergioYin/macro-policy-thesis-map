# Cold Start Walkthrough

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Step count: 5

## Steps

| Step | Title | Command | Expected result |
| --- | --- | --- | --- |
| 1 | Inspect available commands | macro-policy-thesis-map command-matrix | Markdown and JSON command matrix are written under demo/. |
| 2 | Build the packet from static examples | macro-policy-thesis-map build-packet | A neutral thesis packet is written as Markdown and JSON. |
| 3 | Review evidence safety | macro-policy-thesis-map review-ledger | A review ledger flags low-confidence or advice-like input text. |
| 4 | Check public readiness | macro-policy-thesis-map public-readiness | A public readiness report lists pass/fail gates. |
| 5 | Run final local checks | macro-policy-thesis-map selfcheck && macro-policy-thesis-map public-scan && macro-policy-thesis-map diff-check | All commands exit successfully before sharing artifacts. |

## Safety Notes

| Note |
| --- |
| Use static CSV files only. |
| Run local static commands only; no network access or broker connection is part of the walkthrough. |
| Do not add live market data, broker actions, trading recommendations, or personalized advice. |
| Treat review-ledger blockers as release blockers until the input text is revised. |
