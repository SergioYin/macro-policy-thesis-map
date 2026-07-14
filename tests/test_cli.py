from pathlib import Path

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
    assert main(["release-manifest", "--root", str(ROOT), "--out-json", str(manifest_json), "--out-md", str(manifest_md)]) == 0
    assert main(["maturity-report", "--root", str(ROOT), "--out-json", str(maturity_json), "--out-md", str(maturity_md)]) == 0
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
        (["quickstart-check"], "demo/quickstart_check.json"),
        (["command-matrix"], "demo/command_matrix.json"),
        (["cold-start-walkthrough"], "demo/cold_start_walkthrough.json"),
    ],
)
def test_default_example_commands_work_from_empty_cwd(tmp_path, monkeypatch, argv, output):
    monkeypatch.chdir(tmp_path)

    assert main(argv) == 0

    assert (tmp_path / output).exists()


def test_missing_custom_event_path_stays_strict(tmp_path):
    assert main(["build-packet", "--root", str(tmp_path), "--events", "missing.csv"]) == 2
