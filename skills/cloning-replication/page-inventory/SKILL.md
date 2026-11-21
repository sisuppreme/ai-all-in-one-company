# page-inventory

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Wayback CDX Server API — https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md ; migration inventory practice (crawl + sitemap + analytics + Search Console merge) — https://guestpost.uk/screaming-frog/
- **Depends on:** site-discovery, clone-ethics
- **Feeds into:** design-extraction, asset-harvesting, behavior-cloning, page-reconstruction, fidelity-verification

## When to use / Do NOT use

- **Use when:** an authorized discovery crawl exists and the replication scope must be fixed as one reconciled table — the contract every later D16 skill builds, samples, and verifies against.
- **Do NOT use when:** discovery has not run (use site-discovery first), the D14 authorization record does not exist (stop; clone-ethics gates all D16 work), or the deliverable is a content copy — the inventory is a map of pages, never a harvest of the target's text or imagery.

## Rules

1. **CL-021 — Four-source merge.** The inventory is built by merging the rendered crawl, the XML sitemap(s), analytics/Search Console top pages, and the Wayback CDX index. If client analytics access is unavailable, the three remaining sources are the minimum and the missing source is recorded on the inventory header — never silently skipped.
2. **CL-022 — One row per canonical page.** Each row is one canonical URL after normalization (trailing slash, query parameters, casing resolved; redirect sources resolved to their target). A redirect source is an attribute of its target row, never a row itself.
3. **CL-023 — Mandatory row fields.** Every row carries: canonical URL, page type, template ID, component set, HTTP status, last capture date, provenance flag (`public`, `archived-only`, or `inferred`), scope status (`built`, `planned`, or `excluded`), and priority. A row missing any field is unfinished, not filed.
4. **CL-024 — Templates by DOM structure.** Rows are clustered into template families by DOM structure, so shared layouts are built once. Pages differing only in data (product, post, profile) share one parameterized template row set; a template ID is assigned before any reconstruction starts.
5. **CL-025 — States and viewports are rows too.** Materially distinct states (logged-out vs. logged-in shell, empty vs. populated list, error state) and viewport variants that change layout are inventoried as variant rows linked to their parent page, with their own priority.
6. **CL-026 — No silent deletion.** A discovered page that is out of scope stays in the table with scope status `excluded` and a one-line reason. "Missing" and "excluded" must always be distinguishable; a row is removed only by merging it as a duplicate, with the merge recorded.
7. **CL-027 — Count reconciliation.** The inventory row count equals the reconciled discovery count from site-discovery. Every URL present in one source and absent from another carries a reconciliation note (orphan, sitemap-only, archived-only, JS-route) before sign-off.
8. **CL-028 — Signed scope contract.** The client signs off the in-scope count (`built` + `planned` rows) before reconstruction starts. That count is the engagement's scope contract; pages discovered later enter through a recorded scope change, not by quiet addition.
9. **CL-029 — Authorized input only.** The inventory is built only from authorized discovery output and inherits its robots.txt compliance. It is never extended by fetching disallowed paths; gated pages are listed as gated with provenance noted, never accessed by bypass.
10. **CL-030 — Map, not copy.** Rows record provenance and rights-relevant facts (for example, pages whose assets are third-party) but never embed the target's copyrighted text, imagery, or branded assets as reusable content.
11. **CL-031 — Evidence frozen at sign-off.** At scope sign-off the underlying evidence set (captures, crawl output, CDX responses) is frozen and referenced by the inventory version, so later skills verify against the same baseline even if the live site changes.
12. **CL-032 — Versioned table.** The inventory is a committed, versioned file. Every change after sign-off (new row, status change, template re-cluster) is a dated revision entry, so any later fidelity result can be traced to the inventory version it was checked against.

## BAN list

- **BAN-CL-011 — Navigation-only inventory.** Banned: building the inventory from the site's navigation menu or homepage links alone and presenting it as all pages. Defeats: DET-CRWL-007. Bad: the inventory lists the 14 menu pages of a store while 300 product and blog pages from the sitemap and CDX index never appear. Instead: merge crawl, sitemap, analytics, and CDX sources and reconcile the differences (CL-021, CL-027). Severity: BLOCK.
- **BAN-CL-012 — Silent row deletion.** Banned: deleting out-of-scope or inconvenient rows so the table looks complete. Defeats: DET-CRWL-005. Bad: 40 archived-only landing pages are dropped from the draft, and the final report claims the inventory covers "the whole site." Instead: keep every discovered row with scope status `excluded` and a stated reason (CL-026). Severity: BLOCK.
- **BAN-CL-013 — Duplicate canonical rows.** Banned: listing the same page more than once under URL variants (trailing slash, tracking parameters, casing, redirect source). Defeats: DET-CRWL-005. Bad: `/pricing`, `/pricing/`, and `/pricing?utm_source=ad` appear as three rows and are rebuilt as three pages. Instead: canonicalize and merge into one row, with variants recorded as attributes (CL-022). Severity: BLOCK.
- **BAN-CL-014 — Extending the inventory by disallowed fetching.** Banned: fetching robots-disallowed, login-gated, or paywalled URLs to "complete" the inventory. Defeats: DET-CRWL-014. Bad: the crawler logs in with a borrowed account to enumerate the dashboard pages the public crawl cannot see. Instead: list gated pages as gated from authorized evidence only, and record disallowed paths as excluded by robots (CL-029). Severity: BLOCK.
- **BAN-CL-015 — Inventory as content copy.** Banned: pasting the target's page copy, headlines, or image files into inventory rows as reusable content. Defeats: DET-CRWL-009. Bad: each row carries the target's full marketing text "so reconstruction can paste it back." Instead: rows carry URLs, structure, and rights facts only; content is recreated or replaced downstream (CL-030). Severity: BLOCK.

## Gates

- **G-CL-011 — Reconciliation diff.** Verifies: CL-021, CL-027. Check: automated — script compares the inventory's canonical URL set against the reconciled site-discovery URL set (crawl ∪ sitemap ∪ analytics ∪ CDX); any URL in one set and not the other, without a reconciliation note, fails. Pass: zero unexplained differences. Fail: block scope sign-off. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the reconciled set is the pattern inventory's route set, not the crawl/sitemap/analytics/CDX union; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-012 — Classification completeness.** Verifies: CL-023, CL-026. Check: automated — script asserts every row has all mandatory fields populated and a scope status of `built`, `planned`, or `excluded`, and that every `excluded` row carries a non-empty reason. Pass: 100% of rows fully classified. Fail: block scope sign-off. Recorded in: progress.md.
- **G-CL-013 — Canonical uniqueness.** Verifies: CL-022. Check: automated — canonicalize every row URL (lowercase host, resolve trailing slash and tracking parameters, follow recorded redirects to target) and assert the resulting set has no duplicates. Pass: zero duplicate canonical URLs. Fail: block scope sign-off. Recorded in: progress.md.
- **G-CL-014 — Robots and gating audit.** Verifies: CL-029. Check: automated — compare the inventory's source URLs against the discovery crawl's robots.txt Disallow set and gated-path list; any row whose evidence came from a disallowed fetch or a bypassed gate fails. Pass: zero violations. Fail: block the engagement pending D14 review. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the audit asserts pattern-reference provenance on every row and zero fetches in the crawl log; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-015 — Sample verification.** Verifies: CL-023, CL-024. Check: manual — fetch a random 10% sample of rows and confirm URL, HTTP status, and template label against the live page or its archived capture. Pass: every sampled row matches; any mismatch triggers a full re-check of its template family. Fail: block scope sign-off. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — no live page or archived capture may be consulted; row accuracy is covered by G-CL-011 (adapted) and G-CL-012; see the pattern-reference disposition table in the clone-rebuild playbook.

## Anti-patterns

- **Round-number scope.** The inventory lands on a suspiciously round count ("exactly 100 pages") because discovery stopped at a crawl limit. Catch it: compare the count against each source's raw total; a cap hit during any source pull invalidates the merge until re-run uncapped.
- **Template inflation.** Near-identical pages are each given their own template ID, so reconstruction rebuilds one layout twenty times. Catch it: sort rows by DOM-structure hash; families differing only in text or data merge into one parameterized template (CL-024).
- **Priority by menu order.** Priorities simply mirror the navigation order instead of traffic and business value. Catch it: cross-check priority against the analytics top-pages source; a high-traffic page ranked below a footer link means priority was guessed.
- **Stale-status drift.** Rows keep the HTTP status and capture date from the first crawl while the site changes underneath. Catch it: any row whose last capture date predates the evidence freeze (CL-031) without a re-check note is flagged before sign-off.

## Examples

- [Example 1 — Four sources merged, one reconciled table](examples/example-1.md) — corrects CL-021.
- [Example 2 — URL variants merged into one canonical row](examples/example-2.md) — corrects CL-022.
- [Example 3 — Out-of-scope pages kept as excluded rows](examples/example-3.md) — corrects CL-026.

## Recall anchors

- The inventory is the contract: if it is not a row, it is out of scope — in writing.
- Four sources in, one canonical row per page.
- Excluded is a status with a reason, never a deletion.
- Gated pages are listed as gated, never fetched around.
- Sign-off freezes the count and the evidence.

## Checklist

- [ ] All four sources merged, or the missing source recorded on the header (CL-021).
- [ ] Canonical URLs unique across rows; redirect sources are attributes, not rows (G-CL-013).
- [ ] Every row fully classified: built, planned, or excluded with a reason (G-CL-012).
- [ ] Row count reconciles with site-discovery, differences noted (G-CL-011).
- [ ] No row's evidence came from a disallowed or bypassed fetch (G-CL-014).
- [ ] States and viewport variants inventoried as linked variant rows (CL-025).
- [ ] Client signed off the in-scope count; evidence set frozen and versioned (CL-028, CL-031).
