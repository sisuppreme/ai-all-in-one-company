# asset-harvesting

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://github.com/iipc/warc-specifications/blob/master/specifications/warc-format/warc-1.1/index.md ; https://webrecorder.net/blog/2021-02-22-introducing-browsertrix-crawler/
- **Depends on:** clone-ethics (D14 gate), site-discovery, page-inventory, licensing (D14)
- **Feeds into:** page-reconstruction, fidelity-verification, design-extraction

## When to use / Do NOT use

- **Use when:** An authorized rebuild needs the target's asset inventory — images, media, fonts, documents, icons — captured with provenance so each asset can be reused, recreated, or replaced on a recorded rights basis.
- **Do NOT use when:** No D14 authorization record exists (stop; clone-ethics gates first), when the need is design values rather than files (design-extraction), or to stock a general asset library from a site (out of scope; harvest only what in-scope pages reference).

## Rules

1. **CL-061 — Authorization precedes harvesting.** No asset is fetched before the D14 clone-ethics authorization record exists and predates the first harvest log entry.
2. **CL-062 — Harvest the full in-scope surface.** Extract asset URLs from HTML, CSS, JS, and network logs for every page in page-inventory; a file the live site no longer serves is recovered from an archived capture or recorded as unrecoverable, never silently skipped.
3. **CL-063 — Manifest before workspace.** Every harvested asset gets a manifest row — source URL, capture date, checksum, rights decision — before the file enters the rebuild workspace; a file with no row does not exist for the build.
4. **CL-064 — Four verdicts only.** Each manifest row carries exactly one rights decision: `owned`, `licensed`, `recreate`, or `replace`. An undecided asset is treated as `replace` until a decision is recorded.
5. **CL-065 — Archive-grade capture.** Captures are stored as WARC records (ISO 28500) with full request/response provenance, via a browser-driven archiver (e.g. Browsertrix Crawler) for JS-heavy pages; where WARC tooling is impractical, the fallback is a HAR plus checksum manifest, and the choice is recorded.
6. **CL-066 — Only owned/licensed ship as-is.** Assets decided `recreate` or `replace` are rebuilt or substituted before build; the harvested original never enters the ship folders in harvested form.
7. **CL-067 — Licensed needs a license record.** A `licensed` verdict cites the license — holder, scope, and transferability to this rebuild checked. Even on the client's own site, third-party stock and font licenses govern; "the client uses it" is not a license record.
8. **CL-068 — Trademarks are logged, never reused.** Logos, wordmarks, and brand artwork are recorded in the manifest with verdict `replace` and their placement noted, so reconstruction knows what the operator's own mark must substitute; they are never harvested into the rebuild's assets.
9. **CL-069 — Fonts are assets.** A harvested font file ships only after its license permits the rebuild's use (embedding/redistribution terms checked); an unlicensed font goes to design-extraction as a substitution record, not into the build.
10. **CL-070 — Never hotlink.** The deliverable references only local, manifest-covered asset files; no built page, stylesheet, or script URL points at the source domain.
11. **CL-071 — Respectful, lawful capture.** The harvester sends an identifying user-agent, obeys robots.txt Disallow rules, and respects rate limits; assets are never pulled from behind a login or paywall by bypass — gated assets are recorded as gated.
12. **CL-072 — Provenance survives the source.** The WARC record and checksum remain the evidence after the live site changes or vanishes; a harvested file whose checksum no longer matches its capture record is re-captured or dropped, never quietly kept.

## BAN list

- **BAN-CL-031 — Manifest-less shipment.** Banned: an asset file entering the rebuild with no manifest row or no rights decision. Defeats: DET-CRWL-007. Bad: `hero.jpg` is copied from the crawl folder into `src/assets/` because the build needs it today. Instead: create the manifest row (source URL, capture date, checksum, verdict) first; the file moves only after the row exists. Severity: BLOCK.
- **BAN-CL-032 — Silent reuse of protected media.** Banned: shipping a harvested photograph, illustration, font, or copy file unchanged without an `owned`/`licensed` verdict. Defeats: DET-CRWL-009. Bad: the target's product photo library is bulk-downloaded and ships as the rebuild's gallery. Instead: record verdict `recreate` or `replace` and shoot, license, or substitute the operator's own media before build. Severity: BLOCK.
- **BAN-CL-033 — Hotlinking the source CDN.** Banned: the deliverable loading any asset from the source site's domain at runtime. Defeats: DET-CRWL-015. Bad: the rebuild's `<img src="https://target.example/media/banner.jpg">` works until the original site redesigns, then breaks. Instead: ship a local file with a manifest row and a reuse verdict, or a recorded replacement. Severity: BLOCK.
- **BAN-CL-034 — Bypass harvesting.** Banned: pulling asset files from behind a login or paywall using borrowed credentials or an access workaround. Defeats: DET-CRWL-008. Bad: a customer's login is used to download the members-only media kit "for completeness." Instead: record those assets as gated; obtain them only through access the client legitimately provisions. Severity: BLOCK.
- **BAN-CL-035 — Robots-blind bulk harvest.** Banned: crawling asset paths robots.txt disallows, or fetching at rates that burden the target, to complete the inventory. Defeats: DET-CRWL-014. Bad: the harvester ignores the `/media/` Disallow and pulls 4,000 files overnight. Instead: obey the Disallow set, log disallowed paths as excluded, and throttle to the recorded crawl rate. Severity: BLOCK.

## Gates

- **G-CL-031 — Manifest completeness (automated).** Verifies: CL-063, CL-064. Check: script walks the rebuild's asset folders and asserts every file has a manifest row with source URL, capture date, checksum, and one of the four verdicts. Pass: zero orphan files, zero verdict-less rows. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — manifest rows record origin “original creation” in place of source URL and capture date; checksum, verdict, and zero-orphan bars unchanged; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-032 — Checksum spot-check (automated).** Verifies: CL-065, CL-072. Check: recompute checksums for a random 10% sample (minimum 10 files) of harvested assets and compare against their WARC records and manifest rows. Pass: 100% match. Fail: block shipment; mismatched files are re-captured or dropped. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — no WARC records exist because nothing was harvested; on-disk checksum integrity is asserted by G-CL-031 (adapted); see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-033 — Hotlink scan (automated).** Verifies: CL-070. Check: `grep -rE "https?://(www\.)?<source-domain>" dist/` over built HTML, CSS, and JS, filtered to asset references (img, srcset, url(), font, media). Pass: zero hits. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: NOT APPLICABLE — no source domain exists; every shipped asset is a local file in the G-CL-031 manifest, so hotlinking is structurally excluded; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-034 — Verdict enforcement audit (automated).** Verifies: CL-066, CL-067, CL-068. Check: script asserts no file whose manifest verdict is `recreate`, `replace`, or undecided exists in the ship asset folders in harvested form, and every `licensed` row cites a license record (holder, scope, transferability). Pass: zero violations. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — harvested form is evidenced by the manifest's origin field plus the zero-fetch crawl log; the licensed-row citation check runs unchanged; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-035 — Access compliance check (automated).** Verifies: CL-061, CL-071. Check: grep the harvest log against the target's robots.txt Disallow set and against the gated-URL list from site-discovery; confirm the authorization record's timestamp predates the first log entry. Pass: zero disallowed or gated fetches; authorization predates harvest. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the robots/gated grep runs against the zero-fetch harvest log; the authorization-predates-work half runs unchanged; see the pattern-reference disposition table in the clone-rebuild playbook.

## Anti-patterns

- **Folder-dump harvest.** Everything lands in one folder with names like `img_final2.png`, and provenance is reconstructed later from memory. Catch it: any file not created through the manifest-first flow (CL-063) is suspect until its row exists.
- **Screenshot-substitute assets.** A screenshot crop stands in for a missing image file because it "looks the same." Catch it: shipped media must be real files with checksums in the manifest, never crops of a capture.
- **Verdict drift.** An asset marked `replace` early quietly becomes the shipped hero image under deadline pressure. Catch it: run the verdict audit (G-CL-034) at ship time, not at harvest time.
- **Whole-library sweep.** The entire media library is harvested "just in case," far beyond what in-scope pages reference, inflating rights exposure. Catch it: every manifest row names the in-scope page that references the asset; rows that name none are out of scope.

## Examples

- [Example 1 — Photo library shipped vs. recreate verdict](examples/example-1.md) — violates/corrects CL-066, BAN-CL-032.
- [Example 2 — Hotlinked banner vs. local licensed file](examples/example-2.md) — violates/corrects CL-070, BAN-CL-033.
- [Example 3 — Logo in the asset folder vs. logged replacement](examples/example-3.md) — violates/corrects CL-068, BAN-CL-032.

## Recall anchors

- No manifest row, no file — provenance is recorded at capture, not reconstructed.
- Four verdicts only; undecided means replace.
- Only owned/licensed ship as-is; everything else is recreated or replaced.
- Trademarks and logos are logged for replacement, never harvested for reuse.
- Never hotlink, never bypass, never outrun robots.txt.

## Checklist

- [ ] D14 authorization record exists and predates the first harvest log entry (CL-061).
- [ ] Asset URLs extracted from HTML, CSS, JS, and network logs for every in-scope page (CL-062).
- [ ] Every file in the rebuild's asset folders has a manifest row with source URL, capture date, checksum, and verdict (G-CL-031).
- [ ] Captures stored as WARC records, or the HAR fallback choice recorded (CL-065).
- [ ] Every `licensed` verdict cites a license record with transferability checked (CL-067).
- [ ] No `recreate`/`replace`/undecided asset ships in harvested form (G-CL-034).
- [ ] Built output contains zero references to the source domain (G-CL-033).
- [ ] Harvest log shows zero robots-disallowed or gated fetches (G-CL-035).
