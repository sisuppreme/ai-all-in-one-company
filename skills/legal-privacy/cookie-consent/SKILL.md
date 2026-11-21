# cookie-consent

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/ ; https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng ; *Planet49*, C-673/17 (CJEU, 1 Oct 2019)
- **Depends on:** privacy-laws, audit-trails
- **Feeds into:** legal-documents, compliance-audit, dsar-handling

## When to use / Do NOT use

- **Use when:** a site or app sets cookies, loads SDKs or tags, or embeds third-party content; building or changing the consent banner, the tag-loading layer, the cookie inventory, or the privacy notice's cookie section; adding any new tracker, purpose, or third party.
- **Do NOT use when:** the question is which regime applies or whether consent is the right lawful basis at all — that is privacy-laws and, past its escalation stops, qualified counsel. This skill implements consent mechanics; it never declares a banner "compliant."

## Rules

1. **LG-081 — Inventory before banner.** Every cookie, SDK, tag, and embed is inventoried with name, owner, purpose, and lifetime, and classified strictly necessary (exempt) or consent-gated. The banner is built from the inventory, never the other way round.
2. **LG-082 — Default state is off.** An unclassified tracker is treated as non-essential and blocked until classified. Classification is a recorded decision in the inventory, not a developer's assumption at load time.
3. **LG-083 — Nothing non-essential fires before consent.** Enforcement lives in the tag-loading layer: no non-essential cookie is set and no non-essential third-party request fires until a consent state allowing that purpose exists. Banner copy is not an enforcement mechanism.
4. **LG-084 — Symmetric first layer.** Accept, reject, and granular purposes appear on the banner's first layer at equal prominence — same visual weight, same number of clicks. Rejecting is never more steps, smaller, dimmer, or deeper than accepting, and content is not walled off until the user accepts.
5. **LG-085 — No pre-ticked consent.** Every purpose toggle starts off; consent is a positive action by the user. A pre-ticked checkbox or pre-enabled toggle is invalid consent (*Planet49*, C-673/17).
6. **LG-086 — No implied consent.** Scrolling, continued browsing, inactivity, or closing the banner without choosing grants nothing. Until an explicit choice is recorded, the state stays "no consent" and LG-083 keeps applying.
7. **LG-087 — Granular per purpose.** Purposes are consented separately (e.g. analytics, marketing, functional); accept-all exists only alongside per-purpose choice, never as the only route. One purpose's consent never silently covers another.
8. **LG-088 — Consent is recorded as data.** Each consent event stores: subject or pseudonymous ID, timestamp, banner version, per-purpose choices, and capture mechanism. Without the record, consent cannot be demonstrated (GDPR Article 7(1)) even if the banner was perfect; records are queryable per subject and serve as DSAR evidence.
9. **LG-089 — Withdrawal is as easy as giving.** A persistent control (footer link or settings entry) reopens the choices in the same number of steps as giving consent. Withdrawal takes effect on the next page load: previously allowed tags stop firing and their cookies are removed or blocked.
10. **LG-090 — New purposes need fresh consent.** Adding a purpose or a third party bumps the banner version and re-prompts for the affected purposes only; existing consent never stretches to cover what the user never saw.
11. **LG-091 — One dataset, three renderings.** The cookie inventory, the banner's purpose list, and the privacy notice's cookie section are generated from one dataset. Drift between any two is a defect that fails review.
12. **LG-092 — Consent state is a runtime contract.** Analytics, marketing, and product code read consent state as an input and are tested against it like any feature flag. For CCPA-scope products the parallel mechanism — opt-out of sale/sharing plus honoring opt-out preference signals — is recorded the same way (LG-088).

## BAN list

- **BAN-LG-041 — Pre-ticked toggles.** Banned: shipping a banner whose purpose toggles or checkboxes start enabled, so doing nothing counts as agreeing. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: the analytics toggle renders on; a user who clicks "Save" without touching it is recorded as having consented to analytics. Instead: every toggle starts off and only a user's own action turns it on (LG-085). Severity: BLOCK.
- **BAN-LG-042 — Decorative reject.** Banned: a banner with no reject control, a reject buried in a settings layer the accept path never visits, or a reject button that closes the banner without recording or honoring refusal. Defeats: DET-CON-028. Bad: "Accept all" sits on layer one; "Reject" exists only inside a preferences modal, and clicking it sets a cookie the tag layer ignores. Instead: reject on the first layer at equal prominence, recorded and honored like any other choice (LG-084, LG-088). Severity: BLOCK.
- **BAN-LG-043 — Trackers loaded before consent.** Banned: analytics, advertising, or social tags placed in the page head or tag manager so they fire on first load, before any consent state exists. Defeats: DET-CON-015. Bad: the privacy notice says "we only track with your consent" while the landing page fires three third-party requests before the banner is even dismissed. Instead: gate every non-essential tag behind consent state in the loading layer (LG-083). Severity: BLOCK.
- **BAN-LG-044 — Choices that don't stick.** Banned: a rejection or withdrawal that the product forgets — the banner re-prompts every visit as if no choice was made, or tags resume after withdrawal. Defeats: DET-FAKE-016. Bad: a user rejects marketing cookies; next visit the banner returns at full size and the marketing pixel fires again "because the session is new." Instead: persist the recorded choice per subject and honor it across sessions until it expires or is changed (LG-088, LG-089). Severity: BLOCK.
- **BAN-LG-045 — Cookie lists that don't match reality.** Banned: a banner purpose list or privacy-notice cookie table that omits cookies the site actually sets, or lists cookies and purposes the site does not have. Defeats: DET-CON-014. Bad: the notice's cookie table, copied from a template, names a chat-widget cookie the product never had and omits the two analytics cookies it sets daily. Instead: render both lists from the single inventory dataset and diff them against observed cookies (LG-091, G-LG-044). Severity: WARN.

## Gates

- **G-LG-041 — Pre-consent network scan.** Verifies: LG-082, LG-083. Check (automated): a headless browser with a fresh profile loads the key pages with no interaction; capture every cookie set and every third-party request. Pass: zero non-essential cookies set and zero non-essential third-party requests fired before consent. Fail: block shipment. Recorded in: progress.md.
- **G-LG-042 — Consent-state test matrix.** Verifies: LG-087, LG-089, LG-092. Check (automated): scripted runs for accept-all, reject-all, partial (one purpose on), and withdraw-after-accept; assert exactly which tags fire in each state, including that withdrawal stops previously allowed tags on the next page load. Pass: observed tag behavior matches the recorded choice in all four runs. Fail: block shipment — a tag firing in the rejected state is a release blocker. Recorded in: progress.md.
- **G-LG-043 — Choice persistence check.** Verifies: LG-088, LG-089. Check (automated): reject all, reload, and return in a new session; assert the recorded choice is read back, no non-essential tag fires, and the banner does not re-prompt as if no choice existed. Pass: choice honored across reload and session. Fail: block shipment. Recorded in: progress.md.
- **G-LG-044 — Inventory drift diff.** Verifies: LG-081, LG-091. Check (automated): diff the cookie set observed in the G-LG-041/G-LG-042 runs against the inventory, the banner's purpose list, and the privacy notice's cookie section. Pass: the three renderings and the observed set agree exactly. Fail: block shipment until the dataset or the site is corrected. Recorded in: progress.md.
- **G-LG-045 — Symmetry and record review.** Verifies: LG-084, LG-085, LG-086, LG-088. Check (manual): inspect the first-layer banner — accept, reject, and purposes equally prominent, no toggle pre-enabled, no consent wall; then pull one stored consent record and confirm it carries subject, timestamp, banner version, and per-purpose choices, and reopen choices from the persistent control counting the steps. Pass: all hold. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Necessary-creep.** Borderline trackers get classified "strictly necessary" one by one until the exempt list does the tracking. Catch it by re-reading each exempt entry against the test: would the exact service the user asked for break without it?
- **Dark-pattern drift.** Banner A/B tests quietly optimize toward accept — brighter accept button, dimmer reject — with no compliance review of the variants. Catch it by treating every banner variant as a compliance surface that passes G-LG-045 before it runs.
- **Version amnesia.** Banner purposes or wording change but the banner version stays the same, so stored consent records no longer say what users actually agreed to. Catch it by tying the version string to the purposes dataset (LG-091): a purposes diff without a version bump fails review.
- **Signal blindness.** An opt-out preference signal is honored for logged-in users only, or recorded but never wired into the tag layer. Catch it by including a signal-present run in the G-LG-042 matrix.

## Examples

- [Example 1 — The pre-ticked analytics toggle](examples/example-1.md) — violates/corrects LG-085.
- [Example 2 — Reject in the basement](examples/example-2.md) — violates/corrects LG-084.
- [Example 3 — Withdrawal that actually stops the tags](examples/example-3.md) — violates/corrects LG-089.

## Recall anchors

- Default is off: unclassified means blocked, not loaded.
- Reject is one click, same size, same layer as accept.
- Nothing fires before consent — enforcement is in the loader, not the copy.
- Consent is a record: who, when, which version, which purposes.
- Withdrawal stops the tags on the next page load, not eventually.

## Checklist

- [ ] Every cookie, SDK, and tag is inventoried and classified (LG-081, LG-082).
- [ ] Pre-consent scan shows zero non-essential cookies or requests (G-LG-041).
- [ ] First layer offers accept, reject, and purposes at equal prominence; no consent wall (LG-084, G-LG-045).
- [ ] No toggle or checkbox is pre-enabled; no consent is implied by browsing (LG-085, LG-086).
- [ ] Consent-state matrix passes for accept-all, reject-all, partial, and withdraw (G-LG-042).
- [ ] Choices persist across reloads and sessions (LG-088, G-LG-043).
- [ ] Withdrawal is reachable in the same steps as giving and stops tags next load (LG-089).
- [ ] Inventory, banner purposes, and notice cookie section agree with observed cookies (LG-091, G-LG-044).
