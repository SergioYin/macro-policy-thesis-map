"""Markdown and HTML renderers."""

from __future__ import annotations

from html import escape
from typing import Any


def table(headers: list[str], rows: list[list[Any]]) -> str:
    output = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        output.append("| " + " | ".join("" if value is None else str(value) for value in row) + " |")
    return "\n".join(output)


def packet_md(payload: dict[str, Any]) -> str:
    rows = [
        [item["policy_area"], item["dominant_direction"], item["event_count"], f"{item['average_confidence']:.3f}", ", ".join(item["channels"])]
        for item in payload["policy_areas"]
    ]
    evidence = [[item["date"], item["event_type"], item["policy_area"], item["direction"], item["evidence"]] for item in payload["evidence"]]
    return f"""# {payload['title']}

{payload['boundaries']}

## Policy Areas

{table(["Area", "Direction", "Events", "Avg confidence", "Channels"], rows)}

## Evidence

{table(["Date", "Type", "Area", "Direction", "Evidence"], evidence)}
"""


def comparison_md(payload: dict[str, Any]) -> str:
    rows = [[item["policy_area"], item["status"], item["prior_direction"], item["current_direction"], item["event_delta"]] for item in payload["rows"]]
    return f"""# Macro Policy History Comparison

{payload['boundaries']}

{table(["Area", "Status", "Prior", "Current", "Event delta"], rows)}
"""


def ledger_md(payload: dict[str, Any]) -> str:
    rows = [[item["severity"], item["policy_area"], item["finding"]] for item in payload["findings"]]
    return f"""# Review Ledger

{payload['boundaries']}

{table(["Severity", "Area", "Finding"], rows)}
"""


def fixture_doctor_md(payload: dict[str, Any]) -> str:
    rows = [
        [item["severity"], item.get("row"), item["check"], item.get("source", ""), item.get("policy_area", ""), item["finding"]]
        for item in payload["findings"]
    ]
    return f"""# Fixture Doctor

{payload['boundaries']}

Status: {payload['status']}

Rows checked: {payload['row_count']}

Blockers: {payload['blocker_count']}

Reviews: {payload['review_count']}

As of: {payload['as_of']}

Max source age days: {payload['max_source_age_days']}

{table(["Severity", "Row", "Check", "Source", "Area", "Finding"], rows)}
"""


def input_schema_md(payload: dict[str, Any]) -> str:
    rows = [
        [
            item["name"],
            item["type"],
            "yes" if item["required"] else "no",
            item.get("format", ""),
            item.get("minimum", ""),
            item.get("maximum", ""),
            ", ".join(item.get("allowed_values", [])),
            item["description"],
        ]
        for item in payload["columns"]
    ]
    controls = [[item] for item in payload["quality_controls"]]
    return f"""# Input Schema

{payload['boundaries']}

Schema version: {payload['schema_version']}

Format: {payload['format']}

Required columns: {", ".join(payload['required_columns'])}

## Data Dictionary

{table(["Column", "Type", "Required", "Format", "Min", "Max", "Allowed values", "Description"], rows)}

## Quality Controls

{table(["Control"], controls)}
"""


def scenario_library_md(payload: dict[str, Any]) -> str:
    rows = [
        [
            item["scenario_id"],
            item["name"],
            item["region"],
            item["policy_area"],
            item["time_horizon"],
            item["shock_axis"],
            item["direction_label"],
            ", ".join(item["schema_fields"]),
            item["adaptation_note"],
        ]
        for item in payload["scenarios"]
    ]
    rules = [[item] for item in payload["schema_adaptation_rules"]]
    return f"""# Static Scenario Library

{payload['boundaries']}

Version: {payload['version']}

Fixture type: {payload['fixture_type']}

Scenario count: {payload['scenario_count']}

## Scenarios

{table(["Scenario", "Name", "Region", "Area", "Horizon", "Axis", "Direction", "Schema fields", "Adaptation note"], rows)}

## Schema Adaptation Rules

{table(["Rule"], rules)}
"""


def assumption_registry_md(payload: dict[str, Any]) -> str:
    rows = [
        [
            item["assumption_id"],
            item["category"],
            item["statement"],
            item["owner"],
            item["validation"],
            item["schema_impact"],
            item["status"],
        ]
        for item in payload["assumptions"]
    ]
    controls = [[item] for item in payload["review_controls"]]
    return f"""# Assumption Registry

{payload['boundaries']}

Version: {payload['version']}

Assumption count: {payload['assumption_count']}

## Assumptions

{table(["Assumption", "Category", "Statement", "Owner", "Validation", "Schema impact", "Status"], rows)}

## Review Controls

{table(["Control"], controls)}
"""


def data_dictionary_diff_md(payload: dict[str, Any]) -> str:
    rows = [
        [
            item["dictionary"],
            item["column_count"],
            ", ".join(item["shared_with_base"]),
            ", ".join(item["additive_columns"]) or "none",
            ", ".join(item["base_columns_not_present"]) or "none",
            item["adaptation_posture"],
        ]
        for item in payload["dictionaries"]
    ]
    recommendations = [[item["decision"], item["rationale"]] for item in payload["recommendations"]]
    constraints = [[item] for item in payload["finance_safety_constraints"]]
    return f"""# Data Dictionary Diff

{payload['boundaries']}

Version: {payload['version']}

Base dictionary: {payload['base_dictionary']}

Dictionary count: {payload['dictionary_count']}

## Dictionary Comparison

{table(["Dictionary", "Columns", "Shared with base", "Additive columns", "Base columns not present", "Adaptation posture"], rows)}

## Recommendations

{table(["Decision", "Rationale"], recommendations)}

## Finance Safety Constraints

{table(["Constraint"], constraints)}
"""


def troubleshoot_md(payload: dict[str, Any]) -> str:
    checks = [
        [item["name"], item["status"], item["symptom"], ", ".join(item["evidence"]), item["resolution"]]
        for item in payload["checks"]
    ]
    commands = [[item] for item in payload["validation_commands"]]
    return f"""# Operator Troubleshooting Guide

{payload['boundaries']}

Version: {payload['version']}

Status: {payload['status']}

Reviews: {payload['review_count']} / {payload['check_count']}

## Checks

{table(["Check", "Status", "Symptom", "Evidence", "Resolution"], checks)}

## Validation Commands

{table(["Command"], commands)}
"""


def docs_export_md(payload: dict[str, Any]) -> str:
    docs = [[item["title"], item["path"], item["bytes"], item["sha256"][:16], item["purpose"]] for item in payload["documents"]]
    missing = [[item["title"], item["path"], item["purpose"]] for item in payload["missing"]] or [["none", "none", "none"]]
    commands = [[item] for item in payload["validation_commands"]]
    return f"""# Operator Documentation Export

{payload['boundaries']}

Version: {payload['version']}

Status: {payload['status']}

Documents: {payload['doc_count']}

Missing: {payload['missing_count']}

## Documents

{table(["Title", "Path", "Bytes", "SHA-256 prefix", "Purpose"], docs)}

## Missing

{table(["Title", "Path", "Purpose"], missing)}

## Validation Commands

{table(["Command"], commands)}
"""


def readme_snippet_md(payload: dict[str, Any]) -> str:
    commands = "\n".join(payload["commands"])
    outputs = [[item] for item in payload["outputs"]]
    return f"""# README Snippet

{payload['boundaries']}

Version: {payload['version']}

```bash
{commands}
```

## Expected Outputs

{table(["Path"], outputs)}
"""


def cli_help_md(payload: dict[str, Any]) -> str:
    rows = [[item["command"], item["usage"], item["purpose"], ", ".join(item["outputs"]), item["safety"]] for item in payload["commands"]]
    return f"""# CLI Help Export

{payload['boundaries']}

Version: {payload['version']}

Command count: {payload['command_count']}

{table(["Command", "Usage", "Purpose", "Outputs", "Safety"], rows)}
"""


def manifest_md(payload: dict[str, Any]) -> str:
    rows = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    return f"""# Release Manifest

{payload['boundaries']}

Artifact count: {payload['artifact_count']}

{table(["Path", "Bytes", "SHA-256 prefix"], rows)}
"""


def maturity_md(payload: dict[str, Any]) -> str:
    rows = [[item["name"], "pass" if item["passed"] else "review"] for item in payload["checks"]]
    return f"""# Maturity Report

{payload['boundaries']}

Score: {payload['score']} / {payload['max_score']}

Status: {payload['status']}

{table(["Check", "Result"], rows)}
"""


def quickstart_md(payload: dict[str, Any]) -> str:
    checks = [[item["name"], "pass" if item["passed"] else "review", item["path"]] for item in payload["checks"]]
    commands = [[item["command"], ", ".join(item["expected_outputs"])] for item in payload["starter_commands"]]
    return f"""# Quickstart Check

{payload['boundaries']}

Status: {payload['status']}

Passed: {payload['passed_count']} / {payload['check_count']}

## Checks

{table(["Check", "Result", "Path"], checks)}

## Starter Commands

{table(["Command", "Expected outputs"], commands)}
"""


def command_matrix_md(payload: dict[str, Any]) -> str:
    rows = [
        [item["command"], item["purpose"], ", ".join(item["inputs"]), ", ".join(item["outputs"]), item["safety"]]
        for item in payload["commands"]
    ]
    return f"""# Command Matrix

{payload['boundaries']}

Command count: {payload['command_count']}

{table(["Command", "Purpose", "Inputs", "Outputs", "Safety"], rows)}
"""


def adoption_notes_md(payload: dict[str, Any]) -> str:
    artifacts = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    commands = [[item] for item in payload["release_commands"]]
    actions = [[item] for item in payload["cold_user_next_actions"]]
    boundaries = [[item] for item in payload["safety_boundaries"]]
    return f"""# Release Owner Adoption Notes

{payload['boundaries']}

Version: {payload['version']}

Maturity: {payload['maturity_status']} ({payload['maturity_score']} / {payload['maturity_max_score']})

Public readiness: {payload['public_readiness_status']}

Release manifest artifacts: {payload['release_artifact_count']}

## Release Commands

{table(["Command"], commands)}

## Cold User Next Actions

{table(["Action"], actions)}

## Safety Boundaries

{table(["Boundary"], boundaries)}

## Artifact Hashes

{table(["Path", "Bytes", "SHA-256 prefix"], artifacts)}
"""


def reviewer_scorecard_md(payload: dict[str, Any]) -> str:
    rows = [
        [
            item["name"],
            "pass" if item["passed"] else "review",
            item["description"],
            ", ".join(item["maturity_mapping"]) or ", ".join(item["evidence"]),
        ]
        for item in payload["rubric"]
    ]
    artifacts = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    return f"""# Reviewer Scorecard

{payload['boundaries']}

Version: {payload['version']}

Status: {payload['status']}

Score: {payload['score']} / {payload['max_score']}

## Rubric Mapping

{table(["Rubric", "Result", "Description", "Evidence mapping"], rows)}

## Artifact Hashes

{table(["Path", "Bytes", "SHA-256 prefix"], artifacts)}
"""


def release_deck_md(payload: dict[str, Any]) -> str:
    slides = []
    for slide in payload["slides"]:
        points = "\n".join(f"- {point}" for point in slide["points"])
        slides.append(f"## {slide['slide']}. {slide['title']}\n\n{points}")
    artifacts = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    return f"""# Release Owner Promotion Deck

{payload['boundaries']}

Version: {payload['version']}

Slide count: {payload['slide_count']}

{chr(10).join(slides)}

## Artifact Hashes

{table(["Path", "Bytes", "SHA-256 prefix"], artifacts)}
"""


def bundle_export_md(payload: dict[str, Any]) -> str:
    artifacts = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    missing = [[item] for item in payload["missing"]] or [["none"]]
    commands = [[item] for item in payload["release_commands"]]
    return f"""# Public Promotion Bundle Export

{payload['boundaries']}

Version: {payload['version']}

Status: {payload['status']}

Export root: {payload['export_root']}

Artifact count: {payload['artifact_count']}

Missing count: {payload['missing_count']}

## Release Commands

{table(["Command"], commands)}

## Missing

{table(["Path"], missing)}

## Artifact Manifest

{table(["Path", "Bytes", "SHA-256 prefix"], artifacts)}
"""


def case_gallery_md(payload: dict[str, Any]) -> str:
    regions = [
        [item["region"], item["case_count"], f"{item['average_confidence']:.3f}", ", ".join(item["policy_areas"]), ", ".join(item["routes"])]
        for item in payload["regions"]
    ]
    cases = [
        [item["case_id"], item["region"], item["case_title"], item["policy_area"], item["direction"], f"{item['confidence']:.3f}", item["route"], item["command"]]
        for item in payload["cases"]
    ]
    source = payload.get("source", {})
    source_line = ""
    if source:
        source_line = f"\nFixture hash: {source['sha256'][:16]}\n"
    return f"""# Public Macro Policy Case Gallery

{payload['boundaries']}

Fixture type: {payload['fixture_type']}

Case count: {payload['case_count']}

Region count: {payload['region_count']}
{source_line}
## Regions

{table(["Region", "Cases", "Avg confidence", "Policy areas", "Routes"], regions)}

## Cases

{table(["Case", "Region", "Title", "Area", "Direction", "Confidence", "Route", "Command"], cases)}
"""


def thesis_impact_brief_md(payload: dict[str, Any]) -> str:
    theses = [
        [
            item["thesis_id"],
            ", ".join(item["policy_areas"]),
            item["axis_count"],
            f"{item['average_impact_score']:.3f}",
            f"{item['average_confidence']:.3f}",
            ", ".join(item["directions"]),
        ]
        for item in payload["theses"]
    ]
    areas = [[item["policy_area"], item["thesis_count"], item["axis_count"], f"{item['average_impact_score']:.3f}"] for item in payload["policy_areas"]]
    rows = [
        [
            item["thesis_id"],
            item["policy_area"],
            item["sensitivity_axis"],
            item["shock_label"],
            item["impact_direction"],
            f"{item['impact_score']:.3f}",
            f"{item['confidence']:.3f}",
            item["rationale"],
        ]
        for item in payload["sensitivities"]
    ]
    source = payload.get("source", {})
    source_line = f"\nFixture hash: {source['sha256'][:16]}\n" if source else ""
    return f"""# Static Thesis Impact Brief

{payload['boundaries']}

Fixture type: {payload['fixture_type']}

Sensitivity count: {payload['sensitivity_count']}

Thesis count: {payload['thesis_count']}

Policy area count: {payload['policy_area_count']}
{source_line}
## Thesis Summary

{table(["Thesis", "Policy areas", "Axes", "Avg impact", "Avg confidence", "Directions"], theses)}

## Policy Area Summary

{table(["Area", "Theses", "Axes", "Avg impact"], areas)}

## Sensitivity Rows

{table(["Thesis", "Area", "Axis", "Shock", "Direction", "Impact", "Confidence", "Rationale"], rows)}
"""


def exposure_map_md(payload: dict[str, Any]) -> str:
    portfolios = [
        [
            item["portfolio_id"],
            item["sleeve_count"],
            item["exposure_count"],
            item["matched_exposure_count"],
            f"{item['average_exposure_score']:.3f}",
            ", ".join(item["policy_areas"]),
        ]
        for item in payload["portfolios"]
    ]
    exposures = [
        [
            item["portfolio_id"],
            item["sleeve"],
            item["exposure_id"],
            item["policy_area"],
            item["thesis_id"],
            item["exposure_direction"],
            f"{item['exposure_score']:.3f}",
            "yes" if item["sensitivity_match"] else "no",
            item["rationale"],
        ]
        for item in payload["exposures"]
    ]
    return f"""# Static Portfolio Exposure Map

{payload['boundaries']}

Fixture type: {payload['fixture_type']}

Portfolio count: {payload['portfolio_count']}

Exposure count: {payload['exposure_count']}

Matched exposure count: {payload['matched_exposure_count']}

## Portfolio Summary

{table(["Portfolio", "Sleeves", "Exposures", "Matched", "Avg exposure", "Policy areas"], portfolios)}

## Exposure Rows

{table(["Portfolio", "Sleeve", "Exposure", "Area", "Thesis", "Direction", "Score", "Sensitivity match", "Rationale"], exposures)}
"""


def evidence_bundle_md(payload: dict[str, Any]) -> str:
    artifacts = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    missing = [[item] for item in payload["missing"]] or [["none"]]
    commands = [[item] for item in payload["evaluation_commands"]]
    return f"""# Evidence Bundle

{payload['boundaries']}

Status: {payload['status']}

Artifact count: {payload['artifact_count']}

Missing count: {payload['missing_count']}

## Evaluation Commands

{table(["Command"], commands)}

## Missing

{table(["Path"], missing)}

## Artifacts

{table(["Path", "Bytes", "SHA-256 prefix"], artifacts)}
"""


def visual_receipt_md(payload: dict[str, Any]) -> str:
    artifacts = [[item["path"], item["bytes"], item["sha256"][:16]] for item in payload["artifacts"]]
    routes = [[item] for item in payload["routes"]] or [["none"]]
    commands = [[item] for item in payload["commands"]]
    return f"""# Macro Policy Visual Receipt

{payload['boundaries']}

Format: {payload['format']}

Artifacts: {payload['artifact_count']}

Routes: {payload['route_count']}

Commands: {payload['command_count']}

## Artifact Hashes

{table(["Path", "Bytes", "SHA-256 prefix"], artifacts)}

## Routes

{table(["Route"], routes)}

## Commands

{table(["Command"], commands)}
"""


def visual_receipt_svg(payload: dict[str, Any]) -> str:
    artifact_lines = [f"{item['path']}  {item['sha256'][:12]}" for item in payload["artifacts"][:7]]
    route_lines = payload["routes"][:7]
    command_lines = payload["commands"][:4]
    rows = artifact_lines + [""] + route_lines + [""] + command_lines
    height = 190 + len(rows) * 22
    text_rows = "\n".join(
        f'<text x="42" y="{180 + index * 22}" class="mono">{escape(row)}</text>'
        for index, row in enumerate(rows)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">Macro Policy Visual Receipt</title>
<desc id="desc">Static receipt of artifact hashes, public routes, and local commands.</desc>
<style>
.bg{{fill:#f8fafc}} .panel{{fill:#ffffff;stroke:#cbd5e1;stroke-width:1.5}} .title{{font:700 28px Arial,sans-serif;fill:#111827}} .label{{font:700 13px Arial,sans-serif;fill:#334155;text-transform:uppercase}} .body{{font:15px Arial,sans-serif;fill:#1f2937}} .mono{{font:13px ui-monospace,SFMono-Regular,Consolas,monospace;fill:#111827}}
</style>
<rect class="bg" width="960" height="{height}"/>
<rect class="panel" x="24" y="24" width="912" height="{height - 48}" rx="8"/>
<text id="receipt-title" x="42" y="70" class="title">Macro Policy Visual Receipt</text>
<text x="42" y="102" class="body">{escape(payload['boundaries'])}</text>
<text x="42" y="138" class="label">Hashes, Routes, Commands</text>
{text_rows}
</svg>
"""


def visual_receipt_html(payload: dict[str, Any]) -> str:
    artifact_rows = "\n".join(
        f"<tr><td>{escape(item['path'])}</td><td>{item['bytes']}</td><td>{escape(item['sha256'][:16])}</td></tr>"
        for item in payload["artifacts"]
    )
    route_rows = "\n".join(f"<tr><td>{escape(route)}</td></tr>" for route in payload["routes"])
    command_rows = "\n".join(f"<tr><td>{escape(command)}</td></tr>" for command in payload["commands"])
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Macro Policy Visual Receipt</title>
<style>
body{{font-family:Arial,sans-serif;margin:2rem;line-height:1.45;color:#1f2937;background:#f8fafc}}
main{{max-width:1040px;margin:auto}} table{{border-collapse:collapse;width:100%;background:white;margin-bottom:1.5rem}}
th,td{{border:1px solid #d1d5db;padding:.55rem;text-align:left;vertical-align:top}} th{{background:#e5e7eb}}
.notice{{border-left:4px solid #64748b;padding:.75rem;background:white}}
</style>
<main>
<h1>Macro Policy Visual Receipt</h1>
<p class="notice">{escape(payload['boundaries'])}</p>
<h2>Artifact Hashes</h2>
<table><thead><tr><th>Path</th><th>Bytes</th><th>SHA-256 prefix</th></tr></thead><tbody>{artifact_rows}</tbody></table>
<h2>Routes</h2>
<table><thead><tr><th>Route</th></tr></thead><tbody>{route_rows}</tbody></table>
<h2>Commands</h2>
<table><thead><tr><th>Command</th></tr></thead><tbody>{command_rows}</tbody></table>
</main>
</html>
"""


def public_readiness_md(payload: dict[str, Any]) -> str:
    checks = [[item["name"], "pass" if item["passed"] else "block", item["detail"]] for item in payload["checks"]]
    blockers = [[item["name"], item["detail"]] for item in payload["blockers"]] or [["none", "none"]]
    return f"""# Public Readiness

{payload['boundaries']}

Status: {payload['status']}

Passed: {payload['passed_count']} / {payload['check_count']}

## Checks

{table(["Check", "Result", "Detail"], checks)}

## Blockers

{table(["Check", "Detail"], blockers)}
"""


def cold_start_md(payload: dict[str, Any]) -> str:
    steps = [[item["step"], item["title"], item["command"], item["expected_result"]] for item in payload["steps"]]
    notes = [[item] for item in payload["safety_notes"]]
    return f"""# Cold Start Walkthrough

{payload['boundaries']}

Step count: {payload['step_count']}

## Steps

{table(["Step", "Title", "Command", "Expected result"], steps)}

## Safety Notes

{table(["Note"], notes)}
"""


def dashboard_html(packet: dict[str, Any], ledger: dict[str, Any], impact: dict[str, Any] | None = None, exposures: dict[str, Any] | None = None) -> str:
    area_rows = "\n".join(
        f"<tr><td>{escape(item['policy_area'])}</td><td>{escape(item['dominant_direction'])}</td><td>{item['event_count']}</td><td>{item['average_confidence']:.3f}</td></tr>"
        for item in packet["policy_areas"]
    )
    finding_rows = "\n".join(
        f"<tr><td>{escape(item['severity'])}</td><td>{escape(item['policy_area'])}</td><td>{escape(item['finding'])}</td></tr>"
        for item in ledger["findings"]
    )
    sensitivity_section = ""
    if impact is not None:
        thesis_rows = "\n".join(
            f"<tr><td>{escape(item['thesis_id'])}</td><td>{escape(', '.join(item['policy_areas']))}</td><td>{item['axis_count']}</td><td>{item['average_impact_score']:.3f}</td></tr>"
            for item in impact["theses"]
        )
        exposure_rows = ""
        if exposures is not None:
            exposure_rows = "\n".join(
                f"<tr><td>{escape(item['portfolio_id'])}</td><td>{item['exposure_count']}</td><td>{item['matched_exposure_count']}</td><td>{item['average_exposure_score']:.3f}</td></tr>"
                for item in exposures["portfolios"]
            )
        sensitivity_section = f"""
<h2>Static Sensitivity Layer</h2>
<p><a href="thesis_impact_brief.md">Thesis impact brief</a> and <a href="exposure_map.md">exposure map</a></p>
<table><thead><tr><th>Thesis</th><th>Policy areas</th><th>Axes</th><th>Avg impact</th></tr></thead><tbody>{thesis_rows}</tbody></table>
<h2>Static Exposure Layer</h2>
<table><thead><tr><th>Portfolio</th><th>Exposures</th><th>Matched</th><th>Avg exposure</th></tr></thead><tbody>{exposure_rows}</tbody></table>"""
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Macro Policy Thesis Map</title>
<style>
body{{font-family:Arial,sans-serif;margin:2rem;line-height:1.45;color:#1f2937;background:#f8fafc}}
main{{max-width:1040px;margin:auto}} table{{border-collapse:collapse;width:100%;background:white}}
th,td{{border:1px solid #d1d5db;padding:.55rem;text-align:left;vertical-align:top}} th{{background:#e5e7eb}}
.notice{{border-left:4px solid #64748b;padding:.75rem;background:white}}
</style>
<main>
<h1>Macro Policy Thesis Map</h1>
<p class="notice">{escape(packet['boundaries'])}</p>
<h2>Policy Areas</h2>
<table><thead><tr><th>Area</th><th>Direction</th><th>Events</th><th>Avg confidence</th></tr></thead><tbody>{area_rows}</tbody></table>
<h2>Review Ledger</h2>
<table><thead><tr><th>Severity</th><th>Area</th><th>Finding</th></tr></thead><tbody>{finding_rows}</tbody></table>
{sensitivity_section}
</main>
</html>
"""
