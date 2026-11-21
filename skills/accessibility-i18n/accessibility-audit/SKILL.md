# accessibility-audit

## Metadata

- **Owner department:** D13 Accessibility & i18n (AC)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** WCAG 2.2, W3C — https://www.w3.org/TR/WCAG22/ ; axe-core, Deque — https://github.com/dequelabs/axe-core
- **Depends on:** wcag (the audit evaluates against its fixed target)
- **Feeds into:** accessibility-testing, keyboard-accessibility, screen-readers, accessibility-law

## When to use / Do NOT use

- **Use when:** A build, redesign, or release needs an evidence-producing evaluation against WCAG 2.2 AA — before launch, before a procurement claim, or after remediation to verify fixes.
- **Do NOT use when:** Running a quick in-development check (that is accessibility-testing in CI), producing the legal jurisdiction map (accessibility-law), or fixing individual defects (the owning skill, e.g. keyboard-accessibility, does the fix; the audit only finds and records).

## Rules

1. **AC-001 — Fix the scope and target in writing before testing.** The audit plan names the pages, complete processes, and components in scope and states the target as "WCAG 2.2 Level AA" (or the older version a contract or law pins — EAA/EN 301 549 pins 2.1 AA, Section 508 pins 2.0 AA). An audit with no written scope evaluates nothing in particular.
2. **AC-002 — Automated tools are one pass, never the audit.** Automated scanning (axe-core) evaluates only a subset of success criteria. Every audit runs the automated pass AND the manual passes in AC-003; a report based on a tool run alone must state in its own text that it is incomplete.
3. **AC-003 — Every audit includes four passes.** (1) Automated scan over the full scope; (2) keyboard-only walk of every primary process; (3) a smoke test in at least one real screen reader on the primary journeys; (4) visual checks: contrast measurement on rendered colors, 200% zoom, 400% reflow, and focus-visibility observation. Record which pass covered which criteria.
4. **AC-004 — Audit complete processes, not isolated pages.** Scope is defined as user processes (register → verify email → first task; browse → cart → checkout). Conformance is per complete process: a checkout whose step 3 fails is not conformant even if steps 1–2 pass.
5. **AC-005 — Every finding cites a success criterion.** Each finding names the WCAG criterion number it fails (e.g. 1.4.3, 2.4.7, 4.1.2), the page or process step, exact reproduction steps, and a screenshot or recording. A finding worded only as "accessibility issue" is returned for rework.
6. **AC-006 — Severity ranks by user impact, not tool order.** Severity is set by whether the defect blocks, degrades, or merely inconveniences task completion for an affected user group — never by the order or default severity the scanning tool printed.
7. **AC-007 — Report per-criterion conformance, not a verdict.** The report rates each in-scope criterion "supports / partially supports / does not support" (VPAT-style), with the method used per criterion. The word "accessible" never appears as a blanket claim about a page, process, or product.
8. **AC-008 — State the technical result; never a legal conclusion.** Reports state standard, version, level, scope, and date. They never state "ADA compliant" or "legally accessible"; legal applicability is flagged for accessibility-law/D14 to confirm.
9. **AC-009 — Date and version every report; re-audit after fixes.** Conformance decays with every release. Each report carries its date and the build/commit audited; fixed findings are verified by re-running the failing pass, and the re-audit result is appended, not overwritten.
10. **AC-010 — Third-party components are in scope.** Payment widgets, chat embeds, cookie banners, and video players are audited like first-party code (focus order, focus obscured under 2.4.11, iframe titles). "The vendor's widget" is recorded as a finding with the vendor named, never as an exemption.
11. **AC-011 — Triage before sign-off.** Every finding enters a findings register with severity and an owner; sign-off requires zero un-triaged critical findings. Untested scope (e.g. a screen-reader/browser combination not run) is listed as residual risk in the report, not silently omitted.
12. **AC-012 — Method transparency.** The report's method section lists, per pass: tool and version, browser, assistive technology and version, viewport/zoom settings, and the criteria that pass could and could not evaluate — so a reader can see exactly what the evidence does and does not cover.

## BAN list

- **BAN-AC-001 — Scan-only audit reported as conformance.** Banned: running axe-core (or any automated scanner) and reporting the product "accessible" or "WCAG compliant" from its output alone. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: report says "0 axe violations — site is WCAG 2.2 AA compliant" while no keyboard or screen-reader pass was run and focus is invisible site-wide. Instead: run all four passes in AC-003 and report per-criterion results under AC-007, naming which criteria each pass covered. Severity: BLOCK.
- **BAN-AC-002 — Findings without a criterion.** Banned: audit findings phrased as "accessibility issue", "not accessible", or "needs improvement" with no WCAG success-criterion number, reproduction steps, or evidence. Defeats: DET-UX-006. Bad: register entry "Checkout page — accessibility problems, fix ASAP." Instead: "Checkout step 3 — fails WCAG 1.4.3: placeholder text #9a9a9a on #ffffff (2.6:1) on card-number field; reproduce by loading /checkout/payment; screenshot attached." Severity: BLOCK.
- **BAN-AC-003 — Accessibility overlay offered as the fix.** Banned: installing a third-party "accessibility overlay" widget and closing audit findings against it instead of fixing the underlying code. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: findings for placeholder-only labels closed with "resolved by overlay toolbar." Instead: fix the code — give every field a persistent programmatic label — and re-audit the failing pass. Severity: BLOCK.
- **BAN-AC-004 — Clickable divs accepted as controls.** Banned: passing a page whose interactive elements are clickable `<div>`/`<span>` elements with no role, accessible name, or keyboard path, because they "work with a mouse". Defeats: DET-UX-016. Bad: audit notes "filters operable" after mouse-testing a div-based filter bar that keyboard focus never reaches. Instead: record a 4.1.2/2.1.1 finding with reproduction via the keyboard walk; the fix is a native `<button>` or a full APG-pattern widget. Severity: BLOCK.
- **BAN-AC-005 — Legal verdict in a technical report.** Banned: stating "ADA compliant", "EAA compliant", or "legally accessible" anywhere in an audit deliverable. Defeats: DET-NONE — no DET parameter names this signal; pattern owned by this skill. Bad: summary page headed "This product is ADA compliant." Instead: state "Evaluated against WCAG 2.2 Level AA on 2026-11-21; scope and per-criterion results below; legal applicability to be confirmed by D14." Severity: BLOCK.

## Gates

- **G-AC-001 — Automated scan archived.** Verifies: AC-002, AC-003. Check: run `npx @axe-core/cli <each in-scope URL> --save audit/axe-<date>.json` (or the project's axe-core CI job) over every page and process step in the written scope. Where the axe-core CLI cannot be installed or run, the fallback route is this skill's manual gates G-AC-002 (keyboard walk) and G-AC-004 (criterion checklist) performed and recorded in full, with the substitution recorded in progress.md; the automated run remains required wherever the tooling is available. Pass: a dated report file exists for 100% of in-scope URLs and every violation is entered in the findings register. Fail: block sign-off. Recorded in: progress.md.
- **G-AC-002 — Keyboard walk completed.** Verifies: AC-003, AC-004. Check: manual pass — complete each primary process keyboard-only (Tab/Shift+Tab/Enter/Space/arrow keys/Esc), logging every trap, invisible focus stop, and lost-focus event against its criterion. Agent-evidence form: a scripted keyboard-only traversal (e.g. Playwright driving the same key sequences) that logs the same trap, invisible-stop, and lost-focus findings against their criteria satisfies this gate's evidence, with the traversal script and its log recorded in progress.md; where no scripted traversal can run, this gate is **human-required** and blocks autonomous sign-off until the human walk is recorded. Pass: a completed keyboard-walk checklist exists for every primary process, with findings registered. Fail: block sign-off. Recorded in: progress.md.
- **G-AC-003 — Screen-reader smoke test completed.** Verifies: AC-003, AC-004. Check: manual pass — run the primary journeys in at least one real screen reader (e.g. NVDA + Chrome or VoiceOver + Safari), navigating by headings, landmarks, and form controls; verify accessible names, roles, and live-region announcements. **Human-required:** the evidence is a human listening to real assistive technology; no automated or agent-produced substitute satisfies this gate, and autonomous sign-off is blocked until the human test is recorded. Agent-evidence form (interim evidence only — it prepares and de-risks the human test but never replaces it): the agent records an accessibility-tree audit of each primary journey (accessible names, roles, landmarks, and live regions present and correctly ordered) plus the G-AC-002 keyboard evidence in progress.md, marks this gate human-required, and records a human-evidence waiver request naming the human test still owed. Pass: a dated smoke-test record names the AT/browser versions used and lists pass/fail per journey. Fail: block sign-off. Recorded in: progress.md.
- **G-AC-004 — Criterion checklist complete.** Verifies: AC-005, AC-007, AC-012. Check: open the audit checklist artifact; confirm every in-scope WCAG 2.2 A/AA criterion is marked pass / fail / not-applicable and that each mark names the method (automated, keyboard, screen reader, visual) that produced it. Pass: zero unmarked in-scope criteria. Fail: block sign-off. Recorded in: progress.md.
- **G-AC-005 — Zero un-triaged criticals.** Verifies: AC-006, AC-011. Check: query the findings register for severity = critical AND status = un-triaged. Pass: count is zero, and every critical has an owner and a criterion citation. Fail: block sign-off. Recorded in: progress.md.

## Anti-patterns

- **Tool-order triage.** Working the findings register top-to-bottom in scanner output order, so a cosmetic contrast nit gets fixed while a keyboard trap sits at row 40. Catch it by re-sorting the register by user impact (AC-006) before assigning any work.
- **Homepage-only sampling.** Auditing the home page and two marketing pages, then writing conclusions about "the product" while checkout and account flows were never opened. Catch it by comparing the report's claims against the written scope (AC-001) — claims may not exceed scope.
- **Screenshot evidence for dynamic defects.** Attaching a static screenshot as the sole evidence for a focus-order, live-region, or dialog defect that only exists in motion. Catch it by requiring a recording or step-by-step reproduction for any finding whose defect is temporal (AC-005).
- **Silent re-audit overwrite.** Editing the original report after fixes so it reads as if the defects never existed. Catch it by checking the report's version history: re-audit results are appended with their own date (AC-009).

## Examples

- [Example 1 — Scan-only report vs. four-pass audit](examples/example-1.md) — violates/corrects AC-002.
- [Example 2 — Vague finding vs. criterion-cited finding](examples/example-2.md) — violates/corrects AC-005.
- [Example 3 — Page sampling vs. complete-process audit](examples/example-3.md) — violates/corrects AC-004.

## Recall anchors

- A scan is one pass of four — never the audit.
- No criterion number, no finding.
- Audit processes end to end, not pages.
- Report per criterion: supports, partially, does not.
- Technical result only — legal verdicts belong to D14.

## Checklist

- [ ] Written scope names pages, complete processes, components, and the WCAG version/level target (AC-001).
- [ ] All four passes ran: automated scan, keyboard walk (or its scripted agent-evidence form, G-AC-002), screen-reader smoke test (human-required, G-AC-003), visual checks (AC-003).
- [ ] Every finding cites a success criterion, reproduction steps, and evidence (AC-005).
- [ ] Severities are ranked by user impact, and zero criticals are un-triaged (AC-006, G-AC-005).
- [ ] Report rates conformance per criterion and states method and residual risk (AC-007, AC-011, AC-012).
- [ ] Report contains no legal verdict and no blanket "accessible" claim (AC-008).
- [ ] Report is dated and versioned against the audited build (AC-009).
