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


def dashboard_html(packet: dict[str, Any], ledger: dict[str, Any]) -> str:
    area_rows = "\n".join(
        f"<tr><td>{escape(item['policy_area'])}</td><td>{escape(item['dominant_direction'])}</td><td>{item['event_count']}</td><td>{item['average_confidence']:.3f}</td></tr>"
        for item in packet["policy_areas"]
    )
    finding_rows = "\n".join(
        f"<tr><td>{escape(item['severity'])}</td><td>{escape(item['policy_area'])}</td><td>{escape(item['finding'])}</td></tr>"
        for item in ledger["findings"]
    )
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
</main>
</html>
"""
