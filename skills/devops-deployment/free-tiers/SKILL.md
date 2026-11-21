# free-tiers

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://render.com/docs/free ; https://vercel.com/pricing ; https://www.netlify.com/pricing/ ; https://docs.github.com/en/billing/concepts/product-billing/github-actions
- **Depends on:** hosting
- **Feeds into:** cloud-costs, scaling, reliability

## When to use / Do NOT use

- **Use when:** any part of the stack (hosting, database, CI, CDN, storage) runs on a free tier or free plan, at launch or later; when a launch plan claims "$0 hosting"; when a free-tier limit is quoted in any plan, estimate, or client-facing document.
- **Do NOT use when:** the stack is fully paid — use cloud-costs for spend control instead. Do not use this skill to pick the host itself; that is hosting, which consumes this skill's free-tier sheet.

## Rules

1. **DO-161 — One sheet per stack.** Before launch, create a free-tier sheet in the project notes with one row per provider in the stack (hosting, database, CI, CDN, storage, email) and these fields per row: cap, behavior at the cap (hard stop or billing starts), sleep/expiry behavior, commercial-use terms, official limits-page URL, and date checked. A provider missing from the sheet fails G-DO-081.
2. **DO-162 — No unsourced numbers.** A tier limit, quota, or price appears in a plan only if it was read on the provider's official pricing/limits page and the sheet records that URL and the check date. Numbers from blog posts, videos, or memory are placeholders and are marked as such, never presented as limits.
3. **DO-163 — Entries expire after 90 days.** A sheet entry older than 90 days is stale; re-read the official page and update the entry before any launch, migration, or capacity decision that relies on it. Free tiers shrink with little notice, so the check date is part of the fact.
4. **DO-164 — Alert below every hard cap.** Where the provider offers usage alerts or quota notifications, set one below each hard cap (for example at 80% of the recorded cap) before launch, routed to a channel a named person reads. Where no alert exists, record that fact in the sheet and name the manual check that replaces it.
5. **DO-165 — Name the binding constraint.** For the whole stack, identify which cap is reached first at expected launch load and record it in the sheet as the binding constraint, with the expected symptom when it hits (downtime, failed builds, rejected requests). A launch plan that lists caps but no binding constraint is incomplete.
6. **DO-166 — Sleeping tiers are validation-only.** A tier that sleeps or spins down when idle (Render free web services spin down after 15 minutes without inbound traffic and take about a minute to spin back up, checked 2026-11-21) hosts demos and validation only — never a service with real users, inbound webhooks, or scheduled jobs that must fire on time.
7. **DO-167 — Record expiries the day they are created.** When a free resource has a lifetime (Render free PostgreSQL expires 30 days after creation, checked 2026-11-21), record its expiry date in the sheet on creation day and set a reminder before it. An expiry that falls inside the launch window with no migration plan is a launch blocker.
8. **DO-168 — Commercial work needs commercial terms.** Never run a production or revenue-bearing workload on a tier whose terms restrict it to personal or non-commercial use. Check the terms field of the sheet before launch; a mismatch means change the tier or the plan, not ignore the terms.
9. **DO-169 — Shared pools are summed, not per-service.** Where a quota is shared (Render's 750 free instance hours are per workspace per month, not per service, checked 2026-11-21), the sheet records the pool total and the sum of all services drawing on it. Planning each service against the full pool overstates capacity and fails G-DO-081.
10. **DO-170 — No state on ephemeral filesystems.** On tiers whose local filesystem is wiped on spin-down, redeploy, or restart (Render free behavior, checked 2026-11-21), uploads, sessions, and databases live in real external stores. Anything the app writes to local disk on such a tier is treated as disposable cache.
11. **DO-171 — Name the first paid step and its trigger in advance.** The sheet names, per provider, the first paid upgrade and the event that triggers it (first real user, first payment, cap forecast within 30 days). Per the project's $0-spend posture, no paid step is taken before its trigger fires; where a cap cannot be bought past at all (Vercel Hobby cannot purchase extra usage past its caps, as of 2026-11), hitting the cap means a plan change, and the sheet says so.
12. **DO-172 — Hard-stop and billing-start caps are different risks.** The sheet's at-cap behavior field distinguishes "service stops" from "billing starts." A billing-start cap on any provider requires a recorded spend decision (who approved overage, up to what amount) before launch; an unrecorded billing-start cap is an unbudgeted liability.

## BAN list

- **BAN-DO-081 — Invented tier limits.** Banned: stating a free-tier limit, quota, or price in a plan without an official page URL and check date in the sheet. Defeats: DET-INF-027 (nearest match — no DET parameter names this exact signal). Bad: "Render free gives 1,000 hours/month, plenty for launch" — a number from memory, 33% above the real shared pool. Instead: read https://render.com/docs/free, record the actual cap with the date checked, and mark anything unverified as a placeholder. Severity: BLOCK.
- **BAN-DO-082 — Sleeping tier in production.** Banned: pointing real users, production webhooks, or scheduled jobs at a tier that sleeps when idle. Defeats: DET-INF-019. Bad: the production API runs on a free tier that spins down after 15 idle minutes, so the first request each morning — and every payment webhook — waits ~1 minute or times out. Instead: keep sleeping tiers for demos and validation; production runs on an always-on tier or a recorded paid step per DO-171. Severity: BLOCK.
- **BAN-DO-083 — Expiring resource with no expiry record.** Banned: creating a free resource with a fixed lifetime and not recording its expiry date the same day. Defeats: DET-INF-008 (nearest match — no DET parameter names this exact signal). Bad: the free PostgreSQL instance is created at project start; 30 days later it expires mid-launch with the only copy of the data inside. Instead: record the expiry date in the sheet on creation day, set a reminder ahead of it, and name the migration or backup step that runs before it. Severity: BLOCK.
- **BAN-DO-084 — Commercial production on a personal-use tier.** Banned: running a revenue-bearing production service on a tier whose terms allow personal or non-commercial use only. Defeats: DET-INF-019. Bad: the paid product's only deployment sits on a personal hobby tier because it is free; enforcement or a cap hit takes the whole business down with no fallback. Instead: verify the terms field before launch and move commercial production to a tier whose terms permit it, per DO-168. Severity: BLOCK.
- **BAN-DO-085 — Unrecorded billing-start cap.** Banned: launching on a tier where passing the cap starts metered billing, with no recorded spend decision. Defeats: DET-INF-027 (nearest match — no DET parameter names this exact signal). Bad: a traffic spike pushes the project past its free allowance and the first notice is an invoice nobody approved. Instead: record the at-cap behavior per DO-172 and, for billing-start caps, the approved overage decision — or choose a hard-stop tier. Severity: WARN.

## Gates

- **G-DO-081 — Free-tier sheet audit (automated).** Verifies: DO-161, DO-162, DO-163, DO-169. Check: `grep -c '^| ' docs/free-tier-sheet.md` equals the provider count in the stack list, and for every row, `grep -E 'Checked: [0-9]{4}-[0-9]{2}-[0-9]{2}'` matches a date within the last 90 days (verify with `date -d`); each row contains cap, at-cap behavior, sleep/expiry, terms, and source URL fields. Pass: every provider in the stack has a complete row ≤90 days old, and shared pools show the summed draw. Fail: block launch until the sheet is complete and fresh. Recorded in: progress.md.
- **G-DO-082 — Alert coverage check.** Verifies: DO-164. Check: for each hard cap in the sheet, open the provider console and confirm a usage alert exists below the cap routed to a monitored channel; where the provider offers none, confirm the sheet names the manual replacement check. Pass: every hard cap is covered by an alert or a named manual check. Fail: block launch. Recorded in: progress.md.
- **G-DO-083 — Production posture check.** Verifies: DO-166, DO-168. Check: list every production workload and its tier from the sheet; confirm none runs on a sleeping tier or a personal/non-commercial-only tier. Pass: zero production workloads on sleeping or terms-mismatched tiers. Fail: block launch. Recorded in: progress.md.
- **G-DO-084 — Expiry register check.** Verifies: DO-167. Check: for every sheet row with an expiry behavior, confirm an expiry date and a pre-expiry reminder exist, and no expiry falls inside the launch window without a recorded migration step. Pass: all expiries dated, reminded, and covered. Fail: block launch. Recorded in: progress.md.

## Anti-patterns

- **Headline-number planning.** Quoting the biggest number on a pricing page ("generous free bandwidth!") while the binding constraint is a smaller, quieter cap elsewhere in the stack. Catch it by asking which cap is hit first — if nobody can answer, DO-165 was skipped.
- **Screenshot sourcing.** Copying tier numbers from a blog post, video, or comparison table instead of the provider's own page; the numbers are often for a different plan or a past year. Catch it by checking every sheet row has an official-domain URL.
- **Free-stack sprawl.** Spreading one small app across six providers' free tiers to dodge a single cap, multiplying the sheets, alerts, and failure modes the project must track. Catch it by counting providers: each one must earn its place against the operational cost of tracking it.
- **Set-and-forget sheet.** Writing the free-tier sheet once at project start and never re-checking it, so the plan quietly runs on last year's limits. Catch it by sorting the sheet by check date — the oldest date is the plan's real freshness.

## Examples

- [Example 1 — Invented limits in a launch plan](examples/example-1.md) — violates/corrects DO-162.
- [Example 2 — Sleeping tier chosen for a production API](examples/example-2.md) — violates/corrects DO-166.
- [Example 3 — Expiring free database with no expiry recorded](examples/example-3.md) — violates/corrects DO-167.

## Recall anchors

- No number without an official page and a check date.
- Sleeping tiers are for demos; expiring tiers are launch blockers.
- Shared pools are summed across every service, never per-service.
- Know the binding constraint and what happens when it hits.
- Name the first paid step and its trigger before you need it.

## Checklist

- [ ] Free-tier sheet exists with a complete row (cap, at-cap behavior, sleep/expiry, terms, URL, date) for every provider in the stack. (DO-161)
- [ ] Every limit in every plan traces to an official page checked within the last 90 days. (DO-162, DO-163)
- [ ] A usage alert sits below every hard cap, or a named manual check replaces it. (DO-164)
- [ ] The stack's binding constraint and its at-cap symptom are recorded. (DO-165, DO-172)
- [ ] No production workload runs on a sleeping tier or a personal/non-commercial-only tier. (DO-166, DO-168)
- [ ] Every expiring resource has its expiry date and a pre-expiry reminder recorded. (DO-167)
- [ ] Shared pools are recorded as pool totals with the summed draw of all services. (DO-169)
- [ ] The first paid upgrade and its trigger are named for each provider. (DO-171)
