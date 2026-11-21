# PROJECT_ANATOMY.md — The complete anatomy of a professional web project

Purpose: the map every department works from (MASTER_BRIEF.md §4). Every element of a professional web project, researched on eight dimensions — what it is, how it works, why it exists, what happens if it is missing, what good looks like, what AI slop looks like, how to verify it, and the source for those claims — plus the departments that own it and the skills that serve it. Audience: every department, squad, and the single agent who will run this company end-to-end.

How to use: before any project step, find the element you are about to produce here; its Verify line is the check your output must pass, and its Slop line is what the detection squads will flag.

Coverage: 127 elements in 12 parts. Traceability gate (Phase 0 exit): all 227 catalog skills trace to at least one element, and every element names at least one serving skill — verified by script over the element files (method in METRICS.md). Project-file set and playbook-set research: Appendices A and B.


## Part 1 — Product & requirements

## Requirements
- **What:** The agreed, written statements of what a system must do and the constraints it must respect. They are the contract between the people who need the product and the people who build it.
- **How it works:** Teams elicit needs from stakeholders, write each requirement as a single, testable statement, attach attributes (source, priority, rationale), and keep bidirectional traceability from stakeholder need to design, code, and test. Changes go through review, not hallway edits.
- **Why it exists:** It converts vague intent into something buildable, estimable, and verifiable, and gives every later argument a shared reference point.
- **If missing:** Each person builds from a private mental model. Disagreements surface at delivery, when rework is most expensive, and "done" becomes a matter of opinion.
- **Good looks like:** ISO/IEC/IEEE 29148:2018, the international requirements engineering standard, which defines characteristics of a well-formed requirement: necessary, unambiguous, singular, feasible, and verifiable.
- **Slop looks like:** A plausible-sounding list of generic features ("user management, dashboard, notifications") with no source, no priority, and no way to test any item — written once and never traced to anything.
- **Verify:** Pick five requirements at random; for each, confirm a named stakeholder source, a priority, and at least one linked test or acceptance check. Any requirement failing all three is not real.
- **Source:** ISO/IEC/IEEE 29148 tutorial and standard overview, https://www.xopsschool.com/mod/page/view.php?id=3365
- **Owning departments:** D1, D10
- **Skills that serve it:** discovery, requirements-writing

## User stories
- **What:** A short statement of a need from the perspective of the person who has it: "As a [role], I want [capability], so that [benefit]." The written card is a reminder to have a conversation, not a full specification.
- **How it works:** Stories are drafted in workshops with users and builders, kept small enough to finish in one iteration, and refined as work approaches. Ron Jeffries' "card, conversation, confirmation" pattern applies: the card prompts the talk, and confirmation comes from acceptance checks.
- **Why it exists:** Stories keep the user's goal — especially the "so that" benefit — visible during implementation, so the team can propose better ways to reach the same outcome.
- **If missing:** Work is specified as technical tasks ("build the endpoint"), and nobody can say who benefits or whether the result mattered. Features ship complete and unused.
- **Good looks like:** Mike Cohn's guidance at Mountain Goat Software: judge stories with Bill Wake's INVEST test — Independent, Negotiable, Valuable, Estimable, Small, Testable — used as a diagnostic, not a score.
- **Slop looks like:** Template-shaped filler with interchangeable roles ("As a user, I want a seamless experience") or stories that are really disguised tasks, with no benefit clause and nothing testable.
- **Verify:** Read each story aloud and ask who benefits, why now, and what is out of scope. Then check it against INVEST; a story that is not testable or not valuable goes back for refinement.
- **Source:** Mountain Goat Software, "What Makes a Good User Story?", https://www.mountaingoatsoftware.com/agile/user-stories/good-user-stories
- **Owning departments:** D1
- **Skills that serve it:** user-stories, personas-jtbd

## Acceptance criteria
- **What:** The concrete, observable conditions a story or requirement must satisfy before the requester accepts it as done. They define the boundary of "finished" before work starts.
- **How it works:** Product, engineering, and QA write the criteria together, often as scenarios in Gherkin form — Given a context, When an action happens, Then an observable outcome. Those scenarios double as automated acceptance tests in tools such as Cucumber.
- **Why it exists:** They remove ambiguity about edge cases and expected behavior while the answer is still cheap, and they give testers something to test against other than intuition.
- **If missing:** "Done" is negotiated after the fact. Builders guess at business rules (does a pending invitation consume a seat?), testers invent their own expectations, and defects are really undocumented decisions.
- **Good looks like:** Cucumber practice: scenarios written in the customer's own language, describing behavior rather than UI mechanics, with step definitions that execute the checks against the real system.
- **Slop looks like:** Criteria copied from the story text ("the feature works correctly"), happy-path only, or a long checklist of vague adjectives — fast, secure, user-friendly — that no test could pass or fail.
- **Verify:** Run the acceptance test suite (for example `cucumber` or the project's BDD runner). Every story in the release must map to at least one passing scenario, including one failure or boundary case.
- **Source:** Abstracta, "A Guide to Good Cucumber Practices," https://abstracta.us/blog/testing-tools/a-guide-to-good-cucumber-practices
- **Owning departments:** D1, D8
- **Skills that serve it:** acceptance-criteria, user-stories

## Scope boundaries
- **What:** The explicit line between what a project will deliver and what it will not. A boundary is only real when the exclusions are written down, not merely implied by the inclusion list.
- **How it works:** Teams sort candidate requirements into priority classes and record the rejects. DSDM's MoSCoW technique is the classic form: Must have, Should have, Could have, and Won't have (this time), agreed with the business for a fixed timeframe.
- **Why it exists:** Time and budget are fixed in practice; scope is the variable that absorbs pressure. A written boundary lets the team drop lower-priority work deliberately instead of discovering cuts at the deadline.
- **If missing:** Scope creep. Every stakeholder request enters silently, nothing is ever refused, and the project either slips or quietly ships a thinner version of everything.
- **Good looks like:** The DSDM Agile Project Framework's MoSCoW practice, developed from Dai Clegg's 1994 method: Must haves form the Minimum Usable Subset, and Won't haves are recorded in the Prioritised Requirements List so excluded items stay excluded.
- **Slop looks like:** A scope section that lists only inclusions, labels everything "high priority," and contains no Won't-have list at all — a boundary that excludes nothing bounds nothing.
- **Verify:** Inspect the requirements document: it must contain an explicit out-of-scope or Won't-have list, and every Must have must trace to a project objective. Interview one stakeholder and confirm they can name something that is excluded.
- **Source:** Rework library, "MoSCoW Method: Prioritize Requirements the Right Way," https://resources.rework.com/libraries/project-management/moscow-prioritization
- **Owning departments:** D1
- **Skills that serve it:** scope-control, roadmapping

## Cost estimation
- **What:** A forecast of the effort, time, and money a project will consume, stated with its assumptions and its uncertainty. An estimate is a range with a confidence level, not a single promised number.
- **How it works:** Estimators decompose the work, size the pieces (by analogy, expert judgment, or parametric models), and re-estimate as decisions land. The estimate, the target, and the commitment are kept as three separate things, because confusing them corrupts all three.
- **Why it exists:** Estimates let sponsors judge whether a project's targets are realistic and controllable before the money is spent, and they drive staffing, pricing, and sequencing decisions.
- **If missing:** The first number anyone says becomes the budget and the deadline. Overruns appear as surprises, and the team is pressured to cut quality invisibly — testing, documentation, review — to protect a fiction.
- **Good looks like:** Steve McConnell's Cone of Uncertainty (Construx): an estimate made at initial concept can range from 0.25x to 4x the actual cost, and the range narrows only as scope and design decisions are made — so early estimates are quoted as ranges.
- **Slop looks like:** A single confident figure with no decomposition, no assumptions, and no range — precision performed rather than earned, often identical to whatever budget the requester hinted at.
- **Verify:** Inspect the estimate record: it must show the breakdown, the method, the assumptions, and a range. Compare the last five completed items' estimates against their actuals; a team with no estimate-versus-actual history is not estimating, it is guessing.
- **Source:** Steve McConnell, "Software Development's Cone of Uncertainty," Construx white paper, https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf
- **Owning departments:** D1
- **Skills that serve it:** unit-economics, product-metrics

## Fact sheets
- **What:** A short, standardized document that states the verified facts about an artifact — what it is, what it is for, how it was produced, how it performs, and where its limits are — in a fixed set of sections.
- **How it works:** The producer fills the same template every time: identity and provenance, intended use, inputs, measured performance broken down by relevant conditions, risks, and caveats. Claims in the sheet must be backed by measurement or documentation, and the sheet travels with the artifact.
- **Why it exists:** Decisions get made from summaries, not from the artifact itself. A fact sheet makes the summary trustworthy, comparable across artifacts, and honest about what is not known.
- **If missing:** Marketing language replaces measurement. Users adopt the artifact for contexts it was never evaluated in, and nobody can reconstruct later why it was trusted.
- **Good looks like:** Model Cards, proposed by Mitchell et al. (2019) and adopted in the ML field: every released model ships with a card covering intended use, evaluation data, disaggregated performance, ethical considerations, and caveats.
- **Slop looks like:** A fact sheet that reads like a brochure — superlatives instead of measurements, aggregate numbers only, no provenance, no limitations section, and figures that appear nowhere in any test output.
- **Verify:** Pick three quantitative claims in the fact sheet and trace each to its evidence (test run, dataset, or measurement record). Any claim that cannot be traced is removed or marked unverified.
- **Source:** Mitchell et al., "Model Cards for Model Reporting," FAT* 2019, https://arxiv.org/html/1810.03993
- **Owning departments:** D1, D10
- **Skills that serve it:** fact-sheet

## Real content
- **What:** The actual words, data, and media the product will ship with — real names, real figures, real copy written for the real audience — used from design onward instead of stand-in text.
- **How it works:** Content is treated as a design input, not a final polish step. Designers lay out pages with genuine copy and data, including awkward cases: long names, empty states, error messages, and the longest legal sentence. Writers work to a style standard, such as plain language.
- **Why it exists:** Layout, hierarchy, and usability decisions all change when real content arrives. Testing with real content exposes broken flows while they are still cheap to fix.
- **If missing:** The product is designed around tidy fiction. Real copy overflows components, real data breaks tables, and user research sessions measure reactions to text nobody will ever read.
- **Good looks like:** UK government practice: the Department for Education design team records the lesson to use real content, not lorem ipsum, in research sessions, and GOV.UK publishing guidance mandates specific, plain, user-need-led copy.
- **Slop looks like:** Polished screens filled with generic marketing prose, round invented numbers, and copy that could belong to any product in any industry — content generated to fill space rather than to inform.
- **Verify:** Sample five shipped pages and check every factual claim (names, prices, statistics, dates) against the project's fact sheet or a primary source. One untraceable claim fails the check.
- **Source:** GOV.UK publishing guidance, "Use clear language," https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/ ; Department for Education design histories, http://design-histories.education.gov.uk/fatp-lessons-learnt/design-learnings
- **Owning departments:** D9, D1
- **Skills that serve it:** real-content, fact-sheet

## Placeholder detection
- **What:** The systematic hunt for stand-in material — lorem ipsum, dummy data, "coming soon" blocks, sample names, TODO stubs — that survived into a deliverable meant to be real.
- **How it works:** Detection combines automated scans (pattern searches over source, content, and built output for known placeholder strings and generators' fingerprints) with human review of rendered pages. It runs as a release gate, not a one-time cleanup, because placeholders re-enter through every import, template, and generated draft.
- **Why it exists:** Placeholders are harmless in a sketch and corrosive in production: they publish false information, break user trust, and hide the fact that a content or data task was never finished.
- **If missing:** Dummy text ships. Nielsen Norman Group notes that fake copy in prototypes already causes real harm upstream — real content has different length and characteristics, so designs validated against placeholders fail when the truth arrives.
- **Good looks like:** NN/g's guidance in "A Downside of Fake Copy in UI Prototypes": use placeholders only in the earliest stages, then replace them with realistic content before evaluating or shipping the design.
- **Slop looks like:** The failure this element exists to catch: lorem ipsum in a live footer, "John Doe" in a testimonial, 555 phone numbers, stock metrics, and images hot-linked from placeholder services in a production build.
- **Verify:** Run a scan over the repository and the built site, for example `grep -ri "lorem ipsum" .` plus pattern checks for common dummy names, numbers, and placeholder domains. The release passes only with zero hits outside explicitly marked mock files.
- **Source:** Nielsen Norman Group, "A Downside of Fake Copy in UI Prototypes" (video), https://www.nngroup.com/videos/fake-copy/
- **Owning departments:** D8, D9
- **Skills that serve it:** placeholder-scan, real-content

## Documentation
- **What:** The written record that lets someone other than the author understand, operate, extend, and trust the project: guides, references, explanations, and the project files themselves.
- **How it works:** Professional teams organize documentation by reader need rather than by author convenience. The Diátaxis framework is the widely adopted structure: tutorials for learning, how-to guides for tasks, reference for facts, and explanation for background — kept separate because mixing them serves no reader well.
- **Why it exists:** Knowledge held only in people's heads (or in a chat history) decays, cannot be reviewed, and cannot be handed over. Documentation is how a project survives its authors.
- **If missing:** Every question routes to whoever built the thing. New joiners reverse-engineer intent from code, repeat settled mistakes, and cannot safely change anything they do not understand.
- **Good looks like:** Diátaxis, created by Daniele Procida and adopted by hundreds of documentation projects: four distinct forms of documentation, each written for one user need and kept in its own place.
- **Slop looks like:** A single sprawling README that mixes tutorial, reference, and rationale; sections generated to look complete while describing features that do not exist; and no owner or update path, so it rots in place.
- **Verify:** Give a reader unfamiliar with the project one task from each documentation type (learn the basics, complete a task, look up a fact) using only the docs. Time them, note where they get stuck, and check three documented facts against the actual system.
- **Source:** Diátaxis, "A systematic approach to technical documentation authoring," https://diataxis.fr/
- **Owning departments:** D10
- **Skills that serve it:** documentation-writing, project-templates

## Changelog
- **What:** A curated, human-readable record of what changed in each version of a project, newest first — written for the people who use the project, not generated from raw commit messages.
- **How it works:** Every notable change is logged under the version that ships it, grouped by type: Added, Changed, Deprecated, Removed, Fixed, Security. An Unreleased section collects changes as they land, and version numbers follow Semantic Versioning so the number itself signals the impact.
- **Why it exists:** Users, operators, and support teams need to answer "what changed, and does it affect me?" in seconds. The changelog is also the project's public memory of its own evolution.
- **If missing:** Nobody can tell when a behavior changed or why. Upgrades become risky, regressions cannot be bisected by reading, and support answers every question by digging through commits.
- **Good looks like:** Keep a Changelog, the community convention maintained since 2014: one file, reverse chronological order, the six fixed change categories, and Semantic Versioning — followed by tens of thousands of open-source projects.
- **Slop looks like:** A changelog that is a dumped git log, a wall of "bug fixes and improvements," or entries describing features that never shipped — volume without curation, impossible to scan.
- **Verify:** Open CHANGELOG.md: the top entry must match the current released version and date, entries must sit under the standard category headings, and three sampled entries must each correspond to a real, findable change in the release.
- **Source:** Keep a Changelog 1.1.0, https://keepachangelog.com/en/1.1.0/ ; Semantic Versioning 2.0.0, https://semver.org/spec/v2.0.0.html
- **Owning departments:** D10
- **Skills that serve it:** changelog, decision-logs

## Handover
- **What:** The deliberate transfer of a project — its operation, its context, and its open risks — from the people who built it to the people who will run or continue it.
- **How it works:** Handover is a process, not a document dump: a readiness review against a checklist, walkthroughs of architecture and failure modes, shared on-call or shadowing, and a named owner on the receiving side who accepts the transfer. Known landmines are listed explicitly, with the evidence for each.
- **Why it exists:** Projects outlive their builders. Without a structured transfer, operational knowledge, credentials, and the reasons behind decisions leave with the departing team.
- **If missing:** The receiving team learns the system from its first production incident. Simple questions take days, risky changes are avoided or made blindly, and the "bus factor" of the project drops to whoever answers the phone.
- **Good looks like:** Google's SRE onboarding model: before SRE accepts a service, it runs a Production Readiness Review (SRE entrance review) that assesses supportability, identifies deficiencies to fix first, and agrees takeover conditions with the owning team.
- **Slop looks like:** A handover consisting of a repository link and a cheerful message; a "handover document" that lists components but no failure modes, no credentials path, no open risks, and no accepting owner.
- **Verify:** Run the test: the receiving owner, using only the handover materials, must deploy the project, find the runbook, name the top open risks, and state who accepts the transfer. Any step they cannot complete is a handover gap.
- **Source:** Google Cloud Blog, "How SREs find the landmines in a service" (SRE entrance review / Production Readiness Review), https://cloud.google.com/blog/products/gcp/how-sres-find-the-landmines-in-a-service-cre-life-lessons
- **Owning departments:** D10, D1
- **Skills that serve it:** handover, runbook-writing, memory-retrieval, project-takeover

## Part 2 — Architecture & code

## System architecture
- **What:** The high-level structure of the system: its major building blocks, how they communicate, and where its boundaries sit.
- **How it works:** The team decomposes the system into containers (applications, data stores, queues) and components inside them, records the runtime communication paths, and documents the result as layered diagrams that are reviewed and kept current as the system evolves.
- **Why it exists:** So every developer shares one mental model of the system before writing code that must fit into it.
- **If missing:** Each developer invents a private architecture; components duplicate each other, calls cross boundaries arbitrarily, and the system becomes a big ball of mud that no one can reason about or scale.
- **Good looks like:** The C4 model by Simon Brown: hierarchical system context, container, component, and code diagrams that zoom from the whole system down to implementation, documented at c4model.com.
- **Slop looks like:** A single auto-generated box-and-arrow diagram with generic labels ("Frontend", "Backend", "Database"), no actors, no protocols, and no relationship to the actual code.
- **Verify:** Open ARCHITECTURE.md and check that every deployable unit in the repository or infrastructure config appears as a container in the container diagram, and that every arrow names a protocol or data format.
- **Source:** The C4 model for visualising software architecture — https://c4model.com/
- **Owning departments:** D2
- **Skills that serve it:** system-design, c4-diagrams, architecture-patterns

## Stack decisions
- **What:** The deliberate, recorded choice of languages, frameworks, databases, and platforms the project is built on.
- **How it works:** Candidates are compared against explicit criteria (requirements fit, team skill, ecosystem maturity, licensing, operational cost), the winner is chosen, and the reasoning, alternatives, and accepted downsides are written down in a decision record stored with the code.
- **Why it exists:** Stack choices are expensive to reverse; recording why they were made prevents endless re-litigation and uninformed swaps.
- **If missing:** Tools are picked by hype or habit, incompatible pieces are combined, and six months later nobody can explain why the project is stuck with a database or framework that fights its requirements.
- **Good looks like:** Markdown Architectural Decision Records (MADR): one file per decision with context, considered options, decision outcome, and consequences, as templated at adr.github.io.
- **Slop looks like:** A README listing a fashionable stack ("Next.js + Prisma + tRPC") with no rationale, no alternatives considered, and versions that do not match the project's actual dependency files.
- **Verify:** Inspect the decision records folder (for example docs/decisions/): confirm one record exists for each major stack component named in the dependency manifest, each with status "accepted" and at least one rejected alternative.
- **Source:** MADR — Markdown Architectural Decision Records — https://adr.github.io/madr/
- **Owning departments:** D2, D15
- **Skills that serve it:** stack-selection, adr-writing

## API contracts
- **What:** The explicit, machine-readable agreement between an API provider and its consumers: endpoints, request and response shapes, error formats, and authentication requirements.
- **How it works:** The contract is written in a standard description format before or alongside implementation, shared with consumers, and used to generate documentation, client code, and contract tests that fail the build when implementation and contract drift apart.
- **Why it exists:** So frontend, backend, mobile, and third-party integrators can build against the same truth without reading server code or guessing.
- **If missing:** Consumers reverse-engineer responses by trial and error; a field rename or status-code change silently breaks clients in production.
- **Good looks like:** An OpenAPI description maintained as the source of truth for the API, validated in CI and used to generate the published reference documentation.
- **Slop looks like:** Endpoint behavior described only in prose chat messages; error responses that vary per endpoint; fields appearing in examples that the real API never returns.
- **Verify:** Run a linter against the contract file (for example `npx @redocly/cli lint openapi.yaml`), then run the contract test suite and confirm it passes against the running service.
- **Source:** OpenAPI Specification v3.1.0, OpenAPI Initiative — https://spec.openapis.org/oas/v3.1.0
- **Owning departments:** D2, D4
- **Skills that serve it:** api-architecture, api-paradigms, api-versioning

## Data models
- **What:** The representation of the project's information: entities, their attributes, relationships, and integrity rules, as implemented in database schemas and domain objects.
- **How it works:** Modelers identify the core entities and relationships, choose storage structures based on how the application actually reads and writes the data (access patterns), apply constraints and indexes, and evolve the model through versioned migrations.
- **Why it exists:** Data outlives code; a sound model keeps information consistent and queryable long after the first application version is gone.
- **If missing:** The same fact is stored in several places and drifts out of sync, relationships are enforced nowhere, and routine queries require slow full-table scans or fragile application-side joins.
- **Good looks like:** MongoDB's official data modeling guidance: design document structure around the application's queries, deliberately choosing embedded versus referenced data per relationship, documented in the MongoDB Manual.
- **Slop looks like:** One generic table or collection per noun with stringly-typed fields, no constraints, no indexes beyond the primary key, and duplicated copies of the same entity updated inconsistently.
- **Verify:** Inspect the migration history and schema definitions: confirm every entity named in the requirements has a corresponding schema object, foreign keys or references are declared, and the queries used by the main screens are backed by indexes (check with the database's explain-plan command).
- **Source:** MongoDB Manual, "Data Modeling Introduction" — http://mongodocs.github.io/core/data-modeling-introduction.html
- **Owning departments:** D2
- **Skills that serve it:** data-architecture, domain-driven-design

## Code organisation
- **What:** The way source code is divided into modules, packages, and layers, and the rules governing what may depend on what.
- **How it works:** Code is grouped by feature or domain capability rather than by technical type; each module exposes a small public interface, hides its internals, and depends only on declared collaborators, so the folder tree reads as a map of what the system does.
- **Why it exists:** So a developer can find where a change belongs, make it without breaking distant code, and understand the blast radius before editing.
- **If missing:** Logic lands wherever is convenient, circular dependencies form, a one-line change requires editing files across the whole tree, and no newcomer can navigate the project.
- **Good looks like:** NestJS feature modules: each capability (controller, service, module definition) lives in its own folder, providers are encapsulated by default, and cross-module use goes through explicit exports, per the official NestJS documentation.
- **Slop looks like:** Giant `utils` and `helpers` folders, a single `services` directory holding unrelated logic, files named `misc.ts`, and layers that import each other in both directions.
- **Verify:** List the top-level source folders and confirm each maps to a named feature or domain concept; then run the dependency check in the linter or module system (for example, confirm no module imports a non-exported provider from another module).
- **Source:** NestJS documentation, "Modules" — https://docs.nestjs.com/modules
- **Owning departments:** D2, D15
- **Skills that serve it:** architecture-patterns, domain-driven-design, dev-environment

## Configuration
- **What:** Everything that varies between deployments — database URLs, credentials, hostnames, feature settings — held outside the code.
- **How it works:** The same build artifact runs everywhere; each deployment injects its values through environment variables or a secret store. The application reads configuration once at startup, validates it, and fails fast with a clear error when a required value is absent.
- **Why it exists:** So code can be promoted unchanged from development to staging to production, and credentials never live in the repository.
- **If missing:** Developers hardcode endpoints and passwords, commit secrets to version control, and "works on my machine" becomes permanent because every environment quietly runs different code.
- **Good looks like:** Factor III of The Twelve-Factor App: strict separation of config from code, config stored in environment variables, granular and independently managed per deploy.
- **Slop looks like:** An `if (environment === "prod")` branch choosing a hardcoded database URL, a real API key sitting in a committed config file, and defaults silently pointing at production.
- **Verify:** Run `git grep -n "password\|api_key\|secret" -- "*.json" "*.yaml" "*.ts" "*.js"` (excluding test fixtures) and confirm no real credentials appear; then start the app with a required variable unset and confirm it refuses to boot with a naming error.
- **Source:** The Twelve-Factor App, "III. Config" — https://12factor.net/config
- **Owning departments:** D4, D15
- **Skills that serve it:** dev-environment

## API documentation
- **What:** The reference material that lets a developer who has never seen the codebase call the API correctly: endpoints, parameters, examples, errors, and authentication.
- **How it works:** Documentation is generated from, or continuously checked against, the machine-readable API description, and published alongside the service with runnable request examples and a changelog for consumers.
- **Why it exists:** An undocumented API is effectively a private API; consumers cannot integrate with what they cannot discover.
- **If missing:** Integrators guess parameters, misuse error codes, and flood the owning team with basic questions; stale wikis actively mislead them into building against behavior that no longer exists.
- **Good looks like:** API reference generated from the project's OpenAPI description, so every documented path, schema, and response code is derived from the same file the contract tests validate.
- **Slop looks like:** A documentation page listing endpoints that return 404, example payloads with fields the API rejects, and "TODO: document errors" sections shipped as final.
- **Verify:** Pick three documented endpoints at random and execute the documented example requests against a running instance (for example with `curl`); all three must return the documented status code and response shape.
- **Source:** OpenAPI Specification v3.1.0, OpenAPI Initiative — https://spec.openapis.org/oas/v3.1.0
- **Owning departments:** D2, D4
- **Skills that serve it:** api-documentation, api-architecture

## Multi-tenancy
- **What:** Serving multiple customers (tenants) from one application while keeping each tenant's data, configuration, and experience isolated from the others.
- **How it works:** Every request is resolved to a tenant context; data access is scoped by that context at the database layer (shared schema with a tenant key, schema per tenant, or database per tenant), and isolation is enforced by the platform rather than by each developer remembering a filter.
- **Why it exists:** SaaS economics: one codebase and one deployment serving many customers is far cheaper to run and upgrade than one installation per customer.
- **If missing:** Either the product cannot onboard a second customer without a rewrite, or worse, it can — and one tenant's query leaks another tenant's data.
- **Good looks like:** Microsoft's documented tenancy models for Azure data services, which spell out the isolation and cost trade-offs of partition-key-per-tenant versus account-per-tenant designs.
- **Slop looks like:** A `tenant_id` column added to some tables but enforced in application code only where the developer remembered, with admin and reporting queries bypassing it entirely.
- **Verify:** Run the cross-tenant test: authenticate as a user of tenant A and request a known resource ID belonging to tenant B through the API and any export/report endpoint; every attempt must return 403 or 404, never the data.
- **Source:** Microsoft Learn, "Multitenancy — Azure Cosmos DB" (tenancy models: partition key per tenant, account per tenant) — https://learn.microsoft.com/en-us/azure/cosmos-db/multi-tenancy-vector-search
- **Owning departments:** D2, D4
- **Skills that serve it:** multitenancy-saas, data-architecture, saas-conversion

## Feature flags and experimentation
- **What:** Runtime switches that turn features on or off without redeploying, plus the controlled experiments (A/B tests) run behind them.
- **How it works:** Code checks a flag through a central toggle router; flag values are configured per environment, user segment, or percentage rollout. Experiment flags assign each user consistently to a variant, and outcomes are measured against a defined metric before the winning variant ships to everyone.
- **Why it exists:** To decouple deployment from release: ship code safely, roll out gradually, kill a broken feature instantly, and replace opinion with measured evidence.
- **If missing:** Every release is all-or-nothing, a bad feature requires an emergency redeploy to withdraw, and product decisions are argued rather than tested.
- **Good looks like:** The taxonomy in Pete Hodgson's "Feature Toggles" on martinfowler.com: release, experiment, operations, and permissioning toggles, each with an expected lifespan and an owner.
- **Slop looks like:** Permanent `if (true)` branches, flags with names like `new_feature_v2_final`, no record of who owns a flag, and "experiments" with no metric, no end date, and both variants still running a year later.
- **Verify:** Open the flag configuration for the production environment and confirm every flag in the codebase appears there with an owner and a state; then flip one release flag off in a staging environment and confirm the feature disappears without a redeploy.
- **Source:** Pete Hodgson, "Feature Toggles (aka Feature Flags)", martinfowler.com — https://martinfowler.com/articles/feature-toggles.html
- **Owning departments:** D4, D2
- **Skills that serve it:** feature-flags, experimentation-platform

## Versioning
- **What:** The disciplined numbering and labeling of releases of the software and its APIs, so consumers can tell what changed and whether upgrading is safe.
- **How it works:** Each release gets a version identifier under a published scheme; breaking changes, compatible additions, and fixes increment different parts of the number; APIs additionally support old and new versions side by side during a deprecation window announced in advance.
- **Why it exists:** So users, integrators, and operators can reason about compatibility, plan upgrades, and roll back to a known state.
- **If missing:** "Latest" is the only version anyone can name, a silent breaking change takes down every consumer at once, and bug reports cannot be tied to the code that produced them.
- **Good looks like:** Semantic Versioning 2.0.0: MAJOR for incompatible API changes, MINOR for backward-compatible functionality, PATCH for backward-compatible fixes, with released versions never modified after publication.
- **Slop looks like:** Version numbers bumped at random (1.0 to 3.0 for a typo fix), breaking API changes shipped under the same version, and no changelog connecting versions to changes.
- **Verify:** Compare the current API version identifier against the previous release's contract: if any endpoint was removed or its response shape changed incompatibly, the major version must have increased; confirm the version in the deployed service's metadata endpoint matches the repository's release tag.
- **Source:** Semantic Versioning 2.0.0 — https://semver.org/
- **Owning departments:** D15, D2
- **Skills that serve it:** versioning, api-versioning

## Part 3 — Data & services

## Databases and migrations
- **What:** The primary database holds the product's durable state; migrations are the versioned, ordered code files that evolve its schema over time.
- **How it works:** Each schema change is a timestamped migration committed to the repo. The runner applies pending migrations in order and records applied versions in a tracking table, so every environment converges to the same schema. Risky changes use expand-and-contract (add new shape, backfill, switch reads, drop old shape) and run inside transactions where the database supports transactional DDL.
- **Why it exists:** Code and schema must change together, reproducibly, on every machine and in production.
- **If missing:** Environments drift apart, deploys break against an unexpected schema, and fixes become manual SQL nobody can reproduce or roll back.
- **Good looks like:** The Rails Guides' Active Record Migrations: versioned files, a reversible `change` method, explicit `up`/`down` where reversal is not automatic, and DDL wrapped in transactions.
- **Slop looks like:** The ORM auto-syncing tables in production, hand-edited production schema, already-applied migrations edited in place, and migrations with no working rollback.
- **Verify:** On an empty database, run the full migration set, diff the resulting schema against the committed schema file, roll back the last migration, and re-apply it cleanly.
- **Source:** Ruby on Rails Guides, "Active Record Migrations" — https://guides.rubyonrails.org/v7.1.3/active_record_migrations.html
- **Owning departments:** D5 (primary), D4.
- **Skills that serve it:** schema-design, migrations, sql-fundamentals, nosql-patterns, transactions-concurrency, tenant-isolation, backup-recovery.

## Caching
- **What:** A fast, temporary copy of frequently read or expensive-to-compute data, held in an in-memory store such as Redis or at the CDN edge.
- **How it works:** In the dominant cache-aside pattern, the application checks the cache first; on a miss it reads the database, stores the result under a key with a TTL, and returns it. Writes update the database and delete the affected keys, so staleness is bounded by TTL and explicit invalidation. Hot-key stampedes are controlled with locks or early refresh.
- **Why it exists:** It cuts read latency and shields the primary database from repetitive load.
- **If missing:** Every page view hits the database, latency grows with traffic, and a traffic spike can cascade into a database outage.
- **Good looks like:** Redis's official cache-aside documentation: hash the lookup into a key, populate on miss, expire with TTL, invalidate on write.
- **Slop looks like:** Caching with no TTL and no invalidation (stale prices forever), per-user data stored under shared keys (a data leak), and the cache treated as the source of truth.
- **Verify:** With query logging on, request the same resource twice and confirm the second response issues no database query; then update the record and confirm the old value is no longer served.
- **Source:** Redis documentation, "Redis cache-aside" — https://redis.io/docs/latest/develop/use-cases/cache-aside/
- **Owning departments:** D5 (primary), D4.
- **Skills that serve it:** caching, query-performance, data-access, read-replicas.

## Search
- **What:** Finding records by relevance across text content — titles, descriptions, documents — rather than by exact-match lookups.
- **How it works:** Text is tokenized and normalized into an inverted index (a `tsvector` column with a GIN index in PostgreSQL, or a dedicated engine such as Elasticsearch, OpenSearch, or Typesense). The index is built and refreshed as records change, and queries are ranked, filtered, and faceted instead of scanned row by row.
- **Why it exists:** Users cannot browse a large catalog by hand, and `LIKE '%term%'` has no ranking and degrades to a full table scan.
- **If missing:** Search is slow, returns unranked or wrong results, and newly added content silently never appears.
- **Good looks like:** PostgreSQL's documented full text search: `to_tsvector` / `to_tsquery`, weighted fields, `ts_rank` ordering, and a GIN index keeping it fast.
- **Slop looks like:** A `LIKE` query on the main table presented as "search," an index that is built once and never updated, and results ordered by insertion rather than relevance.
- **Verify:** Create a record containing a distinctive word and confirm it appears in results; run `EXPLAIN` on the search query to confirm index use; delete the record and confirm it disappears.
- **Source:** PostgreSQL documentation, "Text Search Functions and Operators" — https://www.postgresql.org/docs/10/functions-textsearch.html
- **Owning departments:** D5 (primary), D4.
- **Skills that serve it:** search-engines, vector-db, indexing, data-access.

## File storage and media handling
- **What:** User uploads and media assets stored in object storage (such as S3), while the database keeps only metadata and object keys — never the bytes.
- **How it works:** The server issues a short-lived presigned URL and the browser uploads directly to the bucket, keeping large files off the app server. Uploads are validated for type and size, processed asynchronously (thumbnails, transcodes, virus scans) through a job queue, and delivered through a CDN. Buckets are private by default; access is granted through signed URLs.
- **Why it exists:** App servers are stateless and replaceable; local disks fill, and file traffic should not compete with request handling.
- **If missing:** Uploads vanish on redeploy, disks fill until the server dies, and private documents leak through permanent public URLs.
- **Good looks like:** AWS's S3 presigned URL documentation: private objects, time-limited scoped access for both upload and download.
- **Slop looks like:** Files saved into the app's public folder, base64 blobs stored in database rows, no file-type validation, and world-readable buckets.
- **Verify:** Upload through the UI and confirm the object exists in the bucket while the database row holds only its key; request the file unauthenticated and confirm access is denied; confirm the signed URL stops working after expiry.
- **Source:** Amazon S3 documentation, "Download and upload objects with presigned URLs" — https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html
- **Owning departments:** D4 (primary), D5.
- **Skills that serve it:** file-uploads, media-processing, queues-jobs, data-access.

## Real-time features
- **What:** The server pushing updates to connected clients as they happen — chat, live feeds, presence, collaborative editing — instead of clients asking repeatedly.
- **How it works:** A WebSocket connection is opened with an HTTP upgrade handshake and kept alive with ping/pong heartbeats; for one-way updates, server-sent events suffice. The server routes messages by channel or room, and a pub/sub layer (such as Redis) fans events out across multiple server instances. Clients reconnect with backoff and catch up on missed events; the socket is authenticated at handshake.
- **Why it exists:** Polling wastes bandwidth and still feels stale; interactive features are unusable with multi-second lag.
- **If missing:** Users see outdated state until they refresh, and teams often compensate with aggressive polling that hammers the API.
- **Good looks like:** MDN's WebSocket API documentation: the handshake, `open`/`message`/`close` events, and `wss` for secure connections.
- **Slop looks like:** A one-second `setInterval` poll marketed as real-time, a socket with no reconnect logic, no authentication on the connection, and subscriptions held in one process's memory so the feature breaks the moment a second instance runs.
- **Verify:** Open two sessions, act in one, and confirm the other updates without a refresh; drop the connection and confirm the client reconnects; confirm an unauthenticated socket attempt is rejected.
- **Source:** MDN Web Docs, "WebSocket" — https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
- **Owning departments:** D4.
- **Skills that serve it:** realtime, queues-jobs, notifications.

## Notifications
- **What:** Event-driven messages that reach users outside an active request: push notifications and the in-app notification inbox.
- **How it works:** A domain event triggers a notification service, which records the notification in the database (the inbox is the source of truth) and dispatches to channel providers — FCM or APNs for push, Web Push with VAPID keys for browsers. Device tokens are stored per user, sends are queued, and tokens the provider reports as invalid are pruned. User preferences and opt-outs are checked before sending.
- **Why it exists:** Replies, failed payments, and security alerts are worthless if the user only discovers them on their next visit.
- **If missing:** Users miss time-sensitive events, churn rises, and failed-payment recovery never starts.
- **Good looks like:** Firebase Cloud Messaging's documented model: registration tokens per device, the HTTP v1 API, topic messaging, and delivery reporting.
- **Slop looks like:** A bell icon rendering a hardcoded list, push tokens never stored so nothing can ever be sent, sends performed synchronously inside the web request, and dead tokens retried forever.
- **Verify:** Trigger the event on a test account and confirm the notification arrives on a real device or browser and exists in the notifications table; invalidate the token and confirm the failure is logged and the token pruned.
- **Source:** Firebase documentation, "Firebase Cloud Messaging" — https://firebase.google.com/docs/cloud-messaging
- **Owning departments:** D4 (primary), D11.
- **Skills that serve it:** notifications, queues-jobs, third-party-apis.

## Webhooks
- **What:** Server-to-server HTTP callbacks: your application receives events from providers (payment succeeded, subscription canceled) and may also send events to customers' own endpoints.
- **How it works:** The receiving endpoint verifies the signature — an HMAC computed over the raw request body with the endpoint secret — stores the event, returns a 2xx immediately, and processes asynchronously from a queue. Because delivery is at-least-once and unordered, processing is idempotent: events are deduplicated by ID and handlers converge state rather than increment it. Senders retry failures with backoff and log every delivery attempt.
- **Why it exists:** Money and account state change outside your requests; polling for those changes is slow, lossy, and rate-limited.
- **If missing:** Paid users are never activated, canceled users keep access, and local state quietly drifts from the provider's truth.
- **Good looks like:** Stripe's webhook documentation: verify signatures on the raw body, respect the timestamp tolerance against replay, acknowledge fast, and handle duplicate events.
- **Slop looks like:** An endpoint that trusts any POST claiming "payment succeeded," heavy processing before responding (causing timeouts and duplicate retries), and no deduplication.
- **Verify:** Replay a real test event with the provider's tooling and confirm the state change; send the same event twice and confirm a single effect; send a forged request with a bad signature and confirm rejection.
- **Source:** Stripe documentation, "Receive Stripe events in your webhook endpoint" — https://docs.stripe.com/webhooks
- **Owning departments:** D11 (primary), D4.
- **Skills that serve it:** webhooks, payments, queues-jobs, api-keys-management.

## Transactional email and SMS
- **What:** System-generated messages bound to a user action — verification codes, password resets, receipts, delivery alerts — as distinct from marketing campaigns.
- **How it works:** The application enqueues the message and a provider (Amazon SES, SendGrid, Twilio) delivers it. The sending domain is authenticated with SPF, DKIM, and DMARC records so receiving servers trust it. Delivery, bounce, and complaint outcomes return through provider webhooks or status callbacks and are stored against the message; SMS sends record the provider message SID and its status transitions.
- **Why it exists:** Account recovery, verification, and receipts are load-bearing flows; if the message does not arrive, the product is broken.
- **If missing:** Users are locked out with no reset path, there is no proof of purchase, and unauthenticated mail lands in spam.
- **Good looks like:** Amazon SES's DMARC guidance (aligned SPF and DKIM on the sending domain) and Twilio's status-callback model for tracking each SMS to delivery.
- **Slop looks like:** Mail sent from the app server with no SPF/DKIM, a "reset email sent" toast with nothing behind it, and delivery assumed because the API call returned success — with bounces never recorded.
- **Verify:** Complete a signup and password reset in staging and confirm both messages arrive with SPF, DKIM, and DMARC passing in the headers; confirm the delivery or bounce status is recorded from the provider callback.
- **Source:** Amazon SES documentation, "Complying with DMARC authentication protocol in Amazon SES" — https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dmarc.html ; Twilio documentation, "Track the Message Status of Outbound Messages" — https://www.twilio.com/docs/messaging/guides/track-outbound-message-status
- **Owning departments:** D11 (primary), D4.
- **Skills that serve it:** transactional-email, sms, webhooks, queues-jobs.

## Payments and billing
- **What:** Charging customers — one-off payments, subscriptions, invoices, refunds, and disputes — delegated to a payment provider such as Stripe while your database mirrors the state.
- **How it works:** Charges and checkout sessions are created server-side, always with idempotency keys so a retried request cannot double-charge. Card data goes directly to the provider, keeping your servers out of PCI scope. Subscription state is driven by the invoice lifecycle and provider webhooks, not by your own timers. Failed renewals enter dunning — scheduled retries plus customer notification — before access is cut, and refunds and disputes are handled as explicit flows.
- **Why it exists:** Billing errors destroy trust and money movement is regulated; correctness here is existential, not cosmetic.
- **If missing:** Customers are double-charged on retries, keep access after canceling (or lose it while paid), and there is no orderly refund path.
- **Good looks like:** Stripe Billing's documented subscription invoice lifecycle, paired with Stripe's idempotent-request support for safe retries.
- **Slop looks like:** The charge amount taken from the client request body, the success page treated as proof of payment instead of the webhook, no idempotency key (a double-click double-charges), and a "cancel" button that only hides the UI.
- **Verify:** In test mode, buy with a test card and confirm the paid invoice grants access; double-submit the checkout and confirm a single charge; replay the payment webhook and confirm no duplicate grant.
- **Source:** Stripe documentation, "Subscription invoices" — https://docs.stripe.com/billing/invoices/subscription ; "Idempotent requests" — https://docs.stripe.com/api/idempotent_requests
- **Owning departments:** D11 (primary), D4.
- **Skills that serve it:** payments, subscriptions, invoicing-tax, refunds-disputes, dunning, webhooks.

## Third-party integrations
- **What:** Deliberate connections to external services the product depends on but does not control: OAuth identity providers, maps, analytics, CRMs, shipping and tax APIs.
- **How it works:** Each integration sits behind an internal adapter that owns the provider's API shape, so provider changes touch one place. Credentials live in environment or secret storage, separate per environment. Calls carry explicit timeouts; transient failures retry with exponential backoff and jitter; a circuit breaker fails fast during a provider outage instead of piling up blocked requests. Responses are validated before use, and the product degrades gracefully when a provider is down.
- **Why it exists:** Rebuilding commodity capabilities is waste, but an unmanaged dependency becomes your outage.
- **If missing:** One provider's bad day hangs your request threads and takes your whole application down with it.
- **Good looks like:** Microsoft's Azure Architecture Center circuit breaker pattern: stop calling a failing dependency after a threshold, let it recover, probe before resuming.
- **Slop looks like:** API keys committed in frontend code, outbound calls with no timeout, response shapes trusted without validation, and an integration declared done because it worked once in development.
- **Verify:** In staging, point the integration at a dead endpoint and confirm the app degrades instead of hanging; search the repo and built frontend bundle for the API key and confirm it is absent; inspect logs to confirm timeout and backoff behavior.
- **Source:** Microsoft Learn, Azure Architecture Center, "Circuit Breaker Pattern" — https://learn.microsoft.com/en-gb/azure/architecture/patterns/circuit-breaker
- **Owning departments:** D11 (primary), D4.
- **Skills that serve it:** third-party-apis, api-keys-management, oauth-sso, sdk-embeddables, queues-jobs.

## Seed data rules
- **What:** The scripted initial data a database needs to be useful: required reference data (roles, plans, lookup values) and, for development only, realistic sample records.
- **How it works:** A seed script lives in the repo and runs after migrations. It is idempotent — upserting by natural key — so re-running it changes nothing. Required reference data is kept separate from development sample data, and sample data is generated synthetically, never copied from real users. Production receives only controlled reference-data seeds through the normal release process, never demo content.
- **Why it exists:** Every developer machine, CI run, and review environment must reach the same known starting state without manual setup.
- **If missing:** A fresh clone will not boot (missing roles or plans), tests depend on one person's local database, and onboarding stalls.
- **Good looks like:** Prisma's documented seeding: an integrated `prisma db seed` command that consistently re-creates the same starting data after migrations.
- **Slop looks like:** A seed that inserts duplicates on every run, demo accounts with guessable credentials shipped to production, real customer records copied into development seeds, and a one-off SQL dump committed once and never maintained.
- **Verify:** On an empty database, run migrations and the seed twice; confirm row counts are identical after the second run and the app boots with the documented development login; confirm the production pipeline contains no sample-data seed step.
- **Source:** Prisma documentation, "Seeding" — https://www.prisma.io/docs/orm/v6/prisma-migrate/workflows/seeding
- **Owning departments:** D5 (primary), D4.
- **Skills that serve it:** seed-data, migrations, data-quality, schema-design.

## Part 4 — Delivery pipeline

## Testing (unit/integration/e2e)
- **What:** Automated checks at three scopes: unit tests verify single functions in isolation, integration tests verify components together (an API against a real database), and end-to-end (e2e) tests drive the finished application through real user flows in a browser.
- **How it works:** Unit tests run in milliseconds under a runner such as Vitest or pytest, with external dependencies mocked. Integration tests start a real database, often a throwaway container, and exercise endpoints and queries. E2E tools such as Playwright launch Chromium, Firefox, and WebKit, click through signup or checkout, and assert on what the user sees. All three layers run locally and again in CI on every pull request.
- **Why it exists:** Each layer catches failures the others miss: logic errors cheaply in units, contract and data errors in integration, broken journeys in e2e — before users find them.
- **If missing:** Regressions ship silently. Checking a change means slow manual clicking, so teams stop checking, and a routine refactor becomes a production incident.
- **Good looks like:** Playwright's official best-practices guide: test user-visible behavior, keep every test isolated with its own data, and use resilient locators such as `getByRole` and web-first assertions instead of fixed sleeps.
- **Slop looks like:** One giant e2e script full of `sleep(5000)` calls and brittle XPath selectors, tests that only pass in a single order — or no tests at all, just "I clicked around and it worked."
- **Verify:** From a clean checkout, `npm test` and `npx playwright test` both exit 0. Then deliberately break one assertion and re-run: the suite must fail. A suite that cannot fail proves nothing.
- **Source:** Playwright, "Best Practices," https://playwright.dev/docs/best-practices
- **Owning departments:** D8 (QA, Testing & Verification)
- **Skills that serve it:** unit-testing, integration-testing, e2e-testing, test-strategy, test-data, qa-gates

## CI/CD
- **What:** The automated pipeline that builds, tests, and prepares every code change for release. Continuous integration verifies changes as they are merged, frequently; continuous delivery/deployment then ships verified changes automatically or after an approval step.
- **How it works:** Workflow files (for example `.github/workflows/*.yml`) declare triggers (push, pull request), jobs, and steps. On each trigger, a fresh runner checks out the code, installs dependencies, lints, builds, and runs the test layers. Status checks block merging while red. A delivery stage deploys the passing artifact to staging and then, automatically or on approval, to production.
- **Why it exists:** It removes "works on my machine" from the process: every change is built and tested the same way, on a clean machine, with an auditable result attached to the commit.
- **If missing:** Merges land unverified, broken code reaches the main branch and is discovered by whoever pulls next, and releasing depends on one person remembering the manual steps.
- **Good looks like:** GitHub's own CI documentation: workflows that build and test every pull request on GitHub-hosted or self-hosted runners, with required status checks gating the merge.
- **Slop looks like:** A workflow file that exists but is commented out, a pipeline that always passes because its only step is `echo ok`, or CI that runs only on the main branch — after the damage is already merged.
- **Verify:** Open a throwaway pull request containing a deliberately failing test: the workflow must run, report the failure, and block the merge. Fix the test and confirm the check turns green.
- **Source:** GitHub Docs, "Continuous integration," https://docs.github.com/en/actions/get-started/continuous-integration
- **Owning departments:** D6 (DevOps, Deployment, Production, Hosting & Domains), D8 (QA, Testing & Verification)
- **Skills that serve it:** ci-cd, qa-gates, preview-environments

## Deployment
- **What:** Moving a verified build from the repository onto running infrastructure — and being able to move back. It covers environment promotion, release strategy (rolling, blue-green, canary), and rollback.
- **How it works:** The pipeline promotes the same immutable artifact through preview and staging to production, so what was tested is exactly what ships. Platforms such as Vercel and Netlify create a unique preview deployment for every pull request and a production deployment from the production branch. Rollback re-points traffic to the previous known-good deployment instead of patching a live server.
- **Why it exists:** Code has no value on a laptop. A defined deployment path makes releases routine, repeatable, and reversible instead of rare, manual, and frightening.
- **If missing:** The demo lives on localhost, "deploying" means copying files to a server by hand, nobody can say which version is live, and a bad release has no way back.
- **Good looks like:** Vercel's documented Git workflow: preview deployments for every push, production deployments from the production branch, and instant rollback to an earlier deployment.
- **Slop looks like:** "It works on localhost" with no deployment target at all, files uploaded over FTP to the live server, or production code edited in place so the running version exists nowhere in Git.
- **Verify:** In the host's deployment dashboard, confirm the live production deployment was built from the current commit SHA in Git, and that the previous deployment is listed and can be restored.
- **Source:** Vercel Docs, "Deploying Git Repositories with Vercel," https://vercel.com/docs/v1/features/repositories/
- **Owning departments:** D6 (DevOps, Deployment, Production, Hosting & Domains)
- **Skills that serve it:** deployment-strategies, ci-cd, preview-environments, containers

## Infrastructure
- **What:** The underlying compute, network, and storage the application runs on — servers or containers, load balancers, databases, firewalls — together with the code that provisions and configures them.
- **How it works:** In professional projects, infrastructure is declared as code (Terraform, Pulumi, CloudFormation) and committed to the repository. A plan step shows exactly what will change before anything is applied, and state is stored remotely with locking. Environments (development, staging, production) are stamped out from the same modules with different variables, so they differ only where intended.
- **Why it exists:** Declared infrastructure is reproducible and reviewable: a new environment, a disaster-recovery rebuild, or a region move becomes an apply, not an archaeology project.
- **If missing:** Servers are hand-built snowflakes configured by clicking through a console. Nobody can rebuild them, staging quietly differs from production, and one lost VM takes the product down with it.
- **Good looks like:** HashiCorp's Terraform language documentation: declarative resource blocks describe the intended end state, and Terraform computes and orders the changes needed to reach it.
- **Slop looks like:** Infrastructure that exists only inside one person's cloud console account, its setup remembered rather than written — or a generated Terraform file that was never planned, applied, or checked for drift.
- **Verify:** Run `terraform plan` against the committed configuration in a clean checkout: it completes and reports no changes (or only intended ones) against live state.
- **Source:** HashiCorp, "Terraform Language Documentation," https://developer.hashicorp.com/terraform/language
- **Owning departments:** D6 (DevOps, Deployment, Production, Hosting & Domains)
- **Skills that serve it:** infrastructure-as-code, containers, kubernetes, servers-vps

## Hosting
- **What:** Where the deployed application actually runs and is served to users: a managed platform (Vercel, Netlify, Render, Fly.io), a cloud provider, or a self-managed VPS — including its scaling, uptime, and region behavior.
- **How it works:** Git-connected platforms watch the repository, build on every push, and serve the result over a global CDN with automatic HTTPS. Self-managed hosting runs the app in containers or on a VM behind a reverse proxy, with health checks and log access. Either way, the choice is recorded with its real limits: build minutes, bandwidth, cold starts, regions.
- **Why it exists:** Hosting decides whether the app is reachable, fast, and affordable at real traffic levels — and whether it stays up when a machine fails.
- **If missing:** There is no answer to "where does it run?" The product depends on a developer's machine staying awake, and the first reboot or traffic spike ends it.
- **Good looks like:** Netlify's documented model: connect a Git repository once and every push builds and publishes, pull requests get Deploy Previews, and a failed deploy never replaces the live one.
- **Slop looks like:** A screenshot of the app running at `localhost:3000` presented as "launched," or a host picked with no thought for its sleep policy, bandwidth cap, or region.
- **Verify:** Open the production URL from a different network (for example, a phone on mobile data): the app loads over HTTPS with a valid certificate, and the host's dashboard shows the deployment that produced it.
- **Source:** Netlify Docs, "Create deploys," https://docs.Netlify.com/site-deploys/create-deploys
- **Owning departments:** D6 (DevOps, Deployment, Production, Hosting & Domains)
- **Skills that serve it:** hosting, cdn-strategy, ssl-certificates, servers-vps

## Domains and DNS
- **What:** The domain name users type, and the DNS records that resolve it to the host: A/AAAA records point a name at IP addresses, CNAME aliases one name to another, and TTL sets how long resolvers cache the answer.
- **How it works:** The domain is registered with a registrar and its zone delegated to a DNS provider (often Cloudflare or the host). Records are created for the apex and `www` pointing at the host, plus TXT records that prove ownership for HTTPS certificates and authenticate email (SPF, DKIM, DMARC). Before a migration, the TTL is lowered so the switch propagates quickly, then raised afterward.
- **Why it exists:** Without correct DNS, the best-built application is unreachable or untrusted: wrong records mean downtime, failed certificate issuance, and mail delivered to spam.
- **If missing:** The site lives on a raw IP or a provider subdomain forever — or a single record typo takes it offline for hours because a long TTL keeps serving the wrong answer.
- **Good looks like:** Cloudflare's DNS documentation: at least one IP-resolution record per domain, CNAME flattening at the apex, and proxied records defaulting to an automatic TTL of 300 seconds (as of 2026-11).
- **Slop looks like:** Records copied from a tutorial with the tutorial's IP still in them, a CNAME at the apex breaking other records, or "DNS is still propagating" offered as an excuse for a record that was never created.
- **Verify:** Run `dig +short example.com A` and `dig +short www.example.com CNAME` with the real domain: answers must match the host's documented targets, and `curl -I https://example.com` must return the app with a valid certificate.
- **Source:** Cloudflare Docs, "DNS record types," https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/
- **Owning departments:** D6 (DevOps, Deployment, Production, Hosting & Domains)
- **Skills that serve it:** domains-dns, ssl-certificates, hosting

## Free-tier options
- **What:** The no-cost plans of hosting, CI, and platform providers, used to launch and validate a project before paying. Each free tier is a real product tier with hard limits, not an unlimited trial.
- **How it works:** A typical zero-budget stack combines free app hosting, free CI minutes, and a free-tier database. The mechanics differ per provider: some tiers are usage-capped (bandwidth, requests, build minutes), some sleep when idle, and some are restricted to personal or non-commercial use. Limits reset monthly; hitting one either stops the service or starts billing, depending on the provider.
- **Why it exists:** Free tiers let a project ship, reach real users, and prove value before money is spent — but only if the limits are known before launch day.
- **If missing:** The launch plan assumes "free" means "unlimited": the site dies mid-month when a cap is hit, the database sleeps through a demo, or an unexpected bill arrives.
- **Good looks like:** Caps documented on official pricing pages: Vercel's free Hobby plan includes 100 GB of Fast Data Transfer and 1M function invocations per month and cannot purchase extra usage; Netlify's Free plan is $0 forever with a 300-credit monthly limit and hard limits that cannot be exceeded; GitHub Actions is free on standard runners for public repositories, with 2,000 included minutes per month for private repositories on GitHub Free (all as of 2026-11).
- **Slop looks like:** A launch checklist that says only "host it free somewhere," an invented limit ("10 GB free forever") with no source, or a production business quietly running on a personal-use-only tier.
- **Verify:** For every provider in the stack, open its official pricing or limits page, record the cap and the date checked in the project notes, and set a usage alert below the cap where the provider offers one.
- **Source:** Vercel Pricing, https://vercel.com/pricing ; Netlify Pricing, https://www.netlify.com/pricing/ ; GitHub Docs, "GitHub Actions billing," https://docs.github.com/en/billing/concepts/product-billing/github-actions
- **Owning departments:** D6 (DevOps, Deployment, Production, Hosting & Domains)
- **Skills that serve it:** free-tiers, hosting, ci-cd

## Part 5 — Reliability & observability

## Monitoring
- **What:** The continuous collection and display of metrics that show whether the system is healthy and serving users. It answers "is it working?" at a glance, before users complain.
- **How it works:** Services expose metrics (request rate, error rate, latency percentiles, CPU, memory, queue depth) to a time-series store such as Prometheus. Dashboards chart them; recording rules pre-aggregate expensive queries. Google's SRE practice centers user-facing systems on four golden signals: latency, traffic, errors, and saturation.
- **Why it exists:** Failures are inevitable; monitoring shortens the time between a failure starting and a human knowing about it.
- **If missing:** Outages are discovered via customer complaints and social media. Slow degradations (memory leaks, disk filling) run silently until they become hard failures.
- **Good looks like:** Google SRE book practice: every user-facing service has a dashboard built on the four golden signals, with latency tracked as percentiles (p50/p95/p99), not averages, and error latency separated from success latency.
- **Slop looks like:** A monitoring setup that only pings the homepage, or a dashboard copied from a tutorial that charts CPU while the checkout endpoint returns 500s unmeasured.
- **Verify:** Open the production dashboard for the service and confirm all four golden signals are charted for the last 24 hours; then run `promtool check rules` against the Prometheus config and confirm it parses with no errors.
- **Source:** Google, *Site Reliability Engineering*, "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/
- **Owning departments:** D12, D6
- **Skills that serve it:** monitoring, dashboards, apm

## Logging
- **What:** Timestamped, structured records of discrete events inside the system — requests, errors, state changes — kept centrally and searchable. Logs are the raw narrative you read when metrics say something is wrong.
- **How it works:** Applications emit structured (JSON) logs with consistent fields: timestamp, level, service, request or trace ID, and message. A shipper (Fluent Bit, the OpenTelemetry Collector) forwards them to a central store (Loki, Elasticsearch, Cloud Logging) with retention limits. Sensitive data is never logged, per the OWASP Logging Cheat Sheet.
- **Why it exists:** Metrics show *that* something failed; logs show *what* happened, in what order, for which request.
- **If missing:** Debugging becomes guesswork and reproduction attempts. Post-incident, there is no timeline, so the same failure recurs because its cause was never established.
- **Good looks like:** Every production log line is parseable JSON carrying a trace ID, so one user request can be followed across services; passwords, tokens, and card numbers are provably absent (OWASP logging guidance).
- **Slop looks like:** `console.log("here")` debugging statements shipped to production, plain-text logs with no request ID, and stack traces written to a local file on an ephemeral container that vanishes on restart.
- **Verify:** Pick one failed production request from the error tracker, copy its trace ID, and search the central log store — every service it touched must return matching entries. Then grep the application source for `console.log` in server code; the count in production paths must be zero.
- **Source:** OWASP, *Logging Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- **Owning departments:** D12, D4
- **Skills that serve it:** logging, error-tracking

## Alerting
- **What:** The rules that decide which signals page a human, and when. Alerting turns monitoring data into action; everything that does not need a human now is a ticket or a dashboard, not a page.
- **How it works:** Alert rules evaluate metric queries against thresholds, ideally tied to SLO burn rate (how fast the error budget is being consumed) rather than raw CPU. Alerts route through a manager (Alertmanager, PagerDuty) with deduplication, grouping, and escalation policies, and each alert links to a runbook.
- **Why it exists:** Humans cannot watch dashboards 24/7. Pages exist so that user-impacting problems wake someone while they are still small.
- **If missing:** Either nobody is told about real outages, or — the opposite failure — so many noisy pages fire that on-call staff mute them and miss the real one.
- **Good looks like:** Google SRE Workbook practice: multi-window, multi-burn-rate alerts on SLOs (for example, page when the error budget burns at a rate that would exhaust it in days, ticket at slower burn), each alert actionable and symptom-based.
- **Slop looks like:** An alert on "CPU > 80% for 1 minute" that fires every deploy, alerts with no runbook link, and a single email inbox as the escalation path for a revenue-critical service.
- **Verify:** Run `promtool check rules` on the alert rule files; then trigger one alert in staging (stop a staging service) and confirm the page reaches the on-call phone within the documented time and includes a runbook link.
- **Source:** Google, *The Site Reliability Workbook*, "Alerting on SLOs" — https://sre.google/workbook/alerting-on-slos/
- **Owning departments:** D12, D6
- **Skills that serve it:** alerting, monitoring, incident-response

## Backups
- **What:** Point-in-time copies of data (database, uploaded files, configuration) stored separately from production, kept on a schedule with defined retention. A backup is only real if it can be restored.
- **How it works:** Automated jobs take scheduled snapshots or dumps (for example, PostgreSQL base backups plus WAL archiving for point-in-time recovery) to object storage in a different failure domain, encrypted, with lifecycle rules expiring old copies. Backup success and failure are themselves monitored and alerted.
- **Why it exists:** Data loss — from bugs, bad migrations, ransomware, or provider failure — is the one failure class that cannot be fixed by redeploying code.
- **If missing:** A single destructive event (a dropped table, a compromised account) permanently destroys user data, and with it the business.
- **Good looks like:** PostgreSQL documented practice: scheduled base backups combined with continuous WAL archiving, so the database can be restored to any moment, not just the last nightly dump — and restores are rehearsed, not assumed.
- **Slop looks like:** A backup cron job that has been failing silently for months, backups stored on the same disk as the database, and a team that has never once performed a restore.
- **Verify:** Restore drill: restore the most recent production backup into a scratch instance (`pg_restore` or the provider's restore flow), run the application's smoke queries against it, and record the elapsed time. Also list the backup bucket and confirm a successful backup exists for every day in the retention window.
- **Source:** PostgreSQL documentation, "Backup and Restore" — https://www.postgresql.org/docs/current/backup.html
- **Owning departments:** D5, D6
- **Skills that serve it:** backup-recovery

## Rollback
- **What:** The ability to return a deployment to the previous known-good version quickly when a release causes harm. Rollback is the escape hatch that makes deploying safe.
- **How it works:** Releases are versioned and immutable; the platform keeps the previous version deployable (Kubernetes rollout history, blue/green slots, or the prior release artifact). Database changes use expand-and-contract migrations so the old code still runs against the new schema during a rollback window.
- **Why it exists:** Some defects only appear under real traffic. When they do, minutes matter; debugging forward under outage pressure is slower and riskier than reverting.
- **If missing:** A bad deploy becomes a full incident: the team hot-fixes under pressure, often introducing a second bug, while users stay broken.
- **Good looks like:** Kubernetes documented behavior: `kubectl rollout undo` returns a Deployment to its previous revision, and `kubectl rollout history` shows the revision record — the revert is one rehearsed command, not an improvisation.
- **Slop looks like:** "Rollback plan: redeploy from the main branch and hope," migrations that drop columns in the same release that stops using them, and no record of which version is currently live.
- **Verify:** In staging, deploy a deliberately broken version, then execute the documented rollback command and time it; the previous version must be serving and healthy within the project's target (for example, 5 minutes), with `kubectl rollout history` (or the platform equivalent) showing both revisions.
- **Source:** Kubernetes documentation, "Deployment" (rolling back a Deployment) — https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- **Owning departments:** D6, D4
- **Skills that serve it:** rollback, reliability

## Disaster recovery
- **What:** The plan and infrastructure for restoring service after a large-scale loss — a region outage, total data corruption, or a destroyed account. It is defined by two numbers: RTO (how long recovery may take) and RPO (how much data loss, measured in time, is acceptable).
- **How it works:** The team picks a strategy on the cost/recovery spectrum AWS documents — backup and restore, pilot light, warm standby, or multi-site active-active — replicates data to a separate region, keeps infrastructure as code so the stack can be rebuilt, and rehearses failover on a schedule.
- **Why it exists:** Single-system reliability measures do not help when the failure is the whole environment. Without a rehearsed plan, recovery time is measured in days of improvisation.
- **If missing:** A regional outage or account compromise is an existential event: no data copy elsewhere, no runbook, no practiced path back.
- **Good looks like:** AWS Well-Architected practice: RTO and RPO are written down per workload, the chosen strategy (for example, pilot light: RPO in minutes, RTO in tens of minutes) demonstrably meets them in a tested failover, and the test is repeated regularly.
- **Slop looks like:** A DR "plan" that is one wiki paragraph saying "restore from backups," never tested, with backups in the same region as production and no stated RTO or RPO.
- **Verify:** Run the DR game day: execute the failover runbook in the recovery region, measure actual RTO and data loss against the documented RTO/RPO targets, and file the timings in the runbook. If no game day has ever been run, the element fails verification.
- **Source:** AWS, *Disaster Recovery of Workloads on AWS*, "Disaster recovery options in the cloud" — https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html
- **Owning departments:** D6, D5
- **Skills that serve it:** backup-recovery, reliability, incident-response

## Observability
- **What:** The property of a system that lets you understand its internal state from its external outputs — asking new questions of production behavior without shipping new code. It is the discipline that monitoring, logging, and tracing serve together.
- **How it works:** Code is instrumented once, typically with OpenTelemetry, to emit three correlated signals: traces (the path of one request across services), metrics (aggregated measurements), and logs (events) — all carrying the same trace and resource attributes, exported through a collector to any backend.
- **Why it exists:** In distributed systems, failures emerge between services and cannot be reproduced locally. Correlated telemetry is how you find a cause you did not anticipate when writing the code.
- **If missing:** Every novel failure becomes a multi-hour hunt across disconnected tools, and the "fix" is adding more logs and redeploying — while the incident is still running.
- **Good looks like:** OpenTelemetry's documented model: an engineer starts from one slow request, opens its full trace waterfall across services, and pivots from a span directly to that service's logs for the same trace ID — no SSH, no guessing.
- **Slop looks like:** Three unrelated tools (metrics here, logs there, no tracing at all), each service logging in a different format, and no shared ID to connect them, marketed internally as "we have observability."
- **Verify:** Pick a random production request, take its trace ID from any log line or error report, and confirm you can reconstruct its complete cross-service path in the tracing backend within 5 minutes. If the trace is missing spans from any service it touched, instrumentation is incomplete.
- **Source:** OpenTelemetry documentation, "Observability primer" — https://opentelemetry.io/docs/concepts/observability-primer/
- **Owning departments:** D12, D4
- **Skills that serve it:** apm, logging, monitoring, error-tracking

## Incident response
- **What:** The rehearsed human process for handling a serious production failure: declaring the incident, coordinating the response, communicating status, resolving, and learning from it afterward.
- **How it works:** An on-call rotation receives the page. For major incidents, defined roles activate — an Incident Commander who coordinates and decides (but does not personally fix), subject-matter experts who investigate, a scribe who keeps the timeline, and a liaison who communicates with customers. Afterward, a blameless postmortem records timeline, root cause, and follow-up actions.
- **Why it exists:** Under outage pressure, uncoordinated experts duplicate work, contradict each other in public channels, and forget to tell users anything. Process converts panic into parallel, accountable work.
- **If missing:** The founder's phone is the escalation path, status pages stay green while the product is down, and the same incident recurs because no postmortem actions were ever tracked.
- **Good looks like:** PagerDuty's published incident response guide: the Incident Commander is the single authority on status, delegates all repair actions rather than performing them, and owns communication cadence until resolution — a structure adapted from the Incident Command System.
- **Slop looks like:** A "runbook" that is a chat message saying "restart the server and ping me," no on-call schedule, and postmortems that blame a person instead of fixing the system.
- **Verify:** Inspect the on-call tool: a named rotation with at least two levels of escalation must exist for the current week. Then check the last incident's record — it must name an incident commander, contain a timeline, and link a postmortem whose action items have owners and due dates.
- **Source:** PagerDuty, *Incident Response Guide*, "Different Roles" — https://docs.pagerduty.com/ops-guides/incident-response-guide/different-roles
- **Owning departments:** D6, D12
- **Skills that serve it:** incident-response, alerting, dashboards

## Performance budgets
- **What:** Explicit, agreed limits on how slow and how heavy a product may be — page weight, request latency, and user-experience metrics — treated as pass/fail criteria in the build, not aspirations reviewed after launch.
- **How it works:** The team sets budgets from user-experience thresholds (Core Web Vitals: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 at the 75th percentile) plus size limits (JavaScript bundle, image weight, API p95 latency). CI enforces them with tools such as Lighthouse CI; a change that breaches a budget fails the build until fixed or explicitly waived.
- **Why it exists:** Performance degrades by accumulation — every feature adds a little weight. Without a budget, no single change looks responsible, yet the product gets slower every month.
- **If missing:** Pages bloat until mobile users on mid-range phones and slow networks quietly leave; the regression is discovered in conversion data, months late and hard to attribute.
- **Good looks like:** web.dev practice: budgets are anchored to the Core Web Vitals thresholds (LCP 2.5s, INP 200ms, CLS 0.1), measured on real-user field data at the 75th percentile, and enforced per page template rather than as a site-wide average that hides bad pages.
- **Slop looks like:** A budget written in a strategy doc that nothing enforces, Lighthouse run once on the homepage on a fast desktop, and a 4 MB hero video shipped because "it looked fine on the office connection."
- **Verify:** Open the CI pipeline for the last merge: a performance check (for example, `lhci autorun`) must be present and passing against the budget file in the repo. Then confirm the budget file itself names numeric limits for LCP, INP, CLS, and bundle size.
- **Source:** web.dev, "Web Vitals" — https://web.dev/articles/vitals
- **Owning departments:** D12, D4
- **Skills that serve it:** performance-budgets, core-web-vitals, performance-optimization

## Error handling
- **What:** The deliberate design of what the system does when something fails — catching errors at boundaries, returning safe and consistent error responses, recording them with context, and degrading gracefully instead of crashing or leaking internals.
- **How it works:** Each layer handles the errors it can and converts the rest into a standard error contract (stable error codes, a user-safe message, a correlation ID). Unexpected exceptions go to an error tracker (for example, Sentry) with stack trace and context. Users see a helpful state — never a stack trace, SQL error, or raw 500 page; retries with backoff apply only to operations that are safe to repeat.
- **Why it exists:** Errors are guaranteed; their handling decides whether a failure is a minor user inconvenience or a security leak, a lost transaction, and an undebuggable mystery.
- **If missing:** Users hit white screens and cryptic failures, sensitive internals (file paths, queries, framework versions) leak to attackers, and the team never learns the errors happened at all.
- **Good looks like:** OWASP guidance in practice: every API error returns the same shape with a correlation ID, the full detail lands in the error tracker within seconds, and the user-facing message reveals nothing about the stack — verified behavior, not a style preference.
- **Slop looks like:** Empty `catch` blocks that swallow exceptions, `try/catch` around everything "just in case," error pages showing the framework's default debug screen in production, and failed payments that display "Success" because the failure path was never written.
- **Verify:** In staging, force failures: stop the database, submit an invalid payload, and call a non-existent route. Confirm each returns the standard error shape with a correlation ID, no stack trace or SQL text appears in any response, and each event shows up in the error tracker with the same correlation ID.
- **Source:** OWASP, *Error Handling Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html
- **Owning departments:** D4, D12
- **Skills that serve it:** error-handling, error-tracking, logging

## Cost optimisation
- **What:** The ongoing practice of making cloud and infrastructure spend track actual value: paying for the capacity you use, at the best available rate, and knowing which product or feature each unit of spend serves.
- **How it works:** Following the FinOps model (Inform, Optimize, Operate): billing data is ingested and allocated by tags or accounts so cost per service is visible; waste is removed (idle instances, oversized databases, orphaned storage); steady-state capacity is bought at commitment discounts; and budgets with anomaly alerts catch runaway spend early.
- **Why it exists:** Cloud billing is metered and unforgiving — a forgotten test cluster or a misconfigured autoscaler bills every hour until someone notices, and no invoice explains itself.
- **If missing:** The monthly bill grows faster than usage, nobody can say which feature costs what, and the first "optimisation" is an emergency that cuts capacity the product actually needed.
- **Good looks like:** FinOps Framework practice: over 90% of spend is allocated to owning teams, unit economics (cost per request, per customer) are reported alongside revenue, and rightsizing and commitment purchases are a routine cadence, not an annual panic.
- **Slop looks like:** One shared cloud account with no tags, a production-grade instance running a weekend side project for a year, and "cost optimisation" that means turning off the monitoring and backups.
- **Verify:** Open the cost dashboard: at least 90% of the last month's spend must be allocated to a named service or team via tags/accounts, a budget alert must exist for the account, and the most recent rightsizing or waste report must be less than one quarter old.
- **Source:** Microsoft Learn, "FinOps Framework overview" (FinOps Foundation framework) — https://learn.microsoft.com/cloud-computing/finops/framework/finops-framework
- **Owning departments:** D6, D12
- **Skills that serve it:** cloud-costs, scaling, performance-optimization

## Part 6 — Trust, reach & maintenance

## Security
- **What:** The set of controls that keeps an application, its data, and its users safe from unauthorized access, tampering, and abuse. It covers code, configuration, dependencies, and operations, not just login screens.
- **How it works:** Teams threat-model features before building them, apply secure defaults (parameterized queries, output encoding, least-privilege access), set HTTP security headers, encrypt data in transit and at rest, audit dependencies, and run security testing in CI before release.
- **Why it exists:** Every public application is scanned and attacked continuously; one exploitable flaw can expose every user's data at once.
- **If missing:** Broken access control or injection lets an attacker read or modify other users' data, hijack sessions, or take over accounts — usually silently and at scale.
- **Good looks like:** The OWASP Top 10 (2025 edition) used as a release checklist, with OWASP ASVS requirements traced to tests and a written threat model per major feature.
- **Slop looks like:** Authentication checked only in the UI while API endpoints trust the client, SQL built by string concatenation, debug endpoints left live in production, and "security" that is a login page in front of unprotected routes.
- **Verify:** Run `npx @cyclonedx/cyclonedx-npm` or the stack's dependency auditor plus an automated scan (e.g. OWASP ZAP baseline) in CI; inspect response headers with `curl -sI https://<host>` and confirm CSP, HSTS, and X-Content-Type-Options are present.
- **Source:** OWASP Top 10 — https://owasp.org/www-project-top-ten/
- **Owning departments:** D7 (Security & Hardening)
- **Skills that serve it:** owasp, threat-modelling, security-audit, penetration-testing, security-headers, encryption, session-security, api-security, auth-hardening, dependency-safety

## Secrets management
- **What:** The discipline of storing, distributing, rotating, and revoking credentials — API keys, database passwords, signing keys, tokens — outside of source code. A secret is anything that grants access by possession alone.
- **How it works:** Secrets live in environment variables or a dedicated manager (for example a cloud secret store or a vault), are injected at deploy time, scoped per environment, never logged, and rotated on a schedule and immediately on suspicion of exposure. Repos ship a `.env.example` with placeholder names only.
- **Why it exists:** Code is copied, forked, logged, and archived far beyond its author's control; anything committed travels with every copy forever, including git history.
- **If missing:** A single committed key gives attackers the database, the payment account, or the mail provider — and deleting the line later does not remove it from history.
- **Good looks like:** Gitleaks or an equivalent scanner running as a pre-commit hook and CI gate, `.env` files git-ignored from the first commit, and short-lived, least-privilege credentials per service.
- **Slop looks like:** A live Stripe key pasted into a config file "temporarily," production credentials shared in chat or committed in a `.env` that was "going to be removed later," and one master key reused across every environment.
- **Verify:** Run `gitleaks git .` against the full repository history and require zero findings; confirm `git check-ignore .env` succeeds and that `.env.example` contains names with no real values.
- **Source:** Gitleaks — https://github.com/gitleaks/gitleaks
- **Owning departments:** D7 (Security & Hardening)
- **Skills that serve it:** secrets-management, security-audit, supply-chain

## Privacy
- **What:** The practice of collecting only the personal data a product needs, using it only for stated purposes, protecting it, and honoring people's rights over it (access, correction, deletion, export). Privacy is about data handling, not just a policy page.
- **How it works:** Teams keep a data inventory (what is collected, why, where it lives, how long it is kept), minimize collection at the form and schema level, gate analytics and marketing tags behind consent where required, and build working request flows for access and erasure.
- **Why it exists:** Personal data is a liability as much as an asset: users trust products that handle it carefully, and regulations such as the GDPR make that handling a legal duty, not a preference.
- **If missing:** The product hoards data it cannot protect or justify, cannot answer a deletion request, and turns a breach or a regulator's question into an existential event.
- **Good looks like:** A GDPR-aligned setup: a record of processing activities, a data protection impact assessment for high-risk features, and a tested DSAR flow that actually deletes data across the database, backups policy, and third-party processors.
- **Slop looks like:** A privacy policy copied from another product naming data the app does not collect (and missing what it does), a cookie banner with no working reject path, and "delete account" that only hides the profile.
- **Verify:** Submit a test access and erasure request through the real product flow and confirm the data is returned, then absent from the database and admin views; inspect the data inventory against the live schema field by field.
- **Source:** GDPR, Regulation (EU) 2016/679, official text — https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/
- **Owning departments:** D14 (Legal, Privacy & Compliance)
- **Skills that serve it:** privacy-laws, data-residency, dsar-handling, cookie-consent, audit-trails

## Legal and compliance
- **What:** The layer of binding documents and obligations a product operates under: terms of service, privacy policy, cookie consent, age gates, content rules, and sector- or region-specific regulation. It defines what the product may do, not just what it can do.
- **How it works:** Obligations are identified per market and feature (payments, user-generated content, minors, health or finance data), translated into product requirements, implemented as real flows — consent capture, age checks, moderation, audit trails — and reviewed when features or markets change.
- **Why it exists:** A product that ignores its legal surface can be fined, delisted, sued, or forced to shut down a feature overnight, regardless of how well the code works.
- **If missing:** The team discovers obligations after launch: consent that was never valid, content it is liable for, users it was not allowed to serve, records it cannot produce.
- **Good looks like:** Terms and policies written for this product's actual data and features, versioned with acceptance records, a consent log with timestamps, and an audit trail for regulated actions such as refunds and data exports.
- **Slop looks like:** Legal pages generated from a generic template with another company's name left in, "by using this site you agree" with no record of agreement, and compliance claimed in marketing ("GDPR compliant," "PCI certified") that no process supports.
- **Verify:** Read the live terms and privacy policy against the product's actual data inventory and third-party list; create a test account and confirm consent and policy acceptance are recorded with version and timestamp.
- **Source:** GDPR, Regulation (EU) 2016/679, official text — https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/
- **Owning departments:** D14 (Legal, Privacy & Compliance)
- **Skills that serve it:** legal-documents, compliance-audit, age-requirements, privacy-laws, audit-trails, cookie-consent

## Licensing
- **What:** The legal permissions attached to the project's own code and to every third-party component it ships — libraries, fonts, images, and copied snippets. A license states who may use the work, and on what conditions.
- **How it works:** The project carries a LICENSE file chosen deliberately for its own code; dependencies are inventoried with their licenses, checked for compatibility (copyleft obligations, attribution duties, commercial-use limits), and notices are preserved in shipped artifacts.
- **Why it exists:** Code without a license is not free to use — default copyright applies. Incompatible or unnoticed obligations can force a project to open its source, pay, or rip out a component.
- **If missing:** The project silently accumulates legal exposure: a strong-copyleft library in a proprietary product, stock assets used beyond their terms, or the project's own code reused by others with no terms at all.
- **Good looks like:** A clear LICENSE (for example MIT, chosen via Choose a License) in the repo root, an SBOM or license report generated in CI, and attribution notices shipped with the product.
- **Slop looks like:** No LICENSE file at all, a license copied from a tutorial that names the wrong project, and vendored code or fonts dropped in with their license files deleted.
- **Verify:** Check the repo root for a LICENSE file matching the intended terms; run a license scan (for example `npx license-checker` on a Node project) and confirm every reported license is on the project's allowlist.
- **Source:** Choose a License (GitHub) — https://choosealicense.com/
- **Owning departments:** D14 (Legal, Privacy & Compliance)
- **Skills that serve it:** licensing, compliance-audit, supply-chain, dependency-safety

## Accessibility
- **What:** Building interfaces that people with disabilities can perceive, operate, and understand: screen-reader users, keyboard-only users, low-vision users, and people with motor or cognitive impairments. It is a quality property of the UI, not a plugin.
- **How it works:** Teams use semantic HTML first, manage focus visibly and logically, give every control an accessible name, meet contrast minimums, honor reduced-motion settings, and test with automated tools plus real assistive technology during development, not after launch.
- **Why it exists:** A significant share of every audience is locked out by inaccessible UI, and accessibility is a legal requirement for many products and public services.
- **If missing:** Buttons that are clickable divs, forms without labels, and dialogs that trap or lose focus make core flows impossible for assistive-technology users — defects as real as a broken checkout.
- **Good looks like:** WCAG 2.2 AA conformance as the release bar: axe-core checks in CI with zero critical violations, a full keyboard pass on every flow, and a screen-reader smoke test on the top user journeys.
- **Slop looks like:** Alt text missing or filled with file names, placeholder-only form labels, focus outlines removed for looks, click targets too small, and an "accessibility overlay" widget claimed as the fix.
- **Verify:** Run axe-core against the main pages (for example via `@axe-core/playwright` in the test suite) and require zero critical violations; then complete the primary flow keyboard-only, with no mouse, and confirm visible focus throughout.
- **Source:** WCAG 2.2, W3C Recommendation — https://www.w3.org/TR/WCAG22/ ; axe-core — https://github.com/dequelabs/axe-core
- **Owning departments:** D13 (Accessibility, i18n & Inclusive Design)
- **Skills that serve it:** wcag, accessibility-audit, screen-readers, keyboard-accessibility, reduced-motion, accessibility-law, inclusive-copy

## Internationalisation and RTL
- **What:** Engineering a product so it can be localized — translated text, locale-correct dates, numbers, currencies, and plurals — and so its layout works in right-to-left scripts such as Arabic and Urdu as well as left-to-right ones.
- **How it works:** No user-facing string is hard-coded; text lives in message catalogs keyed by meaning, formatting goes through locale APIs (ICU/Intl) driven by CLDR data, layouts use logical CSS properties (margin-inline-start, not margin-left), and direction is set with `dir` attributes so the whole UI mirrors correctly.
- **Why it exists:** Retrofitting i18n into a hard-coded product means touching every screen; RTL support bolted on late produces broken, mirrored-wrong layouts that native readers reject instantly.
- **If missing:** Dates and prices render in the wrong format, strings overflow their containers when translated, plural rules break in most languages, and the Arabic UI is a left-aligned LTR page with Arabic words pasted in.
- **Good looks like:** An ICU/CLDR-based stack (for example the platform `Intl` APIs or ICU4J/MessageFormat) with a complete message catalog, pseudo-localization in CI to catch overflow and hard-coded strings, and RTL visual checks on key screens.
- **Slop looks like:** English strings embedded in components, dates formatted by string concatenation, layouts built on physical left/right properties that collapse under `dir="rtl"`, and machine-translated text shipped without review.
- **Verify:** Switch the product to an RTL locale (ar or ur) and inspect the top flows for correct mirroring, readable text, and no clipped strings; grep the codebase for hard-coded user-facing strings outside the message catalog.
- **Source:** ICU — International Components for Unicode — https://icu.unicode.org/home
- **Owning departments:** D13 (Accessibility, i18n & Inclusive Design)
- **Skills that serve it:** internationalization, localization-workflow, rtl-layouts, inclusive-copy

## SEO/discoverability
- **What:** Making a product findable and understandable by search engines and answer engines: crawlable URLs, correct metadata, structured data, sitemaps, and content that answers real queries. Discoverability is engineered, not sprinkled on.
- **How it works:** Pages render meaningful HTML (server-side or static where it matters), each indexable page has a unique title, description, and canonical URL, structured data uses schema.org types that match the visible content, and sitemap plus robots rules keep crawlers on the pages that matter.
- **Why it exists:** For most products, search is the largest free acquisition channel; pages a crawler cannot render or interpret simply do not exist for that channel.
- **If missing:** The app ships as an empty JavaScript shell to crawlers, duplicate URLs split ranking signals, and key pages are blocked or noindexed by accident — traffic quietly goes to competitors.
- **Good looks like:** Google Search Central's developer guidance followed end to end: validated structured data (Rich Results Test clean), a current XML sitemap submitted in Search Console, and index coverage reviewed like a production dashboard.
- **Slop looks like:** The same title and meta description on every page, keyword-stuffed filler copy, structured data describing content the page does not show, and a staging `noindex` or robots block carried into production.
- **Verify:** Run the live URLs through Google's Rich Results Test and URL Inspection in Search Console; fetch `/robots.txt` and `/sitemap.xml` and confirm they exist, are correct, and list only canonical indexable URLs.
- **Source:** Google Search Central, SEO guide for developers — https://developers.google.com/search/docs/fundamentals/get-started-developers
- **Owning departments:** D9 (Content, SEO, AEO, GEO & Growth)
- **Skills that serve it:** technical-seo, on-page-seo, aeo, geo, web-analytics, seo-migration, rebrand-execution

## Analytics
- **What:** The instrumentation that records what users actually do in the product — events, funnels, retention, revenue — so decisions rest on observed behavior instead of opinion. Analytics covers both product analytics and the web analytics that feed discoverability work.
- **How it works:** Teams define an event taxonomy before building (event names, properties, naming rules), instrument key flows deliberately, route data to an analytics platform (for example GA4 or a privacy-respecting alternative), respect consent state, and review dashboards and data quality on a cadence.
- **Why it exists:** Without measurement, a team cannot tell whether a change helped, where users drop off, or which feature earns its maintenance cost.
- **If missing:** Decisions are made by loudest opinion; broken funnels and dead features stay invisible; and when a question finally comes — "did the redesign work?" — there is no baseline to answer it.
- **Good looks like:** A written tracking plan versioned with the code, consistent event naming, debug validation of every event before release (for example in GA4 DebugView), and consent mode so no data fires before the user agrees.
- **Slop looks like:** An analytics snippet pasted in and never configured, auto-collected pageviews as the entire strategy, duplicate or misspelled event names fragmenting every report, and dashboards showing numbers nobody defined or trusts.
- **Verify:** Perform the primary conversion flow in a test session and confirm each expected event arrives, correctly named and parameterized, in the platform's realtime/debug view; compare the live event list against the tracking plan document.
- **Source:** Google Analytics developer documentation — https://developers.google.com/analytics
- **Owning departments:** D12 (Analytics, Observability & Performance), D9 (Content, SEO, AEO, GEO & Growth)
- **Skills that serve it:** product-analytics, event-tracking, web-analytics, revenue-analytics

## Developer experience and maintenance
- **What:** How fast and safely a new developer (or agent) can get the project running, understand it, change it, and ship it — plus the ongoing work of updates, refactoring, and debt control that keeps the product changeable over years.
- **How it works:** A scripted, documented setup (one command to install, configure, and run), pinned tool versions, readable structure, semantic versioning and a changelog for releases, scheduled dependency updates, and a tech-debt register where shortcuts are recorded with owners instead of forgotten.
- **Why it exists:** Most of a product's cost is paid after launch, by whoever maintains it. Poor DX taxes every change; unmanaged debt compounds until change itself becomes the risk.
- **If missing:** Setup takes days of tribal knowledge, dependencies rot into unpatched vulnerabilities, releases are untraceable, and every fix risks breaking something nobody dares to touch.
- **Good looks like:** Semantic Versioning with a maintained CHANGELOG, a README that takes a fresh clone to a running app in minutes, automated dependency update PRs (reviewed, not ignored), and refactoring done in small, tested steps.
- **Slop looks like:** "Works on my machine" setup with undocumented manual steps, no lockfile or version pins, a changelog that stopped at v1.0, and TODO comments standing in for a debt process.
- **Verify:** From a clean clone in a fresh environment, follow only the README and time the path to a running app with tests passing; inspect the repo for a lockfile, a CHANGELOG with recent entries, and version tags matching releases.
- **Source:** Semantic Versioning 2.0.0 — https://semver.org/
- **Owning departments:** D15 (Developer Experience, Tooling & Maintenance)
- **Skills that serve it:** dev-environment, dependency-management, tech-debt, refactoring, legacy-migration, monorepo-tooling, code-generation, project-takeover, prototype-hardening

## Part 7 — Interface & experience

## Design system and design tokens
- **What:** A design system is the documented set of reusable styles, components, and rules for a product's interface; design tokens are its atomic values (color, spacing, type, radius, duration) stored as named data.
- **How it works:** Primitive tokens (e.g. `blue-600`) feed semantic tokens (`color-action-primary`), which components consume. Tokens live in one source file, often DTCG-format JSON, and are transformed into CSS variables, Tailwind config, or native constants per platform.
- **Why it exists:** It makes visual decisions explicit and shared, so forty screens stay consistent and a rebrand is a token change, not a rewrite.
- **If missing:** Every screen hard-codes its own hex values and spacing; drift accumulates until no two pages look related.
- **Good looks like:** The Design Tokens Format Module 2025.10 from the W3C Design Tokens Community Group standardizes token files with `$value`, `$type`, and aliases; GOV.UK and IBM Carbon publish full token-backed systems.
- **Slop looks like:** A "system" that is one gradient, one font, and copy-pasted cards, with raw hex values scattered through components and no semantic layer.
- **Verify:** Inspect the token source file; grep the codebase for hard-coded hex colors and pixel values outside it — the count should be near zero.
- **Source:** Design Tokens Format Module 2025.10 — https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
- **Owning departments:** D3
- **Skills that serve it:** design-system, design-tokens, rebrand-execution

## Component library
- **What:** The coded collection of reusable UI building blocks — buttons, inputs, dialogs, tables — each with defined props, variants, and states, documented for builders.
- **How it works:** Components are built once against tokens, published (package or shared folder), and documented with live examples, typically in Storybook, where each story captures one state. Pages are assembled from the library, not hand-built.
- **Why it exists:** It stops teams re-inventing the same button twelve ways and makes behavior (focus, keyboard, disabled) correct once, everywhere.
- **If missing:** Every page ships bespoke markup; a fix to "the button" must be repeated in dozens of places and inevitably is not.
- **Good looks like:** The GOV.UK Design System ships tested, accessible components with usage guidance; Storybook is the standard workshop for developing and documenting them in isolation.
- **Slop looks like:** A folder of near-duplicate components with inconsistent props, no stories, and pages that bypass the library with one-off markup.
- **Verify:** Run Storybook and confirm every library component has stories covering its variants and states; grep pages for raw `<button>`/`<input>` markup that duplicates a library component.
- **Source:** Structuring your Storybook — https://storybook.js.org/blog/structuring-your-storybook/ ; GOV.UK button component — https://design-system.service.gov.uk/components/button/
- **Owning departments:** D3
- **Skills that serve it:** component-library, frontend-core

## Layout and responsive design
- **What:** The grid, spacing, and breakpoint rules that arrange content so it works from a narrow phone to a wide monitor without horizontal scrolling or orphaned content.
- **How it works:** Layouts use CSS grid and flexbox with fluid units; breakpoints are added where the content breaks, not at device names, and container queries let a component respond to its own space. Images use `srcset`/`sizes` and reserved dimensions to avoid layout shift.
- **Why it exists:** Users arrive on every viewport size; a layout designed only at 1440px silently fails most of them.
- **If missing:** Fixed-width pages force pinch-zooming and horizontal scroll on mobile, sidebars crush content, and text lines run unreadably wide on desktop.
- **Good looks like:** web.dev's responsive design guidance: design for the small screen first, widen until the layout needs a major breakpoint, and keep text columns near 70–80 characters.
- **Slop looks like:** One desktop screenshot layout, a single `max-width: 768px` media query that stacks everything, and content hidden on mobile "because it didn't fit."
- **Verify:** Resize the browser from 320px to 1920px (or run a device-matrix screenshot pass) and check for horizontal scrollbars, overlap, and unreadable line lengths at each step.
- **Source:** GOV.UK layout style — https://design-system.service.gov.uk/styles/layout/ ; responsive design course — https://academia.sh/en/courses/layout-and-responsive-design
- **Owning departments:** D3
- **Skills that serve it:** layout-responsive, frontend-core

## Typography
- **What:** The type system: font choices, a modular size scale, line heights, weights, and rules for headings, body, captions, and data.
- **How it works:** A small set of text styles (e.g. display, heading, body, caption) is defined as tokens with size, line height, and tracking; fluid sizing with `clamp()` scales between viewports. Body text targets comfortable measure and line height; fonts are subset, self-hosted or efficiently loaded with `font-display`.
- **Why it exists:** Type carries most of the information on the web; hierarchy and readability are decided here, not by decoration.
- **If missing:** Sizes are picked per element, headings look like body text, and pages read as flat walls with no scannable structure.
- **Good looks like:** GOV.UK sets everything in one typeface on a fixed scale with defined heading and body styles, sentence case, and restrained use of bold.
- **Slop looks like:** Five font families, gradient or all-caps headline text, 12 arbitrary font sizes, and body copy at low contrast gray.
- **Verify:** Inspect computed styles across pages: count distinct font sizes and families (should match the token scale), and measure body line length and line height.
- **Source:** GOV.UK headings and typography styles — https://design-system.service.gov.uk/styles/headings/
- **Owning departments:** D3
- **Skills that serve it:** typography

## UI states (loading, empty, error, success)
- **What:** The designed appearance of every view in each condition it can be in: loading, empty (first use, no results, cleared), error, partial, and success.
- **How it works:** Each data-dependent view is specified as a state matrix. Loading uses skeletons matched to the final layout or a spinner for short waits; empty states explain what belongs here and offer the next action; errors say what happened in plain language and offer retry; success confirms the action completed.
- **Why it exists:** Real usage is mostly non-ideal states; users judge trustworthiness by how the product behaves when data is absent or something fails.
- **If missing:** Users face blank white screens, infinite spinners, and dead ends, and cannot tell "still loading" from "broken" from "nothing here."
- **Good looks like:** NN/g's empty-state guidelines: communicate system status, provide learning cues, and give a direct pathway to the key task — never leave a container silently blank.
- **Slop looks like:** A generic spinner for every wait, "No data" as the only empty copy, raw error codes or stack text shown to users, and no confirmation after actions.
- **Verify:** Throttle the network in DevTools, load each main view with an empty account, force an API error (block the request), and submit a form — screenshot all four states per view.
- **Source:** NN/g, Designing Empty States in Complex Applications — https://www.nngroup.com/articles/empty-state-interface-design/
- **Owning departments:** D3, D13
- **Skills that serve it:** ui-states

## Motion and animation
- **What:** The purposeful movement of interface elements — transitions, reveals, feedback — governed by shared duration and easing tokens.
- **How it works:** Motion is specified like any other token: standard durations and easing curves, applied to state changes and continuity (an element that moves shows where it went). Animations prefer `transform` and `opacity` for performance, and every non-essential animation is removed or replaced under `prefers-reduced-motion`.
- **Why it exists:** Done well, motion explains cause and effect and preserves context; it is feedback, not decoration.
- **If missing:** Interfaces feel abrupt and disorienting — content teleports, users lose track of what changed — or, at the other extreme, nothing in the brief constrains it and decoration takes over.
- **Good looks like:** web.dev's guidance on `prefers-reduced-motion`: build a motion-reduced variant for users who request it, and the W3C technique C39 for suppressing animation accordingly.
- **Slop looks like:** Bounce and parallax on everything, animations that ignore `prefers-reduced-motion`, inconsistent durations per component, and motion that blocks input.
- **Verify:** Enable "Reduce motion" in the OS or emulate `prefers-reduced-motion: reduce` in DevTools rendering settings, then traverse the site: non-essential animation must be gone while state changes remain clear.
- **Source:** MDN, prefers-reduced-motion — https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion ; W3C technique C39 — https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
- **Owning departments:** D3, D13
- **Skills that serve it:** motion

## Scroll experiences
- **What:** Deliberate behavior tied to scrolling: reveal-on-enter, scroll progress, pinned/sticky sections, parallax, and snap points.
- **How it works:** Modern implementations use CSS scroll-driven animations (`animation-timeline: scroll()` / `view()`) or IntersectionObserver, which run off the main thread or fire once, instead of scroll event handlers doing layout work per frame. Reveals are progressive enhancement: content is visible if the script or timeline never runs.
- **Why it exists:** Scroll is the primary navigation gesture on content pages; choreographing it can pace a story and signal reading progress.
- **If missing:** Either long pages are inert walls with no pacing, or (worse) the team bolts on scroll-jacking that fights the user's own scrolling.
- **Good looks like:** MDN's scroll-driven animation timelines: keyframes linked to scroll progress declaratively in CSS, performant because they avoid main-thread scroll listeners.
- **Slop looks like:** JavaScript scroll handlers causing jank, elements invisible until a script reveals them (blank page when JS fails), hijacked scrolling, and no reduced-motion fallback.
- **Verify:** Load the page with JavaScript disabled — all content must be present. Then scroll with DevTools performance recording and confirm no long tasks tied to scroll events.
- **Source:** MDN, Scroll-driven animation timelines — https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines ; CSS Scroll-Driven Animations spec — https://drafts.csswg.org/scroll-animations/
- **Owning departments:** D3
- **Skills that serve it:** scroll-experiences

## Client state management
- **What:** How the browser-side application holds and updates its own state — UI state (menus, selections, drafts), session state, and shared app state — separately from server data.
- **How it works:** State is classified first: local component state for one widget, a store (e.g. Redux, Zustand, or framework signals/context) for state shared across the app, and the URL for shareable state. Updates flow one way through explicit actions or setters, never by mutating shared objects in place.
- **Why it exists:** Without a model, state scatters across components, copies disagree, and bugs become "sometimes the cart shows the wrong total."
- **If missing:** Prop drilling, duplicated copies of the same fact, and screens that contradict each other until a refresh.
- **Good looks like:** Redux's documented principles: a single source of truth in one store, state is read-only, and changes happen only by dispatching actions through pure reducers.
- **Slop looks like:** Server data copied into a global store and hand-synchronized, global variables mutated from anywhere, and state stored in the DOM.
- **Verify:** Inspect the app: can every piece of shared state be traced to one owner and one update path? Change state in one view and confirm all dependent views update without a reload.
- **Source:** An intro to Redux and how state is updated (quoting the official Redux principles) — https://www.freecodecamp.org/news/an-intro-to-redux-and-how-state-is-updated-in-a-redux-application-839c8334d1b1/
- **Owning departments:** D3
- **Skills that serve it:** frontend-state, frontend-core

## Client data fetching
- **What:** How the client requests, caches, refreshes, and mutates server data, including loading and error states for every request.
- **How it works:** Server state is kept in a dedicated query cache keyed by query key, with per-query freshness (`staleTime`), background refetching on mount/focus/reconnect, request deduplication, retries with backoff, and mutations that invalidate or optimistically update affected queries — as implemented by TanStack Query or framework loaders.
- **Why it exists:** Server data is shared, asynchronous, and changes without the client knowing; treating it like local state causes stale screens and duplicate requests.
- **If missing:** Every component fetches in `useEffect`, the same endpoint is hit five times per page, and users see yesterday's data labeled as current.
- **Good looks like:** TanStack Query's documented defaults: cached data is stale immediately unless `staleTime` says otherwise, stale queries refetch in the background, and failed queries retry three times with exponential backoff before surfacing an error.
- **Slop looks like:** Fetch-on-mount in every component with no cache, no cancellation (race conditions on fast navigation), spinners that flash on every revisit, and errors swallowed silently.
- **Verify:** Open DevTools Network, navigate between two views repeatedly: the endpoint should be requested once, then served from cache with background revalidation; go offline mid-session and confirm a designed error state.
- **Source:** TanStack Query, Important Defaults — https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults
- **Owning departments:** D3
- **Skills that serve it:** data-fetching

## Client routing
- **What:** The mapping between URLs and views in a single-page application: route definitions, parameters, nested layouts, navigation, and not-found handling, without full page reloads.
- **How it works:** A router (e.g. React Router's data routers, or file-based routing in Next.js/Nuxt) matches the path, renders nested layouts around an outlet, and runs route loaders/actions for data and mutations. Links use the router's component; guards redirect unauthenticated users; unknown paths render a designed 404 view; scroll position and focus are managed on navigation.
- **Why it exists:** URLs are the web's sharing and bookmarking mechanism; an app whose views have no real URLs breaks deep links, the back button, and SEO.
- **If missing:** Navigation is a state flag, refresh loses your place, the back button exits the app, and no page can be linked to.
- **Good looks like:** React Router data routers: routes defined as objects with loaders that fetch before render and `errorElement` boundaries per route.
- **Slop looks like:** Hash-only URLs for a public site, `<a href>` full reloads inside the SPA, route guards treated as security (they are UX only — the API must still authorize), and a blank screen on unknown paths.
- **Verify:** Deep-link directly to a nested route in a fresh tab, use back/forward through five views, and visit a nonsense URL — each must land on the correct view or the designed 404.
- **Source:** React Router guide (data routers, loaders, error boundaries) — https://micropyramid.com/blog/react-router-for-navigation/
- **Owning departments:** D3
- **Skills that serve it:** client-routing

## Forms
- **What:** The data-entry surfaces of the product: fields, labels, validation, error handling, submission, and confirmation.
- **How it works:** Every control has a visible, programmatically associated label; instructions and format hints appear before or within the label, not only in errors; required fields are marked in text; validation runs on blur/submit and reports errors inline, tied to the field with `aria-describedby` and `aria-invalid`, with an error summary for multiple failures. `autocomplete` attributes let browsers fill known data; submission prevents duplicates and confirms the result.
- **Why it exists:** Forms are where users give the product data, money, and trust; most abandonment and most accessibility failures happen here.
- **If missing:** Users guess formats, lose entered data to unclear errors, and screen-reader users cannot tell which field failed.
- **Good looks like:** The W3C WAI forms guidance: associate a label with every control, put instructions where screen readers in forms mode will read them, and help users find, understand, and correct mistakes.
- **Slop looks like:** Placeholder text used as the only label, "Invalid input" errors, red borders with no text, validation on every keystroke, and forms that clear all input after one error.
- **Verify:** Submit the form empty and with one bad field using only the keyboard, then with a screen reader: focus must move to an error summary, each error must name its field and fix, and entered data must survive.
- **Source:** W3C WAI, Developing for Web Accessibility (labels, instructions, error help) — http://www.w3.org/WAI/tips/developing/
- **Owning departments:** D3, D13
- **Skills that serve it:** forms

## Data visualisation
- **What:** Charts, graphs, and data tables that turn numbers into a readable statement, chosen to match the question the data answers.
- **How it works:** Start from the message (change over time, comparison, share, correlation, flow, geography), then pick the chart family that answers it — lines for time, bars for comparison, scatter for correlation. Bars start at zero, series are labeled directly where possible, color encodes meaning (one accent, gray for context), and every chart ships with an accessible table or text alternative.
- **Why it exists:** A well-chosen chart shows a pattern in seconds; a poorly chosen one hides or distorts it.
- **If missing:** Teams default to whatever the charting library renders first, and dashboards become decoration that no one can read a decision from.
- **Good looks like:** Datawrapper's Academy guide: the chart's main statement acts as a compass for type, title, and color, and whole chart families can be ruled out once the goal is named.
- **Slop looks like:** 3D pie charts with twelve slices, dual axes implying false correlation, rainbow palettes, truncated bar axes, and charts with no axis labels or source.
- **Verify:** For each chart, state its one-sentence message and check the type matches it; confirm bar axes start at zero and that a data table or aria-described summary exists.
- **Source:** Datawrapper, A friendly guide to choosing a chart type — https://www.datawrapper.de/blog/chart-types-guide
- **Owning departments:** D3
- **Skills that serve it:** data-visualisation

## PWA and offline
- **What:** Progressive Web App capability: a web app manifest (name, icons, display mode) plus a service worker that caches the app shell and data so the app installs and works offline or on poor networks.
- **How it works:** The service worker registers on load, precaches the shell on `install`, cleans old caches on `activate`, and intercepts `fetch` events with a per-resource strategy — cache-first for static assets, network-first or stale-while-revalidate for data. Cache names are versioned so updates actually reach users.
- **Why it exists:** Connectivity is intermittent for much of the world; an app that dies with the network loses users at exactly the moments they need it.
- **If missing:** A dropped connection shows the browser's error page, repeat visits reload everything, and there is no install path.
- **Good looks like:** MDN's PWA guidance: the app splits into the main UI code and the service worker, which caches resources at install and serves them through the fetch event with an explicit strategy.
- **Slop looks like:** A manifest added "for the badge" with no working service worker, cache-everything-forever strategies that serve stale apps for weeks, and offline pages that are the browser default.
- **Verify:** In DevTools Application tab, confirm the service worker is active and the manifest parses; then use Network "Offline" throttling, reload, and complete the app's core task end to end.
- **Source:** MDN, Offline and background operation — https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation
- **Owning departments:** D3
- **Skills that serve it:** pwa-offline

## WebGL and 3D
- **What:** GPU-accelerated 2D/3D rendering in the browser via the WebGL API (or WebGPU), usually through a library such as Three.js or Babylon.js, rendered into a `<canvas>`.
- **How it works:** JavaScript control code and GLSL shaders run on the GPU: geometry goes into buffers, vertex shaders position it, fragment shaders color it, and a render loop draws frames. Professional work adds context-loss handling, device-pixel-ratio caps, quality scaling for weak GPUs, and a static fallback image or content when WebGL is unavailable.
- **Why it exists:** Product configurators, maps, data scenes, and interactive visuals need real-time 3D that DOM and SVG cannot deliver.
- **If missing:** Teams fake 3D with heavy video or GIF (huge, non-interactive), or ship raw WebGL that crashes silently on devices without GPU support.
- **Good looks like:** MDN's WebGL tutorial pattern: obtain the context, check for `null` (unsupported) and bail out with a message, and build up from shaders, buffers, and textures — with frameworks like Three.js encapsulating the boilerplate.
- **Slop looks like:** A full-screen WebGL hero that blocks content, drains battery, has no fallback when the context fails, ignores reduced motion, and leaves keyboard and screen-reader users with an empty canvas.
- **Verify:** Block WebGL in the browser (or use a device without it) and confirm the fallback renders; profile the page on a low-end phone for frame rate and check the canvas has a text alternative.
- **Source:** MDN, Getting started with WebGL — https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL
- **Owning departments:** D3
- **Skills that serve it:** webgl-3d

## Part 8 — AI features

## LLM integration
- **What:** The server-side layer that calls a hosted or self-hosted model API, manages keys, timeouts, retries, streaming, and structured outputs. It turns a nondeterministic model into a bounded application dependency.
- **How it works:** Application code sends a system prompt, conversation history, and optional tools to the provider; it enforces a JSON Schema for the reply, validates the result, handles rate limits with backoff, and falls back to a smaller model or a non-AI path on failure.
- **Why it exists:** Without an integration contract, model behavior, latency, and cost leak into every feature. A single wrapper centralizes model choice, versioning, and error handling.
- **If missing:** Features call the API ad hoc, parse free text with fragile string matching, hang on provider errors, and break silently when a model is deprecated.
- **Good looks like:** OpenAI documents Structured Outputs with `strict: true` so responses adhere to a supplied JSON Schema instead of only being valid JSON, enabling robust production flows. Timeouts, idempotency keys, and a tested fallback complete the pattern.
- **Slop looks like:** A chatbot widget pasted from a tutorial, API key exposed in client code, no timeout, no schema validation, and `JSON.parse` on raw model text.
- **Verify:** Inspect the LLM client module for timeout, retry, and schema validation; run the integration test suite with the provider mocked to return malformed JSON and a 429, and confirm the fallback path executes.
- **Source:** OpenAI, Introduction to Structured Outputs — https://developers.openai.com/cookbook/examples/structured_outputs_intro?translationFallback=es-419
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** llm-integration, ai-cost-control, ai-retrofit

## Prompt engineering
- **What:** The disciplined authoring, versioning, and testing of system and user prompts that steer model behavior. Prompts are treated as source code, not copy.
- **How it works:** Prompts live in versioned files or a prompt registry with a clear task description, context, step-by-step instructions, few-shot examples, and an explicit output format. Changes go through review and are tested against an eval set before release.
- **Why it exists:** Small wording changes can shift accuracy, tone, and format compliance. Untracked prompts edited in a dashboard cannot be reviewed, rolled back, or reproduced.
- **If missing:** Behavior drifts between environments, regressions appear after silent edits, and no one can explain why output quality changed.
- **Good looks like:** Anthropic's prompting best practices advise being clear and direct, being specific about output format and constraints, and providing instructions as sequential steps. Teams pair that guidance with stored examples inside structured tags and a colleague test for clarity.
- **Slop looks like:** One vague paragraph — "you are a helpful assistant, answer nicely" — hard-coded in three places, no examples, no version, and prompt fixes shipped without any test.
- **Verify:** Check the repository for a prompts directory under version control; run `git log` on a prompt file to confirm history, and run the prompt regression eval after a deliberate wording change.
- **Source:** Anthropic, Prompting best practices — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** prompt-engineering

## AI safety and guardrails
- **What:** Input, output, and tool guardrails that constrain what the model may receive, produce, and do. It covers moderation, topical limits, prompt-injection defenses, and least-privilege tool access.
- **How it works:** User input is screened before or in parallel with the main call; retrieved content is treated as untrusted data, not instructions; outputs are validated before display; state-changing tools require deterministic policy checks in application code, not model judgment alone.
- **Why it exists:** A language model cannot reliably distinguish instructions from data in the same token stream, so attackers can hide directives in messages, documents, or web pages the model reads.
- **If missing:** The feature leaks system context or sensitive data, executes injected instructions, generates policy-violating output, or takes excessive actions with user permissions.
- **Good looks like:** OpenAI's guardrails cookbook implements input guardrails for topical limits, jailbreaking, and prompt injection, and output guardrails that validate generated content, noting the accuracy, latency, and cost trade-off. OWASP lists Prompt Injection as LLM01.
- **Slop looks like:** No moderation on input or output, retrieved web text concatenated directly into the system prompt, and a model allowed to call payment or deletion tools unchecked.
- **Verify:** Run a red-team test set containing direct and indirect injection payloads in documents and user messages; inspect that tool calls pass a server-side allowlist and that blocked inputs return a safe fallback.
- **Source:** OWASP Top 10 for LLM Applications — https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-slides-v1_0_1.pdf ; OpenAI, How to implement LLM guardrails — https://developers.openai.com/cookbook/examples/how_to_use_guardrails
- **Owning departments:** D17 (AI Features & Applied ML), D7 (Security)
- **Skills that serve it:** ai-safety

## RAG and retrieval
- **What:** Retrieval-augmented generation grounds answers in a private or current corpus by retrieving relevant chunks at query time and citing them in the prompt. The model generates; the retriever supplies facts.
- **How it works:** Documents are split into chunks, embedded, and stored in a vector index with metadata. At query time the question is embedded, top candidates are retrieved, optionally reranked, filtered by permissions, and inserted as context with an instruction to answer only from that context or say it does not know.
- **Why it exists:** Models have a training cutoff, no access to private data, and hallucinate when asked beyond their knowledge. Retrieval makes answers current, attributable, and correctable by fixing the corpus.
- **If missing:** The assistant invents policies, prices, and product details, cannot cite sources, and stays wrong until the next model release.
- **Good looks like:** OpenAI's RAG cookbook combines a vector store such as Qdrant with few-shot examples to improve correctness and reduce hallucinations, and evaluates the result. Google's ranking API documentation describes reranking retrieved candidates by how well a document answers the query.
- **Slop looks like:** Whole PDFs dumped into the prompt, no chunking or permission filter, no citations, and no check that retrieved text actually supports the answer.
- **Verify:** Ask questions whose answers exist in one indexed document and questions with no answer in the corpus; inspect traces to confirm retrieved chunk IDs, permission filtering, citations, and an abstention on the unanswerable set.
- **Source:** OpenAI, Fine-Tuning for retrieval augmented generation (RAG) with Qdrant — https://developers.openai.com/cookbook/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant ; Google Cloud, Improve search and RAG quality with ranking API — https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** rag-retrieval, embeddings-search

## Embeddings and semantic search
- **What:** Embeddings map text to dense vectors so meaning, not just keywords, can be compared. Semantic search retrieves items whose vectors are nearest to the query vector.
- **How it works:** An embedding model encodes documents offline and queries at runtime; a vector database or approximate nearest-neighbor index returns candidates by cosine or dot-product similarity. Teams choose model, dimension, chunking, and hybrid keyword-plus-vector retrieval based on evals.
- **Why it exists:** Keyword search misses synonyms and paraphrases. Embeddings let "refund for a broken charger" match a returns policy that never uses those words.
- **If missing:** Search stays brittle, related content is invisible, and RAG, recommendations, and deduplication have no reliable similarity signal.
- **Good looks like:** OpenAI documents that embeddings measure relatedness of text strings, that distance between vectors measures relatedness, and that vectors can be stored in a vector database for search, clustering, and recommendations. Model choice is recorded with its dimension.
- **Slop looks like:** A new embedding model swapped in without re-indexing, vectors compared across incompatible models, or semantic search shipped with no keyword fallback for exact names and codes.
- **Verify:** Run a fixed query set with known relevant items and measure recall at K before and after any model change; inspect index metadata to confirm a single embedding model and dimension across the corpus.
- **Source:** OpenAI, Vector embeddings — https://developers.openai.com/api/docs/guides/embeddings
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** embeddings-search, search-relevance

## Recommendations
- **What:** A system that ranks items for a specific user or item context — related products, next articles, people or tools to try — using behavior, content similarity, and business rules.
- **How it works:** The product catalog and user events (views, clicks, purchases) are ingested; a model or rules engine generates candidates, filters out purchased, unavailable, or ineligible items, ranks them, and serves a list through an API or serving config with a popularity fallback for cold start.
- **Why it exists:** Catalogs are too large to browse. Relevant recommendations increase discovery and conversion, while random or purely popular lists waste the surface.
- **If missing:** Users see the same global bestsellers everywhere, new items never surface, and recommendation slots are filled by hand or left empty.
- **Good looks like:** Google Cloud documents that Vertex AI Search for commerce returns ranked product identifiers only after products are uploaded, user events are recorded, and a trained model and active serving config exist; new events can take time to be reflected in the model.
- **Slop looks like:** "Recommended for you" that is identical for every visitor, recommends out-of-stock or already purchased items, and logs no events to learn from.
- **Verify:** Request recommendations as two different test users with different histories and confirm the lists differ; check that excluded and out-of-stock items never appear and that a cold-start user receives the documented fallback.
- **Source:** Google Cloud, Get recommendations — https://cloud.google.com/retail/docs/predict
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** recommendations

## Search relevance
- **What:** The measurement and tuning of how well search orders results for a query, combining lexical matching, semantic similarity, freshness, popularity, and business boosts. Relevance is a measured property, not an opinion.
- **How it works:** Retrieval first gathers a candidate set, then a ranking stage scores and orders it. Teams maintain a judgment set of queries with graded relevance labels, compute metrics such as NDCG at K offline, and validate changes with online click and conversion signals before rollout.
- **Why it exists:** Default ranking rarely matches a product's intent. Without a judgment set, every stakeholder anecdote triggers a tweak that helps one query and silently harms hundreds of others.
- **If missing:** Search returns technically matching but useless results, zero-result queries go unnoticed, and ranking changes ship on vibes with no regression check.
- **Good looks like:** Google Cloud documents custom ranking in Vertex AI Search as a weighted expression over signals such as semantic relevance, keyword similarity, and document fields, tuned systematically. NDCG is documented as normalized by the ideal ranking, bounded 0 to 1, and comparable across queries.
- **Slop looks like:** Boosting whatever a manager searched for, no labeled test queries, sorting by date and calling it relevance, or an LLM reranker with no latency or quality budget.
- **Verify:** Run the offline evaluation script on the versioned judgment set and compare NDCG@10 against the previous release; inspect the search analytics report for zero-result and reformulated queries.
- **Source:** Google Cloud, Customize search results ranking — https://cloud.google.com/generative-ai-app-builder/docs/custom-ranking ; NDCG — https://metricgate.com/docs/ndcg/
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** search-relevance

## AI evaluation
- **What:** Repeatable tests that score an AI feature against a fixed dataset of realistic inputs and expected outcomes. Evals are the unit tests of nondeterministic features.
- **How it works:** A golden dataset holds inputs, reference answers or required facts, and edge cases. A runner executes the current prompt and model; graders — exact checks, rubric scoring, or a calibrated model judge — produce pass rates and per-category breakdowns stored with each change.
- **Why it exists:** Model and prompt changes can improve one behavior and regress another invisibly. Without a score, teams cannot tell whether a change helped, choose between models, or catch provider-side drift.
- **If missing:** Quality is judged by trying three chats manually, regressions reach users, and every model upgrade becomes an unmeasured gamble.
- **Good looks like:** OpenAI's Evals cookbook defines a dataset of question-answer pairs, configures an LLM-based pass/fail grader against ground truth, and runs the same eval across models to compare them. Failed cases from production are added back to the dataset.
- **Slop looks like:** No dataset, a judge trusted without checking its agreement with human labels, or an eval run once at launch and never again.
- **Verify:** Inspect the eval dataset and latest report in the repository; change the model or prompt in a branch, rerun the eval command, and confirm scores are recorded and a regression blocks merge.
- **Source:** OpenAI, Evals API Use-case - Web Search Evaluation — https://developers.openai.com/cookbook/examples/evaluation/use-cases/web-search-evaluation
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** ai-evaluation

## AI observability and cost control
- **What:** Tracing, logging, and budgeting for every model call: prompt and model version, tokens in and out, latency, cost, retrieval sources, and user feedback. It makes AI spend and failure modes visible per feature and per user.
- **How it works:** Each request emits a trace with child spans for retrieval, guardrails, tools, and generation, plus usage metadata. Dashboards aggregate cost by model and feature; alerts fire on budget thresholds, error spikes, or latency regressions; per-user quotas and cheaper-model routing enforce limits.
- **Why it exists:** Token billing is usage-based and unbounded by default. A loop, a long-context feature, or an abusive user can multiply spend overnight, and without traces a bad answer cannot be reproduced or diagnosed.
- **If missing:** The first signal of a problem is the provider invoice, hallucinations cannot be traced to a prompt or retrieved chunk, and no one knows which feature loses money.
- **Good looks like:** LangSmith documents automatic recording of LLM token usage and costs, with breakdowns in individual traces, project stats, and dashboards, including input and output token categories. Mature teams pair that tracing with hard token budgets and a non-AI fallback when a cap is hit.
- **Slop looks like:** No usage logging, one shared API key for every feature, retries with no cap, and the largest model used for trivial classification tasks.
- **Verify:** Open the tracing dashboard for a test request and confirm prompt version, token counts, cost, and retrieval spans are present; set a low test budget, exceed it, and confirm the alert fires and the fallback engages.
- **Source:** LangChain, LangSmith Cost tracking — https://docs.langchain.com/langsmith/cost-tracking
- **Owning departments:** D17 (AI Features & Applied ML)
- **Skills that serve it:** ai-observability, ai-cost-control

## Part 9 — Customer experience

## Support ticketing
- **What:** A system that converts every customer request, from any channel, into a tracked ticket with an owner, a status, and a full conversation history.
- **How it works:** Requests arrive by email, web form, chat, or API; each becomes a ticket carrying requester, assignee, priority, type, and tags. Triggers auto-acknowledge receipt, agents reply publicly or add internal notes, and status moves New → Open → Pending → Solved → Closed under views and SLAs that drive triage.
- **Why it exists:** It gives every request one queue, one owner, and one auditable record, so nothing depends on who happened to see an email.
- **If missing:** Support is a shared inbox or a mailto link; two agents answer the same question differently, urgent issues sit unseen, and there is no record when a customer disputes what was promised.
- **Good looks like:** Zendesk's documented model: all channels funnel into one ticket record with defined statuses, a creation trigger that emails the customer a trackable link, and separate Tickets (agent) and Requests (customer) API views.
- **Slop looks like:** A Contact page whose form posts to an endpoint that stores nothing and sends no email, while the page claims "we reply within 24 hours."
- **Verify:** Submit a test request from an external address; confirm a ticket ID is created, an acknowledgment email arrives, the ticket appears in the agent queue, and a reply reaches the customer.
- **Source:** Zendesk Tickets API documentation — https://developer.zendesk.com/api-reference/ticketing/tickets/tickets
- **Owning departments:** D18 (Customer Experience & Support)
- **Skills that serve it:** support-ticketing

## In-app chat
- **What:** A messenger embedded in the product or site where users start a conversation with support without leaving the page they are stuck on.
- **How it works:** A JavaScript snippet or mobile SDK loads the messenger with the workspace ID; signed-in users are identified with user ID, email, and a server-signed JWT, so conversations attach to the right account and cannot be impersonated. Conversations route to a shared inbox with office hours, automated first responses, and handoff to a human or a ticket.
- **Why it exists:** It captures help requests at the moment of friction, with the user's identity and context attached, instead of forcing users to go find support.
- **If missing:** Users must hunt for an email address, leave the product, and re-explain their account and problem from scratch; many abandon silently instead.
- **Good looks like:** Intercom's documented install: snippet before `</body>` on every page, Messenger enabled in settings, identity verified with server-generated JWTs, and the installation tested before going live.
- **Slop looks like:** A chat bubble copied from a tutorial that loops a generic bot script, never reaches a human, and collects messages nobody monitors.
- **Verify:** Open the app logged in and logged out and start a conversation in each state; confirm both land in the team inbox with the correct identity, and that a forged user ID is rejected.
- **Source:** Intercom developer documentation, Messenger installation — https://developers.intercom.com/installing-intercom/web/installation
- **Owning departments:** D18 (Customer Experience & Support)
- **Skills that serve it:** in-app-chat

## Help center
- **What:** A public, searchable knowledge base of help articles that lets customers solve common problems themselves, at any hour.
- **How it works:** Content is organized as categories → sections → articles, built in setup mode, branded, then activated. Articles are written from real ticket patterns, kept single-purpose, and surfaced inside the product, the chat widget, and agent replies, so self-service and support reinforce each other.
- **Why it exists:** Most support questions repeat; a help center answers them instantly at near-zero marginal cost and measurably reduces ticket volume.
- **If missing:** Every repeated question becomes a ticket, response times grow for everyone, and users who find no answer assume the product is unsupported.
- **Good looks like:** Zendesk Guide's documented flow: enable the help center in setup mode, structure categories, sections, and articles, add a customer portal for ticket submission and tracking, and activate only when ready.
- **Slop looks like:** A "Help" page with three generic FAQs written at launch, screenshots from an old UI version, and no working search — decoration, not self-service.
- **Verify:** Take the five most common real support questions; as an unauthenticated visitor, answer each using only help-center search, and confirm every article link resolves and matches the current UI.
- **Source:** Zendesk, "Getting started with your help center" — https://support.zendesk.com/hc/en-us/articles/4408846795674-Getting-started-with-your-help-center
- **Owning departments:** D18 (Customer Experience & Support)
- **Skills that serve it:** help-center

## User onboarding
- **What:** The guided first-run experience — welcome, setup steps, and a first core action — that takes a new signup from account creation to real use.
- **How it works:** A welcome step captures intent; a short checklist sequences the essential tasks, and each item completes on a real product event rather than a page view. Tooltips and tours teach by doing, progress persists across sessions, and different personas get different paths where their activation steps differ.
- **Why it exists:** Signup is not adoption; without guidance, new users face an empty product, cannot tell what to do first, and leave before experiencing any value.
- **If missing:** New users land on an empty dashboard with no next step, bounce in the first session, and the acquisition effort that brought them is wasted.
- **Good looks like:** Appcues' documented pattern: define the activation goal first, keep the checklist short (its editor suggests six or fewer items), mark items complete on real events, and follow up based on each user's checklist state.
- **Slop looks like:** A fourteen-step modal tour that fires on every login, cannot be dismissed permanently, and teaches features the user's plan does not include.
- **Verify:** Create a fresh test account and onboard using only in-product guidance; confirm each checklist item ticks only when its real event fires, and that a second login does not restart the tour.
- **Source:** Appcues documentation, "Build effective Checklists" — https://appcues.helpjuice.com/checklists/checklist-best-practices
- **Owning departments:** D18 (Customer Experience & Support), D1 (Product & Requirements)
- **Skills that serve it:** user-onboarding

## Activation
- **What:** The measurable moment a new user first receives the product's core value, defined as a specific instrumented event that predicts retention.
- **How it works:** The team names the aha-moment action, instruments it as an event, and validates with cohort analysis that users completing it early retain better than those who do not. Onboarding, checklists, and nudges are then aimed at that event, and the activation rate is tracked as a funnel metric with one shared definition.
- **Why it exists:** Most retention problems are activation problems; a team cannot improve a funnel step it has never defined or measured.
- **If missing:** Teams optimize signups and page views while the actual value moment goes unmeasured, onboarding debates run on opinion, and churn stays unexplained.
- **Good looks like:** Amplitude's documented approach: find the aha moment, align product, marketing, and data on one activation definition, validate it against retention with behavioral analytics, then remove friction at the funnel step where users stall.
- **Slop looks like:** Declaring "activation = signed up," or copying another product's famous milestone, with no validation against your own retention data.
- **Verify:** In analytics, compute last month's signup-cohort activation rate and compare 30-day retention of activated versus non-activated users; the written definition must match the instrumented event exactly.
- **Source:** Amplitude, "Driving product engagement by obsessing over activation" — https://amplitude.com/blog/getting-started-activation
- **Owning departments:** D18 (Customer Experience & Support), D1 (Product & Requirements), D12 (Analytics, Observability & Performance)
- **Skills that serve it:** activation-metrics

## Trial conversion
- **What:** The system that moves trial users into paid subscriptions at trial end: reminders, payment-method capture, and a defined outcome for every trial state.
- **How it works:** The subscription is created with a trial end date; the billing platform fires a trial-will-end webhook several days before expiry, triggering reminder emails and in-app prompts. The team chooses card-upfront or no-card trials and configures what happens with no payment method — invoice, pause, or cancel — rather than inheriting defaults.
- **Why it exists:** Trials convert on momentum and clarity; silence at expiry produces surprise charges for some users and silent lapses for others.
- **If missing:** Users are charged without warning, generating refunds, chargebacks, and angry tickets — or trials quietly expire with no prompt, leaking the revenue the trial existed to create.
- **Good looks like:** Stripe's documented trial mechanics: `trial_end` or `trial_period_days` at creation, the `customer.subscription.trial_will_end` event to prompt for a payment method, and explicit missing-payment-method behavior.
- **Slop looks like:** A "14-day free trial" banner on the marketing site while the product has no trial state at all — full price charged on day one, or trial access that never expires.
- **Verify:** In test mode, run a subscription with a one-day trial; confirm the trial-will-end webhook fires, the reminder email sends, and at expiry the subscription transitions exactly as configured for both card and no-card cases.
- **Source:** Stripe, "Use free trial periods on subscriptions" — https://docs.stripe.com/billing/subscriptions/trials/free-trials
- **Owning departments:** D18 (Customer Experience & Support), D1 (Product & Requirements)
- **Skills that serve it:** trial-conversion

## Feedback loops (in-product)
- **What:** Built-in channels — NPS and CSAT surveys, post-resolution ratings, feature requests — that capture user sentiment inside the product and route it to teams who can act on it.
- **How it works:** Surveys trigger at lifecycle moments (after onboarding, after a support resolution, at set intervals) and are targeted by segment. Scores and comments attach to the user or account record, are reviewed on a regular cadence by product and support, detractors receive follow-up, and shipped fixes are announced back to the users who asked for them.
- **Why it exists:** Analytics shows what users do, not why; without an in-product loop, the loudest feedback channel becomes public reviews and silent churn.
- **If missing:** Product decisions fly blind, unhappy accounts surface only when they cancel, and users who do give feedback never hear back — so they stop giving it.
- **Good looks like:** Intercom's documented NPS practice: in-product surveys at defined milestones (first at two months, then every six months), ratings analyzed at account level, and comments routed monthly to the owning product and education teams.
- **Slop looks like:** An NPS popup that appears on every page load, stores responses in a spreadsheet nobody opens, and shows a "Thanks!" message wired to nothing.
- **Verify:** Trigger each survey as a test user and submit a low score with a comment; confirm the response lands on the user record, reaches the owning team's queue or report, and that frequency caps prevent re-prompting.
- **Source:** Intercom, "How your NPS survey responses make Intercom better" — https://www.intercom.com/help/en/articles/5256662-how-your-nps-survey-responses-make-intercom-better
- **Owning departments:** D18 (Customer Experience & Support), D1 (Product & Requirements), D12 (Analytics, Observability & Performance)
- **Skills that serve it:** feedback-loops

## Churn prevention
- **What:** The interventions that stop avoidable cancellations: cancel-flow save offers, exit surveys, failed-payment recovery, and win-back paths.
- **How it works:** Clicking cancel opens a short exit survey whose stated reason routes to a matched save offer — pause for low usage, downgrade or discount for price, support escalation for bugs — before a clear final confirmation. Involuntary churn is handled in parallel: smart payment retries, automatic card updates, and dunning emails carrying a payment-update link. Reasons and save outcomes are logged and reviewed.
- **Why it exists:** A large share of churn is situational rather than terminal — wrong plan, temporary pause, expired card — and is recoverable at the moment of intent.
- **If missing:** One click cancels with no reason captured and no alternative offered, and failed cards silently end subscriptions the customer wanted to keep.
- **Good looks like:** Recurly's documented Cancel Save flow intercepts a cancellation with a reason survey and a tailored offer; Stripe's Smart Retries and failed-payment emails recover the involuntary side.
- **Slop looks like:** A cancel button that errors out or demands an email to support, paired with a generic "special offer" popup shown to every user regardless of their reason.
- **Verify:** Walk the cancel flow as a test subscriber for each exit reason; confirm the matched offer applies correctly in billing, cancellation still completes cleanly when the offer is declined, and the reason is recorded.
- **Source:** Recurly Engage, "Cancel Save" — https://docs.recurly.com/recurly-engage/docs/cancel-save ; Stripe, "Automate payment retries" — https://docs.stripe.com/billing/revenue-recovery/smart-retries
- **Owning departments:** D18 (Customer Experience & Support), D12 (Analytics, Observability & Performance)
- **Skills that serve it:** churn-prevention

## Status communications
- **What:** A public status page plus an incident-communication practice that tells users what is broken, what it affects, and when the next update will arrive.
- **How it works:** Page components mirror what customers actually use — sign-in, dashboard, API. During an incident the team posts early with known impact, updates on a stated cadence through consistent states (Investigating, Identified, Monitoring, Resolved), notifies subscribers by email or SMS, embeds status in the app and help center, and publishes a postmortem after major incidents.
- **Why it exists:** During an outage, users flood support and social channels looking for answers; one trusted source of truth cuts duplicate tickets and preserves trust.
- **If missing:** Users learn about downtime from each other, file duplicate tickets, and assume the worst about data loss; a technical outage becomes a reputation event.
- **Good looks like:** Atlassian Statuspage's documented tips: communicate early, often (about every 30 minutes), and precisely; stay consistent across channels; own the problem; and prepare incident templates before they are needed.
- **Slop looks like:** A status page showing "All systems operational" during a real outage because nobody owns updating it — worse than having no page at all.
- **Verify:** Run an incident drill: create a test incident and confirm subscriber notifications send, the in-app embed reflects it, and timestamps show the first post and update cadence meeting the documented standard.
- **Source:** Atlassian Statuspage, "Incident communication tips" — https://support.atlassian.com/statuspage/docs/incident-communication-tips/
- **Owning departments:** D18 (Customer Experience & Support)
- **Skills that serve it:** status-communications

## Part 10 — Cloning & replication

## Site discovery
- **What:** Finding the complete set of hosts, URL spaces, and archived captures that make up the source site, before any rebuild work begins.
- **How it works:** The crawler fetches robots.txt and the sitemap index first, then walks the link graph from the home page in a real browser. JavaScript bundle route manifests are extracted to expose client-side routes no link points to, and the Wayback Machine CDX index is queried with `matchType=domain` or `matchType=prefix` to enumerate historical captures, including pages the live site no longer serves.
- **Why it exists:** A rebuild can only cover what discovery found; it defines the scope everything else is measured against.
- **If missing:** Orphan pages, archived-only pages, and entire sections are silently skipped, and the rebuild ships incomplete while claiming full coverage.
- **Good looks like:** The Internet Archive's CDX Server API documentation, which defines match scopes (exact, prefix, host, domain), field selection, and collapsing for enumerating every capture of a site.
- **Slop looks like:** Crawling only the links on the home page, declaring the site "fully mapped," or crawling paths robots.txt disallows.
- **Verify:** Diff the discovered URL list against the CDX `matchType=domain` result set and the sitemap URL count; the three lists must reconcile, with every difference explained.
- **Source:** Wayback CDX Server API — https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md
- **Owning departments:** D16 (Cloning & Replication)
- **Skills that serve it:** site-discovery

## Page inventory
- **What:** The catalog of every in-scope page: URL, page type, template, component set, HTTP status, and last known capture date. It is the rebuild's checklist and scope contract.
- **How it works:** Crawl output, sitemap entries, and CDX records are merged, deduplicated, and canonicalized (trailing slashes, query parameters, URL casing). Pages are clustered by DOM structure into templates, each row is marked public, archived-only, or inferred, and the client agrees the in-scope count before reconstruction starts.
- **Why it exists:** It turns "the site" into a finite, countable work list, so completeness is provable instead of asserted.
- **If missing:** Pages are dropped without anyone noticing, shared templates are rebuilt repeatedly with small differences, and nobody can say when the clone is done.
- **Good looks like:** The Sitemaps protocol's discipline of one canonical URL per entry, applied the same way to the inventory: one row per canonical page, no duplicates, no redirect sources counted as pages.
- **Slop looks like:** An inventory generated from the navigation menu alone, with blog posts, landing pages, and utility pages missing, presented as "all pages."
- **Verify:** Count check — inventory rows equal the reconciled discovery count; then fetch a random 10 percent sample of rows and confirm each URL, status, and template label against the live or archived page.
- **Source:** Wayback CDX Server API (capture enumeration used to build the inventory) — https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md
- **Owning departments:** D16 (Cloning & Replication)
- **Skills that serve it:** page-inventory

## Design extraction
- **What:** Recovering the source site's design system — colors, typography, spacing scale, radii, shadows, and component patterns — as reusable tokens the rebuild is built from.
- **How it works:** Browser automation samples computed styles across representative pages and states (hover, focus, disabled). Raw values are clustered: near-identical colors and spacings collapse into single tokens, font stacks and type scales are recorded as found, and the result is exported as a token file rather than copied page by page.
- **Why it exists:** A rebuild driven by the source's actual system stays consistent across dozens of pages; one styled by eye drifts on every page.
- **If missing:** Every page is styled ad hoc, colors and spacing wander, and visual parity fails in aggregate even when individual pages look close.
- **Good looks like:** The Design Tokens Format Module 2025.10, a Final Community Group Report, which defines a standard JSON interchange format for tokens (`$value`, `$type`, groups, aliases) that tools such as Style Dictionary consume.
- **Slop looks like:** Inventing a plausible palette, substituting a similar-looking font, and hardcoding hex values per page instead of extracting the real values.
- **Verify:** Run a script comparing each token value against computed styles sampled from the source pages, and grep the rebuild's CSS for color or font values that appear in no token — the count must be zero.
- **Source:** Design Tokens Format Module 2025.10 (W3C Community Group Report) — https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/
- **Owning departments:** D16 (Cloning & Replication)
- **Skills that serve it:** design-extraction

## Asset harvesting
- **What:** Collecting the images, fonts, icons, and media the rebuild needs, with the source and rights status of every asset recorded before it is used.
- **How it works:** Asset URLs are extracted from HTML, CSS, and network logs, and from archived captures where the live file is gone. Captures are stored in WARC containers with full request and response records. Each asset gets a manifest row: source URL, capture date, and a rights decision — owned, licensed, recreate, or replace. Copyrighted material is recreated or replaced, never silently reused.
- **Why it exists:** A rebuild without its media is a skeleton, and harvesting without a rights record imports someone else's copyright into the new site.
- **If missing:** Broken images and vanished hotlinks, or a shipped site full of photographs and fonts nobody had the right to use.
- **Good looks like:** The WARC file format, ISO 28500, maintained by the IIPC: the standard container the Internet Archive itself uses to store harvested web content with its provenance intact.
- **Slop looks like:** Bulk-downloading a competitor's photo library and shipping it unchanged, or hotlinking the source site's CDN so the "clone" breaks when the original changes.
- **Verify:** Inspect the asset manifest: every file in the rebuild's asset folders has a row with source URL and rights decision, and a spot check of file checksums matches the WARC records.
- **Source:** The WARC Format 1.1 specification (IIPC, ISO 28500) — https://github.com/iipc/warc-specifications/blob/master/specifications/warc-format/warc-1.1/index.md
- **Owning departments:** D16 (Cloning & Replication)
- **Skills that serve it:** asset-harvesting

## Behaviour cloning
- **What:** Reproducing how the source pages behave — menus, forms and their validation, modals, animations, client-side routing, and interactive states — not only how they look.
- **How it works:** An engineer drives the source site in a real browser and records each flow as a scripted interaction: clicks, inputs, expected state changes, and the network responses behind them. Those recordings become automated tests. The rebuild is developed until the same scripts pass against it unchanged.
- **Why it exists:** Users experience behavior first. A pixel-accurate page with dead controls is a screenshot, not a clone.
- **If missing:** Forms that accept anything or nothing, menus that never open, filters that do not filter, and checkout flows that dead-end — all discovered by the client, not the builder.
- **Good looks like:** Playwright's documented test workflow: scripted browser interactions with assertions, recorded once and replayed against every build, so behavior is specified as executable checks rather than remembered impressions.
- **Slop looks like:** Rebuilding appearance from screenshots, then declaring interactive elements "working" without ever clicking them; submit buttons that only show a success message.
- **Verify:** Run the recorded interaction suite against the rebuild: every in-scope interactive element has at least one passing test, and a manual click-through of the inventory's flow list is signed off.
- **Source:** Playwright Test documentation (scripted interactions and visual comparisons) — https://playwright.dev/docs/test-snapshots
- **Owning departments:** D16 (Cloning & Replication)
- **Skills that serve it:** behavior-cloning, clone-redesign

## Page reconstruction
- **What:** Building the pages that cannot be captured directly — auth-gated, deleted, or never archived — from surviving evidence plus the extracted design system.
- **How it works:** Routes are inferred from JavaScript bundle manifests, sitemap hints, API responses, and naming conventions, and older versions are recovered from Wayback captures where they exist. Pages with evidence are rebuilt to match it. Pages with none are designed fresh from the extracted tokens and component patterns, and the inventory marks them designed-not-cloned.
- **Why it exists:** Real sites have login walls and archive gaps; a migration still has to deliver settings, billing, and dashboard pages.
- **If missing:** Gated flows are absent from the rebuild, or invented wholesale and passed off as recovered originals the client believes were verified.
- **Good looks like:** Using the CDX index's digest field and dated captures to establish what a page actually contained at a given time, and treating anything beyond that evidence as new design.
- **Slop looks like:** Fabricating a plausible dashboard from generic patterns and labeling it a "verified clone" of a page nobody on the project has ever seen.
- **Verify:** Inspect the inventory: every page carries a status of captured, inferred, or designed; designed pages make no parity claim, and each inferred route is spot-checked against the bundle route manifest or a capture.
- **Source:** Wayback CDX Server API (capture and digest lookup) — https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md
- **Owning departments:** D16 (Cloning & Replication)
- **Skills that serve it:** page-reconstruction, clone-redesign

## Fidelity verification
- **What:** Measuring, with numbers, how closely the rebuild matches the source in appearance and behavior, against thresholds agreed before the comparison runs.
- **How it works:** Source and rebuild are screenshotted at the agreed viewports in the same browser engine, and the images are pixel-diffed; the OmniForge brief sets the bar at 95 percent pixel similarity or better on key viewports. DOM structure is compared alongside, dynamic regions are masked, and every in-scope interactive element must pass its interaction checklist.
- **Why it exists:** "Looks the same" is an opinion until it is a diff report; a ship gate needs a threshold, not an impression.
- **If missing:** Visual drift ships unnoticed, disputes about closeness become taste arguments, and parity claims in the delivery report are unfounded.
- **Good looks like:** Playwright's visual comparisons: the first run stores golden baseline screenshots, later runs compare against them and emit expected, actual, and diff images for every failure.
- **Slop looks like:** Eyeballing two screenshots side by side and reporting "pixel-perfect," or quietly regenerating the baselines so a failing comparison turns green.
- **Verify:** Run the visual test suite in CI against the committed baselines and read the diff report per page; any baseline update must carry a recorded reason, and interaction checklists must show zero untested elements.
- **Source:** Playwright visual comparisons documentation — https://playwright.dev/docs/test-snapshots
- **Owning departments:** D16 (Cloning & Replication), D8 (QA)
- **Skills that serve it:** fidelity-verification

## Clone ethics
- **What:** The authorization and rights gate for the whole pipeline: whose site may be cloned, what may be reused, and what must be recreated, replaced, or dropped.
- **How it works:** Work starts only with written authorization — the client's own site or a licensed target — recorded in the project file. The crawler identifies itself, honors robots.txt, respects rate limits, and never bypasses logins or paywalls. Layout patterns and behavior may be recreated; trademarks, logos, and copyrighted text and images are never copied verbatim, and competitor clones must differ in branding and content.
- **Why it exists:** Cloning sits one decision away from impersonation and infringement; this check is what separates migration and learning from phishing and theft.
- **If missing:** A pixel-perfect copy of a competitor's branded site: trademark and copyright exposure, takedown and legal risk, and a deliverable that deceives its visitors.
- **Good looks like:** RFC 9309 itself, which states that robots rules "are not a form of access authorization" — the absence of a Disallow line is not permission; permission comes from the owner.
- **Slop looks like:** Cloning a live brand end to end, keeping its logo, copy, and photography, and calling it a template; or scraping behind a login with borrowed credentials.
- **Verify:** Check the project file for a dated authorization record that precedes the first crawl log entry; grep the rebuild for source brand names and trademarked assets, allowing only approved references; confirm crawl logs contain no robots-disallowed URL.
- **Source:** RFC 9309, Robots Exclusion Protocol — https://www.rfc-editor.org/rfc/rfc9309.html
- **Owning departments:** D16 (Cloning & Replication), D14 (Legal)
- **Skills that serve it:** clone-ethics

## Part 11 — Depth elements I: product, backend & data

## User research and personas
- **What:** Structured inquiry into who the users are and what they need, distilled into personas: named, evidence-based archetypes that stand in for real user segments during design and build decisions.
- **How it works:** The team interviews and observes target users, surveys behavior, and mines support tickets and analytics, then clusters findings into a small set of personas, each with goals, context, constraints, and representative tasks. Personas are cited in requirements and design reviews whenever a trade-off needs a user-side answer.
- **Why it exists:** It replaces the team's guesses about "the user" with shared, checkable evidence, so features are prioritized by observed need rather than by whoever argues loudest.
- **If missing:** The team designs for itself, builds features nobody asked for, and discovers the mismatch only after launch, when fixing it costs the most.
- **Good looks like:** Nielsen Norman Group's guidance that personas must be built from actual user research — interviews, field studies, surveys — and kept memorable so the team uses them as shorthand in decisions.
- **Slop looks like:** Invented personas with stock-photo names, ages, and hobbies generated in one sitting, citing no interviews or data, then framed as research.
- **Verify:** Open the research file: it names the methods used, the number and source of participants, and dates; each persona traces to specific findings, not assertions.
- **Source:** Nielsen Norman Group, "Personas Make Users Memorable" — https://www.nngroup.com/articles/persona/
- **Owning departments:** D1
- **Skills that serve it:** user-research

## Competitive analysis
- **What:** A systematic comparison of rival products — features, pricing, positioning, and user experience — used to find gaps, table stakes, and defensible differentiation.
- **How it works:** Analysts pick direct and indirect competitors, run the same core tasks in each product, and score them against shared criteria: capability coverage, usability, price, and proof. Findings land in a matrix that feeds positioning and roadmap choices, refreshed on a schedule.
- **Why it exists:** It stops the team from building in a vacuum: some features are mandatory because every rival has them, and others are worthless because the market already solved them better.
- **If missing:** The product launches blind — missing table-stakes features users expect, duplicating commodity work, and claiming differentiation that evaporates on first comparison.
- **Good looks like:** Nielsen Norman Group's competitive usability evaluations: comparing your product against two to four competing designs on the same tasks to learn what works and what fails before investing.
- **Slop looks like:** A feature-checklist table scraped from competitors' marketing pages, with checkmarks for features never actually tried, presented as analysis.
- **Verify:** Inspect the analysis artifact: each competitor claim links to a dated screenshot, trial account note, or public page; conclusions cite the matrix, not memory.
- **Source:** Nielsen Norman Group, "Competitive Usability Evaluations" — https://www.nngroup.com/articles/competitive-usability-evaluations/
- **Owning departments:** D1
- **Skills that serve it:** competitive-analysis

## Pricing and monetization
- **What:** The model that turns product value into revenue: what is charged for (the value metric), the pricing model, tier structure, and how billing, trials, and upgrades are wired into the product.
- **How it works:** The team picks a value metric that grows with customer value, chooses a model (per seat, tiered flat rate, usage-based, hybrid, per outcome), designs tiers with a natural upgrade path, and implements it through a billing provider with products, prices, subscriptions, and webhooks.
- **Why it exists:** Pricing is a product decision, not an afterthought: the wrong metric caps revenue or charges for the wrong thing, and retrofitting billing into a finished product is painful and error-prone.
- **If missing:** The product ships with a hard-coded "Pro" flag, no upgrade path, manual invoicing, and pricing that cannot change without a redeploy.
- **Good looks like:** Stripe's SaaS pricing guidance: sequence the decision as value metric first, then pricing model, then tier structure, then measurement, with tiers designed so customers graduate as they grow.
- **Slop looks like:** Copying a competitor's three price points with invented feature splits, a free tier with no limits or conversion path, and prices hard-coded in page copy.
- **Verify:** Check the billing provider dashboard: products and prices exist as configured objects matching the pricing page exactly; run a test-mode checkout and upgrade to confirm proration and entitlements change.
- **Source:** Stripe, "A Guide to SaaS Pricing and Packaging" — https://stripe.com/resources/more/saas-pricing-and-packaging-strategy
- **Owning departments:** D1
- **Skills that serve it:** pricing-monetization

## Market expansion
- **What:** The evidence-based decision to launch an existing, already-shipping product into a new country or distinct market — and the readiness work that makes the launch survivable: local payments, locale support, legal obligations, local pricing, the local competitive set, and support.
- **How it works:** Each candidate market gets one readiness record, scored on evidence across fixed dimensions (payments, localization tier, privacy and residency obligations, pricing, competition, support) against criteria registered before scoring begins. A pilot with pre-set kill thresholds precedes full launch, and the record closes with exactly one dated decision — GO, CONDITIONAL GO, or NO-GO — signed by a named decider.
- **Why it exists:** A product that works at home can fail abroad for reasons invisible from home: the dominant local payment method is unsupported, prices converted at the exchange rate are prices nobody local will pay, or a data-residency law the architecture violates. The decision is cheap; the failed launch is not.
- **If missing:** Expansion happens on enthusiasm — a translated homepage, FX-converted prices, no local payment method, contracts signed and dates announced before the legal exposure is discovered.
- **Good looks like:** The World Bank Global Findex Database's per-economy payment-method and account-ownership data used as evidence for the payments dimension, and Unicode CLDR locale data (currencies, date and number formats) verified rather than assumed for the localization dimension.
- **Slop looks like:** A slide-deck verdict of "huge market, let's launch," prices produced by currency conversion, machine-translated legal pages, and a pilot with no kill criteria that can never be declared a failure.
- **Verify:** Open the readiness record: every dimension cites dated evidence rather than opinion, the criteria predate the scores, and the closing decision is one of the three values, signed and dated, with conditions or reasons that cite the dimension evidence.
- **Source:** World Bank Global Findex Database — https://globalfindex.worldbank.org/
- **Owning departments:** D1
- **Skills that serve it:** market-expansion

## API implementation
- **What:** The actual building of endpoints — routing, request handling, business logic, persistence, and responses — as distinct from the contract that specifies them. It includes the client side of the craft: conventions an SDK must honor so consumers can integrate reliably.
- **How it works:** Developers implement resource-oriented endpoints per the contract, apply consistent naming, status codes, error shapes, pagination, and versioning, then expose the same surface through maintained SDKs that wrap authentication, retries, and typed models so consumers do not hand-roll HTTP.
- **Why it exists:** A contract nobody implements consistently is fiction; disciplined implementation and SDK design are what make an API predictable enough for strangers to build on.
- **If missing:** Endpoints drift from the spec, every route invents its own error format and pagination, and consumers write brittle glue code that breaks on each release.
- **Good looks like:** Microsoft's REST API Guidelines, published for consistency across its cloud APIs, paired with Stripe's practice of maintaining official server-side SDKs for seven languages generated against one API behavior.
- **Slop looks like:** Endpoints returning HTTP 200 with error strings in the body, verbs in URLs, three pagination styles in one API, and an "SDK" that is a renamed fetch wrapper.
- **Verify:** Run the contract test suite against the running server; diff live responses against the OpenAPI document; install the SDK in a clean project and complete the quickstart task using only its README.
- **Source:** Microsoft, "REST API Design Guidelines" — https://devblogs.microsoft.com/microsoft365dev/rest-api-design-guidelines/ ; Stripe, "Introduction to server-side SDKs" — https://docs.stripe.com/sdks/server-side
- **Owning departments:** D4, D2
- **Skills that serve it:** api-building, rest-conventions, sdk-design

## Input validation
- **What:** Checking every piece of incoming data — syntax and semantics — against explicit rules before the application trusts, stores, or acts on it.
- **How it works:** Each field gets defined rules: type, format, length, range, and membership in an allowlist where the value set is known. Validation runs server-side, as early as possible in the data flow, using framework validators or a schema validator; failures return clear errors without partial writes.
- **Why it exists:** All input is hostile until proven otherwise. Validation is the boundary that keeps malformed or malicious data from corrupting the database and triggering failures in downstream components.
- **If missing:** Bad data persists silently, business rules are bypassed with crafted requests, and injection and mass-assignment attacks find open doors.
- **Good looks like:** OWASP's Input Validation Cheat Sheet: allowlist validation, syntactic plus semantic checks (for example, start date before end date), and schema validation of structured data, enforced on a trusted system.
- **Slop looks like:** Validation only in browser JavaScript, a single denylist regex for "bad characters," and endpoints that accept and store any JSON body they receive.
- **Verify:** Send boundary and malformed payloads to each endpoint (wrong types, oversized strings, unknown fields, inconsistent date ranges) and confirm rejection with no partial state change in the database.
- **Source:** OWASP Cheat Sheet Series, "Input Validation Cheat Sheet" — https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- **Owning departments:** D4, D7
- **Skills that serve it:** validation

## Authentication and authorization implementation
- **What:** The code that proves who a caller is (authentication) and decides what that identity may do (authorization), including session handling and role-based permission checks on every protected operation.
- **How it works:** Passwords are hashed with a vetted algorithm, sessions or tokens are generated with high-entropy identifiers on a trusted system, rotated at login, and expired on logout and timeout. Authorization maps users to roles and roles to permissions — the NIST RBAC model — and a server-side check runs on each request, not just in the UI.
- **Why it exists:** Identity is the perimeter of a web application. A single missing permission check turns a normal account into an administrator, and weak session handling makes stolen tokens equivalent to stolen passwords.
- **If missing:** Broken access control: users read and modify each other's data by changing an ID in the URL, sessions never expire, and privilege escalation is a matter of editing a request.
- **Good looks like:** OWASP's Session Management Cheat Sheet (new session ID on authentication, Secure and HttpOnly cookie attributes, idle and absolute timeouts) combined with the NIST RBAC reference model standardized as INCITS 359.
- **Slop looks like:** Authorization enforced by hiding buttons, an `isAdmin` flag trusted from the client, plaintext or MD5 password storage, and one shared API key for all users.
- **Verify:** Run an authorization test matrix: for each role, request every protected endpoint with valid, missing, and other users' credentials; confirm 401/403 responses and no data leakage; inspect the user table to confirm hashed passwords.
- **Source:** OWASP Cheat Sheet Series, "Session Management Cheat Sheet" — https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html ; NIST CSRC, "Role Based Access Control" — https://csrc.nist.gov/projects/role-based-access-control
- **Owning departments:** D7, D4
- **Skills that serve it:** backend-auth, rbac

## Rate limiting and abuse controls
- **What:** Enforced caps on how many requests a client, account, or IP may make in a window, plus the surrounding controls — concurrency limits, lockouts, and 429 responses — that keep automated abuse from consuming the service.
- **How it works:** A limiter (commonly token bucket) counts requests per key at the edge or in middleware, with stricter limits on expensive or sensitive endpoints such as login and search. Rejected requests return HTTP 429 with a reason and retry guidance; clients back off exponentially with jitter.
- **Why it exists:** Without limits, one buggy script or one attacker can exhaust compute, run up third-party API bills, brute-force credentials, and deny service to everyone else.
- **If missing:** Credential stuffing runs at full speed, scrapers mirror the whole catalog, and a single runaway integration takes the API down for all customers.
- **Good looks like:** Stripe's published rate-limit system: a global per-account limit, lower per-endpoint limits, a separate concurrency limit, and 429 responses carrying a header that states exactly which limit was hit.
- **Slop looks like:** No limits anywhere except a comment saying "add rate limiting later," or a limiter keyed on an IP header the client can spoof, silently dropping legitimate traffic when it misfires.
- **Verify:** Script a burst of requests above the documented limit against a test endpoint and confirm 429 responses with retry headers; confirm normal-rate traffic and a second client key are unaffected.
- **Source:** Stripe Documentation, "Rate limits" — https://edge-docs.stripe.com/rate-limits
- **Owning departments:** D4, D7
- **Skills that serve it:** rate-limiting

## Admin and internal tools
- **What:** The staff-only interfaces operators use to manage the product: looking up users, correcting data, issuing refunds, toggling features, and resolving support cases without touching the database directly.
- **How it works:** Admins get a separate, authenticated surface — often generated from the data models, as in framework admin systems — with its own roles, scoped permissions, and an audit log of who changed what. Dangerous actions require confirmation and are reversible where possible. PCI scope note: admin tools sit inside the payment trust boundary whenever staff can view orders or trigger refunds, so they must never display or store full card numbers; keeping card data inside the payment provider (for example, Stripe-hosted collection) is what holds the product to the smallest PCI DSS scope, SAQ A.
- **Why it exists:** Operations are inevitable: the choice is between a controlled, logged tool and engineers running raw SQL against production under time pressure.
- **If missing:** Support cannot resolve routine cases, data fixes happen through untracked database edits, and one mistake in a console session deletes production records with no audit trail.
- **Good looks like:** Django's admin: a model-driven internal interface whose docs state plainly it is an organization's internal management tool, gated by staff status and per-model permissions; Stripe's PCI guide documents how hosted card collection keeps merchant scope at SAQ A.
- **Slop looks like:** An `/admin` route protected only by a hidden URL, full card numbers rendered in an order table, and delete buttons with no confirmation, logging, or undo.
- **Verify:** Log in as a limited staff role and confirm restricted sections are denied server-side; perform a test refund and confirm it appears in the audit log with actor and timestamp; search admin pages and logs for any full card number pattern.
- **Source:** Django documentation, "The Django admin site" — https://docs.djangoproject.com/en/4.2/ref/contrib/admin/ ; Stripe, "What is PCI DSS compliance?" — https://stripe.com/guides/pci-compliance
- **Owning departments:** D4, D10
- **Skills that serve it:** admin-tools, pci-compliance

## Data warehousing
- **What:** A separate analytical store that consolidates data from the operational database and other sources into schemas optimized for reporting and analysis rather than transactions.
- **How it works:** Data is extracted from source systems, loaded into a warehouse (often columnar, with storage and compute separated), and modeled into fact and dimension tables or curated datasets. Analysts query the warehouse with SQL, so heavy reporting never competes with production traffic.
- **Why it exists:** Operational databases are built for fast single-record writes and reads; running scans and joins for dashboards against them slows the product and still answers questions badly.
- **If missing:** Every report is a hand-written query against production, numbers differ between teams because each query defines metrics differently, and historical analysis is impossible once records are updated in place.
- **Good looks like:** Google BigQuery's documented model: a serverless warehouse with columnar storage and separated storage and compute layers, governed datasets, and standard SQL access for analysts.
- **Slop looks like:** A nightly CSV emailed around as "the warehouse," dashboards querying the production primary at peak hours, and revenue figures that change depending on who wrote the query.
- **Verify:** Confirm the warehouse exists as its own system with scheduled loads; reconcile one headline metric (for example, yesterday's order count) between warehouse and source; run the standard dashboard during business hours and check production database load is unaffected.
- **Source:** Google Cloud Documentation, "BigQuery overview" — https://cloud.google.com/bigquery/docs/introduction?hl=vi
- **Owning departments:** D5
- **Skills that serve it:** data-warehousing

## ETL and data pipelines
- **What:** The automated flows that move data between systems: extracting from sources, transforming it into clean, consistent shapes, and loading it into destinations such as the warehouse — on a schedule, with retries and monitoring.
- **How it works:** Ingestion pulls raw data from APIs, databases, files, and event streams into a landing zone unchanged. Transformation jobs then validate, deduplicate, join, and model it. An orchestrator defines the whole flow as a directed acyclic graph of tasks with dependencies, schedules runs, retries failures, supports backfills, and records the state of every task instance.
- **Why it exists:** Manual data movement does not scale and fails silently; pipelines make data flow repeatable, observable, and recoverable instead of depending on someone's laptop script.
- **If missing:** Reports run on stale or partial data, a failed copy goes unnoticed for weeks, and nobody can say which numbers came from which source version.
- **Good looks like:** Apache Airflow's documented model: workflows as Python-defined DAGs, operators as task templates, and task instances with explicit states (queued, running, success, failed, up for retry) visible in one UI.
- **Slop looks like:** A chain of cron jobs and shell scripts with no dependency tracking, silent partial loads, transformations edited directly in production, and no way to re-run a single day.
- **Verify:** Open the orchestrator UI and confirm every pipeline shows a last successful run within its schedule window; kill a transformation task in staging and confirm it retries, alerts, and does not publish partial output.
- **Source:** Apache Airflow Documentation, "Concepts" — https://airflow.apache.org/docs/apache-airflow/2.0.0/concepts.html
- **Owning departments:** D5
- **Skills that serve it:** etl-pipelines, data-ingestion, pipeline-orchestration

## Read replicas and read scaling
- **What:** Read-only copies of the primary database that receive its changes continuously and serve read queries, so read traffic scales horizontally instead of overloading one instance.
- **How it works:** The provider replicates writes from the primary to replicas asynchronously using the engine's built-in replication. The application routes writes and read-after-write-sensitive queries to the primary, and tolerant reads — feeds, search, reporting — to replicas, while monitoring replication lag.
- **Why it exists:** Most applications read far more than they write; replicas let read capacity grow beyond a single instance's compute and I/O limits without re-architecting the data layer.
- **If missing:** Read growth saturates the primary, page loads degrade under reporting load, and the only lever left is buying a bigger instance until that runs out too.
- **Good looks like:** Amazon RDS read replicas as documented by AWS: route application queries to replicas to scale read-heavy workloads, with the explicit caveat that asynchronous replication means replicas can be stale.
- **Slop looks like:** Replicas created but never routed to, all reads still hitting the primary — or the opposite: checkout reads its own just-written order from a lagging replica and shows the customer an empty cart.
- **Verify:** Check the routing configuration for read/write splitting; write a record and measure time until it appears on the replica; confirm a lag metric and alert exist and that consistency-critical reads are pinned to the primary.
- **Source:** AWS Documentation, "Working with DB instance read replicas" — https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
- **Owning departments:** D5
- **Skills that serve it:** read-replicas

## Event-driven architecture
- **What:** A structure in which components communicate by emitting and reacting to events — records of things that happened — instead of calling each other directly, decoupling producers from consumers in identity and time.
- **How it works:** A service publishes an event (for example, `OrderPlaced`) to a broker or log; interested services subscribe and react independently. Teams deliberately choose among distinct patterns — event notification, event-carried state transfer, event sourcing, and CQRS — rather than treating "events" as one thing.
- **Why it exists:** Direct call chains couple every service to every other's availability and internals; events let new consumers attach without modifying producers, and let work proceed asynchronously.
- **If missing:** Synchronous chains fail together, adding one integration means editing the core service, and there is no durable record of what happened to reconstruct or audit system behavior.
- **Good looks like:** Martin Fowler's analysis distinguishing the four patterns people conflate under "event-driven," including the warning that event notification's weakness is losing a visible statement of overall system behavior.
- **Slop looks like:** A message queue installed as decoration while services still call each other synchronously, events used as disguised commands a producer secretly depends on, and no schema, ordering, or replay story for the event stream.
- **Verify:** Inspect the broker: each event type has a documented schema and named consumers; disable one consumer in staging and confirm producers keep working and the backlog drains when it returns.
- **Source:** Martin Fowler, "What do you mean by 'Event-Driven'?" — https://www.martinfowler.com/articles/201701-event-driven.html
- **Owning departments:** D2
- **Skills that serve it:** event-driven

## Content moderation and trust & safety
- **What:** The policies, reporting channels, review queues, and enforcement actions that keep user-generated content and behavior within the platform's rules and the law.
- **How it works:** The platform publishes a policy, gives users in-product reporting on content and accounts, and routes reports plus automated detections into a review queue. Reviewers apply tiered enforcement — labeling, reduced visibility, removal, suspension, ban — with priority tiers for the most severe violations and an appeal path for mistakes.
- **Why it exists:** Any product with user content attracts spam, abuse, fraud, and illegal material; without moderation the product becomes unusable, advertisers and payment partners leave, and regulators arrive.
- **If missing:** Reports go into an unmonitored inbox, abuse stays up for weeks, enforcement is arbitrary and unappealable, and the first viral incident becomes a legal and press crisis.
- **Good looks like:** The Trust & Safety Professional Association's curriculum: policy in two forms (public expectations and internal enforcement guidance), moderation by humans and automation combined, and a defined ladder of enforcement actions with the highest-harm policies prioritized.
- **Slop looks like:** A "report" button that sends an email nobody reads, bans issued by a single keyword filter with no human review, and no record of why any action was taken.
- **Verify:** File a test report from a user account and trace it through the queue to a decision; confirm each enforcement action is logged with policy cited, and that an appeal submission reaches a reviewer.
- **Source:** Trust & Safety Professional Association, "Content Moderation Simulation" (T&S Curriculum) — https://www.tspa.org/curriculum/ts-curriculum/content-moderation-simulation/
- **Owning departments:** D7
- **Skills that serve it:** content-moderation, user-reporting

## Project status tracking and postmortems
- **What:** The living record of where a project stands — what is done, in progress, blocked, and decided — plus the blameless postmortem written after significant incidents or failures, turning both into institutional memory.
- **How it works:** Status lives in one maintained place: the README states what the project is and how to run it, a progress log or tracker records milestones and current state, and decisions are appended as they happen. After an incident, the team writes a postmortem: timeline, impact, root causes, and follow-up actions with owners, reviewed and shared.
- **Why it exists:** Work that exists only in chat scrollback and memory is lost; written status lets anyone — including a future maintainer or a fresh agent session — resume without archaeology, and postmortems stop the same failure from recurring.
- **If missing:** Every handover starts from zero, the same incident happens twice, stakeholders get status by interrupting the team, and nobody can say what was decided or why.
- **Good looks like:** Google's SRE postmortem culture: postmortems are expected after defined triggers (user-visible downtime, data loss, manual intervention), written blamelessly, focused on contributing causes, and closed only when preventive actions are in place.
- **Slop looks like:** A README still containing the project generator's boilerplate, a status doc last updated at kickoff, and a postmortem that names a person to blame and ends with "be more careful."
- **Verify:** Open the README and progress record: both carry dates within the current work cycle and match the actual state of the deliverables; pick the most recent incident and confirm a postmortem exists with owned, dated action items.
- **Source:** Google SRE, "Postmortem Culture: Learning from Failure" — https://sre.google/workbook/postmortem-culture/
- **Owning departments:** D10
- **Skills that serve it:** progress-tracking, postmortem-writing, readme-writing

## Part 12 — Depth elements II: testing & content

## Visual regression testing
- **What:** Automated comparison of rendered screenshots against approved baselines, so unintended visual changes fail the build instead of reaching users.
- **How it works:** Baseline screenshots for key pages and states are committed to the repo. Each CI run re-renders the same pages in a pinned browser and environment, pixel-diffs them against the baselines, and fails when differences exceed a configured threshold. Dynamic regions (timestamps, ads, avatars) are masked, and intentional design changes update baselines only through reviewed pull requests.
- **Why it exists:** Functional tests pass even when a CSS change pushes the checkout button off-screen; only a pixel-level comparison sees layout, spacing, font, and overflow regressions.
- **If missing:** Visual breakage ships silently and is found by users or screenshots on social media, usually on the one viewport nobody opened manually.
- **Good looks like:** Playwright's documented visual comparison flow: `expect(page).toHaveScreenshot()` generates reference screenshots on first run, compares on later runs, and baselines are regenerated deliberately with `--update-snapshots`.
- **Slop looks like:** An agent claims "looks fine" from reading the CSS, or a screenshot test is written once, fails on font rendering, and gets deleted instead of configured.
- **Verify:** Run `npx playwright test --grep @visual` in CI and confirm a seeded CSS change (e.g. shift a header by 20px) fails with a diff image artifact.
- **Source:** Playwright visual comparisons documentation — https://playwright.dev/docs/test-snapshots
- **Owning departments:** D8 (QA)
- **Skills that serve it:** visual-regression, browser-verification

## Load and performance testing
- **What:** Scripted simulation of many concurrent users against a staging or production-like environment to measure latency, throughput, and error rates under realistic and peak traffic.
- **How it works:** Load scripts model real user journeys as virtual users that ramp up, hold, and spike. Pass/fail thresholds are codified up front — for example p(95) response time and error-rate ceilings — and the run fails automatically when a threshold is breached. Results are compared release over release.
- **Why it exists:** A page that responds in 200 ms for one developer can collapse at 500 concurrent sessions because of connection pools, locks, or an unindexed query; only load reveals that before launch day does.
- **If missing:** The first real traffic spike becomes the load test, run in production, with paying users as the test data.
- **Good looks like:** Grafana k6 practice: thresholds such as `http_req_failed: ['rate<0.01']` and `http_req_duration: ['p(95)<200']` codify SLOs, and a breached threshold ends the test with a failed status that blocks the pipeline.
- **Slop looks like:** "Tested with 10 users, it was fast" — or a load script that hammers the homepage only, ignores login and checkout, and reports averages that hide the p(99) tail.
- **Verify:** Run the k6 scenario in CI (`k6 run load/checkout.js`) and confirm the run exits non-zero when a threshold is deliberately tightened below current performance.
- **Source:** Grafana k6 thresholds documentation — https://grafana.com/docs/k6/next/using-k6/thresholds/
- **Owning departments:** D8 (QA), D12 (Analytics)
- **Skills that serve it:** load-testing

## Chaos and resilience testing
- **What:** Deliberate, controlled injection of failures — killed instances, added latency, severed dependencies — to prove the system keeps serving users when components break.
- **How it works:** The team defines a measurable steady state (error rate, successful orders per minute), states a hypothesis that it holds during the experiment, then injects a real-world failure into a limited blast radius with an abort switch ready. Observed deviation either disproves the hypothesis and generates a fix, or builds verified confidence. Experiments are automated and rerun continuously.
- **Why it exists:** Retries, timeouts, fallbacks, and redundancy are usually written but never exercised; untested failover code fails exactly when it is first needed, during a real outage.
- **If missing:** Resilience is a claim in the architecture document, not a property of the running system, and the first dependency outage cascades into a full outage.
- **Good looks like:** The Principles of Chaos Engineering method: define steady state, hypothesize it continues in control and experiment groups, introduce variables reflecting real events like crashed servers or severed connections, and try to disprove the hypothesis — while minimizing blast radius.
- **Slop looks like:** Randomly killing production processes with no hypothesis, no steady-state metric, and no abort criteria — vandalism rebranded as chaos — or "chaos" that only ever runs in a staging environment that resembles nothing.
- **Verify:** Inspect the experiment record for one recent run: hypothesis, blast radius, abort criteria, and steady-state graphs before/during/after; confirm the abort switch was tested.
- **Source:** Principles of Chaos Engineering — https://principlesofchaos.org/
- **Owning departments:** D8 (QA)
- **Skills that serve it:** chaos-testing

## Contract testing
- **What:** Verification that a service provider and each of its consumers still agree on the shape of their interactions — request/response formats, status codes, and required fields — without needing a shared end-to-end environment.
- **How it works:** Consumer tests run against a mock provider and record the interactions the consumer actually depends on as a contract file. The contract is published to a broker; provider CI replays every interaction against the real provider and publishes the verification result. A deployment gate (can-i-deploy) blocks any version whose contracts are unverified or broken.
- **Why it exists:** In a multi-service or frontend/backend split, the most expensive integration bugs are silent schema drift: a renamed field or changed type that unit tests on both sides pass and production rejects.
- **If missing:** Breaking API changes are discovered by the consumer team after deploy, as runtime errors in someone else's service.
- **Good looks like:** Pact's consumer-driven flow: the consumer specifies expected interactions, Pact generates the contract, and the provider verifies it meets the consumer's expectations before release.
- **Slop looks like:** The contract is a copy of the provider's full response schema, so every harmless field addition "breaks" the contract — or contracts exist but no pipeline gate reads the verification results, so failures change nothing.
- **Verify:** Change a required response field's type in the provider, run provider verification, and confirm it fails and the deploy gate reports the version as not deployable.
- **Source:** Pact consumer testing documentation — https://pact-foundation.github.io/pact-python/consumer/
- **Owning departments:** D8 (QA)
- **Skills that serve it:** contract-testing

## Security testing
- **What:** Systematic testing of the application for exploitable weaknesses — injection, broken access control, authentication flaws, information leakage — using a defined methodology rather than ad-hoc poking.
- **How it works:** Testers work through a checklist of test cases by category, combining scanners for breadth with manual testing for logic flaws scanners cannot see (authorization, business logic). Each finding is recorded with evidence, severity, and remediation, then retested after the fix. Dependency and configuration scanning runs in CI on every change.
- **Why it exists:** Attackers run the same checklists; a vulnerability found by a test report costs a fix, while the same vulnerability found by an attacker costs data, money, and trust.
- **If missing:** The application ships with textbook flaws — an IDOR on an order endpoint, debug comments leaking internal routes — that any scanner would have flagged in minutes.
- **Good looks like:** The OWASP Web Security Testing Guide: 100+ named test cases with stable IDs (e.g. WSTG-INFO-05, reviewing webpage content for information leakage in comments, metadata, and exposed source maps), each with objectives, test steps, and remediation.
- **Slop looks like:** "We use HTTPS and hashed passwords, so it's secure" — or a scanner report pasted into a ticket with every finding left untriaged, including the criticals.
- **Verify:** Pick three WSTG categories relevant to the app (authentication, authorization, input validation) and confirm executed test records with pass/fail evidence exist for the current release.
- **Source:** OWASP Web Security Testing Guide (WSTG-INFO-05) — https://owasp.github.io/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Webpage_Content_for_Information_Leakage
- **Owning departments:** D8 (QA)
- **Skills that serve it:** security-testing

## Accessibility testing
- **What:** Checking that pages work for people using assistive technology — screen readers, keyboard-only navigation, magnification — against WCAG criteria, with automated scans plus manual verification.
- **How it works:** Automated scans (axe-core via Playwright) run in CI on every key page and state, failing the build on violations such as missing labels, invalid ARIA, or insufficient contrast. Because automation catches only automatically detectable problems, the process adds keyboard walkthroughs, focus-order checks, and screen-reader passes for critical flows before release.
- **Why it exists:** Accessibility defects are functional defects for a large share of users, and in many markets a legal requirement; they are also nearly free to fix at build time and expensive to retrofit.
- **If missing:** A checkout that a sighted mouse user completes in a minute is impossible with a keyboard, and nobody on the team ever finds out.
- **Good looks like:** Playwright's documented approach: `@axe-core/playwright` scans a page or a scoped component state with `AxeBuilder`, asserts zero violations, and the docs explicitly pair this with manual assessment because automated tests detect only some problems.
- **Slop looks like:** An agent adds `alt="image"` to every picture, sprinkles ARIA attributes onto divs, and declares the site "WCAG compliant" without ever running a scan or touching a keyboard.
- **Verify:** Run the accessibility test suite (`npx playwright test tests/a11y`) and confirm it fails when a form label is removed; then complete the signup flow keyboard-only.
- **Source:** Playwright accessibility testing documentation — https://playwright.dev/docs/accessibility-testing
- **Owning departments:** D8 (QA)
- **Skills that serve it:** accessibility-testing

## Bug triage and defect management
- **What:** The standing process that turns a stream of defect reports into decisions: validate, classify by severity and priority, assign an owner, schedule or explicitly defer, and track each defect to a verified closure.
- **How it works:** All reports enter one intake queue with a required template (steps to reproduce, environment, expected vs. actual). A regular triage session reviews new bugs, sets severity (technical impact) independently from priority (business urgency), deduplicates, assigns, and slots fixes into sprints or a reviewed won't-fix decision. Reopened and aging defects are re-evaluated as context changes.
- **Why it exists:** Without triage, the loudest reporter wins, duplicates multiply, critical defects age in an unowned backlog, and "known issue" becomes where bugs go to be forgotten.
- **If missing:** Releases ship carrying unreviewed crash reports, while developers burn sprint time on cosmetic defects that arrived with the most exclamation marks.
- **Good looks like:** The documented triage workflow: review every new bug for validity and completeness, classify on a standard severity scale (Critical/High/Medium/Low) and a separate priority scale (P1 fix immediately through P4), assign, schedule, and re-evaluate as context changes.
- **Slop looks like:** An AI-generated tracker full of plausible tickets nobody owns: duplicates of the same defect worded five ways, severity set to "high" on everything, and no reproduction steps on any of them.
- **Verify:** Sample 10 open defects: each must have reproduction steps, environment, severity and priority as separate fields, a named owner, and a state that changed within the team's triage cadence.
- **Source:** Bug triage process guide (severity/priority classification workflow) — https://www.bugreel.io/blog/bug-triage-process-guide
- **Owning departments:** D8 (QA)
- **Skills that serve it:** bug-triage

## Content strategy and production
- **What:** The plan that decides what content gets made, for whom, and why — audience, goals, topics, formats, channels — plus the production workflow that moves each piece from brief to published and maintained.
- **How it works:** Strategy sets goals and audience needs; planning turns them into an editorial calendar with owners and deadlines for each production stage (drafting, editing, design, approval). Each piece starts from a brief tying it to a goal and a search or user intent, passes review for accuracy and voice, is published with distribution, and is later measured and refreshed or retired.
- **Why it exists:** Without it, publishing is random: duplicated topics, orphaned pages that answer nothing, and a blog that produces volume instead of the pages that bring signups or sales.
- **If missing:** Content exists but compounds into nothing — no topic ownership, no internal logic, no updates — and search and readers both treat the site as noise.
- **Good looks like:** Mailchimp's documented content planning practice: define clear goals and audience, choose formats and channels, and run an editorial calendar that coordinates drafting, editing, design, and approval stages so nothing falls through the cracks.
- **Slop looks like:** Thirty AI-generated posts a week on whatever keywords were cheapest, none briefed, none edited, none updated — a content farm wearing the company's own domain.
- **Verify:** Open the editorial calendar: every published item from the last month traces to a brief naming its audience, goal, and target query or intent, plus an owner and a review step.
- **Source:** Mailchimp content planning guide — https://mailchimp.com/resources/content-planning/
- **Owning departments:** D9 (Content/SEO)
- **Skills that serve it:** content-strategy, copywriting

## Structured data and metadata
- **What:** Machine-readable markup (typically schema.org vocabulary in JSON-LD) plus page metadata that tells search engines exactly what a page is — product, article, event, FAQ — instead of leaving them to guess from prose.
- **How it works:** Each page type gets a template that emits valid JSON-LD with all required properties for its rich-result type, populated from the same data that renders the visible page. Markup is validated during development with the Rich Results Test and monitored after deployment through Search Console's rich-result reports, because templating changes can silently break it.
- **Why it exists:** Structured data is what makes a page eligible for rich results — prices, ratings, availability shown directly in search — and removes ambiguity that costs rankings and clicks.
- **If missing:** Pages rank as plain blue links while competitors show stars and prices, and a template refactor can invalidate markup across the whole site unnoticed.
- **Good looks like:** Google Search Central's documented practice: JSON-LD is the recommended format, all required properties must be present for rich-result eligibility, and validity is checked with the Rich Results Test during development and status reports after deployment.
- **Slop looks like:** JSON-LD pasted from a generator with placeholder values ("Product Name", price 0.00), review markup for ratings the page doesn't show, or a trailing comma that makes the whole block invalid — shipped unchecked.
- **Verify:** Run the production product and article URLs through the Rich Results Test and confirm zero errors; then diff the JSON-LD values against the visible page content.
- **Source:** Google Search Central, introduction to structured data — https://developers.google.com/structured-data/
- **Owning departments:** D9 (Content/SEO)
- **Skills that serve it:** structured-data

## Internal linking and sitemaps
- **What:** The deliberate link architecture inside a site — which pages link to which, with what anchor text — together with the XML sitemap that lists the URLs the site wants indexed.
- **How it works:** Important pages are linked from navigation, hubs, and relevant body content so both users and crawlers reach them in a few clicks; orphan pages are found and fixed. The sitemap is generated from the actual route/content inventory, lists only canonical, indexable, live URLs, respects the protocol limits (50,000 URLs / 50 MB per file, sitemap index beyond that), and is submitted in Search Console and referenced in robots.txt.
- **Why it exists:** Crawlers discover and rank pages largely through links; a page nobody links to may never be indexed, and a sitemap full of dead or duplicate URLs wastes crawl budget and trust.
- **If missing:** New content sits unindexed for weeks, deep pages rot, and the sitemap proudly lists 404s, redirects, and noindex pages.
- **Good looks like:** Google's documented sitemap practice: fully-qualified absolute URLs, UTF-8 encoding, size limits observed, sitemap index files for large sites, and submission through Search Console.
- **Slop looks like:** A sitemap.xml generated once at launch and never regenerated, internal links that all say "click here," and a site where the pricing page is reachable only from the sitemap.
- **Verify:** Fetch /sitemap.xml, sample 20 URLs, and confirm each returns 200, is canonical and indexable, and appears in the rendered navigation or in-content links — not only in the sitemap.
- **Source:** Google Search Central, build and submit a sitemap — https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=en&visit_id=638151133303993489-3155693086&rd=1
- **Owning departments:** D9 (Content/SEO)
- **Skills that serve it:** internal-linking, sitemaps, seo-migration

## Social and open-graph
- **What:** The meta tags (Open Graph and Twitter Card) that control how a page renders when its URL is shared — title, description, image, and canonical URL in the preview card on social networks and messaging apps.
- **How it works:** Every public page emits the four required Open Graph properties — og:title, og:type, og:image, og:url — plus og:description and site name, generated from the page's own content with a purpose-built share image (commonly 1200×630). After launch, URLs are run through platform debuggers to force a fresh scrape and confirm the card renders as designed, because platforms cache previews aggressively.
- **Why it exists:** Shared links are a primary distribution channel; the preview card is effectively a free ad whose headline and image the publisher either controls or leaves to a scraper's guesswork.
- **If missing:** Links preview as bare URLs or with a random cropped image and the site's own name as the title — the share still happens, the clicks don't.
- **Good looks like:** The Open Graph protocol itself: four required properties per page, structured image properties (width, height, alt, secure_url), and type-specific properties such as article:published_time for posts.
- **Slop looks like:** og:image pointing to the homepage logo for every page, a relative image URL crawlers can't resolve, og:url set to the homepage site-wide, or tags copied from another site with its name still in og:site_name.
- **Verify:** Paste three production URLs (home, article, product) into Meta's Sharing Debugger and confirm each shows its own correct title, description, and full-size image with no warnings.
- **Source:** The Open Graph protocol specification — https://ogp.me
- **Owning departments:** D9 (Content/SEO)
- **Skills that serve it:** social-open-graph

## Lifecycle messaging (email/push campaigns)
- **What:** Automated, behavior-triggered message programs mapped to customer lifecycle stages — onboarding, activation, engagement, retention, win-back — across email, push, and in-app channels, as distinct from one-off campaign blasts.
- **How it works:** The team defines stages with entry and exit events stored on the user profile. Each stage has journeys: a trigger (signup, first purchase, 30 days inactive) starts a timed, branching sequence with a conversion goal and a control group, sent only to users with the right subscription/opt-in status. Frequency caps stop stages from colliding, and results are reported per stage against its primary metric.
- **Why it exists:** A welcome blast to everyone forever treats a loyal customer and a stranger identically; lifecycle programs send the right nudge at the moment behavior says it matters, which is where retention and repeat revenue come from.
- **If missing:** New users get no onboarding path, lapsed users get no win-back, and the only emails anyone receives are undifferentiated promotions that train them to unsubscribe.
- **Good looks like:** Braze's documented model: five lifecycle stages (acquisition, onboarding/activation, engagement, retention, win-back), each with a goal, an owner, and a primary metric, with campaigns assigned conversion events and measured against control groups.
- **Slop looks like:** A single "newsletter" automation copied from a template, still sending "We miss you!" to users who purchased yesterday, with placeholder merge fields rendering as "Hi {{first_name}}" in production.
- **Verify:** In the messaging platform, open the onboarding and win-back journeys: confirm trigger events, opt-in targeting, conversion goals, and a control group exist, and send test messages to a seed account on each channel.
- **Source:** Braze documentation, create a campaign (delivery types, targeting, conversion events) — http://braze.com/docs/user_guide/messaging/campaigns/creating_campaign
- **Owning departments:** D9 (Content/SEO)
- **Skills that serve it:** lifecycle-email

## Growth experimentation
- **What:** A disciplined program of controlled experiments — A/B tests on pages, flows, pricing, and messaging — run from written hypotheses and decided by pre-set statistical rules, so growth comes from verified wins instead of opinions.
- **How it works:** Each experiment starts with a hypothesis, one primary metric, and a planned runtime/sample size. Traffic is randomly split between control and variation; results are read on the primary metric with confidence intervals and health checks such as sample ratio mismatch detection. Winning variations are shipped, losers and inconclusive results are documented, and learnings feed the next hypothesis backlog.
- **Why it exists:** Teams reliably guess wrong about what users prefer; experimentation converts arguments into measurements and stops the highest-paid person's opinion from being the product strategy.
- **If missing:** The site changes constantly but nothing is learned — wins and regressions are indistinguishable, and a redesign can quietly cut conversion for months.
- **Good looks like:** Optimizely's documented results practice: automatic sample-ratio-mismatch health indicators, confidence intervals and false-discovery-rate control from its Stats Engine, and decision guidance to run tests at least one full business cycle and to treat losing results as usable learning.
- **Slop looks like:** A test stopped after two days because one variant was "winning," results cherry-picked from a secondary metric, five tests overlapping on the same page, and no record of any of it.
- **Verify:** Open the last concluded experiment's results page: confirm a written hypothesis, a primary metric, an SRM/health check pass, and a recorded ship/kill decision that matches the data.
- **Source:** Optimizely experimentation strategy documentation, taking action on experiment results — https://docs.optimizely.com/experimentation-strategy/docs/take-action-based-on-the-results-of-an-experiment
- **Owning departments:** D12 (Analytics), D9 (Content/SEO)
- **Skills that serve it:** growth-experiments

## Appendix A — Project-files research (Phase 0)

Slice H. Sources checked 2026-11-21. Where no external standard was found for a brief-internal file name, the entry says so instead of borrowing an unrelated citation.



GitHub's community-profile system is the closest thing to a platform-level standard for repository files: GitHub recognizes README, LICENSE, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, SUPPORT, and GOVERNANCE by name and surfaces them in the UI (docs.github.com). File conventions with named external standards behind them: CHANGELOG (Keep a Changelog), DECISIONS (the ADR practice, Nygard 2011 / MADR), .env-based config (Twelve-Factor App, factor III), runbooks (Google SRE practice). The remaining mandated files are sound professional practice but use brief-specific names; they are marked UNVERIFIED as external conventions.

| File | Purpose | In mandated 22? | Evidence / source |
|---|---|---|---|
| README.md | Project overview, setup, and entry point for every reader | Yes | GitHub community-profile standard file — https://docs.github.com/en/enterprise-cloud@latest/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file |
| CONTRIBUTING.md | How to contribute: setup, workflow, review expectations | Yes | GitHub community health file, linked when a contributor opens an issue or PR — same source as above |
| SECURITY.md | Supported versions and how to report a vulnerability privately | Yes | GitHub community health file, surfaced on the repo Security tab — same source as above |
| CHANGELOG.md | Curated, human-readable record of notable changes per version | Yes | Keep a Changelog standard: newest first, ISO 8601 dates, six change types (Added/Changed/Deprecated/Removed/Fixed/Security) — https://keepachangelog.com/en/2.0.0/ |
| DECISIONS.md | Why significant choices were made, so the reasoning survives the team | Yes | ADR practice (Nygard, 2011; MADR template): one short record per decision with context, decision, status, consequences — https://www.archyl.com/blog/architecture-decision-records-best-practices |
| .env.example | Names every required environment variable without committing secret values | Yes | Twelve-Factor App factor III: store config in the environment, strictly separate config from code — https://12factor.net/config |
| runbook.md | Step-by-step procedures an on-call engineer can execute during an incident | Yes | Google SRE practice: recorded on-call procedures with troubleshooting steps; AWS Well-Architected defines a runbook as "a documented process to achieve a specific outcome" — https://www.arvokas.io/blog/runbook-vs-playbook |
| requirements.md | What is being built, for whom, and the acceptance bar | Yes | UNVERIFIED as a fixed file name — no cross-industry standard found; requirements documents themselves are universal practice |
| progress.md | Current state: done, in progress, blocked, next | Yes | UNVERIFIED as an external convention — brief-internal file; analogous to status sections in project READMEs and sprint boards |
| stack.md | The chosen technologies and the reasons for each choice | Yes | UNVERIFIED as a file name; the content overlaps ADR territory (see DECISIONS.md row) |
| ARCHITECTURE.md | System structure, components, and data flow in one document | Yes | UNVERIFIED as a fixed file name; commonly a `docs/` document alongside a `docs/adr/` folder — https://www.outcomeops.ai/blogs/what-is-an-adr-and-why-theyre-critical-for-ai-powered-development |
| handover.md | What a new owner needs to run, maintain, and extend the project | Yes | UNVERIFIED as an external convention — brief-internal file |
| fact-sheet.md | Verified facts about the product/company that copy and code may cite | Yes | UNVERIFIED as an external convention — brief-internal file (Real Content Rule artifact) |
| API_CONTRACTS.md | The API's endpoints, payloads, and guarantees in one reference | Yes | UNVERIFIED as a file name; the machine-readable equivalent is an OpenAPI document, which this file should point to rather than duplicate |
| SCHEMA.md | Human-readable map of the database schema and its invariants | Yes | UNVERIFIED as an external convention — brief-internal file; migrations remain the machine source of truth |
| DESIGN_TOKENS.md | The named color, type, and spacing values the UI is built from | Yes | UNVERIFIED as a file name; token-based design systems are standard practice, the file name is not |
| SECURITY_BASELINE.md | The non-negotiable security rules every project in the repo follows | Yes | UNVERIFIED as an external convention — brief-internal companion to SECURITY.md (which is per-project reporting policy) |
| OBSERVABILITY_SPEC.md | What is logged, metered, traced, and alerted on, and to what standard | Yes | UNVERIFIED as a file name; observability practice itself is covered by the SRE literature cited in the runbook row |
| CONTENT_METADATA.md | Titles, descriptions, and structured-data rules for content pages | Yes (conditional: content projects) | UNVERIFIED as an external convention — brief-internal file |
| PAYMENT_SECURITY.md | Payment-handling rules (PCI scope, no card data in app code/logs) | Yes (conditional: payment projects) | UNVERIFIED as a file name; PCI DSS itself is the governing standard, not this file |
| CLONE_DESIGN_SYSTEM.md | The extracted design system a clone/rebuild must match | Yes (conditional: clone projects) | UNVERIFIED as an external convention — brief-internal file |
| TESTING.md | Test strategy: what is tested at which level, and the coverage bar | Yes | UNVERIFIED as a standalone file name; test documentation more often lives in CONTRIBUTING.md or `docs/` |

### Additions the research supports

Files not in the mandated 22 that real projects commonly keep, each with a source:

- **LICENSE** — GitHub detects and displays it, and the community-profile checklist expects one; without it the default is "all rights reserved," which blocks reuse. Source: https://raw.githubusercontent.com/joelparkerhenderson/github-special-files-and-paths/main/README.md
- **CODE_OF_CONDUCT.md** — A GitHub community health file defining engagement standards; surfaced on the repo's community profile. Source: https://docs.github.com/en/enterprise-cloud@latest/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
- **SUPPORT.md** — A GitHub community health file telling users where to get help; linked when someone opens an issue, which reduces misdirected bug reports. Source: same docs.github.com page as above
- **GOVERNANCE.md** — A GitHub community health file stating how decisions are made; fits this repo's Board/Orchestrator structure. Source: same docs.github.com page as above
- **CODEOWNERS** (in root, `docs/`, or `.github/`) — Assigns reviewers per path; GitHub auto-requests their review on pull requests and branch protection can require their approval. Source: https://docs.github.com/enterprise-cloud@latest/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- **`docs/adr/` folder** — Standard ADR practice stores one numbered file per decision (`0001-use-postgresql.md`) rather than one growing DECISIONS.md; DECISIONS.md can stay as the index. Source: https://www.outcomeops.ai/blogs/what-is-an-adr-and-why-theyre-critical-for-ai-powered-development
- **`.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`** — GitHub-recognized template files that structure incoming reports and PRs; the brief's §11 feedback loop files issues, so templates serve it directly. Source: https://raw.githubusercontent.com/joelparkerhenderson/github-special-files-and-paths/main/README.md
- **`.gitignore`** — Prevents secrets, build output, and dependencies from being committed; every professional repo has one. GitHub publishes official per-stack templates — UNVERIFIED in this pass (not fetched), widely known.
- **`.github/dependabot.yml`** — GitHub-recognized config for automated dependency-update PRs; supports the repo's quarterly claim/dependency re-verification duty (§11). Source: https://raw.githubusercontent.com/joelparkerhenderson/github-special-files-and-paths/main/README.md

## Appendix B — Playbook-set justification (Phase 0, §5.6)

The 20 types below are business-function types (what a client asks for), drawn from agency and platform category lists, not architecture patterns (SPA/MPA/PWA are build choices that cut across all 20). Sources: BairesDev's web-application type list (https://www.bairesdev.com/blog/types-web-application-development/), DEV's custom web application breakdown for businesses (https://dev.to/applogiq_it_services/types-of-custom-web-applications-what-every-business-should-know-482a), a business web-application survey covering CRM, portals, stores, booking, and analytics (https://ostohlo.com/blog/veb-prilozheniya-dlya-biznesa.html), and a portal/CMS/e-commerce type survey (https://provisiosolutions.com/blog/2021/10/14/what-types-web-apps-are-used-businesses).

| # | Web-app type | Maps to playbook | Gap? |
|---|---|---|---|
| 1 | SaaS product (subscription software) | SaaS web app | No |
| 2 | E-commerce store | E-commerce store | No |
| 3 | Two-sided marketplace | Two-sided marketplace | No |
| 4 | Blog / news / content site | Content / blog site | No |
| 5 | Portfolio / marketing site | Portfolio / marketing site | No |
| 6 | Landing page / lead generation | Landing page | No |
| 7 | Analytics / admin dashboard | Dashboard / admin panel | No |
| 8 | Internal business tool / CRM | Internal CRUD / admin tool | No — CRM is this playbook's core case |
| 9 | API / backend service for other apps | API + database service | No |
| 10 | Real-time chat / messaging app | Real-time / chat app | No |
| 11 | Clone / rebuild / platform migration | Clone / rebuild | No |
| 12 | Booking & appointment system (clinics, salons, rentals, hotels) | SaaS web app (nearest) | **Yes** — availability calendars, slot holds, reminders, no-show and cancellation flows, and per-resource scheduling are the product, not SaaS features; no playbook names them |
| 13 | Online learning platform (LMS: courses, lessons, progress, quizzes) | Content / blog site (nearest) | **Yes** — enrollment, progress tracking, assessments, and certificates have no home; content playbook covers publishing, not learning state |
| 14 | Customer / client portal (invoices, tickets, documents, account self-service) | Dashboard / admin panel (nearest) | Partial — the dashboard playbook is staff-facing; a portal is customer-facing with different trust, onboarding, and support flows |
| 15 | Directory / listing site (search-led catalog, e.g. a tools directory) | Content / blog site (nearest) | Partial — taxonomy, faceted search, listing submission, and verification workflows exceed the content playbook |
| 16 | Social network / community platform | Real-time / chat app (nearest) | Partial — chat covers messaging only; feeds, follows, moderation, and reporting are uncovered |
| 17 | Job board | Two-sided marketplace (nearest) | Partial — listings and applications fit the marketplace shape, but there are no transactions, payouts, or escrow to gate |
| 18 | Help desk / support portal | Internal CRUD / admin tool (nearest) | Partial — agent side fits CRUD; the customer-facing ticket submission and status side is a portal (row 14) |
| 19 | AI-powered app (chatbot, AI feature product) | SaaS web app + D17 step | Partial — §5.6 already handles this by rule (SaaS playbook plus an explicit D17 step); acceptable, but the rule lives outside the playbook files |
| 20 | Regulated-industry portal (patient portal, banking dashboard) | Dashboard / admin panel (nearest) | Partial — the flow maps, but sector compliance (health/financial data rules) is a D14 variation no playbook states |

**Verdict:** The 11-playbook set covers the commercial core — 11 of the 20 types map exactly, and the brief's own fallback rule (match on payments/accounts/content-led, most answers wins) absorbs the partial fits without inventing process. It is not sufficient as-is: two common, high-demand types are real gaps, not partial fits. Add a **Booking & scheduling** playbook (row 12: calendar/slot state, reminders, cancellation policy, per-resource availability — a distinct data model and failure set) and an **Online learning (LMS)** playbook (row 13: enrollment, progress state, assessments — state machines the content playbook never exercises). The remaining partial fits (portal, directory, job board, community, regulated portal) are variants of existing playbooks and should be recorded as named variants inside those playbook files rather than as new playbooks, keeping the set at 13.

## Appendix C — Traceability

- Method: every element's "Skills that serve it" line was extracted by script and diffed against the 227-skill catalog in MASTER_BRIEF.md §3.12, in both directions.
- Result at Phase 0 exit: 227/227 skills trace to at least one element; 127/127 elements name at least one serving skill; 0 orphans in either direction.
- The first pass (68 elements, the §4-named set only) left 74 skills untraced — all of D3, D17, D18 plus depth skills — which is why Parts 7–9 and 11–12 exist: the brief's element list is a floor, and the research found what it does not name.

**Phase 8 addendum (2026-11-21, v1.1.0):** the catalog has since grown to **235 skills / 128 elements**. Phase 8's debater stage assigned anatomy elements to all 8 new hybrid-mission skills and added one new element — **Market expansion** (serving `market-expansion`) — bringing the element count from 127 to 128; `SKILLS_INDEX.md` was regenerated with zero "no anatomy element" warnings. This addendum records the growth only; the Phase 0 traceability record above stands unaltered as the Phase 0 exit result.

