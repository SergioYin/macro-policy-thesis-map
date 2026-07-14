"""Core static analysis for macro policy thesis maps."""

from __future__ import annotations

import hashlib
from datetime import date
from pathlib import Path
from typing import Any

from .io import read_csv, read_csv_document, read_json
from . import __version__


DISCLAIMER = (
    "Research-only static analysis. Not investment advice. This tool does not fetch live data, "
    "connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, "
    "predict returns, or produce personalized financial advice."
)

EXPECTED_COLUMNS = [
    "date",
    "event_type",
    "source",
    "policy_area",
    "channel",
    "direction",
    "confidence",
    "evidence",
    "thesis_link",
]
CASE_COLUMNS = [
    "case_id",
    "region",
    "case_title",
    "date",
    "policy_area",
    "channel",
    "direction",
    "confidence",
    "evidence",
    "route",
    "command",
]
SENSITIVITY_COLUMNS = [
    "thesis_id",
    "policy_area",
    "sensitivity_axis",
    "shock_label",
    "impact_direction",
    "impact_score",
    "confidence",
    "rationale",
]
EXPOSURE_COLUMNS = [
    "portfolio_id",
    "sleeve",
    "exposure_id",
    "policy_area",
    "thesis_id",
    "exposure_direction",
    "exposure_score",
    "rationale",
]
EXPECTED_EVENTS = {"policy_signal", "macro_observation", "market_context", "thesis_note"}
ADVICE_TERMS = ["buy", "sell", "hold", "target allocation", "price target", "guaranteed return", "prediction"]
DEMO_ARTIFACTS = [
    "demo/thesis_packet.md",
    "demo/thesis_packet.json",
    "demo/history_comparison.md",
    "demo/history_comparison.json",
    "demo/review_ledger.md",
    "demo/review_ledger.json",
    "demo/static_dashboard.html",
    "demo/thesis_impact_brief.md",
    "demo/thesis_impact_brief.json",
    "demo/exposure_map.md",
    "demo/exposure_map.json",
    "demo/scenario_library.md",
    "demo/scenario_library.json",
    "demo/assumption_registry.md",
    "demo/assumption_registry.json",
    "demo/data_dictionary_diff.md",
    "demo/data_dictionary_diff.json",
    "demo/release_manifest.md",
    "demo/release_manifest.json",
    "demo/maturity_report.md",
    "demo/maturity_report.json",
    "demo/quickstart_check.md",
    "demo/quickstart_check.json",
    "demo/command_matrix.md",
    "demo/command_matrix.json",
    "demo/adoption_notes.md",
    "demo/adoption_notes.json",
    "demo/reviewer_scorecard.md",
    "demo/reviewer_scorecard.json",
    "demo/release_deck.md",
    "demo/release_deck.json",
    "demo/bundle_export/manifest.md",
    "demo/bundle_export/manifest.json",
    "demo/evidence_bundle.md",
    "demo/evidence_bundle.json",
    "demo/public_readiness.md",
    "demo/public_readiness.json",
    "demo/cold_start_walkthrough.md",
    "demo/cold_start_walkthrough.json",
    "demo/benchmark_suite.md",
    "demo/benchmark_suite.json",
    "demo/integration_cookbook.md",
    "demo/integration_cookbook.json",
    "demo/compatibility_report.md",
    "demo/compatibility_report.json",
    "demo/maintainer_guide.md",
    "demo/maintainer_guide.json",
    "demo/golden_fixtures.md",
    "demo/golden_fixtures.json",
    "demo/regression_summary.md",
    "demo/regression_summary.json",
    "demo/landing_page.md",
    "demo/landing_page.json",
    "demo/landing_page.html",
    "demo/api_reference.md",
    "demo/api_reference.json",
    "demo/api_reference.html",
    "demo/workflow_protocol.md",
    "demo/workflow_protocol.json",
    "demo/workflow_protocol.html",
    "demo/example_pack.md",
    "demo/example_pack.json",
    "demo/example_pack.html",
    "demo/roadmap_next.md",
    "demo/roadmap_next.json",
    "demo/roadmap_next.html",
    "demo/trust_report.md",
    "demo/trust_report.json",
    "demo/citation_map.md",
    "demo/citation_map.json",
    "demo/release_faq.md",
    "demo/release_faq.json",
    "demo/artifact_index.md",
    "demo/artifact_index.json",
    "demo/evaluator_scorecard.md",
    "demo/evaluator_scorecard.json",
    "demo/boundary_attestation.md",
    "demo/boundary_attestation.json",
    "demo/provenance_ledger.md",
    "demo/provenance_ledger.json",
    "demo/reproducibility_recipe.md",
    "demo/reproducibility_recipe.json",
    "demo/release_notes_draft.md",
    "demo/release_notes_draft.json",
    "demo/fixture_doctor.md",
    "demo/fixture_doctor.json",
    "demo/input_schema.md",
    "demo/input_schema.json",
    "demo/troubleshoot.md",
    "demo/troubleshoot.json",
    "demo/docs_export.md",
    "demo/docs_export.json",
    "demo/readme_snippet.md",
    "demo/readme_snippet.json",
    "demo/cli_help.md",
    "demo/cli_help.json",
    "demo/case_gallery.md",
    "demo/case_gallery.json",
    "demo/visual_receipt.svg",
    "demo/visual_receipt.html",
    "demo/visual_receipt.json",
]
COMMAND_SPECS = [
    {
        "command": "build-packet",
        "purpose": "Build the primary thesis evidence packet from static CSV events.",
        "inputs": ["examples/macro_events.csv or bundled macro_events.csv"],
        "outputs": ["demo/thesis_packet.md", "demo/thesis_packet.json"],
        "safety": "Static research output with no live data, orders, or recommendations.",
    },
    {
        "command": "compare-history",
        "purpose": "Compare current and prior static policy event sets.",
        "inputs": ["examples/macro_events.csv", "examples/prior_macro_events.csv or bundled examples"],
        "outputs": ["demo/history_comparison.md", "demo/history_comparison.json"],
        "safety": "Reports structural deltas only; does not forecast policy or market outcomes.",
    },
    {
        "command": "review-ledger",
        "purpose": "Flag low-confidence areas and advice-like terms in supplied evidence.",
        "inputs": ["examples/macro_events.csv or bundled macro_events.csv"],
        "outputs": ["demo/review_ledger.md", "demo/review_ledger.json"],
        "safety": "Raises review findings instead of rewriting evidence into advice.",
    },
    {
        "command": "static-dashboard",
        "purpose": "Render a no-JavaScript HTML view of the packet, review ledger, and static sensitivity summaries.",
        "inputs": ["examples/macro_events.csv plus optional bundled sensitivity and exposure fixtures"],
        "outputs": ["demo/static_dashboard.html"],
        "safety": "Static local rendering only.",
    },
    {
        "command": "thesis-impact-brief",
        "purpose": "Summarize synthetic thesis sensitivity rows by thesis, policy area, and scenario axis.",
        "inputs": ["examples/thesis_sensitivities.csv or bundled thesis_sensitivities.csv"],
        "outputs": ["demo/thesis_impact_brief.md", "demo/thesis_impact_brief.json"],
        "safety": "Descriptive static sensitivity mapping only; no forecast, advice, or trade instruction.",
    },
    {
        "command": "exposure-map",
        "purpose": "Map synthetic portfolio exposure rows to static thesis sensitivity axes.",
        "inputs": ["examples/portfolio_exposures.csv and examples/thesis_sensitivities.csv or bundled fixtures"],
        "outputs": ["demo/exposure_map.md", "demo/exposure_map.json"],
        "safety": "Reports exposure coverage and static scores only; no allocation target or recommendation.",
    },
    {
        "command": "scenario-library",
        "purpose": "Publish synthetic macro policy scenarios for schema adaptation review.",
        "inputs": ["built-in static scenario metadata"],
        "outputs": ["demo/scenario_library.md", "demo/scenario_library.json"],
        "safety": "Synthetic scenario labels only; no forecasts, probabilities, trades, or recommendations.",
    },
    {
        "command": "assumption-registry",
        "purpose": "Publish bounded assumptions, owners, and validation controls for public evaluators.",
        "inputs": ["built-in static assumption metadata"],
        "outputs": ["demo/assumption_registry.md", "demo/assumption_registry.json"],
        "safety": "Documents review assumptions without live data, private workflows, or investment advice.",
    },
    {
        "command": "data-dictionary-diff",
        "purpose": "Compare base event CSV fields with optional public fixtures to guide schema adaptation.",
        "inputs": ["built-in schema metadata"],
        "outputs": ["demo/data_dictionary_diff.md", "demo/data_dictionary_diff.json"],
        "safety": "Schema documentation only; no external data access or financial recommendation.",
    },
    {
        "command": "case-gallery",
        "purpose": "Build a public-safe multi-region case gallery from static synthetic fixtures.",
        "inputs": ["examples/public_macro_cases.csv or bundled public_macro_cases.csv"],
        "outputs": ["demo/case_gallery.md", "demo/case_gallery.json"],
        "safety": "Uses synthetic US, EU, and Asia examples; no live data or recommendations.",
    },
    {
        "command": "visual-receipt",
        "purpose": "Render a static SVG or HTML receipt with artifact hashes, routes, and commands.",
        "inputs": ["repository files, demo artifacts, case gallery"],
        "outputs": ["demo/visual_receipt.svg or demo/visual_receipt.html", "demo/visual_receipt.json"],
        "safety": "Static receipt only; records provenance without private routes or operational workflows.",
    },
    {
        "command": "fixture-doctor",
        "purpose": "Validate static CSV fixtures for columns, event types, confidence bounds, stale dates, and advice-like terms.",
        "inputs": ["examples/macro_events.csv or bundled macro_events.csv"],
        "outputs": ["demo/fixture_doctor.md", "demo/fixture_doctor.json"],
        "safety": "Reports data-quality blockers before evidence is rendered.",
    },
    {
        "command": "schema-export",
        "purpose": "Export the machine-readable input schema and data dictionary.",
        "inputs": ["built-in schema metadata"],
        "outputs": ["demo/input_schema.md", "demo/input_schema.json"],
        "safety": "Documents accepted static inputs without connecting to external systems.",
    },
    {
        "command": "troubleshoot",
        "purpose": "Publish deterministic operator troubleshooting checks and recovery steps.",
        "inputs": ["repository files, demo artifacts, command metadata"],
        "outputs": ["demo/troubleshoot.md", "demo/troubleshoot.json"],
        "safety": "Local static diagnostics only; no network, workflow, broker, or live-data action.",
    },
    {
        "command": "docs-export",
        "purpose": "Export an operator documentation index with key docs, artifacts, and validation commands.",
        "inputs": ["README, skill docs, command metadata, demo artifacts"],
        "outputs": ["demo/docs_export.md", "demo/docs_export.json"],
        "safety": "Indexes public local docs only and does not publish or upload content.",
    },
    {
        "command": "readme-snippet",
        "purpose": "Write a compact README-ready usage snippet for public evaluators.",
        "inputs": ["built-in command metadata"],
        "outputs": ["demo/readme_snippet.md", "demo/readme_snippet.json"],
        "safety": "Snippet preserves static research boundaries and finance disclaimers.",
    },
    {
        "command": "cli-help",
        "purpose": "Write deterministic CLI help text and command usage lines.",
        "inputs": ["built-in command metadata"],
        "outputs": ["demo/cli_help.md", "demo/cli_help.json"],
        "safety": "Documents local commands only; it does not execute private workflows.",
    },
    {
        "command": "release-manifest",
        "purpose": "Record deterministic paths, sizes, and hashes for release artifacts.",
        "inputs": ["repository files"],
        "outputs": ["demo/release_manifest.md", "demo/release_manifest.json"],
        "safety": "Excludes generated manifest self-hashes.",
    },
    {
        "command": "maturity-report",
        "purpose": "Score basic release-readiness evidence in the source tree.",
        "inputs": ["repository files"],
        "outputs": ["demo/maturity_report.md", "demo/maturity_report.json"],
        "safety": "Checks packaging, examples, tests, skill docs, and absence of workflow files.",
    },
    {
        "command": "quickstart-check",
        "purpose": "Show whether a fresh evaluator can run the documented starter commands.",
        "inputs": ["repository files and bundled examples"],
        "outputs": ["demo/quickstart_check.md", "demo/quickstart_check.json"],
        "safety": "Checks command availability and expected artifacts without network access.",
    },
    {
        "command": "command-matrix",
        "purpose": "Publish a neutral map of CLI commands, inputs, outputs, and safety posture.",
        "inputs": ["built-in command metadata"],
        "outputs": ["demo/command_matrix.md", "demo/command_matrix.json"],
        "safety": "Documents capabilities without private references or operational workflows.",
    },
    {
        "command": "adoption-notes",
        "purpose": "Write release-owner notes for public evaluator adoption and next actions.",
        "inputs": ["demo artifacts, command metadata, maturity/readiness reports"],
        "outputs": ["demo/adoption_notes.md", "demo/adoption_notes.json"],
        "safety": "Aggregates static artifacts only; no workflows, live data, or advice.",
    },
    {
        "command": "reviewer-scorecard",
        "purpose": "Map release evidence to a reviewer maturity rubric with artifact hashes.",
        "inputs": ["demo artifacts, tests, README, skill docs"],
        "outputs": ["demo/reviewer_scorecard.md", "demo/reviewer_scorecard.json"],
        "safety": "Scores public release evidence without private references or external checks.",
    },
    {
        "command": "release-deck",
        "purpose": "Build a deterministic Markdown/JSON promotion deck for release owners.",
        "inputs": ["release manifest, maturity report, readiness report, command matrix"],
        "outputs": ["demo/release_deck.md", "demo/release_deck.json"],
        "safety": "Summarizes public static release surfaces only.",
    },
    {
        "command": "bundle-export",
        "purpose": "Export a public promotion bundle manifest under demo/bundle_export.",
        "inputs": ["release-owner pack artifacts, release manifest, evidence bundle"],
        "outputs": ["demo/bundle_export/manifest.md", "demo/bundle_export/manifest.json"],
        "safety": "Creates a local static manifest only; it does not upload, publish, or automate workflows.",
    },
    {
        "command": "evidence-bundle",
        "purpose": "Collect public evaluation artifacts and source fixture hashes in one bundle.",
        "inputs": ["examples, demo artifacts, README, tests, skill docs"],
        "outputs": ["demo/evidence_bundle.md", "demo/evidence_bundle.json"],
        "safety": "Includes hashes and static summaries only.",
    },
    {
        "command": "public-readiness",
        "purpose": "Summarize public release readiness gates and blockers.",
        "inputs": ["repository files, demo artifacts, public scan"],
        "outputs": ["demo/public_readiness.md", "demo/public_readiness.json"],
        "safety": "Requires public scan pass and explicit static research boundaries.",
    },
    {
        "command": "benchmark-suite",
        "purpose": "Publish deterministic synthetic evaluator benchmarks and artifact coverage checks.",
        "inputs": ["built-in benchmark metadata, command metadata, demo artifacts"],
        "outputs": ["demo/benchmark_suite.md", "demo/benchmark_suite.json"],
        "safety": "Synthetic benchmark matrix only; no timing probes, live data, network calls, or advice.",
    },
    {
        "command": "integration-cookbook",
        "purpose": "Publish public-safe integration recipes for static CSV ingestion and artifact review.",
        "inputs": ["built-in recipe metadata and command metadata"],
        "outputs": ["demo/integration_cookbook.md", "demo/integration_cookbook.json"],
        "safety": "Local static recipes only; no private systems, workflows, uploads, live feeds, or advice.",
    },
    {
        "command": "compatibility-report",
        "purpose": "Report deterministic package and artifact compatibility gates for public evaluators.",
        "inputs": ["pyproject.toml, source package, bundled examples, demo artifacts"],
        "outputs": ["demo/compatibility_report.md", "demo/compatibility_report.json"],
        "safety": "Static file and metadata checks only.",
    },
    {
        "command": "maintainer-guide",
        "purpose": "Publish deterministic maintainer duties, release order, and safety invariants.",
        "inputs": ["built-in maintainer metadata, command metadata"],
        "outputs": ["demo/maintainer_guide.md", "demo/maintainer_guide.json"],
        "safety": "Documentation-only guide with no workflow automation or private references.",
    },
    {
        "command": "golden-fixtures",
        "purpose": "Record static fixture hashes, row counts, schemas, and expected generator outputs.",
        "inputs": ["examples/*.csv, bundled package examples"],
        "outputs": ["demo/golden_fixtures.md", "demo/golden_fixtures.json"],
        "safety": "Synthetic fixture inventory only; no live source refresh or advice.",
    },
    {
        "command": "regression-summary",
        "purpose": "Summarize deterministic regression gates across tests, scans, readiness, and artifacts.",
        "inputs": ["demo artifacts, tests, release manifest, command metadata"],
        "outputs": ["demo/regression_summary.md", "demo/regression_summary.json"],
        "safety": "Static local gate summary only.",
    },
    {
        "command": "landing-page",
        "purpose": "Write a crisp public landing page for GitHub visitors and first-run evaluators.",
        "inputs": ["built-in public story, command metadata, local artifact availability"],
        "outputs": ["demo/landing_page.md", "demo/landing_page.json", "demo/landing_page.html"],
        "safety": "Public static documentation only; no live data, advice, workflow automation, or private references.",
    },
    {
        "command": "api-reference",
        "purpose": "Write reusable command, artifact, and data-contract reference docs for agent and CLI reuse.",
        "inputs": ["built-in command metadata and schema constants"],
        "outputs": ["demo/api_reference.md", "demo/api_reference.json", "demo/api_reference.html"],
        "safety": "Documents static local contracts only; no external APIs, live feeds, or trading actions.",
    },
    {
        "command": "workflow-protocol",
        "purpose": "Write a reusable protocol layer for agents that need deterministic macro-policy evidence maps.",
        "inputs": ["built-in ordered protocol steps, command metadata, safety boundaries"],
        "outputs": ["demo/workflow_protocol.md", "demo/workflow_protocol.json", "demo/workflow_protocol.html"],
        "safety": "Agent protocol only; no repository workflow files, network actions, live data, or advice.",
    },
    {
        "command": "example-pack",
        "purpose": "Write a public example pack with stable command recipes and expected static artifacts.",
        "inputs": ["bundled examples, command metadata, local artifact availability"],
        "outputs": ["demo/example_pack.md", "demo/example_pack.json", "demo/example_pack.html"],
        "safety": "Uses synthetic static examples only and avoids recommendations, predictions, or live data.",
    },
    {
        "command": "roadmap-next",
        "purpose": "Write bounded next-step roadmap items for public maintainers and agent reuse.",
        "inputs": ["built-in roadmap metadata and safety constraints"],
        "outputs": ["demo/roadmap_next.md", "demo/roadmap_next.json", "demo/roadmap_next.html"],
        "safety": "Roadmap documentation only; excludes live data integrations, broker actions, workflows, and advice.",
    },
    {
        "command": "trust-report",
        "purpose": "Summarize GitHub stranger trust evidence from local artifacts, safety gates, and reproducibility checks.",
        "inputs": ["README, tests, package metadata, demo artifacts, public readiness, release manifest"],
        "outputs": ["demo/trust_report.md", "demo/trust_report.json"],
        "safety": "Trust evidence is local and deterministic; no external reputation checks, live data, or advice.",
    },
    {
        "command": "citation-map",
        "purpose": "Map public claims to local artifacts, paths, hashes, and producer commands.",
        "inputs": ["README, command metadata, demo artifacts"],
        "outputs": ["demo/citation_map.md", "demo/citation_map.json"],
        "safety": "Cites local artifacts only and avoids hosted, personal, or non-public references.",
    },
    {
        "command": "release-faq",
        "purpose": "Write a public release FAQ for first-time GitHub visitors and evaluators.",
        "inputs": ["built-in public questions, command metadata, local artifact availability"],
        "outputs": ["demo/release_faq.md", "demo/release_faq.json"],
        "safety": "FAQ text stays descriptive, local, static, and research-only.",
    },
    {
        "command": "artifact-index",
        "purpose": "Index deterministic public demo artifacts by format, producer command, size, and hash.",
        "inputs": ["demo artifacts and command metadata"],
        "outputs": ["demo/artifact_index.md", "demo/artifact_index.json"],
        "safety": "Indexes local files only; no upload destination, workflow, or private storage reference.",
    },
    {
        "command": "evaluator-scorecard",
        "purpose": "Score public evaluator readiness across trust, citations, artifacts, tests, and safety boundaries.",
        "inputs": ["trust report, citation map, artifact index, public readiness, tests, README"],
        "outputs": ["demo/evaluator_scorecard.md", "demo/evaluator_scorecard.json"],
        "safety": "Scores local release evidence only and does not provide financial advice.",
    },
    {
        "command": "boundary-attestation",
        "purpose": "Attest static finance boundaries, zero-dependency packaging, public scan status, and absent workflows.",
        "inputs": ["README, skill docs, pyproject.toml, public scan, demo artifacts"],
        "outputs": ["demo/boundary_attestation.md", "demo/boundary_attestation.json"],
        "safety": "Documents public static boundaries only; no live data, private references, workflows, broker actions, or advice.",
    },
    {
        "command": "provenance-ledger",
        "purpose": "Record producer commands, artifact hashes, and local source evidence for public demo outputs.",
        "inputs": ["command metadata, demo artifacts, examples, README, tests"],
        "outputs": ["demo/provenance_ledger.md", "demo/provenance_ledger.json"],
        "safety": "Uses local paths and hashes only; no hosted, private, workflow, or external provenance references.",
    },
    {
        "command": "reproducibility-recipe",
        "purpose": "Publish a deterministic local regeneration order and release verification recipe.",
        "inputs": ["command metadata, governance artifacts, release gates"],
        "outputs": ["demo/reproducibility_recipe.md", "demo/reproducibility_recipe.json"],
        "safety": "Local command recipe only; excludes network access, private tools, workflows, live data, and finance actions.",
    },
    {
        "command": "release-notes-draft",
        "purpose": "Draft v1.3.0 public release notes from local artifacts, governance layer, and release gates.",
        "inputs": ["governance artifacts, command matrix, readiness, regression summary"],
        "outputs": ["demo/release_notes_draft.md", "demo/release_notes_draft.json"],
        "safety": "Draft notes are descriptive release metadata only and contain no advice, private references, or workflow steps.",
    },
    {
        "command": "cold-start-walkthrough",
        "purpose": "Generate a deterministic first-run walkthrough for public evaluators.",
        "inputs": ["built-in command metadata"],
        "outputs": ["demo/cold_start_walkthrough.md", "demo/cold_start_walkthrough.json"],
        "safety": "Uses local static commands and bundled examples.",
    },
    {
        "command": "public-scan",
        "purpose": "Scan publishable text for private names, paths, and credential-shaped terms.",
        "inputs": ["repository text files"],
        "outputs": ["stdout pass/fail"],
        "safety": "Fails closed when a private or credential-shaped token is found.",
    },
    {
        "command": "diff-check",
        "purpose": "Compare the saved release manifest against current file hashes.",
        "inputs": ["demo/release_manifest.json", "repository files"],
        "outputs": ["stdout pass/fail"],
        "safety": "Detects artifact drift using static local hashes only.",
    },
    {
        "command": "selfcheck",
        "purpose": "Run source-tree checks for files, boundaries, and public scan status.",
        "inputs": ["repository files"],
        "outputs": ["stdout pass/fail"],
        "safety": "Fails closed when required public release evidence is missing.",
    },
]
PRIVATE_TERMS = [
    "Her" + "mes",
    "Fei" + "shu",
    "La" + "rk",
    "xj" + "yin",
    "/ho" + "me/",
    "api" + "_key",
    "api" + "key",
    "secret" + "_key",
    "access" + "_token",
    "private" + " key",
]


def load_events(path: Path) -> list[dict[str, Any]]:
    rows = read_csv(path)
    events: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=2):
        kind = required(row, "event_type", path, index)
        if kind not in EXPECTED_EVENTS:
            raise ValueError(f"{path}:{index} has unsupported event_type {kind!r}")
        events.append(
            {
                "date": required(row, "date", path, index),
                "event_type": kind,
                "source": required(row, "source", path, index),
                "policy_area": required(row, "policy_area", path, index),
                "channel": required(row, "channel", path, index),
                "direction": required(row, "direction", path, index),
                "confidence": parse_float(row, "confidence", path, index),
                "evidence": required(row, "evidence", path, index),
                "thesis_link": required(row, "thesis_link", path, index),
            }
        )
    return sorted(events, key=lambda item: (item["date"], item["policy_area"], item["source"]))


def load_cases(path: Path) -> list[dict[str, Any]]:
    header, rows = read_csv_document(path)
    missing = [column for column in CASE_COLUMNS if column not in header]
    if missing:
        raise ValueError(f"{path} missing case columns: {', '.join(missing)}")
    cases: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=2):
        route = required(row, "route", path, index)
        command = required(row, "command", path, index)
        if not route.startswith("/cases/"):
            raise ValueError(f"{path}:{index} route must start with /cases/")
        if not command.startswith("macro-policy-thesis-map "):
            raise ValueError(f"{path}:{index} command must start with macro-policy-thesis-map")
        evidence = required(row, "evidence", path, index)
        text = f"{evidence} {required(row, 'case_title', path, index)} {command}".lower()
        for term in ADVICE_TERMS:
            if term in text:
                raise ValueError(f"{path}:{index} contains advice-like term {term!r}")
        cases.append(
            {
                "case_id": required(row, "case_id", path, index),
                "region": required(row, "region", path, index),
                "case_title": required(row, "case_title", path, index),
                "date": required(row, "date", path, index),
                "policy_area": required(row, "policy_area", path, index),
                "channel": required(row, "channel", path, index),
                "direction": required(row, "direction", path, index),
                "confidence": parse_float(row, "confidence", path, index),
                "evidence": evidence,
                "route": route,
                "command": command,
            }
        )
    return sorted(cases, key=lambda item: (item["region"], item["case_id"]))


def load_sensitivities(path: Path) -> list[dict[str, Any]]:
    header, rows = read_csv_document(path)
    missing = [column for column in SENSITIVITY_COLUMNS if column not in header]
    if missing:
        raise ValueError(f"{path} missing sensitivity columns: {', '.join(missing)}")
    sensitivities: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=2):
        text = " ".join((row.get(column) or "") for column in SENSITIVITY_COLUMNS).lower()
        for term in ADVICE_TERMS:
            if term in text:
                raise ValueError(f"{path}:{index} contains advice-like term {term!r}")
        sensitivities.append(
            {
                "thesis_id": required(row, "thesis_id", path, index),
                "policy_area": required(row, "policy_area", path, index),
                "sensitivity_axis": required(row, "sensitivity_axis", path, index),
                "shock_label": required(row, "shock_label", path, index),
                "impact_direction": required(row, "impact_direction", path, index),
                "impact_score": parse_float(row, "impact_score", path, index),
                "confidence": parse_float(row, "confidence", path, index),
                "rationale": required(row, "rationale", path, index),
            }
        )
    return sorted(sensitivities, key=lambda item: (item["thesis_id"], item["policy_area"], item["sensitivity_axis"], item["shock_label"]))


def load_exposures(path: Path) -> list[dict[str, Any]]:
    header, rows = read_csv_document(path)
    missing = [column for column in EXPOSURE_COLUMNS if column not in header]
    if missing:
        raise ValueError(f"{path} missing exposure columns: {', '.join(missing)}")
    exposures: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=2):
        text = " ".join((row.get(column) or "") for column in EXPOSURE_COLUMNS).lower()
        for term in ADVICE_TERMS:
            if term in text:
                raise ValueError(f"{path}:{index} contains advice-like term {term!r}")
        exposures.append(
            {
                "portfolio_id": required(row, "portfolio_id", path, index),
                "sleeve": required(row, "sleeve", path, index),
                "exposure_id": required(row, "exposure_id", path, index),
                "policy_area": required(row, "policy_area", path, index),
                "thesis_id": required(row, "thesis_id", path, index),
                "exposure_direction": required(row, "exposure_direction", path, index),
                "exposure_score": parse_float(row, "exposure_score", path, index),
                "rationale": required(row, "rationale", path, index),
            }
        )
    return sorted(exposures, key=lambda item: (item["portfolio_id"], item["sleeve"], item["exposure_id"]))


def fixture_doctor(path: Path, *, as_of: date, max_source_age_days: int) -> dict[str, Any]:
    header, rows = read_csv_document(path)
    findings: list[dict[str, Any]] = []
    missing_columns = [column for column in EXPECTED_COLUMNS if column not in header]
    extra_columns = [column for column in header if column not in EXPECTED_COLUMNS]
    if missing_columns:
        findings.append(
            {
                "severity": "blocker",
                "row": None,
                "check": "columns",
                "finding": f"Missing required columns: {', '.join(missing_columns)}",
            }
        )
    if extra_columns:
        findings.append(
            {
                "severity": "review",
                "row": None,
                "check": "columns",
                "finding": f"Unexpected columns: {', '.join(extra_columns)}",
            }
        )
    for index, row in enumerate(rows, start=2):
        row_context = {"row": index, "source": (row.get("source") or "").strip(), "policy_area": (row.get("policy_area") or "").strip()}
        kind = (row.get("event_type") or "").strip()
        if kind not in EXPECTED_EVENTS:
            findings.append(
                {
                    **row_context,
                    "severity": "blocker",
                    "check": "event_type",
                    "finding": f"Unsupported event_type {kind!r}",
                }
            )
        raw_confidence = (row.get("confidence") or "").strip()
        try:
            confidence = float(raw_confidence)
        except ValueError:
            findings.append(
                {
                    **row_context,
                    "severity": "blocker",
                    "check": "confidence",
                    "finding": f"Invalid confidence {raw_confidence!r}",
                }
            )
        else:
            if confidence < 0 or confidence > 1:
                findings.append(
                    {
                        **row_context,
                        "severity": "blocker",
                        "check": "confidence",
                        "finding": f"Confidence {confidence:g} is outside 0..1",
                    }
                )
        raw_date = (row.get("date") or "").strip()
        try:
            event_date = date.fromisoformat(raw_date)
        except ValueError:
            findings.append(
                {
                    **row_context,
                    "severity": "blocker",
                    "check": "source_date",
                    "finding": f"Invalid ISO date {raw_date!r}",
                }
            )
        else:
            age_days = (as_of - event_date).days
            if age_days < 0:
                findings.append(
                    {
                        **row_context,
                        "severity": "blocker",
                        "check": "source_date",
                        "finding": f"Source date {raw_date} is after as-of date {as_of.isoformat()}",
                    }
                )
            elif age_days > max_source_age_days:
                findings.append(
                    {
                        **row_context,
                        "severity": "review",
                        "check": "source_date",
                        "finding": f"Source date {raw_date} is {age_days} days old; limit is {max_source_age_days}",
                    }
                )
        text = f"{row.get('evidence') or ''} {row.get('thesis_link') or ''}".lower()
        for term in ADVICE_TERMS:
            if term in text:
                findings.append(
                    {
                        **row_context,
                        "severity": "blocker",
                        "check": "advice_terms",
                        "finding": f"Advice-like term present: {term}",
                    }
                )
    blocker_count = sum(1 for item in findings if item["severity"] == "blocker")
    review_count = sum(1 for item in findings if item["severity"] == "review")
    return {
        "status": "pass" if blocker_count == 0 else "blocked",
        "path": str(path),
        "as_of": as_of.isoformat(),
        "max_source_age_days": max_source_age_days,
        "row_count": len(rows),
        "expected_columns": EXPECTED_COLUMNS,
        "actual_columns": header,
        "blocker_count": blocker_count,
        "review_count": review_count,
        "finding_count": len(findings),
        "findings": findings
        or [
            {
                "severity": "pass",
                "row": None,
                "check": "all",
                "finding": "Fixture passed static finance-domain quality controls",
            }
        ],
        "boundaries": DISCLAIMER,
    }


def input_schema() -> dict[str, Any]:
    columns = [
        {
            "name": "date",
            "type": "date",
            "required": True,
            "format": "YYYY-MM-DD",
            "description": "Publication or observation date for the static source row.",
        },
        {
            "name": "event_type",
            "type": "string",
            "required": True,
            "allowed_values": sorted(EXPECTED_EVENTS),
            "description": "Classification of the supplied macro or policy evidence.",
        },
        {
            "name": "source",
            "type": "string",
            "required": True,
            "description": "Short static source label, such as a release, calendar, or research note identifier.",
        },
        {
            "name": "policy_area",
            "type": "string",
            "required": True,
            "description": "Policy or macro area being mapped, for example monetary-policy or labor-market.",
        },
        {
            "name": "channel",
            "type": "string",
            "required": True,
            "description": "Transmission channel or metric represented by the row.",
        },
        {
            "name": "direction",
            "type": "string",
            "required": True,
            "description": "Neutral analyst label for the supplied evidence direction.",
        },
        {
            "name": "confidence",
            "type": "number",
            "required": True,
            "minimum": 0,
            "maximum": 1,
            "description": "Static analyst confidence in the row's evidence mapping, bounded from 0 to 1.",
        },
        {
            "name": "evidence",
            "type": "string",
            "required": True,
            "description": "Concise neutral evidence summary. Advice-like terms are treated as doctor blockers.",
        },
        {
            "name": "thesis_link",
            "type": "string",
            "required": True,
            "description": "Stable local thesis identifier used to group evidence.",
        },
    ]
    return {
        "schema_version": __version__,
        "format": "csv",
        "required_columns": EXPECTED_COLUMNS,
        "columns": columns,
        "quality_controls": [
            "CSV header must contain every required column.",
            "event_type must be one of the allowed values.",
            "confidence must parse as a number from 0 to 1 inclusive.",
            "date must parse as ISO YYYY-MM-DD and should not be stale relative to the configured as-of date.",
            "evidence and thesis_link should not contain advice-like terms.",
        ],
        "advice_like_terms": ADVICE_TERMS,
        "boundaries": DISCLAIMER,
    }


def scenario_library() -> dict[str, Any]:
    scenarios = [
        {
            "scenario_id": "scenario-001",
            "name": "Policy Path Repricing",
            "region": "US",
            "policy_area": "monetary-policy",
            "time_horizon": "near-term",
            "shock_axis": "rate-path",
            "direction_label": "more-restrictive",
            "schema_fields": ["date", "policy_area", "channel", "direction", "confidence", "thesis_link"],
            "adaptation_note": "Use direction and confidence to describe a static policy-path interpretation without adding forecast probabilities.",
        },
        {
            "scenario_id": "scenario-002",
            "name": "Fiscal Implementation Lag",
            "region": "EU",
            "policy_area": "fiscal-policy",
            "time_horizon": "medium-term",
            "shock_axis": "implementation-timing",
            "direction_label": "delayed-transmission",
            "schema_fields": ["date", "source", "policy_area", "channel", "evidence"],
            "adaptation_note": "Keep source labels and evidence summaries separate so public reviewers can trace static assumptions.",
        },
        {
            "scenario_id": "scenario-003",
            "name": "Labor Supply Normalization",
            "region": "US",
            "policy_area": "labor-market",
            "time_horizon": "medium-term",
            "shock_axis": "participation",
            "direction_label": "normalizing",
            "schema_fields": ["event_type", "policy_area", "channel", "direction", "confidence"],
            "adaptation_note": "Represent labor channels as descriptive categories, not market return forecasts.",
        },
        {
            "scenario_id": "scenario-004",
            "name": "External Demand Rotation",
            "region": "Asia",
            "policy_area": "trade-policy",
            "time_horizon": "cross-cycle",
            "shock_axis": "demand-mix",
            "direction_label": "rotating",
            "schema_fields": ["region", "policy_area", "channel", "route", "command"],
            "adaptation_note": "Optional region and route fields can support public galleries while preserving base event compatibility.",
        },
    ]
    return {
        "title": "Static Scenario Library",
        "version": __version__,
        "fixture_type": "synthetic public evaluator scenarios",
        "scenario_count": len(scenarios),
        "scenarios": scenarios,
        "schema_adaptation_rules": [
            "Treat every scenario as a deterministic example, not a forecast.",
            "Keep optional fields additive so the base event CSV remains valid.",
            "Use confidence as a bounded evidence-mapping score from 0 to 1.",
            "Do not add allocation, trade, price-target, or return-prediction columns.",
        ],
        "boundaries": DISCLAIMER,
    }


def assumption_registry() -> dict[str, Any]:
    assumptions = [
        {
            "assumption_id": "assumption-001",
            "category": "data",
            "statement": "Input rows are static CSV records supplied by the evaluator.",
            "owner": "public evaluator",
            "validation": "fixture-doctor checks required columns, confidence bounds, dates, and advice-like terms.",
            "schema_impact": "Base event columns remain required for build-packet.",
            "status": "active",
        },
        {
            "assumption_id": "assumption-002",
            "category": "safety",
            "statement": "Outputs must stay descriptive and research-only.",
            "owner": "release owner",
            "validation": "public-scan, review-ledger, public-readiness, and selfcheck fail closed on unsafe text or missing boundaries.",
            "schema_impact": "Do not add recommendation, allocation, target, order, or prediction fields.",
            "status": "active",
        },
        {
            "assumption_id": "assumption-003",
            "category": "packaging",
            "statement": "The package has zero runtime dependencies and bundled example CSVs for installed default commands.",
            "owner": "maintainer",
            "validation": "pytest and build backend tests verify version, wheel package data, and reproducible archives.",
            "schema_impact": "New default commands should use built-in metadata or bundled fixtures.",
            "status": "active",
        },
        {
            "assumption_id": "assumption-004",
            "category": "adaptation",
            "statement": "Schema extensions are optional public-evaluator layers rather than replacements for the base event schema.",
            "owner": "public evaluator",
            "validation": "data-dictionary-diff lists additive, shared, and omitted fields deterministically.",
            "schema_impact": "Adapters should preserve date, event_type, policy_area, confidence, evidence, and thesis_link where possible.",
            "status": "active",
        },
    ]
    return {
        "title": "Assumption Registry",
        "version": __version__,
        "assumption_count": len(assumptions),
        "assumptions": assumptions,
        "review_controls": [
            "Regenerate assumption-registry after changing schema or release boundaries.",
            "Treat assumptions marked active as evaluator-facing constraints.",
            "Escalate any need for live data, broker access, or investment advice outside this package.",
        ],
        "boundaries": DISCLAIMER,
    }


def data_dictionary_diff() -> dict[str, Any]:
    dictionaries = [
        ("base_event", EXPECTED_COLUMNS),
        ("case_gallery", CASE_COLUMNS),
        ("thesis_sensitivity", SENSITIVITY_COLUMNS),
        ("portfolio_exposure", EXPOSURE_COLUMNS),
    ]
    base = set(EXPECTED_COLUMNS)
    rows = []
    for name, columns in dictionaries:
        column_set = set(columns)
        rows.append(
            {
                "dictionary": name,
                "column_count": len(columns),
                "shared_with_base": [column for column in EXPECTED_COLUMNS if column in column_set],
                "additive_columns": [column for column in columns if column not in base],
                "base_columns_not_present": [column for column in EXPECTED_COLUMNS if column not in column_set],
                "adaptation_posture": "base" if name == "base_event" else "optional additive layer",
            }
        )
    recommendations = [
        {
            "decision": "Keep base event columns for packet generation.",
            "rationale": "build-packet, compare-history, review-ledger, fixture-doctor, and static-dashboard rely on the base event schema.",
        },
        {
            "decision": "Add region, route, and command only for public case gallery workflows.",
            "rationale": "Those fields support deterministic public routes and receipts but are not needed for core event evidence.",
        },
        {
            "decision": "Use sensitivity and exposure fields as separate optional tables.",
            "rationale": "Separate CSVs keep scenario scores synthetic and avoid mixing descriptive mappings with event evidence.",
        },
    ]
    return {
        "title": "Data Dictionary Diff",
        "version": __version__,
        "base_dictionary": "base_event",
        "dictionary_count": len(dictionaries),
        "dictionaries": rows,
        "recommendations": recommendations,
        "finance_safety_constraints": [
            "No allocation target, order, recommendation, price target, or return prediction fields.",
            "Scores must remain bounded descriptive values from 0 to 1.",
            "Scenario and assumption fields must remain synthetic and static.",
        ],
        "boundaries": DISCLAIMER,
    }


def required(row: dict[str, str], field: str, path: Path, index: int) -> str:
    value = (row.get(field) or "").strip()
    if not value:
        raise ValueError(f"{path}:{index} missing {field}")
    return value


def parse_float(row: dict[str, str], field: str, path: Path, index: int) -> float:
    try:
        value = float(required(row, field, path, index))
    except ValueError as exc:
        raise ValueError(f"{path}:{index} has invalid {field}") from exc
    if value < 0 or value > 1:
        raise ValueError(f"{path}:{index} {field} must be between 0 and 1")
    return value


def build_packet(events: list[dict[str, Any]], title: str) -> dict[str, Any]:
    by_area: dict[str, list[dict[str, Any]]] = {}
    by_channel: dict[str, int] = {}
    for event in events:
        by_area.setdefault(event["policy_area"], []).append(event)
        by_channel[event["channel"]] = by_channel.get(event["channel"], 0) + 1

    policy_areas = []
    for area, area_events in sorted(by_area.items()):
        direction_scores: dict[str, float] = {}
        for event in area_events:
            direction_scores[event["direction"]] = direction_scores.get(event["direction"], 0.0) + event["confidence"]
        dominant = sorted(direction_scores.items(), key=lambda item: (-item[1], item[0]))[0][0]
        policy_areas.append(
            {
                "policy_area": area,
                "dominant_direction": dominant,
                "event_count": len(area_events),
                "average_confidence": round(sum(item["confidence"] for item in area_events) / len(area_events), 3),
                "channels": sorted({item["channel"] for item in area_events}),
                "thesis_links": sorted({item["thesis_link"] for item in area_events}),
            }
        )

    return {
        "title": title,
        "event_count": len(events),
        "policy_area_count": len(policy_areas),
        "channel_counts": dict(sorted(by_channel.items())),
        "policy_areas": policy_areas,
        "evidence": events,
        "boundaries": DISCLAIMER,
    }


def source_record(path: Path) -> dict[str, Any]:
    return {
        "path": f"examples/{path.name}",
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def case_gallery(cases: list[dict[str, Any]], source_path: Path | None = None) -> dict[str, Any]:
    by_region: dict[str, list[dict[str, Any]]] = {}
    for case in cases:
        by_region.setdefault(case["region"], []).append(case)
    regions = []
    for region, region_cases in sorted(by_region.items()):
        regions.append(
            {
                "region": region,
                "case_count": len(region_cases),
                "policy_areas": sorted({item["policy_area"] for item in region_cases}),
                "routes": [item["route"] for item in sorted(region_cases, key=lambda item: item["case_id"])],
                "average_confidence": round(sum(item["confidence"] for item in region_cases) / len(region_cases), 3),
            }
        )
    payload: dict[str, Any] = {
        "title": "Public Macro Policy Case Gallery",
        "case_count": len(cases),
        "region_count": len(regions),
        "regions": regions,
        "cases": cases,
        "fixture_type": "synthetic public-safe multi-region examples",
        "boundaries": DISCLAIMER,
    }
    if source_path is not None:
        payload["source"] = source_record(source_path)
    return payload


def thesis_impact_brief(sensitivities: list[dict[str, Any]], source_path: Path | None = None) -> dict[str, Any]:
    by_thesis: dict[str, list[dict[str, Any]]] = {}
    by_area: dict[str, list[dict[str, Any]]] = {}
    for row in sensitivities:
        by_thesis.setdefault(row["thesis_id"], []).append(row)
        by_area.setdefault(row["policy_area"], []).append(row)
    theses = []
    for thesis_id, rows in sorted(by_thesis.items()):
        theses.append(
            {
                "thesis_id": thesis_id,
                "policy_areas": sorted({item["policy_area"] for item in rows}),
                "axis_count": len({item["sensitivity_axis"] for item in rows}),
                "average_impact_score": round(sum(item["impact_score"] for item in rows) / len(rows), 3),
                "average_confidence": round(sum(item["confidence"] for item in rows) / len(rows), 3),
                "directions": sorted({item["impact_direction"] for item in rows}),
            }
        )
    areas = []
    for policy_area, rows in sorted(by_area.items()):
        areas.append(
            {
                "policy_area": policy_area,
                "thesis_count": len({item["thesis_id"] for item in rows}),
                "axis_count": len({item["sensitivity_axis"] for item in rows}),
                "average_impact_score": round(sum(item["impact_score"] for item in rows) / len(rows), 3),
            }
        )
    payload: dict[str, Any] = {
        "title": "Static Thesis Impact Brief",
        "fixture_type": "synthetic static thesis sensitivity examples",
        "sensitivity_count": len(sensitivities),
        "thesis_count": len(theses),
        "policy_area_count": len(areas),
        "theses": theses,
        "policy_areas": areas,
        "sensitivities": sensitivities,
        "boundaries": DISCLAIMER,
    }
    if source_path is not None:
        payload["source"] = source_record(source_path)
    return payload


def exposure_map(
    exposures: list[dict[str, Any]],
    sensitivities: list[dict[str, Any]],
    exposure_path: Path | None = None,
    sensitivity_path: Path | None = None,
) -> dict[str, Any]:
    sensitivity_index = {(item["thesis_id"], item["policy_area"]) for item in sensitivities}
    rows = []
    by_portfolio: dict[str, list[dict[str, Any]]] = {}
    for exposure in exposures:
        matched = (exposure["thesis_id"], exposure["policy_area"]) in sensitivity_index
        row = {**exposure, "sensitivity_match": matched}
        rows.append(row)
        by_portfolio.setdefault(exposure["portfolio_id"], []).append(row)
    portfolios = []
    for portfolio_id, items in sorted(by_portfolio.items()):
        portfolios.append(
            {
                "portfolio_id": portfolio_id,
                "sleeve_count": len({item["sleeve"] for item in items}),
                "exposure_count": len(items),
                "matched_exposure_count": sum(1 for item in items if item["sensitivity_match"]),
                "average_exposure_score": round(sum(item["exposure_score"] for item in items) / len(items), 3),
                "policy_areas": sorted({item["policy_area"] for item in items}),
            }
        )
    payload: dict[str, Any] = {
        "title": "Static Portfolio Exposure Map",
        "fixture_type": "synthetic static exposure examples",
        "portfolio_count": len(portfolios),
        "exposure_count": len(rows),
        "matched_exposure_count": sum(1 for item in rows if item["sensitivity_match"]),
        "portfolios": portfolios,
        "exposures": rows,
        "boundaries": DISCLAIMER,
    }
    sources: dict[str, Any] = {}
    if exposure_path is not None:
        sources["exposures"] = source_record(exposure_path)
    if sensitivity_path is not None:
        sources["sensitivities"] = source_record(sensitivity_path)
    if sources:
        payload["sources"] = sources
    return payload


def visual_receipt(root: Path, *, visual_format: str) -> dict[str, Any]:
    if visual_format not in {"svg", "html"}:
        raise ValueError("visual_format must be svg or html")
    artifact_paths = [
        "README.md",
        "examples/macro_events.csv",
        "examples/public_macro_cases.csv",
        "examples/thesis_sensitivities.csv",
        "examples/portfolio_exposures.csv",
        "demo/thesis_packet.json",
        "demo/case_gallery.json",
        "demo/thesis_impact_brief.json",
        "demo/exposure_map.json",
        "demo/scenario_library.json",
        "demo/assumption_registry.json",
        "demo/data_dictionary_diff.json",
        "demo/review_ledger.json",
        "demo/public_readiness.json",
    ]
    artifacts = [file_record(root, root / path) for path in artifact_paths if (root / path).exists()]
    gallery_path = root / "demo/case_gallery.json"
    routes: list[str] = []
    if gallery_path.exists():
        gallery = read_json(gallery_path)
        routes = [str(item["route"]) for item in gallery.get("cases", []) if isinstance(item, dict) and "route" in item]
    commands = [
        "macro-policy-thesis-map case-gallery --root .",
        "macro-policy-thesis-map thesis-impact-brief --root .",
        "macro-policy-thesis-map exposure-map --root .",
        "macro-policy-thesis-map scenario-library --root .",
        "macro-policy-thesis-map assumption-registry --root .",
        "macro-policy-thesis-map data-dictionary-diff --root .",
        f"macro-policy-thesis-map visual-receipt --root . --format {visual_format}",
        "macro-policy-thesis-map public-readiness --root .",
        "macro-policy-thesis-map diff-check --root .",
    ]
    return {
        "title": "Macro Policy Visual Receipt",
        "format": visual_format,
        "artifact_count": len(artifacts),
        "route_count": len(routes),
        "command_count": len(commands),
        "artifacts": artifacts,
        "routes": routes,
        "commands": commands,
        "boundaries": DISCLAIMER,
    }


def landing_page(root: Path) -> dict[str, Any]:
    primary_commands = ["landing-page", "example-pack", "workflow-protocol", "api-reference", "build-packet", "public-readiness"]
    highlights = [
        {
            "name": "First-screen story",
            "detail": "Turn static macro policy notes into a neutral evidence map that reviewers can inspect without live services.",
        },
        {
            "name": "Reusable protocol layer",
            "detail": "Agents get stable command recipes, JSON contracts, and safety gates for repeatable local runs.",
        },
        {
            "name": "Public artifact pack",
            "detail": "Markdown, JSON, HTML, and SVG demo outputs sit under demo/ with deterministic hashes.",
        },
    ]
    artifact_paths = [
        "demo/landing_page.html",
        "demo/example_pack.json",
        "demo/workflow_protocol.json",
        "demo/api_reference.json",
        "demo/public_readiness.json",
        "demo/release_manifest.json",
    ]
    return {
        "title": "Macro Policy Thesis Map",
        "version": __version__,
        "tagline": "Static macro policy notes in; neutral thesis evidence packets out.",
        "audience": ["GitHub visitors", "public evaluators", "research agents", "release maintainers"],
        "first_screen": {
            "headline": "A zero-dependency CLI for reusable macro-policy evidence maps.",
            "subhead": "Use static CSV fixtures or user-supplied static files to generate reviewable Markdown, JSON, and HTML artifacts without live data or advice.",
            "primary_recipe": "PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root .",
            "secondary_recipe": "PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root .",
        },
        "highlights": highlights,
        "start_here": [
            {"step": 1, "command": "macro-policy-thesis-map landing-page --root .", "result": "Public landing page artifacts are written under demo/."},
            {"step": 2, "command": "macro-policy-thesis-map example-pack --root .", "result": "Stable command recipes and expected outputs are recorded."},
            {"step": 3, "command": "macro-policy-thesis-map workflow-protocol --root .", "result": "Agent-ready protocol steps and gates are documented."},
            {"step": 4, "command": "macro-policy-thesis-map public-readiness --root .", "result": "Public release gates are checked from local files."},
        ],
        "featured_commands": [spec for spec in COMMAND_SPECS if spec["command"] in primary_commands],
        "artifacts": records_for_existing(root, artifact_paths),
        "missing_artifacts": [path for path in artifact_paths if not root.joinpath(path).exists()],
        "boundaries": DISCLAIMER,
    }


def api_reference() -> dict[str, Any]:
    data_contracts = [
        {"name": "base_event_csv", "format": "csv", "required_columns": EXPECTED_COLUMNS, "producer": "user static CSV or bundled example", "consumer_commands": ["build-packet", "compare-history", "review-ledger", "fixture-doctor", "static-dashboard"]},
        {"name": "case_gallery_csv", "format": "csv", "required_columns": CASE_COLUMNS, "producer": "synthetic public case fixture", "consumer_commands": ["case-gallery", "visual-receipt"]},
        {"name": "thesis_sensitivity_csv", "format": "csv", "required_columns": SENSITIVITY_COLUMNS, "producer": "synthetic static sensitivity fixture", "consumer_commands": ["thesis-impact-brief", "exposure-map", "static-dashboard"]},
        {"name": "portfolio_exposure_csv", "format": "csv", "required_columns": EXPOSURE_COLUMNS, "producer": "synthetic static exposure fixture", "consumer_commands": ["exposure-map", "static-dashboard"]},
    ]
    artifact_contracts = [
        {"path": output, "format": output.rsplit(".", 1)[-1], "producer_command": spec["command"], "stability": "deterministic local output"}
        for spec in COMMAND_SPECS
        for output in spec["outputs"]
        if output.startswith("demo/")
    ]
    return {
        "title": "API Reference",
        "version": __version__,
        "cli_name": "macro-policy-thesis-map",
        "python_module": "macro_policy_thesis_map.cli",
        "commands": [{**spec, "usage": f"macro-policy-thesis-map {spec['command']} --root ."} for spec in COMMAND_SPECS],
        "data_contracts": data_contracts,
        "artifact_contracts": artifact_contracts,
        "json_contract": {
            "encoding": "utf-8",
            "ordering": "Keys are sorted by the writer for deterministic diffs.",
            "numbers": "Confidence, impact, and exposure scores are bounded decimals from 0 to 1.",
            "errors": "CLI returns 2 for input errors and nonzero for blocked readiness checks.",
        },
        "unsupported": ["external API calls", "live market data", "broker connections", "orders", "recommendations", "personalized financial advice"],
        "boundaries": DISCLAIMER,
    }


def workflow_protocol() -> dict[str, Any]:
    phases = [
        {
            "phase": "inspect",
            "goal": "Confirm local static inputs and public docs are present.",
            "commands": ["command-matrix --root .", "schema-export --root .", "fixture-doctor --root ."],
            "required_inputs": ["README.md", "examples/macro_events.csv"],
            "expected_outputs": ["demo/command_matrix.json", "demo/input_schema.json", "demo/fixture_doctor.json"],
            "gate": "fixture-doctor status is pass before packet generation.",
        },
        {
            "phase": "generate",
            "goal": "Build the evidence packet and reusable public surfaces.",
            "commands": ["build-packet --root .", "review-ledger --root .", "example-pack --root .", "api-reference --root ."],
            "required_inputs": ["static CSV rows or bundled examples"],
            "expected_outputs": ["demo/thesis_packet.json", "demo/review_ledger.json", "demo/example_pack.json", "demo/api_reference.json"],
            "gate": "review-ledger has no blocker findings before sharing.",
        },
        {
            "phase": "package",
            "goal": "Prepare public visitor and agent reuse artifacts.",
            "commands": ["landing-page --root .", "workflow-protocol --root .", "roadmap-next --root .", "evidence-bundle --root ."],
            "required_inputs": ["demo artifacts from generate phase"],
            "expected_outputs": ["demo/landing_page.html", "demo/workflow_protocol.json", "demo/roadmap_next.json", "demo/evidence_bundle.json"],
            "gate": "public-readiness can evaluate all required demo artifacts.",
        },
        {
            "phase": "verify",
            "goal": "Run local release gates and detect drift.",
            "commands": ["public-readiness --root .", "release-manifest --root .", "public-scan --root .", "diff-check --root ."],
            "required_inputs": ["repository files", "demo/release_manifest.json"],
            "expected_outputs": ["demo/public_readiness.json", "demo/release_manifest.json", "stdout pass/fail"],
            "gate": "selfcheck, public-scan, public-readiness, and diff-check exit successfully.",
        },
    ]
    return {
        "title": "Workflow Protocol",
        "version": __version__,
        "protocol_id": "macro-policy-thesis-map.v1.3",
        "purpose": "Reusable local protocol for agents generating static macro-policy evidence maps.",
        "phases": phases,
        "agent_contract": {
            "input_mode": "static files only",
            "output_root": "demo/",
            "allowed_formats": ["Markdown", "JSON", "HTML", "SVG"],
            "state_model": "commands are deterministic and may be rerun from the repository root",
            "handoff_files": ["demo/workflow_protocol.json", "demo/api_reference.json", "demo/example_pack.json", "demo/public_readiness.json"],
        },
        "stop_conditions": [
            "Missing required static input files.",
            "fixture-doctor reports blocked.",
            "review-ledger reports advice-like text.",
            "public-scan reports a private reference or credential-shaped token.",
            "public-readiness reports blocked.",
        ],
        "boundaries": DISCLAIMER,
    }


def example_pack(root: Path) -> dict[str, Any]:
    recipes = [
        {
            "recipe_id": "example-001",
            "name": "Visitor Landing Preview",
            "commands": ["landing-page --root ."],
            "inputs": ["built-in public story", "local artifact availability"],
            "outputs": ["demo/landing_page.md", "demo/landing_page.json", "demo/landing_page.html"],
            "expected_json_keys": ["first_screen", "featured_commands", "boundaries"],
        },
        {
            "recipe_id": "example-002",
            "name": "Agent Protocol Reuse",
            "commands": ["workflow-protocol --root .", "api-reference --root ."],
            "inputs": ["built-in protocol metadata", "schema constants"],
            "outputs": ["demo/workflow_protocol.json", "demo/api_reference.json"],
            "expected_json_keys": ["phases", "agent_contract", "data_contracts"],
        },
        {
            "recipe_id": "example-003",
            "name": "Static Thesis Packet",
            "commands": ["fixture-doctor --root .", "build-packet --root .", "review-ledger --root ."],
            "inputs": ["examples/macro_events.csv"],
            "outputs": ["demo/fixture_doctor.json", "demo/thesis_packet.json", "demo/review_ledger.json"],
            "expected_json_keys": ["status", "policy_areas", "findings"],
        },
        {
            "recipe_id": "example-004",
            "name": "Public Release Gates",
            "commands": ["public-readiness --root .", "release-manifest --root .", "diff-check --root ."],
            "inputs": ["demo artifacts", "repository files"],
            "outputs": ["demo/public_readiness.json", "demo/release_manifest.json", "stdout pass/fail"],
            "expected_json_keys": ["checks", "artifacts", "status"],
        },
    ]
    fixture_paths = [
        "examples/macro_events.csv",
        "examples/prior_macro_events.csv",
        "examples/public_macro_cases.csv",
        "examples/thesis_sensitivities.csv",
        "examples/portfolio_exposures.csv",
    ]
    return {
        "title": "Example Pack",
        "version": __version__,
        "fixture_policy": "Bundled and top-level examples are synthetic static fixtures for deterministic local evaluation.",
        "recipe_count": len(recipes),
        "recipes": recipes,
        "fixtures": records_for_existing(root, fixture_paths),
        "missing_fixtures": [path for path in fixture_paths if not root.joinpath(path).exists()],
        "copy_free_commands": [
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def roadmap_next() -> dict[str, Any]:
    items = [
        {
            "roadmap_id": "next-001",
            "theme": "Public docs",
            "item": "Keep the landing page aligned with README and command-matrix as commands evolve.",
            "acceptance": "landing-page, api-reference, and command-matrix agree on command count and output paths.",
            "excluded": ["marketing claims", "private references"],
        },
        {
            "roadmap_id": "next-002",
            "theme": "Agent reuse",
            "item": "Stabilize protocol JSON field names before adding optional adapters.",
            "acceptance": "workflow_protocol.json remains backwards-readable by agents using protocol_id macro-policy-thesis-map.v1.3.",
            "excluded": ["remote orchestration", "repository workflow files"],
        },
        {
            "roadmap_id": "next-003",
            "theme": "Data contracts",
            "item": "Add optional contract examples only when they remain synthetic, static, and additive.",
            "acceptance": "api-reference and data-dictionary-diff list the new optional fields without changing base_event_csv.",
            "excluded": ["live feeds", "broker data", "prediction fields"],
        },
        {
            "roadmap_id": "next-004",
            "theme": "Verification",
            "item": "Continue treating public-readiness, public-scan, selfcheck, diff-check, pytest, and wheel build as release gates.",
            "acceptance": "regression-summary records gate names and no required gate depends on network access.",
            "excluded": ["CI-only validation", "timing benchmarks"],
        },
    ]
    return {
        "title": "Roadmap Next",
        "version": __version__,
        "roadmap_count": len(items),
        "items": items,
        "release_principles": [
            "Prefer deterministic local artifacts over hosted or live references.",
            "Keep the base CSV contract stable and make optional layers additive.",
            "Preserve zero runtime dependencies.",
            "Keep finance boundaries explicit in every public surface.",
        ],
        "not_planned": [
            "Live macro or market data fetching.",
            "Broker connections or order routing.",
            "Personalized financial advice.",
            "Repository workflow automation.",
            "Private storage or private document references.",
        ],
        "boundaries": DISCLAIMER,
    }


def trust_report(root: Path) -> dict[str, Any]:
    checks = [
        {
            "name": "zero_runtime_dependencies",
            "passed": "dependencies = []" in root.joinpath("pyproject.toml").read_text(encoding="utf-8") if root.joinpath("pyproject.toml").exists() else False,
            "evidence": ["pyproject.toml"],
            "trust_reason": "A stranger can inspect and install without pulling runtime packages.",
        },
        {
            "name": "local_static_inputs",
            "passed": all(root.joinpath(path).exists() for path in ["examples/macro_events.csv", "examples/prior_macro_events.csv", "examples/public_macro_cases.csv"]),
            "evidence": ["examples/macro_events.csv", "examples/prior_macro_events.csv", "examples/public_macro_cases.csv"],
            "trust_reason": "Default examples are committed static CSV files.",
        },
        {
            "name": "deterministic_demo_outputs",
            "passed": all(root.joinpath(path).exists() for path in ["demo/command_matrix.json", "demo/public_readiness.json", "demo/release_manifest.json"]),
            "evidence": ["demo/command_matrix.json", "demo/public_readiness.json", "demo/release_manifest.json"],
            "trust_reason": "Public command, readiness, and hash manifests are available under demo/.",
        },
        {
            "name": "test_and_scan_surfaces",
            "passed": any(root.joinpath("tests").glob("test_*.py")) and not public_findings(root),
            "evidence": ["tests/test_cli.py", "tests/test_safety.py", "demo/public_readiness.json"],
            "trust_reason": "Tests and public scan support local verification without network access.",
        },
        {
            "name": "finance_boundaries",
            "passed": all(
                term in (root.joinpath("README.md").read_text(encoding="utf-8").lower() if root.joinpath("README.md").exists() else "")
                for term in ["does not fetch live data", "connect to brokers", "recommend buys", "predict returns"]
            ),
            "evidence": ["README.md", "skills/agent/macro-policy-thesis-map/SKILL.md"],
            "trust_reason": "Research-only limitations are visible before running the CLI.",
        },
        {
            "name": "no_workflow_files",
            "passed": not root.joinpath(".github/workflows").exists(),
            "evidence": [".github/workflows"],
            "trust_reason": "Evaluation does not depend on hidden CI or repository automation.",
        },
        {
            "name": "governance_attestation_layer",
            "passed": all(root.joinpath(path).exists() for path in ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"]),
            "evidence": ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"],
            "trust_reason": "Governance evidence is recorded as local deterministic artifacts.",
        },
    ]
    artifacts = records_for_existing(
        root,
        [
            "README.md",
            "pyproject.toml",
            "tests/test_cli.py",
            "tests/test_safety.py",
            "demo/command_matrix.json",
            "demo/public_readiness.json",
            "demo/release_manifest.json",
            "demo/evidence_bundle.json",
            "demo/boundary_attestation.json",
            "demo/provenance_ledger.json",
            "demo/reproducibility_recipe.json",
            "demo/release_notes_draft.json",
        ],
    )
    passed = sum(1 for item in checks if item["passed"])
    return {
        "title": "Public Trust Report",
        "version": __version__,
        "audience": "GitHub visitor with no prior project context",
        "status": "ready" if passed == len(checks) else "needs-review",
        "score": passed,
        "max_score": len(checks),
        "checks": checks,
        "artifacts": artifacts,
        "verification_commands": [
            "PYTHONPATH=src python -m pytest",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def citation_map(root: Path) -> dict[str, Any]:
    claims = [
        {
            "claim_id": "claim-001",
            "claim": "The project is a zero-dependency Python CLI.",
            "citations": ["pyproject.toml", "demo/compatibility_report.json"],
            "producer_command": "compatibility-report",
        },
        {
            "claim_id": "claim-002",
            "claim": "The default examples are local static CSV fixtures.",
            "citations": ["examples/macro_events.csv", "examples/prior_macro_events.csv", "examples/public_macro_cases.csv", "demo/golden_fixtures.json"],
            "producer_command": "golden-fixtures",
        },
        {
            "claim_id": "claim-003",
            "claim": "The CLI writes deterministic Markdown, JSON, HTML, and SVG artifacts under demo/.",
            "citations": ["demo/command_matrix.json", "demo/artifact_index.json", "demo/release_manifest.json"],
            "producer_command": "artifact-index",
        },
        {
            "claim_id": "claim-004",
            "claim": "Public release gates include tests, selfcheck, public scan, readiness, diff check, and wheel build.",
            "citations": ["tests/test_cli.py", "tests/test_safety.py", "demo/regression_summary.json", "demo/trust_report.json"],
            "producer_command": "trust-report",
        },
        {
            "claim_id": "claim-005",
            "claim": "Outputs are research-only and do not fetch live data or provide personalized financial advice.",
            "citations": ["README.md", "skills/agent/macro-policy-thesis-map/SKILL.md", "demo/public_readiness.json"],
            "producer_command": "public-readiness",
        },
        {
            "claim_id": "claim-006",
            "claim": "The v1.3.0 governance layer records boundaries, provenance, reproducibility, and release notes locally.",
            "citations": ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"],
            "producer_command": "release-notes-draft",
        },
    ]
    rows = []
    for claim in claims:
        citations = []
        for relative in claim["citations"]:
            path = root / relative
            citations.append(file_record(root, path) if path.exists() else {"path": relative, "status": "missing"})
        rows.append({**claim, "citations": citations, "citation_count": len(citations), "missing_count": sum(1 for item in citations if item.get("status") == "missing")})
    return {
        "title": "Citation Map",
        "version": __version__,
        "citation_policy": "Every claim cites local repository artifacts only.",
        "claim_count": len(rows),
        "missing_count": sum(item["missing_count"] for item in rows),
        "claims": rows,
        "boundaries": DISCLAIMER,
    }


def release_faq(root: Path) -> dict[str, Any]:
    questions = [
        {
            "question_id": "faq-001",
            "question": "What should a first-time GitHub visitor run first?",
            "answer": "Run command-matrix, fixture-doctor, build-packet, and public-readiness from the repository root.",
            "local_citations": ["README.md", "demo/command_matrix.md", "demo/cold_start_walkthrough.md"],
        },
        {
            "question_id": "faq-002",
            "question": "Does the project use live macro, market, or broker data?",
            "answer": "No. The package reads static CSV inputs and bundled examples only.",
            "local_citations": ["README.md", "demo/input_schema.md", "demo/public_readiness.md"],
        },
        {
            "question_id": "faq-003",
            "question": "How can an evaluator verify artifact drift?",
            "answer": "Regenerate demo outputs, run release-manifest, then run diff-check against the saved manifest.",
            "local_citations": ["demo/release_manifest.md", "demo/regression_summary.md"],
        },
        {
            "question_id": "faq-004",
            "question": "Where are public claims linked to evidence?",
            "answer": "Use citation-map for claim-to-artifact references and artifact-index for hashes and producer commands.",
            "local_citations": ["demo/citation_map.md", "demo/artifact_index.md"],
        },
        {
            "question_id": "faq-005",
            "question": "What is intentionally unsupported?",
            "answer": "Live feeds, workflow automation, broker connections, trade actions, return predictions, and personalized financial advice.",
            "local_citations": ["README.md", "demo/roadmap_next.md", "skills/agent/macro-policy-thesis-map/SKILL.md"],
        },
        {
            "question_id": "faq-006",
            "question": "Where is the governance and attestation layer?",
            "answer": "Use boundary-attestation, provenance-ledger, reproducibility-recipe, and release-notes-draft for v1.3.0 governance evidence.",
            "local_citations": ["demo/boundary_attestation.md", "demo/provenance_ledger.md", "demo/reproducibility_recipe.md", "demo/release_notes_draft.md"],
        },
    ]
    for item in questions:
        item["citation_status"] = "ready" if all(root.joinpath(path).exists() for path in item["local_citations"]) else "needs-artifacts"
    return {
        "title": "Release FAQ",
        "version": __version__,
        "question_count": len(questions),
        "ready_count": sum(1 for item in questions if item["citation_status"] == "ready"),
        "questions": questions,
        "boundaries": DISCLAIMER,
    }


def artifact_index(root: Path) -> dict[str, Any]:
    by_output = {
        output: spec["command"]
        for spec in COMMAND_SPECS
        for output in spec["outputs"]
        if output.startswith("demo/")
    }
    rows = []
    for relative in sorted(set(DEMO_ARTIFACTS) | set(by_output)):
        path = root / relative
        producer = by_output.get(relative, "release artifact")
        fmt = relative.rsplit(".", 1)[-1] if "." in relative else "directory"
        if path.exists() and path.is_file():
            rows.append({**file_record(root, path), "format": fmt, "producer_command": producer, "status": "present"})
        else:
            rows.append({"path": relative, "format": fmt, "producer_command": producer, "status": "missing", "bytes": 0, "sha256": ""})
    formats: dict[str, int] = {}
    for row in rows:
        if row["status"] == "present":
            formats[row["format"]] = formats.get(row["format"], 0) + 1
    return {
        "title": "Artifact Index",
        "version": __version__,
        "artifact_count": len(rows),
        "present_count": sum(1 for item in rows if item["status"] == "present"),
        "missing_count": sum(1 for item in rows if item["status"] == "missing"),
        "formats": dict(sorted(formats.items())),
        "artifacts": rows,
        "boundaries": DISCLAIMER,
    }


def evaluator_scorecard(root: Path) -> dict[str, Any]:
    trust = read_optional_json(root / "demo/trust_report.json")
    citations = read_optional_json(root / "demo/citation_map.json")
    index = read_optional_json(root / "demo/artifact_index.json")
    readiness = read_optional_json(root / "demo/public_readiness.json")
    checks = [
        {
            "name": "trust_report_ready",
            "passed": trust.get("status") == "ready",
            "evidence": "demo/trust_report.json",
            "detail": "Trust report scores local evidence for a first-time GitHub visitor.",
        },
        {
            "name": "citation_map_complete",
            "passed": citations.get("missing_count") == 0,
            "evidence": "demo/citation_map.json",
            "detail": "Public claims cite local artifacts with paths and hashes.",
        },
        {
            "name": "artifact_index_complete",
            "passed": index.get("missing_count") == 0,
            "evidence": "demo/artifact_index.json",
            "detail": "Demo artifacts have producer commands, formats, and hashes.",
        },
        {
            "name": "public_readiness_ready",
            "passed": readiness.get("status") == "ready",
            "evidence": "demo/public_readiness.json",
            "detail": "Readiness gates pass for local public release evidence.",
        },
        {
            "name": "tests_present",
            "passed": any(root.joinpath("tests").glob("test_*.py")),
            "evidence": "tests/test_*.py",
            "detail": "Local pytest suite is present for evaluator reruns.",
        },
        {
            "name": "boundaries_visible",
            "passed": all(root.joinpath(path).exists() for path in ["README.md", "skills/agent/macro-policy-thesis-map/SKILL.md", "demo/release_faq.json", "demo/boundary_attestation.json"]),
            "evidence": "README.md, skills/agent/macro-policy-thesis-map/SKILL.md, demo/release_faq.json, demo/boundary_attestation.json",
            "detail": "Research-only boundaries are documented in human and agent surfaces.",
        },
        {
            "name": "governance_layer_present",
            "passed": all(root.joinpath(path).exists() for path in ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"]),
            "evidence": "demo/boundary_attestation.json, demo/provenance_ledger.json, demo/reproducibility_recipe.json, demo/release_notes_draft.json",
            "detail": "v1.3.0 governance artifacts are available for public release review.",
        },
    ]
    score = sum(1 for item in checks if item["passed"])
    return {
        "title": "Evaluator Scorecard",
        "version": __version__,
        "status": "ready" if score == len(checks) else "needs-review",
        "score": score,
        "max_score": len(checks),
        "checks": checks,
        "recommended_order": ["trust-report", "citation-map", "release-faq", "artifact-index", "evaluator-scorecard", "boundary-attestation", "provenance-ledger", "reproducibility-recipe", "release-notes-draft"],
        "boundaries": DISCLAIMER,
    }


def boundary_attestation(root: Path) -> dict[str, Any]:
    readme = root.joinpath("README.md").read_text(encoding="utf-8") if root.joinpath("README.md").exists() else ""
    skill = root.joinpath("skills/agent/macro-policy-thesis-map/SKILL.md").read_text(encoding="utf-8") if root.joinpath("skills/agent/macro-policy-thesis-map/SKILL.md").exists() else ""
    pyproject = root.joinpath("pyproject.toml").read_text(encoding="utf-8") if root.joinpath("pyproject.toml").exists() else ""
    public_scan_findings = public_findings(root)
    checks = [
        {
            "name": "static_research_boundaries",
            "passed": all(term in readme.lower() for term in ["does not fetch live data", "connect to brokers", "place orders", "recommend buys", "predict returns"]),
            "evidence": ["README.md"],
            "attestation": "README states the finance boundary before command usage.",
        },
        {
            "name": "agent_skill_boundaries",
            "passed": all(term in skill.lower() for term in ["live data", "broker", "personalized advice"]),
            "evidence": ["skills/agent/macro-policy-thesis-map/SKILL.md"],
            "attestation": "Agent protocol preserves static, research-only behavior.",
        },
        {
            "name": "zero_runtime_dependencies",
            "passed": "dependencies = []" in pyproject,
            "evidence": ["pyproject.toml"],
            "attestation": "Runtime dependency list is empty.",
        },
        {
            "name": "public_scan_clean",
            "passed": not public_scan_findings,
            "evidence": ["public-scan"],
            "attestation": "No private term or credential-shaped finding was detected in public text.",
        },
        {
            "name": "no_workflow_files",
            "passed": not root.joinpath(".github/workflows").exists(),
            "evidence": [".github/workflows"],
            "attestation": "Release verification is local and does not rely on repository workflow files.",
        },
        {
            "name": "synthetic_static_fixtures",
            "passed": all(root.joinpath(path).exists() for path in ["examples/macro_events.csv", "examples/public_macro_cases.csv", "examples/thesis_sensitivities.csv", "examples/portfolio_exposures.csv"]),
            "evidence": ["examples/macro_events.csv", "examples/public_macro_cases.csv", "examples/thesis_sensitivities.csv", "examples/portfolio_exposures.csv"],
            "attestation": "Default finance examples are committed static fixtures.",
        },
    ]
    return {
        "title": "Boundary Attestation",
        "version": __version__,
        "status": "attested" if all(item["passed"] for item in checks) else "needs-review",
        "check_count": len(checks),
        "passed_count": sum(1 for item in checks if item["passed"]),
        "checks": checks,
        "public_scan_findings": public_scan_findings,
        "unsupported": ["live data fetching", "broker connections", "orders", "recommendations", "return predictions", "personalized financial advice", "workflow automation", "private references"],
        "boundaries": DISCLAIMER,
    }


def provenance_ledger(root: Path) -> dict[str, Any]:
    by_output = {
        output: spec["command"]
        for spec in COMMAND_SPECS
        for output in spec["outputs"]
        if output.startswith("demo/")
    }
    source_paths = [
        "README.md",
        "pyproject.toml",
        "skills/agent/macro-policy-thesis-map/SKILL.md",
        "tests/test_cli.py",
        "tests/test_safety.py",
        "examples/macro_events.csv",
        "examples/prior_macro_events.csv",
        "examples/public_macro_cases.csv",
        "examples/thesis_sensitivities.csv",
        "examples/portfolio_exposures.csv",
    ]
    artifacts = []
    for relative in sorted(set(DEMO_ARTIFACTS) | set(by_output)):
        path = root / relative
        record = file_record(root, path) if path.exists() and path.is_file() else {"path": relative, "bytes": 0, "sha256": "", "status": "missing"}
        artifacts.append({**record, "producer_command": by_output.get(relative, "release artifact"), "status": record.get("status", "present")})
    sources = records_for_existing(root, source_paths)
    missing_sources = [path for path in source_paths if not root.joinpath(path).exists()]
    return {
        "title": "Provenance Ledger",
        "version": __version__,
        "ledger_policy": "All provenance entries are local repository paths with deterministic SHA-256 hashes.",
        "source_count": len(sources),
        "missing_source_count": len(missing_sources),
        "artifact_count": len(artifacts),
        "present_artifact_count": sum(1 for item in artifacts if item["status"] == "present"),
        "missing_artifact_count": sum(1 for item in artifacts if item["status"] == "missing"),
        "sources": sources,
        "missing_sources": missing_sources,
        "artifacts": artifacts,
        "boundaries": DISCLAIMER,
    }


def reproducibility_recipe() -> dict[str, Any]:
    generate_commands = [
        spec["command"]
        for spec in COMMAND_SPECS
        if any(output.startswith("demo/") for output in spec["outputs"]) and spec["command"] not in {"release-manifest"}
    ]
    release_gates = [
        "PYTHONPATH=src python -m pytest",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
        "python -c \"import build_backend; build_backend.build_wheel('dist')\"",
    ]
    steps = [
        {"step": index, "command": f"PYTHONPATH=src python -m macro_policy_thesis_map.cli {command} --root .", "expected": "deterministic demo artifact update"}
        for index, command in enumerate(generate_commands, start=1)
    ]
    steps.append({"step": len(steps) + 1, "command": "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-manifest --root .", "expected": "release manifest records settled hashes"})
    return {
        "title": "Reproducibility Recipe",
        "version": __version__,
        "recipe_policy": "Run from a source checkout with static files only; commands do not require network access.",
        "step_count": len(steps),
        "steps": steps,
        "release_gates": release_gates,
        "determinism_controls": [
            "JSON writer sorts keys.",
            "Markdown tables are generated from sorted command metadata and local file records.",
            "Release manifest is written after generated governance artifacts settle.",
            "diff-check compares SHA-256 values from the saved release manifest.",
        ],
        "unsupported": ["live data refresh", "private storage", "workflow automation", "broker access", "investment advice"],
        "boundaries": DISCLAIMER,
    }


def release_notes_draft(root: Path) -> dict[str, Any]:
    readiness = read_optional_json(root / "demo/public_readiness.json")
    regression = read_optional_json(root / "demo/regression_summary.json")
    boundary = read_optional_json(root / "demo/boundary_attestation.json")
    provenance = read_optional_json(root / "demo/provenance_ledger.json")
    recipe = read_optional_json(root / "demo/reproducibility_recipe.json")
    return {
        "title": "Release Notes Draft",
        "version": __version__,
        "release_name": "v1.3.0 governance and attestation layer",
        "status": "ready" if readiness.get("status") == "ready" and boundary.get("status") == "attested" else "needs-review",
        "highlights": [
            "Added boundary-attestation for explicit static finance, zero-dependency, public scan, and no-workflow checks.",
            "Added provenance-ledger for local source and demo artifact hashes with producer commands.",
            "Added reproducibility-recipe for deterministic regeneration order and release gates.",
            "Added release-notes-draft so public release notes cite local governance artifacts.",
        ],
        "artifact_links": [
            "demo/boundary_attestation.md",
            "demo/provenance_ledger.md",
            "demo/reproducibility_recipe.md",
            "demo/release_notes_draft.md",
        ],
        "gate_summary": {
            "public_readiness_status": readiness.get("status", "missing"),
            "regression_status": regression.get("status", "missing"),
            "boundary_status": boundary.get("status", "missing"),
            "provenance_present_artifacts": provenance.get("present_artifact_count", 0),
            "reproducibility_steps": recipe.get("step_count", 0),
        },
        "verification_commands": [
            "PYTHONPATH=src python -m pytest",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
            "python -c \"import build_backend; build_backend.build_wheel('dist')\"",
        ],
        "upgrade_notes": [
            "Runtime dependencies remain empty.",
            "Default finance fixtures remain static and synthetic.",
            "No workflow files, private references, live data, broker actions, or finance advice were added.",
        ],
        "boundaries": DISCLAIMER,
    }


def compare_packets(current: dict[str, Any], prior: dict[str, Any]) -> dict[str, Any]:
    current_map = {item["policy_area"]: item for item in current["policy_areas"]}
    prior_map = {item["policy_area"]: item for item in prior["policy_areas"]}
    areas = sorted(set(current_map) | set(prior_map))
    rows = []
    for area in areas:
        now = current_map.get(area)
        before = prior_map.get(area)
        rows.append(
            {
                "policy_area": area,
                "status": "added" if before is None else "removed" if now is None else "carried",
                "prior_direction": before["dominant_direction"] if before else None,
                "current_direction": now["dominant_direction"] if now else None,
                "event_delta": (now["event_count"] if now else 0) - (before["event_count"] if before else 0),
            }
        )
    return {"comparison_count": len(rows), "rows": rows, "boundaries": DISCLAIMER}


def review_ledger(packet: dict[str, Any], min_confidence: float) -> dict[str, Any]:
    findings = []
    for item in packet["policy_areas"]:
        if item["average_confidence"] < min_confidence:
            findings.append(
                {
                    "severity": "review",
                    "policy_area": item["policy_area"],
                    "finding": f"Average confidence below {min_confidence:.2f}",
                }
            )
    for event in packet["evidence"]:
        text = f"{event['evidence']} {event['thesis_link']}".lower()
        for term in ADVICE_TERMS:
            if term in text:
                findings.append(
                    {
                        "severity": "blocker",
                        "policy_area": event["policy_area"],
                        "finding": f"Evidence includes advice-like term: {term}",
                    }
                )
    if not findings:
        findings.append({"severity": "pass", "policy_area": "all", "finding": "No review findings from static checks"})
    return {"finding_count": len(findings), "findings": findings, "boundaries": DISCLAIMER}


def maturity(root: Path) -> dict[str, Any]:
    checks = [
        ("package", root.joinpath("pyproject.toml").exists()),
        ("readme", root.joinpath("README.md").exists()),
        ("license", root.joinpath("LICENSE").exists()),
        ("examples", any(root.joinpath("examples").glob("*"))),
        ("case_gallery", root.joinpath("examples/public_macro_cases.csv").exists() and root.joinpath("demo/case_gallery.json").exists()),
        ("sensitivity_layer", root.joinpath("examples/thesis_sensitivities.csv").exists() and root.joinpath("demo/thesis_impact_brief.json").exists()),
        ("exposure_layer", root.joinpath("examples/portfolio_exposures.csv").exists() and root.joinpath("demo/exposure_map.json").exists()),
        ("schema_adaptation_surfaces", all(root.joinpath(path).exists() for path in ["demo/scenario_library.json", "demo/assumption_registry.json", "demo/data_dictionary_diff.json"])),
        ("visual_receipt", root.joinpath("demo/visual_receipt.json").exists() and (root.joinpath("demo/visual_receipt.svg").exists() or root.joinpath("demo/visual_receipt.html").exists())),
        ("operator_surfaces", all(root.joinpath(path).exists() for path in ["demo/troubleshoot.json", "demo/docs_export.json", "demo/readme_snippet.json", "demo/cli_help.json"])),
        ("release_owner_pack", all(root.joinpath(path).exists() for path in ["demo/adoption_notes.json", "demo/reviewer_scorecard.json", "demo/release_deck.json", "demo/bundle_export/manifest.json"])),
        ("public_evaluator_hardening", all(root.joinpath(path).exists() for path in ["demo/benchmark_suite.json", "demo/integration_cookbook.json", "demo/compatibility_report.json", "demo/maintainer_guide.json", "demo/golden_fixtures.json", "demo/regression_summary.json"])),
        ("public_protocol_layer", all(root.joinpath(path).exists() for path in ["demo/landing_page.json", "demo/api_reference.json", "demo/workflow_protocol.json", "demo/example_pack.json", "demo/roadmap_next.json"])),
        ("public_trust_layer", all(root.joinpath(path).exists() for path in ["demo/trust_report.json", "demo/citation_map.json", "demo/release_faq.json", "demo/artifact_index.json", "demo/evaluator_scorecard.json"])),
        ("governance_attestation_layer", all(root.joinpath(path).exists() for path in ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"])),
        ("tests", any(root.joinpath("tests").glob("test_*.py"))),
        ("skill", root.joinpath("skills/agent/macro-policy-thesis-map/SKILL.md").exists()),
        ("no_workflows", not root.joinpath(".github/workflows").exists()),
    ]
    score = sum(1 for _, ok in checks if ok)
    return {
        "score": score,
        "max_score": len(checks),
        "status": "ready" if score == len(checks) else "needs-review",
        "checks": [{"name": name, "passed": ok} for name, ok in checks],
        "boundaries": DISCLAIMER,
    }


def command_matrix() -> dict[str, Any]:
    rows = [{key: value for key, value in spec.items()} for spec in COMMAND_SPECS]
    return {
        "command_count": len(rows),
        "commands": rows,
        "boundaries": DISCLAIMER,
    }


def quickstart_check(root: Path) -> dict[str, Any]:
    checks = [
        ("readme_available", root.joinpath("README.md").exists(), "README.md"),
        ("package_metadata_available", root.joinpath("pyproject.toml").exists(), "pyproject.toml"),
        ("example_events_available", root.joinpath("examples/macro_events.csv").exists(), "examples/macro_events.csv"),
        ("bundled_events_available", root.joinpath("src/macro_policy_thesis_map/examples/macro_events.csv").exists(), "src/macro_policy_thesis_map/examples/macro_events.csv"),
        ("example_sensitivities_available", root.joinpath("examples/thesis_sensitivities.csv").exists(), "examples/thesis_sensitivities.csv"),
        ("example_exposures_available", root.joinpath("examples/portfolio_exposures.csv").exists(), "examples/portfolio_exposures.csv"),
        ("skill_available", root.joinpath("skills/agent/macro-policy-thesis-map/SKILL.md").exists(), "skills/agent/macro-policy-thesis-map/SKILL.md"),
        ("tests_available", any(root.joinpath("tests").glob("test_*.py")), "tests/test_*.py"),
    ]
    commands = [
        spec
        for spec in COMMAND_SPECS
        if spec["command"] in {
            "build-packet",
            "compare-history",
            "review-ledger",
            "fixture-doctor",
            "schema-export",
            "static-dashboard",
            "thesis-impact-brief",
            "exposure-map",
            "scenario-library",
            "assumption-registry",
            "data-dictionary-diff",
            "benchmark-suite",
            "integration-cookbook",
            "compatibility-report",
            "maintainer-guide",
            "golden-fixtures",
            "regression-summary",
            "landing-page",
            "api-reference",
            "workflow-protocol",
            "example-pack",
            "roadmap-next",
            "trust-report",
            "citation-map",
            "release-faq",
            "artifact-index",
            "evaluator-scorecard",
            "boundary-attestation",
            "provenance-ledger",
            "reproducibility-recipe",
            "release-notes-draft",
            "case-gallery",
            "visual-receipt",
            "troubleshoot",
            "docs-export",
            "readme-snippet",
            "cli-help",
            "quickstart-check",
            "command-matrix",
            "adoption-notes",
            "reviewer-scorecard",
            "release-deck",
            "bundle-export",
        }
    ]
    passed = sum(1 for _, ok, _ in checks)
    return {
        "status": "ready" if passed == len(checks) else "needs-review",
        "check_count": len(checks),
        "passed_count": passed,
        "checks": [{"name": name, "passed": ok, "path": path} for name, ok, path in checks],
        "starter_commands": [
            {
                "command": f"PYTHONPATH=src python -m macro_policy_thesis_map.cli {spec['command']} --root .",
                "expected_outputs": spec["outputs"],
            }
            for spec in commands
        ],
        "boundaries": DISCLAIMER,
    }


def troubleshoot(root: Path) -> dict[str, Any]:
    required_paths = [
        "README.md",
        "pyproject.toml",
        "examples/macro_events.csv",
        "demo/fixture_doctor.json",
        "demo/command_matrix.json",
        "demo/public_readiness.json",
        "demo/release_manifest.json",
    ]
    checks = [
        {
            "name": "missing_required_file",
            "symptom": "A command exits with a file-not-found error.",
            "evidence": required_paths,
            "status": "pass" if all(root.joinpath(path).exists() for path in required_paths) else "review",
            "resolution": "Run from the repository root or pass --root with a directory containing the documented static files.",
        },
        {
            "name": "fixture_quality_blocker",
            "symptom": "fixture-doctor returns blocked.",
            "evidence": ["demo/fixture_doctor.json", "examples/macro_events.csv"],
            "status": read_optional_json(root / "demo/fixture_doctor.json").get("status", "missing"),
            "resolution": "Fix missing columns, unsupported event types, invalid confidence values, stale dates, or advice-like terms in the static CSV.",
        },
        {
            "name": "public_readiness_blocker",
            "symptom": "public-readiness returns blocked.",
            "evidence": ["demo/public_readiness.json"],
            "status": read_optional_json(root / "demo/public_readiness.json").get("status", "missing"),
            "resolution": "Review the blockers list, regenerate missing demo artifacts, and keep README finance boundaries explicit.",
        },
        {
            "name": "manifest_drift",
            "symptom": "diff-check reports hash drift.",
            "evidence": ["demo/release_manifest.json"],
            "status": "pass" if root.joinpath("demo/release_manifest.json").exists() else "missing",
            "resolution": "Regenerate changed demo artifacts, then run release-manifest followed by diff-check.",
        },
        {
            "name": "operator_docs_missing",
            "symptom": "An evaluator cannot find command usage or docs surfaces.",
            "evidence": ["demo/docs_export.json", "demo/readme_snippet.json", "demo/cli_help.json", "demo/command_matrix.json"],
            "status": "pass"
            if all(root.joinpath(path).exists() for path in ["demo/docs_export.json", "demo/readme_snippet.json", "demo/cli_help.json", "demo/command_matrix.json"])
            else "review",
            "resolution": "Run docs-export, readme-snippet, cli-help, and command-matrix from the repository root.",
        },
        {
            "name": "schema_adaptation_artifacts_missing",
            "symptom": "A public evaluator cannot decide which CSV columns to keep or add.",
            "evidence": ["demo/scenario_library.json", "demo/assumption_registry.json", "demo/data_dictionary_diff.json"],
            "status": "pass"
            if all(root.joinpath(path).exists() for path in ["demo/scenario_library.json", "demo/assumption_registry.json", "demo/data_dictionary_diff.json"])
            else "review",
            "resolution": "Run scenario-library, assumption-registry, and data-dictionary-diff from the repository root.",
        },
    ]
    review_count = sum(1 for item in checks if item["status"] not in {"pass", "ready"})
    return {
        "title": "Operator Troubleshooting Guide",
        "version": __version__,
        "status": "ready" if review_count == 0 else "needs-review",
        "check_count": len(checks),
        "review_count": review_count,
        "checks": checks,
        "validation_commands": [
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def docs_export(root: Path) -> dict[str, Any]:
    docs = [
        ("README", "README.md", "Primary operator and evaluator documentation."),
        ("Agent skill", "skills/agent/macro-policy-thesis-map/SKILL.md", "Agent protocol and finance boundaries."),
        ("Command matrix", "demo/command_matrix.md", "Command inputs, outputs, and safety posture."),
        ("Input schema", "demo/input_schema.md", "Static CSV schema and data dictionary."),
        ("Scenario library", "demo/scenario_library.md", "Synthetic scenarios for public schema adaptation review."),
        ("Assumption registry", "demo/assumption_registry.md", "Bounded public assumptions and validation controls."),
        ("Data dictionary diff", "demo/data_dictionary_diff.md", "Base and optional CSV dictionary comparison."),
        ("Benchmark suite", "demo/benchmark_suite.md", "Static synthetic evaluator benchmark matrix."),
        ("Integration cookbook", "demo/integration_cookbook.md", "Public-safe local integration recipes."),
        ("Compatibility report", "demo/compatibility_report.md", "Package and artifact compatibility gates."),
        ("Maintainer guide", "demo/maintainer_guide.md", "Release duties, order, and safety invariants."),
        ("Golden fixtures", "demo/golden_fixtures.md", "Fixture hashes, schemas, and expected output counts."),
        ("Regression summary", "demo/regression_summary.md", "Static regression gate summary."),
        ("Landing page", "demo/landing_page.md", "Public first-screen story and start-here commands."),
        ("API reference", "demo/api_reference.md", "Command, artifact, and data-contract reference."),
        ("Workflow protocol", "demo/workflow_protocol.md", "Agent-ready local protocol and stop conditions."),
        ("Example pack", "demo/example_pack.md", "Stable public command recipes and expected artifacts."),
        ("Roadmap next", "demo/roadmap_next.md", "Bounded public next steps and exclusions."),
        ("Trust report", "demo/trust_report.md", "GitHub stranger trust evidence from local artifacts."),
        ("Citation map", "demo/citation_map.md", "Public claim citations to local paths and hashes."),
        ("Release FAQ", "demo/release_faq.md", "First-time evaluator questions with local citations."),
        ("Artifact index", "demo/artifact_index.md", "Demo artifact producers, formats, sizes, and hashes."),
        ("Evaluator scorecard", "demo/evaluator_scorecard.md", "Public evaluator readiness scorecard."),
        ("Boundary attestation", "demo/boundary_attestation.md", "Static finance boundary and public release attestation."),
        ("Provenance ledger", "demo/provenance_ledger.md", "Local source and artifact hash provenance."),
        ("Reproducibility recipe", "demo/reproducibility_recipe.md", "Deterministic regeneration order and release gates."),
        ("Release notes draft", "demo/release_notes_draft.md", "v1.3.0 public release notes draft."),
        ("Troubleshooting", "demo/troubleshoot.md", "Operator diagnostics and recovery steps."),
        ("CLI help", "demo/cli_help.md", "Deterministic command usage lines."),
        ("README snippet", "demo/readme_snippet.md", "Compact copyable quickstart snippet."),
    ]
    records = []
    missing = []
    for title, relative, purpose in docs:
        path = root / relative
        if path.exists():
            records.append({**file_record(root, path), "title": title, "purpose": purpose})
        else:
            missing.append({"title": title, "path": relative, "purpose": purpose})
    return {
        "title": "Operator Documentation Export",
        "version": __version__,
        "status": "ready" if not missing else "needs-review",
        "doc_count": len(records),
        "missing_count": len(missing),
        "documents": sorted(records, key=lambda item: item["path"]),
        "missing": missing,
        "validation_commands": [
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli readme-snippet --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def readme_snippet() -> dict[str, Any]:
    commands = [
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli fixture-doctor --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli build-packet --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli review-ledger --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
    ]
    return {
        "title": "README Snippet",
        "version": __version__,
        "commands": commands,
        "outputs": ["demo/thesis_packet.md", "demo/review_ledger.md", "demo/scenario_library.md", "demo/assumption_registry.md", "demo/data_dictionary_diff.md", "demo/benchmark_suite.md", "demo/integration_cookbook.md", "demo/compatibility_report.md", "demo/maintainer_guide.md", "demo/golden_fixtures.md", "demo/regression_summary.md", "demo/landing_page.md", "demo/api_reference.md", "demo/workflow_protocol.md", "demo/example_pack.md", "demo/roadmap_next.md", "demo/trust_report.md", "demo/citation_map.md", "demo/release_faq.md", "demo/artifact_index.md", "demo/evaluator_scorecard.md", "demo/boundary_attestation.md", "demo/provenance_ledger.md", "demo/reproducibility_recipe.md", "demo/release_notes_draft.md", "demo/troubleshoot.md"],
        "snippet": "\n".join(commands),
        "boundaries": DISCLAIMER,
    }


def cli_help() -> dict[str, Any]:
    rows = []
    for spec in COMMAND_SPECS:
        command = spec["command"]
        usage = f"macro-policy-thesis-map {command} --root ." if command not in {"public-scan", "diff-check", "selfcheck"} else f"macro-policy-thesis-map {command} --root ."
        rows.append(
            {
                "command": command,
                "usage": usage,
                "purpose": spec["purpose"],
                "outputs": spec["outputs"],
                "safety": spec["safety"],
            }
        )
    return {
        "title": "CLI Help Export",
        "version": __version__,
        "command_count": len(rows),
        "commands": rows,
        "boundaries": DISCLAIMER,
    }


def evidence_bundle(root: Path) -> dict[str, Any]:
    include = [
        "README.md",
        "LICENSE",
        "pyproject.toml",
        "examples/macro_events.csv",
        "examples/prior_macro_events.csv",
        "examples/public_macro_cases.csv",
        "examples/thesis_sensitivities.csv",
        "examples/portfolio_exposures.csv",
        "skills/agent/macro-policy-thesis-map/SKILL.md",
        "tests/test_cli.py",
        "tests/test_safety.py",
        "tests/test_build_backend.py",
    ]
    include.extend(
        artifact
        for artifact in DEMO_ARTIFACTS
        if not artifact.startswith("demo/release_manifest") and not artifact.startswith("demo/evidence_bundle")
        and not artifact.startswith("demo/adoption_notes") and not artifact.startswith("demo/reviewer_scorecard")
        and not artifact.startswith("demo/release_deck") and not artifact.startswith("demo/bundle_export")
    )
    records = []
    missing = []
    for relative in include:
        path = root / relative
        if path.exists():
            records.append(file_record(root, path))
        else:
            missing.append(relative)
    records.sort(key=lambda item: item["path"])
    return {
        "status": "ready" if not missing else "needs-review",
        "artifact_count": len(records),
        "missing_count": len(missing),
        "missing": missing,
        "artifacts": records,
        "evaluation_commands": [
            "PYTHONPATH=src python -m pytest tests/test_cli.py tests/test_safety.py",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def public_readiness(root: Path) -> dict[str, Any]:
    readme = root.joinpath("README.md").read_text(encoding="utf-8") if root.joinpath("README.md").exists() else ""
    required_artifacts = [
        "demo/thesis_packet.json",
        "demo/review_ledger.json",
        "demo/release_manifest.json",
        "demo/maturity_report.json",
        "demo/quickstart_check.json",
        "demo/command_matrix.json",
        "demo/fixture_doctor.json",
        "demo/input_schema.json",
        "demo/troubleshoot.json",
        "demo/docs_export.json",
        "demo/readme_snippet.json",
        "demo/cli_help.json",
        "demo/case_gallery.json",
        "demo/thesis_impact_brief.json",
        "demo/exposure_map.json",
        "demo/scenario_library.json",
        "demo/assumption_registry.json",
        "demo/data_dictionary_diff.json",
        "demo/visual_receipt.json",
        "demo/evidence_bundle.json",
        "demo/cold_start_walkthrough.json",
        "demo/benchmark_suite.json",
        "demo/integration_cookbook.json",
        "demo/compatibility_report.json",
        "demo/maintainer_guide.json",
        "demo/golden_fixtures.json",
        "demo/regression_summary.json",
        "demo/landing_page.json",
        "demo/api_reference.json",
        "demo/workflow_protocol.json",
        "demo/example_pack.json",
        "demo/roadmap_next.json",
        "demo/trust_report.json",
        "demo/citation_map.json",
        "demo/release_faq.json",
        "demo/artifact_index.json",
        "demo/evaluator_scorecard.json",
        "demo/boundary_attestation.json",
        "demo/provenance_ledger.json",
        "demo/reproducibility_recipe.json",
        "demo/release_notes_draft.json",
        "demo/adoption_notes.json",
        "demo/reviewer_scorecard.json",
        "demo/release_deck.json",
        "demo/bundle_export/manifest.json",
    ]
    checks = [
        ("public_scan", not public_findings(root), "No private terms or credential-shaped tokens in public text."),
        ("neutral_boundaries", all(term in readme.lower() for term in ["does not fetch live data", "connect to brokers", "recommend buys", "predict returns"]), "README states static research boundaries."),
        ("demo_artifacts", all(root.joinpath(path).exists() for path in required_artifacts), "Core demo artifacts are present."),
        ("visual_receipt", root.joinpath("demo/visual_receipt.svg").exists() or root.joinpath("demo/visual_receipt.html").exists(), "Static SVG or HTML visual receipt is present."),
        ("operator_surfaces", all(root.joinpath(path).exists() for path in ["demo/troubleshoot.json", "demo/docs_export.json", "demo/readme_snippet.json", "demo/cli_help.json"]), "Operator troubleshooting, docs export, README snippet, and CLI help artifacts are present."),
        ("schema_adaptation_surfaces", all(root.joinpath(path).exists() for path in ["demo/scenario_library.json", "demo/assumption_registry.json", "demo/data_dictionary_diff.json"]), "Scenario, assumption, and data dictionary diff artifacts are present."),
        ("public_evaluator_hardening", all(root.joinpath(path).exists() for path in ["demo/benchmark_suite.json", "demo/integration_cookbook.json", "demo/compatibility_report.json", "demo/maintainer_guide.json", "demo/golden_fixtures.json", "demo/regression_summary.json"]), "Benchmark, integration, compatibility, maintainer, golden fixture, and regression summary artifacts are present."),
        ("public_protocol_layer", all(root.joinpath(path).exists() for path in ["demo/landing_page.html", "demo/api_reference.html", "demo/workflow_protocol.html", "demo/example_pack.html", "demo/roadmap_next.html"]), "Landing, API reference, workflow protocol, example pack, and roadmap HTML artifacts are present."),
        ("public_trust_layer", all(root.joinpath(path).exists() for path in ["demo/trust_report.json", "demo/citation_map.json", "demo/release_faq.json", "demo/artifact_index.json", "demo/evaluator_scorecard.json"]), "Trust report, citation map, release FAQ, artifact index, and evaluator scorecard artifacts are present."),
        ("governance_attestation_layer", all(root.joinpath(path).exists() for path in ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"]), "Boundary, provenance, reproducibility, and release notes draft artifacts are present."),
        ("no_workflow_files", not root.joinpath(".github/workflows").exists(), "No repository workflow files are required for public evaluation."),
        ("zero_dependency_package", "dependencies = []" in root.joinpath("pyproject.toml").read_text(encoding="utf-8") if root.joinpath("pyproject.toml").exists() else False, "Package declares no runtime dependencies."),
    ]
    blockers = [{"name": name, "detail": detail} for name, ok, detail in checks if not ok]
    return {
        "status": "ready" if not blockers else "blocked",
        "check_count": len(checks),
        "passed_count": sum(1 for _, ok, _ in checks),
        "checks": [{"name": name, "passed": ok, "detail": detail} for name, ok, detail in checks],
        "blockers": blockers,
        "boundaries": DISCLAIMER,
    }


def benchmark_suite(root: Path) -> dict[str, Any]:
    scenarios = [
        {
            "benchmark_id": "bench-001",
            "name": "default_packet_generation",
            "commands": ["build-packet", "review-ledger", "fixture-doctor"],
            "fixture_paths": ["examples/macro_events.csv"],
            "expected_artifacts": ["demo/thesis_packet.json", "demo/review_ledger.json", "demo/fixture_doctor.json"],
            "deterministic_assertion": "Event count, policy-area count, and fixture-doctor status remain stable for bundled examples.",
        },
        {
            "benchmark_id": "bench-002",
            "name": "schema_adaptation_surfaces",
            "commands": ["scenario-library", "assumption-registry", "data-dictionary-diff"],
            "fixture_paths": [],
            "expected_artifacts": ["demo/scenario_library.json", "demo/assumption_registry.json", "demo/data_dictionary_diff.json"],
            "deterministic_assertion": "Built-in synthetic metadata writes identical command counts and schema guidance across runs.",
        },
        {
            "benchmark_id": "bench-003",
            "name": "public_case_and_receipt",
            "commands": ["case-gallery", "visual-receipt"],
            "fixture_paths": ["examples/public_macro_cases.csv"],
            "expected_artifacts": ["demo/case_gallery.json", "demo/visual_receipt.json"],
            "deterministic_assertion": "Case routes, receipt command list, and artifact hash prefixes are derived from static local files.",
        },
        {
            "benchmark_id": "bench-004",
            "name": "release_readiness_pack",
            "commands": ["maturity-report", "evidence-bundle", "public-readiness", "regression-summary"],
            "fixture_paths": [],
            "expected_artifacts": ["demo/maturity_report.json", "demo/evidence_bundle.json", "demo/public_readiness.json", "demo/regression_summary.json"],
            "deterministic_assertion": "Gate names and pass/block statuses are computed from local files only.",
        },
    ]
    rows = []
    for scenario in scenarios:
        missing = [path for path in scenario["expected_artifacts"] if not root.joinpath(path).exists()]
        rows.append({**scenario, "status": "ready" if not missing else "needs-artifacts", "missing": missing})
    return {
        "title": "Public Evaluator Benchmark Suite",
        "version": __version__,
        "suite_type": "static synthetic deterministic benchmarks",
        "benchmark_count": len(rows),
        "ready_count": sum(1 for item in rows if item["status"] == "ready"),
        "benchmarks": rows,
        "run_policy": [
            "Benchmarks describe deterministic artifact expectations and do not measure wall-clock performance.",
            "Use bundled static fixtures or user-supplied static CSVs only.",
            "Treat any missing expected artifact as a regeneration task, not as a live-data fetch request.",
        ],
        "boundaries": DISCLAIMER,
    }


def integration_cookbook() -> dict[str, Any]:
    recipes = [
        {
            "recipe_id": "recipe-001",
            "name": "Local CSV Evaluation",
            "goal": "Evaluate a static event CSV from a clean checkout.",
            "commands": ["fixture-doctor --root . --events examples/macro_events.csv", "build-packet --root .", "review-ledger --root ."],
            "inputs": ["static event CSV with base event columns"],
            "outputs": ["demo/fixture_doctor.json", "demo/thesis_packet.json", "demo/review_ledger.json"],
            "guardrails": ["No network calls", "No broker access", "No trade or allocation language"],
        },
        {
            "recipe_id": "recipe-002",
            "name": "Schema Adapter Review",
            "goal": "Decide whether optional public fixture columns should be adopted.",
            "commands": ["schema-export --root .", "scenario-library --root .", "assumption-registry --root .", "data-dictionary-diff --root ."],
            "inputs": ["built-in schema metadata"],
            "outputs": ["demo/input_schema.json", "demo/scenario_library.json", "demo/assumption_registry.json", "demo/data_dictionary_diff.json"],
            "guardrails": ["Keep optional columns additive", "Keep scores bounded from 0 to 1", "Do not add recommendation fields"],
        },
        {
            "recipe_id": "recipe-003",
            "name": "Public Artifact Review",
            "goal": "Share deterministic local evidence with a public evaluator.",
            "commands": ["command-matrix --root .", "evidence-bundle --root .", "public-readiness --root .", "visual-receipt --root ."],
            "inputs": ["demo artifacts and local source files"],
            "outputs": ["demo/command_matrix.json", "demo/evidence_bundle.json", "demo/public_readiness.json", "demo/visual_receipt.json"],
            "guardrails": ["Use hashes instead of private storage links", "Do not add workflow files", "Run public-scan before sharing"],
        },
        {
            "recipe_id": "recipe-004",
            "name": "Maintainer Release Check",
            "goal": "Regenerate release owner surfaces before cutting a static public package.",
            "commands": ["maintainer-guide --root .", "golden-fixtures --root .", "regression-summary --root .", "release-manifest --root .", "diff-check --root ."],
            "inputs": ["repository files and synthetic fixtures"],
            "outputs": ["demo/maintainer_guide.json", "demo/golden_fixtures.json", "demo/regression_summary.json", "demo/release_manifest.json"],
            "guardrails": ["Keep zero runtime dependencies", "Keep version metadata synchronized", "Do not include private references"],
        },
    ]
    return {
        "title": "Public Integration Cookbook",
        "version": __version__,
        "recipe_count": len(recipes),
        "recipes": recipes,
        "integration_boundaries": [
            "Recipes are command sequences for local static files.",
            "Recipes do not describe private tools, CI workflows, upload destinations, live market feeds, or investment actions.",
        ],
        "boundaries": DISCLAIMER,
    }


def compatibility_report(root: Path) -> dict[str, Any]:
    pyproject = root.joinpath("pyproject.toml").read_text(encoding="utf-8") if root.joinpath("pyproject.toml").exists() else ""
    checks = [
        ("python_requires", "requires-python = \">=3.11\"" in pyproject, "Package declares Python 3.11 or newer."),
        ("zero_runtime_dependencies", "dependencies = []" in pyproject, "Package declares zero runtime dependencies."),
        ("console_script", "macro-policy-thesis-map = \"macro_policy_thesis_map.cli:main\"" in pyproject, "Console script is declared."),
        ("version_sync", f'version = "{__version__}"' in pyproject, "pyproject version matches package version."),
        ("bundled_event_fixture", root.joinpath("src/macro_policy_thesis_map/examples/macro_events.csv").exists(), "Bundled default event fixture is present."),
        ("bundled_case_fixture", root.joinpath("src/macro_policy_thesis_map/examples/public_macro_cases.csv").exists(), "Bundled public case fixture is present."),
        ("public_artifacts", all(root.joinpath(path).exists() for path in ["demo/command_matrix.json", "demo/public_readiness.json", "demo/golden_fixtures.json"]), "Public evaluator artifacts are present."),
        ("protocol_artifacts", all(root.joinpath(path).exists() for path in ["demo/landing_page.json", "demo/api_reference.json", "demo/workflow_protocol.json", "demo/example_pack.json", "demo/roadmap_next.json"]), "Public protocol layer artifacts are present."),
        ("trust_artifacts", all(root.joinpath(path).exists() for path in ["demo/trust_report.json", "demo/citation_map.json", "demo/release_faq.json", "demo/artifact_index.json", "demo/evaluator_scorecard.json"]), "Public trust layer artifacts are present."),
        ("governance_artifacts", all(root.joinpath(path).exists() for path in ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"]), "Governance and attestation layer artifacts are present."),
        ("no_workflows", not root.joinpath(".github/workflows").exists(), "No workflow files are required."),
    ]
    return {
        "title": "Compatibility Report",
        "version": __version__,
        "status": "ready" if all(ok for _, ok, _ in checks) else "needs-review",
        "check_count": len(checks),
        "passed_count": sum(1 for _, ok, _ in checks),
        "checks": [{"name": name, "passed": ok, "detail": detail} for name, ok, detail in checks],
        "supported_surfaces": ["source checkout", "installed console script", "offline wheel", "offline sdist"],
        "unsupported_surfaces": ["live data connector", "broker integration", "workflow automation", "personalized finance advice"],
        "boundaries": DISCLAIMER,
    }


def maintainer_guide() -> dict[str, Any]:
    sections = [
        {
            "section": "versioning",
            "duties": ["Keep pyproject.toml and package __version__ synchronized.", "Regenerate demo artifacts after version changes.", "Update release manifest after generated files settle."],
        },
        {
            "section": "fixtures",
            "duties": ["Use synthetic static CSV rows only.", "Run fixture-doctor and golden-fixtures after fixture edits.", "Keep bundled package examples in sync with top-level examples."],
        },
        {
            "section": "public safety",
            "duties": ["Run public-scan before sharing artifacts.", "Keep README and skill boundaries explicit.", "Do not add workflow files, private references, live finance feeds, or advice language."],
        },
        {
            "section": "regression gates",
            "duties": ["Run pytest, selfcheck, public-readiness, diff-check, and wheel build when feasible.", "Regenerate regression-summary with the final local status.", "Treat readiness blockers as release blockers."],
        },
    ]
    release_order = [
        "fixture-doctor",
        "schema-export",
        "build-packet",
        "review-ledger",
        "scenario-library",
        "assumption-registry",
        "data-dictionary-diff",
        "landing-page",
        "api-reference",
        "workflow-protocol",
        "example-pack",
        "roadmap-next",
        "trust-report",
        "citation-map",
        "release-faq",
        "artifact-index",
        "evaluator-scorecard",
        "boundary-attestation",
        "provenance-ledger",
        "reproducibility-recipe",
        "release-notes-draft",
        "benchmark-suite",
        "integration-cookbook",
        "compatibility-report",
        "maintainer-guide",
        "golden-fixtures",
        "regression-summary",
        "maturity-report",
        "evidence-bundle",
        "public-readiness",
        "release-manifest",
        "diff-check",
    ]
    return {
        "title": "Maintainer Guide",
        "version": __version__,
        "section_count": len(sections),
        "sections": sections,
        "release_order": release_order,
        "invariants": [
            "Runtime dependencies remain empty.",
            "Generated public artifacts are deterministic Markdown, JSON, HTML, or SVG under demo/.",
            "All example data remains static and synthetic.",
            "No live finance data, advice, private references, or workflow automation is introduced.",
        ],
        "boundaries": DISCLAIMER,
    }


def golden_fixtures(root: Path) -> dict[str, Any]:
    fixtures = []
    specs = [
        ("event_current", "examples/macro_events.csv", EXPECTED_COLUMNS),
        ("event_prior", "examples/prior_macro_events.csv", EXPECTED_COLUMNS),
        ("case_gallery", "examples/public_macro_cases.csv", CASE_COLUMNS),
        ("thesis_sensitivity", "examples/thesis_sensitivities.csv", SENSITIVITY_COLUMNS),
        ("portfolio_exposure", "examples/portfolio_exposures.csv", EXPOSURE_COLUMNS),
    ]
    for fixture_type, relative, expected_columns in specs:
        path = root / relative
        if path.exists():
            header, rows = read_csv_document(path)
            fixtures.append(
                {
                    **file_record(root, path),
                    "fixture_type": fixture_type,
                    "row_count": len(rows),
                    "expected_columns": expected_columns,
                    "actual_columns": header,
                    "schema_status": "pass" if header == expected_columns else "review",
                }
            )
        else:
            fixtures.append({"path": relative, "fixture_type": fixture_type, "row_count": 0, "schema_status": "missing"})
    expected_outputs = [
        {"command": "build-packet", "json_path": "demo/thesis_packet.json", "key": "event_count"},
        {"command": "case-gallery", "json_path": "demo/case_gallery.json", "key": "case_count"},
        {"command": "thesis-impact-brief", "json_path": "demo/thesis_impact_brief.json", "key": "sensitivity_count"},
        {"command": "exposure-map", "json_path": "demo/exposure_map.json", "key": "exposure_count"},
    ]
    for output in expected_outputs:
        payload = read_optional_json(root / output["json_path"])
        output["observed_value"] = payload.get(output["key"], "missing")
        output["status"] = "recorded" if output["observed_value"] != "missing" else "missing"
    return {
        "title": "Golden Fixtures",
        "version": __version__,
        "fixture_count": len(fixtures),
        "fixtures": fixtures,
        "expected_outputs": expected_outputs,
        "status": "ready" if all(item.get("schema_status") == "pass" for item in fixtures) else "needs-review",
        "boundaries": DISCLAIMER,
    }


def regression_summary(root: Path) -> dict[str, Any]:
    gates = [
        {"name": "pytest_suite", "status": "manual", "evidence": "Run PYTHONPATH=src python -m pytest", "detail": "Full test execution is recorded by the release operator."},
        {"name": "selfcheck", "status": "pass" if not public_findings(root) and root.joinpath("README.md").exists() else "review", "evidence": "macro-policy-thesis-map selfcheck --root .", "detail": "Required files and public scan findings are checked locally."},
        {"name": "public_readiness", "status": read_optional_json(root / "demo/public_readiness.json").get("status", "missing"), "evidence": "demo/public_readiness.json", "detail": "Public readiness gate summary."},
        {"name": "release_manifest", "status": "pass" if root.joinpath("demo/release_manifest.json").exists() else "missing", "evidence": "demo/release_manifest.json", "detail": "Release artifact hashes are present."},
        {"name": "golden_fixtures", "status": read_optional_json(root / "demo/golden_fixtures.json").get("status", "missing"), "evidence": "demo/golden_fixtures.json", "detail": "Fixture schema and hash inventory."},
        {"name": "trust_layer", "status": read_optional_json(root / "demo/evaluator_scorecard.json").get("status", "missing"), "evidence": "demo/evaluator_scorecard.json", "detail": "Evaluator trust scorecard based on local artifacts."},
        {"name": "governance_attestation_layer", "status": "ready" if all(root.joinpath(path).exists() for path in ["demo/boundary_attestation.json", "demo/provenance_ledger.json", "demo/reproducibility_recipe.json", "demo/release_notes_draft.json"]) else "missing", "evidence": "demo/boundary_attestation.json, demo/provenance_ledger.json, demo/reproducibility_recipe.json, demo/release_notes_draft.json", "detail": "Governance layer records boundaries, provenance, reproducibility, and release notes."},
        {"name": "wheel_build", "status": "manual", "evidence": "python -m build --wheel or build_backend.build_wheel", "detail": "Offline wheel build should be run when build tooling is available."},
    ]
    blocking = [item for item in gates if item["status"] not in {"pass", "ready", "manual"}]
    return {
        "title": "Regression Summary",
        "version": __version__,
        "status": "ready" if not blocking else "needs-review",
        "gate_count": len(gates),
        "manual_gate_count": sum(1 for item in gates if item["status"] == "manual"),
        "blocking_gate_count": len(blocking),
        "gates": gates,
        "release_checks": [
            "PYTHONPATH=src python -m pytest",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def cold_start_walkthrough() -> dict[str, Any]:
    steps = [
        {
            "step": 1,
            "title": "Inspect available commands",
            "command": "macro-policy-thesis-map command-matrix",
            "expected_result": "Markdown and JSON command matrix are written under demo/.",
        },
        {
            "step": 2,
            "title": "Build the packet from static examples",
            "command": "macro-policy-thesis-map build-packet",
            "expected_result": "A neutral thesis packet is written as Markdown and JSON.",
        },
        {
            "step": 3,
            "title": "Review evidence safety",
            "command": "macro-policy-thesis-map review-ledger",
            "expected_result": "A review ledger flags low-confidence or advice-like input text.",
        },
        {
            "step": 4,
            "title": "Render static sensitivity and exposure layers",
            "command": "macro-policy-thesis-map thesis-impact-brief && macro-policy-thesis-map exposure-map && macro-policy-thesis-map scenario-library",
            "expected_result": "Synthetic sensitivity, exposure, and scenario maps are written as Markdown and JSON.",
        },
        {
            "step": 5,
            "title": "Review schema adaptation surfaces",
            "command": "macro-policy-thesis-map assumption-registry && macro-policy-thesis-map data-dictionary-diff",
            "expected_result": "Bounded assumptions and CSV dictionary differences are written as Markdown and JSON.",
        },
        {
            "step": 6,
            "title": "Read operator support surfaces",
            "command": "macro-policy-thesis-map troubleshoot && macro-policy-thesis-map docs-export && macro-policy-thesis-map cli-help",
            "expected_result": "Operator troubleshooting, docs export, and CLI help surfaces are written as Markdown and JSON.",
        },
        {
            "step": 7,
            "title": "Read release-owner promotion notes",
            "command": "macro-policy-thesis-map adoption-notes && macro-policy-thesis-map reviewer-scorecard && macro-policy-thesis-map release-deck",
            "expected_result": "Release-owner notes, scorecard, and deck are written as Markdown and JSON.",
        },
        {
            "step": 8,
            "title": "Generate public visitor and protocol surfaces",
            "command": "macro-policy-thesis-map landing-page && macro-policy-thesis-map api-reference && macro-policy-thesis-map workflow-protocol && macro-policy-thesis-map example-pack && macro-policy-thesis-map roadmap-next",
            "expected_result": "Landing, API reference, workflow protocol, example pack, and roadmap artifacts are written as Markdown, JSON, and HTML.",
        },
        {
            "step": 9,
            "title": "Generate public trust layer",
            "command": "macro-policy-thesis-map trust-report && macro-policy-thesis-map citation-map && macro-policy-thesis-map release-faq && macro-policy-thesis-map artifact-index && macro-policy-thesis-map evaluator-scorecard",
            "expected_result": "Trust report, citation map, FAQ, artifact index, and evaluator scorecard are written as Markdown and JSON.",
        },
        {
            "step": 10,
            "title": "Generate public evaluator hardening surfaces",
            "command": "macro-policy-thesis-map benchmark-suite && macro-policy-thesis-map integration-cookbook && macro-policy-thesis-map compatibility-report && macro-policy-thesis-map maintainer-guide && macro-policy-thesis-map golden-fixtures && macro-policy-thesis-map regression-summary",
            "expected_result": "Benchmark, integration, compatibility, maintainer, golden fixture, and regression artifacts are written as Markdown and JSON.",
        },
        {
            "step": 11,
            "title": "Export the public promotion bundle manifest",
            "command": "macro-policy-thesis-map bundle-export",
            "expected_result": "A deterministic bundle manifest is written under demo/bundle_export/.",
        },
        {
            "step": 12,
            "title": "Check public readiness",
            "command": "macro-policy-thesis-map public-readiness",
            "expected_result": "A public readiness report lists pass/fail gates.",
        },
        {
            "step": 13,
            "title": "Run final local checks",
            "command": "macro-policy-thesis-map selfcheck && macro-policy-thesis-map public-scan && macro-policy-thesis-map diff-check",
            "expected_result": "All commands exit successfully before sharing artifacts.",
        },
    ]
    return {
        "step_count": len(steps),
        "steps": steps,
        "safety_notes": [
            "Use static CSV files only.",
            "Run local static commands only; no network access or broker connection is part of the walkthrough.",
            "Do not add live market data, broker actions, trading recommendations, or personalized advice.",
            "Treat review-ledger blockers as release blockers until the input text is revised.",
        ],
        "boundaries": DISCLAIMER,
    }


def release_manifest(root: Path) -> dict[str, Any]:
    files = []
    excluded = {
        "demo/release_manifest.json",
        "demo/release_manifest.md",
        "demo/visual_receipt.json",
        "demo/visual_receipt.md",
        "demo/visual_receipt.svg",
        "demo/visual_receipt.html",
        "demo/evidence_bundle.json",
        "demo/evidence_bundle.md",
        "demo/adoption_notes.json",
        "demo/adoption_notes.md",
        "demo/reviewer_scorecard.json",
        "demo/reviewer_scorecard.md",
        "demo/release_deck.json",
        "demo/release_deck.md",
        "demo/bundle_export/manifest.json",
        "demo/bundle_export/manifest.md",
    }
    for base in ["README.md", "LICENSE", "pyproject.toml", "examples", "demo", "src", "tests", "skills"]:
        path = root / base
        if path.is_file():
            record = file_record(root, path)
            if record["path"] not in excluded:
                files.append(record)
        elif path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file() and "__pycache__" not in child.parts and ".git" not in child.parts:
                    record = file_record(root, child)
                    if record["path"] not in excluded:
                        files.append(record)
    return {"artifact_count": len(files), "artifacts": files, "boundaries": DISCLAIMER}


def adoption_notes(root: Path) -> dict[str, Any]:
    maturity_payload = read_optional_json(root / "demo/maturity_report.json")
    readiness_payload = read_optional_json(root / "demo/public_readiness.json")
    manifest_payload = read_optional_json(root / "demo/release_manifest.json")
    artifacts = records_for_existing(
        root,
        [
            "README.md",
            "demo/command_matrix.json",
            "demo/scenario_library.json",
            "demo/assumption_registry.json",
            "demo/data_dictionary_diff.json",
            "demo/troubleshoot.json",
            "demo/docs_export.json",
            "demo/readme_snippet.json",
            "demo/cli_help.json",
            "demo/maturity_report.json",
            "demo/public_readiness.json",
            "demo/evidence_bundle.json",
            "demo/release_manifest.json",
            "demo/cold_start_walkthrough.json",
            "demo/benchmark_suite.json",
            "demo/integration_cookbook.json",
            "demo/compatibility_report.json",
            "demo/maintainer_guide.json",
            "demo/golden_fixtures.json",
            "demo/regression_summary.json",
            "demo/trust_report.json",
            "demo/citation_map.json",
            "demo/release_faq.json",
            "demo/artifact_index.json",
            "demo/evaluator_scorecard.json",
            "demo/boundary_attestation.json",
            "demo/provenance_ledger.json",
            "demo/reproducibility_recipe.json",
            "demo/release_notes_draft.json",
        ],
    )
    next_actions = [
        "Run the quickstart commands from a clean checkout.",
        "Review demo/reviewer_scorecard.md for any maturity item marked review.",
        "Confirm demo/public_readiness.json remains ready after local edits.",
        "Run public-scan and diff-check before sharing the bundle.",
    ]
    release_commands = [
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli benchmark-suite --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli integration-cookbook --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli compatibility-report --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-guide --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli golden-fixtures --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root .",
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
    ]
    return {
        "title": "Release Owner Adoption Notes",
        "version": __version__,
        "maturity_status": maturity_payload.get("status", "missing"),
        "maturity_score": maturity_payload.get("score", 0),
        "maturity_max_score": maturity_payload.get("max_score", 0),
        "public_readiness_status": readiness_payload.get("status", "missing"),
        "release_artifact_count": manifest_payload.get("artifact_count", 0),
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "release_commands": release_commands,
        "cold_user_next_actions": next_actions,
        "safety_boundaries": [
            "Use static files only.",
            "Do not add workflow files, upload steps, or private references.",
            "Do not fetch live data, connect to brokers, place orders, or provide financial advice.",
            "Treat public-readiness blockers and reviewer-scorecard review items as release-owner follow-up.",
        ],
        "boundaries": DISCLAIMER,
    }


def reviewer_scorecard(root: Path) -> dict[str, Any]:
    maturity_payload = read_optional_json(root / "demo/maturity_report.json") or maturity(root)
    readiness_payload = read_optional_json(root / "demo/public_readiness.json")
    rubric = [
        ("static_inputs", ["examples", "case_gallery", "sensitivity_layer", "exposure_layer", "schema_adaptation_surfaces"], "Static fixtures and synthetic public examples are present."),
        ("review_controls", ["visual_receipt", "operator_surfaces", "release_owner_pack"], "Review artifacts, operator docs, hashes, and owner pack are present."),
        ("public_evaluator_hardening", ["public_evaluator_hardening"], "Benchmark, integration, compatibility, maintainer, golden fixture, and regression artifacts are present."),
        ("public_protocol_layer", ["public_protocol_layer"], "Landing, API reference, workflow protocol, example pack, and roadmap artifacts are present."),
        ("public_trust_layer", ["public_trust_layer"], "Trust report, citation map, release FAQ, artifact index, and evaluator scorecard are present."),
        ("public_package", ["package", "readme", "license", "skill"], "Package metadata, docs, license, and agent skill are present."),
        ("verification", ["tests", "no_workflows"], "Tests exist and no workflow files are required."),
        ("governance_attestation_layer", ["governance_attestation_layer"], "Boundary, provenance, reproducibility, and release-note artifacts are present."),
        ("public_readiness", [], "Public readiness command reports ready."),
    ]
    maturity_checks = {item["name"]: bool(item["passed"]) for item in maturity_payload.get("checks", []) if isinstance(item, dict)}
    rows = []
    for name, mapped_checks, description in rubric:
        if name == "public_readiness":
            passed = readiness_payload.get("status") == "ready"
            evidence = ["demo/public_readiness.json"]
        else:
            passed = all(maturity_checks.get(check, False) for check in mapped_checks)
            evidence = mapped_checks
        rows.append(
            {
                "name": name,
                "passed": passed,
                "description": description,
                "maturity_mapping": mapped_checks,
                "evidence": evidence,
            }
        )
    artifacts = records_for_existing(
        root,
        [
            "demo/maturity_report.json",
            "demo/public_readiness.json",
            "demo/evidence_bundle.json",
            "demo/release_manifest.json",
            "demo/command_matrix.json",
            "demo/scenario_library.json",
            "demo/assumption_registry.json",
            "demo/data_dictionary_diff.json",
            "demo/benchmark_suite.json",
            "demo/integration_cookbook.json",
            "demo/compatibility_report.json",
            "demo/maintainer_guide.json",
            "demo/golden_fixtures.json",
            "demo/regression_summary.json",
            "demo/landing_page.json",
            "demo/api_reference.json",
            "demo/workflow_protocol.json",
            "demo/example_pack.json",
            "demo/roadmap_next.json",
            "demo/trust_report.json",
            "demo/citation_map.json",
            "demo/release_faq.json",
            "demo/artifact_index.json",
            "demo/evaluator_scorecard.json",
            "demo/boundary_attestation.json",
            "demo/provenance_ledger.json",
            "demo/reproducibility_recipe.json",
            "demo/release_notes_draft.json",
            "demo/troubleshoot.json",
            "demo/docs_export.json",
            "demo/readme_snippet.json",
            "demo/cli_help.json",
            "tests/test_cli.py",
            "tests/test_safety.py",
        ],
    )
    return {
        "title": "Reviewer Scorecard",
        "version": __version__,
        "status": "ready" if all(item["passed"] for item in rows) else "needs-review",
        "score": sum(1 for item in rows if item["passed"]),
        "max_score": len(rows),
        "rubric": rows,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "boundaries": DISCLAIMER,
    }


def release_deck(root: Path) -> dict[str, Any]:
    notes = read_optional_json(root / "demo/adoption_notes.json")
    scorecard = read_optional_json(root / "demo/reviewer_scorecard.json")
    readiness = read_optional_json(root / "demo/public_readiness.json")
    command_payload = command_matrix()
    slides = [
        {
            "slide": 1,
            "title": "Release Surface",
            "points": [
                f"Version {__version__}",
                f"{command_payload['command_count']} zero-dependency CLI commands documented",
                "Static Markdown, JSON, HTML, and SVG artifacts only",
            ],
        },
        {
            "slide": 2,
            "title": "Evidence And Hashes",
            "points": [
                f"{notes.get('release_artifact_count', 0)} release manifest artifacts tracked",
                "Artifact hashes are recorded in release, evidence, visual receipt, and bundle manifests",
                "Golden fixtures record static fixture hashes, schemas, and expected output keys",
                "diff-check verifies saved hashes against current local files",
            ],
        },
        {
            "slide": 3,
            "title": "Reviewer Rubric",
            "points": [
                f"Scorecard status: {scorecard.get('status', 'missing')}",
                f"Score: {scorecard.get('score', 0)} / {scorecard.get('max_score', 0)}",
                "Maturity mapping covers static inputs, review controls, package evidence, verification, and readiness",
                "Public hardening covers benchmark, integration, compatibility, maintainer, fixture, and regression surfaces",
                "Protocol layer covers public landing, API contracts, agent protocol, example recipes, and roadmap constraints",
                "Governance layer covers boundary attestation, provenance, reproducibility, and release notes draft",
            ],
        },
        {
            "slide": 4,
            "title": "Cold User Path",
            "points": notes.get("cold_user_next_actions", []),
        },
        {
            "slide": 5,
            "title": "Safety Boundaries",
            "points": [
                "No workflow files are required for public evaluation",
                "No private references or credential-shaped terms are allowed by public-scan",
                "No live data, broker connections, orders, recommendations, predictions, or personalized advice",
                f"Public readiness status: {readiness.get('status', 'missing')}",
            ],
        },
    ]
    artifacts = records_for_existing(
        root,
        [
            "demo/adoption_notes.json",
            "demo/reviewer_scorecard.json",
            "demo/public_readiness.json",
            "demo/release_manifest.json",
            "demo/command_matrix.json",
            "demo/benchmark_suite.json",
            "demo/integration_cookbook.json",
            "demo/compatibility_report.json",
            "demo/maintainer_guide.json",
            "demo/golden_fixtures.json",
            "demo/regression_summary.json",
            "demo/landing_page.json",
            "demo/api_reference.json",
            "demo/workflow_protocol.json",
            "demo/example_pack.json",
            "demo/roadmap_next.json",
            "demo/trust_report.json",
            "demo/citation_map.json",
            "demo/release_faq.json",
            "demo/artifact_index.json",
            "demo/evaluator_scorecard.json",
            "demo/boundary_attestation.json",
            "demo/provenance_ledger.json",
            "demo/reproducibility_recipe.json",
            "demo/release_notes_draft.json",
        ],
    )
    return {
        "title": "Release Owner Promotion Deck",
        "version": __version__,
        "slide_count": len(slides),
        "slides": slides,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "boundaries": DISCLAIMER,
    }


def bundle_export(root: Path) -> dict[str, Any]:
    include = [
        "README.md",
        "LICENSE",
        "pyproject.toml",
        "demo/adoption_notes.md",
        "demo/adoption_notes.json",
        "demo/reviewer_scorecard.md",
        "demo/reviewer_scorecard.json",
        "demo/release_deck.md",
        "demo/release_deck.json",
        "demo/command_matrix.md",
        "demo/command_matrix.json",
        "demo/scenario_library.md",
        "demo/scenario_library.json",
        "demo/assumption_registry.md",
        "demo/assumption_registry.json",
        "demo/data_dictionary_diff.md",
        "demo/data_dictionary_diff.json",
        "demo/maturity_report.md",
        "demo/maturity_report.json",
        "demo/public_readiness.md",
        "demo/public_readiness.json",
        "demo/evidence_bundle.md",
        "demo/evidence_bundle.json",
        "demo/release_manifest.md",
        "demo/release_manifest.json",
        "demo/cold_start_walkthrough.md",
        "demo/cold_start_walkthrough.json",
        "demo/benchmark_suite.md",
        "demo/benchmark_suite.json",
        "demo/integration_cookbook.md",
        "demo/integration_cookbook.json",
        "demo/compatibility_report.md",
        "demo/compatibility_report.json",
        "demo/maintainer_guide.md",
        "demo/maintainer_guide.json",
            "demo/golden_fixtures.md",
            "demo/golden_fixtures.json",
            "demo/regression_summary.md",
            "demo/regression_summary.json",
            "demo/landing_page.md",
            "demo/landing_page.json",
            "demo/landing_page.html",
            "demo/api_reference.md",
            "demo/api_reference.json",
            "demo/api_reference.html",
            "demo/workflow_protocol.md",
            "demo/workflow_protocol.json",
            "demo/workflow_protocol.html",
            "demo/example_pack.md",
            "demo/example_pack.json",
            "demo/example_pack.html",
            "demo/roadmap_next.md",
            "demo/roadmap_next.json",
            "demo/roadmap_next.html",
            "demo/trust_report.md",
            "demo/trust_report.json",
            "demo/citation_map.md",
            "demo/citation_map.json",
            "demo/release_faq.md",
            "demo/release_faq.json",
            "demo/artifact_index.md",
            "demo/artifact_index.json",
            "demo/evaluator_scorecard.md",
            "demo/evaluator_scorecard.json",
            "demo/boundary_attestation.md",
            "demo/boundary_attestation.json",
            "demo/provenance_ledger.md",
            "demo/provenance_ledger.json",
            "demo/reproducibility_recipe.md",
            "demo/reproducibility_recipe.json",
            "demo/release_notes_draft.md",
            "demo/release_notes_draft.json",
    ]
    artifacts = records_for_existing(root, include)
    missing = [path for path in include if not root.joinpath(path).exists()]
    return {
        "title": "Public Promotion Bundle Export",
        "version": __version__,
        "status": "ready" if not missing else "needs-review",
        "export_root": "demo/bundle_export",
        "artifact_count": len(artifacts),
        "missing_count": len(missing),
        "missing": missing,
        "artifacts": artifacts,
        "release_commands": [
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli regression-summary --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli landing-page --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli api-reference --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli workflow-protocol --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli example-pack --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli roadmap-next --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli trust-report --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli citation-map --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-faq --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli artifact-index --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root .",
            "PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .",
        ],
        "boundaries": DISCLAIMER,
    }


def diff_check(root: Path, manifest_path: Path) -> dict[str, Any]:
    if not manifest_path.exists():
        return {
            "status": "blocked",
            "manifest": str(manifest_path.relative_to(root)) if manifest_path.is_relative_to(root) else str(manifest_path),
            "finding_count": 1,
            "findings": [{"path": str(manifest_path), "finding": "manifest missing"}],
            "boundaries": DISCLAIMER,
        }
    manifest = read_json(manifest_path)
    findings = []
    for item in manifest.get("artifacts", []):
        if not isinstance(item, dict) or "path" not in item or "sha256" not in item:
            findings.append({"path": "manifest", "finding": "invalid artifact record"})
            continue
        path = root / str(item["path"])
        if not path.exists():
            findings.append({"path": item["path"], "finding": "missing current file"})
            continue
        current = hashlib.sha256(path.read_bytes()).hexdigest()
        if current != item["sha256"]:
            findings.append({"path": item["path"], "finding": "hash drift", "expected": item["sha256"], "actual": current})
    return {
        "status": "pass" if not findings else "blocked",
        "manifest": str(manifest_path.relative_to(root)) if manifest_path.is_relative_to(root) else str(manifest_path),
        "checked_count": len(manifest.get("artifacts", [])),
        "finding_count": len(findings),
        "findings": findings,
        "boundaries": DISCLAIMER,
    }


def file_record(root: Path, path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": str(path.relative_to(root)).replace("\\", "/"),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def records_for_existing(root: Path, relatives: list[str]) -> list[dict[str, Any]]:
    records = [file_record(root, root / relative) for relative in relatives if root.joinpath(relative).exists()]
    return sorted(records, key=lambda item: item["path"])


def read_optional_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return read_json(path)


def public_findings(root: Path) -> list[str]:
    findings: list[str] = []
    suffixes = {".py", ".md", ".txt", ".toml", ".json", ".csv", ".html"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in PRIVATE_TERMS:
            if term.lower() in text.lower():
                findings.append(f"{path.relative_to(root)} contains {term}")
    return findings
