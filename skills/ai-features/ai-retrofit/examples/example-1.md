# Example 1 — The overnight inbox replacement, staged instead

> Hypothetical product: "HelpDesk Pro," a live support inbox used by a
> 14-person support team. All figures below are this scenario's recorded
> numbers, not industry statistics.

## Before

```text
Release plan (v4.2, one deploy, Monday 09:00):
  - Remove the manual triage queue (team picks a category + assignee).
  - All incoming tickets are auto-triaged by the model: category,
    priority, and assignee are written straight onto the ticket.
  - No feature flag. No cohort. Rollback = "redeploy v4.1 if it goes bad."
  - Success measure: "agents say it feels faster."
```

There is no record of how manual triage performed before the change, so
there is nothing to compare against. On the first morning a prompt
regression misroutes billing tickets to the technical queue; agents only
notice hours later from customer replies, and restoring manual triage
takes a full redeploy during business hours.

## After

**Step 1 — Record the baseline first (AI-201, G-AI-101).** For two weeks
before any AI code ships, the team records the manual flow: median
time-to-first-assignment, share of tickets re-triaged by a human within
one hour (the misroute proxy), tickets handled per agent per day, and the
manual category/assignee chosen for a fixed sample of 200 real tickets.
That sample becomes the comparison set for every later stage.

**Step 2 — Inventory the insertion points (AI-203).** Three candidates
are scored on value-if-right, harm-if-wrong, human review, and
reversibility:

| Insertion point | Human sees output first? | Reversible? | Decision |
|---|---|---|---|
| Suggested category + assignee shown to the agent, who confirms | Yes | Yes | Build first |
| Auto-assign low-risk password-reset tickets | No | Partly | Build last, only after stage data |
| Auto-reply to the customer | No | No | Not built |

**Step 3 — AI proposes, the agent disposes (AI-204).** The suggestion
appears in a panel on the existing ticket view, stored separately from
the ticket with model ID, prompt version, and timestamp. Clicking
"Apply" writes category and assignee through the same validated write
path manual triage always used; ignoring the panel changes nothing.

**Step 4 — Stage the rollout behind a kill switch (AI-209, AI-210,
AI-212).**

```text
Flag: ai_triage_suggest (server-side; per-cohort and per-insertion-point)
Stage 0: internal test workspace          — 1 week
Stage 1: 3 named volunteer agents         — 2 weeks
Stage 2: whole support team               — after G-AI-105 passes
Abort thresholds (written before Stage 1): misroute proxy > baseline +2 pts,
  fallback rate > 15%, or support contacts about triage up 2 days running
  → flag off, named owner: support lead on duty.
Cost: projected from measured volume (≈ scenario: 900 tickets/day × avg
  ticket length from real records); each stage carries its own spend
  ceiling, re-checked before widening (AI-210).
```

**Step 5 — Rehearse the rollback before Stage 1 (AI-212, G-AI-104).**
In staging, with suggestions already created, the flag is flipped off:
the panel disappears within the recorded target time, manual triage
serves every ticket, existing suggestions stay readable, and no ticket
record has changed. The end state is also named: graduate, extend, or
remove, with a decision date six weeks after Stage 2.

**Step 6 — Report pilot numbers as pilot numbers (AI-211).** The Stage 1
report is headed "3 volunteer agents, 2 weeks, suggestion panel only" —
its acceptance rate is never quoted as a team-wide or product-wide
result.

The non-AI path stays intact throughout (AI-202): with the flag off or
the provider failing, the regression suite still passes every
pre-existing triage task (G-AI-101).

## Note

Violates AI-202, AI-209, and AI-212 (BAN-AI-101, big-bang replacement of
a working flow). Corrected by recording the AI-201 baseline, keeping the
manual queue intact and tested, staging behind a server-side kill switch
with written abort thresholds and per-stage cost ceilings, and
rehearsing the rollback before the first external stage (G-AI-104,
G-AI-105).
