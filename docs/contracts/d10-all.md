# Contract: D10 ↔ ALL — Project Memory

- **Backbone link:** #10 of 13 (MASTER_BRIEF.md §3.11) — fan-out
- **Link type:** SHARES
- **Owner department:** D10 Project Memory
- **Consumer departments:** ALL (D1–D9, D11–D18) — every department writes and reads
- **Liaisons:** D10 Major Lead (single liaison); each consuming department names one contact in its Phase 2 deliverable map
- **Skills on the owner side:** project-templates, progress-tracking, decision-logs, handover (D10)

## Artifact that passes

The project file set (`PROJECT_FILES.md` set): `requirements.md` (what is being
built and why), `progress.md` (state, gate results, next step), `stack.md` (the
chosen stack and its reasons), and `DECISIONS.md` (the decision index; full records
in docs/adr/). D10 owns the templates and the discipline; every department authors
its own entries.

## Format

Markdown, per the project-templates skill. Entries are dated; decisions are
append-only (an accepted record is immutable except its status); progress.md
states current facts, not aspirations — planned work is marked as planned.

## When it passes

Continuously, and as a hard checkpoint at every phase close and every handover:
no phase closes on stale project files.

## Acceptance test (how the receiver verifies)

**Joint gate — docs.** Before relying on the files, the receiving side checks:
progress.md's last entry is from the current work session; every shipped artifact
named in progress.md exists at the path given; every decision referenced in the
work appears in DECISIONS.md. The handover skill's PRR-style check applies at
handover: a named accepting owner and an explicit landmines list.

## If the test fails

The files are brought current before further build work. Work performed against
stale project files is re-verified against the corrected record — the files are
the project's memory, and a wrong memory silently corrupts every later step.
