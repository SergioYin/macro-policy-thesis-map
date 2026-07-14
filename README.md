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
PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli docs-export --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli readme-snippet --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli cli-help --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli static-dashboard --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli thesis-impact-brief --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli exposure-map --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli case-gallery --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli visual-receipt --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli release-manifest --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli maturity-report --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli quickstart-check --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli command-matrix --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli adoption-notes --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli reviewer-scorecard --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli release-deck --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli bundle-export --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli cold-start-walkthrough --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli evidence-bundle --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli public-readiness --root .
PYTHONPATH=src python -B -m macro_policy_thesis_map.cli public-scan --root .
PYTHONPATH=src python -B -m macro_policy_thesis_map.cli diff-check --root .
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
macro-policy-thesis-map troubleshoot
macro-policy-thesis-map docs-export
macro-policy-thesis-map readme-snippet
macro-policy-thesis-map cli-help
macro-policy-thesis-map static-dashboard
macro-policy-thesis-map thesis-impact-brief
macro-policy-thesis-map exposure-map
macro-policy-thesis-map case-gallery
macro-policy-thesis-map visual-receipt
macro-policy-thesis-map quickstart-check
macro-policy-thesis-map command-matrix
macro-policy-thesis-map adoption-notes
macro-policy-thesis-map reviewer-scorecard
macro-policy-thesis-map release-deck
macro-policy-thesis-map bundle-export
```

The installed CLI uses bundled example CSVs for default event, case, sensitivity, and exposure inputs when `examples/macro_events.csv`, `examples/prior_macro_events.csv`, `examples/public_macro_cases.csv`, `examples/thesis_sensitivities.csv`, and `examples/portfolio_exposures.csv` are not present in the current `--root`. Pass `--events`, `--current`, `--prior`, `--cases`, `--sensitivities`, or `--exposures` to use your own static CSVs. `selfcheck` and `diff-check` validate the source tree and should be run from a project checkout.

## Boundaries

This project is research tooling only. It does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice. Reports are based only on static files provided by the user.

## Demo Links

- `demo/thesis_packet.md` and `demo/thesis_packet.json`
- `demo/history_comparison.md` and `demo/history_comparison.json`
- `demo/review_ledger.md` and `demo/review_ledger.json`
- `demo/fixture_doctor.md` and `demo/fixture_doctor.json`
- `demo/input_schema.md` and `demo/input_schema.json`
- `demo/troubleshoot.md` and `demo/troubleshoot.json`
- `demo/docs_export.md` and `demo/docs_export.json`
- `demo/readme_snippet.md` and `demo/readme_snippet.json`
- `demo/cli_help.md` and `demo/cli_help.json`
- `demo/static_dashboard.html`
- `demo/thesis_impact_brief.md` and `demo/thesis_impact_brief.json`
- `demo/exposure_map.md` and `demo/exposure_map.json`
- `demo/case_gallery.md` and `demo/case_gallery.json`
- `demo/visual_receipt.md`, `demo/visual_receipt.json`, `demo/visual_receipt.svg`, and `demo/visual_receipt.html`
- `demo/release_manifest.md` and `demo/release_manifest.json`
- `demo/maturity_report.md` and `demo/maturity_report.json`
- `demo/quickstart_check.md` and `demo/quickstart_check.json`
- `demo/command_matrix.md` and `demo/command_matrix.json`
- `demo/adoption_notes.md` and `demo/adoption_notes.json`
- `demo/reviewer_scorecard.md` and `demo/reviewer_scorecard.json`
- `demo/release_deck.md` and `demo/release_deck.json`
- `demo/bundle_export/manifest.md` and `demo/bundle_export/manifest.json`
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

Run `troubleshoot`, `docs-export`, `readme-snippet`, and `cli-help` when handing the project to an operator or reviewer who needs deterministic support surfaces under `demo/`. These commands only read local files and built-in command metadata; they do not fetch data, publish content, create workflow files, or perform broker or trading actions.

The public case gallery uses a separate synthetic fixture:

```text
case_id,region,case_title,date,policy_area,channel,direction,confidence,evidence,route,command
```

The bundled gallery fixture includes US, EU, and Asia examples. These rows are public-safe examples for exercising routes, commands, and visual receipt hashes; they are not live macro data and are not financial recommendations.

The static thesis sensitivity fixture uses:

```text
thesis_id,policy_area,sensitivity_axis,shock_label,impact_direction,impact_score,confidence,rationale
```

The static portfolio exposure fixture uses:

```text
portfolio_id,sleeve,exposure_id,policy_area,thesis_id,exposure_direction,exposure_score,rationale
```

The bundled sensitivity and exposure rows are synthetic. `impact_score` and `exposure_score` are descriptive static scores from `0` to `1`; they are not live risk measures, allocation targets, trade instructions, or recommendations.

## Commands

- `build-packet`: creates the primary JSON and Markdown thesis map.
- `compare-history`: compares bundled current and prior event files.
- `review-ledger`: flags low-confidence or advice-like text in static inputs.
- `fixture-doctor`: validates static CSV fixtures for columns, event types, confidence bounds, stale dates, and advice-like terms.
- `schema-export`: writes the machine-readable input schema and data dictionary.
- `troubleshoot`: writes deterministic operator checks, symptoms, evidence paths, and recovery steps.
- `docs-export`: writes an operator documentation index with hashes for key docs and support artifacts.
- `readme-snippet`: writes a compact README-ready quickstart snippet with static research boundaries.
- `cli-help`: writes deterministic command usage lines and safety posture.
- `static-dashboard`: writes a no-JavaScript HTML dashboard.
- `thesis-impact-brief`: writes a deterministic Markdown/JSON brief for synthetic thesis sensitivities.
- `exposure-map`: writes a deterministic Markdown/JSON map from synthetic exposure rows to thesis sensitivity coverage.
- `case-gallery`: writes a public-safe multi-region case gallery as Markdown and JSON.
- `visual-receipt`: writes a static SVG or HTML receipt plus JSON/Markdown receipt metadata.
- `release-manifest`: records artifact paths, sizes, and hashes.
- `selfcheck`: checks required files, boundaries, and public-scan status.
- `public-scan`: scans publishable text for private names, private paths, and credential-shaped terms.
- `diff-check`: compares the saved release manifest against current file hashes.
- `maturity-report`: scores release readiness evidence.
- `quickstart-check`: verifies first-evaluator source files and starter command outputs.
- `command-matrix`: publishes command inputs, outputs, purposes, and safety posture.
- `adoption-notes`: writes release-owner public adoption notes, release commands, artifact hashes, cold-user next actions, and safety boundaries.
- `reviewer-scorecard`: maps maturity/readiness evidence to a public reviewer rubric with artifact hashes.
- `release-deck`: writes a deterministic Markdown/JSON promotion deck for release owners.
- `bundle-export`: writes a deterministic bundle manifest under `demo/bundle_export`.
- `evidence-bundle`: collects public evaluation artifact hashes and focused check commands.
- `public-readiness`: summarizes release-readiness gates and blockers.
- `cold-start-walkthrough`: writes a deterministic first-run walkthrough for public evaluators.
