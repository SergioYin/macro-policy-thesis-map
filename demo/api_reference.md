# API Reference

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

CLI: `macro-policy-thesis-map`

Python module: `macro_policy_thesis_map.cli`

## Commands

| Command | Usage | Purpose | Outputs |
| --- | --- | --- | --- |
| build-packet | macro-policy-thesis-map build-packet --root . | Build the primary thesis evidence packet from static CSV events. | demo/thesis_packet.md, demo/thesis_packet.json |
| compare-history | macro-policy-thesis-map compare-history --root . | Compare current and prior static policy event sets. | demo/history_comparison.md, demo/history_comparison.json |
| review-ledger | macro-policy-thesis-map review-ledger --root . | Flag low-confidence areas and advice-like terms in supplied evidence. | demo/review_ledger.md, demo/review_ledger.json |
| static-dashboard | macro-policy-thesis-map static-dashboard --root . | Render a no-JavaScript HTML view of the packet, review ledger, and static sensitivity summaries. | demo/static_dashboard.html |
| thesis-impact-brief | macro-policy-thesis-map thesis-impact-brief --root . | Summarize synthetic thesis sensitivity rows by thesis, policy area, and scenario axis. | demo/thesis_impact_brief.md, demo/thesis_impact_brief.json |
| exposure-map | macro-policy-thesis-map exposure-map --root . | Map synthetic portfolio exposure rows to static thesis sensitivity axes. | demo/exposure_map.md, demo/exposure_map.json |
| scenario-library | macro-policy-thesis-map scenario-library --root . | Publish synthetic macro policy scenarios for schema adaptation review. | demo/scenario_library.md, demo/scenario_library.json |
| assumption-registry | macro-policy-thesis-map assumption-registry --root . | Publish bounded assumptions, owners, and validation controls for public evaluators. | demo/assumption_registry.md, demo/assumption_registry.json |
| data-dictionary-diff | macro-policy-thesis-map data-dictionary-diff --root . | Compare base event CSV fields with optional public fixtures to guide schema adaptation. | demo/data_dictionary_diff.md, demo/data_dictionary_diff.json |
| case-gallery | macro-policy-thesis-map case-gallery --root . | Build a public-safe multi-region case gallery from static synthetic fixtures. | demo/case_gallery.md, demo/case_gallery.json |
| visual-receipt | macro-policy-thesis-map visual-receipt --root . | Render a static SVG or HTML receipt with artifact hashes, routes, and commands. | demo/visual_receipt.svg or demo/visual_receipt.html, demo/visual_receipt.json |
| fixture-doctor | macro-policy-thesis-map fixture-doctor --root . | Validate static CSV fixtures for columns, event types, confidence bounds, stale dates, and advice-like terms. | demo/fixture_doctor.md, demo/fixture_doctor.json |
| schema-export | macro-policy-thesis-map schema-export --root . | Export the machine-readable input schema and data dictionary. | demo/input_schema.md, demo/input_schema.json |
| troubleshoot | macro-policy-thesis-map troubleshoot --root . | Publish deterministic operator troubleshooting checks and recovery steps. | demo/troubleshoot.md, demo/troubleshoot.json |
| docs-export | macro-policy-thesis-map docs-export --root . | Export an operator documentation index with key docs, artifacts, and validation commands. | demo/docs_export.md, demo/docs_export.json |
| readme-snippet | macro-policy-thesis-map readme-snippet --root . | Write a compact README-ready usage snippet for public evaluators. | demo/readme_snippet.md, demo/readme_snippet.json |
| cli-help | macro-policy-thesis-map cli-help --root . | Write deterministic CLI help text and command usage lines. | demo/cli_help.md, demo/cli_help.json |
| release-manifest | macro-policy-thesis-map release-manifest --root . | Record deterministic paths, sizes, and hashes for release artifacts. | demo/release_manifest.md, demo/release_manifest.json |
| maturity-report | macro-policy-thesis-map maturity-report --root . | Score basic release-readiness evidence in the source tree. | demo/maturity_report.md, demo/maturity_report.json |
| quickstart-check | macro-policy-thesis-map quickstart-check --root . | Show whether a fresh evaluator can run the documented starter commands. | demo/quickstart_check.md, demo/quickstart_check.json |
| command-matrix | macro-policy-thesis-map command-matrix --root . | Publish a neutral map of CLI commands, inputs, outputs, and safety posture. | demo/command_matrix.md, demo/command_matrix.json |
| adoption-notes | macro-policy-thesis-map adoption-notes --root . | Write release-owner notes for public evaluator adoption and next actions. | demo/adoption_notes.md, demo/adoption_notes.json |
| reviewer-scorecard | macro-policy-thesis-map reviewer-scorecard --root . | Map release evidence to a reviewer maturity rubric with artifact hashes. | demo/reviewer_scorecard.md, demo/reviewer_scorecard.json |
| release-deck | macro-policy-thesis-map release-deck --root . | Build a deterministic Markdown/JSON promotion deck for release owners. | demo/release_deck.md, demo/release_deck.json |
| bundle-export | macro-policy-thesis-map bundle-export --root . | Export a public promotion bundle manifest under demo/bundle_export. | demo/bundle_export/manifest.md, demo/bundle_export/manifest.json |
| evidence-bundle | macro-policy-thesis-map evidence-bundle --root . | Collect public evaluation artifacts and source fixture hashes in one bundle. | demo/evidence_bundle.md, demo/evidence_bundle.json |
| public-readiness | macro-policy-thesis-map public-readiness --root . | Summarize public release readiness gates and blockers. | demo/public_readiness.md, demo/public_readiness.json |
| benchmark-suite | macro-policy-thesis-map benchmark-suite --root . | Publish deterministic synthetic evaluator benchmarks and artifact coverage checks. | demo/benchmark_suite.md, demo/benchmark_suite.json |
| integration-cookbook | macro-policy-thesis-map integration-cookbook --root . | Publish public-safe integration recipes for static CSV ingestion and artifact review. | demo/integration_cookbook.md, demo/integration_cookbook.json |
| compatibility-report | macro-policy-thesis-map compatibility-report --root . | Report deterministic package and artifact compatibility gates for public evaluators. | demo/compatibility_report.md, demo/compatibility_report.json |
| maintainer-guide | macro-policy-thesis-map maintainer-guide --root . | Publish deterministic maintainer duties, release order, and safety invariants. | demo/maintainer_guide.md, demo/maintainer_guide.json |
| golden-fixtures | macro-policy-thesis-map golden-fixtures --root . | Record static fixture hashes, row counts, schemas, and expected generator outputs. | demo/golden_fixtures.md, demo/golden_fixtures.json |
| regression-summary | macro-policy-thesis-map regression-summary --root . | Summarize deterministic regression gates across tests, scans, readiness, and artifacts. | demo/regression_summary.md, demo/regression_summary.json |
| landing-page | macro-policy-thesis-map landing-page --root . | Write a crisp public landing page for GitHub visitors and first-run evaluators. | demo/landing_page.md, demo/landing_page.json, demo/landing_page.html |
| api-reference | macro-policy-thesis-map api-reference --root . | Write reusable command, artifact, and data-contract reference docs for agent and CLI reuse. | demo/api_reference.md, demo/api_reference.json, demo/api_reference.html |
| workflow-protocol | macro-policy-thesis-map workflow-protocol --root . | Write a reusable protocol layer for agents that need deterministic macro-policy evidence maps. | demo/workflow_protocol.md, demo/workflow_protocol.json, demo/workflow_protocol.html |
| example-pack | macro-policy-thesis-map example-pack --root . | Write a public example pack with stable command recipes and expected static artifacts. | demo/example_pack.md, demo/example_pack.json, demo/example_pack.html |
| roadmap-next | macro-policy-thesis-map roadmap-next --root . | Write bounded next-step roadmap items for public maintainers and agent reuse. | demo/roadmap_next.md, demo/roadmap_next.json, demo/roadmap_next.html |
| trust-report | macro-policy-thesis-map trust-report --root . | Summarize GitHub stranger trust evidence from local artifacts, safety gates, and reproducibility checks. | demo/trust_report.md, demo/trust_report.json |
| citation-map | macro-policy-thesis-map citation-map --root . | Map public claims to local artifacts, paths, hashes, and producer commands. | demo/citation_map.md, demo/citation_map.json |
| release-faq | macro-policy-thesis-map release-faq --root . | Write a public release FAQ for first-time GitHub visitors and evaluators. | demo/release_faq.md, demo/release_faq.json |
| artifact-index | macro-policy-thesis-map artifact-index --root . | Index deterministic public demo artifacts by format, producer command, size, and hash. | demo/artifact_index.md, demo/artifact_index.json |
| evaluator-scorecard | macro-policy-thesis-map evaluator-scorecard --root . | Score public evaluator readiness across trust, citations, artifacts, tests, and safety boundaries. | demo/evaluator_scorecard.md, demo/evaluator_scorecard.json |
| cold-start-walkthrough | macro-policy-thesis-map cold-start-walkthrough --root . | Generate a deterministic first-run walkthrough for public evaluators. | demo/cold_start_walkthrough.md, demo/cold_start_walkthrough.json |
| public-scan | macro-policy-thesis-map public-scan --root . | Scan publishable text for private names, paths, and credential-shaped terms. | stdout pass/fail |
| diff-check | macro-policy-thesis-map diff-check --root . | Compare the saved release manifest against current file hashes. | stdout pass/fail |
| selfcheck | macro-policy-thesis-map selfcheck --root . | Run source-tree checks for files, boundaries, and public scan status. | stdout pass/fail |

## Data Contracts

| Contract | Format | Required columns | Consumers |
| --- | --- | --- | --- |
| base_event_csv | csv | date, event_type, source, policy_area, channel, direction, confidence, evidence, thesis_link | build-packet, compare-history, review-ledger, fixture-doctor, static-dashboard |
| case_gallery_csv | csv | case_id, region, case_title, date, policy_area, channel, direction, confidence, evidence, route, command | case-gallery, visual-receipt |
| thesis_sensitivity_csv | csv | thesis_id, policy_area, sensitivity_axis, shock_label, impact_direction, impact_score, confidence, rationale | thesis-impact-brief, exposure-map, static-dashboard |
| portfolio_exposure_csv | csv | portfolio_id, sleeve, exposure_id, policy_area, thesis_id, exposure_direction, exposure_score, rationale | exposure-map, static-dashboard |

## Artifact Contracts

| Path | Format | Producer | Stability |
| --- | --- | --- | --- |
| demo/thesis_packet.md | md | build-packet | deterministic local output |
| demo/thesis_packet.json | json | build-packet | deterministic local output |
| demo/history_comparison.md | md | compare-history | deterministic local output |
| demo/history_comparison.json | json | compare-history | deterministic local output |
| demo/review_ledger.md | md | review-ledger | deterministic local output |
| demo/review_ledger.json | json | review-ledger | deterministic local output |
| demo/static_dashboard.html | html | static-dashboard | deterministic local output |
| demo/thesis_impact_brief.md | md | thesis-impact-brief | deterministic local output |
| demo/thesis_impact_brief.json | json | thesis-impact-brief | deterministic local output |
| demo/exposure_map.md | md | exposure-map | deterministic local output |
| demo/exposure_map.json | json | exposure-map | deterministic local output |
| demo/scenario_library.md | md | scenario-library | deterministic local output |
| demo/scenario_library.json | json | scenario-library | deterministic local output |
| demo/assumption_registry.md | md | assumption-registry | deterministic local output |
| demo/assumption_registry.json | json | assumption-registry | deterministic local output |
| demo/data_dictionary_diff.md | md | data-dictionary-diff | deterministic local output |
| demo/data_dictionary_diff.json | json | data-dictionary-diff | deterministic local output |
| demo/case_gallery.md | md | case-gallery | deterministic local output |
| demo/case_gallery.json | json | case-gallery | deterministic local output |
| demo/visual_receipt.svg or demo/visual_receipt.html | html | visual-receipt | deterministic local output |
| demo/visual_receipt.json | json | visual-receipt | deterministic local output |
| demo/fixture_doctor.md | md | fixture-doctor | deterministic local output |
| demo/fixture_doctor.json | json | fixture-doctor | deterministic local output |
| demo/input_schema.md | md | schema-export | deterministic local output |
| demo/input_schema.json | json | schema-export | deterministic local output |
| demo/troubleshoot.md | md | troubleshoot | deterministic local output |
| demo/troubleshoot.json | json | troubleshoot | deterministic local output |
| demo/docs_export.md | md | docs-export | deterministic local output |
| demo/docs_export.json | json | docs-export | deterministic local output |
| demo/readme_snippet.md | md | readme-snippet | deterministic local output |
| demo/readme_snippet.json | json | readme-snippet | deterministic local output |
| demo/cli_help.md | md | cli-help | deterministic local output |
| demo/cli_help.json | json | cli-help | deterministic local output |
| demo/release_manifest.md | md | release-manifest | deterministic local output |
| demo/release_manifest.json | json | release-manifest | deterministic local output |
| demo/maturity_report.md | md | maturity-report | deterministic local output |
| demo/maturity_report.json | json | maturity-report | deterministic local output |
| demo/quickstart_check.md | md | quickstart-check | deterministic local output |
| demo/quickstart_check.json | json | quickstart-check | deterministic local output |
| demo/command_matrix.md | md | command-matrix | deterministic local output |
| demo/command_matrix.json | json | command-matrix | deterministic local output |
| demo/adoption_notes.md | md | adoption-notes | deterministic local output |
| demo/adoption_notes.json | json | adoption-notes | deterministic local output |
| demo/reviewer_scorecard.md | md | reviewer-scorecard | deterministic local output |
| demo/reviewer_scorecard.json | json | reviewer-scorecard | deterministic local output |
| demo/release_deck.md | md | release-deck | deterministic local output |
| demo/release_deck.json | json | release-deck | deterministic local output |
| demo/bundle_export/manifest.md | md | bundle-export | deterministic local output |
| demo/bundle_export/manifest.json | json | bundle-export | deterministic local output |
| demo/evidence_bundle.md | md | evidence-bundle | deterministic local output |
| demo/evidence_bundle.json | json | evidence-bundle | deterministic local output |
| demo/public_readiness.md | md | public-readiness | deterministic local output |
| demo/public_readiness.json | json | public-readiness | deterministic local output |
| demo/benchmark_suite.md | md | benchmark-suite | deterministic local output |
| demo/benchmark_suite.json | json | benchmark-suite | deterministic local output |
| demo/integration_cookbook.md | md | integration-cookbook | deterministic local output |
| demo/integration_cookbook.json | json | integration-cookbook | deterministic local output |
| demo/compatibility_report.md | md | compatibility-report | deterministic local output |
| demo/compatibility_report.json | json | compatibility-report | deterministic local output |
| demo/maintainer_guide.md | md | maintainer-guide | deterministic local output |
| demo/maintainer_guide.json | json | maintainer-guide | deterministic local output |
| demo/golden_fixtures.md | md | golden-fixtures | deterministic local output |
| demo/golden_fixtures.json | json | golden-fixtures | deterministic local output |
| demo/regression_summary.md | md | regression-summary | deterministic local output |
| demo/regression_summary.json | json | regression-summary | deterministic local output |
| demo/landing_page.md | md | landing-page | deterministic local output |
| demo/landing_page.json | json | landing-page | deterministic local output |
| demo/landing_page.html | html | landing-page | deterministic local output |
| demo/api_reference.md | md | api-reference | deterministic local output |
| demo/api_reference.json | json | api-reference | deterministic local output |
| demo/api_reference.html | html | api-reference | deterministic local output |
| demo/workflow_protocol.md | md | workflow-protocol | deterministic local output |
| demo/workflow_protocol.json | json | workflow-protocol | deterministic local output |
| demo/workflow_protocol.html | html | workflow-protocol | deterministic local output |
| demo/example_pack.md | md | example-pack | deterministic local output |
| demo/example_pack.json | json | example-pack | deterministic local output |
| demo/example_pack.html | html | example-pack | deterministic local output |
| demo/roadmap_next.md | md | roadmap-next | deterministic local output |
| demo/roadmap_next.json | json | roadmap-next | deterministic local output |
| demo/roadmap_next.html | html | roadmap-next | deterministic local output |
| demo/trust_report.md | md | trust-report | deterministic local output |
| demo/trust_report.json | json | trust-report | deterministic local output |
| demo/citation_map.md | md | citation-map | deterministic local output |
| demo/citation_map.json | json | citation-map | deterministic local output |
| demo/release_faq.md | md | release-faq | deterministic local output |
| demo/release_faq.json | json | release-faq | deterministic local output |
| demo/artifact_index.md | md | artifact-index | deterministic local output |
| demo/artifact_index.json | json | artifact-index | deterministic local output |
| demo/evaluator_scorecard.md | md | evaluator-scorecard | deterministic local output |
| demo/evaluator_scorecard.json | json | evaluator-scorecard | deterministic local output |
| demo/cold_start_walkthrough.md | md | cold-start-walkthrough | deterministic local output |
| demo/cold_start_walkthrough.json | json | cold-start-walkthrough | deterministic local output |

## Unsupported

| Surface |
| --- |
| external API calls |
| live market data |
| broker connections |
| orders |
| recommendations |
| personalized financial advice |
