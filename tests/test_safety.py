from pathlib import Path

from macro_policy_thesis_map.cli import main
from macro_policy_thesis_map.core import DISCLAIMER, public_findings, review_ledger


ROOT = Path(__file__).resolve().parents[1]


def test_disclaimer_sets_static_research_boundaries():
    lower = DISCLAIMER.lower()

    assert "not investment advice" in lower
    assert "does not fetch live data" in lower
    assert "connect to brokers" in lower
    assert "place orders" in lower
    assert "predict returns" in lower


def test_public_scan_passes_repo():
    assert main(["public-scan", "--root", str(ROOT)]) == 0


def test_public_scan_detects_private_terms(tmp_path):
    private_term = "api" + "_key"
    (tmp_path / "note.md").write_text(f"bad {private_term}\n", encoding="utf-8")

    assert public_findings(tmp_path) == [f"note.md contains {private_term}"]


def test_review_ledger_flags_advice_like_fixture_text():
    packet = {
        "policy_areas": [
            {
                "policy_area": "test-policy",
                "average_confidence": 0.9,
            }
        ],
        "evidence": [
            {
                "policy_area": "test-policy",
                "evidence": "This note says buy immediately",
                "thesis_link": "example",
            }
        ],
    }

    payload = review_ledger(packet, 0.55)

    assert payload["findings"][0]["severity"] == "blocker"
