# Example 1 — Backfill with an orphan report, not a default-tenant sweep

Scenario (hypothetical): "DispatchDesk," a job-scheduling app built for one
client, Northgate Facilities, is converting to multi-tenant SaaS. The legacy
tenant has been created first as an ordinary catalog tenant (AR-263). Three
tables now need a tenant key: `jobs`, `job_documents`, and `attachments`.
All counts below are the conversion plan's own working numbers for this
fictional product, not industry data.

## Before

The draft migration does everything in one step:

```sql
ALTER TABLE attachments ADD COLUMN tenant_id bigint NOT NULL DEFAULT 1;
UPDATE attachments SET tenant_id = 1 WHERE tenant_id IS NULL;
```

The reasoning in the pull request: "Everything in the database belongs to
Northgate, so tenant 1 is always right, and the default lets the NOT NULL
land in the same deploy." An engineer also offers to "just run the UPDATE
from the console first, so the migration is quick when it ships."

That plan is banned twice over. Sweeping every unassigned row into the
legacy tenant is the default-tenant sweep (BAN-AR-133), and a hand-run
console update is the console backfill (BAN-AR-132). It also breaks
AR-264 — column, backfill, and constraint in one step, with no resumable
job — and AR-265: nobody has stated a rule for which rows belong to whom,
so "everything is Northgate's" is an assumption, not a decision. It happens
to be wrong: Northgate's office manager confirms a second firm used the
app informally for one season, under a shared login — the "invisible
second client" the inventory (AR-261) was supposed to find.

## After

The conversion runs as expand, backfill, verify, contract (AR-264):

1. **Expand.** `tenant_id` ships nullable on all three tables, with no
   default. Nothing about user-visible behavior changes.
2. **Backfill as a versioned job.** A resumable, batched job (batches of
   500 rows, rate-limited, logging rows done / remaining / errors) assigns
   ownership by stated rules (AR-265): a job belongs to the tenant of its
   owning crew lead; a document belongs to the tenant of its job; an
   attachment belongs to the tenant of its uploading user.
3. **Orphans go to a report, not to tenant 1.** The job leaves 214
   attachments unassigned and writes them to an orphan report with the
   reason each rule failed. Reviewing it, the team finds:
   - 161 uploaded by the second firm's shared login → assigned to a second
     legacy tenant created for that firm under AR-263, after its owner
     confirms the list in writing.
   - 38 uploaded by a since-deleted admin account, filenames matching
     Northgate job references → assigned to Northgate, with the filename
     rule recorded next to each decision.
   - 15 with no uploader, no job link, and no matching filename → left
     unassigned; the contract step stays blocked for `attachments` until
     Northgate's owner identifies them as test uploads and approves their
     deletion.
4. **Reconcile, then contract.** Gate G-AR-132 runs: zero NULL `tenant_id`
   values, an empty orphan report, and per-tenant row counts that sum
   exactly to the pre-conversion totals for all three tables. Only then do
   the NOT NULL constraint and the tenant-leading indexes land, and
   uniqueness is re-scoped in the same step — `UNIQUE (tenant_id, ref_code)`
   replaces the global unique on job reference codes (AR-266).

Note: corrects AR-264 and AR-265 — the backfill is a separate, resumable,
observable job under migrations discipline, every row gets a decided owner
from a stated rule, and unassigned rows block cutover in an orphan report
instead of being swept into a default tenant (BAN-AR-132, BAN-AR-133;
verified by G-AR-132).
