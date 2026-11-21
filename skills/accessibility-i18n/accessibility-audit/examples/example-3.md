# Example 3 — Page sampling vs. complete-process audit

## Before

> **Scope:** Home page, About page, Pricing page.
> All three pages pass the automated scan and the contrast check. Report conclusion: "Registration and checkout conform to WCAG 2.2 AA."

Registration and checkout were never opened. Step 3 of checkout (payment confirmation) moves focus to the top of the document after the confirmation dialog closes, stranding keyboard and screen-reader users — a defect no sampled page could have revealed, now covered by a conformance claim.

## After

> **Scope:** The complete processes (1) register → verify email → first task, and (2) browse → cart → checkout → confirmation, plus the home, about, and pricing pages. Target: WCAG 2.2 AA.
> Finding 12 — Checkout step 3 (confirmation) — fails WCAG 2.4.3 Focus Order, severity: major. Closing the confirmation dialog drops focus to the document top instead of returning it to the "Place order" trigger. Reproduce: complete checkout keyboard-only; on the confirmation dialog press Esc and observe focus. Per-criterion results for both processes are in the attached table; no conformance statement is made for any process step not listed in this scope.

*Demonstrates AC-004 — audit complete processes, not isolated pages.*
