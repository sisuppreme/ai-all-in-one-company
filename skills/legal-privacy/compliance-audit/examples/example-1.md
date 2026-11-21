# Example 1 — The 94% dashboard

Note: demonstrates LG-127 (findings are defects, not percentages) and BAN-LG-061.

## Before

The quarterly compliance dashboard shows a single green figure: "Compliance: 94%". The number is computed from how many obligations-register rows exist and have an owner filled in. Underneath it, three controls have never been test-run — the DSAR flow, the consent matrix, and the license scan — and one of them, the DSAR flow, is broken: the request form's submit handler returns a server error. Nobody knows, because the score has no findings list attached to it, and the 94% is quoted in a sales deck.

## After

The dashboard's score is deleted. In its place the audit publishes a findings list: each control with its last test date and evidence link, and each gap as a finding — "F-2026-014: DSAR intake flow fails on submit (drill, 2026-11-21). Severity: high. Owner: backend lead. Remediation date: 2026-12-05." The DSAR control is recorded as failing until the drill is re-run and passes. The sales deck drops the percentage and cites only the dated audit record.
