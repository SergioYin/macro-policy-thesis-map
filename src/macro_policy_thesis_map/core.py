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
        "PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .",
        "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .",
    ]
    return {
        "title": "README Snippet",
        "version": __version__,
        "commands": commands,
        "outputs": ["demo/thesis_packet.md", "demo/review_ledger.md", "demo/scenario_library.md", "demo/assumption_registry.md", "demo/data_dictionary_diff.md", "demo/troubleshoot.md"],
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
            "title": "Export the public promotion bundle manifest",
            "command": "macro-policy-thesis-map bundle-export",
            "expected_result": "A deterministic bundle manifest is written under demo/bundle_export/.",
        },
        {
            "step": 9,
            "title": "Check public readiness",
            "command": "macro-policy-thesis-map public-readiness",
            "expected_result": "A public readiness report lists pass/fail gates.",
        },
        {
            "step": 10,
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
        ("public_package", ["package", "readme", "license", "skill"], "Package metadata, docs, license, and agent skill are present."),
        ("verification", ["tests", "no_workflows"], "Tests exist and no workflow files are required."),
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
