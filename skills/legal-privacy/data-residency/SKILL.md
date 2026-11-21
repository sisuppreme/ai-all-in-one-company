# data-residency

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32021D0914 ; https://www.dataprotection.ie/en/organisations/international-transfers/transfers-personal-data-third-countries-or-international-organisations ; https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/
- **Depends on:** privacy-laws
- **Feeds into:** legal-documents, compliance-audit, dsar-handling

## When to use / Do NOT use

- **Use when:** any processor or sub-processor is added or changed; infrastructure regions are chosen or altered (cloud region, backups, CDN, log sinks); product copy, a privacy notice, or a sales answer states where data lives or that it "stays" somewhere; a new market with localisation duties is entered.
- **Do NOT use when:** the question is which obligations apply at all (use privacy-laws and its obligations register first), or a transfer's legality is contested or novel (stop and require qualified counsel — this skill is implementation guidance, not legal advice).

## Rules

1. **LG-021 — The transfer register is the artifact.** For every processor and sub-processor, the register records: what personal data it receives, every location where that data is stored and processed, and the GDPR Chapter V mechanism covering each flow (adequacy decision, SCCs, BCR, derogation, or not-a-transfer because EEA-only). A flow with no register row does not exist as far as this skill is concerned.
2. **LG-022 — Register row before integration.** No processor, SDK, or third-party endpoint is integrated before its register row exists with a named transfer mechanism. "The vendor is GDPR compliant" is a slogan, not a mechanism, and never fills the field.
3. **LG-023 — Mechanism hierarchy, in order.** Check Article 45 adequacy first; failing that, Article 46 safeguards — in practice the Commission's 2021 SCCs; Article 49 derogations are last-resort only. Skipping a step requires a recorded reason in the register row.
4. **LG-024 — SCCs are documents, not checkboxes.** Where SCCs are the mechanism, the module is matched to the transfer scenario (controller/processor roles), a transfer impact assessment is documented post-*Schrems II* (destination law assessed, supplementary measures named where needed), and the signed DPA/SCCs are stored with the register.
5. **LG-025 — Inventory everywhere data actually lives.** The inventory covers primary datastores, replicas, backup targets, log sinks, analytics tools, support/helpdesk tools, error trackers, and CDN behavior — each with its region. A store nobody inventoried is treated as an unregistered transfer until proven otherwise.
6. **LG-026 — Config matches the register.** Region settings in infrastructure and deployment config (cloud regions, backup regions, log destinations) must equal the register's approved locations. Changing a region in config without updating the register first is a defect; the register leads, config follows.
7. **LG-027 — Residency claims must be provable.** Any claim in product copy, the privacy notice, or sales material ("data stays in the EU", "hosted in Germany") must be provable from the register plus infra config, line by line — including backups, logs, and support access. A claim that cannot be proven is deleted, not softened.
8. **LG-028 — Regions are operator decisions, recorded with a source.** The builder never assumes a region, a mechanism, or that a market has no localisation duty. Each region/mechanism choice is recorded in the register with who decided it, the source relied on, and the date.
9. **LG-029 — Support access is a transfer.** Remote access to personal data from a third country (support engineers, an agency, a contractor) is a transfer and appears in the register with its locations and mechanism, exactly like a hosting flow.
10. **LG-030 — Onward transfers are tracked on change, not annually.** Each processor's sub-processor list is reviewed when the vendor issues a change notice; register rows are updated at that moment. A register that no longer matches the vendor's current sub-processor list is stale and fails review.
11. **LG-031 — Derogations are per-transfer, never architecture.** An Article 49 derogation is documented for a specific transfer with its specific ground. A product flow that *depends* on a derogation to function is a defect and is re-architected onto adequacy or SCCs.
12. **LG-032 — Hard localisation is a separate, verified register row.** Sector rules and non-EU regimes that mandate local hosting are recorded as their own register rows, verified per market and sector at the date of entry. GDPR alone does not mandate EU hosting, and no market's localisation duty is generalised to others.

## BAN list

- **BAN-LG-011 — Vendor slogan as transfer mechanism.** Banned: a register row whose mechanism field reads "vendor is GDPR compliant", "covered by vendor's privacy policy", or equivalent, with no Chapter V mechanism named. Defeats: DET-CON-028. Bad: the register lists the email provider with mechanism "GDPR compliant (see their site)" while mail data is processed in the US. Instead: name the mechanism — adequacy, or SCCs with the module and the impact assessment on file (LG-022, LG-024). Severity: BLOCK.
- **BAN-LG-012 — Residency claim the infrastructure contradicts.** Banned: publishing a residency claim while any store, backup, log sink, or support location sits outside the claimed area. Defeats: DET-CON-015. Bad: the pricing page says "Your data never leaves the EU" while error reports flow to a US-region tracker. Instead: fix the configuration to match the claim, or delete the claim (LG-027). Severity: BLOCK.
- **BAN-LG-013 — Region in config that is not in the register.** Banned: a cloud region, backup region, or log destination present in deployment config but absent from the register's approved locations. Defeats: DET-INF-024. Bad: backups replicate to a second region enabled during a console session; the register still lists one region. Instead: the register is updated and approved before the config change ships (LG-026). Severity: BLOCK.
- **BAN-LG-014 — Derogation dressed as a standing safeguard.** Banned: relying on an Article 49 derogation for a recurring product flow while the privacy notice or register describes the flow as covered by SCCs or adequacy. Defeats: DET-CON-014. Bad: nightly analytics exports to a third-country tool run "on consent" as a standing design, while the notice lists SCCs as the mechanism. Instead: put the flow on a real mechanism or stop the flow; derogations stay per-transfer and documented (LG-031). Severity: BLOCK.
- **BAN-LG-015 — Stale register after a sub-processor change.** Banned: leaving register rows unchanged after a vendor's sub-processor change notice adds, removes, or relocates a sub-processor. Defeats: DET-CON-018. Bad: the vendor announces a new sub-processor processing in a new country; six months later the register still shows the old list, and the privacy notice with it. Instead: update the rows on the change notice and re-check every affected claim (LG-030). Severity: WARN.

## Gates

- **G-LG-011 — Config-vs-register region scan.** Verifies: LG-025, LG-026. Check (automated): extract every region setting from the deployment/IaC config (datastores, backup targets, log sinks, CDN) and diff against the register's approved locations, e.g. `grep -rhoE "region: [a-z0-9-]+" infra/ | sort -u` compared line-by-line with the register's location column. Pass: zero regions in config that are absent from the register. Fail: block deployment until the register or the config changes. Recorded in: progress.md.
- **G-LG-012 — Processor completeness check.** Verifies: LG-021, LG-022. Check (automated): list every third-party SDK and outbound third-party endpoint in the codebase/network manifest and assert each has a transfer-register row with a non-empty mechanism field. Pass: every integration maps to a row; no empty mechanism fields. Fail: block release; the unregistered integration is removed or registered first. Recorded in: progress.md.
- **G-LG-013 — Full inventory coverage audit.** Verifies: LG-025, LG-029. Check (automated): enumerate from config and vendor consoles every datastore, backup target, log sink, analytics tool, support tool, and remote-access location, each with its region, and diff the enumeration against the register. Pass: the enumeration and the register are identical sets. Fail: block shipment; each gap becomes a register row or a removed store. Recorded in: progress.md.
- **G-LG-014 — Mechanism documents on file.** Verifies: LG-023, LG-024. Check (manual): for every non-adequacy transfer row, open the stored signed DPA/SCCs, confirm the module matches the row's roles, and confirm a dated transfer impact assessment exists. Pass: documents present and matching for all such rows. Fail: block shipment of any feature using that processor. Recorded in: progress.md.
- **G-LG-015 — Residency claim provability review.** Verifies: LG-027, LG-028. Check (manual): grep all product copy and the privacy notice for residency wording ("stays in", "hosted in", "never leaves", region or country names) and trace each claim to register rows plus config evidence. Pass: every claim traces fully, including backups, logs, and support access. Fail: block publication; the claim is fixed or deleted. Recorded in: progress.md.

## Anti-patterns

- **Primary-region tunnel vision.** The app database sits in the approved region, so residency is declared done — while backups, logs, analytics, and the helpdesk quietly live elsewhere. Catch it by running the G-LG-013 enumeration before believing any residency statement, including your own.
- **Launch-day register.** The register is written once for launch and never touched again, while processors, sub-processors, and regions drift for a year. Catch it by checking the register's last-updated date against the vendor change-notice inbox before any release.
- **CDN invisibility.** Edge caching and edge logs are treated as "not storage", so a worldwide CDN never enters the inventory even though it processes personal data (request logs, IP addresses) at every point of presence. Catch it by listing the CDN as a processor with its log locations.
- **Failover amnesia.** Multi-region failover or a provider's default replication is enabled for reliability and forgotten; the second region is real residency from day one. Catch it by reading the datastore's replication settings, not just its primary region, during inventory.

## Examples

- [Example 1 — Analytics SDK added with no transfer mechanism](examples/example-1.md) — violates/corrects LG-022.
- [Example 2 — "Data never leaves the EU" vs. a US log sink](examples/example-2.md) — violates/corrects LG-027.
- [Example 3 — Backup region enabled in config, absent from the register](examples/example-3.md) — violates/corrects LG-026.

## Recall anchors

- A flow with no register row does not exist — register before you integrate.
- Adequacy first, SCCs second with an impact assessment, derogations never as architecture.
- Backups, logs, analytics, and support desks are residency too.
- If the claim can't be proven from the register and the config, delete the claim.
- Regions are the operator's recorded decision, never the builder's assumption.

## Checklist

- [ ] Every processor and sub-processor has a register row: data received, storage and processing locations, named mechanism (LG-021).
- [ ] No integration shipped before its register row existed (LG-022).
- [ ] SCC rows name the module and have the signed DPA/SCCs and a dated impact assessment on file (LG-024).
- [ ] Inventory covers backups, replicas, log sinks, analytics, support tools, and CDN behavior — each with a region (LG-025).
- [ ] Config-vs-register region scan (G-LG-011) and processor completeness check (G-LG-012) both pass.
- [ ] Every residency claim in copy and the privacy notice traced to register plus config evidence, or deleted (LG-027).
- [ ] Support-access locations registered as transfers (LG-029); sub-processor change notices actioned (LG-030).
