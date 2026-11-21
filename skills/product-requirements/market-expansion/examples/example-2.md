# Example 2 — The converted price

_All product, people, dates, and figures in this example are hypothetical
and illustrative. They are a worked example of the record format, not
real-world market facts or real competitor prices._

Scenario: LedgerLane (the hypothetical invoicing SaaS from Example 1)
is preparing its German pricing page. Home-market price: $20/month.

## Before

The local pricing page is drafted in one step:

> "Pro — €18.40/month"

€18.40 is $20 converted at the spot exchange rate on the day the page
was built (2026-04-06). No in-market evidence was gathered, no local
unit economics were run, and the number was typed by hand into three
places — the pricing page, the checkout configuration, and a sales
one-pager — which have already drifted apart: the one-pager says
€18.50 after a manual "rounding fix."

This is **BAN-PR-132** (FX-converted pricing) and violates **PR-270**:
a price produced by converting the home-market price at a spot rate,
with no local evidence step, is not a local price. It also fails
**PR-275**, because the "German margin" in the planning sheet is the
home-market margin pasted into a new row — payment-processing cost,
support cost, and taxes are all home-market inputs, none flagged as
assumptions.

## After

The converted figure is deleted from all three surfaces. The readiness
record's pricing section is rebuilt in the order **PR-270** and
**PR-275** require:

1. **In-market evidence first (PR-270).** The competitive-analysis
   input, captured from live local pricing pages on 2026-04-13, shows
   the three closest local competitors for the same tier at
   hypothetical €11, €13, and €15/month. A dated in-market
   willingness-to-pay exercise (12 interviews, 2026-04-08 to
   2026-04-11, recorded in the record's demand section under
   **PR-273**) found the target segment treating roughly €14 as the
   "expected, not suspiciously cheap" point for this feature set.
2. **Market unit economics re-derived (PR-275).** The check is rebuilt
   from local inputs only: the candidate local price; the actual
   processing cost of the payment methods live-tested under **PR-268**
   (from the provider's live-environment records, not the home-market
   rate); the local support cost from the **PR-271** model (named
   vendor, German-language coverage); and the applicable local tax
   treatment recorded under **PR-269**. Every input carries its local
   source and date (**PR-266**); no home-market input survives, so no
   input needs an "assumption" flag.

   At a candidate price of €14/month the re-derived contribution is
   positive but thinner than the home market's, mainly because local
   support cost per user is higher — a fact the converted €18.40 had
   hidden rather than solved, since it priced the product above every
   local competitor.
3. **One price, handed to the fact sheet (PR-270).** The decider
   records the German price as **€14/month** in the readiness record,
   dated 2026-04-20, and that single figure is handed to the fact
   sheet. The pricing page and checkout render from that source; the
   sales one-pager links to the pricing page instead of restating the
   number, so the three surfaces cannot drift again.

Before publication, the page copy is checked against the record under
**PR-280** and gate **G-PR-135**: the price matches the fact sheet,
and the page claims only the payment methods that passed the live-fire
check **G-PR-134** under **PR-268**.

## Note

Corrected under PR-270 and PR-275, avoiding BAN-PR-132: the local price
is a deliberate decision built from in-market competitor and
willingness-to-pay evidence and from unit economics re-derived with
local inputs — never an exchange-rate conversion of the home price.
