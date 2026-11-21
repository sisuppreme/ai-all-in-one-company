# placeholder-scan

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** SquirrelScan content rules, "Placeholder text" — https://docs.squirrelscan.com/rules/content/placeholder-text ; VerifixScan, "Placeholder text in production" — https://www.verifixscan.com/problems/placeholder-text-in-production ; skills/detection/fake/PARAMETERS.md (DET-FAKE-001…022) and skills/detection/content/PARAMETERS.md (DET-CON-001…028) in this repo
- **Depends on:** qa-gates
- **Feeds into:** bug-triage, browser-verification, e2e-testing

## When to use / Do NOT use

- **Use when:** before every release, and whenever a feature claims to work end to end — run the scan to prove no placeholder copy, stub handler, fixture data, or simulated function ships in the production build.
- **Do NOT use when:** judging whether a real function is correct (that is e2e-testing and browser-verification), or flagging a clearly labeled demo or sample — a labeled demo is honest and is never a finding. Fixes belong to the builder skill named in the DET parameter's Fix field; this skill produces the verdict, not the repair.

## Rules

1. **QA-281 — Two passes, both mandatory.** Every release runs the static pass (pattern sweep of the shipped artifact) and the dynamic pass (the DET-FAKE probe checklist against the running build). Neither pass alone clears a release.
2. **QA-282 — Scan the shipped artifact.** Scope is the production bundle, production routes, and production seed state. A clean staging demo does not clear a dirty production build. The static sweep scans rendered output, not source: run the pattern list over the built pages and shipped strings as a user receives them, never over source files — template-syntax patterns false-positive on source constructs (the `${` fingerprint matches every JavaScript template literal). Source files are in scope only for QA-291's import and bundle-content check.
3. **QA-283 — The pattern list is versioned.** The fingerprint list lives in the repo as a reviewed file. Every fake that reaches production adds its fingerprint to the static list and its probe to the dynamic checklist in the same change that fixes it.
4. **QA-284 — Static fingerprints, exact set.** The sweep covers at minimum: `lorem|ipsum|dolor sit amet`; `TODO|FIXME|XXX` and stub markers in shipped strings; unrendered template syntax (`{{`, `}}`, `${`, `[object Object]`, literal `undefined`/`NaN` outside code blocks); placeholder contacts (`example.com`, `example@`, `555-01`, `123 Main Street`); "coming soon" / "content to follow" in live fields, meta, and alt text; known template/CMS default strings for the stack in use.
5. **QA-285 — Success without a write is a blocker.** A success UI state (toast, confirmation page, "saved" indicator) with no corresponding server write in the network capture is a blocker finding by definition, filed against the matching DET-FAKE parameter — never a style note.
6. **QA-286 — Dynamic probes per interactive feature.** Each interactive feature gets, per release: the persistence test (act, reload, log in again — the change must survive), the network test (the action must produce a real request and a stored result), the wrong-password probe on auth, the decline-card probe on payment, and the fresh-account emptiness check (a new account shows empty states, not staged content).
7. **QA-287 — Seeded-fault negative control.** The scan is itself tested: a throwaway branch seeded with a stub handler and a fixture-rendered list must make the sweep exit non-zero. The control runs in CI on a schedule; a scanner that passes the seeded branch is broken and blocks releases until repaired.
8. **QA-288 — Allow-list entries expire.** Every allow-list entry names the visible label that makes the exception honest (demo banner, "sample" tag) and an expiry tied to a named release. An expired entry fails the scan like any other hit.
9. **QA-289 — Findings are defects, with provenance.** Each finding is filed in bug-triage at the severity of the DET parameter it matches (blocker for undisclosed simulation of a core function), naming the DET ID and the fingerprint or probe that caught it.
10. **QA-290 — The scan never grades its own homework.** The scan configuration is reviewed repo code. Removing or loosening a pattern requires the same waiver record as loosening any qa-gate: named owner, reason, expiry.
11. **QA-291 — Fixtures stay unreachable.** Seed and fixture files must not be imported by, bundled into, or reachable from production code paths. The sweep checks imports and bundle contents, not just visible copy.
12. **QA-292 — Placeholder media counts.** Stock or generated images presented as the real team, real customers, or real product shots are findings (DET-CON-019), as are placeholder image URLs and grey-box assets in production routes.

## BAN list

- **BAN-QA-141 — Lorem ipsum in the build.** Banned: any lorem ipsum or variant fragment in shipped copy, headings, or titles. Defeats: DET-CON-001. Bad: the pricing page ships with "Lorem ipsum dolor sit amet" under two plan tiers. Instead: write the final plan copy from the fact sheet, or remove the section until the copy exists. Severity: BLOCK.
- **BAN-QA-142 — Success toast, no request.** Banned: a form or action that shows success without issuing a request or storing anything. Defeats: DET-FAKE-015. Bad: the contact form shows "Message sent!" while the network capture shows zero requests and no record is created. Instead: wire the form to the real endpoint and show success only after a confirmed server response. Severity: BLOCK.
- **BAN-QA-143 — Fixture array as the live catalog.** Banned: hardcoded fixture or seed arrays rendered as the product catalog, user list, or testimonial set. Defeats: DET-FAKE-014. Bad: the storefront renders a `const products = [...]` literal with invented names, prices, and five-star quotes. Instead: render from the real data source; with no data, show the designed empty state. Severity: BLOCK.
- **BAN-QA-144 — Placeholder contact details.** Banned: `example@` addresses, 555-01xx numbers, or template street addresses in live contact blocks, footers, or checkout help text. Defeats: DET-CON-005. Bad: the footer lists support@example.com and (555) 014-2200 on the production site. Instead: publish the real, monitored contact details, verified by a test message before release. Severity: BLOCK.
- **BAN-QA-145 — Timer-driven "live" indicators.** Banned: "live", "online now", viewer counts, or activity feeds driven by random timers or rotation through staged entries. Defeats: DET-FAKE-018. Bad: a "128 people viewing" badge whose number is `Math.floor(Math.random()*50)+100` on a 5-second interval. Instead: bind the indicator to the real presence/analytics source, or remove the badge. Severity: BLOCK.

## Gates

- **G-QA-141 — Static sweep clean.** Verifies: QA-282, QA-284, QA-291, QA-292. Check: automated — run the versioned pattern list over the rendered production output (built pages and shipped strings), e.g. `rg -i -n "lorem|ipsum|dolor sit amet|example\.com|example@|555-01|coming soon|content to follow" dist/` plus the template-syntax and stub-marker patterns from the pattern file; exclude documented code-sample contexts. Scan rendered output, not source: copy and template-syntax patterns run against the build output only (against source they false-positive, e.g. `${` in JavaScript template literals); source is examined only for QA-291's fixture-import fingerprints. Pass: exit 0 with zero unallow-listed hits. Fail: block the release; each hit is filed per QA-289. Recorded in: progress.md.
- **G-QA-142 — Seeded-fault control.** Verifies: QA-287. Check: automated — on the seeded throwaway branch (one stub handler returning success, one fixture-rendered list, one lorem ipsum paragraph), run the same sweep command as G-QA-141. Pass: exit code non-zero and all three seeds reported. Fail: the scanner is treated as broken; releases block until the control passes again. Recorded in: progress.md.
- **G-QA-143 — Dynamic checklist complete.** Verifies: QA-285, QA-286. Check: per release, the DET-FAKE checklist is executed against the running production build; every interactive feature has filed evidence for its persistence test and network test, plus the wrong-password, decline-card, and fresh-account probes where applicable. Pass: evidence exists for 100% of interactive features and no success-without-write observation stands. Fail: block the release; each gap or fake is filed per QA-289. Recorded in: progress.md.
- **G-QA-144 — Allow-list audit.** Verifies: QA-288, QA-290. Check: automated — a script reads the allow-list file and confirms every entry names its honesty label and an expiry release that has not yet shipped. Pass: zero expired or unlabeled entries. Fail: block the release until entries are renewed with a waiver record or the exceptions are removed. Recorded in: progress.md.

## Anti-patterns

- **Scanner theater.** The sweep runs against the source tree while the shipped bundle is built differently, so the scan certifies an artifact nobody ships. Catch it: the gate command's target path is the build output directory, and the seeded-fault control (G-QA-142) seeds the built artifact, not just source.
- **Green by deletion.** A finding is closed by deleting its pattern from the list instead of fixing the fake. Catch it: pattern-list diffs are reviewed like gate changes (QA-290); a shrinking list with no corresponding code fix is the tell.
- **Demo creep.** A "temporary" demo mode with staged data quietly becomes the production experience, its banner removed in a redesign. Catch it: allow-list expiries (QA-288) force the demo to be re-justified or removed every release.
- **English-only fingerprints.** The pattern list covers English placeholder copy, so localized filler and template defaults in other languages sail through. Catch it: when a locale ships, its placeholder strings and CMS defaults are added to the list in the same change.

## Examples

- [Example 1 — Lorem ipsum and placeholder contacts in the shipped footer](examples/example-1.md) — corrects QA-284.
- [Example 2 — A contact form whose success toast fired with no request](examples/example-2.md) — corrects QA-285.
- [Example 3 — A fixture array rendered as the live product catalog](examples/example-3.md) — corrects QA-291.

## Recall anchors

- Scan the artifact you ship, not the demo you staged.
- Success with no server write is a blocker, full stop.
- Every escaped fake leaves a fingerprint and a probe behind.
- Allow-list entries name their label and expire.
- A labeled demo is honest; an unlabeled one is a finding.

## Checklist

- [ ] Static sweep ran on the rendered production output — not source — and exited 0 (G-QA-141).
- [ ] Seeded-fault control still bites: the seeded branch exits non-zero (G-QA-142).
- [ ] Dynamic checklist evidence filed for every interactive feature (G-QA-143).
- [ ] No success UI state lacks a matching server write in the network capture (QA-285).
- [ ] Fresh-account check shows real empty states, not staged content (QA-286).
- [ ] Allow-list has no expired or unlabeled entries (G-QA-144).
- [ ] Every finding is filed as a defect with its DET ID and severity (QA-289).
- [ ] Any new fake found this release added its fingerprint and probe to the lists (QA-283).
