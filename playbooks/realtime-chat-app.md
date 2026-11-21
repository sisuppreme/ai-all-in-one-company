# Playbook — Real-time / Chat App

## Goal

Build a web application whose core value is live: chat, presence, live updates, or collaborative state that reaches every connected client in near-real time, stays correct across disconnects and reconnects, and degrades honestly when the live path fails.

## Departments + order

Step 0 (always-on core) → D1 → D2+D7 → D3+D13+D4+D5 → D14 → D12 → D18 → D7+D8 → D6 → D9

This matches the brief's order for this type, with D14, D12, and D18 made explicit steps (chat content is personal data, connection load is a performance problem, and the chat surface itself is a D18 skill) instead of implicit ones.

## Skills to load

Load this playbook's bundle first: `bundles/realtime-chat-app.md`. Then, per step:

| Skill | Bundle |
|---|---|
| project-templates, progress-tracking | `bundles/core.md` |
| secrets-management, qa-gates | `bundles/core.md` |
| requirements-writing | `bundles/product-requirements.md` |
| system-design | `bundles/architecture.md` |
| realtime, queues-jobs, notifications, api-building | `bundles/backend.md` |
| frontend-core, frontend-state | `bundles/frontend.md` |
| accessibility-audit, wcag | `bundles/accessibility-i18n.md` |
| schema-design | `bundles/database.md` |
| auth-hardening, owasp, content-moderation | `bundles/security.md` |
| privacy-laws, cookie-consent | `bundles/legal-privacy.md` |
| performance-budgets, monitoring, alerting | `bundles/analytics-observability.md` |
| in-app-chat, user-onboarding, help-center | `bundles/customer-experience.md` |
| placeholder-scan | `bundles/qa-testing.md` |
| ci-cd, hosting | `bundles/devops-deployment.md` |
| technical-seo (public landing/help pages only) | `bundles/seo-content.md` |

Conditional: if the app adds AI features (smart replies, summarization, AI moderation assist), add a D17 step before D7+D8 (llm-integration, ai-safety) — AI output in a live conversation is user-facing content and gets the full D17 treatment. D18's help-center is required only if the app ships public support surfaces; in-app-chat and user-onboarding always apply.

## Docs to write first

1. `fact-sheet.md` — product facts: who talks to whom, expected concurrency, message retention promises. Retention and scale numbers come from the user or research, never invented.
2. `stack.md` — transport choice (WebSocket / SSE / managed realtime provider) with the reason recorded, and the fallback transport.
3. `progress.md` — playbook trace and gate results.
4. Message/presence model sketch — the entities (conversation, message, presence, typing, read state) and which of them are persisted vs ephemeral, agreed before schema work starts.

## Step-by-step sequence

0. **Always-on core.** Load `bundles/core.md`; project files, `progress.md`, secrets baseline.
1. **D1 requirements.** requirements-writing: name the live behaviors precisely (delivery, ordering, presence, typing indicators, read receipts) and which are must-have vs decorative. *Decision point: if expected concurrency or retention is unknown, stop and ask (§6.3) — both change the architecture materially.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
2. **D2+D7 design.** system-design: connection topology, fan-out path, where ordering is enforced, what happens when a node dies mid-conversation (G-AR-001, G-AR-003). In parallel, auth-hardening: a socket connection is an authenticated session, not an open pipe (G-BE-103 connection authorization test).
3. **D3+D13+D4+D5 build.** Backend: api-building for the REST surface, realtime for the live channel, queues-jobs for everything that must survive a disconnect (offline delivery, push fan-out, retries — G-BE-091 failure-injection, G-BE-093 transactional-enqueue). schema-design: messages and read state persisted with constraints (G-DB-001); presence is ephemeral and never the source of truth. Frontend: frontend-state owns connection state, optimistic sends, and reconciliation on reconnect (G-FE-091 trace test, G-FE-093 URL state round-trip). D13 in the same step: the message UI passes accessibility-audit (G-AC-001) — live regions, keyboard-complete composer, focus management on new messages.
4. **D14 legal/privacy.** privacy-laws register: message content, retention period, deletion path, and export are decided and recorded (G-LG-001, G-LG-002). cookie-consent if any tracking ships (G-LG-041). *Decision point: if the product promises end-to-end encryption, stop and confirm the key-management design with the user — it changes D2, D4, and D7 work and must never be a marketing line without the mechanism behind it.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
5. **D12 performance/observability.** performance-budgets for the client (G-AN-101); monitoring covers connection count, fan-out latency, and queue depth as golden signals (G-AN-051, G-AN-052); alerting on queue backlog and connection failure rate (G-AN-061).
6. **D18 experience surfaces.** in-app-chat governs the chat surface's delivery honesty, and the delivery-state discipline behind G-CX-011 and G-CX-013 applies to the product's own conversations. The gates' support-widget forms apply only if the product ships a support surface with those features: the team-inbox delivery test (G-CX-011), the office-hours offline path and ticket queue (G-CX-013), and the config-vs-copy audit (G-CX-014 — every availability and reply-time claim in the copy matches the configured office hours and expected reply times). A chat product without a support surface records those gates N/A with the reason in `progress.md`; its delivery evidence is step 7's G-BE-101/G-CX-012 instead. user-onboarding for first-run (G-CX-031 fresh-account walkthrough). notifications: if the product ships a notification subsystem (an inbox, channels, preferences), the wiring is verified end to end (G-BE-131 trigger test, G-BE-133 preference timing test); if it ships no notifications, or notifications with no preference surface, record the inapplicable gate N/A with the reason in `progress.md`.
7. **D7+D8 verification.** Security: G-SE-001 (ZAP baseline, 0 criticals), G-BE-103 (connection authorization test — an unauthenticated or cross-conversation socket must fail), G-CX-012 (forged-identity test). Realtime correctness: G-BE-101 (two-session live update), G-BE-102 (drop-and-reconnect), G-BE-104 (slow-consumer). QA: G-QA-111, placeholder-scan G-QA-141 (scan rendered output, not source). content-moderation pass if users can post content visible to others.
8. **D6 deploy.** ci-cd (G-DO-001), hosting with the realtime topology from `stack.md` actually provisioned (G-DO-071). *No deployment before step 7 is green.*
9. **D9 finish.** technical-seo for the public surfaces only (landing, help) — the app itself is behind auth and stays out of the index (G-CO-001).

## Gates that must pass

- **Security:** G-SE-001 (0 critical findings), G-SE-031, G-BE-103, G-CX-012.
- **Realtime correctness:** G-BE-101, G-BE-102, G-BE-104, G-BE-091, G-BE-093, G-FE-091.
- **Delivery honesty:** G-CX-011, G-CX-013, G-CX-014, G-BE-131.
- **Accessibility:** G-AC-001, G-AC-005 — WCAG 2.2 AA pass.
- **Privacy:** G-LG-001, G-LG-002.
- **QA:** G-QA-111, G-QA-141 — all green.
- **Performance/deploy:** G-AN-101, G-AN-051, G-DO-001, G-DO-071.

## Failure handling

- **Drop-and-reconnect fails (G-BE-102):** the defect is in state reconciliation, not the transport — fix in frontend-state/realtime (single source of truth for message state, server sequence as arbiter), never by adding a manual refresh button and calling it done.
- **Slow-consumer test fails (G-BE-104):** add bounded buffers and a documented drop/backpressure policy in realtime; a consumer that cannot keep up gets a resync, not an unbounded queue.
- **Delivery-state audit fails (G-CX-014):** remove or rename the dishonest state in the UI copy and the state machine together; shipping a "delivered" tick the backend cannot prove is a release blocker, not a copy tweak.
- **Queue backlog alarms in the D12 drill (G-AN-062):** scale or shed load per the system-design failure review (G-AR-003) before deploy; do not raise the alarm threshold to silence it.
- **Any other gate fails:** fix in the owning department, re-run, record both results in `progress.md`.

## Definition of done

Two-session, reconnect, and slow-consumer tests green; no unauthenticated or cross-conversation socket possible; UI delivery states match provable backend states; retention and deletion behavior matches the privacy register; monitoring and alerts live on connection and queue signals; deployed and reachable (G-DO-071) with all gates above green. **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* when every gate except the provisioning-waived ones is green, each waived gate is recorded as a provisioning waiver per §6.3, and the unblocking conditions are listed in `progress.md` — the deployment requirements above remain open until the environment exists.

## Worked mini-example — team chat for a small support team

1. Core loaded; fact-sheet records 40 seats, 30-day retention (user-confirmed).
2. D1: must-haves = 1:1 + group conversations, delivery + read state, offline catch-up. Typing indicators marked decorative.
3. D2 picks WebSocket with SSE fallback; ordering enforced by per-conversation server sequence. G-AR-003 covers node-death mid-conversation.
4. Build: messages persisted (G-DB-001); sends enqueue transactionally (G-BE-093); presence kept ephemeral.
5. Frontend-state reconciles on reconnect by sequence gap-fill; G-BE-102 passes after one fix round (duplicate render on replay).
6. D14: retention register entry + deletion job verified; no E2EE claimed — the design does not provide it, so the copy does not say it.
7. D18: G-CX-014 catches a "Delivered" label shown on enqueue, not on peer receipt → state renamed "Sent" until receipt exists.
8. D7+D8: G-BE-103 blocks a forged conversation join; G-SE-001 clean; G-QA-141 clean.
9. D12: fan-out latency and queue depth on the dashboard; alert drill fires on a staged backlog (G-AN-062).
10. Deploy via ci-cd; G-DO-071 confirms the live app; two test accounts exchange messages on the production host.
