# Findability Test — Phase 6 (Formal, §5.3)

**Tester:** fresh Phase 6 test agent (did not build this repo).
**Method:** BOOTSTRAP.md read first, then SKILLS_INDEX.md scanned by department section + Keywords + Use-when lines. No SKILL.md file was opened before all 10 first choices below were committed in writing. Scoring (Part 2) was done only after this commitment, by opening each chosen skill's own "When to use" line and judging strictly whether that skill owns the task.
**Pass bar:** 9/10 correct first choices; tasks span ≥6 departments.

---

## Part 1 — Committed first choices (index only, before any SKILL.md was opened)

| # | Task | First-choice skill | Path | Dept |
|---|------|--------------------|------|------|
| T1 | A checkout page must stop losing buyers on mobile — find and fix the friction. | `forms` | `skills/frontend/forms/SKILL.md` | D3 |
| T2 | Set up error tracking and alerting for a production API before launch. | `error-tracking` | `skills/analytics-observability/error-tracking/SKILL.md` | D12 |
| T3 | Write the public changelog and release notes for version 2.0 of a developer tool. | `changelog` | `skills/project-memory/changelog/SKILL.md` | D10 |
| T4 | A SaaS needs per-tenant data isolation reviewed before onboarding enterprise customers. | `tenant-isolation` | `skills/database/tenant-isolation/SKILL.md` | D5 |
| T5 | Prepare a site to be acquired: organize the codebase documentation for due diligence. | `handover` | `skills/project-memory/handover/SKILL.md` | D10 |
| T6 | Add passkeys / WebAuthn login to an existing web app. | `backend-auth` | `skills/backend/backend-auth/SKILL.md` | D4 |
| T7 | Reduce the cloud bill: find waste in a Kubernetes deployment. | `cloud-costs` | `skills/devops-deployment/cloud-costs/SKILL.md` | D6 |
| T8 | A landing page's hero section looks generic and AI-made — diagnose why and fix the design. | `design-system` | `skills/frontend/design-system/SKILL.md` | D3 |
| T9 | Handle a GDPR data-deletion request correctly across backups and logs. | `dsar-handling` | `skills/legal-privacy/dsar-handling/SKILL.md` | D14 |
| T10 | Make a React app's long list scroll at 60fps. | `performance-optimization` | `skills/analytics-observability/performance-optimization/SKILL.md` | D12 |

**Departments spanned by first choices:** D3, D4, D5, D6, D10, D12, D14 = **7 departments** (bar: ≥6).

### Index-only reasoning notes (recorded at commitment time)

- **T1 → forms:** the index entry for `forms` names checkout explicitly ("building or reviewing any form — signup, checkout, settings, search-with-filters, multi-step flows — its labels, validation, error handling, and submission behavior"). Checkout friction on mobile is a form-behavior problem first; `layout-responsive` (mobile view squeezed) was the runner-up.
- **T2 → error-tracking:** the task names error tracking first; `error-tracking` owns capturing/grouping/triaging errors and feeds `alerting`. `alerting` owns the paging policy on top of the signals/issues error-tracking produces.
- **T3 → changelog:** `changelog` owns CHANGELOG.md for a release; its own index entry states release notes are written *from* the changelog, so the changelog skill owns the combined deliverable.
- **T4 → tenant-isolation:** "per-tenant **data** isolation reviewed" — `tenant-isolation` covers any table, query, job, or cache key touching tenant-owned data. `multitenancy-saas` (D2) was the runner-up; it owns choosing/auditing the isolation *model* at architecture level, while this task reads as enforcement-level review of the data layer.
- **T5 → handover:** acquisition = project changes hands; `handover` runs the readiness review and acceptance test that close a transfer, which is what due-diligence documentation prep is.
- **T6 → backend-auth:** "implementing … login … anywhere the system must prove who a caller is" is `backend-auth`'s stated ownership. `auth-hardening` (D7, incl. MFA enrolment) was the runner-up. **Noted at commitment time: no index entry anywhere contains the keyword "passkey" or "WebAuthn"** — routing depended entirely on the generic word "login".
- **T7 → cloud-costs:** the task is a bill/waste problem; `cloud-costs` owns spend and "optimisation" work, and `scaling`/`kubernetes` both feed into it. `kubernetes` owns running workloads, not their cost.
- **T8 → design-system:** `design-system`'s index entry explicitly claims "§3 diagnosis and CV cures" and reviewing a page for "monotony, drift, invented proof" — the diagnose-why-it-looks-AI-made skill.
- **T9 → dsar-handling:** erasure is one of the named DSAR flows ("access, export, rectification, erasure, restriction, or objection requests … processor deletion instructions").
- **T10 → performance-optimization:** a measured performance problem with a fix to prove; `performance-optimization` owns the measure–fix–verify loop (the fix itself executes under the owning department's skill). `core-web-vitals` (field metrics verdict) and `frontend-core` (performance budget as base layer) were runners-up.

---

## Part 2 — Scoring (after commitment; each chosen SKILL.md opened)

Each verdict below quotes the chosen skill's own "When to use" line from its SKILL.md. Judged strictly: a choice is correct only if that skill's Use-when owns the task, not merely relates to it.

| # | First choice | Verdict | Evidence from the skill's own Use-when |
|---|--------------|---------|------------------------------------------|
| T1 | `forms` | ✅ Correct | "building or reviewing any form — signup, **checkout**, settings, search-with-filters, multi-step flows — its labels, validation, error handling, and submission behavior." Checkout is named verbatim; mobile checkout friction is form behavior (labels, validation, errors, submission). |
| T2 | `error-tracking` | ✅ Correct | "setting up or changing how unhandled errors are captured, grouped, scrubbed, triaged, and read at release time — for any client or server surface." The task's primary deliverable. Its own Do-NOT-use assigns alert *routing/policy* to `alerting`, which is this skill's declared Load-with/Feeds-into companion — error-tracking is the correct first load; alerting follows from it. |
| T3 | `changelog` | ✅ Correct | "a project ships anything a user can notice — a release, a deprecation, a fix — and its CHANGELOG.md must be created, updated, or cut for release." Its Do-NOT-use confirms release notes are written *from* the changelog, so this skill owns the combined changelog + release-notes deliverable. |
| T4 | `tenant-isolation` | ✅ Correct | "the product serves more than one tenant (or will), and any table, query, job, or cache key touches tenant-owned data." A pre-enterprise review of per-tenant **data** isolation is an enforcement review across tables/queries/cache keys — this skill's exact scope. Its Do-NOT-use cedes only *choosing the tenancy model* to `multitenancy-saas`; the task does not question the model. (See defect D-2 for the near-overlap.) |
| T5 | `handover` | ✅ Correct | "a project changes hands — new owner, new maintainer, end of engagement… this skill runs the readiness review and the acceptance test that close the transfer." An acquisition is a change of owner; due-diligence documentation prep is the transfer readiness review. `documentation-writing` is the expected second load for authoring individual pages (handover's Do-NOT-use itself routes page-writing there), but the owning first choice for "prepare to be acquired" is handover. |
| T6 | `backend-auth` | ✅ Correct | "implementing or reviewing signup, login, logout, session handling, or password reset for any client — anywhere the system must prove who a caller is before trusting a request… This skill owns identity proof and the session lifecycle." Adding a passkey login is implementing a new identity-proof/login method. Its Do-NOT-use cedes only *in-depth attack hardening* to `auth-hardening` (D7), not login implementation. (See defect D-1: routing succeeded only via the generic word "login".) |
| T7 | `cloud-costs` | ✅ Correct | "the project spends anything on cloud resources… when a bill, budget, or cost estimate is produced; when autoscaling, instance sizing, or commitment discounts are decided; when 'optimisation' work is proposed." A cloud-bill/waste task is this skill verbatim; `kubernetes` owns running workloads, not their cost, and feeds into this skill via `scaling`. |
| T8 | `design-system` | ✅ Correct | "reviewing a page for system-level failures: monotony, drift, invented proof. This skill is the primary home for WCPM's visual-language material: §2 catalog (as reference), **§3 diagnosis and CV cures**, §4 design brief and distinctiveness, and §6 visual craft." "Diagnose why it looks generic/AI-made" is this skill's stated diagnosis material. |
| T9 | `dsar-handling` | ✅ Correct | "building or reviewing the flows for access, export, rectification, **erasure**, restriction, or objection requests; wiring the request log, response clocks, or processor deletion instructions." A GDPR deletion request is an erasure request; propagation into backups/logs and processors is executed under this flow (with D5 `backup-recovery` / D14 `audit-trails` as companions). |
| T10 | `performance-optimization` | ✅ Correct | "a measured performance problem exists… and the job is to find the cause, fix it, and prove the fix with the same instrument that found the problem." A 60fps scroll target is a measured performance problem; the skill's own boundary text states the fix executes under the owning department's skill (D3 frontend) inside this skill's measure–fix–verify loop. `frontend-core` owns the performance *budget* as a base layer, not this fix loop. (See defect D-3.) |

### Result

- **Score: 10/10 correct first choices.**
- **Departments spanned:** 7 (D3, D4, D5, D6, D10, D12, D14) — bar ≥6 met.
- **Pass bar (9/10): PASS.**

No first choice was wrong, so no corrective owner needs to be named for any task. Two choices (T4, T5) had a credible runner-up and were resolved by the chosen skill's own Do-NOT-use boundary lines — the index's boundary statements, not just its Keywords, carried the routing.

---

## Part 3 — Index defects found

Three defects, all minor: none caused a miss in this run, but each is a place where the index routes by implication rather than by the task's own terms.

- **D-1 — Missing keyword: passkeys / WebAuthn (T6).** No entry in the entire index contains "passkey" or "WebAuthn" — not in Keywords, not in any Use-when line. `backend-auth` routes only via the generic words "login" / "identity proof", and `auth-hardening` via "MFA enrolment". A fresh agent keyword-matching the task's actual terms ("passkeys", "WebAuthn") finds zero hits and must fall back to browsing department sections. *Fix:* add passkeys/WebAuthn to `backend-auth`'s Use-when line (e.g. "…login (password, passkey/WebAuthn, magic link)…") so the derived Keywords pick the terms up.
- **D-2 — Overlapping audit claims, missing cross-reference (T4).** `multitenancy-saas` (D2) claims the isolation model must be "chosen, implemented, or **audited**", while `tenant-isolation` (D5) owns enforcement of isolation across tables/queries/jobs/cache keys. Both entries can claim an "isolation review". The disambiguation exists only inside `tenant-isolation`'s Do-NOT-use line; `multitenancy-saas`'s index entry never points data-level reviews to D5. *Fix:* add a cross-reference in `multitenancy-saas`'s Use-when or Do-NOT-use index text: data-level isolation enforcement/review → `tenant-isolation`.
- **D-3 — Missing keywords: rendering performance (T10).** No entry mentions frame rate, scroll performance, list virtualization, or rendering jank. `performance-optimization`'s Use-when speaks of templates failing field p75, endpoints breaching p95/p99, and load tests — a client-side rendering task matches only by generalizing to "a measured performance problem exists". *Fix:* extend `performance-optimization`'s (or `frontend-core`'s) Use-when with an explicit client-rendering clause (e.g. "…or a client rendering problem — jank, dropped frames, long lists") so the derived Keywords include the terms such tasks actually use.

**Index defect count: 3** (2 keyword gaps, 1 missing cross-reference).
