from pathlib import Path
import hashlib
import json

import pytest

from macro_policy_thesis_map.cli import main


ROOT = Path(__file__).resolve().parents[1]


def test_build_packet_writes_json_and_markdown(tmp_path):
    out_json = tmp_path / "packet.json"
    out_md = tmp_path / "packet.md"

    assert main(["build-packet", "--root", str(ROOT), "--out-json", str(out_json), "--out-md", str(out_md)]) == 0

    assert "policy_areas" in out_json.read_text(encoding="utf-8")
    assert "Not investment advice" in out_md.read_text(encoding="utf-8")


def test_compare_history_and_ledger(tmp_path):
    compare_json = tmp_path / "comparison.json"
    compare_md = tmp_path / "comparison.md"
    ledger_json = tmp_path / "ledger.json"
    ledger_md = tmp_path / "ledger.md"

    assert main(["compare-history", "--root", str(ROOT), "--out-json", str(compare_json), "--out-md", str(compare_md)]) == 0
    assert main(["review-ledger", "--root", str(ROOT), "--out-json", str(ledger_json), "--out-md", str(ledger_md)]) == 0

    assert "event_delta" in compare_json.read_text(encoding="utf-8")
    assert "finding_count" in ledger_json.read_text(encoding="utf-8")


def test_dashboard_manifest_maturity_and_selfcheck(tmp_path):
    dashboard = tmp_path / "dashboard.html"
    manifest_json = tmp_path / "manifest.json"
    manifest_md = tmp_path / "manifest.md"
    maturity_json = tmp_path / "maturity.json"
    maturity_md = tmp_path / "maturity.md"

    assert main(["static-dashboard", "--root", str(ROOT), "--out-html", str(dashboard)]) == 0
    assert main(["thesis-impact-brief", "--root", str(ROOT)]) == 0
    assert main(["exposure-map", "--root", str(ROOT)]) == 0
    assert main(["case-gallery", "--root", str(ROOT)]) == 0
    assert main(["visual-receipt", "--root", str(ROOT)]) == 0
    assert main(["troubleshoot", "--root", str(ROOT)]) == 0
    assert main(["docs-export", "--root", str(ROOT)]) == 0
    assert main(["readme-snippet", "--root", str(ROOT)]) == 0
    assert main(["cli-help", "--root", str(ROOT)]) == 0
    assert main(["release-manifest", "--root", str(ROOT), "--out-json", str(manifest_json), "--out-md", str(manifest_md)]) == 0
    assert main(["maturity-report", "--root", str(ROOT), "--out-json", str(maturity_json), "--out-md", str(maturity_md)]) == 0
    assert main(["adoption-notes", "--root", str(ROOT)]) == 0
    assert main(["reviewer-scorecard", "--root", str(ROOT)]) == 0
    assert main(["release-deck", "--root", str(ROOT)]) == 0
    assert main(["bundle-export", "--root", str(ROOT)]) == 0
    assert main(["selfcheck", "--root", str(ROOT)]) == 0

    assert "<html" in dashboard.read_text(encoding="utf-8")
    assert "artifact_count" in manifest_json.read_text(encoding="utf-8")
    assert "ready" in maturity_json.read_text(encoding="utf-8")


def test_promotion_readiness_commands_write_public_artifacts(tmp_path):
    quick_json = tmp_path / "quickstart.json"
    quick_md = tmp_path / "quickstart.md"
    matrix_json = tmp_path / "matrix.json"
    matrix_md = tmp_path / "matrix.md"
    cold_json = tmp_path / "cold.json"
    cold_md = tmp_path / "cold.md"

    assert main(["quickstart-check", "--root", str(ROOT), "--out-json", str(quick_json), "--out-md", str(quick_md)]) == 0
    assert main(["command-matrix", "--root", str(ROOT), "--out-json", str(matrix_json), "--out-md", str(matrix_md)]) == 0
    assert main(["cold-start-walkthrough", "--root", str(ROOT), "--out-json", str(cold_json), "--out-md", str(cold_md)]) == 0

    assert '"status": "ready"' in quick_json.read_text(encoding="utf-8")
    assert "quickstart-check" in matrix_json.read_text(encoding="utf-8")
    assert "static commands" in cold_md.read_text(encoding="utf-8")


def test_fixture_doctor_and_schema_export(tmp_path):
    doctor_json = tmp_path / "doctor.json"
    doctor_md = tmp_path / "doctor.md"
    schema_json = tmp_path / "schema.json"
    schema_md = tmp_path / "schema.md"

    assert main(["fixture-doctor", "--root", str(ROOT), "--out-json", str(doctor_json), "--out-md", str(doctor_md)]) == 0
    assert main(["schema-export", "--root", str(ROOT), "--out-json", str(schema_json), "--out-md", str(schema_md)]) == 0

    assert '"status": "pass"' in doctor_json.read_text(encoding="utf-8")
    assert "Fixture Doctor" in doctor_md.read_text(encoding="utf-8")
    schema_text = schema_json.read_text(encoding="utf-8")
    assert '"schema_version": "0.7.0"' in schema_text
    assert "confidence" in schema_text
    assert "Data Dictionary" in schema_md.read_text(encoding="utf-8")


def test_operator_usability_surfaces(tmp_path):
    trouble_json = tmp_path / "troubleshoot.json"
    trouble_md = tmp_path / "troubleshoot.md"
    docs_json = tmp_path / "docs.json"
    docs_md = tmp_path / "docs.md"
    snippet_json = tmp_path / "snippet.json"
    snippet_md = tmp_path / "snippet.md"
    help_json = tmp_path / "help.json"
    help_md = tmp_path / "help.md"

    assert main(["troubleshoot", "--root", str(ROOT), "--out-json", str(trouble_json), "--out-md", str(trouble_md)]) == 0
    assert main(["docs-export", "--root", str(ROOT), "--out-json", str(docs_json), "--out-md", str(docs_md)]) == 0
    assert main(["readme-snippet", "--root", str(ROOT), "--out-json", str(snippet_json), "--out-md", str(snippet_md)]) == 0
    assert main(["cli-help", "--root", str(ROOT), "--out-json", str(help_json), "--out-md", str(help_md)]) == 0

    assert "Operator Troubleshooting Guide" in trouble_md.read_text(encoding="utf-8")
    assert "validation_commands" in trouble_json.read_text(encoding="utf-8")
    assert "Operator Documentation Export" in docs_md.read_text(encoding="utf-8")
    assert "documents" in docs_json.read_text(encoding="utf-8")
    assert "fixture-doctor --root ." in snippet_md.read_text(encoding="utf-8")
    assert "CLI Help Export" in help_md.read_text(encoding="utf-8")
    assert "troubleshoot" in help_json.read_text(encoding="utf-8")


def test_thesis_impact_brief_and_exposure_map(tmp_path):
    impact_json = tmp_path / "impact.json"
    impact_md = tmp_path / "impact.md"
    exposure_json = tmp_path / "exposure.json"
    exposure_md = tmp_path / "exposure.md"

    assert main(["thesis-impact-brief", "--root", str(ROOT), "--out-json", str(impact_json), "--out-md", str(impact_md)]) == 0
    assert main(["exposure-map", "--root", str(ROOT), "--out-json", str(exposure_json), "--out-md", str(exposure_md)]) == 0

    assert '"thesis_count": 4' in impact_json.read_text(encoding="utf-8")
    assert "Static Thesis Impact Brief" in impact_md.read_text(encoding="utf-8")
    assert '"matched_exposure_count": 5' in exposure_json.read_text(encoding="utf-8")
    assert "Static Portfolio Exposure Map" in exposure_md.read_text(encoding="utf-8")


def test_schema_adaptation_commands(tmp_path):
    scenario_json = tmp_path / "scenario.json"
    scenario_md = tmp_path / "scenario.md"
    assumption_json = tmp_path / "assumption.json"
    assumption_md = tmp_path / "assumption.md"
    diff_json = tmp_path / "diff.json"
    diff_md = tmp_path / "diff.md"

    assert main(["scenario-library", "--root", str(ROOT), "--out-json", str(scenario_json), "--out-md", str(scenario_md)]) == 0
    assert main(["assumption-registry", "--root", str(ROOT), "--out-json", str(assumption_json), "--out-md", str(assumption_md)]) == 0
    assert main(["data-dictionary-diff", "--root", str(ROOT), "--out-json", str(diff_json), "--out-md", str(diff_md)]) == 0

    assert '"scenario_count": 4' in scenario_json.read_text(encoding="utf-8")
    assert "Static Scenario Library" in scenario_md.read_text(encoding="utf-8")
    assert '"assumption_count": 4' in assumption_json.read_text(encoding="utf-8")
    assert "Assumption Registry" in assumption_md.read_text(encoding="utf-8")
    assert '"base_dictionary": "base_event"' in diff_json.read_text(encoding="utf-8")
    assert "Data Dictionary Diff" in diff_md.read_text(encoding="utf-8")


def test_case_gallery_and_visual_receipt(tmp_path):
    gallery_json = tmp_path / "gallery.json"
    gallery_md = tmp_path / "gallery.md"
    receipt_json = tmp_path / "receipt.json"
    receipt_md = tmp_path / "receipt.md"
    receipt_svg = tmp_path / "receipt.svg"
    receipt_html = tmp_path / "receipt.html"

    assert main(["case-gallery", "--root", str(ROOT), "--out-json", str(gallery_json), "--out-md", str(gallery_md)]) == 0
    assert (
        main(
            [
                "visual-receipt",
                "--root",
                str(ROOT),
                "--out-json",
                str(receipt_json),
                "--out-md",
                str(receipt_md),
                "--out-visual",
                str(receipt_svg),
            ]
        )
        == 0
    )
    assert (
        main(
            [
                "visual-receipt",
                "--root",
                str(ROOT),
                "--format",
                "html",
                "--out-json",
                str(receipt_json),
                "--out-md",
                str(receipt_md),
                "--out-visual",
                str(receipt_html),
            ]
        )
        == 0
    )

    gallery_text = gallery_json.read_text(encoding="utf-8")
    assert '"region": "US"' in gallery_text
    assert '"region": "EU"' in gallery_text
    assert '"region": "Asia"' in gallery_text
    assert "/cases/us-001" in gallery_md.read_text(encoding="utf-8")
    assert "<svg" in receipt_svg.read_text(encoding="utf-8")
    assert "<html" in receipt_html.read_text(encoding="utf-8")
    assert "sha256" in receipt_json.read_text(encoding="utf-8")


def test_fixture_doctor_blocks_bad_finance_fixture(tmp_path):
    fixture = tmp_path / "bad.csv"
    fixture.write_text(
        "\n".join(
            [
                "date,event_type,source,policy_area,channel,direction,confidence,evidence,thesis_link",
                "2026-04-01,trade_call,source,monetary-policy,discount-rate,restrictive,1.5,Buy now,thesis-alpha",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    out_json = tmp_path / "doctor.json"
    out_md = tmp_path / "doctor.md"

    assert main(["fixture-doctor", "--root", str(tmp_path), "--events", "bad.csv", "--out-json", str(out_json), "--out-md", str(out_md)]) == 1
    text = out_json.read_text(encoding="utf-8")
    assert '"status": "blocked"' in text
    assert "event_type" in text
    assert "Confidence 1.5 is outside 0..1" in text
    assert "Advice-like term present: buy" in text


def test_evidence_bundle_and_public_readiness_surfaces(tmp_path):
    bundle_json = tmp_path / "bundle.json"
    bundle_md = tmp_path / "bundle.md"
    readiness_json = tmp_path / "readiness.json"
    readiness_md = tmp_path / "readiness.md"

    assert main(["evidence-bundle", "--root", str(ROOT), "--out-json", str(bundle_json), "--out-md", str(bundle_md)]) == 0
    readiness_status = main(["public-readiness", "--root", str(ROOT), "--out-json", str(readiness_json), "--out-md", str(readiness_md)])

    assert "evaluation_commands" in bundle_json.read_text(encoding="utf-8")
    assert "Evidence Bundle" in bundle_md.read_text(encoding="utf-8")
    assert readiness_status in {0, 1}
    assert "public_scan" in readiness_json.read_text(encoding="utf-8")


def test_release_owner_promotion_pack_commands(tmp_path):
    adoption_json = tmp_path / "adoption.json"
    adoption_md = tmp_path / "adoption.md"
    scorecard_json = tmp_path / "scorecard.json"
    scorecard_md = tmp_path / "scorecard.md"
    deck_json = tmp_path / "deck.json"
    deck_md = tmp_path / "deck.md"
    export_json = tmp_path / "manifest.json"
    export_md = tmp_path / "manifest.md"

    assert main(["adoption-notes", "--root", str(ROOT), "--out-json", str(adoption_json), "--out-md", str(adoption_md)]) == 0
    assert main(["reviewer-scorecard", "--root", str(ROOT), "--out-json", str(scorecard_json), "--out-md", str(scorecard_md)]) == 0
    assert main(["release-deck", "--root", str(ROOT), "--out-json", str(deck_json), "--out-md", str(deck_md)]) == 0
    assert main(["bundle-export", "--root", str(ROOT), "--out-json", str(export_json), "--out-md", str(export_md)]) == 0

    assert '"version": "0.7.0"' in adoption_json.read_text(encoding="utf-8")
    assert "cold_user_next_actions" in adoption_json.read_text(encoding="utf-8")
    assert "maturity_mapping" in scorecard_json.read_text(encoding="utf-8")
    assert "Release Owner Promotion Deck" in deck_md.read_text(encoding="utf-8")
    assert '"export_root": "demo/bundle_export"' in export_json.read_text(encoding="utf-8")


def test_diff_check_detects_manifest_drift(tmp_path):
    source = tmp_path / "note.txt"
    source.write_text("before\n", encoding="utf-8")
    manifest_json = tmp_path / "manifest.json"
    manifest_json.write_text(
        json.dumps(
            {
                "artifacts": [
                    {
                        "path": "note.txt",
                        "bytes": source.stat().st_size,
                        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    assert main(["diff-check", "--root", str(tmp_path), "--manifest", str(manifest_json)]) == 0

    source.write_text("after\n", encoding="utf-8")

    assert main(["diff-check", "--root", str(tmp_path), "--manifest", str(manifest_json)]) == 1


def test_public_readiness_blocks_incomplete_tree(tmp_path):
    (tmp_path / "README.md").write_text("does not fetch live data connect to brokers recommend buys predict returns\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("dependencies = []\n", encoding="utf-8")

    assert main(["public-readiness", "--root", str(tmp_path)]) == 1


@pytest.mark.parametrize(
    ("argv", "output"),
    [
        (["build-packet"], "demo/thesis_packet.json"),
        (["compare-history"], "demo/history_comparison.json"),
        (["review-ledger"], "demo/review_ledger.json"),
        (["static-dashboard"], "demo/static_dashboard.html"),
        (["thesis-impact-brief"], "demo/thesis_impact_brief.json"),
        (["exposure-map"], "demo/exposure_map.json"),
        (["scenario-library"], "demo/scenario_library.json"),
        (["assumption-registry"], "demo/assumption_registry.json"),
        (["data-dictionary-diff"], "demo/data_dictionary_diff.json"),
        (["fixture-doctor"], "demo/fixture_doctor.json"),
        (["schema-export"], "demo/input_schema.json"),
        (["troubleshoot"], "demo/troubleshoot.json"),
        (["docs-export"], "demo/docs_export.json"),
        (["readme-snippet"], "demo/readme_snippet.json"),
        (["cli-help"], "demo/cli_help.json"),
        (["case-gallery"], "demo/case_gallery.json"),
        (["visual-receipt"], "demo/visual_receipt.json"),
        (["quickstart-check"], "demo/quickstart_check.json"),
        (["command-matrix"], "demo/command_matrix.json"),
        (["adoption-notes"], "demo/adoption_notes.json"),
        (["reviewer-scorecard"], "demo/reviewer_scorecard.json"),
        (["release-deck"], "demo/release_deck.json"),
        (["bundle-export"], "demo/bundle_export/manifest.json"),
        (["cold-start-walkthrough"], "demo/cold_start_walkthrough.json"),
    ],
)
def test_default_example_commands_work_from_empty_cwd(tmp_path, monkeypatch, argv, output):
    monkeypatch.chdir(tmp_path)

    assert main(argv) == 0

    assert (tmp_path / output).exists()


def test_missing_custom_event_path_stays_strict(tmp_path):
    assert main(["build-packet", "--root", str(tmp_path), "--events", "missing.csv"]) == 2


def test_missing_custom_case_path_stays_strict(tmp_path):
    assert main(["case-gallery", "--root", str(tmp_path), "--cases", "missing.csv"]) == 2
