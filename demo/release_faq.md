# Release FAQ

Research-only static analysis. Not investment advice. This tool does not fetch live data, connect to brokers, place orders, recommend buys, sells, holds, target allocations, or trades, predict returns, or produce personalized financial advice.

Version: 1.5.0

Questions: 6

Ready: 6 / 6

| ID | Question | Answer | Local citations | Status |
| --- | --- | --- | --- | --- |
| faq-001 | What should a first-time GitHub visitor run first? | Run command-matrix, fixture-doctor, build-packet, and public-readiness from the repository root. | README.md, demo/command_matrix.md, demo/cold_start_walkthrough.md | ready |
| faq-002 | Does the project use live macro, market, or broker data? | No. The package reads static CSV inputs and bundled examples only. | README.md, demo/input_schema.md, demo/public_readiness.md | ready |
| faq-003 | How can an evaluator verify artifact drift? | Regenerate demo outputs, run release-manifest, then run diff-check against the saved manifest. | demo/release_manifest.md, demo/regression_summary.md | ready |
| faq-004 | Where are public claims linked to evidence? | Use citation-map for claim-to-artifact references and artifact-index for hashes and producer commands. | demo/citation_map.md, demo/artifact_index.md | ready |
| faq-005 | What is intentionally unsupported? | Live feeds, workflow automation, broker connections, trade actions, return predictions, and personalized financial advice. | README.md, demo/roadmap_next.md, skills/agent/macro-policy-thesis-map/SKILL.md | ready |
| faq-006 | Where is the governance and attestation layer? | Use boundary-attestation, provenance-ledger, reproducibility-recipe, release-notes-draft, onboarding-checklist, maintainer-handoff, and release-audit-summary for v1.5.0 final release evidence. | demo/boundary_attestation.md, demo/provenance_ledger.md, demo/reproducibility_recipe.md, demo/release_notes_draft.md, demo/release_audit_summary.md | ready |
