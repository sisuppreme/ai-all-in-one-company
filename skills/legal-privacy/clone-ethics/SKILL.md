# clone-ethics

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.rfc-editor.org/rfc/rfc9309.html
- **Depends on:** audit-trails, licensing
- **Feeds into:** site-discovery, asset-harvesting, behavior-cloning, page-reconstruction, fidelity-verification

## When to use / Do NOT use

- **Use when:** any work would crawl, inventory, harvest from, or replicate an existing site — before the first request is made — to create the authorization record, rule on per-asset rights decisions, and set the crawl-conduct limits that D16 (site-discovery, asset-harvesting, behavior-cloning, page-reconstruction) then executes inside.
- **Do NOT use when:** the work is the technical replication itself (that is D16; this skill sets the gate D16 must pass, it does not crawl or rebuild), the question is a dependency or font license (licensing), or the rights position is contested — a disputed ownership claim, a former vendor's build, a franchise — where the correct output is to stop and require qualified counsel. This skill is implementation guidance, not legal advice.

## Rules

1. **LG-181 — Authorization precedes access, structurally.** A written authorization record exists in the project file before any crawl, inventory fetch, or harvest request touches the target. The record is a pre-committed artifact — a dated file committed to the repo — and the crawl tooling checks for it and fails closed when it is absent, stale, or out of scope. A verbal go-ahead, a chat message, or a record written after crawling started does not satisfy this rule.
2. **LG-182 — Legitimate grounds are a closed list.** Clone work proceeds only on one of four grounds, named in the authorization record: (a) the operator's own property; (b) written authorization from the client or rights holder; (c) public-domain or expired rights, with the expiry basis stated; (d) an interoperability study that copies no protected expression (behavior and interfaces observed, expression never lifted). A ground not on this list — "it is publicly visible", "everyone clones competitors", "only for inspiration" — is not a ground.
3. **LG-183 — The record names who, their right, and the scope.** The authorization record states: the authorizer's name and role, the basis of their right to authorize (owner, licensee, client of record), the target domains, the asset classes in scope, the purpose of the clone, and the date. If any element is ambiguous — an agency cloning a client's site, a build a former vendor claims rights in — work stops at inventory (URLs only, no harvesting) until the position is resolved in writing.
4. **LG-184 — Every asset carries a rights decision.** Each asset class in the harvesting manifest — layout, copy text, images, fonts, logos, data — carries exactly one decision: `owned`, `licensed`, `recreate`, or `replace`, prepared with evidence by D16 and approved under this skill. An asset with no decision defaults to `replace`; an undecided asset is never harvested "pending" a decision.
5. **LG-185 — `licensed` is never self-approved.** A `licensed` decision is a legal judgment — license scope, transferability, territory — and the harvesting flow cannot approve its own. Structurally: the manifest tooling rejects any `licensed` row whose approver is the same actor that prepared the harvest, and the row must attach the license evidence (the license text or grant, its scope, and why it covers this reuse). No evidence attached, no `licensed` decision. **Single-operator mode is a named variant, never a silent deletion.** Where one operator runs the whole engagement, no second approver exists, so the separation is rebuilt from artifacts instead of people: (a) the authorization record is created and committed before any harvest, timestamped, and names the specific license evidence the `licensed` decision relies on; (b) the license document itself — the text or grant a second approver would have checked — is attached to or cited by the manifest row; (c) the operator records a self-check of the row against the license terms (scope, transferability, territory) as a separate, later step in progress.md, after the harvest, never in the same act as preparing it. Without all three, the `licensed` class is closed to a solo operator: the row reads `replace`. Every other part of this rule applies unchanged; the two-person form above remains the general case wherever a second approver exists.
6. **LG-186 — Protected expression is never replicated for a competing product.** Trademarks, logos, trade dress, copy text, and proprietary images or photography from the target are never carried into a clone that will compete with or substitute for the source — regardless of how the crawl was authorized. The sole exception is reuse the authorization explicitly covers word-for-word, such as the client's own brand assets in their own migration.
7. **LG-187 — Recreate the pattern, never the identity.** Layout patterns, interaction behavior, and information architecture may be recreated in original code. A competitor clone ships with different branding, different copy, and different imagery; if a side-by-side viewer could mistake the clone for the source brand, the clone fails this rule even if every file was rewritten from scratch.
8. **LG-188 — Crawl conduct is identified, permitted, and polite.** The crawler identifies itself honestly (a user agent naming the project and a contact), fetches and honors the target's robots.txt in full before the first crawl request, and respects the site's stated terms and reasonable rate limits. Every domain's robots check is logged with its date before crawling begins.
9. **LG-189 — Blocks are never worked around.** No login with borrowed, shared, or client-unrelated credentials; no paywall circumvention; no mirror, cache, or alternate-route harvesting of a blocked source. A blocked or robots-excluded target is dropped, the drop is logged with reason and date, and any exception is an explicit written decision under this skill — never a crawler configuration change.
10. **LG-190 — Robots silence is not a rights license.** An absent robots.txt, or one without a Disallow, speaks only to crawl access: RFC 9309 states robots rules "are not a form of access authorization", and they say nothing at all about reuse rights. Crawl permission under LG-188 never upgrades an asset's rights decision under LG-184.
11. **LG-191 — Decisions are audit-trail entries.** The authorization record and every rights decision — approver, date, basis, evidence reference — are filed as audit-trail entries under the audit-trails skill. A decision that exists only in a chat thread or a crawler config comment does not exist.
12. **LG-192 — No parity claims, and contested calls escalate.** Pages that were designed rather than cloned carry no parity or "identical to" claim in the delivery report or anywhere else. Where the rights position is genuinely contested or novel, this skill's output is a stop: work holds at inventory until qualified counsel resolves it in writing.

## BAN list

- **BAN-LG-091 — Crawl first, authorize later.** Banned: any discovery crawl, inventory fetch, or harvest that runs before the authorization record's date, with the record written afterward to match what already happened. Defeats: DET-CRWL-014. Bad: the team crawls a client's old site on Monday "to scope the job" and files the authorization record on Friday once the client signs. Instead: commit the dated authorization record first and let the pre-flight gate (G-LG-091) refuse any crawl that predates it, under LG-181. Severity: BLOCK.
- **BAN-LG-092 — The brand lift called a template.** Banned: shipping a clone that keeps the source's logo, copy, photography, or trade dress — end to end or in part — and describing it as a template, a starting point, or a faithful rebuild. Defeats: DET-CRWL-009. Bad: a competitor's pricing page is rebuilt with its headline copy, product photos, and logo intact, delivered as "pixel-perfect clone". Instead: recreate layout and behavior in original code with different branding, copy, and imagery, under LG-186 and LG-187. Severity: BLOCK.
- **BAN-LG-093 — Borrowed-credential or paywall-bypass harvesting.** Banned: reaching protected content with someone else's login, a shared account, a session cookie, or a mirror/cache route around a login wall, paywall, or crawler block. Defeats: DET-CRWL-008. Bad: a teammate's personal subscription login is used to scrape a members-only template gallery the project has no rights in. Instead: drop the source, log the drop with reason and date, and proceed only on an explicit written decision under LG-189. Severity: BLOCK.
- **BAN-LG-094 — The harvester approves its own `licensed` call.** Banned: a manifest row marked `licensed` where the same run, agent, or person that harvested the asset also recorded the approval — or where no license evidence is attached. Defeats: DET-CRWL-007. Bad: the harvest report marks 40 stock photos `licensed — "they were on the client's old site"` with the harvester as approver and no license on file. Instead: attach the license evidence and route the decision to a separate approver under LG-185 — or, where no second approver exists, complete LG-185's single-operator mode in full; without evidence the decision is `replace`. Severity: BLOCK.
- **BAN-LG-095 — Robots silence read as permission.** Banned: treating a missing robots.txt, a missing Disallow, or a permissive crawl policy as authorization to copy and reuse the site's assets, text, or branding. Defeats: DET-CRWL-016. Bad: "their robots.txt allows everything, so we can lift the photo library" appears in the harvest plan. Instead: let robots rules govern crawl access only, and decide reuse per asset under LG-184 and LG-190. Severity: BLOCK.

## Gates

- **G-LG-091 — Pre-flight authorization check.** Verifies: LG-181, LG-182, LG-183. Check (automated): before any crawl or harvest tooling runs, a script asserts the project's authorization record file exists, is dated, names the authorizer, their right to authorize, one of the four LG-182 grounds, the in-scope domains and asset classes — and that its commit timestamp predates the current run. The crawler refuses to start when the check fails. Pass: record complete, in scope, and pre-committed. Fail: block the run (fail closed). Recorded in: progress.md.
- **G-LG-092 — Authorization-vs-crawl timestamp comparison.** Verifies: LG-181, LG-191. Check (automated): compare the authorization record's timestamp against the first entry in the project's crawl log; also assert every rights decision in the manifest has a matching audit-trail entry. Pass: record predates first crawl entry, and every decision is trailed. Fail: block delivery; a crawl-first sequence is recorded as a finding, not cured retroactively. Recorded in: progress.md.
- **G-LG-093 — Manifest completeness and approval check.** Verifies: LG-184, LG-185. Check (automated): scan the harvesting manifest — every asset file has a row, every row has a decision, every `licensed` row attaches license evidence and either names an approver different from the harvesting actor or satisfies all three LG-185 single-operator conditions (pre-committed authorization record naming the evidence, license attached or cited, separate later self-check recorded in progress.md), and every undecided row reads `replace`. Pass: zero gaps, zero `licensed` rows self-approved outside those conditions. Fail: block delivery until each row is cleared or replaced. Recorded in: progress.md.
- **G-LG-094 — Brand-residue scan.** Verifies: LG-186, LG-187. Check (automated): grep the rebuild for the source's brand names, trademarked terms, and slogans, and hash-compare shipped media against the harvested-asset set; any hit outside the authorization's explicitly approved reuse list blocks. Pass: zero unapproved residue. Fail: block delivery until each hit is removed or proven covered by the authorization. Recorded in: progress.md.
- **G-LG-095 — Crawl-conduct log audit.** Verifies: LG-188, LG-189, LG-190. Check (automated + manual): review the crawl log — a robots.txt fetch is logged per domain before its first content request, no disallowed path appears, the user agent identifies the project, request rates stay within the recorded limit, and no authenticated or paywalled URL was fetched. Pass: conduct matches the log on every point. Fail: block delivery and file each breach as a finding. Recorded in: progress.md.

## Anti-patterns

- **The retroactive paper trail.** The authorization record's prose describes the crawl suspiciously well — because it was written after it. Catch it by trusting only the commit timestamp (G-LG-092), never the date typed in the document.
- **Scope creep by asset class.** The authorization covers layout study, but photography and copy quietly join the harvest "since we were already there". Catch it by diffing the manifest's asset classes against the record's scope line before harvesting starts.
- **Inspiration laundering.** A lifted page is paraphrased just enough — synonyms swapped, one photo changed — and relabeled "inspired by". Catch it with the side-by-side test in LG-187: if a viewer could mistake it for the source brand, it is a clone, not an inspiration.
- **The exception that became the route.** One written bypass decision for a single blocked page turns into the crawler's standing configuration for the whole domain. Catch it by expiring every LG-189 decision to the exact URLs it names and re-deciding any expansion.

## Examples

- [Example 1 — The crawl that started before the paperwork](examples/example-1.md) — violates/corrects LG-181, LG-183.
- [Example 2 — "Licensed", approved by the harvester](examples/example-2.md) — violates/corrects LG-184, LG-185.
- [Example 3 — The template that kept the brand](examples/example-3.md) — violates/corrects LG-186, LG-187.

## Recall anchors

- No record, no crawl — the tooling fails closed.
- Grounds are a closed list of four; "it was public" is not one of them.
- `licensed` is a judgment the harvester can never make about its own harvest.
- Robots rules govern access, never reuse rights.
- Recreate the pattern; never ship the identity.

## Checklist

- [ ] The authorization record is committed, dated, and names the authorizer, their right, an LG-182 ground, scope, and purpose — before any crawl ran (LG-181, LG-182, LG-183, G-LG-091, G-LG-092).
- [ ] Every manifest asset has a rights decision; undecided assets read `replace` (LG-184, G-LG-093).
- [ ] Every `licensed` row attaches license evidence and names a separate approver — or, in single-operator mode, meets all three LG-185 artifact conditions (LG-185, G-LG-093).
- [ ] No trademark, logo, trade dress, copy, or proprietary imagery ships in a competing clone (LG-186, LG-187, G-LG-094).
- [ ] The crawl log shows an identified crawler, a robots check per domain, respected rate limits, and no bypassed blocks (LG-188, LG-189, G-LG-095).
- [ ] No reuse decision rests on robots.txt silence (LG-190).
- [ ] The authorization record and all rights decisions exist as audit-trail entries (LG-191, G-LG-092).
- [ ] Designed-not-cloned pages carry no parity claim, and contested rights are escalated in writing, not decided in the run (LG-192).
