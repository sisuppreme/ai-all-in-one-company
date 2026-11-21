# infrastructure-as-code

## Metadata

- **Owner department:** D6 DevOps & Deployment (DO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developer.hashicorp.com/terraform/language ; https://developer.hashicorp.com/terraform/language/state
- **Depends on:** none — standalone: authored from the infrastructure the project needs and the live cloud state, inspected directly; it is the record, not a consumer of another skill's output. Feeds ci-cd, deployment-strategies, kubernetes, hosting, cloud-costs.
- **Feeds into:** ci-cd, deployment-strategies, kubernetes, hosting, cloud-costs

## When to use / Do NOT use

- **Use when:** creating, changing, or auditing any durable infrastructure — compute, network, load balancers, DNS, storage, IAM — or when a project has console-built infrastructure with no code record.
- **Do NOT use when:** the change is application code or data (use the owning D4/D5 skill); for a fully managed platform, apply this skill to the platform's committed config files, which are its IaC of record.

## Rules

1. **DO-101 — Everything durable is declared.** All durable infrastructure (compute, network, DNS, storage, IAM) is declared in code — Terraform, Pulumi, CloudFormation, or a managed platform's committed config files — in the project repo or a named companion deployment repo; nothing durable exists only in a console.
2. **DO-102 — Plan before apply.** Every change follows change → `plan` output attached to the PR showing exactly what will be created, modified, or destroyed → review → apply from CI; no change is applied without a reviewed plan.
3. **DO-103 — Remote, locked state.** State is stored remotely with locking and access control; local state files are never the source of truth for a shared environment.
4. **DO-104 — State is never hand-edited or committed with secrets.** State files are never edited by hand, never committed to version control containing credentials, and are themselves backed up so a lost state file does not orphan the infrastructure.
5. **DO-105 — Drift is a fail.** A scheduled or PR-triggered read-only `plan` against live state that reports changes nobody proposed is a failed check and a finding to resolve, not a curiosity to note and ignore.
6. **DO-106 — Console changes are emergencies.** A change made directly in a console is permitted only to stop an active incident and is back-ported into code the same day, with the back-port verified by a clean plan.
7. **DO-107 — Modules stamped per environment.** Environments are stamped from the same versioned modules with different variable values; per-environment copy-paste forks of the same resources are not maintained.
8. **DO-108 — Check before declaring "no IaC."** Before recording that a project has no IaC, check companion deployment repos and non-Terraform declarative systems (orchestration manifests, provisioning playbooks, platform config files); the test is declaration plus convergent application, not the tool brand.
9. **DO-109 — Destroy is a reviewed operation.** `destroy` and any plan containing resource deletions pass the same plan-and-review gate as creation, with the deletion list read line by line before approval.
10. **DO-110 — Providers and modules are pinned.** Provider and module versions are pinned to exact versions in the configuration; unpinned sources that float to latest on the next init are not used for shared environments.
11. **DO-111 — Fresh-environment build is proven.** The code can build a working environment from empty: applying it into a fresh account or namespace and passing smoke checks is demonstrated at least once per major module change.

## BAN list

- **BAN-DO-051 — Console-only infrastructure.** Banned: durable servers, networks, or DNS created by clicking in a console with no corresponding declaration in code. Defeats: DET-INF-024. Bad: the production VPC and its security groups exist only in the account owner's console session; nobody can reproduce or audit them. Instead: declare the resources in Terraform (or the platform's committed config) and import the existing resources so plan converges. Severity: BLOCK.
- **BAN-DO-052 — Generated-but-never-applied IaC.** Banned: shipping a generated `main.tf` that was never planned or applied while the real environment was hand-built separately. Defeats: DET-INF-024. Bad: the repo's Terraform describes the demo stack; production was built by hand and has diverged silently for months. Instead: run `plan` against the real environment, import or reconcile every difference, and apply from CI so the code and the environment are the same thing. Severity: BLOCK.
- **BAN-DO-053 — State committed with secrets.** Banned: committing a state file (or any IaC artifact) containing credentials or secret attribute values to version control. Defeats: DET-INF-005. Bad: `terraform.tfstate` with plaintext database passwords is pushed to the project repo. Instead: move state to a remote, access-controlled backend, add state files to `.gitignore`, and rotate every secret the committed file exposed. Severity: BLOCK.
- **BAN-DO-054 — Unexplained drift waved through.** Banned: seeing a non-empty unscheduled `plan` and applying or ignoring it without identifying what changed and why. Defeats: DET-INF-024. Bad: the nightly plan shows a security group rule nobody added; the team applies anyway to "make it green." Instead: stop, identify the out-of-band change from the plan diff, and either back-port it into code the same day or revert it through code. Severity: BLOCK.

## Gates

- **G-DO-051 — Drift check.** Verifies: DO-105, DO-106. Check: CI runs `terraform plan -detailed-exitcode` (read-only) on every infrastructure PR and on a nightly schedule. Pass: exit code 0 (no changes) or the plan diff matches the PR's stated intent exactly. Fail: block the change and open a drift finding. Recorded in: progress.md.
- **G-DO-052 — No state or secrets in the repo.** Verifies: DO-103, DO-104. Check: `git ls-files | grep -E '\.tfstate' ; grep -rn 'password\|secret_key' --include='*.tfstate' .` returns nothing, and the backend configuration block names a remote backend with locking. Pass: no state files tracked and a remote locked backend is configured. Fail: block shipment until state is migrated and exposed secrets are rotated. Recorded in: progress.md.
- **G-DO-053 — Fresh-environment build test.** Verifies: DO-101, DO-111. Check: apply the code into an empty account or namespace (`terraform apply` in the sandbox target), then run the project's smoke checks against the new environment. Pass: apply completes with no manual console steps and smoke checks pass. Fail: block release of the module change. Recorded in: progress.md.
- **G-DO-054 — Declaration coverage review.** Verifies: DO-101, DO-108. Check: list the live environment's durable resources from the provider console/API and reconcile the list against the code and any companion deployment repo, item by item. Pass: every durable resource traces to a declaration. Fail: block shipment; undeclared resources are imported or removed. Recorded in: progress.md.

## Anti-patterns

- **Tutorial-shaped infrastructure.** The configuration is a copied provider tutorial with the tutorial's example names, CIDR blocks, and placeholder values still in it; catch it by searching for example values and resources nobody on the project can explain.
- **One mega-module.** Every resource for every environment lives in a single root module with hundreds of resources, so every plan is unreadable and every apply touches everything; catch it when a one-line change produces a plan nobody can review.
- **Variables in name only.** A module claims to be reusable but hardcodes region, instance size, and names in the resource bodies, so "stamping a new environment" means editing the module; catch it by diffing what a second environment would actually change.
- **Import-and-forget.** Existing resources were imported once to make the first plan green, but the generated configuration was never cleaned up or reviewed, so the code records attributes nobody chose; catch it by reading imported blocks for provider-default filler.

## Examples

- [Example 1 — Console-built network declared and imported](examples/example-1.md) — violates/corrects DO-101.
- [Example 2 — Drift found and back-ported](examples/example-2.md) — violates/corrects DO-105.
- [Example 3 — State moved to a remote locked backend](examples/example-3.md) — violates/corrects DO-103.

## Recall anchors

- If it is not in code, it does not exist — it is a rumor with an IP address.
- Plan is the review; apply is just the signature.
- Drift is a finding, never a shrug.
- Console changes are emergencies: back-port the same day or revert.
- State is the map to everything — remote, locked, backed up, never hand-edited.

## Checklist

- [ ] Every durable resource in the live environment traces to a declaration in code (DO-101, G-DO-054).
- [ ] The latest change shipped with a reviewed `plan` attached to its PR (DO-102).
- [ ] State is remote, locked, access-controlled, and backed up; no state file is tracked in the repo (DO-103, DO-104, G-DO-052).
- [ ] The most recent scheduled drift check is clean or its findings are resolved (DO-105, G-DO-051).
- [ ] Any console change from an incident was back-ported the same day (DO-106).
- [ ] All environments are stamped from the same versioned modules with different variables (DO-107).
- [ ] Provider and module versions are pinned exactly (DO-110).
