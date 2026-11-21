# Example 3 — A phased, verified rebrand

Scenario: A help-desk product renames from HelpKite to Sorrel Desk. It ships
in English, Urdu, and Arabic, and the decision record (CL-701) records a
deliberate phase split: Phase 1 is the English product and website; Phase 2,
two weeks later, is the Urdu and Arabic locales once their replacement copy
has passed inclusive-copy review (CL-710). Each phase is complete in itself,
and the launch is reported as partial until Phase 2 ships.

## Before

The team's original plan has none of that discipline:

- Surfaces are scheduled to drip out as each owner finishes them — website
  on Monday, in-app strings on Thursday, help centre "when support gets to
  it" — so for most of a week the live product presents HelpKite and Sorrel
  Desk as its current identity at the same time, the mixed-identity launch
  banned by BAN-CL-705.
- No baseline is recorded before the swap. When, a few days after launch,
  a top landing page's title is found truncated and a sitemap entry is
  invalid, nobody can say whether the rebrand caused either problem or
  whether both predate it.
- There is no staging rehearsal, no preserved copy of the old token set or
  logo files, and no closing audit. The rebrand is declared "done" from the
  launch-day screenshot thread, while the Arabic locale and two email
  templates quietly still carry the old name, found weeks later by a user.

## After

The rebrand is executed under CL-712, CL-714, and CL-716:

**Phased, rehearsed launch (CL-712).** The full Phase 1 inventory is
executed once on staging and verified there before production is touched.
Production then ships as one release containing the whole Phase 1
inventory — website, app, emails, help centre, and third-party surfaces
together — so the live product never presents two identities as current.
Phase 2 is a second complete release for the Urdu and Arabic locales, and
progress.md reports the rebrand as "Phase 1 of 2 launched" in between,
never as launched (CL-710). The pre-swap token set, logo files, catalogs,
and templates are preserved as a versioned artifact for the whole
verification window, so rollback restores that artifact rather than
reconstructing the old identity from screenshots (CL-713). The change set
contains identity changes only, so the functional regression gate
G-CL-704 compares identical critical-flow results before and after.

**Baseline comparison (CL-714).** Before launch, baseline snapshots are
recorded for the surfaces a rebrand can silently damage: the top landing
pages' titles and indexation status, sitemap validity, structured-data
validity, the status and redirect behaviour of the highest-traffic URLs,
and primary-flow completion (sign-up, sign-in, ticket creation, password
reset). After each phase, the same checks are re-run against the baseline
under G-CL-705. When the post-launch check shows one help-centre URL
returning a redirect chain that the baseline shows as a direct 200, it is
investigated and fixed as a rebrand defect — not waved away as normal
fluctuation without evidence.

**Residue report and closure (CL-716).** At the end of the verification
window, the inventory is re-run as an audit and filed in progress.md:

| Inventory group | Result | Detail |
|---|---|---|
| Website + in-app surfaces (Phase 1) | `swapped` | Verified by the G-CL-702 residue scan on staging and production |
| Urdu + Arabic catalogs (Phase 2) | `swapped` | Second release; glossary entry includes the old name as a do-not-use variant (CL-710) |
| Terms + privacy legal entity name | `kept by exception` | Registered entity unchanged — CL-706 exception, confirmed by the named legal reviewer under CL-707 |
| Pre-rename blog posts + changelog | `kept by exception` | Historical archive under CL-706; not rewritten |
| App-store listing icon | `missed` | Store console still showed the old icon at the CL-715 console check; fixed and re-verified, with the fix date recorded in the report |

Only when G-CL-705 passes — third-party surfaces opened in their own
consoles, baseline differences explained or fixed, the CL-709 contrast
result for the new token pairs on record, and this residue report filed —
is the rebrand marked closed. The one `missed` row does not fail the story;
hiding it would have. It is exactly what the residue report exists to catch.

Note: corrects CL-712, CL-714, and CL-716 — launch whole (or as recorded,
complete phases), compare post-launch state against a pre-rebrand baseline,
and close only with a residue report in which every surface is `swapped`,
`kept by exception`, or `missed` with a fix date.
