# Playbook — Clone / Rebuild

## Goal

Rebuild an existing website or web app as a new, original implementation that matches the source's structure, design language, and behavior — without copying protected assets, code, or copy. The rebuild is evidence-led: what can be observed and verified is reconstructed; what cannot (auth-gated pages, backend behavior) is designed fresh in the same design system and **marked designed-not-cloned**, never presented as a verified copy.

## Departments + order

Step 0 (always-on core) → **D14 pre-flight (authorization only)** → D16 → D3+D13+D4+D5 → D14 (full) → D12 → D7+D8 → D6 → D9

**Order deviation (one line):** D14's clone-ethics pre-flight runs before D16, not after the build group as the brief's summary table suggests, because the authorization record must exist and predate the first crawl — everything else follows the table.

## Skills to load

Load this playbook's bundle first: `bundles/clone-rebuild.md`. Then, per step:

| Skill | Bundle |
|---|---|
| project-templates, progress-tracking | `bundles/core.md` |
| secrets-management, qa-gates | `bundles/core.md` |
| clone-ethics | `bundles/legal-privacy.md` |
| site-discovery, page-inventory, design-extraction, asset-harvesting, behavior-cloning, page-reconstruction, fidelity-verification | `bundles/cloning-replication.md` |
| frontend-core, design-tokens, component-library | `bundles/frontend.md` |
| accessibility-audit, wcag | `bundles/accessibility-i18n.md` |
| api-building | `bundles/backend.md` |
| schema-design | `bundles/database.md` |
| privacy-laws, legal-documents | `bundles/legal-privacy.md` |
| performance-budgets | `bundles/analytics-observability.md` |
| owasp, placeholder-scan | `bundles/security.md`, `bundles/qa-testing.md` |
| ci-cd, hosting | `bundles/devops-deployment.md` |
| technical-seo | `bundles/seo-content.md` |

Conditional: if the rebuild adds AI features the source did not have, that is new product work — run the SaaS playbook's D17 step for those features only. If the rebuild needs support surfaces, add a D18 step (help-center, user-onboarding) before D9.

## Docs to write first

1. `fact-sheet.md` — the source site's verified facts (owner, purpose, public claims) with sources; nothing about the source is asserted without evidence.
2. **Authorization record** (per clone-ethics) — who authorized the rebuild, the legal basis (own site, client engagement, public-reference study), scope, and date. Written and committed **before any crawl**.
3. `progress.md` — playbook trace, gate results, deviation log.
4. Page inventory (produced by D16, but its file and classification scheme are agreed before discovery starts).

## Pattern-reference mode (no crawlable target)

**When it applies.** The authorization record names a *pattern class* — the typical structure, components, and interactions of a kind of site — and **zero target domains**. Nothing is crawled, fetched, scraped, or harvested; the ground is normally LG-182(d), an interoperability study that copies no protected expression. This mode is named because the standard path presupposes one concrete crawlable target: without one, roughly half the D16 gates would otherwise be vacuous or un-runnable, answerable only by ad-hoc waiver. When the authorization record names no target domains, this section governs: steps 2–5 and 9 follow the dispositions below in place of their standard text, and every ADAPTED or NOT APPLICABLE disposition actually used is recorded in the deviation log (G-CL-064, adapted).

**What replaces the crawl artifacts.**

- **Pattern inventory** — written first, alongside the authorization record: the pattern class's route types, component patterns, and interaction patterns, written from public knowledge, plus a **protected-items list** (the brand names, marks, and copy characteristic of the class that must never be reproduced). It replaces the sitemap and CDX URL lists, the WARC records, the source captures, and the robots fetches as the evidence base.
- **Crawl log** — still kept, and records **zero fetches**. It is the negative evidence that no crawl happened, and several gates below read it.
- **Design tokens** — authored originals for the rebuild; their provenance is the design record, not source samples.
- **Behavior specs** — designed from the pattern inventory and marked designed-from-pattern; nothing is recorded from a target.
- **Assets** — original creations; the asset manifest records origin in place of a source URL.

**Per-gate dispositions (D16).** RUN = the gate runs exactly as written. ADAPTED = the gate runs against the substitute evidence named. NOT APPLICABLE = the gate cannot run in this mode, for the reason named; recording it as passed is a false gate record.

| Gate | Disposition | Substitute evidence / reason |
|---|---|---|
| G-CL-001 | ADAPTED | The authorization record names the pattern class and zero target domains; its pre-commit timestamp is compared against the first inventory artifact instead of a crawl start. |
| G-CL-002 | ADAPTED | No domain exists to fetch robots from and no fetch occurs; evidence is the crawl log recording zero fetches plus the record's no-target scope. |
| G-CL-003 | ADAPTED | The pattern inventory replaces the crawl, sitemap, and CDX lists: every inventoried route traces to a pattern-inventory entry or carries a designed/excluded note. |
| G-CL-004 | NOT APPLICABLE | No JS bundle manifests exist and no target page may be loaded; route existence is established by the pattern inventory (G-CL-003, adapted). |
| G-CL-005 | ADAPTED | Provenance tags read "pattern reference" instead of a fetch source; the zero-authenticated-fetch assertion is evidenced by the zero-fetch crawl log. |
| G-CL-011 | ADAPTED | The reconciled set is the pattern inventory's route set, not crawl ∪ sitemap ∪ analytics ∪ CDX; zero unexplained differences still required. |
| G-CL-012 | RUN | Classification completeness operates on the inventory itself; unchanged. |
| G-CL-013 | RUN | Canonical uniqueness operates on the inventory's route identifiers; unchanged (no recorded redirects exist to follow). |
| G-CL-014 | ADAPTED | No fetch evidence can exist; the audit asserts every row's provenance is pattern-reference and the crawl log shows zero fetches. |
| G-CL-015 | NOT APPLICABLE | No live page or archived capture may be consulted in this mode; row accuracy is covered by G-CL-011 (adapted) and G-CL-012. |
| G-CL-021 | NOT APPLICABLE | Tokens are authored, not extracted — no source samples exist to trace to; token discipline is gated by G-CL-022 and G-CL-025 (adapted). |
| G-CL-022 | RUN | The orphan-value scan runs on the rebuild's own CSS; unchanged. |
| G-CL-023 | ADAPTED | The component list checked is the pattern inventory's; an "unsampled — reason" record reads as a designed-state record from the design record; full state coverage or an explicit reason is still required. |
| G-CL-024 | ADAPTED | The review runs over the pattern inventory and the build's asset folders; the replace-list is the inventory's protected-items list, and G-LG-094's brand-residue scan covers the build. |
| G-CL-025 | ADAPTED | The token-only render runs unchanged; the comparison basis is the pattern inventory's recorded design characteristics, not a source capture. |
| G-CL-031 | ADAPTED | Manifest rows record origin "original creation" in place of source URL and capture date; checksum, verdict, and zero-orphan requirements unchanged. |
| G-CL-032 | NOT APPLICABLE | No WARC records exist because nothing was harvested; on-disk checksum integrity is already asserted by G-CL-031 (adapted). |
| G-CL-033 | NOT APPLICABLE | There is no source domain to scan for; hotlinking is excluded structurally because every shipped asset is a local file in the G-CL-031 manifest. |
| G-CL-034 | ADAPTED | "Harvested form" is evidenced by the manifest's origin field (every row an original creation) plus the zero-fetch crawl log; the `licensed`-row license-citation check runs unchanged. |
| G-CL-035 | ADAPTED | The robots/gated grep runs against the zero-fetch harvest log; the authorization-predates-work half runs unchanged against the first inventory or harvest artifact. |
| G-CL-041 | ADAPTED | No recording starts and no test accounts exist; the check asserts the authorization record exists, predates the first behavior spec, and covers pattern-reference behavior specification. |
| G-CL-042 | ADAPTED | The diff runs against the pattern inventory's interaction list; specs are marked designed-from-pattern, and exclusions carry reasons as before. |
| G-CL-043 | ADAPTED | The frozen set is the pattern-derived spec suite, frozen at spec sign-off instead of at recording; hash-matching and fix-the-rebuild-never-the-tests run unchanged. |
| G-CL-044 | ADAPTED | The personal-data scan runs unchanged over specs and source; the verbatim-copy and fingerprint scans compare against the pattern inventory's protected-items list, there being no target copy or code. |
| G-CL-045 | RUN | The click-through runs on the rebuild against its (pattern-derived) specs; unchanged. |
| G-CL-051 | RUN | Statuses remain mandatory; in this mode `captured` is unavailable by definition and rows read `inferred` or `designed`. |
| G-CL-052 | RUN | Parity claims are exactly what this mode must never make for designed rows; unchanged. |
| G-CL-053 | ADAPTED | Template coverage runs unchanged; the target-string grep compares against the pattern inventory's protected-items list instead of one target's domain, logo filenames, and copy strings. |
| G-CL-054 | ADAPTED | The evidence chain per row is: pattern-inventory citation for `inferred` rows, the zero-fetch crawl log as the recorded absence of capture tiers, and the design record for `designed` rows. |
| G-CL-055 | RUN | The authorization record exists, predates reconstruction, and names pattern-reference reconstruction in scope; there are no gated rows. |
| G-CL-061 | NOT APPLICABLE | No source captures exist to baseline against and this mode makes no visual-parity claim; visual quality is gated by G-CL-025 (adapted) and the D13 accessibility gates. |
| G-CL-062 | NOT APPLICABLE | No baselines exist (follows G-CL-061); changes to any project-kept regression baselines of the rebuild itself are reviewed under G-CL-064 (adapted). |
| G-CL-063 | RUN | The checklist diff runs on the rebuild's executed interaction tests; unchanged. |
| G-CL-064 | ADAPTED | With no diff report, the review runs over the deviation log against this disposition table: every ADAPTED or NOT APPLICABLE gate and every excluded inventory row must carry its entry and reason. |
| G-CL-065 | RUN | No comparison run exists in this mode, so any parity or similarity claim fails for lack of a backing run ID; unchanged. |

The D14 authorization gates (G-LG-091–095) run as written — the crawl log they read records zero fetches — and the D13, D7, D8, D12, and D6 gates are unaffected.

## Step-by-step sequence

0. **Always-on core.** Load `bundles/core.md`; set up project files (project-templates), start `progress.md`, apply the secrets baseline.
1. **D14 pre-flight — authorization before anything touches the target.** Run clone-ethics: write the authorization record, then pass **G-LG-091** (pre-flight authorization check) and **G-LG-092** (authorization-vs-crawl timestamp comparison — the record must be older than the first crawl log entry). *Decision point: if there is no authorization basis — not the user's site, no client engagement, no legitimate study purpose — stop and ask (§6.3). No authorization, no crawl, no exceptions.* (Unattended run: BOOTSTRAP's approval-points rule applies at this point — a decision recorded in the commissioning brief or `requirements.md` counts as the answer; if none is recorded and no user is reachable, follow the §6.3 stuck protocol (log-and-continue, then the safe defaults) and record the substitution in `progress.md`.)
2. **D16 discovery.** site-discovery maps routes, sitemaps, robots, and the JS-bundle route manifest (G-CL-001 authorization pre-flight, G-CL-002 robots and terms compliance, G-CL-003 three-source reconciliation). Respect robots.txt and the target's terms; rate-limit the crawl.
3. **D16 inventory.** page-inventory classifies every route: public / auth-gated / not found / historical-only (Wayback). Pass G-CL-011 (reconciliation diff) and G-CL-013 (canonical uniqueness). *Decision point: for each auth-gated or unrecoverable route, choose — design fresh from patterns + extracted tokens (marked designed-not-cloned) or drop the route with the reason recorded. Never guess-and-present-as-copy.*
4. **D16 extraction.** design-extraction pulls design tokens, component patterns, and layout rules (G-CL-021 token traceability diff, G-CL-024 replace-list completeness). asset-harvesting collects only assets cleared for use; every asset gets a verdict in the manifest (G-CL-031 manifest completeness, G-CL-034 verdict enforcement audit). *Protected assets — logos, brand marks, proprietary images, copy text — are never reused; they are replaced with original equivalents.*
5. **D16 behavior capture.** behavior-cloning records observable interactions on public pages (G-CL-041 authorization and account pre-flight, G-CL-043 frozen-suite acceptance run). No credential-stuffing, no bypassing logins to "see" gated behavior.
6. **Build — D3+D13+D4+D5.** page-reconstruction rebuilds pages from tokens + inventory (G-CL-051 inventory status audit, G-CL-052 parity-claim check). Frontend built with frontend-core/component-library; D13 runs in the same step — accessibility-audit on every template (G-AC-001, G-AC-005). Backend and schema are designed fresh (api-building, schema-design): the source's backend is not observable and is never claimed to be matched.
7. **D14 full pass.** privacy-laws register for the rebuilt site's own data handling; legal-documents for its own terms/privacy text; G-LG-094 (brand-residue scan) proves no source branding survives in the rebuild.
8. **D12 performance.** performance-budgets set and asserted for the rebuilt templates (G-AN-101 CI budget assertion).
9. **D7+D8 verification.** Security pass (G-SE-001 ZAP baseline, 0 critical findings). Fidelity-verification runs the parity suite: G-CL-061 (visual comparison suite), G-CL-064 (deviation log review), G-CL-065 (report claim check — every parity claim in the report traces to evidence; designed-not-cloned pages are reported as designed). qa-gates: G-QA-111, and placeholder-scan G-QA-141 (scan rendered output, not source — no placeholder text or lorem survives in what ships).
10. **D6 deploy.** ci-cd (G-DO-001) then hosting (G-DO-071 external production check). Deployment happens only after steps 7–9 pass.
11. **D9 finish.** technical-seo on the rebuilt site's own behalf (G-CO-001 promotion indexability diff) — canonical tags point at the new site, never the source.

## Gates that must pass

- **Ethics (blocking, before crawl):** G-LG-091, G-LG-092; **(before ship):** G-LG-093, G-LG-094 — no protected asset copied, no brand residue.
- **Discovery/inventory:** G-CL-001, G-CL-002, G-CL-003, G-CL-011, G-CL-013.
- **Extraction/harvest:** G-CL-021, G-CL-024, G-CL-031, G-CL-034.
- **Reconstruction/fidelity:** G-CL-051, G-CL-052, G-CL-061, G-CL-064, G-CL-065 — parity thresholds met, every claim evidence-backed.
- **Accessibility:** G-AC-001, G-AC-005 — WCAG 2.2 AA pass.
- **Security/QA:** G-SE-001 (0 criticals), G-QA-111, G-QA-141 — all green.
- **Performance/deploy:** G-AN-101, G-DO-001, G-DO-071.

## Failure handling

- **G-LG-091/092 fails (no or late authorization):** stop the playbook. Delete any crawl data gathered before the record existed; do not "backdate" anything. Resume only with a real authorization record, and re-run discovery from scratch.
- **Fidelity gate fails on a page (G-CL-061):** the page returns to step 6 with the deviation log entry as the work order. If parity is unreachable because the source behavior was never observable, reclassify the page designed-not-cloned and rebuild it as a design task — never tune the comparison threshold to force a pass.
- **Brand residue found (G-LG-094):** replace the asset/copy with an original equivalent and re-run the scan; a second hit in the same asset class triggers a full-manifest audit (G-CL-034) before proceeding.
- **Any other gate fails mid-playbook:** fix in the owning department, re-run that gate, record both results in `progress.md`. No gate is waived silently; a waiver needs a DECISIONS.md entry.

## Definition of done

Authorization record predates all crawl data; inventory complete with every page classified (reconstructed vs designed-not-cloned); all gates above green; fidelity report published with evidence per claim and designed pages labeled; no protected asset, brand mark, or source copy text in the shipped build; deployed and reachable (G-DO-071); `progress.md` shows the full gate trail. **Pre-provisioning complete:** where no production environment exists yet, the project may be recorded as *pre-provisioning complete* when every gate except the provisioning-waived ones is green, each waived gate is recorded as a provisioning waiver per §6.3, and the unblocking conditions are listed in `progress.md` — the deployment requirements above remain open until the environment exists.

## Worked mini-example — rebuild of a small SaaS marketing site (public pages only)

1. Core loaded; fact-sheet records the source's owner and purpose from its public About page.
2. Authorization record committed: client engagement letter dated today, scope = marketing pages only. G-LG-091/092 pass.
3. site-discovery finds 14 routes via sitemap + JS manifest; robots allows all 14. G-CL-003 reconciles.
4. Inventory: 11 public, 2 auth-gated (app login, dashboard), 1 dead. The 2 gated routes marked designed-not-cloned.
5. design-extraction yields 46 tokens; replace-list flags the logo and 6 hero images as protected → originals commissioned.
6. behavior-cloning captures the pricing toggle and FAQ accordion from public pages.
7. Build: 11 pages reconstructed, 2 designed fresh in the extracted system; G-AC-001 passes on all templates.
8. Fidelity suite: 10/11 reconstructed pages within threshold; the blog index deviates → deviation log, one fix round, passes.
9. G-LG-094 clean, G-SE-001 0 criticals, G-QA-141 clean. Deploy via ci-cd; G-DO-071 confirms the live site.
10. Report ships: parity claims cite the comparison suite; the 2 designed pages are labeled designed-not-cloned.
