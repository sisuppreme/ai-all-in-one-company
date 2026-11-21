# licensing

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://spdx.org/licenses/ ; https://choosealicense.com/
- **Depends on:** none — standalone: license checks read the actual license texts of the dependencies, fonts, images, and datasets being added — primary legal sources, not another skill's output. Its verdicts feed compliance-audit and legal-documents.
- **Feeds into:** compliance-audit, legal-documents

## When to use / Do NOT use

- **Use when:** adding any dependency, font, image, dataset, or copied snippet; vendoring third-party code; preparing a release (SBOM and notices); choosing or changing the project's own LICENSE; reviewing whether an asset's terms permit the intended use, including transfer to a client or a rebuild.
- **Do NOT use when:** the question is a contested rights call — disputed ownership, a license whose terms are ambiguous for the intended use, a takedown or infringement claim. This skill records provenance and applies the written tier policy; it never interprets a license for a contested case or gives legal advice (LG-112).

## Rules

1. **LG-101 — Every component is inventoried.** Every shipped component — library, font, image, dataset, copied snippet — has an inventory row recording its name, version, origin, and license as an SPDX License List identifier (e.g. `MIT`, `Apache-2.0`, `GPL-3.0-only`), so policy is machine-checkable instead of name-matching prose. A component with no row does not ship.
2. **LG-102 — Provenance is recorded at adoption time.** The inventory row is written when the component is adopted: where it came from, where its license text lives, and the adoption date. An asset whose provenance cannot be established is treated as unlicensed until proven otherwise.
3. **LG-103 — "No license found" is forbidden-tier.** Absence of a license is not permission: default copyright means all rights reserved. A component with no license found is replaced, or the rights holder's written permission is obtained and filed with the inventory row.
4. **LG-104 — Tiers are set per distribution model.** The project's written license policy defines three tiers — allowed (permissive), review (weak or file-level copyleft), forbidden without a written exception (strong/network copyleft in a distribution model it infects, non-commercial terms, no license found) — separately for each way the product ships (hosted service vs. distributed artifact). The same library can be allowed in one model and forbidden in the other; the tier is decided against the actual model, never in the abstract.
5. **LG-105 — Review-tier items get a named decision.** Every review-tier component carries a recorded decision: the decider's name, the date, the distribution model considered, and the reasoning. An undecided review-tier component does not ship.
6. **LG-106 — Exceptions are written and expire.** A forbidden-tier exception names the component, the reason, the approver, and a review date. An exception past its review date is void until re-approved; a verbal exception does not exist.
7. **LG-107 — Vendored code keeps its license files.** Vendored code, fonts, and assets keep their license and copyright files intact in the tree. Stripping them is a defect found by scan (G-LG-054), not a cleanup step.
8. **LG-108 — Notices are generated, never hand-written.** Attribution is discharged by a notices file generated from the inventory and shipped with the product; where a license triggers a copyleft source-offer duty, the offer is implemented as a real download or disclosure of the corresponding source, not a link to upstream. A notices entry with no inventory row, or a shipped component with no notices entry, is a defect.
9. **LG-109 — An SBOM is emitted per release.** Each release emits an SBOM (SPDX or CycloneDX format) from the build, and the SBOM, the inventory, and the notices file are diffed against each other (G-LG-052). The OpenChain ISO/IEC 5230 program elements are the reference for what the compliance program contains.
10. **LG-110 — Licensing is a CI property.** Adding or upgrading a component re-runs the scan and inventory update in the same change. Licensing is never a launch-week audit reconstructed from memory.
11. **LG-111 — The project's own LICENSE is chosen deliberately.** At project creation a LICENSE is selected deliberately (Choose a License is the selection aid), names this project and its rights holder, and matches the intended distribution. No LICENSE file means nobody — including future collaborators — has permission to use the code.
12. **LG-112 — Transferability is checked; contested calls escalate.** Before an asset ships in client work or a rebuild, its terms are checked for transferability (e.g. stock and font licenses that do not transfer). Where the rights position is ambiguous or contested, work on that asset stops and the call goes to qualified counsel with the inventory record attached.

## BAN list

- **BAN-LG-051 — Vendored material shipped with its license files stripped.** Banned: dropping vendored code, a font, or an asset into the tree with its LICENSE, COPYING, or copyright notices deleted. Defeats: DET-CON-020. Bad: a charting library is vendored under `vendor/`; its LICENSE and copyright header are removed "to keep the folder clean," leaving code in the product with no attribution or terms. Instead: keep the license and copyright files with the vendored copy and add the inventory row (LG-101, LG-107). Severity: BLOCK.
- **BAN-LG-052 — "Fully licensed" claimed with no inventory behind it.** Banned: stating in product copy, a client deliverable, or a store listing that all assets or components are licensed or rights-cleared when no inventory and tier record exists to prove it. Defeats: DET-CON-028. Bad: the delivery report says "all imagery fully licensed"; half the photos came from a bulk download with no rights record. Instead: make the claim only for what the inventory covers, component by component, or do not make it (LG-101, LG-102). Severity: BLOCK.
- **BAN-LG-053 — A LICENSE file that names another project.** Banned: copying a LICENSE from a tutorial, template, or another repository so the shipped file names the wrong project or rights holder. Defeats: DET-CON-017. Bad: the repo's LICENSE reads "Copyright (c) 2023 Example Tutorial App" while the product is a client storefront under a different name and owner. Instead: choose the license deliberately for this project and put this project's name and rights holder in it (LG-111). Severity: BLOCK.
- **BAN-LG-054 — A component shipped because "no license" was read as "free to use."** Banned: shipping a library, snippet, font, or dataset for which no license was found, on the reasoning that public availability implies permission. Defeats: DET-CON-020. Bad: a utility snippet copied from a personal blog with no license statement is pasted into the codebase and shipped in two releases. Instead: treat no-license-found as forbidden-tier — replace the component or file the rights holder's written permission (LG-103). Severity: BLOCK.
- **BAN-LG-055 — Notices or license claims that contradict the inventory.** Banned: publishing a notices file, attribution page, or compliance claim (e.g. "OpenChain conformant") that the inventory and scan results do not support, or leaving a generated notices file stale after components change. Defeats: DET-CON-014. Bad: the shipped notices list twelve components; the release contains nineteen, including a copyleft library whose source-offer duty nobody implemented. Instead: regenerate notices from the inventory at release and implement triggered duties as real disclosures (LG-108, LG-109). Severity: WARN.

## Gates

- **G-LG-051 — CI license scan.** Verifies: LG-101, LG-103, LG-104. Check (automated): run a source-level scan (ScanCode Toolkit) plus the ecosystem metadata checker (`license-checker`, `pip-licenses`, or `cargo-deny`) over the full tree, including vendored directories; compare every detected SPDX identifier against the policy tiers for the target distribution model. Pass: no forbidden-tier identifier, no unlisted identifier, and no component detected that lacks an inventory row. Fail: block the build. Recorded in: progress.md.
- **G-LG-052 — SBOM–inventory–notices diff.** Verifies: LG-108, LG-109. Check (automated): emit the release SBOM (SPDX or CycloneDX) and diff its component set against the inventory and the generated notices file. Pass: the three sets are identical. Fail: block shipment until the missing row or notices entry exists. Recorded in: progress.md.
- **G-LG-053 — Provenance completeness lint.** Verifies: LG-101, LG-102. Check (automated): lint the inventory — every row must carry a non-empty SPDX identifier, origin, license-text location, and adoption date; a row marked "unknown" in any field fails. Pass: zero incomplete rows. Fail: block shipment; the component is provenanced, replaced, or removed. Recorded in: progress.md.
- **G-LG-054 — Vendored-file integrity scan.** Verifies: LG-107. Check (automated): for every vendored directory, assert a LICENSE/COPYING/NOTICE file (or the upstream license text recorded in the inventory) is present and non-empty. Pass: every vendored component retains its license material. Fail: block shipment and restore the files from upstream. Recorded in: progress.md.
- **G-LG-055 — Decision and exception register review.** Verifies: LG-105, LG-106, LG-112. Check (manual): read the decision register — every review-tier component in the inventory has a named decision with reasoning; every exception names component, reason, approver, and a review date that has not passed; every client/rebuild asset has a recorded transferability check or an escalation entry. Pass: all three hold in writing. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Launch-week license audit.** The inventory is assembled once, just before release, from memory and folder names. Catch it by comparing inventory adoption dates against commit history; rows all dated in the same week as the release were reconstructed, not recorded (LG-102).
- **Metadata-only trust.** The check reads package-manager license fields and calls the tree clean, while vendored files, fonts, and pasted snippets — exactly what metadata misses — go unscanned. Catch it by asking what the scan covered; a scan with no source-level pass over `vendor/` and asset folders is incomplete (G-LG-051).
- **Tier by vibe.** A component is waved through because its license "looks like MIT" from its name or README badge, without reading the actual license text or recording an SPDX identifier. Catch it in review: no SPDX ID and no license-text location in the row means the tier was guessed (LG-101).
- **Exception amnesia.** A forbidden-tier component was "agreed in a call" months ago; nothing is written and nobody remembers the terms. Catch it by asking for the exception record; if it cannot be produced, the exception does not exist (LG-106).

## Examples

- [Example 1 — The snippet with no license](examples/example-1.md) — violates/corrects LG-103.
- [Example 2 — The font folder with its license deleted](examples/example-2.md) — violates/corrects LG-107.
- [Example 3 — The copyleft library nobody tiered](examples/example-3.md) — violates/corrects LG-104.

## Recall anchors

- No license found means no permission — default copyright applies.
- Unknown provenance is unlicensed until proven otherwise.
- Every component: SPDX ID, origin, tier — recorded when adopted, not at launch.
- Notices are generated from the inventory, never hand-written.
- Tier follows the distribution model: the same library can be allowed hosted and forbidden shipped.

## Checklist

- [ ] Every shipped component has an inventory row with SPDX identifier, origin, and adoption date (LG-101, LG-102, G-LG-053).
- [ ] No component with no license found is shipped without filed written permission (LG-103, BAN-LG-054).
- [ ] Every review-tier component has a named, reasoned decision; every exception is written and in date (LG-105, LG-106, G-LG-055).
- [ ] Vendored code and assets retain their license and copyright files (LG-107, G-LG-054).
- [ ] The release SBOM, inventory, and shipped notices diff clean (LG-108, LG-109, G-LG-052).
- [ ] The CI license scan passes for the target distribution model (LG-104, G-LG-051).
- [ ] The project's own LICENSE names this project, and client/rebuild assets have a transferability check or escalation on record (LG-111, LG-112).
