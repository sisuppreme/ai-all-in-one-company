# UI/UX Upscaler — Spec 09: Architecture Leak

> Companion spec to `skills/frontend/ui-ux-upscaler/SKILL.md`. THE TOP-PRIORITY spec.
> Origin: MUHIUM's test, 2026-11-23 — the generated UI/UX exposed which DB the app
> uses, how many pages it has, the architecture, everything. The standing rule from
> skill-building time was that an app's structure/architecture must NEVER leak into
> UI/UX; the test FAILED it. This file is the fix, ordered 2026-11-24 ~08:05 PKT.
> **SCOPE: web apps ONLY** (native: the leak rule applies unchanged — §3.5 — but
> native specs themselves are an adaptation note only, `02-theme-decision.md` §8).

## 1. The principle

The UI agent USES all of the app's skills to understand the app — architecture,
backend, database, API, integrations, everything — but surfaces NONE of their
internals in the UI. Understanding is inward; the UI is outward. The two directions
never mix.

- **Use (inward):** read the architecture skill to know the data model; read the
  backend skill to know what the API can do; read the database skill to know what is
  stored and how it relates; read the API skill to know the endpoints. This knowledge
  makes the UI correct: the right fields, the right flows, the right states, the right
  error handling.
- **Surface (outward):** only user-facing concepts — what the user sees, does, owns,
  and pays for, in the user's own words. The UI names books, bookings, readings,
  invoices, guests, nights, gigabytes — never tables, endpoints, modules, or stacks.
- **The test:** show any UI surface to a non-technical user of the product. If they
  need to know how the app is built to understand it, it leaks. If a sentence would
  still make sense after replacing the entire stack (Postgres→SQLite, REST→GraphQL,
  React→Vue), it does not leak. If replacing the stack would make the sentence false
  or meaningless, it leaks — rewrite it.
- **The veto:** any leak is a gate FAIL veto regardless of the /80 score
  (design-intelligence §5 pass rule + `01-audit-and-scoring.md` §5 + `11-scoring-shipping.md`
  §1). A 72/80 app with 1 leak does not ship. Leak score target is 0, always.

## 2. The hard ban list (with a rationale per item)

| # | Banned from ALL user-facing surfaces | Rationale — why it harms the user (not just "it's untidy") |
|---|---|---|
| B-1 | DB names / types ("PostgreSQL", "MongoDB", "SQLite", "MySQL", versions) | The user cannot act on it. It answers a question nobody asked ("what stores my
  data?") while raising one they cannot answer ("is Postgres safe?"). It also tells an
  attacker the stack. Trust comes from what the product does with data, not from naming the engine. |
| B-2 | Table / collection names ("`bookings`", "`users`", "`field_readings`", "rows", "records", "documents" as a storage term) | "Rows" and "records" are the system's units, not the user's. The user has bookings,
  books, readings — counting rows tells them the system counted something, not what they own. |
| B-3 | Page / route counts or structures ("12 pages", "4 modules", "3 sections in the admin", sitemap-style counts) | The user navigates by job, not by inventory. A count of pages tells them the app is
  large, not whether it does their job — and it goes stale the moment a route is added. |
| B-4 | API endpoints ("/v2/bookings", "/api/users/42", any URL path naming a resource operation, query strings naming fields) | An endpoint is an instruction to a machine, not information for a person. Shown to a
  user it is noise; copied by a user into a support ticket it is a security exposure. |
| B-5 | Internal module / service names ("Billing Service", "Auth Module", "Sync Worker", "CRM", team/service ownership labels) | The user has one product, not a service diagram. Module names make the user do the
  work of mapping the org chart onto their problem ("which service do I complain to?"). |
| B-6 | Tech-stack labels ("React", "Next.js", "Node", "AWS", "Stripe" as a stack label — see §7 for the payment-provider exception, "Powered by X" badges that name infrastructure) | Stack labels are the builder's résumé, not the user's information. They invite the
  user to judge the product by its tools instead of its behaviour — and they date the
  product the moment the stack changes. |
| B-7 | Schema / field names ("`users.email`", "`bookings.guest_id`", "`customer_id`", camelCase/snake_case identifiers, constraint names, "NOT NULL", "FK violation", "unique constraint") | A field name is an address inside the machine. In an error message it blames the
  user in a language they don't speak ("your `guest_id` is invalid" — the user has no
  `guest_id`; they have a guest). In a label it replaces a human noun with a variable. |
| B-8 | Status codes / technical error identifiers ("404", "422", "500", "ERR_CONNECTION", trace IDs, "Error: Cannot read properties of undefined") | A code is a diagnosis for the developer, not a message for the user. The user needs
  what happened + what to do. The code goes to the log and the support reference (a
  user-facing reference code like "ABC-123" is allowed — §7 — because it is opaque: it
  names nothing about the stack). |

**Scope of "user-facing surfaces":** every pixel the user can see or hear — copy,
labels, headings, placeholders, helper text, tooltips, aria-labels, `title` attributes,
error/empty/loading strings, URLs shown in the UI, page titles, notification text,
email subjects the app sends, PDF/invoice text, and anything rendered by an error
boundary or a third-party default. If it renders in the browser, it is user-facing.
"Only developers will see it" is not a defence — the test is rendering, not intent
(see §3.5 for dev-tools-visible labels and error boundaries).

## 3. Leak taxonomy — where leaks hide

### 3.1 UI copy

Headings, subheadings, body copy, marketing claims ("Built on PostgreSQL for
reliability"), feature lists ("12 pages of reports"), and footers. Hunt: read every
heading aloud; any heading that names a technology or a count of app parts is a leak.

### 3.2 Empty states

The most common hiding place: an empty table/list that says "No rows in `bookings`" or
"No records found". The empty state is written by the developer who built the list,
and they name the thing they queried. Fix per `04-component-upgrades.md` §15 (L-C4):
what is empty (user concept) + why + the next action.

### 3.3 Error messages

The second most common hiding place: raw or lightly wrapped backend errors surfaced
verbatim ("422: `users.email` unique constraint", "Failed to fetch /v2/invoices",
"ECONNREFUSED postgres:5432"). Hunt: trigger every error path (see §4.3) and read the
resulting string. Any string containing a B-1–B-8 item is a leak — rewrite per §6.

### 3.4 Admin screens

Settings, admin panels, billing, and "system" screens are where teams feel licensed to
show stack terms ("Connected database: PostgreSQL 15", "API version: v2", "Storage
engine: …"). They are not licensed: an admin is a user (`04` §13, L-C7). Technical
detail an admin genuinely needs is expressed in user concepts — see §7.

### 3.5 Dev-tools-visible labels

Error boundaries that render `error.message`; React/Vue dev overlays; default 404/500
pages from the framework; `console` text that is also rendered (e.g. a debug banner
left enabled in production); component/display names that surface via error boundaries
(`PostgresTable failed to render`); `title` attributes and aria-labels copied from
field names. Hunt: trigger an error boundary on every route family; open the app with
dev tools closed and read what actually renders. Anything naming the stack that renders
— even in a corner, even "temporarily" — is a leak. (Console-only output that never
renders is not a UI leak; it is still removed before ship by the regression checklist,
`10-regression-rollback.md` §2, because a console error a user is asked to paste into
a support ticket becomes a leak the moment they paste it.)

### 3.6 Loading text

"Fetching /v2/bookings…", "Loading table `invoices`…", "Syncing Postgres…". Loading
text is written by the developer who wrote the fetch call, and it names the call.
Fix per L-C6: "Loading your bookings…".

### 3.7 URLs shown to users

Share links, breadcrumbs, "view" links, and redirect notices that display an internal
API URL or a query string naming fields (`?user_id=42&table=bookings`). The displayed
URL is the user-facing path only. (The browser address bar's own URL is the app's
routing — that is not a leak by itself; a route path that names a module
(`/admin/postgres-tables`) is.)

## 4. Detection method — how to hunt leaks in a real app

### 4.1 Copy scan (1–2 hours)

1. Extract every user-facing string: grep the codebase for string literals in JSX/
   templates/components + i18n files + error definitions. (For React: grep string
   literals in `src/`; for Vue: templates + i18n; for plain HTML: the HTML files.)
2. Run the ban-list grep over the extracted strings: `Postgres|Mongo|SQLite|MySQL|
   /v2?/|/api/|table|rows?|records?|module|service|React|Next\.js|Node|AWS|_id|
   404|422|500|NOT NULL|constraint|endpoint|schema` — tune the pattern to the app's
   actual stack (add its real DB, its real services, its real table names from the
   schema — the schema is read inward to build the grep, never outward into the UI).
3. Each hit is triaged: LEAK (renders to the user — fix), FALSE POSITIVE (a comment,
   a log-only string, a test fixture — record it as triaged, not deleted), or
   NEEDS-DECISION (a genuinely technical need — see §7, express in user concepts).

### 4.2 Error-path walkthrough (half day — the highest-yield hunt)

For every primary flow, trigger the failure at each step and read the resulting UI:
- Submit a form with invalid data (validation errors — the #1 leak source).
- Submit with the network off (network errors).
- Submit with the server returning 4xx/5xx (server errors — stub the response).
- Load a route with the API down (page-level error state).
- Trigger an error boundary (throw in a component in a staging build).
- Open an empty list, an empty search, an empty billing history (empty states).
Record every string the user sees. Any B-1–B-8 item = a leak with a §6 rewrite.

### 4.3 Route / label inventory vs user concepts (1 hour)

List every route and every nav label. Beside each, write the user concept it serves
("bookings — the user's bookings"). Any route/label whose user-concept column is empty
or is filled with a stack term ("postgres-tables — the tables") is a leak. Routes
themselves are renamed only if the path is shown to users; internal route names that
never render are not leaks — but a nav label that names a module is.

### 4.4 The non-technical-user test (30 minutes, the cheapest test in this file)

Show 5 surfaces (landing, dashboard, one form error, one empty state, settings) to a
non-technical user of the product (or, failing that, read them aloud as if to one).
Ask: "What does this mean? What do you do next?" Any answer that requires knowing
how the app is built ("I'd have to ask what Postgres is") marks a leak. Record the
exact sentence that failed — that sentence is the rewrite target.

## 5. The leak-audit checklist (for the design-intelligence quality gate)

Run at every pass exit (Pass 1–7) on everything that pass touched, and in full at the
AFTER gate (`11-scoring-shipping.md` §1). Checklist (each item pass/fail, with evidence):

- [ ] L-1 Copy scan re-run: ban-list grep over all user-facing strings touched = 0 hits
  (or every hit triaged in writing per §4.1 step 3).
- [ ] L-2 Error-path walkthrough re-run on touched flows: 0 leaking error strings.
- [ ] L-3 Empty states on touched lists: every empty state passes L-C4 (user concept +
  why + next action), 0 table/record mentions.
- [ ] L-4 Token/component names: no token, class, or component name that can reach the
  UI (via error boundaries, dev overlays, or `title`/aria attributes) names the stack.
- [ ] L-5 URLs shown to users: displayed URLs are user-facing paths only.
- [ ] L-6 Counts shown: every count is a count of user things with its unit named
  (L-C5); 0 counts of pages/routes/modules/tables/records.
- [ ] L-7 Genuinely-technical needs: every item in §7 has a user-concept expression
  recorded; no item was left in stack terms "because the user needs the detail".
- [ ] L-8 Leak score: BEFORE <N> → AFTER <M>, target 0. Any leak = gate FAIL veto
  regardless of the /80 score (see §1).

**Scored item:** leak count is recorded as its own scored line in the audit file
(`01-audit-and-scoring.md` §2 §3 and §5): `Leak score BEFORE: <N> → AFTER: <M> /
target 0`. It is not folded into the /80 total (folding it would let a high /80
average it away) — it stands beside the total as a veto: `GATE: PASS only if /80 ≥64
AND hard categories 10/10 AND leak score = 0`.

## 6. Leak-vs-clean example pairs (at least 8 — each: leaking UI → clean version)

| # | Leaking UI text / behaviour (BEFORE) | Clean user-facing version (AFTER) | Ban item |
|---|---|---|---|
| L-1 | Settings: "Connected database: PostgreSQL 15" | "Your data is stored securely." (If a status is needed: "Your data is backed up daily." — the fact the user cares about is the backup, not the engine.) | B-1 |
| L-2 | Error toast: "422: `users.email` unique constraint — duplicate key" | "That email is already registered. [Sign in] or [Reset password]." | B-7, B-8 |
| L-3 | Dashboard stat: "1,204 rows in `bookings`" | "1,204 bookings" (with the unit named; the stat's label is "Bookings this month" — the count is of user things). | B-2 |
| L-4 | Sidebar footer: "12 pages · 4 modules" | (Removed entirely — the user navigates by job; the count served no user need. If a version is needed for support, it goes in the support reference code, §7.) | B-3 |
| L-5 | Loading: "Fetching /v2/bookings…" | "Loading your bookings…" | B-4, B-6 |
| L-6 | Settings → Sync: "API endpoint: /v2/readings · table: field_readings" | "Your readings sync when you're back in signal." (The user's question is "will my work be saved?" — answered in user terms.) | B-4, B-2 |
| L-7 | Billing → Storage: "PostgreSQL 15 · 7.2 GB" | "Storage: 7.2 GB of 10 GB used" + the usage vessel element (`06-signature-elements.md` E-06). | B-1 |
| L-8 | Form error: "Error: Cannot read properties of undefined (reading 'customer_id')" | "We couldn't save your invoice. Check your connection and try again. [Retry]" (+ reference code ABC-123 for support, §7). | B-7, B-8 |
| L-9 | Empty orders list: "No records found in `orders`" | "No orders yet — when someone orders, they'll appear here. [Share your shop link]" | B-2 |
| L-10 | Admin banner: "Billing Service v2.3 — Auth Module healthy" | (Removed — the user has one product. If an admin needs a health signal, it is "All systems working" with a timestamp, in user terms; the version goes to the log, not the screen.) | B-5, B-6 |
| L-11 | Invoice PDF footer: "Generated by Node 20 · React 18 · table invoices" | "Invoice INV-2026-114 · Issued 24 Nov 2026" (the invoice's own facts, in user terms). | B-6, B-2 |
| L-12 | Search empty state: "0 results — query: SELECT * FROM books WHERE title LIKE '%x%'" | "No books match 'x'. Try a different title or author. [Clear search]" | B-2, B-7 |

Rewrite rule for every pair: keep the USER'S next step, delete the machine's address.
If the clean version has no next step and the leaking version had none either, the
surface probably should not exist — remove it (L-4, L-10) rather than rewording it.

## 7. When the backend genuinely needs user-visible technical info

Sometimes the user really does need a technical fact. The rule is: express it in user
concepts, never stack terms. The translation table:

| Genuine need | Stack-term version (banned) | User-concept version (correct) |
|---|---|---|
| Storage limit | "PostgreSQL 15 · 7.2 GB" / "Database size: 7.2 GB" | "Storage: 7.2 GB of 10 GB used · 2.8 GB left" (+ the usage vessel, `06` E-06) |
| Support diagnosis | "Send us the trace ID / stack trace" | "Include reference ABC-123" — an opaque code the support team can map to the
  incident internally. The code names nothing about the stack. |
| Version for support | "App v2.3.1 · React 18 · API v2" (shown in the UI) | A "About" line for support only: "Version 2.3.1 · Reference ABC-123" — the app
  version (a product fact) is fine; the stack list is not. |
| Sync/offline status | "Sync worker: pending · table field_readings: 42 rows queued" | "42 readings waiting to sync — they'll send when you're back in signal." |
| Payment provider | "Processed by Stripe (stripe.com)" as a stack label | A payment provider MAY be named where the user is choosing or trusting a payment
  method ("Pay with card — processed securely") — name the provider only on the
  payment step, as a trust mark the user recognises, never as a stack label elsewhere.
  "Powered by Stripe" on a marketing page is a stack label; "Card payments are
  processed securely by Stripe" at checkout is a trust fact. The line is whether the
  user is deciding something by it. |
| File/data export | "Export table `bookings` as CSV (Postgres dump)" | "Download your bookings as a spreadsheet (.csv)" — the format the user opens is
  named (CSV/spreadsheet); the dump mechanism is not. |
| Performance/plan limits | "Rate limit: 100 req/min on /v2/bookings" | "Pro plan: up to 1,000 bookings a month" — the limit in the user's units, on the
  plan they bought. |

If no user-concept translation exists for a piece of technical information, the
information does not belong in the UI at all — it belongs in the log, the runbook, or
the support tool. "The user needs the detail" is tested by §4.4: if a non-technical
user cannot use the detail to decide anything, it is not needed.

## 8. Cross-reference map

| This file's section | Where it is used |
|---|---|
| §1 principle + veto | `01-audit-and-scoring.md` §2 §3, §5; `11-scoring-shipping.md` §1 (gate) |
| §2 ban list | `04-component-upgrades.md` §2 (copy/label rules L-C1–L-C8); `02-theme-decision.md` §§3.6/4.4 (leak exit criteria) |
| §3 taxonomy | `01-audit-and-scoring.md` §4 step 6 (leak sweep); `03-staged-passes.md` §1.5 (per-pass leak gate) |
| §4 detection | `01-audit-and-scoring.md` §4 (audit walk step 6) |
| §5 checklist | Every pass exit (`03`); the AFTER gate (`11` §1) |
| §6 pairs | `04` §§5/13/15/17 (error/empty/settings copy); `08-case-studies.md` (one worked leak fix per study) |
| §7 translations | `04` §13 (settings/billing); `06` E-06 (usage vessel) |
