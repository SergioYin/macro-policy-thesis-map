# Operator Troubleshooting Guide

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.7.0

Status: ready

Reviews: 0 / 6

## Checks

| Check | Status | Symptom | Evidence | Resolution |
| --- | --- | --- | --- | --- |
| missing_required_file | pass | A command exits with a file-not-found error. | README.md, pyproject.toml, examples/macro_events.csv, demo/fixture_doctor.json, demo/command_matrix.json, demo/public_readiness.json, demo/release_manifest.json | Run from the repository root or pass --root with a directory containing the documented static files. |
| fixture_quality_blocker | pass | fixture-doctor returns blocked. | demo/fixture_doctor.json, examples/macro_events.csv | Fix missing columns, unsupported event types, invalid confidence values, stale dates, or advice-like terms in the static CSV. |
| public_readiness_blocker | ready | public-readiness returns blocked. | demo/public_readiness.json | Review the blockers list, regenerate missing demo artifacts, and keep README finance boundaries explicit. |
| manifest_drift | pass | diff-check reports hash drift. | demo/release_manifest.json | Regenerate changed demo artifacts, then run release-manifest followed by diff-check. |
| operator_docs_missing | pass | An evaluator cannot find command usage or docs surfaces. | demo/docs_export.json, demo/readme_snippet.json, demo/cli_help.json, demo/command_matrix.json | Run docs-export, readme-snippet, cli-help, and command-matrix from the repository root. |
| schema_adaptation_artifacts_missing | pass | A public evaluator cannot decide which CSV columns to keep or add. | demo/scenario_library.json, demo/assumption_registry.json, demo/data_dictionary_diff.json | Run scenario-library, assumption-registry, and data-dictionary-diff from the repository root. |

## Validation Commands

| Command |
| --- |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-readiness --root . |
| PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root . |
