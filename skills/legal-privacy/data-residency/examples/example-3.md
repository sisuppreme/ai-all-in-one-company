# Example 3 — Backup region enabled in config, absent from the register

## Before

During an incident, an engineer enables cross-region backup replication to a second cloud region from the provider console, to protect against data loss. The change works and is forgotten.

The transfer register still lists exactly one approved location. The privacy notice, generated from the register, says backups are kept in that one region. For months, backup copies of all personal data sit in a country the register has never assessed and no mechanism covers.

## After

The G-LG-011 config-vs-register scan flags the second region at the next deployment review. The team makes the decision properly, as an operator decision recorded with its source and date:

1. The residency commitment is reviewed: the second region is in a country with no adequacy decision, and no SCC/impact-assessment work exists for a backup flow.
2. The operator decides the backups stay in the approved region; replication is reconfigured to a second availability zone inside it instead.
3. The register is updated to record the decision, and the console change is replaced by a config change in version control so the scan can see it.

*Corrects LG-026 (config matches the register; the register leads) and LG-028 (region choices are operator decisions recorded with a source, never assumed by the builder).*
