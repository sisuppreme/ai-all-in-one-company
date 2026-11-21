# <skill-name>

<!-- SKILL_TEMPLATE.md — the mandatory §5.4 format. Every SKILL.md follows this section order exactly. Delete these comments in a real skill. -->

## Metadata

- **Owner department:** <D-code and name, e.g. D1 Product & Requirements (PR)>
- **Skill version:** 1.0.0
- **Last verified:** <YYYY-MM-DD — the date the tool/API claims below were checked against the listed sources>
- **Sources:** <real URLs for every tool/API/standard claim in this skill; no claim without a source>
- **Depends on:** <skill names this skill needs loaded first, or "none">
- **Feeds into:** <skill names that consume this skill's output>

<!-- Semantics: Depends on = consumes inputs from; Feeds into = outputs consumed by; cycles are permitted between co-evolving skills and carry no execution-order meaning. -->

## When to use / Do NOT use

- **Use when:** <the concrete situations that call for this skill>
- **Do NOT use when:** <situations where another skill or no skill applies, and which one instead>

## Rules

<!-- Numbered rules, each with its registry ID: <CODE>-<NNN> from this skill's block in docs/RULE_ID_REGISTRY.md. A rule is one verifiable instruction — if a gate cannot check it, rewrite it. -->

1. **<CODE>-001 — <Rule name>.** <The rule, stated so a single agent can follow and check it.>

## BAN list

<!-- Hard prohibitions. Each entry: ID BAN-<CODE>-<NNN> from this skill's block; the banned pattern in one line; the DET parameter it defeats; a bad example; the correct replacement; severity BLOCK (gate fails) or WARN (flag for review). An item lives here OR in Anti-patterns, never both. DET citation honesty (Phase 4 convention): cite a DET parameter only when its defined signal semantically matches the banned pattern. Where no DET parameter names the signal, write "Defeats: DET-NONE — no DET parameter names this signal; governed by <rule IDs>" — never cite a nearest-match parameter as if it were exact. -->

- **BAN-<CODE>-001 — <Pattern name>.** Banned: <the pattern, one line>. Defeats: DET-<FAMILY>-<NNN>. Bad: <concrete bad example>. Instead: <the correct replacement>. Severity: BLOCK.

## Gates

<!-- ≥3 gates, ≥1 automated where the domain permits. Each gate: ID G-<CODE>-<NNN> from this skill's block; the rule IDs it verifies; the exact check (command / grep / manual step / browser verification); pass criterion; fail action; result recorded in the project's progress.md. -->

- **G-<CODE>-001 — <Gate name>.** Verifies: <CODE>-001. Check: <exact check>. Pass: <criterion>. Fail: <block shipment / warn>. Recorded in: progress.md.

## Anti-patterns

<!-- Failure modes to recognise in your own draft output; a hit triggers rework, not an automatic gate fail. Nothing here may duplicate a BAN entry. -->

- **<Anti-pattern name>.** <What it looks like, and how to catch it in your own output before anyone else does.>

## Examples

<!-- ≥3 before/after pairs, one per major rule cluster. The full pairs live in this skill's examples/ folder (one file per pair: slop version, correct version, one-line note naming the rule violated). List them here with their rule links. -->

- [Example 1 — <title>](examples/example-1.md) — violates/corrects <CODE>-001.

## Recall anchors

<!-- ≤5 one-line reminders an agent can hold in mind mid-task. -->

- <Anchor 1.>

## Checklist

<!-- The pre-ship self-check for this skill's work. Every box must be honestly checkable. -->

- [ ] <Check 1 — tied to a rule or gate above.>
