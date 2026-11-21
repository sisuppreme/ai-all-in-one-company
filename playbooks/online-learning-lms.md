# Playbook — Online Learning (LMS)

## Goal

Build a learning platform where the learning state is the product: courses made of lessons, enrollment, per-learner progress that is never lost or faked, assessments that record real attempts, and completion that means something — layered on the content playbook's publishing discipline and the SaaS playbook's account/payment machinery.

## Departments + order

Step 0 (always-on core) → D1 → D2+D7 → D3+D13+D4+D5 → D11 (if paid) → D14 → D12 → D18 → D7+D8 → D6 → D9

A hybrid of the Content and SaaS orders: content structure is designed with the course model (D2), learning state is built with the app (D4+D5), and D9 still finishes — a course catalog nobody can find enrolls nobody.

## Skills to load

Load this playbook's bundle first: `bundles/online-learning-lms.md`. Then, per step:

Key skills (§5.6, assigned in the Phase 6 defect loop — DR-04): `requirements-writing`, `system-design`, `frontend-core`, `api-building`, `schema-design`, `payments`, `ci-cd`.

| Skill | Bundle |
|---|---|
| project-templates, progress-tracking | `bundles/core.md` |
| secrets-management, qa-gates | `bundles/core.md` |
| requirements-writing, fact-sheet | `bundles/product-requirements.md` |
| system-design | `bundles/architecture.md` |
| frontend-core, frontend-state, forms | `bundles/frontend.md` |
| accessibility-audit, wcag | `bundles/accessibility-i18n.md` |
| api-building, media-processing, file-uploads | `bundles/backend.md` |
| schema-design | `bundles/database.md` |
| payments, subscriptions, transactional-email | `bundles/integrations-payments.md` |
| content-strategy, technical-seo, structured-data | `bundles/seo-content.md` |
| privacy-laws, legal-documents | `bundles/legal-privacy.md` |
| performance-budgets, core-web-vitals | `bundles/analytics-observability.md` |
| user-onboarding, help-center, activation-metrics | `bundles/customer-experience.md` |
| owasp, auth-hardening | `bundles/security.md` |
| placeholder-scan | `bundles/qa-testing.md` |
| ci-cd, hosting | `bundles/devops-deployment.md` |

Conditional: subscriptions applies for membership/all-access models; payments alone for per-course sales; neither for a fully free catalog (record the model in the fact-sheet). If the platform adds AI features (tutoring, generated quizzes, recommendations), add a D17 step before D7+D8 (llm-integration, ai-safety, ai-evaluation) — AI-generated assessment content is assessment content and is reviewed like it.

## Docs to write first

1. `fact-sheet.md` — the offer facts: course catalog (real courses only), pricing/membership model, what completion certifies, refund terms. **No invented courses, instructors, student counts, or accreditation claims** — a certificate or outcome claim the operator cannot back does not ship.
2. Course/progress model note — course → module → lesson hierarchy; the progress state machine (not started → in progress → completed, per lesson, rolled up per course); what an assessment attempt is; decided before schema work.
3. `stack.md` — stack, video hosting choice (provider embed vs self-hosted via media-processing), payment provider if paid.
4. `progress.md` — playbook trace and gate results.

The full mandated set for this type is `templates/mandated-manifest-online-learning-lms.txt`, which governs (G-PM-001); the list above is the hand-written starting subset. The manifest's `PAYMENT_SECURITY.md` is a conditional file (PM-005): it is emitted when the step-4 money step applies (a paid catalog or a membership model); for a fully free catalog it is recorded not-applicable — with the money model as the reason — in the generation record, instead of being created.

## Step-by-step sequence

0. **Always-on core.** Load `bundles/core.md`; project files, `progress.md`, secrets baseline.
1. **D1 requirements.** requirements-writing for two populations: learners and instructors/admins. content-strategy in the same step: the catalog's information architecture (subjects, levels, course pages) is a content decision with SEO consequences, made before build. *Decision points: free, per-course, or membership? Are certificates issued, and what do they claim? If the money model or the certificate claim is undecided, stop and ask (§6.3).* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
2. **D2+D7 design.** system-design: progress is server-side state, written by lesson-completion events, resumable across devices; the client never asserts completion the server did not record (G-AR-001, G-AR-004 data-ownership audit — progress belongs to the learner record, owned by D5's schema). auth-hardening for learner/instructor roles (G-SE-031).
3. **D3+D13+D4+D5 build.** schema-design: enrollment, progress, and attempt records with constraints (G-DB-001, G-DB-002) — one active enrollment per learner per course, progress percentages computed from lesson records, never stored as an editable number. api-building for catalog, enrollment, and progress endpoints (G-BE-001, G-BE-002 persistence per write). media-processing for lesson video/audio: transcodes, poster frames, caption tracks (G-BE-121 golden-file test, G-BE-123 failure-state drill — a failed transcode shows an honest processing state, never a fake playable lesson). file-uploads for instructor materials and learner submissions (G-BE-111 upload round-trip, G-BE-112 hostile-file pack). Both routings are conditional on the `stack.md` choices: if lessons are delivered by provider embed rather than self-hosted media, media-processing and its gates (G-BE-121, G-BE-123) record N/A with the reason in `progress.md`; if the course model accepts no uploads (no instructor materials, no learner submissions), file-uploads and its gates (G-BE-111, G-BE-112) record N/A the same way. Assessments built on forms discipline (G-FE-121, G-FE-123 — a double-submitted attempt is one attempt). Frontend-state carries playback position and optimistic progress with server reconciliation (G-FE-091). D13 in the same step, with LMS-specific weight: video lessons ship captions and transcripts, quizzes are keyboard- and screen-reader-complete (G-AC-001, G-AC-003 screen-reader smoke test).
4. **D11 money (if paid).** payments in test mode (G-IN-001, G-IN-002): purchase grants enrollment via webhook-confirmed state, never via the success redirect alone (G-IN-051 forgery test). subscriptions for membership models (G-IN-011 test-clock lifecycle walk — a lapsed membership's access change is rehearsed, not assumed). *Decision point: if no payment provider is chosen, stop and ask (§6.3).* transactional-email for enrollment and completion messages (G-IN-061, G-IN-064). (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
5. **D14 legal/privacy.** privacy-laws register: learner records, progress data, and — if the audience includes minors — the age-requirements analysis is a blocking input, not a footnote (G-LG-001, G-LG-002). legal-documents: terms, refund policy, and the certificate wording exactly as it will be issued.
6. **D12 performance.** performance-budgets (G-AN-101) on catalog and lesson pages; core-web-vitals field plan (G-AN-111) — lesson pages are media-heavy and budget accordingly.
7. **D18 learner experience.** user-onboarding: enroll → first lesson → first completion is one unbroken path (G-CX-031 fresh-account walkthrough, G-CX-032 event-binding audit — the activation events the onboarding claims to fire actually fire). help-center for learner support (G-CX-021 top-questions walkthrough).
8. **D7+D8 verification.** Security: G-SE-001 (0 criticals), G-SE-031; enrollment forgery test — a learner cannot self-grant a paid course or a completion. Progress rehearsal: enroll → complete lessons across two devices → progress identical on both → assessment attempted, failed, retaken per the model → course completes → certificate issued with the exact approved wording. QA: G-QA-111; placeholder-scan G-QA-141 (scan rendered output, not source) — demo courses with fake lessons are placeholder content and do not ship; the launch catalog is the real catalog from the fact-sheet, even if it is small.
9. **D6 deploy.** ci-cd (G-DO-001), hosting (G-DO-071); media pipeline verified in production with one real lesson upload.
10. **D9 finish.** technical-seo + structured-data for the public catalog (G-CO-001; G-CO-081 CI schema validation, G-CO-082 markup-vs-visible diff — Course markup describes the real course: real instructor, real syllabus, no invented ratings).

## Gates that must pass

- **Learning state:** G-DB-001, G-DB-002, G-BE-002, G-FE-091 — progress is server-recorded, constraint-backed, and consistent across devices.
- **Media:** G-BE-121, G-BE-123, G-BE-111, G-BE-112 — lessons process honestly; uploads are safe.
- **Money (if paid):** G-IN-001, G-IN-002, G-IN-051; membership models also G-IN-011 — enrollment follows verified payment, never a redirect.
- **Accessibility:** G-AC-001, G-AC-003, G-AC-005 — WCAG 2.2 AA pass, captions/transcripts present on lesson media.
- **Content/SEO:** G-CO-041 (brief traceability), G-CO-081, G-CO-082 — markup matches the visible, real course.
- **Legal:** G-LG-001, G-LG-002; certificate and outcome claims match the fact-sheet exactly.
- **Onboarding:** G-CX-031, G-CX-032.
- **Security/QA:** G-SE-001 (0 critical findings), G-QA-111, G-QA-141 — no demo courses in production.
- **Performance/deploy:** G-AN-101, G-DO-001, G-DO-071.

## Failure handling

- **Progress inconsistency across devices:** the defect is architectural (client-asserted state); fix by making the server the only writer of completion per the data-ownership audit (G-AR-004). Never patch it with a "sync now" button.
- **Enrollment granted without verified payment (forgery test fails):** release blocker. Enrollment moves behind webhook-confirmed payment state; re-run the full money rehearsal.
- **Lesson media fails processing (G-BE-123):** the lesson stays in an honest "processing/failed" state visible to the instructor; a lesson that pretends to be playable and is not is a placeholder-scan failure, not a media bug.
- **Certificate or marketing claim exceeds the fact-sheet:** the claim is cut or corrected before launch — the fix is never to edit the fact-sheet to match the copy.
- **Structured-data diff fails (G-CO-082):** markup is regenerated from the same data that renders the page; hand-written course markup is removed.
- **Any other gate fails:** fix in the owning department, re-run, record both results in `progress.md`.

## Definition of done

A learner can enroll, learn, be assessed, and complete with progress that survives devices and deploys; enrollment and completion cannot be forged; every lesson playable is really playable and captioned; the catalog contains only real courses with claims the fact-sheet backs; deployed (G-DO-071) with all gates above green. **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* when every gate except the provisioning-waived ones is green, each waived gate is recorded as a provisioning waiver per §6.3, and the unblocking conditions are listed in `progress.md` — the deployment requirements above remain open until the environment exists.

## Worked mini-example — a small platform selling one photography course

1. Core loaded; fact-sheet records: one real course (24 lessons), per-course price set by the owner, completion certificate states course name + learner + date — no accreditation claimed.
2. D1 + content-strategy: catalog is one course page + curriculum; learner and instructor requirement sets written separately.
3. D2: progress = per-lesson completion events on the server; percentage computed, never stored (G-AR-004 records ownership).
4. Build: enrollment/progress constraints pass G-DB-002; a double-submitted quiz attempt records once (G-FE-123).
5. Media: 24 lessons transcoded with caption tracks (G-BE-121); one corrupted upload lands in an honest failed state for the instructor (G-BE-123).
6. D11 test mode: purchase → webhook → enrollment granted (G-IN-002); a forged success-redirect without a webhook grants nothing.
7. D13: screen-reader smoke test completes a quiz end to end (G-AC-003); captions verified on three sampled lessons.
8. Rehearsal: learner completes 10 lessons on desktop, continues on phone — progress identical; finishes, certificate issues with the approved wording.
9. D7+D8: G-SE-001 clean; G-QA-141 confirms no demo course exists in the production seed.
10. Deploy (G-DO-071); Course structured data validates against the visible page (G-CO-082); catalog page indexed (G-CO-001).
