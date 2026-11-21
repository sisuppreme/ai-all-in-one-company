# domains-dns

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Cloudflare Docs, "DNS record types" — https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/
- **Depends on:** hosting
- **Feeds into:** ssl-certificates, cdn-strategy

## When to use / Do NOT use

- **Use when:** a domain is registered, transferred, or pointed at a host; any DNS record is created, changed, or removed; a migration moves a live domain between hosts; or mail starts sending from a domain.
- **Do NOT use when:** the task is certificate issuance or renewal mechanics (ssl-certificates) or CDN caching and edge rules (cdn-strategy). This skill owns the records those skills depend on, not their internals.

## Rules

1. **DO-201 — The domain is an organizational asset.** The production domain is registered to the organization, or demonstrably recoverable by it, with auto-renew on, MFA on the registrar account, and the transfer lock on. A domain only one person can renew or recover fails this rule.
2. **DO-202 — Records carry intent.** Every record exists because a named service needs it, and the apex and `www` names point at the host's documented targets for this project. The intended zone is written down as a record sheet before records are created.
3. **DO-203 — No bare CNAME at the apex.** The apex name never holds a plain CNAME record, which conflicts with the other records the apex must carry. Use the provider's CNAME flattening, ALIAS, or ANAME mechanism, or the A/AAAA records the host documents.
4. **DO-204 — Lower TTL before a migration.** Before a planned change, lower the affected records' TTL (proxied Cloudflare records default to an automatic 300-second TTL, as of 2026-11); make the change after the old TTL has elapsed, verify, then raise the TTL again.
5. **DO-205 — Verify with `dig`, not the dashboard.** A change is verified by `dig +short` output against the authoritative nameservers matching the record sheet. A registrar dashboard's green checkmark is not verification.
6. **DO-206 — Mail records ship with the domain setup.** SPF, DKIM, and DMARC records are published before the domain sends mail, not after the first spam-folder incident.
7. **DO-207 — No record points at a dead or borrowed target.** No record targets a tutorial's example IP, a documentation placeholder, or a decommissioned host. A stale record is removed in the same change that replaces it.
8. **DO-208 — The zone is versioned or exported.** DNS is declared in IaC, or the zone is exported after every change and the export committed. The current state of the zone must be reconstructible from the repository alone.
9. **DO-209 — Expiry and lock status are monitored.** The domain's expiry date is recorded with an alert ahead of it, and auto-renew, MFA, and transfer-lock status are re-verified quarterly.
10. **DO-210 — "Propagation" is never a status.** A change is reported done only when `dig` against the authoritative nameservers returns the new value. A record that was never created is reported as never created, with the `dig` output as evidence.

## BAN list

- **BAN-DO-101 — Tutorial-copied records.** Banned: DNS records copied from a tutorial or blog post, including that post's example IP or hostname. Defeats: DET-INF-030. Bad: the apex A record points at the IP address printed in the setup tutorial the developer followed. Instead: take the target from the host's own documentation for this project, record it on the record sheet, and verify it with `dig +short`. Severity: BLOCK.
- **BAN-DO-102 — Bare CNAME at the apex.** Banned: a plain CNAME record on the apex/root name. Defeats: DET-INF-030. Bad: `@ CNAME app.hosting.example` is created and the apex MX and TXT records stop resolving. Instead: use CNAME flattening, ALIAS, or ANAME at the apex, or the A/AAAA records the host documents. Severity: BLOCK.
- **BAN-DO-103 — The personal-account domain.** Banned: a production domain held in a personal registrar account with no auto-renew, no MFA, and no recovery path for the organization. Defeats: DET-INF-030. Bad: the company domain sits on the founder's personal account and card; when the card expires, the domain lapses. Instead: hold the domain in the organization's account with auto-renew, MFA, and the transfer lock on. Severity: BLOCK.
- **BAN-DO-104 — "Still propagating" as an excuse.** Banned: reporting a DNS change as pending propagation when the record was never created or points at the wrong target. Defeats: DET-INF-030. Bad: the site is down for a day under the status "DNS is still propagating" while `dig` shows no A record exists at all. Instead: create the record, verify with `dig` against the authoritative nameservers, and report the actual `dig` output. Severity: WARN.

## Gates

- **G-DO-101 — Record-sheet match.** Verifies: DO-202, DO-205. Check: automated — run `dig +short <domain> A`, `dig +short www.<domain> CNAME`, and `dig +short www.<domain> A` after every change and quarterly; diff the output against the committed record sheet. Pass: every returned value matches the sheet exactly. Fail: block sign-off; correct the record or the sheet in the same change. Before a production environment is provisioned, this gate's disposition is a recorded provisioning waiver per the §6.3 protocol; it unblocks when a production domain is provisioned and its DNS records are live to query. Recorded in: progress.md.
- **G-DO-102 — Registrar posture check.** Verifies: DO-201, DO-209. Check: manual registrar-console review with evidence (export or screenshot) covering account ownership, auto-renew, MFA, and transfer lock, plus the recorded expiry date and its alert. Pass: all four controls on and the expiry alert set. Fail: block launch until the posture is fixed. Recorded in: progress.md.
- **G-DO-103 — Mail authentication present.** Verifies: DO-206. Check: automated — `dig +short <domain> TXT`, `dig +short <selector>._domainkey.<domain> TXT`, and `dig +short _dmarc.<domain> TXT` all return records before the domain sends mail. Pass: SPF, DKIM, and DMARC records all resolve. Fail: block sending mail from the domain. Recorded in: progress.md.
- **G-DO-104 — Zone export currency.** Verifies: DO-208. Check: compare the committed zone export (or IaC state) date against the date of the last DNS change recorded in progress.md. Pass: the export is the same age or newer than the last change. Fail: export the zone and commit it before sign-off. Recorded in: progress.md.

## Anti-patterns

- **Record sprawl.** Forgotten subdomains from old previews and experiments still resolve to dead services. Catch it by diffing the zone export against the record sheet at the quarterly check; a record nobody can name a service for is removed.
- **The imported zone.** A previous project's zone file is imported wholesale, including its service-verification TXT records for tools this project never uses. Catch it by reviewing every imported record against this project's record sheet before applying.
- **TTL left at migration value.** The 60-second TTL set for a migration is never raised afterward, leaving the zone permanently chatty and fragile. Catch it by making "TTL restored" the last line of every migration checklist.
- **Two sources of truth.** Some records live in the registrar panel and others in a DNS provider, and nobody is sure which zone is authoritative. Catch it by confirming the nameservers with `dig +short <domain> NS` and keeping exactly one authoritative zone.

## Examples

- [Example 1 — Apex pointed with a bare CNAME](examples/example-1.md) — violates/corrects DO-203.
- [Example 2 — Migration done on hope and "propagation"](examples/example-2.md) — violates/corrects DO-204, DO-205, DO-210.
- [Example 3 — Mail sent before its records existed](examples/example-3.md) — violates/corrects DO-206.

## Recall anchors

- The domain belongs to the organization, never to a person's account.
- No bare CNAME at the apex — flatten, alias, or use A records.
- Lower TTL first, change, verify with `dig`, then raise TTL.
- `dig` output is verification; a dashboard checkmark is not.
- SPF, DKIM, and DMARC ship with the domain, not after the first incident.

## Checklist

- [ ] Domain held by the organization with auto-renew, MFA, and transfer lock verified with evidence (DO-201).
- [ ] Record sheet written, and apex plus `www` match it under `dig +short` (DO-202, DO-205).
- [ ] No bare CNAME at the apex; flattening/ALIAS or A/AAAA used instead (DO-203).
- [ ] Migration TTL lowered before the change and restored after verification (DO-204).
- [ ] SPF, DKIM, and DMARC records resolve before the domain sends mail (DO-206).
- [ ] No record points at a tutorial example, placeholder, or decommissioned host (DO-207).
- [ ] Current zone export or IaC state committed after the last change (DO-208).
