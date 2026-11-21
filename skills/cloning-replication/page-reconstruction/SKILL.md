# page-reconstruction

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md ; https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
- **Depends on:** page-inventory, design-extraction, clone-ethics (D14)
- **Feeds into:** fidelity-verification

## When to use / Do NOT use

- **Use when:** an in-scope inventory page cannot be captured directly — it is auth-gated, deleted, or never archived — and must be rebuilt from surviving evidence.
- **Do NOT use when:** the page was captured intact; build from the capture instead. Do NOT use when no D14 authorization record covers reconstruction; stop and route to clone-ethics first.

## Rules

1. **CL-101 — Authorization precedes reconstruction.** No page is reconstructed before the D14 authorization record exists and names reconstruction in scope; the record's date is checked against the first build artifact's date.
2. **CL-102 — Evidence hierarchy is binding.** Rebuild from the highest available tier: (1) dated Wayback captures, (2) JS bundle route manifests, sitemap hints, and API responses, (3) the extracted design system and component patterns. A lower tier is used only after the tiers above it are checked and recorded as absent.
3. **CL-103 — Every row carries a status.** Each inventory row is labeled `captured`, `inferred`, or `designed` before its build starts; the label is stored in the inventory, not in the builder's head.
4. **CL-104 — Parity claims attach to `captured` only.** Only a `captured` page may be described as a clone or as matching the source. An `inferred` page is "reconstructed from partial evidence"; a `designed` page is "new design in the source's system."
5. **CL-105 — Build follows inventory order.** Pages are built in the priority order fixed in the page inventory; nothing outside the inventory is improvised, however plausible it seems.
6. **CL-106 — Operator content only.** Reconstructed pages render with the operator's own copy, data, and branding. Recovered target copy is a structural reference (length, placement, hierarchy) and is replaced unless the client owns the rights, per the D14 record.
7. **CL-107 — No target assets ship.** The target's images, logos, wordmarks, and trade dress never appear in a reconstructed page; placeholders or operator assets stand in, and each substitution is listed in the build notes.
8. **CL-108 — Structure from evidence, code original.** Layout and function are recreated from the evidence and the design-token file; markup and code are written fresh for the rebuild, never lifted from the target's served source.
9. **CL-109 — Gated pages need provided access.** An auth-gated page is reconstructed only from client-provided access or client-provided evidence (exports, screenshots, recordings). Absence from archives is never a reason to bypass the gate.
10. **CL-110 — Capture claims verified by digest.** A Wayback capture is cited as evidence only after its CDX `digest` and timestamp are recorded in the inventory row, so what the capture actually contained is checkable later.
11. **CL-111 — Inferred structure is spot-verified.** Every route or component inferred from a bundle manifest or API response is cross-checked against at least one second evidence item (sitemap entry, capture fragment, or client confirmation) before build.
12. **CL-112 — Deviations are logged, not hidden.** Where evidence runs out mid-page, the gap and the design decision that filled it are written into the inventory row's notes before the page is marked built.

## BAN list

- **BAN-CL-051 — Fabricated page labeled a verified clone.** Banned: inventing a plausible page from generic patterns and calling it a clone of a page nobody has seen. Defeats: DET-CRWL-013. Bad: a dashboard assembled from a UI kit is delivered as "verified clone of the admin console," a page that was never captured. Instead: label the row `designed`, build it in the source's design system, and present it to the client as new design. Severity: BLOCK.
- **BAN-CL-052 — Target copy and branding shipped verbatim.** Banned: resurrecting the target's text, photography, logo, or trade dress in the reconstructed page. Defeats: DET-CRWL-009. Bad: headlines and hero photography recovered from a capture are pasted into the rebuild unchanged. Instead: use recovered material as a structural reference only and replace it with the operator's own content unless the D14 record confirms the client owns the rights. Severity: BLOCK.
- **BAN-CL-053 — Bypassing a gate to obtain evidence.** Banned: using borrowed credentials, a shared login, or a paywall workaround to see a page that archives do not hold. Defeats: DET-CRWL-008. Bad: the builder logs in with a customer's credentials found in a forum post to screenshot a members-only page. Instead: record the page as gated and reconstruct only from client-provided access or evidence. Severity: BLOCK.
- **BAN-CL-054 — Skipping a higher evidence tier.** Banned: reconstructing from the design system or from memory while an unchecked Wayback capture or bundle manifest exists. Defeats: DET-CRWL-002. Bad: a deleted pricing page is rebuilt from a screenshot in a blog post although three dated CDX captures were never queried. Instead: query and record every higher tier first; only a recorded absence licenses the next tier down. Severity: BLOCK.
- **BAN-CL-055 — Improvising pages outside the inventory.** Banned: adding pages, sections, or flows that appear in no inventory row because they "must have existed." Defeats: DET-CRWL-013. Bad: a settings page is invented to complete a navigation menu that has a gap. Instead: build only inventory rows; raise the gap as an inventory question for the client. Severity: WARN.

## Gates

- **G-CL-051 — Inventory status audit (automated).** Verifies: CL-103. Check: script scans the inventory table and fails on any row whose status field is empty or outside {`captured`, `inferred`, `designed`}. Pass: 100% of rows carry a valid status. Fail: block shipment. Recorded in: progress.md.
- **G-CL-052 — Parity-claim check (automated).** Verifies: CL-104. Check: grep deliverable docs, page metadata, and filenames for parity-claim phrases — "identical to", "1:1", "pixel-perfect", "exact copy of", "matches the original", "verified copy", "same as" followed by the target's name — joined to any row not labeled `captured`; any match fails. Matching is by claim phrase, never by the bare word "clone": the word clone in a project name (e.g. ShopClone), a file name, or a reference to this playbook or skill family is not a parity claim and is never flagged. Pass: zero matches. Fail: block shipment until the claim is corrected. Recorded in: progress.md.
- **G-CL-053 — Template-coverage and content check (automated).** Verifies: CL-105, CL-106, CL-107. Check: script asserts every inventory row maps to exactly one built template, renders each template with the operator's content set, and greps the rendered output and asset folders for the target's domain, logo filenames, and recovered copy strings; any hit fails. Pass: full coverage, zero target strings or assets. Fail: block shipment. Recorded in: progress.md. Pattern-reference mode: ADAPTED — coverage runs unchanged, and the target-string grep compares against the pattern inventory's protected-items list; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-054 — Evidence-tier log review.** Verifies: CL-102, CL-110, CL-111. Check: manual review of each `inferred`/`designed` row's notes — a CDX digest + timestamp for capture-based claims, a recorded absence for each skipped tier, and a second evidence item for each inferred route. Pass: every row's evidence chain is complete. Fail: return the row to evidence gathering. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the evidence chain is the pattern-inventory citation, the zero-fetch crawl log as the recorded absence of capture tiers, and the design record; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-055 — Authorization pre-flight.** Verifies: CL-101, CL-109. Check: confirm the D14 authorization record exists, predates the first reconstruction artifact, and names reconstruction in scope; list every gated row and its client-provided evidence source. Pass: record valid and every gated row sourced legitimately. Fail: block all reconstruction work. Recorded in: progress.md.

## Anti-patterns

- **Screenshot-memory drift.** The builder "remembers" roughly how the page looked and fills gaps from that impression; catch it by requiring every layout claim to point at a capture, manifest line, or token before it is built.
- **Uniform-confidence reporting.** The progress summary lists all pages as "rebuilt" with no status split, so the client cannot tell evidence from invention; catch it by reporting counts per status label in every update.
- **Gap-filling by symmetry.** A missing page variant is mirrored from its sibling (the "cancel" flow copied from "confirm") without evidence it existed; catch it by checking each variant against its own inventory row.
- **Polish before provenance.** Effort goes into making an inferred page look finished before its evidence chain is recorded, and the polish quietly becomes the claim; catch it by running G-CL-054 before any visual pass.

## Examples

- [Example 1 — The deleted pricing page](examples/example-1.md) — violates/corrects CL-102, CL-110.
- [Example 2 — The gated admin console](examples/example-2.md) — violates/corrects CL-104, CL-109.
- [Example 3 — Recovered copy in the rebuild](examples/example-3.md) — violates/corrects CL-106, CL-107.

## Recall anchors

- Highest evidence tier first; a skipped tier needs a recorded absence.
- Only `captured` pages may claim parity — everything else is labeled honestly.
- Structure from the target, content from the operator.
- No inventory row, no page.
- A gate is a fact about access, never an obstacle to route around.

## Checklist

- [ ] D14 authorization record exists, predates the build, and names reconstruction (CL-101).
- [ ] Every inventory row labeled `captured`, `inferred`, or `designed` (CL-103).
- [ ] CDX digest and timestamp recorded for every capture used as evidence (CL-110).
- [ ] Higher tiers recorded as absent before any lower tier was used (CL-102).
- [ ] No parity language attached to `inferred` or `designed` rows (CL-104, G-CL-052).
- [ ] Rendered pages contain only operator copy, data, and branding (CL-106, CL-107).
- [ ] Gated rows sourced only from client-provided access or evidence (CL-109).
- [ ] Every evidence gap and gap-filling decision logged in the row notes (CL-112).
