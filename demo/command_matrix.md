# Command Matrix

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Command count: 18

| Command | Purpose | Inputs | Outputs | Safety |
| --- | --- | --- | --- | --- |
| build-packet | Build the primary thesis evidence packet from static CSV events. | examples/macro_events.csv or bundled macro_events.csv | demo/thesis_packet.md, demo/thesis_packet.json | Static research output with no live data, orders, or recommendations. |
| compare-history | Compare current and prior static policy event sets. | examples/macro_events.csv, examples/prior_macro_events.csv or bundled examples | demo/history_comparison.md, demo/history_comparison.json | Reports structural deltas only; does not forecast policy or market outcomes. |
| review-ledger | Flag low-confidence areas and advice-like terms in supplied evidence. | examples/macro_events.csv or bundled macro_events.csv | demo/review_ledger.md, demo/review_ledger.json | Raises review findings instead of rewriting evidence into advice. |
| static-dashboard | Render a no-JavaScript HTML view of the packet and review ledger. | examples/macro_events.csv or bundled macro_events.csv | demo/static_dashboard.html | Static local rendering only. |
| case-gallery | Build a public-safe multi-region case gallery from static synthetic fixtures. | examples/public_macro_cases.csv or bundled public_macro_cases.csv | demo/case_gallery.md, demo/case_gallery.json | Uses synthetic US, EU, and Asia examples; no live data or recommendations. |
| visual-receipt | Render a static SVG or HTML receipt with artifact hashes, routes, and commands. | repository files, demo artifacts, case gallery | demo/visual_receipt.svg or demo/visual_receipt.html, demo/visual_receipt.json | Static receipt only; records provenance without private routes or operational workflows. |
| fixture-doctor | Validate static CSV fixtures for columns, event types, confidence bounds, stale dates, and advice-like terms. | examples/macro_events.csv or bundled macro_events.csv | demo/fixture_doctor.md, demo/fixture_doctor.json | Reports data-quality blockers before evidence is rendered. |
| schema-export | Export the machine-readable input schema and data dictionary. | built-in schema metadata | demo/input_schema.md, demo/input_schema.json | Documents accepted static inputs without connecting to external systems. |
| release-manifest | Record deterministic paths, sizes, and hashes for release artifacts. | repository files | demo/release_manifest.md, demo/release_manifest.json | Excludes generated manifest self-hashes. |
| maturity-report | Score basic release-readiness evidence in the source tree. | repository files | demo/maturity_report.md, demo/maturity_report.json | Checks packaging, examples, tests, skill docs, and absence of workflow files. |
| quickstart-check | Show whether a fresh evaluator can run the documented starter commands. | repository files and bundled examples | demo/quickstart_check.md, demo/quickstart_check.json | Checks command availability and expected artifacts without network access. |
| command-matrix | Publish a neutral map of CLI commands, inputs, outputs, and safety posture. | built-in command metadata | demo/command_matrix.md, demo/command_matrix.json | Documents capabilities without private references or operational workflows. |
| evidence-bundle | Collect public evaluation artifacts and source fixture hashes in one bundle. | examples, demo artifacts, README, tests, skill docs | demo/evidence_bundle.md, demo/evidence_bundle.json | Includes hashes and static summaries only. |
| public-readiness | Summarize public release readiness gates and blockers. | repository files, demo artifacts, public scan | demo/public_readiness.md, demo/public_readiness.json | Requires public scan pass and explicit static research boundaries. |
| cold-start-walkthrough | Generate a deterministic first-run walkthrough for public evaluators. | built-in command metadata | demo/cold_start_walkthrough.md, demo/cold_start_walkthrough.json | Uses local static commands and bundled examples. |
| public-scan | Scan publishable text for private names, paths, and credential-shaped terms. | repository text files | stdout pass/fail | Fails closed when a private or credential-shaped token is found. |
| diff-check | Compare the saved release manifest against current file hashes. | demo/release_manifest.json, repository files | stdout pass/fail | Detects artifact drift using static local hashes only. |
| selfcheck | Run source-tree checks for files, boundaries, and public scan status. | repository files | stdout pass/fail | Fails closed when required public release evidence is missing. |
