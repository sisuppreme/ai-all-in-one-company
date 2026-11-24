# UI/UX Upscaler — Spec 10: Regression & Rollback

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md` (§7). The plan the
> SKILL.md points to for keeping the upgrade safe.
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule:** the regression checklist includes the leak check — a
> pass that reintroduces a leak fails regression even if every flow is green
> (`09-architecture-leak.md` §5 checklist, item L-1–L-8).

## 1. Behaviour baseline freeze (before Pass 1 — nothing moves without it)

### 1.1 What the baseline contains

| Baseline item | How it is captured | Where it lives |
|---|---|---|
| Route inventory | Every route + its family (`01-audit-and-scoring.md` §2 §1 table); dead routes listed separately | Audit file §1 |
| Primary flows | The 3–6 flows the user actually completes (named, with steps): e.g. Northwind — filter, drill into an invoice, export the month, mark paid; Harbour — browse→detail, add to basket, checkout→confirmation; Fieldnote — change plan, invite member, toggle notification. Each flow has a scripted happy path + its error path. | Audit file §6 + `tests/regression/<flow>.md` (or the project's e2e suite) |
| Screenshots | Full-page screenshots at 1440×900 and 390×844 for every route family (before state) | `regression/baseline/<family>-1440.png`, `…-390.png` |
| Performance profile | Full-page scroll profile on a mid-range CPU-throttled (4×) profile per route family: longest task, total long-task time, frames >50 ms, plus Lighthouse scores | Audit file §5 evidence + `regression/baseline/<family>-profile.json` |
| API-call inventory | For each primary flow: the API calls it makes (method + path + shape, recorded from the network log — inward knowledge, never shown in the UI). The inventory is the tripwire: a pass that changes the calls has changed behaviour. | `regression/baseline/<flow>-api.json` |
| Console/network baseline | Console errors/warnings count per route (before); failed requests per flow (before). A pass that adds a console error has regressed, even if the UI looks right. | Audit file §5 evidence |
| Accessibility baseline | axe results per route family (critical/serious counts); keyboard-walk notes (traps, invisible focus). | Audit file §5 evidence |

### 1.2 Freeze rules

- The baseline is captured AFTER the audit and BEFORE Pass 1, on the audited commit
  (record the SHA in the audit file §0). Any code change between the audit and the
  baseline capture invalidates the baseline — re-capture it.
- During the upgrade, routes, data, APIs, and flow outcomes are FROZEN (Protocol
  Step 2). A change to any of them needs a justification written in the audit file
  before it is touched, and the baseline is re-captured for the affected flow.
- The baseline is not a suggestion: a pass whose verification cannot be compared
  against the baseline (because the baseline was never captured) has not been verified.

## 2. The regression checklist (run after EVERY pass — no exceptions)

Run in full after each of the 7 passes, per route family touched. A pass does not exit
until its checklist is green for every family it touched. The checklist is the same
every time — that is the point: a checklist that changes per pass cannot catch
regressions.

| # | Check | Method | Pass bar |
|---|---|---|---|
| R-1 | Primary flows still complete | Run every primary flow's scripted happy path (manual or e2e) | All flows complete with the same outcomes as baseline (same data, same confirmations) |
| R-2 | Primary flows' error paths still work | Run each flow's error path (invalid data, network off, server 5xx stubbed) | Error states appear per `04` §17 (user-concept message + next step + retry); no leaking strings (`09` §4.2) |
| R-3 | Forms | Every form in the touched families: submit valid, submit invalid, check each field's states (rest/focus/error/disabled) | Validation rules unchanged; error messages in user terms; no field lost its label or its error state |
| R-4 | Component states | Every component touched: render all 7 states (rest/hover/focus/active/disabled/loading/empty/error) at 1440 px and 390 px | Each state renders per its `04` spec; no state is blank, broken, or a browser default |
| R-5 | Console | Load every touched route; interact with every primary control | 0 console errors; 0 new console warnings vs baseline (warnings that pre-date the upgrade are listed in the baseline, not excused silently) |
| R-6 | Routes | Visit every route (including dead-route handling: 404 page, redirects) | Every route renders; 404/redirect behaviour unchanged; no route regressed to a blank page |
| R-7 | API calls | Record the network log for each primary flow; diff against the baseline inventory (§1.1) | Same calls, same order, same shape. Any difference = behaviour change — stop, justify in the audit, re-baseline the flow, or roll back |
| R-8 | Performance | Full-page scroll profile (same throttled profile as baseline) per touched family | No scroll-linked long task >50 ms; total long-task time ≤ baseline or ≤200 ms, whichever is lower; frames >50 ms = 0 (or fewer than baseline with a recorded reason) |
| R-9 | Screenshots | Full-page screenshots 1440 px + 390 px per touched family; diff against baseline (and against the previous pass) | Intended changes only. Any unintended pixel diff >0.5% of pixels is investigated, not assumed — an "intended" diff that was not in the pass plan is a regression |
| R-10 | Leak check | Ban-list grep over all user-facing strings touched + error-path strings (§4.2 of `09`) | 0 leaks. A leak found here fails the pass even if R-1–R-9 are green (`09` §1 veto) |
| R-11 | No-JS + reduced motion | Playwright no-JS load per touched route; reduced-motion emulation scroll | All content visible with JS off (G-FE-051); 0 continuing non-essential motion under emulation (G-FE-052) |
| R-12 | Keyboard walk | Tab through every touched route (keyboard only) | 0 traps; focus visible everywhere; focus never obscured by a pinned element (WCAG 2.4.11) |

### 2.1 Checklist evidence

Each run records: date, pass number, families touched, per-item result (PASS/FAIL +
evidence pointer — screenshot, log, profile file), and the name of the person/agent
who ran it. A checklist run with no evidence pointers is not a run. The runs accumulate
in the audit file §8 (or a `regression/runs/` log the audit file points to).

### 2.2 What a single FAIL means

Any FAIL blocks the pass's exit. The pass is fixed and the checklist re-run IN FULL
(not just the failed item — a fix for R-4 can break R-1, and only a full re-run catches
it). Two consecutive full-run failures on the same pass trigger §4 (rollback + re-plan).

## 3. Feature-flag / branch strategy

### 3.1 Branch

- The upgrade lives on its own branch (`upscale/<app>`) from the audit commit until
  the gate passes (`11-scoring-shipping.md` §4). Never upgrade on `main`. A
  half-upgraded `main` is unshippable by definition, and a half-upgraded `main` cannot
  be rolled back by flipping a flag (there is no flag — the code IS main).
- Branch hygiene: the branch rebases onto `main` at most once per pass (at the pass
  boundary, after the checklist is green). A rebase mid-pass invalidates the pass's
  verification — the checklist is re-run after any rebase.

### 3.2 Flags

- One flag per route family (`upscale.landing`, `upscale.dashboard`, `upscale.settings`, …)
  plus one flag per high-risk pass per family (Pass 5 motion: `upscale.motion.<family>`).
  Flags are boolean; record whether each is server- or build-time.
- Default OFF. A flag flips ON only when: that family's regression checklist (§2) is
  green AND its per-family gate score passes (`11` §1 — total ≥64/80 for the family,
  thresholds met, hard categories 10/10, leak score 0).
- Flags are REMOVED in the pass that follows their flip (the cleanup commit is part of
  the pass, not "later"). A flag older than 2 passes is a defect: the old code path is
  still shipped alongside the new one, and the regression checklist must now cover both
  paths — which is why the flag is removed instead.
- Flag OFF is the rollback (§4.1): flipping a flag off restores the old code path for
  that family without a deploy of old code. This only works if the old path is still
  present behind the flag — which is why flags are removed only AFTER the family has
  shipped green for a full pass, not at flip time.

### 3.3 Merge rule

Merge to `main` only when: the full-app gate is green (`11` §4 — total ≥64/80,
thresholds, hard categories 10/10, leak 0) AND the full regression checklist (§2) is
green on the branch AND the branch is rebased onto current `main` with the checklist
re-run after the rebase. A merge with a red item is not a merge — it is a rollback
waiting to happen on `main`, where rollback is ten times more expensive.

## 4. The rollback plan

### 4.1 Each pass records its inverse before it starts

Before Pass N starts, the audit file §6 records the pass's INVERSE — the exact steps
that undo it — in one paragraph per pass, written BEFORE the pass's first commit:

| Pass | Inverse (recorded before the pass starts) |
|---|---|
| P1 Tokens | Revert the token-file commits; restore hard-coded values from the Pass 1 tag (`upscale/pass-1-start`). The greps return to their BEFORE counts. |
| P2 Typography | Revert the scale commits; restore the old sizes from the tag. Contrast fixes are reverted with them (they are part of the pass, not separate). |
| P3 Layout | Revert the grid/pacing commits; restore the old layout from the tag. |
| P4 Components | Revert the component commits; restore the old components from the tag. Behaviour is unchanged either way (the pass is presentation-only), so the inverse is safe. |
| P5 Motion | Restore the old scroll handlers + the old cursor from the tag; delete the shared loop. (The inverse is recorded even though the cursor must never return: the inverse restores the PRE-UPGRADE state for diagnosis, and the re-plan then removes the cursor again properly — the inverse is a diagnostic step, not a shipping state.) |
| P6 Scroll | Revert the scroll-system commits; restore the old scroll behaviour from the tag. |
| P7 Polish | Delete the signature elements (they live in planned grid space; deleting them leaves the layout intact by design — an element whose deletion breaks the layout was never merged). |

The inverse is written before the pass starts because after the pass, the author knows
too much about the new code to write an honest undo. An inverse written after the fact
is a guess.

### 4.2 When to roll back (triggers)

- Two consecutive full checklist failures on the same pass (§2.2).
- A behaviour change discovered by R-7 (API-call diff) that cannot be justified in
  the audit file.
- A gate-category regression: a category that scored higher BEFORE the pass than after
  it (re-score per `11` §1 — a pass that makes a category worse has broken something).
- A leak introduced by the pass that cannot be fixed inside the pass (R-10 FAIL with
  no clean rewrite — see `09` §7: if no user-concept translation exists, the surface
  is removed, not shipped leaking).
- Any team member's "stop" — the upgrade stops at once on "stop" or "rehny dain"
  (standing rule, `dreams/alignment/derived/ALIGNMENT_SYNTHESIS.md`).

### 4.3 How to roll back (procedure)

1. Stop work on the pass. Do not write another commit on top of it.
2. Roll back to the pass's tag (`upscale/pass-N-start`) OR flip the family's flag OFF
   (§3.2) — tag-revert for a branch that has not shipped the family; flag-off for a
   family already live behind a flag. Record which was used.
3. Record the break in the audit file §8: what broke, the evidence (checklist item +
   screenshot/log), the pass's inverse as executed, and the re-plan (what changes
   before the pass is re-attempted — a different approach, a smaller scope, a
   dependency fixed first).
4. Re-plan, then re-attempt the pass from its tag. The re-attempt is a new pass
   attempt with its own checklist run — the failed attempt's checklist results do not
   carry over.

### 4.4 What never happens

- **Never patch forward** on top of a broken pass. A fix commit on top of a failed
  pass hides the break in the history and makes the next regression unbisectable.
  Roll back, re-plan, re-attempt.
- **Never delete the broken feature** to make the design easier (Protocol Step 2).
  If a feature breaks under the upgrade, the upgrade bends around the feature — the
  feature is fixed or the pass is re-planned; the feature is not deleted. A deleted
  feature is recorded in the audit file §7 (deliberately unchanged — no; deleted is
  worse: it is a behaviour change, and it needs a justification + approval before it
  happens, not after).
- **Never ship a known-broken pass** behind a flag "to fix later" (BAN-FE-163 — ship
  now, score later — applies to regression exactly as it applies to scores).

## 5. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 baseline freeze | `01-audit-and-scoring.md` §2 §6 (pass plan); `03` §1.4 (rollback point per pass) |
| §2 checklist | After EVERY pass (`03` §§2–8 exit criteria); `11` §4 (shipping checklist) |
| §3 branch/flags | `07-frameworks.md` §6 (incremental rollout) |
| §4 rollback | `03` §1.4; `08-case-studies.md` §§2.10/3.10/4.10 (regression evidence per study) |
