# Maintainer Guide

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.1.0

Section count: 4

## Duties

| Section | Duties |
| --- | --- |
| versioning | Keep pyproject.toml and package __version__ synchronized.; Regenerate demo artifacts after version changes.; Update release manifest after generated files settle. |
| fixtures | Use synthetic static CSV rows only.; Run fixture-doctor and golden-fixtures after fixture edits.; Keep bundled package examples in sync with top-level examples. |
| public safety | Run public-scan before sharing artifacts.; Keep README and skill boundaries explicit.; Do not add workflow files, private references, live finance feeds, or advice language. |
| regression gates | Run pytest, selfcheck, public-readiness, diff-check, and wheel build when feasible.; Regenerate regression-summary with the final local status.; Treat readiness blockers as release blockers. |

## Release Order

| Step | Command |
| --- | --- |
| 1 | fixture-doctor |
| 2 | schema-export |
| 3 | build-packet |
| 4 | review-ledger |
| 5 | scenario-library |
| 6 | assumption-registry |
| 7 | data-dictionary-diff |
| 8 | landing-page |
| 9 | api-reference |
| 10 | workflow-protocol |
| 11 | example-pack |
| 12 | roadmap-next |
| 13 | benchmark-suite |
| 14 | integration-cookbook |
| 15 | compatibility-report |
| 16 | maintainer-guide |
| 17 | golden-fixtures |
| 18 | regression-summary |
| 19 | maturity-report |
| 20 | evidence-bundle |
| 21 | public-readiness |
| 22 | release-manifest |
| 23 | diff-check |

## Invariants

| Invariant |
| --- |
| Runtime dependencies remain empty. |
| Generated public artifacts are deterministic Markdown, JSON, HTML, or SVG under demo/. |
| All example data remains static and synthetic. |
| No live finance data, advice, private references, or workflow automation is introduced. |
