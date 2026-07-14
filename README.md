# macro-policy-thesis-map

Zero-dependency Python CLI for turning static macro policy notes into neutral thesis evidence packets.

Target users: analysts, reviewers, and research engineers who need reproducible policy-to-thesis maps from user-supplied static files.

## Quickstart

```bash
PYTHONPATH=src python -m macro_policy_thesis_map.cli build-packet --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli compare-history --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli review-ledger --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli fixture-doctor --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli schema-export --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli static-dashboard --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli release-manifest --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli maturity-report --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli quickstart-check --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli command-matrix --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli cold-start-walkthrough --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli evidence-bundle --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli public-readiness --root .
PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .
PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .
```

Installed usage:

```bash
python -m pip install .
mkdir /tmp/macro-policy-demo && cd /tmp/macro-policy-demo
macro-policy-thesis-map build-packet
macro-policy-thesis-map compare-history
macro-policy-thesis-map review-ledger
macro-policy-thesis-map fixture-doctor
macro-policy-thesis-map schema-export
macro-policy-thesis-map static-dashboard
macro-policy-thesis-map quickstart-check
macro-policy-thesis-map command-matrix
```

The installed CLI uses bundled example CSVs for default event inputs when `examples/macro_events.csv` and `examples/prior_macro_events.csv` are not present in the current `--root`. Pass `--events`, `--current`, or `--prior` to use your own static CSVs. `selfcheck` validates the source tree and should be run from a project checkout.

## Boundaries

This project is research tooling only. It does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice. Reports are based only on static files provided by the user.

## Demo Links

- `demo/thesis_packet.md` and `demo/thesis_packet.json`
- `demo/history_comparison.md` and `demo/history_comparison.json`
- `demo/review_ledger.md` and `demo/review_ledger.json`
- `demo/fixture_doctor.md` and `demo/fixture_doctor.json`
- `demo/input_schema.md` and `demo/input_schema.json`
- `demo/static_dashboard.html`
- `demo/release_manifest.md` and `demo/release_manifest.json`
- `demo/maturity_report.md` and `demo/maturity_report.json`
- `demo/quickstart_check.md` and `demo/quickstart_check.json`
- `demo/command_matrix.md` and `demo/command_matrix.json`
- `demo/evidence_bundle.md` and `demo/evidence_bundle.json`
- `demo/public_readiness.md` and `demo/public_readiness.json`
- `demo/cold_start_walkthrough.md` and `demo/cold_start_walkthrough.json`

## Input Format

Event CSV files use:

```text
date,event_type,source,policy_area,channel,direction,confidence,evidence,thesis_link
```

Allowed `event_type` values are `policy_signal`, `macro_observation`, `market_context`, and `thesis_note`. Confidence is a decimal from `0` to `1`. The CLI does not validate whether a policy view is correct; it only organizes supplied evidence and flags static review issues.

Run `fixture-doctor` before generating release artifacts to validate required columns, allowed event types, confidence bounds, stale source dates, and advice-like terms. Run `schema-export` to produce a machine-readable schema and data dictionary under `demo/input_schema.json`.

## Commands

- `build-packet`: creates the primary JSON and Markdown thesis map.
- `compare-history`: compares bundled current and prior event files.
- `review-ledger`: flags low-confidence or advice-like text in static inputs.
- `fixture-doctor`: validates static CSV fixtures for columns, event types, confidence bounds, stale dates, and advice-like terms.
- `schema-export`: writes the machine-readable input schema and data dictionary.
- `static-dashboard`: writes a no-JavaScript HTML dashboard.
- `release-manifest`: records artifact paths, sizes, and hashes.
- `selfcheck`: checks required files, boundaries, and public-scan status.
- `public-scan`: scans publishable text for private names, private paths, and credential-shaped terms.
- `maturity-report`: scores release readiness evidence.
- `quickstart-check`: verifies first-evaluator source files and starter command outputs.
- `command-matrix`: publishes command inputs, outputs, purposes, and safety posture.
- `evidence-bundle`: collects public evaluation artifact hashes and focused check commands.
- `public-readiness`: summarizes release-readiness gates and blockers.
- `cold-start-walkthrough`: writes a deterministic first-run walkthrough for public evaluators.
