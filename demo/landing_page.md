# Macro Policy Thesis Map

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Tagline: Static macro policy notes in; neutral thesis evidence packets out.

## First Screen

Headline: A zero-dependency CLI for reusable macro-policy evidence maps.

Subhead: Use static CSV fixtures or user-supplied static files to generate reviewable Markdown, JSON, and HTML artifacts without live data or advice.

Primary recipe: `PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root .`

Secondary recipe: `PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root .`

## Highlights

| Name | Detail |
| --- | --- |
| First-screen story | Turn static macro policy notes into a neutral evidence map that reviewers can inspect without live services. |
| Reusable protocol layer | Agents get stable command recipes, JSON contracts, and safety gates for repeatable local runs. |
| Public artifact pack | Markdown, JSON, HTML, and SVG demo outputs sit under demo/ with deterministic hashes. |

## Start Here

| Step | Command | Result |
| --- | --- | --- |
| 1 | macro-policy-thesis-map landing-page --root . | Public landing page artifacts are written under demo/. |
| 2 | macro-policy-thesis-map example-pack --root . | Stable command recipes and expected outputs are recorded. |
| 3 | macro-policy-thesis-map workflow-protocol --root . | Agent-ready protocol steps and gates are documented. |
| 4 | macro-policy-thesis-map public-readiness --root . | Public release gates are checked from local files. |

## Featured Commands

| Command | Purpose | Outputs |
| --- | --- | --- |
| build-packet | Build the primary thesis evidence packet from static CSV events. | demo/thesis_packet.md, demo/thesis_packet.json |
| public-readiness | Summarize public release readiness gates and blockers. | demo/public_readiness.md, demo/public_readiness.json |
| landing-page | Write a crisp public landing page for GitHub visitors and first-run evaluators. | demo/landing_page.md, demo/landing_page.json, demo/landing_page.html |
| api-reference | Write reusable command, artifact, and data-contract reference docs for agent and CLI reuse. | demo/api_reference.md, demo/api_reference.json, demo/api_reference.html |
| workflow-protocol | Write a reusable protocol layer for agents that need deterministic macro-policy evidence maps. | demo/workflow_protocol.md, demo/workflow_protocol.json, demo/workflow_protocol.html |
| example-pack | Write a public example pack with stable command recipes and expected static artifacts. | demo/example_pack.md, demo/example_pack.json, demo/example_pack.html |

## Artifact Links

| Path | Bytes | SHA-256 prefix |
| --- | --- | --- |
| demo/api_reference.json | 45374 | 9babdb9e89dfc5ee |
| demo/example_pack.json | 3795 | b2704c9a6deba147 |
| demo/landing_page.html | 3860 | 07cb9a57d8c08c24 |
| demo/public_readiness.json | 2301 | b2e51d04d172c6ca |
| demo/release_manifest.json | 17914 | e974d283d5fe2244 |
| demo/workflow_protocol.json | 3557 | 01116e3fb6b402c8 |
