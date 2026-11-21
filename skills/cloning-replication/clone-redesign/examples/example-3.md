# Example 3 — Parity by feature list

Scenario: an authorized clone-redesign of a reference expense-tracking
app, approaching handover. Function parity is owed for receipt capture,
expense filtering, report export, and approval submission. The redesign
itself is sound: original tokens (G-CL-072 passed), copy written from the
function column (G-CL-073 passed), structurally distinct templates
(G-CL-074 passed).

## Before

The handover document is submitted for sign-off:

```markdown
## Handover — acceptance summary

- Feature parity with the reference: CONFIRMED. Both products provide
  receipt capture, expense search and filters, CSV/PDF report export,
  and manager approval submission. Feature lists compared 1:1,
  no gaps found.
- Visual similarity check: pixel suite run against reference
  screenshots — similarity score low, so design distance confirmed.
- Ready for client acceptance.
```

Two failures, both at the acceptance step:

1. **BAN-CL-075 — parity claimed from the feature list.** No behavior
   suite ever ran. "Both products list filters" says nothing about
   whether the rebuild's filter validation behaves like the reference's
   frozen specs — e.g. whether an invalid date range is rejected inline
   with no request fired, or whether double-submitting an approval
   produces one submission or two. Those behaviours were in the
   function column (CL-142) with behavior-cloning spec citations
   (CL-143), and none of them were exercised.
2. **BAN-CL-074 — pixel-parity tuning in either direction.** The pixel
   suite (G-CL-061) was run on a clone-redesign at all. Under CL-150 it
   is not a distance meter: a low similarity score proves nothing the
   token, copy, and layout gates don't already prove properly, and
   running it invites tuning against the overlay.

G-CL-075 blocks the handover: the acceptance record contains neither the
frozen suite's run ID nor the G-CL-061 NOT APPLICABLE disposition.

## After

Acceptance is rebuilt in CL-150's order — behavior parity first, design
distance second:

```markdown
## Handover — acceptance record (G-CL-075)

(a) Behavior parity — CL-150(a)
    Frozen behavior suite run: run-2026-11-21-expenses-redesign-03
    Suite hash matches the frozen behavior-cloning set: YES
    Result: PASS, unmodified suite.
    Findings during the run: the invalid-date-range spec failed on
    the first run — the rebuild submitted the request instead of
    rejecting inline. Fixed in the filter, suite re-run, PASS.
    (This is exactly the behaviour the feature list could not see.)

(b) Design distance
    G-CL-072 token distance diff: PASS
    G-CL-073 copy-overlap scan: PASS
    G-CL-074 layout-signature review: PASS

(c) Pixel suite disposition — CL-150
    G-CL-061: NOT APPLICABLE — clone-redesign; design distance is
    judged by G-CL-072 to G-CL-074. Recorded in the divergence log
    (CL-152). Not run.

(d) Claims sweep — CL-151
    Handover and product copy claim "functionally equivalent to the
    reference" and "behavior verified against the reference",
    citing run-2026-11-21-expenses-redesign-03. No claim of visual,
    brand, or copy resemblance anywhere; the reference's name, logo,
    and screenshots appear in no marketing or product surface.
```

The claims language is the deliverable's wording now: parity is claimed
only where the evidence exists (behavior, cited by run ID), and nothing
in the handover implies the rebuild looks like, reads like, or is
endorsed by the reference — the LG-187 side-by-side test referenced by
CL-151.

## Note

Violates/corrects CL-150 and BAN-CL-075, with BAN-CL-074 also breached
and corrected in the Before. A matching feature list is an inventory
check, not a parity result: acceptance requires the frozen suite's
passing run plus the design-distance gates, in that order, and the
pixel suite recorded NOT APPLICABLE rather than run.
