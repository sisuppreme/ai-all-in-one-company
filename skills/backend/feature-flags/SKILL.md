# feature-flags

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Pete Hodgson, "Feature Toggles" — https://martinfowler.com/articles/feature-toggles.html ; LaunchDarkly, "Kill switches, progressive rollouts, and user targeting" — https://LaunchDarkly.com/blog/kill-switches-progressive-rollouts-user-targeting/
- **Depends on:** api-building
- **Feeds into:** experimentation-platform, ci-cd

## When to use / Do NOT use

- **Use when:** shipping a risky path before it is proven, rolling a change out gradually, running an experiment, or needing a kill path for a feature in production — any behavior that must change without a redeploy.
- **Do NOT use when:** the behavior is a permission (rbac owns who may do something; a flag may hide a feature, never authorize it), a permanent product configuration value (that is settings, not a flag), or a substitute for finishing the work — a flag is not a way to merge a stub.

## Rules

1. **BE-061 — Registry before code.** A flag exists in the central registry — key, owner, type, safe default, expiry date — before any code references its key. A key invented at the keyboard does not ship.
2. **BE-062 — Every flag has a type.** Each flag is typed release, experiment, ops, or permissioning (the Fowler taxonomy). Type determines expected lifetime: release flags live days, experiment flags live until their end date, ops flags are reviewed on a schedule.
3. **BE-063 — The default is the safe value.** If the flag service is unreachable or the key is unknown, evaluation returns the flag's safe default — for a release flag, the old behavior. A flag outage must never enable the unproven path.
4. **BE-064 — One evaluation path.** Flags are evaluated server-side through a single toggle router. Feature code asks the router; it never calls a flag SDK directly, and client code never decides behavior the server will not re-check.
5. **BE-065 — Bucketing is deterministic.** Percentage rollouts assign users by hashing a stable key (flag key + user ID). The same user gets the same variant on every request, device, and service — never a coin flip per request.
6. **BE-066 — The off path is a tested product path.** The flag-off behavior is built, tested, and monitored like the flag-on behavior. Every release flag has a kill path that takes effect without a redeploy.
7. **BE-067 — Expiry is enforced, removal is done.** A flag past its expiry date fails review. When a release rollout completes, the flag and the dead branch are removed in the same work — removal is part of the feature's definition of done.
8. **BE-068 — Flags never replace authorization.** A flag may control visibility or rollout of a feature; the API still enforces who may use it on every request, flag or no flag.
9. **BE-069 — Flag changes are audited like deploys.** Every production flag change records actor, timestamp, previous and new value, and reason, in a log that survives the flag's removal.
10. **BE-070 — Experiments are pre-registered.** An experiment flag is created only with a hypothesis, a primary metric, and an end date recorded (with experimentation-platform). A flag created "to see what happens" is not an experiment.

## BAN list

- **BAN-BE-031 — The permanent flag.** Banned: a flag that will never be removed — `if (true)` in flag's clothing, a renamed leftover (`new_checkout_v2_final`), or a release flag still gating code two releases after rollout completed. Defeats: DET-CODE-001. Bad: the old checkout branch is unreachable behind a flag fixed at 100%, but every change must still be made twice "just in case." Instead: when rollout completes, delete the flag, the registry entry, and the dead branch in the same change (BE-067). Severity: WARN.
- **BAN-BE-032 — Flag as the only permission check.** Banned: protecting an operation by hiding it behind a flag or a UI toggle while the endpoint itself performs no authorization. Defeats: DET-FAKE-021. Bad: the admin export button renders only when `admin_tools` is on — and `GET /admin/export` answers any authenticated user who asks. Instead: keep the flag for visibility if useful, and enforce the role check server-side on the endpoint (BE-068, rbac). Severity: BLOCK.
- **BAN-BE-033 — Same flag, different defaults.** Banned: one flag key carrying different default values in different services or environments, so the system has no single answer to "is it on?" Defeats: DET-CODE-032. Bad: checkout enables the new pricing path by default while billing defaults to the old one, and orders price differently from invoices. Instead: one registry entry with one safe default; environments override the value explicitly, never the default (BE-061, BE-063). Severity: WARN.
- **BAN-BE-034 — The zombie flag.** Banned: flag keys that no code references anymore, left in the registry and in configuration after their feature shipped or was cut. Defeats: DET-CODE-002. Bad: the registry holds 140 flags, 60 of which no code path reads; reviewers can no longer tell which switches are live, so nobody dares touch any of them. Instead: removing a feature removes its flag everywhere; the registry-vs-codebase diff (G-BE-031) flags orphans in both directions. Severity: WARN.

## Gates

- **G-BE-031 — Registry-vs-codebase diff.** Verifies: BE-061, BE-067. Check: automated — extract every flag key referenced in code and diff against the registry; assert each referenced key exists with an owner and an unexpired date, and each registry entry is referenced by code. Pass: zero orphans in either direction, zero expired flags. Fail: block merge. Recorded in: progress.md.
- **G-BE-032 — Staging flip test.** Verifies: BE-063, BE-066. Check: automated — in staging, turn one release flag off and confirm the feature disappears with no redeploy and the fallback path renders and functions; turn it back on and confirm restoration. Pass: both directions clean. Fail: block the rollout. Recorded in: progress.md.
- **G-BE-033 — Bucketing stability test.** Verifies: BE-065. Check: automated — evaluate one percentage-rollout flag 100 times for each of a sample of user keys across two services; assert a stable variant per user and a distribution within tolerance of the configured percentage. Pass: zero flickers, distribution in tolerance. Fail: block the rollout. Recorded in: progress.md.
- **G-BE-034 — Flag-change audit review.** Verifies: BE-069. Check: manual — review the period's production flag changes; each must carry actor, reason, and previous/new values. Pass: 100% of changes fully recorded. Fail: warn, and complete the record before the next release. Recorded in: progress.md.

## Anti-patterns

- **Flag sprawl.** Dozens of live flags with no shared picture of which are on, so behavior becomes unexplainable. Catch it: pick one user-visible behavior and count the flags that can change it; if nobody can, the sprawl is already in charge.
- **The nested flag tower.** A code path depends on three or four flags in combination, creating a dozen variants nobody has tested. Catch it: if a function reads more than one flag, enumerate the combinations and ask which were ever run.
- **Expiry as paperwork.** The expiry date arrives and is simply extended, release after release, instead of triggering removal. Catch it: read the registry's history — a flag whose date moved three times is permanent and should be treated under BAN-BE-031.
- **The long-lived branch by flag.** A flag is used to develop a feature for months in production's shadow, so the "off" path and the "on" path diverge into two products. Catch it: release flags older than one release cycle are branches, with a branch's merge risk and none of its visibility.

## Examples

- [Example 1 — Permanent flag and dead branch removed at rollout completion](examples/example-1.md) — corrects BE-067.
- [Example 2 — Coin-flip bucketing replaced by deterministic hashing](examples/example-2.md) — corrects BE-065.
- [Example 3 — Flag-hidden admin feature gets real authorization](examples/example-3.md) — corrects BE-068.

## Recall anchors

- Registry before code: owner, type, safe default, expiry.
- The default is the safe value — an outage never enables the new path.
- Same user, same variant, every time.
- The off path is a product path; test it like one.
- A finished rollout deletes the flag, not just flips it.

## Checklist

- [ ] Every flag key in code exists in the registry with owner, type, default, and unexpired date (G-BE-031).
- [ ] Rollouts bucket deterministically on a stable user key (G-BE-033).
- [ ] The flag-off path is tested and the kill path works without a redeploy (G-BE-032).
- [ ] No flag is the only enforcement of a permission (BE-068).
- [ ] Completed rollouts have their flag and dead branch removed (BE-067).
- [ ] Production flag changes in the period are fully audit-logged (G-BE-034).
- [ ] Experiment flags carry a hypothesis, metric, and end date (BE-070).
