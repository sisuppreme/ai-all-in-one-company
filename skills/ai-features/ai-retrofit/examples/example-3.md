# Example 3 — The AI cleanup that overwrote the customer file

> Hypothetical product: "TradeLedger," a live invoicing tool whose
> customer file has accumulated records over nine years — duplicates,
> old address formats, and free-text notes included.

## Before

```text
Nightly job: "AI cleanup" (runs as a deploy migration, then nightly)
  For each customer record:
    - model normalises the address and rewrites it IN PLACE
    - model merges records it judges to be duplicates, deleting the
      "losing" record
    - model fills empty phone / tax-id fields with its best inference
  No proposal state, no provenance, no per-record log a user can open.
```

Six weeks later a customer disputes an invoice sent to an address they
moved away from two years ago: the cleanup had "normalised" a newer
address back to an older one, and a wrong merge had combined two
different businesses with similar names. The original records no longer
exist anywhere, so support cannot restore them, cannot show what
changed, and cannot even list which records the job touched.

## After

**Step 1 — Profile the legacy data before the model reads it at scale
(AI-208).** The profile of the scenario's customer file is recorded
first: field completeness per field, address-format drift across record
ages (three historical formats plus free text), language/encoding mix,
and the share of records the pipeline cannot process — in this scenario,
records with scanned-image-only addresses and records with conflicting
duplicate candidates are classed unprocessable. That share is a routing
input, not an error to hide.

**Step 2 — Evaluate on the real file, not a cleaned sample (AI-207,
G-AI-102).** The golden set is sampled from actual customer records —
including empty fields, pre-validation-era records, very long notes,
and known duplicate pairs — with personal data handled per ai-safety
before it enters any eval set. Acceptance floors are set per category,
including: zero unprocessable records silently dropped, and merge
precision held to the recorded floor because a wrong merge is the
highest-harm error in the AI-203 inventory scoring.

**Step 3 — The cleanup writes proposals, never records (AI-204).**

```text
ai_proposals table (separate from customers):
  proposal_id, customer_id, field, current_value, proposed_value,
  kind (normalise | merge-candidate | fill-suggestion),
  model_id, prompt_version, source_inputs, created_at, status

Customers table: unchanged by any model run.
```

- **Normalisations** appear in the existing customer-edit screen as
  "Suggested change — AI" beside the current value; accepting one writes
  through the product's existing validated save path, with its normal
  audit entry.
- **Merge candidates** are only ever pairs presented to a human with
  both records side by side; the merge itself is the product's existing
  manual merge action. The model never merges.
- **Inferred field fills are not offered at all**: a guessed phone
  number or tax ID presented as data is worse than an empty field, so
  the insertion point fails the AI-203 harm test and is dropped.

**Step 4 — Bulk work is a separate, auditable job (AI-208).** Proposal
generation over the back file runs as a resumable batch job with its own
run ID, its own cost line (AI-210 — re-processing unchanged records is
metered as retrofit waste, and records with an unchanged hash are
skipped), and a per-run report: records processed, proposals created,
records routed to "couldn't process." Unprocessable records stay fully
visible in search and lists with their original data untouched; nothing
is backfilled with a model guess presented as original data.

**Step 5 — Rollback stays trivial (AI-202, AI-212).** Because no
canonical record was ever written by the model, disabling the feature
means hiding the suggestion UI; proposals already accepted by humans
are ordinary edits in the audit log, and unaccepted proposals can be
retained or deleted under the AI-212 end-state data decision.

## Note

Violates AI-204 and AI-208 (BAN-AI-103, model output written over
canonical records unseen). Corrected by profiling the legacy file
first, evaluating on sampled real records including the unprocessable
categories (G-AI-102), storing every AI result as a provenance-marked
proposal applied only through the existing write path, and running bulk
enrichment as a separate resumable, auditable job — never as a side
effect of a deploy or a page view.
