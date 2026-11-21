# pci-compliance

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** PCI DSS v4.0.1 and SAQ structure, https://flopay.co/guides/pci-compliance-for-small-business.html ; SAQ A January 2025 revision, https://scandiweb.com/blog/pci-dss-saq-2025-updates-for-ecommerce-merchants/ ; Stripe, "What is PCI DSS compliance?", https://stripe.com/guides/pci-compliance
- **Depends on:** payments, secrets-management
- **Feeds into:** security-audit, legal-documents

## When to use / Do NOT use

- **Use when:** the product takes card payments in any form — checkout, subscriptions, in-app purchase flows — or staff tools can view orders or trigger refunds.
- **Do NOT use when:** no card payments exist anywhere in the product; for the payment integration mechanics themselves use payments (D11) — this skill owns scope, attestation, and PAN exclusion.

## Rules

1. **SE-241 — Card data never touches the product.** Card entry happens only on the provider's hosted payment page or in provider-served hosted fields/iframe. The product stores and transmits tokens and provider transaction IDs, never the PAN.
2. **SE-242 — PAN and CVV are excluded from every surface.** The full card number and CVV are never stored, logged, rendered, or transmitted by the product — not in database fields, "notes" fields, analytics events, support tickets, error reports, or debug output. CVV is never stored after authorization by anyone.
3. **SE-243 — The integration class sets the SAQ, and is documented before build.** Fully outsourced hosted page/iframe typically maps to SAQ A; a merchant-built form posting to the gateway maps to SAQ A-EP; card data touching your own systems is SAQ D territory. Record the chosen class and its SAQ mapping in the project docs before the integration is built — scope is an architecture decision, not paperwork afterwards.
4. **SE-244 — The acquirer confirms the SAQ type.** The SAQ type is determined by the actual integration and confirmed with the acquirer; the acquirer and card brands, not the PCI SSC and not this skill, have the final word on validation duties. Present SAQ A / A-EP / D as the typical mapping, never a guarantee.
5. **SE-245 — State what PCI DSS is.** PCI DSS v4.0.1 is a contractual obligation enforced through the merchant agreement by the card brands and acquirer, not a statute. Never promise that SAQ A status equals legal compliance in any jurisdiction.
6. **SE-246 — SAQ A does not exempt the embedding site.** Per the January 2025 SAQ A eligibility revision, even SAQ A merchants must confirm their site is protected against script attacks that could affect the payment page. Inventory every third-party script on checkout pages and remove any that are not required.
7. **SE-247 — Admin tools sit inside the payment trust boundary.** Order and refund views show at most card brand and last four digits; refunds and lookups run on provider transaction IDs. Staff tooling never displays, exports, or stores a full card number.
8. **SE-248 — Claims match the filed attestation exactly.** Marketing copy may not say "PCI certified" or "PCI compliant" unless it matches the filed attestation word for word in scope. The provider's compliance does not transfer to the merchant, and a hosted payment page alone never makes the whole business "PCI compliant."
9. **SE-249 — Attestation is repeated, not one-off.** Complete the SAQ on the acquirer's required cadence and again after any integration change: new provider, new checkout flow, new card field, or new third-party script on the payment page.
10. **SE-250 — Payment pages are HTTPS-only with no mixed content.** Every page that embeds, frames, or redirects to card entry is served over HTTPS with a current TLS configuration, and loads no HTTP subresources.
11. **SE-251 — Provider secret keys stay out of source and bundles.** Live secret keys live in environment or a secret manager, never as literals in source, test fixtures, or shipped client code; client code carries only the publishable key.
12. **SE-252 — A PAN found out of place is an incident, not a cleanup task.** If a scan or report finds card data in logs, a database, or tickets: stop the flow that produced it, purge the data, record where it was found and how it got there, and re-run the scan before the work is called done.

## BAN list

- **BAN-SE-121 — PAN or CVV persisted or emitted by the product.** Banned: storing, logging, or rendering a full card number or CVV anywhere, including request-body logs, notes fields, and error reports. Defeats: DET-CODE-029. Bad: the API logger records full request bodies, so `{"card": "4242 4242 4242 4242", "cvc": "123"}` lands in the log store. Instead: log only the token and provider transaction ID, and redact card-shaped fields at the logger. Severity: BLOCK.
- **BAN-SE-122 — Full card number in admin or support tooling.** Banned: any staff-facing page, export, or ticket view that displays or stores a full PAN. Defeats: DET-INF-021. Bad: the admin order page shows the customer's full card number "to help with refunds." Instead: show brand and last four digits only, and run refunds against the provider transaction ID. Severity: BLOCK.
- **BAN-SE-123 — Card entry reachable over HTTP or mixed content.** Banned: a checkout or payment-embedding page served over HTTP, redirecting through HTTP, or loading HTTP scripts/assets. Defeats: DET-INF-014. Bad: the checkout page is HTTPS but loads a marketing script over `http://`, and the payment redirect passes through an HTTP hop. Instead: serve the whole checkout path over HTTPS with HTTP-to-HTTPS redirect and HTTPS-only subresources. Severity: BLOCK.
- **BAN-SE-124 — Provider secret key hardcoded in source.** Banned: a live payment-provider secret key as a string literal in source, config committed to the repo, or a client bundle. Defeats: DET-CODE-018. Bad: `const key = "sk_live_..."` committed in the checkout module "temporarily." Instead: read the secret key from the secret manager or environment on the server; ship only the publishable key to the client. Severity: BLOCK.

## Gates

- **G-SE-121 — PAN-pattern scan.** Verifies: SE-242, SE-252. Check: run a Luhn-validated card-number scan (e.g. a regex for 13–19 digit candidates piped through a Luhn check) over the codebase, a production database dump, and a sample of application and error logs. Pass: zero Luhn-valid hits outside documented test fixtures using published test card numbers. Fail: block shipment; treat hits per SE-252. Recorded in: progress.md.
- **G-SE-122 — Checkout integration review.** Verifies: SE-241, SE-243. Check: on every release that touches checkout, inspect the served page's DOM and source and confirm card fields are provider-served (hosted page or provider iframe origin), and that no product endpoint receives card fields. Pass: card data provably never reaches product systems; the documented integration class still matches reality. Fail: block the release and re-determine the SAQ type. Recorded in: progress.md.
- **G-SE-123 — Checkout script inventory.** Verifies: SE-246. Check: list all third-party script origins loaded on checkout/payment pages (e.g. `grep -o 'src="https://[^"]*"'` over the built checkout pages) and diff against the approved inventory in the project docs. Pass: no unlisted origin; every listed script has a named owner and purpose. Fail: block the release until the script is removed or approved and inventoried. Recorded in: progress.md.
- **G-SE-124 — SAQ currency check.** Verifies: SE-244, SE-249. Check: manual — confirm the completed SAQ and attestation are on file, dated within the acquirer's required cycle, of the type matching the documented integration class, with the acquirer's confirmation recorded. Pass: all four facts hold. Fail: block any launch or compliance claim until the attestation is renewed. Recorded in: progress.md.
- **G-SE-125 — Compliance-claims sweep.** Verifies: SE-245, SE-248. Check: `grep -ri "pci" site-copy/ marketing/` (or the project's copy locations) and compare every claim against the filed attestation. Pass: no claim exceeds the attestation's scope and none calls PCI DSS a law or legal certification. Fail: block publication of the copy. Recorded in: progress.md.

## Anti-patterns

- **Paperwork-first scoping.** Filling in the SAQ before choosing the integration, then quietly designing the checkout to fit the form already filed. Catch it: the SAQ's date predates the integration decision in the project docs.
- **Tokenization theater.** Collecting card data in the product's own JavaScript, sending it to the provider for a token, and calling the result "SAQ A — we only store tokens." If the PAN crossed your code, scope already moved; catch it in the G-SE-122 review.
- **Last-four creep.** Admin views that start at brand + last 4 and gradually gain digits, expiry, or a "full number for support" toggle. Catch it by diffing order-view fields against SE-247 at each release.
- **Set-and-forget attestation.** The SAQ was filed once at launch; the provider, checkout flow, and script stack have all changed since. Catch it: attestation date older than the last checkout change.

## Examples

- [Example 1 — Checkout form: own form vs provider hosted fields](examples/example-1.md) — violates/corrects SE-241, SE-243.
- [Example 2 — Admin order view: full PAN vs brand + last four](examples/example-2.md) — violates/corrects SE-247, SE-242.
- [Example 3 — Marketing claim: "PCI certified" vs attestation-matched copy](examples/example-3.md) — violates/corrects SE-248, SE-245.

## Recall anchors

- If the PAN touches your systems, your scope already changed.
- Hosted page buys SAQ A scope, not a "PCI compliant" business.
- Brand + last four is all staff ever see.
- The acquirer, not the checklist, has the final word.
- Attestation expires; integration changes re-open it.

## Checklist

- [ ] Integration class chosen and documented, with its typical SAQ mapping (SE-243).
- [ ] Card entry is provider-hosted or provider-iframed; no product endpoint receives card fields (SE-241).
- [ ] PAN-pattern scan run over code, database dump, and logs — zero hits (G-SE-121).
- [ ] Admin and support views show at most brand + last four (SE-247).
- [ ] Third-party scripts on checkout pages inventoried and minimized (SE-246).
- [ ] SAQ completed, acquirer-confirmed, and dated within the required cycle (SE-244, SE-249).
- [ ] Every public PCI claim matches the filed attestation exactly (SE-248).
