# sdk-embeddables

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, Payment Element documentation (provider JS pattern, checked 2026-11-21) — https://docs.stripe.com/payments/payment-element ; Stripe, "Receive Stripe events in your webhook endpoint" — https://docs.stripe.com/webhooks
- **Depends on:** api-keys-management, payments
- **Feeds into:** subscriptions, third-party-apis

## When to use / Do NOT use

- **Use when:** a project ships or consumes a client-side piece: a provider's payment element, a third-party SDK loaded into a page, or the project's own embeddable widget that other sites paste in. This skill owns how that piece loads, isolates, versions, and reports state.
- **Do NOT use when:** the integration is server-to-server only (third-party-apis owns the adapter), the question is what a payment outcome means for the order (payments owns money state), or the embed is a marketing tracker with no functional contract (lifecycle-email and cookie-consent own consent for those).

## Rules

1. **IN-221 — Provider JS loads from the provider's origin, per the provider's instructions.** A payment provider's JS (e.g. Stripe.js with the Payment Element) is loaded from the provider's own origin exactly as documented, so card data flows browser → provider directly. A self-hosted, mirrored, or "optimized" copy of a provider's payment JS is never shipped.
2. **IN-222 — The client holds publishable keys only.** The embedded layer is initialized with the provider's public/publishable key, domain- or referrer-restricted where the provider allows. A secret key in a loader snippet, widget config, or client bundle is a defect (key handling itself is api-keys-management).
3. **IN-223 — The client never decides an outcome.** The embed renders state; amounts, entitlements, and success are confirmed server-side (verified webhook or API re-read, per payments). A client callback — element "complete", SDK success event — is display input, never proof.
4. **IN-224 — Sandbox isolation by default.** Your own embeddables ship as an iframe the loader injects; third-party embeds are contained so their DOM, CSS, and errors cannot reach the host page. A widget that requires the host to disable CSP, allow inline scripts, or drop a frame policy is not shippable.
5. **IN-225 — The loader is versioned and immutable per version.** Every release has a semantic version, a changelog entry, and a supported-versions policy; the documented production snippet pins a version (e.g. `loader@1.4.0.js`). "Latest" URLs are development-only and never appear in production documentation or snippets.
6. **IN-226 — Integrity controls where the provider permits them.** Third-party scripts that the provider serves as static files load with subresource integrity (SRI) or an equivalent pin. Where the provider's documented method forbids pinning (its JS must always be the current build from its origin), the provider's instruction wins and the exception is recorded next to the snippet.
7. **IN-227 — No load before consent where tracking is involved.** An SDK or embed that sets cookies, fingerprints, or reports analytics does not load — no script tag, no network request — until the visitor's consent state allows it. Purely functional embeds (a payment element on the checkout page) load only on the pages that need them.
8. **IN-228 — Failure is isolated and visible.** SDKs load async/deferred with a timeout; if the provider's script fails or times out, the host page keeps working and the embed area shows an honest unavailable state with a retry or fallback path. A blank hole or a frozen page is a defect.
9. **IN-229 — Configuration crosses the frame boundary by contract only.** Hosts configure your embed through documented data attributes or `postMessage`; every `postMessage` handler validates the sender's origin and the message shape before acting. Undocumented globals and DOM scraping of the host page are not a configuration surface.
10. **IN-230 — Client-side validation is UX only.** The element may format a card number and flag an obvious typo; the server re-validates everything that matters (amount, eligibility, state) before acting. Nothing the client "validated" is trusted downstream.
11. **IN-231 — Theming uses the documented hooks.** Appearance flows through the provider's appearance API or your embed's CSS-variable contract. Neither side reaches across the boundary: the host does not style inside the provider's iframe, and the widget ships scoped styles that survive a CSS-reset host.
12. **IN-232 — Test mode is labeled and never the production default.** Test-mode keys, demo data, and sandbox endpoints appear only in test builds and are visibly labeled there. The production snippet, docs example, and demo page each state which mode they run; an unlabeled test-mode embed in production is a defect.

## BAN list

- **BAN-IN-111 — The lookalike payment element.** Banned: your own card inputs styled to resemble the provider's element, collecting number/expiry/CVC in page fields. Defeats: DET-FAKE-007. Bad: custom inputs run a Luhn check, accept any 16 digits, and the order is marked paid — no provider is ever contacted. Instead: mount the provider's real element from the provider's origin so the provider validates and decides (IN-221). Severity: BLOCK.
- **BAN-IN-112 — Client-callback success.** Banned: rendering "Payment complete" or unlocking content because the element's client callback fired. Defeats: DET-FAKE-006. Bad: the widget shows a green checkmark on the SDK's success event while the payment was never confirmed server-side — the checkout confirms an order that was charged nothing. Instead: the callback shows a processing state; success renders only after server confirmation (IN-223). Severity: BLOCK.
- **BAN-IN-113 — The decorative trust indicator.** Banned: an embed that displays "secure checkout", "agents online", or live counters driven by local state, timers, or the snippet's config rather than the real system. Defeats: DET-FAKE-018. Bad: the support widget badge cycles "3 agents online" from a random timer on a site with no support desk. Instead: indicators render only values read from the system they describe, or they are removed (IN-223). Severity: BLOCK.
- **BAN-IN-114 — The unlabeled test-mode embed shipped live.** Banned: production pages loading the embed with test keys or demo mode, so interactions complete against a sandbox while presented as real. Defeats: DET-FAKE-006. Bad: the checkout element still carries the test publishable key from the staging snippet; customers "pay" successfully and nothing is ever charged. Instead: production snippets pin live keys, test mode stays in labeled test builds (IN-232). Severity: BLOCK.
- **BAN-IN-115 — The static stand-in.** Banned: when the SDK fails to load, leaving a screenshot-like image, a hardcoded HTML copy, or a pre-rendered success state of the widget in its place. Defeats: DET-FAKE-022. Bad: a CDN outage swaps the payment element for a static mock that still shows a Pay button and a "saved card" — state the system never had. Instead: the embed area shows an honest unavailable state with retry/fallback (IN-228). Severity: BLOCK.

## Gates

- **G-IN-111 — Hostile-host test.** Verifies: IN-224, IN-228, IN-231. Check: automated — browser test loads the embed on a test page served with a strict CSP (no `unsafe-inline`), a CSS-reset host stylesheet, and throttled network; assert the widget renders, functions, applies the theming hooks, and fires its event callbacks. Pass: all assertions hold under the hostile host. Fail: block shipment. Recorded in: progress.md.
- **G-IN-112 — Version-pin check.** Verifies: IN-225. Check: automated — script extracts the version string from the loader file, the documentation examples, and the production snippet, and asserts all three agree and none references a "latest" URL. Pass: one version, pinned everywhere. Fail: block the release. Recorded in: progress.md.
- **G-IN-113 — Payment-element log scan.** Verifies: IN-221, IN-230. Check: automated — complete a test-mode purchase through the embedded element, then scan the project's server request logs for PAN-shaped digit sequences and card field names. Pass: zero hits; card data appears only in the browser → provider path. Fail: block shipment. Recorded in: progress.md.
- **G-IN-114 — Consent-gate test.** Verifies: IN-227. Check: automated — load a page carrying a tracking-capable embed with consent denied and assert zero network requests to the SDK's origins; grant consent and assert the SDK loads. Pass: no pre-consent request, load after consent. Fail: block shipment. Recorded in: progress.md.
- **G-IN-115 — Failure-isolation test.** Verifies: IN-228. Check: automated — browser test blocks the SDK's origin at the network layer, loads the host page, and asserts the page's core functions still pass their smoke checks and the embed area shows the unavailable state. Pass: host unaffected, honest fallback shown. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **The double-loaded snippet.** The host pasted the snippet twice (header plugin plus theme file), so the SDK initializes twice and every event handler fires twice. Catch it: the loader guards on a global sentinel and refuses a second initialization; check the test page's network panel for duplicate script requests.
- **The `postMessage` free-for-all.** A message handler that acts on any origin's messages because "only our widget sends those." Catch it: grep handlers for an origin comparison against the embed's expected origin; a handler without one is this pattern (IN-229).
- **The CSS arms race.** Widget styles escalate with `!important` and global selectors to beat the host, breaking the next host instead. Catch it: the widget's stylesheet contains no global element selectors and no `!important` outside its scoped prefix (IN-231).
- **Snippet drift in the wild.** Hosts run a loader version from two majors ago because nothing told them to update. Catch it: the loader reports its version with its server calls, and the supported-versions policy (IN-225) names the cutoff the dashboard warns about.

## Examples

- [Example 1 — Replacing a lookalike card form with the provider's real element](examples/example-1.md) — corrects IN-221.
- [Example 2 — Pinning the loader instead of shipping "latest"](examples/example-2.md) — corrects IN-225.
- [Example 3 — Making a tracking embed wait for consent and fail soft](examples/example-3.md) — corrects IN-227.

## Recall anchors

- Provider JS comes from the provider's origin — never a copy.
- The client renders state; the server decides outcomes.
- Pin the version; "latest" is for development only.
- No consent, no load — for anything that tracks.
- If the SDK dies, the page lives and says so honestly.

## Checklist

- [ ] Provider JS loads from the provider's origin per its documentation; no self-hosted copies (IN-221, G-IN-113).
- [ ] Only publishable keys reach the client, restricted where the provider allows (IN-222).
- [ ] Success and entitlement render only after server confirmation, never on a client callback (IN-223).
- [ ] Embed is iframe-isolated and works under the host's CSP without weakening it (IN-224, G-IN-111).
- [ ] Loader, docs, and production snippet all pin the same version; no "latest" in production (IN-225, G-IN-112).
- [ ] Tracking-capable embeds make zero requests before consent (IN-227, G-IN-114).
- [ ] Blocking the SDK origin leaves the host page functional with an honest unavailable state (IN-228, G-IN-115).
- [ ] Test mode is labeled and absent from production configuration (IN-232).
