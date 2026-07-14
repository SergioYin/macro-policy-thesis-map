"""Command line interface for macro policy thesis maps."""

from __future__ import annotations

import argparse
from datetime import date
from importlib import resources
import sys
from pathlib import Path

from . import __version__
from .core import (
    DISCLAIMER,
    build_packet,
    case_gallery,
    cold_start_walkthrough,
    command_matrix,
    compare_packets,
    diff_check,
    evidence_bundle,
    exposure_map,
    fixture_doctor,
    input_schema,
    load_cases,
    load_events,
    load_exposures,
    load_sensitivities,
    maturity,
    public_findings,
    public_readiness,
    quickstart_check,
    release_manifest,
    review_ledger,
    thesis_impact_brief,
)
from .io import read_json, resolve, write_json, write_text
from .render import (
    cold_start_md,
    command_matrix_md,
    comparison_md,
    case_gallery_md,
    dashboard_html,
    evidence_bundle_md,
    exposure_map_md,
    fixture_doctor_md,
    input_schema_md,
    ledger_md,
    manifest_md,
    maturity_md,
    packet_md,
    public_readiness_md,
    quickstart_md,
    thesis_impact_brief_md,
    visual_receipt_html,
    visual_receipt_md,
    visual_receipt_svg,
)


DEFAULT_EVENTS = "examples/macro_events.csv"
DEFAULT_PRIOR_EVENTS = "examples/prior_macro_events.csv"
DEFAULT_CASES = "examples/public_macro_cases.csv"
DEFAULT_SENSITIVITIES = "examples/thesis_sensitivities.csv"
DEFAULT_EXPOSURES = "examples/portfolio_exposures.csv"


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="macro-policy-thesis-map", description="Build static macro policy thesis evidence packets.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    packet = sub.add_parser("build-packet", help="Build Markdown and JSON thesis packet from static events.")
    add_event_args(packet)
    packet.add_argument("--title", default="Macro Policy Thesis Map")
    packet.add_argument("--out-md", default="demo/thesis_packet.md")
    packet.add_argument("--out-json", default="demo/thesis_packet.json")
    packet.set_defaults(func=cmd_build_packet)

    compare = sub.add_parser("compare-history", help="Compare current and prior thesis packets or event files.")
    compare.add_argument("--root", default=".")
    compare.add_argument("--current", default=DEFAULT_EVENTS)
    compare.add_argument("--prior", default=DEFAULT_PRIOR_EVENTS)
    compare.add_argument("--out-md", default="demo/history_comparison.md")
    compare.add_argument("--out-json", default="demo/history_comparison.json")
    compare.set_defaults(func=cmd_compare_history)

    ledger = sub.add_parser("review-ledger", help="Build a static review ledger for confidence and safety checks.")
    add_event_args(ledger)
    ledger.add_argument("--min-confidence", type=float, default=0.55)
    ledger.add_argument("--out-md", default="demo/review_ledger.md")
    ledger.add_argument("--out-json", default="demo/review_ledger.json")
    ledger.set_defaults(func=cmd_review_ledger)

    dashboard = sub.add_parser("static-dashboard", help="Build a no-JavaScript static HTML dashboard.")
    add_event_args(dashboard)
    dashboard.add_argument("--out-html", default="demo/static_dashboard.html")
    dashboard.set_defaults(func=cmd_static_dashboard)

    impact = sub.add_parser("thesis-impact-brief", help="Build a static thesis sensitivity impact brief.")
    impact.add_argument("--root", default=".")
    impact.add_argument("--sensitivities", default=DEFAULT_SENSITIVITIES)
    impact.add_argument("--out-md", default="demo/thesis_impact_brief.md")
    impact.add_argument("--out-json", default="demo/thesis_impact_brief.json")
    impact.set_defaults(func=cmd_thesis_impact_brief)

    exposures = sub.add_parser("exposure-map", help="Build a static portfolio exposure map against thesis sensitivities.")
    exposures.add_argument("--root", default=".")
    exposures.add_argument("--sensitivities", default=DEFAULT_SENSITIVITIES)
    exposures.add_argument("--exposures", default=DEFAULT_EXPOSURES)
    exposures.add_argument("--out-md", default="demo/exposure_map.md")
    exposures.add_argument("--out-json", default="demo/exposure_map.json")
    exposures.set_defaults(func=cmd_exposure_map)

    gallery = sub.add_parser("case-gallery", help="Build a public-safe multi-region macro policy case gallery.")
    gallery.add_argument("--root", default=".")
    gallery.add_argument("--cases", default=DEFAULT_CASES)
    gallery.add_argument("--out-md", default="demo/case_gallery.md")
    gallery.add_argument("--out-json", default="demo/case_gallery.json")
    gallery.set_defaults(func=cmd_case_gallery)

    receipt = sub.add_parser("visual-receipt", help="Build a static SVG or HTML receipt with hashes, routes, and commands.")
    receipt.add_argument("--root", default=".")
    receipt.add_argument("--format", choices=["svg", "html"], default="svg")
    receipt.add_argument("--out-visual", default=None)
    receipt.add_argument("--out-md", default="demo/visual_receipt.md")
    receipt.add_argument("--out-json", default="demo/visual_receipt.json")
    receipt.set_defaults(func=cmd_visual_receipt)

    doctor = sub.add_parser("fixture-doctor", help="Validate static CSV fixtures for finance-domain quality controls.")
    add_event_args(doctor)
    doctor.add_argument("--as-of", default="2026-07-15", help="ISO date used for stale-source checks.")
    doctor.add_argument("--max-source-age-days", type=int, default=45)
    doctor.add_argument("--out-md", default="demo/fixture_doctor.md")
    doctor.add_argument("--out-json", default="demo/fixture_doctor.json")
    doctor.set_defaults(func=cmd_fixture_doctor)

    schema = sub.add_parser("schema-export", help="Export the machine-readable input schema and data dictionary.")
    schema.add_argument("--root", default=".")
    schema.add_argument("--out-md", default="demo/input_schema.md")
    schema.add_argument("--out-json", default="demo/input_schema.json")
    schema.set_defaults(func=cmd_schema_export)

    manifest = sub.add_parser("release-manifest", help="Build a deterministic public release manifest.")
    manifest.add_argument("--root", default=".")
    manifest.add_argument("--out-md", default="demo/release_manifest.md")
    manifest.add_argument("--out-json", default="demo/release_manifest.json")
    manifest.set_defaults(func=cmd_release_manifest)

    selfcheck = sub.add_parser("selfcheck", help="Check examples, docs, tests, safety boundaries, and public scan.")
    selfcheck.add_argument("--root", default=".")
    selfcheck.set_defaults(func=cmd_selfcheck)

    public_scan = sub.add_parser("public-scan", help="Scan public text files for private terms and credentials.")
    public_scan.add_argument("--root", default=".")
    public_scan.set_defaults(func=cmd_public_scan)

    diff = sub.add_parser("diff-check", help="Compare the saved release manifest with current file hashes.")
    diff.add_argument("--root", default=".")
    diff.add_argument("--manifest", default="demo/release_manifest.json")
    diff.set_defaults(func=cmd_diff_check)

    mat = sub.add_parser("maturity-report", help="Write a maturity report for release review.")
    mat.add_argument("--root", default=".")
    mat.add_argument("--out-md", default="demo/maturity_report.md")
    mat.add_argument("--out-json", default="demo/maturity_report.json")
    mat.set_defaults(func=cmd_maturity_report)

    quick = sub.add_parser("quickstart-check", help="Write a deterministic first-evaluator quickstart check.")
    quick.add_argument("--root", default=".")
    quick.add_argument("--out-md", default="demo/quickstart_check.md")
    quick.add_argument("--out-json", default="demo/quickstart_check.json")
    quick.set_defaults(func=cmd_quickstart_check)

    matrix = sub.add_parser("command-matrix", help="Write a public matrix of commands, inputs, outputs, and safety posture.")
    matrix.add_argument("--root", default=".")
    matrix.add_argument("--out-md", default="demo/command_matrix.md")
    matrix.add_argument("--out-json", default="demo/command_matrix.json")
    matrix.set_defaults(func=cmd_command_matrix)

    bundle = sub.add_parser("evidence-bundle", help="Write a public evaluation evidence bundle.")
    bundle.add_argument("--root", default=".")
    bundle.add_argument("--out-md", default="demo/evidence_bundle.md")
    bundle.add_argument("--out-json", default="demo/evidence_bundle.json")
    bundle.set_defaults(func=cmd_evidence_bundle)

    readiness = sub.add_parser("public-readiness", help="Write public release-readiness gates and blockers.")
    readiness.add_argument("--root", default=".")
    readiness.add_argument("--out-md", default="demo/public_readiness.md")
    readiness.add_argument("--out-json", default="demo/public_readiness.json")
    readiness.set_defaults(func=cmd_public_readiness)

    cold = sub.add_parser("cold-start-walkthrough", help="Write a deterministic first-run evaluator walkthrough.")
    cold.add_argument("--root", default=".")
    cold.add_argument("--out-md", default="demo/cold_start_walkthrough.md")
    cold.add_argument("--out-json", default="demo/cold_start_walkthrough.json")
    cold.set_defaults(func=cmd_cold_start_walkthrough)
    return parser


def add_event_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--root", default=".")
    parser.add_argument("--events", default=DEFAULT_EVENTS)


def packet_from_args(args: argparse.Namespace) -> tuple[Path, dict[str, object]]:
    root = Path(args.root)
    events = load_events_arg(root, args.events, DEFAULT_EVENTS)
    return root, build_packet(events, getattr(args, "title", "Macro Policy Thesis Map"))


def cmd_build_packet(args: argparse.Namespace) -> int:
    root, payload = packet_from_args(args)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), packet_md(payload))
    return 0


def cmd_compare_history(args: argparse.Namespace) -> int:
    root = Path(args.root)
    current = build_packet(load_events_arg(root, args.current, DEFAULT_EVENTS), "Current Macro Policy Thesis Map")
    prior = build_packet(load_events_arg(root, args.prior, DEFAULT_PRIOR_EVENTS), "Prior Macro Policy Thesis Map")
    payload = compare_packets(current, prior)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), comparison_md(payload))
    return 0


def cmd_review_ledger(args: argparse.Namespace) -> int:
    root, packet = packet_from_args(args)
    payload = review_ledger(packet, args.min_confidence)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), ledger_md(payload))
    return 0


def cmd_static_dashboard(args: argparse.Namespace) -> int:
    root, packet = packet_from_args(args)
    ledger = review_ledger(packet, 0.55)
    impact = None
    exposures = None
    try:
        sensitivity_path, sensitivities = load_sensitivities_arg(root, DEFAULT_SENSITIVITIES)
        impact = thesis_impact_brief(sensitivities, sensitivity_path)
        exposure_path, exposure_rows = load_exposures_arg(root, DEFAULT_EXPOSURES)
        exposures = exposure_map(exposure_rows, sensitivities, exposure_path, sensitivity_path)
    except (OSError, ValueError):
        impact = None
        exposures = None
    write_text(resolve(root, args.out_html), dashboard_html(packet, ledger, impact, exposures))
    return 0


def cmd_thesis_impact_brief(args: argparse.Namespace) -> int:
    root = Path(args.root)
    path, sensitivities = load_sensitivities_arg(root, args.sensitivities)
    payload = thesis_impact_brief(sensitivities, path)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), thesis_impact_brief_md(payload))
    return 0


def cmd_exposure_map(args: argparse.Namespace) -> int:
    root = Path(args.root)
    sensitivity_path, sensitivities = load_sensitivities_arg(root, args.sensitivities)
    exposure_path, exposures = load_exposures_arg(root, args.exposures)
    payload = exposure_map(exposures, sensitivities, exposure_path, sensitivity_path)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), exposure_map_md(payload))
    return 0


def cmd_case_gallery(args: argparse.Namespace) -> int:
    root = Path(args.root)
    cases_path, cases = load_cases_arg(root, args.cases, DEFAULT_CASES)
    payload = case_gallery(cases, cases_path)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), case_gallery_md(payload))
    return 0


def cmd_visual_receipt(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = visual_receipt_payload(root, args.format)
    out_visual = args.out_visual or f"demo/visual_receipt.{args.format}"
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), visual_receipt_md(payload))
    if args.format == "svg":
        write_text(resolve(root, out_visual), visual_receipt_svg(payload))
    else:
        write_text(resolve(root, out_visual), visual_receipt_html(payload))
    return 0


def cmd_fixture_doctor(args: argparse.Namespace) -> int:
    root = Path(args.root)
    path = resolve(root, args.events)
    if path.exists():
        payload = fixture_doctor(path, as_of=date.fromisoformat(args.as_of), max_source_age_days=args.max_source_age_days)
    elif args.events == DEFAULT_EVENTS:
        resource = bundled_event_resource(Path(DEFAULT_EVENTS).name)
        with resources.as_file(resource) as bundled_path:
            payload = fixture_doctor(bundled_path, as_of=date.fromisoformat(args.as_of), max_source_age_days=args.max_source_age_days)
    else:
        raise FileNotFoundError(path)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), fixture_doctor_md(payload))
    return 0 if payload["status"] == "pass" else 1


def cmd_schema_export(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = input_schema()
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), input_schema_md(payload))
    return 0


def cmd_release_manifest(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = release_manifest(root)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), manifest_md(payload))
    return 0


def cmd_maturity_report(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = maturity(root)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), maturity_md(payload))
    return 0


def cmd_quickstart_check(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = quickstart_check(root)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), quickstart_md(payload))
    return 0


def cmd_command_matrix(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = command_matrix()
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), command_matrix_md(payload))
    return 0


def cmd_evidence_bundle(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = evidence_bundle(root)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), evidence_bundle_md(payload))
    return 0


def cmd_public_readiness(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = public_readiness(root)
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), public_readiness_md(payload))
    return 0 if payload["status"] == "ready" else 1


def cmd_cold_start_walkthrough(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = cold_start_walkthrough()
    write_json(resolve(root, args.out_json), payload)
    write_text(resolve(root, args.out_md), cold_start_md(payload))
    return 0


def cmd_public_scan(args: argparse.Namespace) -> int:
    findings = public_findings(Path(args.root))
    if findings:
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    print("public scan passed")
    return 0


def cmd_diff_check(args: argparse.Namespace) -> int:
    root = Path(args.root)
    payload = diff_check(root, resolve(root, args.manifest))
    if payload["status"] == "pass":
        print(f"diff check passed ({payload['checked_count']} files)")
        return 0
    for finding in payload["findings"]:
        print(f"{finding['path']}: {finding['finding']}", file=sys.stderr)
    return 1


def cmd_selfcheck(args: argparse.Namespace) -> int:
    root = Path(args.root)
    required = [
        root / "README.md",
        root / "LICENSE",
        root / "pyproject.toml",
        root / "examples" / "macro_events.csv",
        root / "examples" / "thesis_sensitivities.csv",
        root / "examples" / "portfolio_exposures.csv",
        root / "src" / "macro_policy_thesis_map" / "examples" / "macro_events.csv",
        root / "src" / "macro_policy_thesis_map" / "examples" / "prior_macro_events.csv",
        root / "src" / "macro_policy_thesis_map" / "examples" / "thesis_sensitivities.csv",
        root / "src" / "macro_policy_thesis_map" / "examples" / "portfolio_exposures.csv",
        root / "tests" / "test_cli.py",
        root / "skills" / "agent" / "macro-policy-thesis-map" / "SKILL.md",
        root / "demo" / "quickstart_check.json",
        root / "demo" / "command_matrix.json",
        root / "demo" / "evidence_bundle.json",
        root / "demo" / "public_readiness.json",
        root / "demo" / "cold_start_walkthrough.json",
        root / "demo" / "fixture_doctor.json",
        root / "demo" / "input_schema.json",
        root / "demo" / "case_gallery.json",
        root / "demo" / "visual_receipt.json",
        root / "demo" / "thesis_impact_brief.json",
        root / "demo" / "exposure_map.json",
    ]
    missing = [str(path.relative_to(root)) for path in required if not path.exists()]
    readme = (root / "README.md").read_text(encoding="utf-8").lower() if (root / "README.md").exists() else ""
    boundary_terms = ["does not fetch live data", "connect to brokers", "recommend buys", "predict returns"]
    missing.extend([f"README missing boundary: {term}" for term in boundary_terms if term not in readme])
    findings = public_findings(root)
    missing.extend(findings)
    if missing:
        for item in missing:
            print(item, file=sys.stderr)
        return 1
    print("selfcheck passed")
    return 0


def load_events_arg(root: Path, value: str, default_value: str) -> list[dict[str, object]]:
    path = resolve(root, value)
    if path.exists():
        return load_events(path)
    if value == default_value:
        return load_bundled_events(Path(default_value).name)
    raise FileNotFoundError(path)


def load_cases_arg(root: Path, value: str, default_value: str) -> tuple[Path, list[dict[str, object]]]:
    path = resolve(root, value)
    if path.exists():
        return path, load_cases(path)
    if value == default_value:
        with resources.as_file(bundled_event_resource(Path(default_value).name)) as bundled_path:
            return bundled_path, load_cases(bundled_path)
    raise FileNotFoundError(path)


def load_sensitivities_arg(root: Path, value: str) -> tuple[Path, list[dict[str, object]]]:
    path = resolve(root, value)
    if path.exists():
        return path, load_sensitivities(path)
    if value == DEFAULT_SENSITIVITIES:
        with resources.as_file(bundled_event_resource(Path(DEFAULT_SENSITIVITIES).name)) as bundled_path:
            return bundled_path, load_sensitivities(bundled_path)
    raise FileNotFoundError(path)


def load_exposures_arg(root: Path, value: str) -> tuple[Path, list[dict[str, object]]]:
    path = resolve(root, value)
    if path.exists():
        return path, load_exposures(path)
    if value == DEFAULT_EXPOSURES:
        with resources.as_file(bundled_event_resource(Path(DEFAULT_EXPOSURES).name)) as bundled_path:
            return bundled_path, load_exposures(bundled_path)
    raise FileNotFoundError(path)


def visual_receipt_payload(root: Path, visual_format: str) -> dict[str, object]:
    from .core import visual_receipt

    return visual_receipt(root, visual_format=visual_format)


def load_bundled_events(filename: str) -> list[dict[str, object]]:
    with resources.as_file(bundled_event_resource(filename)) as path:
        return load_events(path)


def bundled_event_resource(filename: str):
    resource = resources.files("macro_policy_thesis_map").joinpath("examples", filename)
    if not resource.is_file():
        raise FileNotFoundError(f"bundled example {filename} is missing")
    return resource


def load_packet(path: Path) -> dict[str, object]:
    payload = read_json(path)
    if "policy_areas" not in payload:
        raise ValueError(f"{path} is not a thesis packet")
    return payload


if __name__ == "__main__":
    raise SystemExit(main())
