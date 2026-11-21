# Example 1 — Eyeballed contrast vs. computed token pairs

## Before

The design review approves a "soft, minimal" palette by eye: placeholder and helper text in `#9a9a9a` on `#ffffff`, secondary button text in `#7f9db9` on white. Nobody measures anything; the mock "looks clean." In the rendered product the placeholder text sits at 2.6:1 and the button text at 2.9:1 — both below the 4.5:1 floor for normal text (1.4.3), and low-vision users cannot read the card form's fields at all.

## After

Every text/background pair lives in the token file and is checked by script (G-AC-011): the script parses the actual hex values, computes each ratio, and fails the build below 4.5:1 for normal text or 3:1 for large text and component boundaries. The palette is adjusted once, in the tokens — helper text to `#595959` on `#ffffff` (7.0:1), button text to `#1f5fa6` on `#ffffff` (6.2:1) — and every screen built from those tokens inherits the pass, in default, hover, and error states alike.

*Demonstrates AC-022 — contrast floors are computed from the actual palette, never eyeballed.*
