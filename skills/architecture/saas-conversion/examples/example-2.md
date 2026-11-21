# Example 2 — Shadow-mode isolation before enforcement, cohort by cohort

Scenario (hypothetical): "LedgerLane," a small invoicing app run for one
accountancy practice, has finished its tenant backfill. Row-level security
policies and tenant-scoped queries are written. The team lead proposes
turning them on. All tenant names and figures below are invented for this
example.

## Before

The release plan is a single Saturday deploy: enable the scoped queries,
switch on RLS, rebuild the search index, and convert the nightly statement
job — for the legacy tenant and for the two pilot tenants who signed up
during the beta, all at once. Rollback is described in one line: "restore
Friday's backup if it goes wrong."

That is the flag-day cutover (BAN-AR-131): one deploy puts everyone on the
new path, and the only way back destroys data written in the meantime. It
also skips AR-268 entirely — isolation would be enforced the first moment
it ever ran — and there is no per-cohort rollback to rehearse, so AR-271
cannot be satisfied either.

## After

Isolation ships in shadow first, then enforces per surface, per cohort:

1. **Observe mode (AR-268).** For each surface — invoice list and detail
   reads, the CSV export, full-text search, file downloads, and the nightly
   statement job — the new tenant-scoped path runs alongside the legacy
   path. Users still see legacy results. Every divergence is logged per
   tenant (AR-276): rows the scoped path would hide, rows it would wrongly
   show.
2. **Divergences are conversion bugs, not noise.** The first week of the
   log shows three real defects, each traced back to the AR-261 inventory:
   - The export job sets no tenant context, so its scoped query returns
     zero rows — a job surface the inventory had marked "internal, leave
     global." Fixed by converting the job to iterate tenants with context
     set per tenant (AR-269).
   - Search results diverge for documents indexed before conversion: the
     index has no tenant field. Fixed by re-indexing with the tenant field
     before search enforcement, as AR-269 requires.
   - Twelve invoices appear in the scoped path for the wrong tenant — a
     backfill rule error on shared-counterparty invoices, corrected through
     the orphan/reassignment process, not by editing rows ad hoc.
3. **Enforce per surface on evidence (G-AR-133).** A surface's enforcement
   switches on only after its divergence log is empty for the agreed
   seven-day observation window. Search enforces nine days after reads,
   because its re-index finished later; surfaces advance independently.
4. **Cutover per cohort behind a flag (AR-270, AR-271).** Enforcement rolls
   out under the flag `conversion.cohort_path`, owned by the platform lead
   with a retirement date in the plan. Cohort 1 is the legacy tenant alone
   — the canary: it already works, so any breakage is the conversion's
   fault. Its error rate, latency, and divergence count are compared
   against its pre-conversion baseline (G-AR-134) before Cohort 2 (the two
   pilot tenants) moves. Before Cohort 1 moved, the rollback was rehearsed
   in staging: flip the flag back, confirm that invoices created during the
   converted window are still readable on the legacy path (they are —
   dual-written during the window, with a reconciliation job reporting
   drift, per AR-274), then flip forward again.

Note: corrects AR-268 and AR-270 — isolation is proven in shadow mode with
a burned-down divergence log (G-AR-133) before it is enforced, and cutover
happens cohort by cohort behind a named flag with a rehearsed rollback
(AR-271, G-AR-134), never as a flag day (BAN-AR-131).
