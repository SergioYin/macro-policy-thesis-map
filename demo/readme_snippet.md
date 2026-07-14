# README Snippet

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 0.7.0

```bash
PYTHONPATH=src python -m macro_policy_thesis_map.cli fixture-doctor --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli build-packet --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli review-ledger --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli scenario-library --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli assumption-registry --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli data-dictionary-diff --root .
PYTHONPATH=src python -m macro_policy_thesis_map.cli troubleshoot --root .
PYTHONPATH=src python -B -m macro_policy_thesis_map.cli selfcheck --root .
```

## Expected Outputs

| Path |
| --- |
| demo/thesis_packet.md |
| demo/review_ledger.md |
| demo/scenario_library.md |
| demo/assumption_registry.md |
| demo/data_dictionary_diff.md |
| demo/troubleshoot.md |
