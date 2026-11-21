# Example 3 — Focus lost when the dialog closed

## Before

The axe scan reports zero violations on the settings page, so the delete-account flow is never walked by keyboard. In production, a keyboard user opens "Delete account," confirms, and focus drops to `<body>` — they must Tab through the entire header and navigation again to continue, with no announcement of what happened.

## After

The per-release keyboard walkthrough includes the delete-account flow. The tester reaches the dialog by Tab, confirms, and records that focus lands on `<body>` instead of returning to the "Account settings" heading. A defect is filed naming WCAG 2.4.3 (Focus Order) with the walkthrough step as evidence; D3 fixes the focus return, and the same walkthrough step is re-run and passes before the defect closes.

Note: demonstrates QA-104 — the keyboard-only walkthrough of named critical flows catches what the automated scan cannot.
