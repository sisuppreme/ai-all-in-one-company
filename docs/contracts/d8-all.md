# Contract: D8 → ALL — QA Gates

- **Backbone link:** #9 of 13 (MASTER_BRIEF.md §3.11) — fan-out
- **Link type:** VERIFIES
- **Owner department:** D8 QA & Testing
- **Consumer departments:** ALL (D1–D7, D9–D18)
- **Liaisons:** D8 Major Lead (single liaison); each consuming department names one contact in its Phase 2 deliverable map
- **Skills on the owner side:** qa-gates, test-strategy, placeholder-scan (D8)

## Artifact that passes

The gate set itself: every skill's Gates section (gate ID, rule IDs verified,
exact check, pass criterion, fail action), plus the gate *results* each project
records in progress.md. D8 owns the gate discipline — gates are mechanical,
exit-code-based commands committed before the work they judge.

## Format

Gates live in the owning skills in the §5.4 format. Results live in the project's
progress.md: gate ID, command run, exit result, date. A gate with no recorded
result did not run.

## When it passes

At every department's definition of done, at every playbook gate step, and at
release. Gates are defined before the work they judge — a gate written after
the output exists is advisory only and cannot certify it.

## Acceptance test (how the receiver verifies)

**Joint gate — QA.** The consuming department runs every gate its loaded skills
define and records the results. D8's discipline checks the checks: seeded-fault
negative controls prove the gates can fail (a gate that has never failed is
suspect), thresholds are never loosened in the same change that fails them,
and waivers are dated records, not edits. A gate that cannot run in the current
environment is recorded as failed with the reason — never skipped silently.

## If the test fails

Shipment blocks for BLOCK-severity gates. The owning department fixes the output
or the underlying rule — it does not edit the gate to pass. Rework cycles are
recorded in WORKFLOW.md per §3.8 rule 5.
