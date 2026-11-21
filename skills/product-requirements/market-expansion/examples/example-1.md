# Example 1 — GO recorded over a BLOCKED legal dimension

_All product, people, dates, and figures in this example are hypothetical
and illustrative. They are a worked example of the record format, not
real-world market facts._

Scenario: LedgerLane, a hypothetical invoicing SaaS already shipping in
its home market, is considering entry into Brazil. Target window:
Q3 2026. Decision owner: Head of Expansion. Named decider: VP Product.

## Before

The expansion "decision" is a line in the leadership sync notes dated
2026-03-02:

> "Leadership agreed — Brazil is a GO for Q3. Team is confident on all
> fronts, overall readiness about 85%. Start the local contract and
> announce the date at the April partner event."

There is no readiness record (violates **PR-261** — a judgement that
lives only in a meeting does not exist), no dated, signed decision in
one of the three permitted values (violates **PR-262**), and no criteria
written before scoring (violates **PR-263**). The "85%" collapses six
dimensions into one average (violates **PR-264**).

Worse, the one check that was done is buried in an email thread: the
privacy-laws obligations register row for Brazil, dated 2026-02-20,
records the local tax registration as "required, not obtained." Under
**PR-269** that status makes the legal dimension **BLOCKED**, and under
**PR-265** a GO recorded over a BLOCKED dimension is invalid — treated
as no decision. Treating the sync remark as the decision is also
**BAN-PR-134** (the verbal go), and the planned April announcement
would be **BAN-PR-133** (announcement before the backing process
exists).

## After

The sync remark is voided and replaced with a single readiness record,
`brazil-readiness.md`, owned and decided as named above. The criteria
were written into the record on 2026-03-09, before any dimension was
scored on 2026-03-16 — the ordering **G-PR-133** audits (**PR-263**).
Each dimension is scored separately, each verdict citing dated evidence
(**PR-264**, **PR-266**); there is no overall percentage:

| Dimension | Verdict | Evidence (dated) |
|---|---|---|
| Localization | READY WITH CONDITIONS | localization-workflow sign-off, 2026-03-12: Portuguese tier is UI-only, signed off; public claim must say UI-only, not "fully localized" (**PR-267**) |
| Payments | READY WITH CONDITIONS | Live-environment test log, 2026-03-14: one real charge, one failure path, and one refund completed for the card method claimed; the second claimed method has test-mode evidence only, so it is struck from the claimed set until live-tested (**PR-268**, **G-PR-134**) |
| Legal | **BLOCKED** | privacy-laws obligations register row, 2026-02-20, and data-residency verdict, 2026-02-24, imported unchanged (**PR-269**): tax registration recorded as "required, not obtained" |
| Pricing | READY | Local price set from in-market competitor pages captured 2026-03-10 and checked against market unit economics in the record (**PR-270**, **PR-275**) |
| Support | READY WITH CONDITIONS | Named support vendor, Portuguese, 08:00–20:00 America/Sao_Paulo, first-response target 4 business hours; contract signed, staffing roster due 2026-04-15 (**PR-271**) |
| Cultural fit | READY WITH CONDITIONS | Named in-market reviewer (São Paulo) walked the primary flows on 2026-03-11; 6 adaptations recorded — 4 done, 2 scheduled as dated conditions (**PR-272**) |

Demand is recorded separately from context (**PR-273**): 14 dated
in-market interviews (Feb–Mar 2026) and a written partner commitment
are cited as demand evidence; a country market-size figure appears
only in a section explicitly labeled "context, not demand evidence"
(**BAN-PR-131** avoided — no unsourced market number is stated).

The record also carries the pilot plan (**PR-274**), the exit plan
(**PR-277**), and a review date of 2026-09-30 (**PR-279**), so the
completeness scan **G-PR-131** passes.

Decision, signed by the VP Product and dated 2026-03-18 (**PR-262**):

> **CONDITIONAL GO.** No public launch, no announcement, and no launch
> date until both conditions close:
> 1. Tax registration obtained and the legal dimension re-evidenced
>    from the privacy-laws register — owner: General Counsel —
>    due 2026-05-29.
> 2. Support vendor roster staffed to the PR-271 coverage above —
>    owner: Support Lead — due 2026-04-15.
>
> If condition 1 is not closed by its date, this decision converts to
> a re-review, not to a launch.

The blocker scan **G-PR-132** passes: one dimension is BLOCKED, the
decision is CONDITIONAL GO (not GO), and the BLOCKED dimension appears
as a dated condition. The April partner-event announcement is cut;
under **PR-280** nothing public may claim availability the record does
not yet support.

## Note

Corrected under PR-265 and PR-269, with PR-261, PR-262, PR-263, PR-264,
and PR-266: a BLOCKED dimension blocks GO, the legal verdict is imported
from the registers rather than re-judged in the room, and the only
decision that exists is the written, dated one in the record.
