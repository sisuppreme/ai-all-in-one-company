# UI/UX Upscaler — Spec 11: Scoring & Shipping

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md` (§8). The method the
> SKILL.md points to for re-scoring and shipping.
> **SCOPE: web apps ONLY** (native: adaptation note in `02-theme-decision.md` §8 only).
> **Architecture-leak rule:** the leak score is a gate FAIL veto regardless of the
> /80 score (`09-architecture-leak.md` §1, §5). A ship decision with a leak is not a
> ship decision — it is a vetoed decision, and the report says so.

## 1. Re-score method (same gate, same widths, same eight categories)

### 1.1 Sameness rules (the re-score must be comparable to the BEFORE score)

| Dimension | BEFORE (audit) | AFTER (re-score) | Rule |
|---|---|---|---|
| Instrument | design-intelligence §5, 8 categories 0–10, total /80 | Same instrument, same anchors (`01-audit-and-scoring.md` §5.2) | A different instrument produces a different number — the movement is meaningless. Never "improve" the anchors between BEFORE and AFTER. |
| Widths | 1440 px and 390 px (+ 1280/768/360 spot checks) | Same widths, same spot checks | A category scored at a different width is not the same measurement. |
| Hard categories tested directly | Cat. 6 (JS disabled), Cat. 7 (reduced-motion emulation) | Same direct tests, not inference | Cat. 6 is scored from the JS-off load test (G-FE-051) + observer-stub test (G-FE-056). Cat. 7 is scored from the reduced-motion emulation pass (G-FE-052). A hard category scored by "looking at the code" is unscored. |
| Scorer stance | Hostile reviewer (FE-329) | Same stance, same anchors | Self-critique drifts generous: a category argued up from a 6 to an 8 without a change is a 6 (design-intelligence anti-pattern). The AFTER score is earned by changes, not by re-reading. |
| Evidence | Screenshot pair / measurement / test output per category | Same evidence standard per category | A category re-scored without new evidence (new screenshots, new measurements, new test outputs) carries its BEFORE score forward — it does not move. |
| Roll-up | App-level = LOWEST family score (`01` §5.3) | Same roll-up | Averaging hides the worst page. The lowest family is the app's score. |

### 1.2 When to re-score

- **Per-pass re-score (light):** after each pass, re-score ONLY the categories that
  pass is the main lever for (`03` §§2–8 name them per pass — e.g. Pass 2 re-scores
  Cat. 3; Pass 5 re-scores Cat. 4 and Cat. 6). The light re-score is a progress signal,
  not a gate result — it is recorded in the audit file §8 with the date and the
  evidence, and it never replaces the full re-score.
- **Full re-score (gate):** after Pass 7, re-score ALL 8 categories, ALL families, in
  full. Pre-fix scores are void (design-intelligence §5). The full re-score is the
  gate result.
- **Loop re-score:** if the gate fails, fix the lowest-scoring category first, then
  re-score the WHOLE app again (all 8 categories, all families). A loop that re-scores
  only the fixed category is not a re-score — the fix may have moved another category,
  and only a full re-score catches it. Loop iterations are recorded in the audit file
  §8 (pass, category fixed, before/after per category, date) — see `03` §9.

### 1.3 Per-category BEFORE → AFTER movement recording

Record per category, in the audit file §8:

| Category | BEFORE | AFTER | Δ | Evidence (AFTER) | Pass(es) that moved it |
|---|---|---|---|---|---|
| 1. Hierarchy & focal order | 4 | 8 | +4 | screenshots hierarchy-after-1440.png / -390.png; 3-second test passes 3/3 | P2, P3 |
| … | | | | | |

Rules: Δ is AFTER − BEFORE (signed, never absolute). A Δ of 0 must say why (already at
threshold, or its lever pass recorded as out-of-scope — which then appears in §3's
deliberately-unchanged list with a reason). A negative Δ is a regression: stop, find
the pass that caused it, and roll back per `10-regression-rollback.md` §4. A Δ larger
than +4 in one category is flagged for review — a 6-point jump usually means the
BEFORE score was wrong (scored generously) or the AFTER score is wrong (scored
kindly); re-score that category from its evidence before accepting it.

## 2. The before/after report template

The report closes the audit file (`01` §2 §8) and is the reply to the user (Protocol
Step 7). Write it in this section order; no section may be omitted.

```markdown
# UI Upgrade Report — <Product name> — <YYYY-MM-DD>

## 0. Verdict [REQUIRED]
- GATE: PASS | FAIL — <one line: total, hard categories, leak score>
- BEFORE <X>/80 → AFTER <Y>/80 (arithmetic shown for both totals)
- Leak score BEFORE <N> → AFTER <M> / target 0 — veto: CLEAR | ACTIVE
- Shipped: YES (commit <SHA>, branch merged <date>) | NO — <reason>

## 1. Defects by class, with counts [REQUIRED]
| Class (01 §3) | Found | Fixed | Left (with reason — see §4) |
| AI-slop instances (S-1–S-19) | <N> | <N> | <N> |
| Missing systems (§3.2) | <N> | <N> | <N> |
| Hard-rule violations (§3.3) | <N> | <N> | <N> |
| Architecture leaks (09 §3) | <N> | <N> | 0 (any number >0 here = gate FAIL — see §0 veto) |
| TOTAL | <N> | <N> | <N> |
- Defect IDs fixed: <list or pointer to audit §2 with statuses>
- Defect IDs left: <list — each must appear in §4 with a reason>

## 2. Passes applied [REQUIRED]
| Pass | Routes/families | Checklist (§10 §2) | Category movement |
| 1 Tokens | all | green <date> | — |
| 2 Typography | all | green <date> | Cat. 3: 6→9 |
| … 7 rows … | | | |
- Rollbacks during the upgrade: <N> — each with its audit §8 record (what broke, inverse executed, re-plan). Zero rollbacks is reported as "0 — no pass required rollback", not omitted.

## 3. Score movement [REQUIRED]
- Per-category table (§1.3 — all 8 rows, BEFORE/AFTER/Δ/evidence/passes).
- Per-family table: each family's BEFORE → AFTER (the app-level score is the lowest family — name it).
- Hard categories tested directly: Cat. 6 — JS-off load <result + evidence>; observer-stub <result>; Cat. 7 — reduced-motion emulation <result + evidence>.
- Loop iterations (if any): <N> — each with the category fixed and the re-score result.

## 4. Deliberately-unchanged items [REQUIRED — see §3 below]
| Item | Reason it stays | Re-check date |
- (Every item here has a reason. An item without a reason fails the gate — see §3.)

## 5. Regression evidence [REQUIRED]
- Regression checklist runs: <N> runs (one per pass per family) — all green, evidence pointers in audit §8 / regression/runs/.
- Baseline comparison: flows <N>/<N> green; API calls unchanged (diff empty); console 0 errors; performance profile AFTER (longest scroll task <X> ms vs baseline <Y> ms).
- Screenshots: before/after pairs 1440 px + 390 px per family — <location>.

## 6. What was upgraded, in plain language [REQUIRED — the reply to the user]
- <3–6 bullets: what changed, the before/after score, what (if anything) was left and why. No claim of "premium" without the score (Protocol Step 7).
```

## 3. What "left unchanged" requires (a reason, or the gate fails)

- **Every item left unchanged needs a reason.** The reason must be one of: (a) behaviour
  freeze — the item works and the upgrade is presentation-layer first (Protocol Step 2);
  (b) out of scope — the item was ruled out before Pass 1 with a recorded scope decision;
  (c) commercial/regulated fact — prices, charge dates, regulated copy (the upgrade
  presents them, it does not renegotiate them); (d) risk — changing it risks the data
  or the flow, and the risk is named (not "it's risky" — WHAT breaks, with the evidence).
  "Ran out of time", "didn't get to it", and "looked fine" are not reasons — an item
  left for one of those is an unfinished defect, not a deliberate choice, and the gate fails.
- **A defect left unfixed without a reason is a failed close-out** (`01` §7). The audit
  file says so, the report says so, and the gate is FAIL until the defect is fixed or
  given a reason from the list above.
- **Leaks are never "left unchanged".** A leak left in place is a gate FAIL veto (`09`
  §1) — there is no reason category that covers a leak. If a leak cannot be fixed
  inside the upgrade, the surface that leaks is removed (`09` §6 rewrite rule) — the
  report records the removal, not the leak.
- **Re-check dates:** every deliberately-unchanged item carries a re-check date (≤90 days).
  An unchanged item with no re-check date is an item abandoned, not an item decided.

## 4. The shipping checklist

All items must be green. One red item blocks shipping — there is no "ship with a known
red item" path (BAN-FE-163).

- [ ] Full re-score green: total ≥64/80, every category at/above threshold, hard
  categories (6, 7) at 10 — with the arithmetic shown and the evidence attached (§1).
- [ ] Leak veto clear: leak score AFTER = 0 (`09` §5 checklist, all 8 items pass).
- [ ] Defect list closed: every defect fixed OR in §4 with a reason from §3's list
  (defects by class table, §2 §1, reconciles: found = fixed + left).
- [ ] Regression checklist green on the branch (`10` §2 — full run after the final
  pass, plus a re-run after the final rebase onto `main`).
- [ ] Branch hygiene: upgrade branch rebased onto current `main`; flags for shipped
  families removed or scheduled for removal in the next pass with a date (§10 §3.2).
- [ ] No-JS + reduced-motion passes green (G-FE-051, G-FE-052, G-FE-056 — test outputs
  attached, not asserted).
- [ ] Scroll profile green on a mid-range throttled profile with all signature elements
  running (longest scroll task ≤50 ms; total long-task time ≤200 ms on a full scroll).
- [ ] Screenshots: before/after pairs 1440 px + 390 px per family, reviewed (not just
  captured — a pair nobody looked at is not evidence).
- [ ] Audit file closed: §8 completed (AFTER table, defects fixed N/M, regression
  evidence, sign-off line) — the sign-off is either a pass or an explicit non-sign
  with a reason, never a soft pass.
- [ ] User reply drafted (§2 §6): what was upgraded, the before/after score, what was
  left and why. No claim of "premium" without the score.

## 5. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 re-score method | `01-audit-and-scoring.md` §5 (the instrument); `03` §9 (gate loop) |
| §2 report template | `01` §2 §8 (audit close-out); Protocol Step 7 (report) |
| §3 left-unchanged | `01` §7 (closing the audit); `08-case-studies.md` §§2.9/3.9/4.9 |
| §4 shipping checklist | `10-regression-rollback.md` §3.3 (merge rule) |
