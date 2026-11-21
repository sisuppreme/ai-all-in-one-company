# Phase 4 Cross-Review — Cluster B (D4, D5, D6)

Reviewer: Phase 4 cross-review, cluster B. Date: 2026-11-21.
Scope: substance review only (format validation already passed 227/227). No skill files were edited.

## Scope covered

**Deep-read (19 skills)** — full read of SKILL.md against the department research file, with at least one example file opened per department sample:

- **D4 Backend (skills/backend):** api-building (+ example-1), backend-auth, queues-jobs, rbac, error-handling, rate-limiting
- **D5 Databases (skills/database):** migrations, seed-data, tenant-isolation (+ example-2), caching, backup-recovery, vector-db
- **D6 DevOps (skills/devops-deployment):** ci-cd, free-tiers, hosting, reliability, kubernetes, rollback (+ example-1), incident-response

**Skimmed (34 skills)** — metadata, rule counts, gate titles and mechanics checked against the research notes:

- D4: rest-conventions, validation, feature-flags, sdk-design, user-reporting, admin-tools, realtime, file-uploads, media-processing, notifications
- D5: schema-design, sql-fundamentals, nosql-patterns, transactions-concurrency, query-performance, indexing, data-access, read-replicas, search-engines, data-warehousing (reconciliation gate read in full), etl-pipelines, data-ingestion, pipeline-orchestration, data-quality
- D6: preview-environments, deployment-strategies, containers, infrastructure-as-code, servers-vps, cdn-strategy, domains-dns, ssl-certificates, scaling, cloud-costs

**Programmatic checks:** every `Depends on` / `Feeds into` entry in all 53 cluster-B skills was resolved against `build/catalog.txt` — 100% resolve to real catalog skills (the single parser hit was a parenthetical artifact in notifications, whose actual reference, transactional-email, is valid). DET parameter definitions were spot-verified against `skills/detection/*/PARAMETERS.md`.

## Findings

### BLOCKER — none

No skill teaches a wrong practice, invents a capability, or contradicts its department research on a core method. All 18 deep-read skills' core methods match their research notes (contract-first handlers, cache-aside, expand-and-contract, build-once-promote-digest, etc.).

### MAJOR

**M-1 — incident-response (D6): the single-operator translation required by the research is missing.**
D6 research, open risk 3, instructs Phase 3 to translate multi-human practices honestly for the single-operator case this repo is built for ("escalation = the user; reviewer gate = a deliberate pause + checklist"), and two sibling skills did exactly that: reliability DO-266 ("for a single operator, the operator plus a stated escalation contact") and deployment-strategies DO-045 ("For a single operator, the reviewer gate becomes a deliberate pause plus the release checklist — the gate is never silently deleted"). incident-response did not:

- DO-281 requires a rotation of "named people" with "at least two escalation levels"; BAN-DO-141's replacement repeats the two-level requirement.
- DO-283 requires an Incident Commander who "does not personally fix anything while commanding"; DO-284 requires a separate scribe.
- G-DO-141 (on-call inspection) passes only with "two or more named escalation levels for the current week."

A single operator — the only operator this repository supports — can never pass G-DO-141 and cannot execute DO-283/DO-284 as written, so the skill is unusable in exactly the context it was commissioned for.
**Suggested fix:** add a single-operator rule mirroring DO-266/DO-045: escalation level 2 = the project owner/user; the operator acts as IC and fixer in sequence (declare → mitigate → communicate → log the timeline contemporaneously in the incident record); adjust G-DO-141 to accept a named primary plus a named escalation contact.

### MINOR

**m-1 — DET citations in BAN entries are sometimes nearest-match rather than exact (all three departments).**
The citations always point at real parameters in the right family, but several do not match the cited parameter's defined signal:

- backend-auth BAN-BE-055 (plaintext/fast-hash password storage) and rbac BAN-BE-063 (default-open unguarded route) both cite DET-CODE-020, whose signal is "disabled security controls and unsafe defaults" (verify=False, CORS *, debug mode). Error-handling BAN-BE-143's use of the same ID is exact (debug error page in production); the other two are stretches.
- free-tiers BAN-DO-081 and BAN-DO-085 (invented tier limits; unrecorded billing-start cap) cite DET-INF-027, whose signal is container resource limits/saturation. BAN-DO-083 (expiring free database, no expiry record) cites DET-INF-008, "No backups configured." The D6 research itself records that the free-tier failure mode has no DET-INF ID, so the drafter had nothing exact to cite.
- seed-data BAN-DB-031/032/035 cite DET-INF-003 / DET-CODE-024 approximately for the seed-specific failure modes.

**Suggested fix:** either annotate these entries as nearest-match in the BAN line, or (better) extend the DET-INF/DET-CODE families with the missing parameters (free-tier misstatement, seed-data leakage) in a Phase 4 detection amendment, and re-point the citations.

**m-2 — vector-db (D5): recall gate has no fixture procedure.**
D5 research, open risk 5, asked Phase 3 to ship the recall-vs-exact check "as a procedure with a placeholder-free template (synthetic vectors generated in the test)." DB-284 and G-DB-142 correctly require a fixed sample query set and a recorded threshold, but no skill text or example describes how a project generates that set synthetically. Each project will improvise it — the exact outcome the research warned against.
**Suggested fix:** add one example file to vector-db showing a generated fixture (seeded synthetic vectors + paraphrase queries produced in-test) and the recall computation, referenced from G-DB-142.

**m-3 — queues-jobs (D4): one BAN/DET pairing is defensible but easy to misread.**
BAN-BE-092 (default-attempt jobs) cites DET-CODE-006; the parameter's signal does include "no retry policy," so the citation holds, but a reader landing from error-handling (where DET-CODE-006 anchors the naked-boundary-call BAN) may read it as a copy error.
**Suggested fix:** none required; optionally add "(retry-policy clause)" after the citation. Recorded for completeness, not as a defect.

## What is excellent — propagate these patterns

- **Posture tiers survived into D6 skills (the research's risk 1, fully answered).** hosting DO-142 labels every deployment validation vs. production posture, names the promotion trigger (first real user, first payment, first availability commitment), and requires listing which DET parameters are knowingly waived at validation posture; reliability DO-273 repeats the declaration; free-tiers DO-171 names the first paid step and its trigger per provider. The D-005 $0-launch vs. production-grade contradiction is resolved in the skills, not left to collide.
- **free-tiers encodes the verification procedure, not the numbers (risk 2, answered).** DO-162/DO-163: no limit without an official page URL and check date; entries go stale at 90 days. All provider figures are presented as dated examples.
- **seed-data draws the QB-10 line as a blocker (D5 risk 1, answered).** DB-068 states a production dashboard populated by seed data "is fake functionality and fake content at the same time," and G-DB-032 enforces it by scanning the production pipeline for the sample-seed step.
- **tenant-isolation teaches the backstop's preconditions, not just policy syntax (D5 risk 2, answered).** Non-owner role (DB-104), transaction-local context (DB-105), WITH CHECK (DB-103), plus a pool-of-1 leak test (G-DB-054) and a role check (G-DB-053) that catches "backstop theater."
- **caching ↔ data-access cross-reference is closed (D5 risk 4, answered).** caching DB-250 makes delete-on-write conditional on all writes flowing through the data-access layer, naming the bypass failure explicitly.
- **kubernetes opens with the adoption test (D6 risk 5, answered).** DO-081 requires a recorded justification, and the Do-NOT-use section routes single-service apps to hosting/servers-vps.
- **api-building example-1 is the model example for the whole repo:** the idempotency key, request hash, and first response are stored in the same transaction as the order, and the total is recomputed server-side — it demonstrates BE-005 and BE-003 simultaneously with runnable code.
- **Gates are mechanical throughout.** Every deep-read skill's automated gate names an exact command, query, or test with a pass/fail assertion (e.g., G-DO-001 broken-test drill via check-run API, G-DB-052 pg_policies catalog query, G-BE-151 burst test). No deep-read skill had a gate that was aspirational as written, and no deep-read rule was too vague to check.

## Verdicts per department

- **D4 Backend & APIs — sound.** 6 deep-read, 10 skimmed; no findings above minor (m-1, m-3 touch two BAN citations).
- **D5 Databases & Data — sound.** 6 deep-read, 14 skimmed; the department's two sharpest research risks (seed data vs. real content, RLS backstop hygiene) are encoded as blocker rules with automated gates. m-2 is a completeness gap, not a correctness one.
- **D6 DevOps & Deployment — sound-with-fixes.** 7 deep-read, 10 skimmed; posture tiers, free-tier verification discipline, and the kubernetes adoption test all landed. Fix M-1 (incident-response single-operator translation) before Phase 6 proof projects rely on the skill, since a single-agent proof project cannot pass G-DO-141 as written.

**Totals: 19 deep-read, 0 blockers, 1 major, 3 minors.**
