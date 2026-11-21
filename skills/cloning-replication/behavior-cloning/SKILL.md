# behavior-cloning

## Metadata

- **Owner department:** D16 Cloning & Replication (CL)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://playwright.dev/docs/test-snapshots ; https://webrecorder.net/browsertrix/
- **Depends on:** clone-ethics, page-inventory
- **Feeds into:** page-reconstruction, fidelity-verification

## When to use / Do NOT use

- **Use when:** an authorized replication engagement has a signed-off page inventory and the target's interactive behavior — forms, modals, filters, routing, validation, animations — must be specified from observation so the rebuild can be re-implemented in original code and accepted against the same recordings.
- **Do NOT use when:** no D14 clone-ethics authorization record exists (run clone-ethics first; this skill refuses to start), the task is page structure or styling (page-inventory, design-extraction), reconstructing pages that cannot be observed (page-reconstruction, which consumes this skill's `unobserved` records), or verifying a finished rebuild (fidelity-verification).

## Rules

1. **CL-081 — Authorization precedes the first recording.** No interaction is recorded, scripted, or replayed on the target before the project's clone-ethics authorization record exists, is dated, names the target and the recording scope, and predates the first recording log entry. Recording tooling checks for the record and fails closed when it is absent or out of scope.
2. **CL-082 — Behavior is specified as executable tests, not prose.** Every in-scope flow is recorded as a scripted interaction (Playwright test scripts are the working format): the clicks and inputs, the expected state change after each step, and the network responses behind it. A flow described only in prose impressions is treated as uncloned.
3. **CL-083 — Every spec records trigger, action, and observed result.** Each interaction spec names its trigger (control, input), the action performed, the observed state change, and any network request the behavior depends on. Only what the recording shows may be written; an expected result the agent did not observe is not part of the spec.
4. **CL-084 — Re-implementation is original code; the target's code is never copied.** Behavior is rebuilt from the observation specs in the project's own code. The target's scripts, bundles, or styles are never copied, deobfuscated, decompiled, or adapted into the rebuild — similarity of behavior is the goal, never similarity of source.
5. **CL-085 — Unobservable interactions are recorded as unobserved, never invented.** Any interaction the operator cannot legitimately observe — behind a login or paywall the operator does not hold, or in a state that cannot be reached — is entered in the behavior record as `unobserved` with the reason. It is never filled in from generic patterns, competitor sites, or plausibility, and it passes to page-reconstruction labeled as such.
6. **CL-086 — Recording uses only the operator's own provisioned accounts.** Where a flow needs an account, the client provisions a test account for the engagement, or the agent registers its own where the target permits. The site owner's, an employee's, or any real user's credentials are never used, borrowed, or replayed from a captured session.
7. **CL-087 — Test data is synthetic, and recordings carry no real personal data.** All inputs used in recordings are fabricated test values. If a recording incidentally captures real users' personal data (names, emails, order details visible in an account view), that data is scrubbed from the recording before it is stored, and the scrub is noted in the recording log.
8. **CL-088 — The evidence set is frozen at inventory sign-off.** The recordings and specs are frozen when the inventory is signed off, and the frozen set is what the rebuild is accepted against. If the source changes afterward, the change is recorded as drift with a date; frozen tests are never silently re-recorded to match.
9. **CL-089 — Coverage spans the whole inventoried interaction surface.** Menus, forms and their validation messages, modals, filters and sorting, search, client-side routing, animation triggers, and error and empty states are all in scope: every interaction listed in the page inventory gets a spec or an `unobserved` record — none is skipped silently.
10. **CL-090 — Content surfaced by behavior is replaced, not transcribed.** Form mechanics, flow order, and validation behavior are functional and may be recreated; the target's marketing copy, help text, error-message wording beyond functional necessity, and branded assets are replaced with the operator's own content, never transcribed verbatim into the rebuild.
11. **CL-091 — Observed timing and edge cases are part of the spec.** Where the recording shows them, the spec records debounce and delay behavior, double-submit handling, invalid-input responses, and slow- or failed-response states. An edge case that was not exercised is listed as unexercised, not assumed.
12. **CL-092 — The frozen suite accepts the rebuild unmodified.** The recorded interaction suite runs against the rebuild unchanged as its acceptance test; development continues until the same scripts pass. Editing, weakening, or deleting a test to make the rebuild pass falsifies the result and is treated as a failed acceptance.

## BAN list

- **BAN-CL-041 — Working by screenshot.** Banned: declaring an interactive element or flow "working" or "cloned" from its appearance in screenshots without executing it. Defeats: DET-CRWL-013. Bad: the rebuild report marks the checkout "behavior verified" because the button looks right; nobody clicked it, and the source's submit actually validates stock before charging. Instead: record every flow as an executable interaction test and let the coverage gate (G-CL-042) refuse any flow without one, under CL-082. Severity: BLOCK.
- **BAN-CL-042 — The target's code in the rebuild.** Banned: copying, deobfuscating, or adapting the target's JavaScript, bundles, or stylesheets into the rebuild to reproduce behavior. Defeats: DET-CRWL-009. Bad: the source's minified filter widget is deobfuscated and pasted into the rebuild because "rebuilding it would take a week". Instead: specify the filter's observed behavior (inputs, state changes, network calls) and re-implement it in original code, under CL-084. Severity: BLOCK.
- **BAN-CL-043 — Invented gated behavior.** Banned: writing a behavior spec for a flow behind a login or paywall the operator cannot legitimately access and presenting it as observed behavior. Defeats: DET-CRWL-002. Bad: the members' billing flow is specced from a competitor's flow and the operator's expectations, and the record lists it as "recorded from source". Instead: enter the flow as `unobserved` with the access reason and hand it to page-reconstruction labeled as such, under CL-085. Severity: BLOCK.
- **BAN-CL-044 — Real credentials, real people's data.** Banned: recording with the site owner's or any real user's credentials, replaying a captured real session, or storing recordings that contain real users' personal data. Defeats: DET-CRWL-008. Bad: the client shares the admin login "to save time", and the recordings capture real customer names and orders that ship with the project files. Instead: use only provisioned test accounts and synthetic data, and scrub any incidental personal data before storage, under CL-086 and CL-087. Severity: BLOCK.
- **BAN-CL-045 — The success toast accepted as behavior.** Banned: treating a success message, toast, or redirect as proof a flow works, without verifying the state change or network effect behind it. Defeats: DET-CRWL-004. Bad: the source's contact form shows "Message sent!" on submit, the spec records "form sends message", and the rebuild clones the toast — while the source in fact posts to a CRM the clone never reproduces. Instead: record the network request and resulting state change as the behavior; where no effect can be verified, say so in the spec, under CL-083. Severity: BLOCK.

## Gates

- **G-CL-041 — Authorization and account pre-flight check.** Verifies: CL-081, CL-086. Check (automated): before recording starts, a script asserts the clone-ethics authorization record exists, is dated, covers behavior recording on the target, and its commit timestamp predates the run; the recording plan lists only provisioned test accounts. Pass: record complete and pre-committed, accounts provisioned. Fail: recording refuses to start (fail closed). Recorded in: progress.md. Pattern-reference mode: ADAPTED — no recording or test accounts exist; the check asserts the authorization record predates the first behavior spec and covers pattern-reference specification; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-042 — Behavior-spec coverage check.** Verifies: CL-082, CL-085, CL-089. Check (automated): diff the page inventory's interaction list against the behavior record; every inventoried interaction must have either an executable spec naming trigger, action, and expected result, or an `unobserved` entry with a reason. Pass: the diff is empty. Fail: block; behavior-cloning is incomplete until every interaction is specced or honestly recorded as unobserved. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the diff runs against the pattern inventory's interaction list, and specs are marked designed-from-pattern; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-043 — Frozen-suite acceptance run.** Verifies: CL-088, CL-092. Check (automated): the recorded interaction suite runs in CI against the rebuild, with the test files hash-matched to the frozen evidence set so any edit is detected. Pass: every in-scope test passes unmodified. Fail: block delivery; failures are fixed in the rebuild, never in the tests. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the frozen set is the pattern-derived spec suite frozen at spec sign-off instead of at recording; hash-matching runs unchanged; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-044 — Recording hygiene scan.** Verifies: CL-084, CL-087, CL-090. Check (automated): scan the stored recordings, specs, and rebuild source for (a) real-looking personal data patterns, (b) verbatim strings from the target's marketing and help copy beyond functional labels, and (c) target-origin code fingerprints (bundle banners, distinctive minified identifiers). Pass: zero hits in all three scans. Fail: block; offending material is scrubbed or rewritten and the finding is logged. Recorded in: progress.md. Pattern-reference mode: ADAPTED — the copy and fingerprint scans compare against the pattern inventory's protected-items list, there being no target copy or code; see the pattern-reference disposition table in the clone-rebuild playbook.
- **G-CL-045 — Full click-through sign-off.** Verifies: CL-083, CL-091. Check (manual): a reviewer clicks through the complete inventoried flow list on the rebuild, comparing each step's state change, validation message, and edge-case behavior against its spec, including at least one invalid-input and one double-submit case per form. Pass: every flow matches its spec or the mismatch is filed as a defect. Fail: block sign-off until mismatches are fixed or the spec is corrected from a new authorized recording. Recorded in: progress.md.

## Anti-patterns

- **Prose impressions.** The behavior record reads "the checkout felt standard, filters worked normally" — impressions that no gate can run and no builder can implement from. Catch it by requiring every flow to exist as an executable test file before it counts as recorded (G-CL-042).
- **Happy-path-only recording.** Every form is recorded with valid data and every flow ends in success, so validation, error, and empty states are discovered for the first time in the rebuild. Catch it by checking each form's spec list for at least one invalid-input recording before sign-off.
- **Spec drift by paraphrase.** Mid-build, specs get "clarified" from memory in chat instead of replayed from the frozen recordings, and the rebuild quietly diverges. Catch it by treating the frozen recording, never a paraphrase, as the only source a spec may be corrected from.
- **Drift denial.** The source site changes mid-engagement, the frozen tests start failing against the source itself, and the team assumes the rebuild is at fault. Catch it by replaying a failing test against the source first; if it fails there too, record drift under CL-088 instead of reworking the rebuild.

## Examples

- [Example 1 — "Verified" from the screenshot](examples/example-1.md) — violates/corrects CL-082, CL-083.
- [Example 2 — The billing flow nobody could see](examples/example-2.md) — violates/corrects CL-085.
- [Example 3 — The borrowed filter widget](examples/example-3.md) — violates/corrects CL-084.

## Recall anchors

- No authorization record, no first click — recording fails closed.
- If it has no executable test, it is not cloned.
- Record what you observed; label what you could not as unobserved.
- Recreate the behavior, never copy the code or the copy.
- The frozen suite judges the rebuild — tests are never edited to pass.

## Checklist

- [ ] The clone-ethics authorization record is committed, covers behavior recording, and predates the first recording (CL-081, G-CL-041).
- [ ] Every inventoried interaction has an executable spec or an `unobserved` record with a reason (CL-082, CL-085, CL-089, G-CL-042).
- [ ] Every spec names trigger, action, observed state change, and network dependency — nothing unobserved is written as fact (CL-083, CL-091).
- [ ] The rebuild's behavior is re-implemented in original code; no target code, deobfuscated or otherwise, is present (CL-084, G-CL-044).
- [ ] Only provisioned test accounts and synthetic data were used; recordings are scrubbed of real personal data (CL-086, CL-087, G-CL-044).
- [ ] The evidence set is frozen at inventory sign-off and any source change since is logged as drift (CL-088).
- [ ] The frozen suite passes against the rebuild unmodified, hashes matching the frozen set (CL-092, G-CL-043).
- [ ] A full manual click-through, including invalid-input and double-submit cases, is signed off against the specs (G-CL-045).
