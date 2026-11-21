# DET-FAKE — Fake-Functionality Detection Parameters (X-Fake)

Purpose: catch features that look real but are simulated — the core evidence base for QB-10, the Real Content Rule. A feature is fake when the UI claims an effect the system never performs: no server state changes, no provider is called, no record persists. An explicitly labeled demo or sandbox is honest and is never flagged; undisclosed simulation of a core function is always a blocker.

## How to run the check

Run two tests before anything else. **Persistence test:** perform the action, reload the page, sign out and back in, and open the app in a second browser or account — the claimed effect must still be there and must be yours. **Network test:** repeat the action with the browser network tab open — a real write produces a server request and a changed response on the next read; a fake one fires no request, or fires one whose response the UI ignores. Then apply the parameters below.

### DET-FAKE-001 — Any-password login
- **Signal:** The login form and what it accepts: try a deliberately wrong password, then a random string.
- **AI-typical:** The form accepts any input, or one hardcoded credential, and "signs in" entirely in client state.
- **Professional:** Credentials are verified server-side against hashed passwords; wrong passwords are rejected with a generic error.
- **Check:** Wrong-password test, then reload test: after a real login a server-issued session survives reload; after logout it does not.
- **False positives:** A labeled demo account with published credentials is legitimate; distinguish by the label and by the session behaving like a real one.
- **Severity:** blocker
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- **Fix:** backend-auth

### DET-FAKE-002 — Session that is only a flag
- **Signal:** Post-login state stored as a `localStorage` boolean or in-memory variable rather than a session cookie or token.
- **AI-typical:** `isLoggedIn = true` in the client; editing storage manually grants "access," and protected data was shipped to the browser anyway.
- **Professional:** The server issues an opaque, high-entropy session ID in a Secure, HttpOnly cookie and enforces authorization on every request.
- **Check:** Clear cookies but keep local storage, then request a protected page or API route directly — the server must refuse.
- **False positives:** A client-side route guard is fine as UX, provided the API also enforces auth; check the API, not the guard.
- **Severity:** blocker
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- **Fix:** backend-auth

### DET-FAKE-003 — Signup that registers nothing
- **Signal:** The registration flow: it shows a success screen, but no account record is created.
- **AI-typical:** Signup validates format, shows "Account created," and discards the data or stores it only in the browser.
- **Professional:** The account is written to the user store, the password hashed, and verification email sent where promised.
- **Check:** Register, sign out, sign in with the new credentials from a private window; also try registering the same email twice — a real store rejects the duplicate.
- **False positives:** Email-verification-pending states legitimately delay first login; the pending record still exists and the duplicate check still fires.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** backend-auth, data-access
- **See also:** DET-CODE-003 (stub functions are the usual code-level cause; CODE-003 covers the stub, FAKE-003 the behavior the user experiences)

### DET-FAKE-004 — Dashboard with frozen numbers
- **Signal:** Revenue, user, and activity figures on dashboards and admin panels, watched across time and actions.
- **AI-typical:** Round, plausible constants rendered from a fixture; performing real transactions never moves them.
- **Professional:** Every figure is computed from live records, so it changes when the underlying data changes.
- **Check:** Data-change test: create or delete a record the metric should count, reload, and confirm the number moves by exactly that amount.
- **False positives:** Cached or periodically aggregated metrics lag legitimately; distinguish by forcing a known change and waiting one stated refresh cycle.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** data-access, api-building

### DET-FAKE-005 — Counters that reset on reload
- **Signal:** Like, view, follower, and cart counters before and after a hard reload and a second visit.
- **AI-typical:** The counter increments in component state, then resets to its hardcoded base value on reload.
- **Professional:** The count is read from the server on load and each action writes through the API.
- **Check:** Increment once, hard-reload, and compare; repeat from a second account and confirm both clients converge on the same total.
- **False positives:** Optimistic UI updates are legitimate when the server value replaces them after the request resolves; a reset to the original base is not.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, data-access

### DET-FAKE-006 — Checkout that charges nothing but confirms an order
- **Signal:** The payment step and the confirmation that follows it: order ID, receipt, and provider reference.
- **AI-typical:** The form accepts any card-shaped input, shows "Payment successful," and no payment provider is ever contacted.
- **Professional:** A provider (e.g., Stripe) creates and confirms a payment intent server-side; the order records the provider's payment ID, and failures decline visibly.
- **Check:** Network test during checkout for a provider call; then verify the payment exists in the provider dashboard and that a known decline card actually declines.
- **False positives:** A sandbox/test-mode integration charges nothing by design; distinguish by the visible test-mode labeling and test keys, which must never ship to production unlabeled.
- **Severity:** blocker
- **Source:** https://docs.stripe.com/testing
- **Fix:** payments

### DET-FAKE-007 — Card validation that accepts everything
- **Signal:** The card fields: submit an expired date, a failing checksum number, and a nonsense CVC.
- **AI-typical:** Any 16 digits pass; there is no Luhn check, no brand detection, and no decline path at all.
- **Professional:** Client validation catches format errors, and the provider's response decides approval; declines surface as errors, not successes.
- **Check:** Use the provider's documented decline test card — a real integration declines it; a simulated one thanks you for your purchase.
- **False positives:** None for the decline path: a checkout with no possible decline is simulated by definition.
- **Severity:** blocker
- **Source:** https://docs.stripe.com/testing
- **Fix:** payments

### DET-FAKE-008 — Search with canned results
- **Signal:** Search behavior across unrelated and nonsense queries.
- **AI-typical:** Every query returns the same fixture list, or results are filtered client-side from a small hardcoded array presented as the catalog.
- **Professional:** Queries reach a server index over the real dataset; result counts and contents vary with the query and the data.
- **Check:** Search for a term that exists only in a record you just created, and for a gibberish string — the first must find it, the second must return an honest empty state.
- **False positives:** Small datasets legitimately return few results; the distinguisher is whether a newly added record becomes findable without a redeploy.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, data-access

### DET-FAKE-009 — "AI" feature with canned responses
- **Signal:** Chatbots, generators, summarizers, and recommenders: probe with unusual, specific, and contradictory inputs.
- **AI-typical:** Responses come from a lookup of canned strings, a rotation of generic templates, or an echo of the prompt; identical inputs in different words get identical answers.
- **Professional:** Requests go to a real model or a real retrieval pipeline, and outputs vary with input in ways templates cannot; where a rules-based fallback exists, it is disclosed.
- **Check:** Network test for a model/API call; then ask a question only answerable from a document you supplied — canned systems fail or hallucinate the fixture answer.
- **False positives:** Cached answers to identical repeated questions are legitimate; vary the wording — a real system still answers the new phrasing.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, real-content

### DET-FAKE-010 — Admin panel that saves nothing
- **Signal:** Admin edits: change a price, a title, or a user's status, then leave and return.
- **AI-typical:** The form shows a "Saved" toast, state updates locally, and the change is gone on reload or invisible to regular users.
- **Professional:** Edits issue authenticated write requests, persist server-side, and propagate to every surface that displays the entity.
- **Check:** Change a value as admin, reload the admin page, then view the public page as an anonymous visitor — all three must agree.
- **False positives:** Draft-versus-published workflows legitimately delay public visibility; a draft state must be visible as a draft in the admin UI.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, data-access
- **See also:** DET-CODE-003 (stub functions are the usual code-level cause; CODE-003 covers the stub, FAKE-010 the persistence behavior)

### DET-FAKE-011 — Delete that only hides
- **Signal:** Delete and archive actions on records, posts, and accounts.
- **AI-typical:** The item disappears from the list because it is filtered out client-side; it reappears on reload, in search, or via its direct URL.
- **Professional:** Deletion (or a clearly labeled soft-delete) happens server-side, and the record is unreachable through every surface.
- **Check:** Delete, reload, open the item's direct URL, and search for its unique text — all must fail to surface it.
- **False positives:** Soft-delete with a visible "Archived" or trash state is honest; hiding without any such state is not.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** data-access, api-building

### DET-FAKE-012 — Upload button that discards the file
- **Signal:** File and avatar uploads: the progress bar, the preview, and what survives a reload.
- **AI-typical:** The file is read into a local object URL for preview and never sent; after reload the placeholder returns.
- **Professional:** The file is uploaded to storage, a durable URL or file ID is saved on the record, and the asset is served back from the server.
- **Check:** Upload a uniquely named file, reload, then open the asset URL in a private window — it must resolve from server storage, not a `blob:` URL.
- **False positives:** Client-side previews before upload are normal; the violation is a completed "Upload successful" state with no server copy.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, data-access

### DET-FAKE-013 — Staged notifications
- **Signal:** Bell icons, badges, and notification feeds, correlated against events that should trigger them.
- **AI-typical:** A fixed list of notifications ("John liked your post") renders for every account, including brand-new ones, and never responds to real events.
- **Professional:** Notifications are generated by real events, stored per user, and read state persists.
- **Check:** Create a fresh account — it must start with an empty feed; trigger a known event from a second account and confirm a new, matching notification arrives and stays read after reload.
- **False positives:** A labeled welcome or onboarding message is legitimate; a feed of other users' fabricated activity is not.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, seed-data

### DET-FAKE-014 — Seed data shipped as real users
- **Signal:** User lists, testimonials, reviews, and activity feeds in a freshly launched product.
- **AI-typical:** Invented people with stock-photo avatars and scripted praise are presented as customers; seed accounts can be "found" in search and messaging.
- **Professional:** Demo and seed data live in development fixtures, are wiped or clearly excluded before launch, and social proof comes only from real, attributable users.
- **Check:** Inspect a fresh production database or sign up and search for the showcased users; cross-check testimonial names against any verifiable source.
- **False positives:** Clearly labeled sample content in a demo environment is fine; the same content presented as real customers in production is the violation.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** seed-data, real-content
- **See also:** DET-VIS-023 (imagery mismatch on the page is VIS-023's tell; FAKE-014 owns the shipped seed data itself)
- **See also:** DET-VIS-027 (avatar presentation is VIS-027's tell; FAKE-014 owns seed accounts presented as real users)
- **See also:** DET-CON-010 (fabricated testimonial quotes are CON-010's verdict; FAKE-014 covers the seed people behind them)
- **See also:** DET-CON-013 (fake review patterns are CON-013's verdict; FAKE-014 covers seed data shipped as real users)
- **See also:** DET-CON-019 (stock photos captioned as the team are CON-019's verdict; FAKE-014 covers seed data presented as real customers)

### DET-FAKE-015 — Forms that submit nowhere
- **Signal:** Contact, newsletter, application, and feedback forms and their success messages.
- **AI-typical:** Submit shows "Message sent" or "Subscribed" while the network tab shows no request, or a request whose payload is discarded.
- **Professional:** Submissions persist to a database, CRM, or email provider, and an owner can retrieve them; failures surface as errors.
- **Check:** Submit a unique marker string, then verify it in the receiving system or admin view; repeat with the network blocked — an honest form reports failure.
- **False positives:** Third-party form endpoints (provider-hosted) still count as real if submissions are retrievable by the owner in that provider.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, placeholder-scan
- **See also:** DET-UX-003 (same defect: FAKE-015 owns the verdict via the persistence/network test; UX-003 covers the user-facing symptom and flow context)
- **See also:** DET-CODE-003 (stub handlers are the code-level cause of submit-nowhere forms; CODE-003 covers the stub, FAKE-015 the shipped behavior)

### DET-FAKE-016 — Profile edits that don't stick
- **Signal:** Settings and profile pages: name, email, preferences, and password changes.
- **AI-typical:** Fields update in local state and toast "Profile updated," but revert on reload or differ between devices.
- **Professional:** Changes write to the user record server-side, sensitive changes re-authenticate, and every session reads the same values.
- **Check:** Change a display name, reload, then sign in from a second browser — the new value must appear in both places.
- **False positives:** Pending-verification states for a new email are legitimate if labeled; the old value must be shown as current until verification completes.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** backend-auth, data-access

### DET-FAKE-017 — Filters and sorting that only rearrange a fixture
- **Signal:** Filter, sort, and pagination controls over lists presented as large or live datasets.
- **AI-typical:** Controls reorder the same small hardcoded set; page 2 repeats page 1, and filter counts never match the results shown.
- **Professional:** Filtering and pagination are executed against the real dataset, with counts derived from the same query as the results.
- **Check:** Apply a filter matching a record you created, then one matching nothing; check that counts, pages, and results stay mutually consistent.
- **False positives:** Client-side filtering of a genuinely small, fully loaded dataset is legitimate — when the UI does not claim a larger dataset than it holds.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** data-access, api-building

### DET-FAKE-018 — Live indicators that are timers
- **Signal:** "Live" viewers, online users, typing indicators, live sales popups, and real-time charts.
- **AI-typical:** Numbers drift on a random timer, popups cycle through a script of invented buyers, and charts animate without any data source.
- **Professional:** Live figures come from a real presence, analytics, or event stream, and social-proof popups fire only on real, recent events.
- **Check:** Open the page in two browsers and compare values; go idle and watch for scripted repetition; check the network tab for a socket or polling source.
- **False positives:** Aggregated or delayed analytics labeled "last 24 hours" are honest; the violation is the word "live" over a random number generator.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** real-content, placeholder-scan

### DET-FAKE-019 — Export and download buttons that fabricate the file
- **Signal:** "Download report," "Export CSV," and invoice or receipt downloads.
- **AI-typical:** The button generates a static sample file, a screenshot-like PDF, or a document whose contents ignore the current filters and data.
- **Professional:** The file is generated from the actual records in view, including changes made seconds earlier.
- **Check:** Create a record with a unique marker, export immediately, and confirm the marker is in the file; edit the record and export again.
- **False positives:** A clearly labeled sample template download is legitimate; a sample delivered as "your report" is not.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, data-access

### DET-FAKE-020 — Password reset that resets nothing
- **Signal:** The forgot-password flow: the email promise, the link or code, and whether the credential actually changes.
- **AI-typical:** The form always shows "Reset link sent," no email exists, or the "reset" accepts any code and the old password keeps working.
- **Professional:** A single-use, expiring token is emailed; using it changes the stored credential and invalidates the old password and other sessions.
- **Check:** Request a reset, complete it with a new password, then confirm the old password fails and the new one works from a private window.
- **False positives:** Enumeration-safe messaging ("if an account exists…") is correct practice; it is honest because the email genuinely arrives for real accounts.
- **Severity:** blocker
- **Source:** https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- **Fix:** backend-auth

### DET-FAKE-021 — Roles and permissions that are cosmetic
- **Signal:** Admin, moderator, and member distinctions, especially where the UI hides controls by role.
- **AI-typical:** Non-admins lose the buttons but keep the ability to call the underlying endpoints directly; "permission denied" exists only as a hidden CSS class.
- **Professional:** Every privileged action is authorized server-side per request, independent of what the UI renders.
- **Check:** As a low-privilege account, replay a privileged request captured from an admin session — the server must reject it.
- **False positives:** Hiding irrelevant UI by role is good UX; it becomes a violation only when it is the sole enforcement.
- **Severity:** blocker
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** backend-auth, api-building

### DET-FAKE-022 — Progress and sync states that lie
- **Signal:** Sync icons, "Saved" indicators, progress bars, and offline queues.
- **AI-typical:** The UI shows "All changes saved" on a timer while edits live only in memory; closing the tab loses work the app claimed to have stored.
- **Professional:** Saved indicators reflect acknowledged server responses, and failures switch the indicator to an error or retry state.
- **Check:** Make an edit, confirm "Saved," immediately kill the tab and reopen; then repeat an edit with the network disabled — the indicator must not claim success.
- **False positives:** Autosave with a visible pending state during the request is legitimate; claiming completion before the response is the violation.
- **Severity:** major
- **Source:** Derived: PROJECT_ANATOMY.md + QB-10 Real Content Rule
- **Fix:** api-building, data-access
