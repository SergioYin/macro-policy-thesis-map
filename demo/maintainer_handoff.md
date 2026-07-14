# Maintainer Handoff

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.4.0

Status: ready

Policy: Maintain local deterministic public artifacts only; do not introduce dependencies, private systems, workflows, live finance feeds, or advice.

Custody: 7

Missing: 0

## Responsibilities

| Area | Owner action | Evidence |
| --- | --- | --- |
| versioning | Keep pyproject.toml, package __version__, README, skill protocol, tests, and generated artifacts synchronized. | pyproject.toml, src/macro_policy_thesis_map/__init__.py, demo/compatibility_report.json |
| artifact custody | Regenerate onboarding, handoff, evidence, readiness, release notes, and manifest files after source changes. | demo/onboarding_checklist.json, demo/maintainer_handoff.json, demo/release_manifest.json |
| finance boundary | Reject live data, workflow automation, broker actions, trade instructions, forecasts, and personalized advice. | README.md, demo/boundary_attestation.json, demo/public_readiness.json |
| release gates | Run pytest, selfcheck, public-scan, public-readiness, diff-check, and wheel build before release handoff. | demo/regression_summary.json, demo/reproducibility_recipe.json |

## Release Gates

| Command |
| --- |
| PYTHONPATH=src python -m pytest |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
| python -c "import build_backend; build_backend.build_wheel('dist')" |

## Artifact Custody

| Path | Status | Bytes | SHA-256 prefix |
| --- | --- | --- | --- |
| README.md | present | 20213 | bd9e1705b4ad4609 |
| skills/agent/macro-policy-thesis-map/SKILL.md | present | 4775 | 6414e2bbb4630894 |
| demo/maintainer_guide.json | present | 2594 | 23c3bcd8b3958d2a |
| demo/onboarding_checklist.json | present | 2593 | e3944b057ecfcc8b |
| demo/public_readiness.json | present | 2471 | d45135eba9e8effb |
| demo/evidence_bundle.json | present | 19080 | 1396ff6300e90c74 |
| demo/regression_summary.json | present | 3389 | 55721620ea052ddc |
