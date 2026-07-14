# Workflow Protocol

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Protocol: `macro-policy-thesis-map.v1.3`

Purpose: Reusable local protocol for agents generating static macro-policy evidence maps.

## Phases

| Phase | Goal | Commands | Expected outputs | Gate |
| --- | --- | --- | --- | --- |
| inspect | Confirm local static inputs and public docs are present. | command-matrix --root ., schema-export --root ., fixture-doctor --root . | demo/command_matrix.json, demo/input_schema.json, demo/fixture_doctor.json | fixture-doctor status is pass before packet generation. |
| generate | Build the evidence packet and reusable public surfaces. | build-packet --root ., review-ledger --root ., example-pack --root ., api-reference --root . | demo/thesis_packet.json, demo/review_ledger.json, demo/example_pack.json, demo/api_reference.json | review-ledger has no blocker findings before sharing. |
| package | Prepare public visitor and agent reuse artifacts. | landing-page --root ., workflow-protocol --root ., roadmap-next --root ., evidence-bundle --root . | demo/landing_page.html, demo/workflow_protocol.json, demo/roadmap_next.json, demo/evidence_bundle.json | public-readiness can evaluate all required demo artifacts. |
| verify | Run local release gates and detect drift. | public-readiness --root ., release-manifest --root ., public-scan --root ., diff-check --root . | demo/public_readiness.json, demo/release_manifest.json, stdout pass/fail | selfcheck, public-scan, public-readiness, and diff-check exit successfully. |

## Agent Contract

| Field | Value |
| --- | --- |
| input_mode | static files only |
| output_root | demo/ |
| allowed_formats | Markdown, JSON, HTML, SVG |
| state_model | commands are deterministic and may be rerun from the repository root |
| handoff_files | demo/workflow_protocol.json, demo/api_reference.json, demo/example_pack.json, demo/public_readiness.json |

## Stop Conditions

| Condition |
| --- |
| Missing required static input files. |
| fixture-doctor reports blocked. |
| review-ledger reports advice-like text. |
| public-scan reports a private reference or credential-shaped token. |
| public-readiness reports blocked. |
