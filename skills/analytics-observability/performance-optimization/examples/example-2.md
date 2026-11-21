# Example 2 — The 4 MB hero on a phone-sized slot

## Before

The landing page ships the photographer's original 4 MB hero image. On the office connection it "looks fine," so when the field report shows mobile LCP failing, the team first spends a day inlining critical CSS by hand and tweaking a text-rendering loop. Mobile LCP does not move: the hero image, displayed in a slot a fraction of its natural size, is over 80% of the page's transferred bytes, and the micro-fixes addressed costs too small to see.

## After

The baseline profile ranks causes by measured share, and the hero image is first by a wide margin. One change fixes it at the source: the image is served at the dimensions the layout actually displays, in a modern compressed format, with responsive variants per breakpoint and fetch priority on the LCP image; below-the-fold images lazy-load. The same throttled lab harness records LCP before/after, the budget re-check confirms no other template regressed, and the field p75 is verified over the following window. The CSS and loop tweaks are dropped — unmeasured, and no longer the constraint.

*Corrects AN-244 and AN-247: causes are attacked in measured order — the big costs first — and image weight is fixed at the source, not worked around.*
