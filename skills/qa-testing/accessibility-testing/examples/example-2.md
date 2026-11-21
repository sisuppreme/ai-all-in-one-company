# Example 2 — "WCAG compliant" from a scan

## Before

Release note: "This release is WCAG 2.2 AA compliant — the automated accessibility scan passed with zero violations." No keyboard walkthrough or screen-reader pass was performed. A keyboard trap in the new checkout dialog (Tab cycles inside it, Esc does nothing) ships in the same release.

## After

Release note: "Accessibility testing this release: axe scan clean on home, signup, checkout, and account pages (default, error, and dialog states); keyboard-only walkthrough completed on signup, checkout, and password-reset flows; NVDA pass on checkout — one defect filed (focus not returned after the payment dialog closes, WCAG 2.4.3), retest pending." The trap is caught by the walkthrough before release, and the note claims only what was actually checked.

Note: demonstrates QA-110 — a scan result is evidence about some problems, never a conformance claim.
