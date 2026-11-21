# X-Code Detection Parameters — Code

Purpose: detect codebases that were AI-generated without professional review, using concrete, checkable signals in source, tests, and history.
Applies to: any delivered repository, before acceptance, merge, or payment milestones.
How to run: run the automated checks first (lint, type check, test suite, coverage, grep passes), then hand-read the flagged files plus one random module end to end; record every hit by DET-CODE ID.

### DET-CODE-001 — Unreachable code after control transfer
- **Signal:** Statements after `return`, `throw`, `break`, or `continue` in the same block; branches guarded by conditions that are always true or false.
- **AI-typical:** Model appends a "safe" fallback after an early return, leaving a tail of code no path can execute.
- **Professional:** Dead branches are deleted in review; control flow is restructured so every statement is reachable.
- **Check:** ESLint `no-unreachable` and `no-constant-condition`; TypeScript `allowUnreachableCode: false`.
- **False positives:** Deliberate feature-flag stubs — distinguish by a linked ticket and a removal date in the comment.
- **Severity:** major
- **Source:** https://eslint.org/docs/v8.x/rules/
- **Fix:** refactoring, code-generation

### DET-CODE-002 — Unused variables, imports, and functions
- **Signal:** Declared identifiers never referenced; imported modules never called; exported helpers with zero call sites in the repo.
- **AI-typical:** Model imports everything it might need and defines helpers speculatively, then uses only some of them.
- **Professional:** Unused code is removed; tree-shaking and lint gates keep the surface minimal.
- **Check:** ESLint `no-unused-vars`; `tsc --noUnusedLocals`; grep each suspicious export for call sites.
- **False positives:** Public API surface and framework-invoked functions (route handlers, lifecycle hooks) — check framework conventions before flagging.
- **Severity:** minor
- **Source:** https://eslint.org/docs/v8.x/rules/
- **Fix:** refactoring, tech-debt

### DET-CODE-003 — Stub functions presented as complete
- **Signal:** Bodies that `return null`, `return []`, `return true`, throw `NotImplementedError`, or contain only a comment, while callers and UI treat the feature as done.
- **AI-typical:** Model scaffolds every function in the plan, implements the easy half, and stubs the rest without saying so.
- **Professional:** Unfinished work throws loudly, is behind a flag, or is not merged; stubs are labeled and tracked.
- **Check:** Grep for `NotImplemented`, `return null` in non-nullable paths, `pass`/`...` bodies; exercise each endpoint and compare against its contract.
- **False positives:** Legitimate null-object patterns and interface defaults — distinguish by documentation and tests asserting the behavior.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** api-building, frontend-core, code-generation
- **See also:** DET-FAKE-003 (a stubbed signup handler is the code-level cause; FAKE-003 owns the shipped-behavior verdict, CODE-003 the stub itself)
- **See also:** DET-FAKE-010 (a stubbed admin save is the code-level cause; FAKE-010 owns the persistence verdict, CODE-003 the stub itself)
- **See also:** DET-FAKE-015 (a stubbed form handler is the code-level cause; FAKE-015 owns the submit-nowhere verdict, CODE-003 the stub itself)

### DET-CODE-004 — Hallucinated APIs and imports
- **Signal:** Imports of packages absent from the manifest, methods that do not exist on the imported class, or parameters in the wrong order versus the library's docs.
- **AI-typical:** Model invents plausible method names (`client.fetchAllUsers()`) from naming conventions instead of the real API.
- **Professional:** Every call resolves against the installed version; type checking and a build prove it.
- **Check:** Clean install from the lockfile, then full build plus type check; grep flagged calls against the package's shipped type definitions.
- **False positives:** Local wrappers with similar names — resolve the import path before flagging.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** code-generation, refactoring

### DET-CODE-005 — Empty or swallowed exception handlers
- **Signal:** `catch` blocks that are empty, contain only a comment, or log and continue as if the operation succeeded.
- **AI-typical:** Model wraps risky code in try/catch to make errors "go away" rather than handling or propagating them.
- **Professional:** Errors are handled at a boundary, converted to a typed error, or rethrown with context; nothing fails silently.
- **Check:** Grep for empty catch blocks (`catch {}` / `except: pass`); ESLint `no-empty` with catch review; fault-injection test on one critical path.
- **False positives:** Intentional best-effort cleanup (cache eviction, analytics) — distinguish by a comment stating why failure is safe.
- **Severity:** blocker
- **Source:** https://cwe.mitre.org/data/published/cwe_v2.1.pdf (CWE-1069: Empty Exception Block; CWE-390: Detection of Error Condition Without Action)
- **Fix:** error-handling, refactoring

### DET-CODE-006 — Missing error handling on I/O boundaries
- **Signal:** Network, filesystem, and database calls with no timeout, no retry policy, and no failure path; promises without rejection handling.
- **AI-typical:** Happy-path-only code: `await fetch(...)` followed immediately by `.json()` and use of the result.
- **Professional:** Every boundary call defines timeout, failure behavior, and what the user sees when it fails.
- **Check:** Grep for `fetch(`, `axios`, query calls; check each for surrounding error handling; run the app with the network disabled and observe.
- **False positives:** Frameworks with global error interceptors — verify the interceptor actually covers the call before clearing.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** error-handling, api-building

### DET-CODE-007 — Copy-paste duplication across files
- **Signal:** Near-identical function bodies in multiple modules, differing only in names or a literal; the same validation or formatting logic re-implemented per page.
- **AI-typical:** Model regenerates a helper in every file instead of importing the shared one, because each file was produced in isolation.
- **Professional:** Shared logic lives in one module; duplication is extracted on the second or third occurrence.
- **Check:** Run a duplication detector (jscpd or PMD CPD) and hand-review the largest repeated blocks.
- **False positives:** Deliberate duplication in generated code or migrations — check for a generator header before flagging.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, tech-debt

### DET-CODE-008 — Generic or misleading names
- **Signal:** `data`, `result`, `temp`, `handleStuff`, `processData`, `manager2`; names that contradict behavior (`getUser` that also writes).
- **AI-typical:** Model names by syntactic role instead of domain meaning, and renames nothing when behavior grows.
- **Professional:** Names state domain intent; a function does what its name says and nothing more.
- **Check:** Read one module aloud; flag every identifier a new hire could not explain; grep for the generic-name list.
- **False positives:** Short names in tiny, obvious scopes (loop indices, math) — judge by scope size, not the name alone.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, code-generation

### DET-CODE-009 — Magic numbers and unexplained literals
- **Signal:** Bare numeric or string literals in logic (`if (retries > 3)`, `status === 7`, timeout `86400000`) with no named constant or comment.
- **AI-typical:** Model inlines plausible values from examples instead of deriving them from configuration or domain constants.
- **Professional:** Domain values are named constants or config; literals appear only where the value is self-evident.
- **Check:** Grep comparisons and arithmetic against bare numbers outside tests and config files; ask the author to explain three sampled values.
- **False positives:** Mathematical constants and 0/1 sentinels in obvious contexts — check surrounding clarity.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, validation

### DET-CODE-010 — Commented-out code blocks
- **Signal:** Multi-line blocks of syntactically valid code inside comments, often older versions of the function directly above.
- **AI-typical:** Model "preserves" the previous attempt as a comment instead of relying on version control.
- **Professional:** Dead alternatives are deleted; git history is the archive, and the tree reads as one coherent version.
- **Check:** Grep comment blocks containing `;`, `{`, or `return`; count blocks longer than five lines.
- **False positives:** License headers, documentation examples, and regex explanations — distinguish by whether the text parses as the project's own code.
- **Severity:** minor
- **Source:** https://cwe.mitre.org/data/published/cwe_v2.1.pdf (CWE-561: Dead Code)
- **Fix:** refactoring, tech-debt

### DET-CODE-011 — TODO / FIXME litter without tracking
- **Signal:** `TODO`, `FIXME`, `HACK`, `XXX` comments with no ticket reference, owner, or date; TODOs describing core functionality ("TODO: add validation").
- **AI-typical:** Model defers every hard part to a TODO and still reports the task complete.
- **Professional:** TODOs are rare, specific, and linked to a tracked issue; core behavior is never a TODO.
- **Check:** `grep -rn "TODO\|FIXME\|HACK"` excluding `samples/`, `templates/`, `examples/`, `docs/`, and locale paths; classify each remaining hit: tracked-and-minor vs. untracked-or-core.
- **False positives:** A small number of ticket-linked TODOs is normal professional practice — flag density and missing references, not existence. TODOs inside sample, template, example, or scaffold files that prompt the person deploying/configuring to supply a value ("TODO: the domain name this instance will respond to") are instructional text addressed to the operator, not deferred developer work — the class is fill-in prompts in copy-and-edit templates, including files whose header states they are meant to be copied and edited.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** tech-debt, refactoring

### DET-CODE-012 — Fake tests that assert nothing
- **Signal:** Tests with no assertions, assertions on constants (`expect(1).toBe(1)`), tests that mock the unit under test itself, or suites that pass with the implementation deleted.
- **AI-typical:** Model writes tests that mirror the implementation's shape so they pass by construction.
- **Professional:** Tests encode the contract; each fails when the behavior it covers is broken.
- **Check:** Mutation spot-check: break one covered behavior by hand and confirm a test fails; grep tests for assertion calls.
- **False positives:** Smoke tests intentionally assert only "does not throw" — verify they are labeled smoke and few.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** unit-testing, integration-testing

### DET-CODE-013 — No tests on critical paths
- **Signal:** Zero test files, or tests only for trivial utilities while payments, auth, and data mutations have none; coverage tooling absent or unconfigured.
- **AI-typical:** Model delivers features first and, when asked for tests, adds them for the simplest pure functions.
- **Professional:** Risk-weighted coverage: money, auth, and destructive operations are tested first; coverage runs in CI.
- **Check:** List test files against the module map; run coverage and inspect which critical modules report zero.
- **False positives:** Early prototypes and spikes — distinguish by whether the code is presented as production-ready.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** unit-testing, integration-testing

### DET-CODE-014 — Inconsistent patterns for the same job
- **Signal:** Two HTTP clients, two date libraries, mixed `async/await` and callback styles, different error shapes from sibling endpoints.
- **AI-typical:** Each file was generated in a separate session and follows whichever example the model recalled that time.
- **Professional:** One way per job, enforced by shared modules, lint rules, and review.
- **Check:** Grep imports of competing libraries; sample three sibling endpoints and compare structure and error format.
- **False positives:** Documented migration in progress — look for an ADR or migration note naming the target pattern.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, tech-debt

### DET-CODE-015 — Over-engineered abstraction for a single use
- **Signal:** Factory/strategy/plugin layers, generic base classes, or config systems each with exactly one implementation or caller.
- **AI-typical:** Model applies textbook patterns at full scale regardless of need, producing indirection nobody uses.
- **Professional:** Abstraction is introduced at the second real use case; single-use code stays direct.
- **Check:** For each abstract class or interface, count implementations; for each factory, count call sites.
- **False positives:** Seams required by a framework or a published library API — check whether an external consumer justifies the layer.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, tech-debt

### DET-CODE-016 — God functions and runaway complexity
- **Signal:** Single functions spanning hundreds of lines mixing validation, I/O, business rules, and formatting; nesting depth beyond four levels.
- **AI-typical:** Model keeps appending to one function because it never refactors mid-generation.
- **Professional:** Functions do one thing at one level of abstraction; complexity budgets are lint-enforced.
- **Check:** ESLint `complexity` and `max-depth` rules; list the ten longest functions and hand-read the top three.
- **False positives:** Generated parsers and state machines — check for generator headers or a note explaining the shape.
- **Severity:** major
- **Source:** https://eslint.org/docs/v8.x/rules/
- **Fix:** refactoring

### DET-CODE-017 — SQL injection surface
- **Signal:** Query strings built by concatenation or template interpolation of request values (`"... WHERE id = " + id`, `` `SELECT ... ${req.params}` ``).
- **AI-typical:** Model writes the shortest working query, interpolating variables directly.
- **Professional:** Parameterized queries or an ORM's bound parameters everywhere; raw SQL is reviewed and allow-listed.
- **Check:** Grep for string concatenation inside query calls; run a SAST scan (Semgrep `sql-injection` rules); probe one endpoint with a quote payload.
- **False positives:** Interpolation of server-side constants only (table names from an allow-list) — trace each interpolated value to its source.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** api-building, validation

### DET-CODE-018 — Hardcoded secrets and credentials
- **Signal:** API keys, passwords, tokens, or connection strings as literals in source, tests, or committed config; `.env` files in the repo.
- **AI-typical:** Model pastes the example key from documentation or the user's prompt straight into code.
- **Professional:** Secrets come from environment or a secret manager; repos carry only `.env.example` with dummy values.
- **Check:** Run gitleaks or trufflehog over the tree and history; grep for `key`, `secret`, `password` assignments to string literals. Before assigning severity to any hit, verify the file's role — hits in sample/template/example configuration are classified under False positives first; a scanner hit alone is not a recorded blocker.
- **False positives:** Obvious placeholders (`"YOUR_API_KEY"`) and test fixtures with fake credentials — confirm the value cannot authenticate anywhere. Sample/template configuration files (paths under `samples/`, `templates/`, `examples/`, `*.sample.*` names, or files headed "copy and edit") containing obviously non-functional example credentials — dictionary-fake values such as `pa$$word` or `changeme`, especially paired with reserved example hosts (`example.com`) — are placeholders of the same class: a blank in a form the operator fills in, not a leaked secret.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** validation, refactoring
- **See also:** DET-INF-005 (secrets committed to version control, including .env files in the repo, are INF-005's scope — for .env in the repo, see DET-INF-005; CODE-018 covers secret literals in source and tests)
- **See also:** DET-INF-006 (secrets reachable in shipped client bundles are INF-006's scope; CODE-018 covers literals at rest in source)

### DET-CODE-019 — Missing input validation at boundaries
- **Signal:** Request bodies, query params, and file uploads used directly — stored, queried, or rendered — with no schema, type, range, or size checks.
- **AI-typical:** Model trusts the client because the demo client always sends well-formed data.
- **Professional:** Every boundary validates against a schema; invalid input gets a structured 4xx, never a crash or a silent write.
- **Check:** Pick three endpoints; send missing, wrong-typed, and oversized fields; confirm rejection and error shape.
- **False positives:** Internal-only endpoints behind another validated service — verify the upstream validation actually exists.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** validation, api-building
- **See also:** DET-UX-004 (same missing validation from the form side: UX-004 owns the field-level behavior the user hits; CODE-019 owns the boundary/schema verdict)

### DET-CODE-020 — Disabled security controls and unsafe defaults
- **Signal:** `verify=False`, CORS `*` with credentials, `eslint-disable` / `@ts-ignore` clusters on security-relevant lines, TLS checks turned off, debug mode on in production config.
- **AI-typical:** Model disables whatever blocked the demo until it ran, and never re-enables it.
- **Professional:** Controls are on by default; any exception is scoped, commented, and tracked.
- **Check:** Grep for `verify=False`, `rejectUnauthorized: false`, `Access-Control-Allow-Origin: *`, suppression comments; review production config.
- **False positives:** Local-development config files — confirm the flagged setting cannot reach the production environment.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** validation, error-handling, refactoring
- **See also:** DET-INF-021 (INF-021 owns the production-reachable debug/admin surface; CODE-020 owns the disabled control or unsafe default in code and config)

### DET-CODE-021 — Comments that narrate instead of explain
- **Signal:** Comments restating the next line (`// increment i`, `// return the result`) on most functions, with docblocks generated for trivial getters.
- **AI-typical:** Model pads every function with a summary comment to look documented.
- **Professional:** Comments explain why and warn about non-obvious constraints; self-evident code carries none.
- **Check:** Sample twenty comments; count how many add information the code does not already state.
- **False positives:** Public API documentation and generated docs sites — judge the internal code, not the published API surface.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, code-generation

### DET-CODE-022 — Identical error messages for different failures
- **Signal:** Every catch returns `"Something went wrong"` or the same generic 500 body, with no error codes, logging of cause, or distinction between client and server faults.
- **AI-typical:** Model wires one global fallback message and reuses it at every layer.
- **Professional:** Errors are typed and coded; clients can act on them; logs carry the underlying cause with a correlation ID.
- **Check:** Trigger three distinct failures (bad input, missing record, downstream outage) and compare responses and logs.
- **False positives:** A uniform public message paired with detailed internal codes is good practice — check for the codes before flagging.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** error-handling, api-building
- **See also:** DET-UX-006 (UX-006 owns the wording the user reads; CODE-022 owns the code shape — one generic error for every failure, no codes or causes)

### DET-CODE-023 — Promises and async work dropped
- **Signal:** Async calls without `await` or `.catch`, fire-and-forget writes whose failure is invisible, `async` functions whose errors surface as unhandled rejections.
- **AI-typical:** Model writes sequential-looking code over async APIs and never traces the rejection path.
- **Professional:** Every promise is awaited, returned, or explicitly detached with error handling and a comment.
- **Check:** ESLint `@typescript-eslint/no-floating-promises` or `require-await` review; run with unhandled-rejection warnings as errors.
- **False positives:** Intentional background jobs — distinguish by the presence of a queue or an explicit detached-with-handler pattern.
- **Severity:** major
- **Source:** https://eslint.org/docs/v8.x/rules/
- **Fix:** error-handling, refactoring

### DET-CODE-024 — Copy of a tutorial or boilerplate left unadapted
- **Signal:** Example domain names (`example.com`), sample entities ("John Doe", "Acme"), leftover demo routes, and default scaffold README text inside a supposedly custom product.
- **AI-typical:** Model starts from a memorized tutorial and renames only the parts the prompt mentioned.
- **Professional:** Scaffolds are pruned; every string, route, and fixture belongs to the actual product.
- **Check:** Grep for `example.com`, `lorem`, `John Doe`, `Acme`, `foo`, `bar` outside test fixtures, documentation, and locale files; list routes and match them to the product spec. Flag `example.com` and sample entities only in executable config, routes, seeds, or defaults that would run in production.
- **False positives:** Test fixtures legitimately use sample data — flag only occurrences reachable in production paths. Locale files, documentation, and user-facing help/example text are production paths that legitimately use sample values: the reserved documentation domains (`example.com`, `example.org`) and reserved IPs exist precisely so help text is correct for every deployment. The class is deliberate examples in text addressed to the reader — distinguish from leftover scaffold by whether the string instructs the reader or configures the system.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, frontend-core, tech-debt
- **See also:** DET-CON-002 (template and CMS default copy shipped as page content is CON-002's scope; CODE-024 covers boilerplate left in code, routes, and fixtures)
- **See also:** DET-CON-005 (placeholder contact details in live contact blocks are CON-005's scope; CODE-024 covers sample entities left in code)

### DET-CODE-025 — Type escapes in typed codebases
- **Signal:** Dense `any`, `as unknown as X`, `@ts-ignore`, or untyped JS files inside a TypeScript project, concentrated exactly where logic is complex.
- **AI-typical:** Model silences the compiler instead of modeling the data, so the hardest code has the weakest types.
- **Professional:** `any` is rare and justified; boundary data is parsed into real types.
- **Check:** `grep -rn ": any\|@ts-ignore\|as unknown"` and map density against module criticality; `tsc --strict` pass.
- **False positives:** Third-party type gaps with a tracked upstream issue — look for a comment linking the issue.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, validation

### DET-CODE-026 — No null or empty-state handling in UI code
- **Signal:** Components render data fields directly with no loading, empty, or error states; lists assume non-empty arrays; optional fields dereferenced unguarded.
- **AI-typical:** Model builds the populated happy-path screen from the mock and stops.
- **Professional:** Every data-driven view defines loading, empty, error, and populated states explicitly.
- **Check:** Run the UI against an empty database and a failing API; grep components for conditional state rendering.
- **False positives:** Static marketing pages with no dynamic data — confirm the component actually consumes data.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** frontend-core, error-handling
- **See also:** DET-VIS-032 (VIS-032 rates the rendered state set; CODE-026 owns the code-level absence of state handling)
- **See also:** DET-UX-008 (UX-008 owns the loading-state behavior verdict; CODE-026 covers all missing states in code)
- **See also:** DET-UX-009 (UX-009 owns the empty-state behavior verdict; CODE-026 covers all missing states in code)
- **See also:** DET-UX-010 (UX-010 owns the failed-load behavior verdict; CODE-026 covers all missing states in code)

### DET-CODE-027 — Business rules duplicated between client and server
- **Signal:** The same pricing, eligibility, or permission logic implemented in frontend and backend with subtly different constants or conditions.
- **AI-typical:** Model generates each layer independently, re-deriving rules from the prompt each time.
- **Professional:** The server is authoritative; the client mirrors only for UX, from a shared definition or generated types.
- **Check:** Pick two core rules; locate every implementation; diff constants and boundary conditions.
- **False positives:** Deliberate UX pre-validation that defers to the server — distinguish by whether the client copy can ever be the deciding one.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** refactoring, api-building, validation

### DET-CODE-028 — Dependency manifest incoherence
- **Signal:** Packages in the manifest never imported, imported packages missing from the manifest, duplicate libraries for one job, or wildcard `*` / `latest` version ranges.
- **AI-typical:** Model edits the manifest from memory across sessions, adding and never pruning.
- **Professional:** Manifest is minimal and pinned by lockfile; every entry is imported; removals are cleaned up.
- **Check:** Run depcheck (or equivalent); diff import list against manifest; inspect version ranges.
- **False positives:** Build-time and plugin packages depcheck cannot see — verify against build config before flagging.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** tech-debt, refactoring

### DET-CODE-029 — Debug output and dead instrumentation shipped
- **Signal:** `console.log` / `print` debugging in production paths, commented breakpoints, verbose request logging including bodies with personal data.
- **AI-typical:** Model debugs by printing during generation and never removes the prints.
- **Professional:** Logging goes through a logger with levels; debug prints are removed before merge; sensitive fields are redacted.
- **Check:** ESLint `no-console` (or project equivalent); grep print statements outside the logging module; inspect log configuration.
- **False positives:** Structured logs at debug level behind configuration — check the level and the default before flagging.
- **Severity:** minor
- **Source:** https://eslint.org/docs/v8.x/rules/
- **Fix:** refactoring, error-handling

### DET-CODE-030 — Race-prone check-then-act sequences
- **Signal:** "Check if exists, then insert" without a unique constraint or transaction; balance read-modify-write without locking; duplicate-submit handling absent on writes.
- **AI-typical:** Model writes the logically sequential version and never considers concurrent requests.
- **Professional:** Invariants live in the database (unique constraints, transactions, atomic updates); handlers are idempotent where retries occur.
- **Check:** Read every create/update path for a uniqueness or balance invariant; verify a matching constraint or transaction exists in the schema.
- **False positives:** Genuinely single-writer internal tools — confirm the deployment really has one writer.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** api-building, validation
- **See also:** DET-UX-024 (UX-024 owns the user-facing duplicate submission via an unlocked control; CODE-030 owns the missing server-side invariant)

### DET-CODE-031 — Version-control history with no review trail
- **Signal:** One giant initial commit containing the whole product, commit messages like "update" or "final version", no branches or pull requests in a multi-week project.
- **AI-typical:** Code was generated in bulk and uploaded once, rather than built in reviewed increments.
- **Professional:** History shows incremental, described commits; merges carry review discussion.
- **Check:** `git log --oneline` and `git log --stat` on the first commits; compare commit count and message quality against project duration.
- **False positives:** A client-supplied zip import or a migrated repository — ask for the original history before concluding.
- **Severity:** minor
- **Source:** Derived: PROJECT_ANATOMY.md Part 11
- **Fix:** tech-debt

### DET-CODE-032 — Configuration drift and copy-pasted config
- **Signal:** The same settings block duplicated across services with diverging values; environment-specific values hardcoded per file instead of one config source.
- **AI-typical:** Model duplicates a working config file for each new service and edits only the obvious fields.
- **Professional:** One config source per environment; shared values are referenced, not copied; drift is detectable by diff.
- **Check:** Diff config files across services; grep for the same hostnames, limits, and feature flags appearing in multiple files with different values.
- **False positives:** Intentionally divergent per-service limits — distinguish by a comment or config documentation naming the difference.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** tech-debt, refactoring
- **See also:** DET-INF-007 (INF-007 owns config hardcoded or hand-edited per machine at deploy time; CODE-032 owns duplication and drift across services in the codebase)

### DET-CODE-033 — Unbounded operations
- **Signal:** List endpoints returning whole tables with no pagination or limit, loops over unbounded query results, file reads loading entire contents into memory, regexes on untrusted input.
- **AI-typical:** Model writes the version that works on the ten-row demo dataset.
- **Professional:** Every collection access is bounded (pagination, limits, streaming); bounds are part of the API contract.
- **Check:** Grep list handlers for `limit`/`page` handling; load-test one endpoint against a large seeded dataset and watch memory and latency.
- **False positives:** Admin exports and reports designed to be complete — distinguish by streaming or async-job design instead of in-request loading.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md Part 2/11
- **Fix:** api-building, validation
