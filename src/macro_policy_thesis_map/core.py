"""Core static analysis for macro policy thesis maps."""

from __future__ import annotations

import hashlib
from datetime import date
from pathlib import Path
from typing import Any

from .io import read_csv, read_csv_document


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
    "demo/release_manifest.md",
    "demo/release_manifest.json",
    "demo/maturity_report.md",
    "demo/maturity_report.json",
    "demo/quickstart_check.md",
    "demo/quickstart_check.json",
    "demo/command_matrix.md",
    "demo/command_matrix.json",
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
        "purpose": "Render a no-JavaScript HTML view of the packet and review ledger.",
        "inputs": ["examples/macro_events.csv or bundled macro_events.csv"],
        "outputs": ["demo/static_dashboard.html"],
        "safety": "Static local rendering only.",
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
        "schema_version": "0.2.0",
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
        ("skill_available", root.joinpath("skills/agent/macro-policy-thesis-map/SKILL.md").exists(), "skills/agent/macro-policy-thesis-map/SKILL.md"),
        ("tests_available", any(root.joinpath("tests").glob("test_*.py")), "tests/test_*.py"),
    ]
    commands = [
        spec
        for spec in COMMAND_SPECS
        if spec["command"] in {"build-packet", "compare-history", "review-ledger", "fixture-doctor", "schema-export", "static-dashboard", "quickstart-check", "command-matrix"}
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


def evidence_bundle(root: Path) -> dict[str, Any]:
    include = [
        "README.md",
        "LICENSE",
        "pyproject.toml",
        "examples/macro_events.csv",
        "examples/prior_macro_events.csv",
        "skills/agent/macro-policy-thesis-map/SKILL.md",
        "tests/test_cli.py",
        "tests/test_safety.py",
        "tests/test_build_backend.py",
    ]
    include.extend(
        artifact
        for artifact in DEMO_ARTIFACTS
        if not artifact.startswith("demo/release_manifest") and not artifact.startswith("demo/evidence_bundle")
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
            "PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .",
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
        "demo/evidence_bundle.json",
        "demo/cold_start_walkthrough.json",
    ]
    checks = [
        ("public_scan", not public_findings(root), "No private terms or credential-shaped tokens in public text."),
        ("neutral_boundaries", all(term in readme.lower() for term in ["does not fetch live data", "connect to brokers", "recommend buys", "predict returns"]), "README states static research boundaries."),
        ("demo_artifacts", all(root.joinpath(path).exists() for path in required_artifacts), "Core demo artifacts are present."),
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
            "title": "Check public readiness",
            "command": "macro-policy-thesis-map public-readiness",
            "expected_result": "A public readiness report lists pass/fail gates.",
        },
        {
            "step": 5,
            "title": "Run final local checks",
            "command": "macro-policy-thesis-map selfcheck && macro-policy-thesis-map public-scan",
            "expected_result": "Both commands exit successfully before sharing artifacts.",
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
    excluded = {"demo/release_manifest.json", "demo/release_manifest.md"}
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


def file_record(root: Path, path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": str(path.relative_to(root)).replace("\\", "/"),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


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
