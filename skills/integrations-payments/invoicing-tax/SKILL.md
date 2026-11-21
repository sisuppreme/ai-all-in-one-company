# invoicing-tax

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Subscription invoices" — https://docs.stripe.com/billing/invoices/subscription
- **Depends on:** payments, subscriptions
- **Feeds into:** refunds-disputes

## When to use / Do NOT use

- **Use when:** a project issues invoices or receipts, corrects them, or handles sales tax / VAT on transactions: invoice numbering, line-item math, tax-data capture, credit notes, document rendering, and records retention. This skill teaches implementation patterns only.
- **Do NOT use when:** the question is what a jurisdiction's rate, threshold, or registration rule actually is — that determination belongs to the operator's qualified accountant or the configured tax engine, never to this skill. Recurring charge mechanics belong to subscriptions; refunds and dispute evidence belong to refunds-disputes.

## Rules

1. **IN-061 — No tax advice, no hardcoded rates.** This skill never states a jurisdiction's tax rate, threshold, or registration rule, and no project code or document may carry one from memory. Any jurisdiction-specific figure in a project document is dated and sourced from the operator's jurisdiction sources, or it is removed.
2. **IN-062 — Rates are operator-supplied configuration.** Every rate and tax rule the system applies lives in configuration — per jurisdiction, product tax category, and effective date — entered by the operator and verified by them against their own jurisdiction sources or their tax engine at setup. A rate literal found in application code is a defect.
3. **IN-063 — Invoices issue from the billing system of record.** An invoice is generated from the stored charge data (or is the provider's own invoice), never assembled from a hand-built template with typed-in amounts. If the data is not in the billing record, it does not appear on the invoice.
4. **IN-064 — Sequential, gapless numbering per legal entity.** Invoice numbers are issued once, in sequence, by one issuing authority per legal entity. No number is skipped silently, reused, or issued by a second system.
5. **IN-065 — Voided invoices are retained and marked.** A voided or canceled invoice stays in the sequence with its number and a void marker. It is never deleted and never renumbered.
6. **IN-066 — The invoice total equals the provider charge to the minor unit.** Line items are copied from the charged amounts, tax is computed from the configured rate for each line's category, and the total is recomputed from those stored line items in integer minor units. A render-time recomputation that can drift from the charge is a defect.
7. **IN-067 — Credit notes correct issued invoices; edits never do.** An issued invoice is immutable. A correction issues a credit note that references the original invoice number and amount, plus a new invoice if the charge is re-issued.
8. **IN-068 — Tax data is captured at purchase time.** Customer legal name, address, tax ID where the operator's regime requires it, place-of-supply evidence, and the product's tax category are collected at checkout and stored on the transaction. Reconstructing them later from support tickets is the failure mode this rule exists to prevent.
9. **IN-069 — The download is the stored record.** The invoice PDF or receipt a customer downloads renders the same stored data that was issued; regenerating it produces the identical document. A static sample, a screenshot-like PDF, or a render from fixture data is fabrication, not a download.
10. **IN-070 — Every product carries an explicit tax category.** Each product is assigned a tax category in configuration, and that category selects the configured rate at charge time. An uncategorized product blocks invoicing for that sale instead of silently defaulting to a rate.
11. **IN-071 — Rounding is one stated, configured rule.** Whether rounding happens per line or per total, and how the currency rounds, is a single configuration choice applied identically by the charge, the invoice, and the credit note — so the three documents can never disagree by a minor unit.
12. **IN-072 — Records are retained and exportable.** Issued invoices and credit notes are stored immutably for the retention period the operator configures, and a bulk export is generated from those stored records — every exported row traceable to an issued document and its provider charge.

## BAN list

- **BAN-IN-031 — The hardcoded rate.** Banned: computing tax at checkout from a rate or threshold typed into code or copied from an article. Defeats: DET-FAKE-006. Bad: the checkout adds "20% VAT" from a constant a developer remembered; the confirmation presents the total as tax-compliant, but no engine and no accountant ever supplied that rate. Instead: the rate resolves from operator-verified configuration or the tax engine at charge time (IN-061, IN-062). Severity: BLOCK.
- **BAN-IN-032 — The sample invoice download.** Banned: a Download Invoice button that returns a static template, a sample PDF, or a render of fixture data instead of the customer's stored invoice. Defeats: DET-FAKE-019. Bad: every customer downloads the same "INV-1001, $49.00" sample regardless of what they actually bought. Instead: the download renders the stored record for that invoice number, and regeneration is identical to the issued document (IN-069). Severity: BLOCK.
- **BAN-IN-033 — The edited issued invoice.** Banned: correcting an issued invoice by editing its stored amounts, lines, or tax fields. Defeats: DET-FAKE-006. Bad: after a pricing complaint, an admin edits invoice INV-1042 from $59 to $49; the document now confirms an amount that was never charged. Instead: leave the issued invoice untouched; issue a credit note referencing it, and a new invoice if re-charged (IN-067). Severity: BLOCK.
- **BAN-IN-034 — The deleted void.** Banned: deleting a voided invoice or reusing its number so the sequence shows no trace of it. Defeats: DET-FAKE-011. Bad: INV-1050 is voided and deleted, its number reissued next week; the provider still holds the original charge, but the books hide it. Instead: the voided invoice stays in the sequence, marked void, and the number is never reused (IN-064, IN-065). Severity: BLOCK.
- **BAN-IN-035 — The self-declared paid invoice.** Banned: marking an invoice "paid" or "sent" from local UI state with no provider payment state and no recorded manual-payment entry behind it. Defeats: DET-FAKE-022. Bad: an admin clicks Mark Paid to close a support ticket; dashboards report the revenue as collected while no charge exists. Instead: invoice status derives from the provider payment state, or from a manual-payment record naming amount, method, and who recorded it (IN-063). Severity: BLOCK.

## Gates

- **G-IN-031 — Totals recomputation check.** Verifies: IN-066, IN-071. Check: automated — script recomputes every invoice in the period from its stored line items and the operator's tax configuration, then compares the result against the stored invoice total and the provider charge amount, in integer minor units. Pass: zero mismatches. Fail: block the release. Recorded in: progress.md.
- **G-IN-032 — Sequence integrity check.** Verifies: IN-064, IN-065. Check: automated — script lists invoice numbers per legal entity and asserts the sequence has no duplicates and no missing numbers except numbers present in the store and marked void. Pass: sequence complete. Fail: block the release and investigate before issuing further invoices. Recorded in: progress.md.
- **G-IN-033 — Render-diff test.** Verifies: IN-069, IN-063. Check: automated — regenerate a sample of issued invoices from stored data and diff every field (number, lines, tax, total, customer details) against the issued documents customers download. Pass: identical output for every sampled invoice. Fail: block shipment. Recorded in: progress.md.
- **G-IN-034 — No-rate-in-code scan.** Verifies: IN-061, IN-062. Check: automated — grep the billing code paths for percentage/rate literals and grep project documents for jurisdiction figures stated without a date and source; assert every applied rate resolves from configuration. Pass: zero hardcoded rates and zero undated jurisdiction figures. Fail: block shipment. Recorded in: progress.md.
- **G-IN-035 — Capture-completeness audit.** Verifies: IN-068, IN-070. Check: automated — query the period's invoiced transactions and assert each carries customer legal name and address, a tax ID wherever configuration marks it required, place-of-supply evidence, and a product tax category. Pass: 100% of invoiced transactions complete. Fail: block the invoicing release. Recorded in: progress.md.

## Anti-patterns

- **The spreadsheet shadow ledger.** Invoices are also tracked in a spreadsheet "just for finance," and the two records drift apart within a month. Catch it: ask which system issues the invoice number — if a human types numbers or totals anywhere outside the billing system of record, that is the real ledger and it is wrong (IN-063).
- **The helpful backfill.** A customer emails their tax ID weeks after purchase and support treats the record as complete because the value now exists somewhere in a ticket. Catch it: tax fields live on the transaction, captured at checkout; a value that exists only in a ticket thread was never captured (IN-068).
- **"The accountant will fix it at year-end."** Known mismatches between invoices and charges are left to accumulate for an annual cleanup. Catch it: the totals and sequence gates (G-IN-031, G-IN-032) run per release; a mismatch older than one release cycle is a process failure, not a backlog item.
- **Template drift on old invoices.** The invoice PDF template gets a redesign and historical invoices quietly re-render differently from what customers originally received. Catch it: after any template change, re-run the render-diff gate (G-IN-033) against invoices issued before the change, not only new ones.

## Examples

- [Example 1 — Replacing a hardcoded rate with operator configuration](examples/example-1.md) — corrects IN-062.
- [Example 2 — Replacing an edited invoice with a credit note](examples/example-2.md) — corrects IN-067.
- [Example 3 — Replacing a sample-PDF download with a render of the stored record](examples/example-3.md) — corrects IN-069.

## Recall anchors

- Patterns, never rates: tax figures are configuration the operator verifies, not knowledge the skill claims.
- The invoice is a render of the charge record — if it is not in the record, it is not on the invoice.
- Numbers are issued once, in sequence; voids stay visible forever.
- Issued means immutable: corrections are credit notes, never edits.
- Capture tax data at checkout; there is no honest way to reconstruct it later.

## Checklist

- [ ] No tax rate, threshold, or jurisdiction rule appears in code or docs without operator configuration and a dated source (IN-061, IN-062, G-IN-034).
- [ ] Invoice numbers are sequential and gapless per legal entity; voids are retained and marked (IN-064, IN-065, G-IN-032).
- [ ] Every invoice total recomputes from stored line items plus configured tax and equals the provider charge to the minor unit (IN-066, G-IN-031).
- [ ] Issued invoices are immutable; corrections exist only as credit notes referencing the original (IN-067).
- [ ] Tax ID, legal name, address, place-of-supply evidence, and product tax category are captured at checkout on every sale (IN-068, IN-070, G-IN-035).
- [ ] Downloads and re-renders reproduce the issued document exactly from stored data (IN-069, G-IN-033).
- [ ] One configured rounding rule is shared by charge, invoice, and credit note (IN-071).
- [ ] Invoices and credit notes are retained for the configured period and bulk exports trace to stored records (IN-072).
