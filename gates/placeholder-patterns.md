# placeholder-patterns.md — Placeholder-scan pattern list (§6.2)

The versioned fingerprint list for the `placeholder-scan` skill (D8). This file is the list the skill's QA-284 rule refers to: the static sweep runs these patterns over the **production build output** (QA-282 — scan the artifact you ship, not the demo you staged), and the dynamic pass runs the probe patterns against the running build. Gate: G-QA-141 (static sweep clean), G-QA-143 (dynamic checklist complete), both in `skills/qa-testing/placeholder-scan/SKILL.md`.

**Maintenance (QA-283, QA-290).** Every fake that reaches production adds its fingerprint to this list and its probe to the dynamic section in the same change that fixes it. Removing or loosening a pattern requires the same waiver record as loosening any qa-gate: named owner, reason, expiry. Patterns are loosened by evidence, not by annoyance — known legitimate matches belong in `gates/placeholder-allowlist.md`, not in a weaker pattern.

**Tiers (Master Brief §6.2 step 5).** Tier 1 is the no-tooling checklist scan of all visible copy plus a manual click-through of every button, link, and form. Tier 2 is the scripted scan below. A Tier 1 hit fails the gate; a Tier 2 hit fails unless allowlisted. The gate records which tier ran.

**Severity.** Each finding is filed as a defect at the severity of the DET parameter it matches (QA-289), naming the DET ID and the fingerprint or probe that caught it. Classes per `gates/DEFECT_TAXONOMY.md`.

## Tier 2 — Static fingerprints (shipped artifact)

| # | Pattern (match against rendered output and shipped strings) | Scope notes | Operationalizes |
|---|---|---|---|
| S-01 | `lorem`, `ipsum`, `dolor sit amet`, and lorem-variant fragments (pseudo-Latin filler from any generator) | Body copy, headings, `<title>`, meta. Quoted-as-subject exception: allowlist A-08. | DET-CON-001 |
| S-02 | Template and CMS defaults for the stack in use: `Hello world!`, `Just another WordPress site`, `Add a description here`, `Your text here`, installer sample pages and theme demo copy | Known default strings per stack; list the installer's pages. Demo-framing exception: DET-CON-002's false-positive clause. | DET-CON-002 |
| S-03 | Unrendered template syntax: `{{`, `}}`, `${`, `%s`; literal `undefined`, `null`, `NaN`, `[object Object]` in prose or titles | Exclude documented code-sample contexts (`<code>`/`<pre>`): allowlist A-09. | DET-CON-003 |
| S-04 | Developer markers in shipped strings: `TODO`, `FIXME`, `XXX`, stub markers; `xxxxx`, `test test` | User-visible copy, fields, meta, alt text. Code comments are NOT this pattern: allowlist A-02. | DET-CON-004 |
| S-05 | `coming soon`, `content to follow`, `under construction` in live fields, meta descriptions, or alt text | Changelog/roadmap exception with a date: allowlist A-10. | DET-CON-004 |
| S-06 | Placeholder contacts: `example.com`, `example@`, `555-01`, `123 Main Street` | Live contact blocks, footers, checkout help text. Instructional/documentation exception: allowlist A-11. | DET-CON-005 |
| S-07 | Fake-name list: `John Doe`, `Jane Smith`, `Test User`, `Acme` — plus **any person name presented as a customer, reviewer, team member, or user that the project's fact-sheet does not contain** | The fact-sheet comparison is the general form of this pattern (brief §6.2 step 5); the named strings are its starter set. | DET-FAKE-014 (people as users), DET-CON-010 (testimonial slots), DET-CON-013 (review slots) |
| S-08 | Round-number social proof with no fact-sheet entry: numeric-pattern heuristics such as `10,000+ happy customers`, round counts of users/customers/projects with no source | A hit is a flag for fact-sheet verification (step 1b), not proof of fabrication by itself; unsourced-on-page alone is not a finding — see allowlist A-13/A-14. | DET-CON-011 |
| S-09 | Placeholder media: `via.placeholder.com`, `placehold.co`, `dummyimage.com` and similar placeholder-image services; grey-box assets; stock or generated images presented as the real team, customers, or product | Production routes only; provenance check per brief §6.2 (fake imagery class). Named-real-people exception: DET-CON-019's professional pattern. | DET-CON-019 (per placeholder-scan QA-292) |
| S-10 | Fixture and seed fingerprints in the shipped bundle: seed/fixture files imported by production code paths, hardcoded fixture arrays rendered as catalog/user/testimonial data, `seed: true` records or demo-mode flags in the production build | Sweep checks imports and bundle contents, not just visible copy (QA-291). Labeled demo exception: allowlist A-05. | DET-FAKE-014 |
| S-11 | `href="#"` and equivalent no-op targets on controls presented as navigation or actions | Static hit is a flag; the verdict comes from the Tier 1 click-through / dynamic probe. In-page fragment links that actually navigate are allowlisted (A-01). Forms that submit nowhere are D-01 below. | Fake-functionality class (brief §6.2); filed under the DET-FAKE parameter the probe matches |

## Dynamic probes (running build, per interactive feature — QA-285, QA-286)

Every release: the persistence test (act, reload, sign in again — the change must survive) and the network test (the action must produce a real request and a stored result) run for each interactive feature, plus the wrong-password, decline-card, and fresh-account probes where applicable. A success UI state with no corresponding server write is a blocker finding by definition (QA-285).

| # | Probe pattern | Operationalizes |
|---|---|---|
| D-01 | Form shows success ("Message sent", "Subscribed", toast) with no request fired, or a request whose payload is discarded | DET-FAKE-015 |
| D-02 | Login accepts a deliberately wrong password or a random string | DET-FAKE-001 |
| D-03 | Post-login state is a `localStorage` flag; direct API request without the session is not refused server-side | DET-FAKE-002 |
| D-04 | Signup shows "Account created" but no record exists; the same email registers twice | DET-FAKE-003 |
| D-05 | Dashboard figures do not move when a record they should count is created or deleted | DET-FAKE-004 |
| D-06 | Like/view/cart counters reset to their base value on hard reload | DET-FAKE-005 |
| D-07 | Checkout confirms an order with no provider call and no provider payment ID | DET-FAKE-006 |
| D-08 | The provider's documented decline test card is accepted | DET-FAKE-007 |
| D-09 | Search returns the same fixture list for unrelated queries; a just-created record is not findable; gibberish returns results instead of an honest empty state | DET-FAKE-008 |
| D-10 | "AI" feature returns canned/template responses; no model or retrieval call in the network capture; a question answerable only from a supplied document fails | DET-FAKE-009 |
| D-11 | Admin edit shows "Saved" but is gone on reload or invisible on the public surface | DET-FAKE-010 |
| D-12 | Deleted item reappears on reload, in search, or at its direct URL, with no visible archived/trash state | DET-FAKE-011 |
| D-13 | Upload shows a completed state but the asset resolves only as a `blob:` URL or reverts on reload | DET-FAKE-012 |
| D-14 | A brand-new account starts with a staged notification feed instead of an empty one | DET-FAKE-013 |
| D-15 | Profile/settings change toasts success but reverts on reload or differs across devices | DET-FAKE-016 |
| D-16 | Filters/sort/pagination only rearrange a small fixture: page 2 repeats page 1, counts disagree with results | DET-FAKE-017 |
| D-17 | "Live" viewers/online/activity indicators drift on a random timer, disagree across two browsers, or cycle scripted entries | DET-FAKE-018 |
| D-18 | Export/download produces a static sample file whose contents ignore current data and filters | DET-FAKE-019 |
| D-19 | Password reset "succeeds" but the old password still works or no email ever arrives for a real account | DET-FAKE-020 |
| D-20 | A privileged request replayed from a low-privilege account is not rejected server-side (role enforced only by hidden UI) | DET-FAKE-021 |
| D-21 | "Saved"/sync indicator claims completion before the server response; work is lost when the tab is killed, or success is claimed with the network disabled | DET-FAKE-022 |

## Seeded-fault control (QA-287, G-QA-142)

This list is itself tested: a throwaway branch seeded with one stub handler, one fixture-rendered list, and one lorem ipsum paragraph must make the sweep exit non-zero with all three seeds reported. A scanner that passes the seeded branch is broken and blocks releases until repaired.
