# Example 2 — Same wireframe, new paint

Scenario: an authorized clone-redesign of a reference class-booking app
for gyms. Function parity is owed for class search, waitlist join/leave,
and booking cancellation. The two-column spec (CL-142) puts navigation
grouping, page composition, and visual hierarchy in the expression column.

## Before

The rebuild's tokens and copy genuinely pass G-CL-072 and G-CL-073 — new
palette, new typeface, all headings rewritten from the function column
under CL-147. The team presents it as a completed redesign.

A wireframe overlay tells a different story. On the home template:

```text
Reference home            Rebuild home
----------------------    ----------------------
Top bar: logo left,       Top bar: logo left,
  search centre,            search centre,
  avatar right              avatar right
Hero: full-width photo    Hero: full-width photo
  + headline + CTA          + new headline + CTA
Row: 4 category tiles     Row: 4 category tiles
Section: "Popular near    Section: renamed heading,
  you" horizontal cards     same horizontal cards
Section: timetable list   Section: timetable list
Footer: 4 link columns    Footer: 4 link columns
```

Every template matches the same way: identical grid structure, identical
first-viewport composition, identical navigation placement, identical
section ordering. Only colors, fonts, imagery, and wording differ.

This is BAN-CL-072 — a reskin presented as a redesign — and a direct
CL-149 failure: "same layout, new colors and fonts" fails however original
the tokens are. No structural differences were named in the design record,
and the divergence log has no entries for the resemblances, so G-CL-074
(layout-signature review) blocks sign-off.

## After

The templates return to design — not to styling tweaks. The design record
is amended first, naming the structural choices per template and the
rebuild's own rationale for each (per CL-149, difference with a reason,
not difference for its own sake):

```text
Template: Home — structural differences recorded (CL-149, CL-152)
- Grid: 12-col editorial grid ->  sidebar + content split; class
  discovery is a repeat task, so filters stay visible instead of
  sitting behind a hero.
- First viewport: full-width photo hero removed; first viewport is
  the member's next booked class + a compact search field.
- Navigation: top bar -> left rail (Bookings, Schedule, Waitlist,
  Profile); grouping changed from the reference's marketing-led
  grouping to task-led grouping (CL-148: IA may move).
- Section order: timetable first, category browsing second,
  promotions moved to the Schedule page entirely.
```

The flow inside the page does not move silently with the layout
(CL-148): search → results → class detail → confirm booking keeps its
exact step sequence, required inputs, and validation outcomes from the
frozen behavior-cloning specs. One deliberate functional change the new
layout suggested — merging the waitlist confirmation step into the class
detail page — is logged in the divergence log as a CL-148 functional
deviation with a reason and an approver *before* it is built, so the
behavior suite's failure on that step reads as a recorded decision, not
a bug.

One resemblance is kept and logged under CL-145: the cancellation flow
retains a conventional confirm-dialog pattern because the destructive
action's confirmation behaviour is dictated by the function, and the log
entry says so.

G-CL-074 is re-run: the reviewer compares structure-only wireframes and
confirms every named difference is present and every remaining
resemblance has a CL-145 entry. It passes; both the differences and the
exception are in the divergence log (CL-152).

## Note

Violates/corrects CL-149 and BAN-CL-072, with CL-145, CL-148, and CL-152
doing the corrective work. Passing the token and copy gates (G-CL-072,
G-CL-073) did not make the Before a redesign — layout signature is its
own obligation, checked by its own gate.
