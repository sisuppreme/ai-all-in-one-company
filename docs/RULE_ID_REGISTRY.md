# Rule ID Registry

Owner: Forge. Every rule, gate, and BAN ID in the repo is assigned here before use (§5.4). IDs are unique repo-wide; renumbering is forbidden; a deprecated ID is retired, never reused.

Assignment scheme (DECISIONS D-012): within each department, skills in catalog order receive fixed blocks — **rules: 20 per skill** (`<CODE>-001` …), **gates: 10 per skill** (`G-<CODE>-001` …), **BAN entries: 10 per skill** (`BAN-<CODE>-001` …). A skill that exhausts its block requests a registry amendment in DECISIONS.md; it never borrows a neighbour's numbers.

## D1 — product-requirements (PR)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| discovery | PR-001–PR-020 | G-PR-001–PR-010 | BAN-PR-001–PR-010 |
| user-research | PR-021–PR-040 | G-PR-011–PR-020 | BAN-PR-011–PR-020 |
| personas-jtbd | PR-041–PR-060 | G-PR-021–PR-030 | BAN-PR-021–PR-030 |
| requirements-writing | PR-061–PR-080 | G-PR-031–PR-040 | BAN-PR-031–PR-040 |
| user-stories | PR-081–PR-100 | G-PR-041–PR-050 | BAN-PR-041–PR-050 |
| acceptance-criteria | PR-101–PR-120 | G-PR-051–PR-060 | BAN-PR-051–PR-060 |
| fact-sheet | PR-121–PR-140 | G-PR-061–PR-070 | BAN-PR-061–PR-070 |
| scope-control | PR-141–PR-160 | G-PR-071–PR-080 | BAN-PR-071–PR-080 |
| competitive-analysis | PR-161–PR-180 | G-PR-081–PR-090 | BAN-PR-081–PR-090 |
| product-metrics | PR-181–PR-200 | G-PR-091–PR-100 | BAN-PR-091–PR-100 |
| pricing-monetization | PR-201–PR-220 | G-PR-101–PR-110 | BAN-PR-101–PR-110 |
| unit-economics | PR-221–PR-240 | G-PR-111–PR-120 | BAN-PR-111–PR-120 |
| roadmapping | PR-241–PR-260 | G-PR-121–PR-130 | BAN-PR-121–PR-130 |
| market-expansion | PR-261–PR-280 | G-PR-131–PR-135 | BAN-PR-131–PR-136 |

## D2 — architecture (AR)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| system-design | AR-001–AR-020 | G-AR-001–AR-010 | BAN-AR-001–AR-010 |
| c4-diagrams | AR-021–AR-040 | G-AR-011–AR-020 | BAN-AR-011–AR-020 |
| stack-selection | AR-041–AR-060 | G-AR-021–AR-030 | BAN-AR-021–AR-030 |
| api-architecture | AR-061–AR-080 | G-AR-031–AR-040 | BAN-AR-031–AR-040 |
| api-versioning | AR-081–AR-100 | G-AR-041–AR-050 | BAN-AR-041–AR-050 |
| api-documentation | AR-101–AR-120 | G-AR-051–AR-060 | BAN-AR-051–AR-060 |
| api-paradigms | AR-121–AR-140 | G-AR-061–AR-070 | BAN-AR-061–AR-070 |
| data-architecture | AR-141–AR-160 | G-AR-071–AR-080 | BAN-AR-071–AR-080 |
| architecture-patterns | AR-161–AR-180 | G-AR-081–AR-090 | BAN-AR-081–AR-090 |
| multitenancy-saas | AR-181–AR-200 | G-AR-091–AR-100 | BAN-AR-091–AR-100 |
| event-driven | AR-201–AR-220 | G-AR-101–AR-110 | BAN-AR-101–AR-110 |
| domain-driven-design | AR-221–AR-240 | G-AR-111–AR-120 | BAN-AR-111–AR-120 |
| adr-writing | AR-241–AR-260 | G-AR-121–AR-130 | BAN-AR-121–AR-130 |
| saas-conversion | AR-261–AR-279 | G-AR-131–AR-136 | BAN-AR-131–AR-136 |

## D3 — frontend (FE)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| frontend-core | FE-001–FE-020 | G-FE-001–FE-010 | BAN-FE-001–FE-010 |
| design-system | FE-021–FE-040 | G-FE-011–FE-020 | BAN-FE-011–FE-020 |
| design-tokens | FE-041–FE-060 | G-FE-021–FE-030 | BAN-FE-021–FE-030 |
| component-library | FE-061–FE-080 | G-FE-031–FE-040 | BAN-FE-031–FE-040 |
| motion | FE-081–FE-100 | G-FE-041–FE-050 | BAN-FE-041–FE-050 |
| scroll-experiences | FE-101–FE-120 | G-FE-051–FE-060 | BAN-FE-051–FE-060 |
| layout-responsive | FE-121–FE-140 | G-FE-061–FE-070 | BAN-FE-061–FE-070 |
| typography | FE-141–FE-160 | G-FE-071–FE-080 | BAN-FE-071–FE-080 |
| ui-states | FE-161–FE-180 | G-FE-081–FE-090 | BAN-FE-081–FE-090 |
| frontend-state | FE-181–FE-200 | G-FE-091–FE-100 | BAN-FE-091–FE-100 |
| data-fetching | FE-201–FE-220 | G-FE-101–FE-110 | BAN-FE-101–FE-110 |
| client-routing | FE-221–FE-240 | G-FE-111–FE-120 | BAN-FE-111–FE-120 |
| forms | FE-241–FE-260 | G-FE-121–FE-130 | BAN-FE-121–FE-130 |
| data-visualisation | FE-261–FE-280 | G-FE-131–FE-140 | BAN-FE-131–FE-140 |
| pwa-offline | FE-281–FE-300 | G-FE-141–FE-150 | BAN-FE-141–FE-150 |
| webgl-3d | FE-301–FE-320 | G-FE-151–FE-160 | BAN-FE-151–FE-160 |
| design-intelligence | FE-321–FE-340 | G-FE-161–FE-170 | BAN-FE-161–FE-170 |
| theme-library | FE-341–FE-360 | G-FE-171–FE-180 | BAN-FE-171–FE-180 |
| ui-ux-upscaler | FE-361–FE-380 | G-FE-181–FE-190 | BAN-FE-181–FE-190 |

## D4 — backend (BE)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| api-building | BE-001–BE-020 | G-BE-001–BE-010 | BAN-BE-001–BE-010 |
| rest-conventions | BE-021–BE-040 | G-BE-011–BE-020 | BAN-BE-011–BE-020 |
| validation | BE-041–BE-060 | G-BE-021–BE-030 | BAN-BE-021–BE-030 |
| feature-flags | BE-061–BE-080 | G-BE-031–BE-040 | BAN-BE-031–BE-040 |
| sdk-design | BE-081–BE-100 | G-BE-041–BE-050 | BAN-BE-041–BE-050 |
| backend-auth | BE-101–BE-120 | G-BE-051–BE-060 | BAN-BE-051–BE-060 |
| rbac | BE-121–BE-140 | G-BE-061–BE-070 | BAN-BE-061–BE-070 |
| user-reporting | BE-141–BE-160 | G-BE-071–BE-080 | BAN-BE-071–BE-080 |
| admin-tools | BE-161–BE-180 | G-BE-081–BE-090 | BAN-BE-081–BE-090 |
| queues-jobs | BE-181–BE-200 | G-BE-091–BE-100 | BAN-BE-091–BE-100 |
| realtime | BE-201–BE-220 | G-BE-101–BE-110 | BAN-BE-101–BE-110 |
| file-uploads | BE-221–BE-240 | G-BE-111–BE-120 | BAN-BE-111–BE-120 |
| media-processing | BE-241–BE-260 | G-BE-121–BE-130 | BAN-BE-121–BE-130 |
| notifications | BE-261–BE-280 | G-BE-131–BE-140 | BAN-BE-131–BE-140 |
| error-handling | BE-281–BE-300 | G-BE-141–BE-150 | BAN-BE-141–BE-150 |
| rate-limiting | BE-301–BE-320 | G-BE-151–BE-160 | BAN-BE-151–BE-160 |

## D5 — database (DB)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| schema-design | DB-001–DB-020 | G-DB-001–DB-010 | BAN-DB-001–DB-010 |
| sql-fundamentals | DB-021–DB-040 | G-DB-011–DB-020 | BAN-DB-011–DB-020 |
| nosql-patterns | DB-041–DB-060 | G-DB-021–DB-030 | BAN-DB-021–DB-030 |
| seed-data | DB-061–DB-080 | G-DB-031–DB-040 | BAN-DB-031–DB-040 |
| transactions-concurrency | DB-081–DB-100 | G-DB-041–DB-050 | BAN-DB-041–DB-050 |
| tenant-isolation | DB-101–DB-120 | G-DB-051–DB-060 | BAN-DB-051–DB-060 |
| migrations | DB-121–DB-140 | G-DB-061–DB-070 | BAN-DB-061–DB-070 |
| query-performance | DB-141–DB-160 | G-DB-071–DB-080 | BAN-DB-071–DB-080 |
| indexing | DB-161–DB-180 | G-DB-081–DB-090 | BAN-DB-081–DB-090 |
| data-access | DB-181–DB-200 | G-DB-091–DB-100 | BAN-DB-091–DB-100 |
| backup-recovery | DB-201–DB-220 | G-DB-101–DB-110 | BAN-DB-101–DB-110 |
| read-replicas | DB-221–DB-240 | G-DB-111–DB-120 | BAN-DB-111–DB-120 |
| caching | DB-241–DB-260 | G-DB-121–DB-130 | BAN-DB-121–DB-130 |
| search-engines | DB-261–DB-280 | G-DB-131–DB-140 | BAN-DB-131–DB-140 |
| vector-db | DB-281–DB-300 | G-DB-141–DB-150 | BAN-DB-141–DB-150 |
| data-warehousing | DB-301–DB-320 | G-DB-151–DB-160 | BAN-DB-151–DB-160 |
| etl-pipelines | DB-321–DB-340 | G-DB-161–DB-170 | BAN-DB-161–DB-170 |
| data-ingestion | DB-341–DB-360 | G-DB-171–DB-180 | BAN-DB-171–DB-180 |
| pipeline-orchestration | DB-361–DB-380 | G-DB-181–DB-190 | BAN-DB-181–DB-190 |
| data-quality | DB-381–DB-400 | G-DB-191–DB-200 | BAN-DB-191–DB-200 |

## D6 — devops-deployment (DO)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| ci-cd | DO-001–DO-020 | G-DO-001–DO-010 | BAN-DO-001–DO-010 |
| preview-environments | DO-021–DO-040 | G-DO-011–DO-020 | BAN-DO-011–DO-020 |
| deployment-strategies | DO-041–DO-060 | G-DO-021–DO-030 | BAN-DO-021–DO-030 |
| containers | DO-061–DO-080 | G-DO-031–DO-040 | BAN-DO-031–DO-040 |
| kubernetes | DO-081–DO-100 | G-DO-041–DO-050 | BAN-DO-041–DO-050 |
| infrastructure-as-code | DO-101–DO-120 | G-DO-051–DO-060 | BAN-DO-051–DO-060 |
| servers-vps | DO-121–DO-140 | G-DO-061–DO-070 | BAN-DO-061–DO-070 |
| hosting | DO-141–DO-160 | G-DO-071–DO-080 | BAN-DO-071–DO-080 |
| free-tiers | DO-161–DO-180 | G-DO-081–DO-090 | BAN-DO-081–DO-090 |
| cdn-strategy | DO-181–DO-200 | G-DO-091–DO-100 | BAN-DO-091–DO-100 |
| domains-dns | DO-201–DO-220 | G-DO-101–DO-110 | BAN-DO-101–DO-110 |
| ssl-certificates | DO-221–DO-240 | G-DO-111–DO-120 | BAN-DO-111–DO-120 |
| scaling | DO-241–DO-260 | G-DO-121–DO-130 | BAN-DO-121–DO-130 |
| reliability | DO-261–DO-280 | G-DO-131–DO-140 | BAN-DO-131–DO-140 |
| incident-response | DO-281–DO-300 | G-DO-141–DO-150 | BAN-DO-141–DO-150 |
| rollback | DO-301–DO-320 | G-DO-151–DO-160 | BAN-DO-151–DO-160 |
| cloud-costs | DO-321–DO-340 | G-DO-161–DO-170 | BAN-DO-161–DO-170 |

## D7 — security (SE)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| owasp | SE-001–SE-020 | G-SE-001–SE-010 | BAN-SE-001–SE-010 |
| session-security | SE-021–SE-040 | G-SE-011–SE-020 | BAN-SE-011–SE-020 |
| api-security | SE-041–SE-060 | G-SE-021–SE-030 | BAN-SE-021–SE-030 |
| auth-hardening | SE-061–SE-080 | G-SE-031–SE-040 | BAN-SE-031–SE-040 |
| secrets-management | SE-081–SE-100 | G-SE-041–SE-050 | BAN-SE-041–SE-050 |
| dependency-safety | SE-101–SE-120 | G-SE-051–SE-060 | BAN-SE-051–SE-060 |
| supply-chain | SE-121–SE-140 | G-SE-061–SE-070 | BAN-SE-061–SE-070 |
| encryption | SE-141–SE-160 | G-SE-071–SE-080 | BAN-SE-071–SE-080 |
| security-headers | SE-161–SE-180 | G-SE-081–SE-090 | BAN-SE-081–SE-090 |
| threat-modelling | SE-181–SE-200 | G-SE-091–SE-100 | BAN-SE-091–SE-100 |
| security-audit | SE-201–SE-220 | G-SE-101–SE-110 | BAN-SE-101–SE-110 |
| penetration-testing | SE-221–SE-240 | G-SE-111–SE-120 | BAN-SE-111–SE-120 |
| pci-compliance | SE-241–SE-260 | G-SE-121–SE-130 | BAN-SE-121–SE-130 |
| content-moderation | SE-261–SE-280 | G-SE-131–SE-140 | BAN-SE-131–SE-140 |

## D8 — qa-testing (QA)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| unit-testing | QA-001–QA-020 | G-QA-001–QA-010 | BAN-QA-001–QA-010 |
| integration-testing | QA-021–QA-040 | G-QA-011–QA-020 | BAN-QA-011–QA-020 |
| e2e-testing | QA-041–QA-060 | G-QA-021–QA-030 | BAN-QA-021–QA-030 |
| browser-verification | QA-061–QA-080 | G-QA-031–QA-040 | BAN-QA-031–QA-040 |
| visual-regression | QA-081–QA-100 | G-QA-041–QA-050 | BAN-QA-041–QA-050 |
| accessibility-testing | QA-101–QA-120 | G-QA-051–QA-060 | BAN-QA-051–QA-060 |
| load-testing | QA-121–QA-140 | G-QA-061–QA-070 | BAN-QA-061–QA-070 |
| chaos-testing | QA-141–QA-160 | G-QA-071–QA-080 | BAN-QA-071–QA-080 |
| contract-testing | QA-161–QA-180 | G-QA-081–QA-090 | BAN-QA-081–QA-090 |
| security-testing | QA-181–QA-200 | G-QA-091–QA-100 | BAN-QA-091–QA-100 |
| test-strategy | QA-201–QA-220 | G-QA-101–QA-110 | BAN-QA-101–QA-110 |
| qa-gates | QA-221–QA-240 | G-QA-111–QA-120 | BAN-QA-111–QA-120 |
| test-data | QA-241–QA-260 | G-QA-121–QA-130 | BAN-QA-121–QA-130 |
| bug-triage | QA-261–QA-280 | G-QA-131–QA-140 | BAN-QA-131–QA-140 |
| placeholder-scan | QA-281–QA-300 | G-QA-141–QA-150 | BAN-QA-141–QA-150 |

## D9 — seo-content (CO)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| technical-seo | CO-001–CO-020 | G-CO-001–CO-010 | BAN-CO-001–CO-010 |
| on-page-seo | CO-021–CO-040 | G-CO-011–CO-020 | BAN-CO-011–CO-020 |
| aeo | CO-041–CO-060 | G-CO-021–CO-030 | BAN-CO-021–CO-030 |
| geo | CO-061–CO-080 | G-CO-031–CO-040 | BAN-CO-031–CO-040 |
| content-strategy | CO-081–CO-100 | G-CO-041–CO-050 | BAN-CO-041–CO-050 |
| copywriting | CO-101–CO-120 | G-CO-051–CO-060 | BAN-CO-051–CO-060 |
| real-content | CO-121–CO-140 | G-CO-061–CO-070 | BAN-CO-061–CO-070 |
| lifecycle-email | CO-141–CO-160 | G-CO-071–CO-080 | BAN-CO-071–CO-080 |
| structured-data | CO-161–CO-180 | G-CO-081–CO-090 | BAN-CO-081–CO-090 |
| sitemaps | CO-181–CO-200 | G-CO-091–CO-100 | BAN-CO-091–CO-100 |
| internal-linking | CO-201–CO-220 | G-CO-101–CO-110 | BAN-CO-101–CO-110 |
| social-open-graph | CO-221–CO-240 | G-CO-111–CO-120 | BAN-CO-111–CO-120 |
| web-analytics | CO-241–CO-260 | G-CO-121–CO-130 | BAN-CO-121–CO-130 |
| growth-experiments | CO-261–CO-280 | G-CO-131–CO-140 | BAN-CO-131–CO-140 |
| seo-migration | CO-281–CO-292 | G-CO-141–CO-145 | BAN-CO-141–CO-146 |

## D10 — project-memory (PM)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| project-templates | PM-001–PM-020 | G-PM-001–PM-010 | BAN-PM-001–PM-010 |
| documentation-writing | PM-021–PM-040 | G-PM-011–PM-020 | BAN-PM-011–PM-020 |
| readme-writing | PM-041–PM-060 | G-PM-021–PM-030 | BAN-PM-021–PM-030 |
| runbook-writing | PM-061–PM-080 | G-PM-031–PM-040 | BAN-PM-031–PM-040 |
| postmortem-writing | PM-081–PM-100 | G-PM-041–PM-050 | BAN-PM-041–PM-050 |
| decision-logs | PM-101–PM-120 | G-PM-051–PM-060 | BAN-PM-051–PM-060 |
| changelog | PM-121–PM-140 | G-PM-061–PM-070 | BAN-PM-061–PM-070 |
| progress-tracking | PM-141–PM-160 | G-PM-071–PM-080 | BAN-PM-071–PM-080 |
| memory-retrieval | PM-161–PM-180 | G-PM-081–PM-090 | BAN-PM-081–PM-090 |
| handover | PM-181–PM-200 | G-PM-091–PM-100 | BAN-PM-091–PM-100 |

## D11 — integrations-payments (IN)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| payments | IN-001–IN-020 | G-IN-001–IN-010 | BAN-IN-001–IN-010 |
| subscriptions | IN-021–IN-040 | G-IN-011–IN-020 | BAN-IN-011–IN-020 |
| refunds-disputes | IN-041–IN-060 | G-IN-021–IN-030 | BAN-IN-021–IN-030 |
| invoicing-tax | IN-061–IN-080 | G-IN-031–IN-040 | BAN-IN-031–IN-040 |
| dunning | IN-081–IN-100 | G-IN-041–IN-050 | BAN-IN-041–IN-050 |
| webhooks | IN-101–IN-120 | G-IN-051–IN-060 | BAN-IN-051–IN-060 |
| transactional-email | IN-121–IN-140 | G-IN-061–IN-070 | BAN-IN-061–IN-070 |
| sms | IN-141–IN-160 | G-IN-071–IN-080 | BAN-IN-071–IN-080 |
| oauth-sso | IN-161–IN-180 | G-IN-081–IN-090 | BAN-IN-081–IN-090 |
| third-party-apis | IN-181–IN-200 | G-IN-091–IN-100 | BAN-IN-091–IN-100 |
| api-keys-management | IN-201–IN-220 | G-IN-101–IN-110 | BAN-IN-101–IN-110 |
| sdk-embeddables | IN-221–IN-240 | G-IN-111–IN-120 | BAN-IN-111–IN-120 |

## D12 — analytics-observability (AN)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| product-analytics | AN-001–AN-020 | G-AN-001–AN-010 | BAN-AN-001–AN-010 |
| event-tracking | AN-021–AN-040 | G-AN-011–AN-020 | BAN-AN-011–AN-020 |
| experimentation-platform | AN-041–AN-060 | G-AN-021–AN-030 | BAN-AN-021–AN-030 |
| revenue-analytics | AN-061–AN-080 | G-AN-031–AN-040 | BAN-AN-031–AN-040 |
| logging | AN-081–AN-100 | G-AN-041–AN-050 | BAN-AN-041–AN-050 |
| monitoring | AN-101–AN-120 | G-AN-051–AN-060 | BAN-AN-051–AN-060 |
| alerting | AN-121–AN-140 | G-AN-061–AN-070 | BAN-AN-061–AN-070 |
| dashboards | AN-141–AN-160 | G-AN-071–AN-080 | BAN-AN-071–AN-080 |
| error-tracking | AN-161–AN-180 | G-AN-081–AN-090 | BAN-AN-081–AN-090 |
| apm | AN-181–AN-200 | G-AN-091–AN-100 | BAN-AN-091–AN-100 |
| performance-budgets | AN-201–AN-220 | G-AN-101–AN-110 | BAN-AN-101–AN-110 |
| core-web-vitals | AN-221–AN-240 | G-AN-111–AN-120 | BAN-AN-111–AN-120 |
| performance-optimization | AN-241–AN-260 | G-AN-121–AN-130 | BAN-AN-121–AN-130 |

## D13 — accessibility-i18n (AC)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| accessibility-audit | AC-001–AC-020 | G-AC-001–AC-010 | BAN-AC-001–AC-010 |
| wcag | AC-021–AC-040 | G-AC-011–AC-020 | BAN-AC-011–AC-020 |
| screen-readers | AC-041–AC-060 | G-AC-021–AC-030 | BAN-AC-021–AC-030 |
| accessibility-law | AC-061–AC-080 | G-AC-031–AC-040 | BAN-AC-031–AC-040 |
| keyboard-accessibility | AC-081–AC-100 | G-AC-041–AC-050 | BAN-AC-041–AC-050 |
| reduced-motion | AC-101–AC-120 | G-AC-051–AC-060 | BAN-AC-051–AC-060 |
| internationalization | AC-121–AC-140 | G-AC-061–AC-070 | BAN-AC-061–AC-070 |
| localization-workflow | AC-141–AC-160 | G-AC-071–AC-080 | BAN-AC-071–AC-080 |
| rtl-layouts | AC-161–AC-180 | G-AC-081–AC-090 | BAN-AC-081–AC-090 |
| inclusive-copy | AC-181–AC-200 | G-AC-091–AC-100 | BAN-AC-091–AC-100 |

## D14 — legal-privacy (LG)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| privacy-laws | LG-001–LG-020 | G-LG-001–LG-010 | BAN-LG-001–LG-010 |
| data-residency | LG-021–LG-040 | G-LG-011–LG-020 | BAN-LG-011–LG-020 |
| dsar-handling | LG-041–LG-060 | G-LG-021–LG-030 | BAN-LG-021–LG-030 |
| legal-documents | LG-061–LG-080 | G-LG-031–LG-040 | BAN-LG-031–LG-040 |
| cookie-consent | LG-081–LG-100 | G-LG-041–LG-050 | BAN-LG-041–LG-050 |
| licensing | LG-101–LG-120 | G-LG-051–LG-060 | BAN-LG-051–LG-060 |
| compliance-audit | LG-121–LG-140 | G-LG-061–LG-070 | BAN-LG-061–LG-070 |
| age-requirements | LG-141–LG-160 | G-LG-071–LG-080 | BAN-LG-071–LG-080 |
| audit-trails | LG-161–LG-180 | G-LG-081–LG-090 | BAN-LG-081–LG-090 |
| clone-ethics | LG-181–LG-200 | G-LG-091–LG-100 | BAN-LG-091–LG-100 |

## D15 — developer-experience (DX)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| dev-environment | DX-001–DX-020 | G-DX-001–DX-010 | BAN-DX-001–DX-010 |
| monorepo-tooling | DX-021–DX-040 | G-DX-011–DX-020 | BAN-DX-011–DX-020 |
| code-generation | DX-041–DX-060 | G-DX-021–DX-030 | BAN-DX-021–DX-030 |
| dependency-management | DX-061–DX-080 | G-DX-031–DX-040 | BAN-DX-031–DX-040 |
| tech-debt | DX-081–DX-100 | G-DX-041–DX-050 | BAN-DX-041–DX-050 |
| refactoring | DX-101–DX-120 | G-DX-051–DX-060 | BAN-DX-051–DX-060 |
| legacy-migration | DX-121–DX-140 | G-DX-061–DX-070 | BAN-DX-061–DX-070 |
| versioning | DX-141–DX-160 | G-DX-071–DX-080 | BAN-DX-071–DX-080 |
| prototype-hardening | DX-161–DX-177 | G-DX-081–DX-086 | BAN-DX-081–DX-088 |
| project-takeover | DX-181–DX-192 | G-DX-091–DX-095 | BAN-DX-091–DX-095 |

## D16 — cloning-replication (CL)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| site-discovery | CL-001–CL-020 | G-CL-001–CL-010 | BAN-CL-001–CL-010 |
| page-inventory | CL-021–CL-040 | G-CL-011–CL-020 | BAN-CL-011–CL-020 |
| design-extraction | CL-041–CL-060 | G-CL-021–CL-030 | BAN-CL-021–CL-030 |
| asset-harvesting | CL-061–CL-080 | G-CL-031–CL-040 | BAN-CL-031–CL-040 |
| behavior-cloning | CL-081–CL-100 | G-CL-041–CL-050 | BAN-CL-041–CL-050 |
| page-reconstruction | CL-101–CL-120 | G-CL-051–CL-060 | BAN-CL-051–CL-060 |
| fidelity-verification | CL-121–CL-140 | G-CL-061–CL-070 | BAN-CL-061–CL-070 |
| clone-redesign | CL-141–CL-154 | G-CL-071–CL-076 | BAN-CL-071–CL-075 |
| rebrand-execution | CL-701–CL-716 | G-CL-701–CL-705 | BAN-CL-701–CL-707 |

## D17 — ai-features (AI)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| llm-integration | AI-001–AI-020 | G-AI-001–AI-010 | BAN-AI-001–AI-010 |
| prompt-engineering | AI-021–AI-040 | G-AI-011–AI-020 | BAN-AI-011–AI-020 |
| ai-safety | AI-041–AI-060 | G-AI-021–AI-030 | BAN-AI-021–AI-030 |
| rag-retrieval | AI-061–AI-080 | G-AI-031–AI-040 | BAN-AI-031–AI-040 |
| embeddings-search | AI-081–AI-100 | G-AI-041–AI-050 | BAN-AI-041–AI-050 |
| recommendations | AI-101–AI-120 | G-AI-051–AI-060 | BAN-AI-051–AI-060 |
| search-relevance | AI-121–AI-140 | G-AI-061–AI-070 | BAN-AI-061–AI-070 |
| ai-evaluation | AI-141–AI-160 | G-AI-071–AI-080 | BAN-AI-071–AI-080 |
| ai-observability | AI-161–AI-180 | G-AI-081–AI-090 | BAN-AI-081–AI-090 |
| ai-cost-control | AI-181–AI-200 | G-AI-091–AI-100 | BAN-AI-091–AI-100 |
| ai-retrofit | AI-201–AI-212 | G-AI-101–AI-105 | BAN-AI-101–AI-105 |

## D18 — customer-experience (CX)

| Skill | Rules | Gates | BAN entries |
|---|---|---|---|
| support-ticketing | CX-001–CX-020 | G-CX-001–CX-010 | BAN-CX-001–CX-010 |
| in-app-chat | CX-021–CX-040 | G-CX-011–CX-020 | BAN-CX-011–CX-020 |
| help-center | CX-041–CX-060 | G-CX-021–CX-030 | BAN-CX-021–CX-030 |
| user-onboarding | CX-061–CX-080 | G-CX-031–CX-040 | BAN-CX-031–CX-040 |
| activation-metrics | CX-081–CX-100 | G-CX-041–CX-050 | BAN-CX-041–CX-050 |
| trial-conversion | CX-101–CX-120 | G-CX-051–CX-060 | BAN-CX-051–CX-060 |
| feedback-loops | CX-121–CX-140 | G-CX-061–CX-070 | BAN-CX-061–CX-070 |
| churn-prevention | CX-141–CX-160 | G-CX-071–CX-080 | BAN-CX-071–CX-080 |
| status-communications | CX-161–CX-180 | G-CX-081–CX-090 | BAN-CX-081–CX-090 |
