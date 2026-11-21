# DEFECT_TAXONOMY.md — Defect classes P0 / P1 / P2 (QB-01)

The defect taxonomy that Quality Bar QB-01 measures against. Every defect found in a sample project or a delivered build is filed at exactly one class below, counted per project in `docs/METRICS.md`, and dispositioned by the ship rules at the end of this file.

> **Source and reconciliation.** The class definitions are the Master Brief's QB-01 text (§6, quality bars) verbatim in substance: *P0 = security/data-loss/crash, P1 = broken feature or gate failure, P2 = cosmetic/copy.* The brief governs. The repo's `qa-gates` skill does not restate these classes; it speaks of "blocker defects" (e.g. QA-226: a gate that reports green on its own seeded fault "is filed as a blocker defect against the gate itself"). That wording describes the defect's **release effect** — it blocks the release — not a separate class: under this taxonomy a gate failure is P1, including a non-biting gate. Two neighboring vocabularies are mapped, not merged, in the table at the end: DET parameter severities (blocker / major / minor) and the inherited QA protocol's failure classes (BLOCKER / MAJOR / MINOR in `gates/QA_PROTOCOL_GATES.md`).

## P0 — Critical

**Definition (QB-01): a security defect, data loss, or a crash.**

A defect is P0 when any of these holds:

- **Security:** an attacker or an unauthorized user can read, modify, or delete data they should not reach; authentication or authorization is bypassable; secrets are exposed in client code, logs, screenshots, or reports. (Undisclosed simulated functionality that defeats a security check — e.g. a login that accepts any password, DET-FAKE-001 — is a security defect and files here, not at its DET severity.)
- **Data loss:** user data is destroyed, corrupted, silently overwritten, or rendered unrecoverable by a normal user action or a routine deploy; a delete, migration, or sync removes more than it was asked to.
- **Crash:** the application, a page, or a core flow crashes, white-screens, or hard-fails for a class of users under normal use (not a single malformed input the UI already rejects).

**Ship rule:** zero P0 defects in anything that ships. A P0 found after shipping is fixed and re-verified before the project is presented again.

## P1 — Major

**Definition (QB-01): a broken feature or a gate failure.**

A defect is P1 when any of these holds:

- **Broken feature:** a feature the project claims does not do what it promises — a form that submits nowhere (DET-FAKE-015), a checkout that confirms without charging (DET-FAKE-006), a dashboard rendering frozen fixture numbers (DET-FAKE-004), a dead primary control (G-QA-04). Fabricated content shipped as real — invented testimonials, statistics, reviews, people (DET-CON-010…013, DET-FAKE-014) — is a broken feature under the Real Content Rule and files here (it becomes P0 only if it is also a security, data-loss, or crash defect).
- **Gate failure:** any mandatory gate in `gates/ACCEPTANCE_GATES.md` fails, any `qa-gates` required check fails, or a gate is discovered to be non-biting (green on its own seeded fault — qa-gates QA-226 files this as a "blocker defect against the gate"; its class here is P1, and its release effect is that the release blocks until the gate bites again).

**Ship rule:** zero P1 defects in sample projects. Every P1 is fixed and re-tested (VERIFIED) or listed in the delivery report with severity, reproduction steps, and the recommended next step (checklist item A-12).

## P2 — Minor

**Definition (QB-01): cosmetic or copy.**

A defect is P2 when it neither breaks a feature nor fails a gate and causes no security, data-loss, or crash harm: a copy error or inconsistency, a cosmetic misalignment that passes the visual gates, an off-tone string, a minor wording or punctuation fault, a non-blocking visual imperfection a reviewer notices but no gate measures.

**Ship rule:** P2 defects may ship only when **logged with a fix date** (QB-01). An unlogged P2 is treated as unfiled work, not as an accepted defect. (The inherited QA protocol's regression rule — max 3 open MINOR, `gates/QA_PROTOCOL_GATES.md` — applies to skill-release QA runs; the QB-01 log-with-a-fix-date rule governs project defects.)

## Vocabulary mapping (map, never merge)

| Source vocabulary | Maps to | Rule |
|---|---|---|
| DET parameter severity "blocker" | P0 or P1 | Classify by the defect's nature, not the label: security / data-loss / crash → P0; everything else (broken feature, fabrication, fake functionality) → P1. |
| DET parameter severity "major" | P1 | Unless the instance is cosmetic in effect, in which case P2 with the reason recorded. |
| DET parameter severity "minor" | P2 | Unless the instance fails a gate, in which case P1 (gate failure governs). |
| qa-gates "blocker defect" | P1 | "Blocker" there names the release effect. The release blocks; the class is P1 (gate failure), or P0 if the underlying defect is security / data-loss / crash. |
| QA protocol failure class BLOCKER | P0 or P1 | Same nature rule as DET "blocker". |
| QA protocol failure class MAJOR | P1 | — |
| QA protocol failure class MINOR | P2 | Max 3 open in a skill-release QA run; project P2s follow the log-with-a-fix-date rule above. |

## Counting

Defect counts are recorded per sample project, by class, in `docs/METRICS.md` (value, definition, measurement method — the brief's fixed metric set includes "QA defect counts by severity per the QB-01 taxonomy, per sample project"). "Zero-defect" (QB-01) is a **target measured against this taxonomy**, not a claim that undetected defects cannot exist.
