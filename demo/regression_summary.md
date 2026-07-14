# Regression Summary

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Status: needs-review

Gates: 9

Manual gates: 2

Blocking gates: 1

## Gates

| Gate | Status | Evidence | Detail |
| --- | --- | --- | --- |
| pytest_suite | manual | Run PYTHONPATH=src python -m pytest | Full test execution is recorded by the release operator. |
| selfcheck | pass | macro-policy-thesis-map selfcheck --root . | Required files and public scan findings are checked locally. |
| public_readiness | ready | demo/public_readiness.json | Public readiness gate summary. |
| release_manifest | pass | demo/release_manifest.json | Release artifact hashes are present. |
| golden_fixtures | ready | demo/golden_fixtures.json | Fixture schema and hash inventory. |
| trust_layer | needs-review | demo/evaluator_scorecard.json | Evaluator trust scorecard based on local artifacts. |
| governance_attestation_layer | ready | demo/boundary_attestation.json, demo/provenance_ledger.json, demo/reproducibility_recipe.json, demo/release_notes_draft.json | Governance layer records boundaries, provenance, reproducibility, and release notes. |
| evaluator_onboarding_layer | ready | demo/onboarding_checklist.json, demo/maintainer_handoff.json | Final onboarding and maintainer handoff artifacts are present. |
| wheel_build | manual | python -m build --wheel or build_backend.build_wheel | Offline wheel build should be run when build tooling is available. |

## Release Checks

| Command |
| --- |
| PYTHONPATH=src python -m pytest |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli evaluator-scorecard --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli boundary-attestation --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli provenance-ledger --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli reproducibility-recipe --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli release-notes-draft --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli onboarding-checklist --root . |
| PYTHONPATH=src python -m macro_policy_thesis_map.cli maintainer-handoff --root . |
