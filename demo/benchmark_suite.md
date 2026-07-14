# Public Evaluator Benchmark Suite

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.2.0

Suite type: static synthetic deterministic benchmarks

Ready: 4 / 4

## Benchmarks

| Benchmark | Name | Status | Commands | Expected artifacts | Deterministic assertion |
| --- | --- | --- | --- | --- | --- |
| bench-001 | default_packet_generation | ready | build-packet, review-ledger, fixture-doctor | demo/thesis_packet.json, demo/review_ledger.json, demo/fixture_doctor.json | Event count, policy-area count, and fixture-doctor status remain stable for bundled examples. |
| bench-002 | schema_adaptation_surfaces | ready | scenario-library, assumption-registry, data-dictionary-diff | demo/scenario_library.json, demo/assumption_registry.json, demo/data_dictionary_diff.json | Built-in synthetic metadata writes identical command counts and schema guidance across runs. |
| bench-003 | public_case_and_receipt | ready | case-gallery, visual-receipt | demo/case_gallery.json, demo/visual_receipt.json | Case routes, receipt command list, and artifact hash prefixes are derived from static local files. |
| bench-004 | release_readiness_pack | ready | maturity-report, evidence-bundle, public-readiness, regression-summary | demo/maturity_report.json, demo/evidence_bundle.json, demo/public_readiness.json, demo/regression_summary.json | Gate names and pass/block statuses are computed from local files only. |

## Run Policy

| Policy |
| --- |
| Benchmarks describe deterministic artifact expectations and do not measure wall-clock performance. |
| Use bundled static fixtures or user-supplied static CSVs only. |
| Treat any missing expected artifact as a regeneration task, not as a live-data fetch request. |
