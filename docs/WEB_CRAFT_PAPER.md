> **Editor's note (OmniForge inheritance, Phase 2).** This paper is inherited from the Web Craft Pro Max project and is reproduced unchanged except for figure corrections: the parameter, family, and tell counts have been corrected throughout to the final research figures — **178 parameters, 17 families, 221 tells** — replacing the superseded 170 / 16 / 213 figures carried in the inherited draft. The paper's human-detection calibration claim (~55.5% human accuracy detecting AI-generated websites) was re-verified in Phase 1: verdict **partially supported** — the near-chance ballpark is consistent with the traceable evidence, but the exact figure could not be traced to a peer-reviewed, website-specific study and must not be cited as a measured fact. See the Calibration section of `skills/detection/visual/PARAMETERS.md`. No other changes have been made to the body.

---

# Why Websites Look AI-Generated — and How to Stop Building Them That Way

## A research synthesis from the Web Craft Pro Max project

**Date:** 21 November 2026
**Status:** Synthesis of a 132-agent research programme conducted 21 November 2026
**Coverage:** 100 worker research files, 15 detection research files, 25 pre-existing specification parts, 10 minor-lead reviews, all 7 major-lead finalized domain files (D1–D7), and 2 major-lead debate files (M5, M7, round R0). The remaining debate files (M1–M4, M6) and the decisions log had not yet been delivered when this paper was written; D2's finalized file was still being written during the debate round (see §8).
**Total evidence base:** 155,782 lines of research, review, finalized, and debate material.

---

## 1. Abstract

In 2026, a large and growing share of new websites is instantly recognizable as AI-generated — not by any single feature, but by a *constellation* of tells: the same indigo gradient, the same three identical feature cards, the same Inter typeface, the same "delve" and "elevate" copy, the same `opacity: 0, y: 20` entrance animation, the same shadcn button recipe. This paper synthesizes a one-day, 132-agent research programme that set out to answer two questions: **(1) by what signals is a website detected as AI-generated, and (2) what rules reliably defeat each signal?**

The research produced a **detection taxonomy of 178 catalogued parameters across 17 families** (Part 00's family list claimed 178 across 17, but a grep count by major lead M7 during the debate round found 178 identified parameter rows in 17 families — the "A11Y 8" family does not exist in the catalog; see §4.1 and debate contest C-101), extended by **43 gap tells** discovered during detection research, for a reconciled detection surface of **221 tells**. It catalogued how detectors actually work — six families of text detection, weighted tell-aggregation website scorers, LLM-as-judge evaluation, and human judgment — and measured their accuracy honestly: vendor claims run 15–30 points above independent benchmarks, and pooled human detection accuracy across 56 studies is 55.54%, barely above chance, because the signals that betray AI output are largely *tacit* — a "feels off" verdict formed in 50 milliseconds to 3 seconds.

The central findings are: **(i)** detection is aggregative — no single tell convicts; three or more visible tells form the "slop fingerprint"; **(ii)** every ban needs a derivation instruction, because banning the obvious defaults produces *escape clusters* (cream-and-terracotta, near-black-and-acid) that are themselves detectable; **(iii)** the strongest tells are *interaction* tells, because a click is proof — a button that does nothing is undetectable in a screenshot and damning in use; **(iv)** detection is a moving target — tell lists decay in months, and the skill built from this research needs a stated re-verification cadence (M7's debate position is 90 days; D3 argued six months — contest C-107, still open); and **(v)** the cure is not a list of bans but a generative system: theme invention from the subject's own world, derivation of every colour from a named source object, semantic motion, a fact sheet behind every claim, and a design brief that enforces measurable divergence from the builder's own last three projects.

The paper also reports the research's limits plainly: 72 of the evidence files were affected by HTTP 429 rate limits during web verification; several workers obtained no live web verification at all; no peer-reviewed study blind-tests whole websites for AI detection; no detector score has been validated against human judgment on the same pages; and several widely quoted figures (including a "73% of AI frontends use Inter" claim) are secondhand or single-source and are flagged as such rather than asserted.

---

## 2. Introduction

### 2.1 The problem

Open a website built by a modern AI agent in 2026 and you will very likely know it within three seconds. Not because you can name what is wrong — most people cannot — but because something *feels off*. The hero is centered. The headline is heavy. The gradient is purple-to-blue. Three identical cards sit in a row, each with a Lucide icon in a rounded square. The copy says the product will "elevate" your workflow and "delve into" your data. The buttons are pill-shaped. The typeface is Inter.

None of this is a defect in isolation. Inter is a good typeface — Linear ships it and scores zero on slop detectors. Gradients are fine. Cards are fine. The problem is *convergence*: the same defaults, chosen by the same models, trained on the same data, producing the same page shape again and again. A 2026 analysis of 1,590 Show HN landing pages (Krebs, April 2026) found 22% were "heavy slop" — four or more recognizable AI patterns — and 32% mildly so, leaving only 46% clean. A 2025 study cited in the research found more than 80% of AI-generated websites sharing almost the same structure. The user who commissioned this research put it from experience: he opened a site, knew instantly it was AI slop, and an AI evaluation scored it 86–96% AI-generated.

### 2.2 Why it matters

The stakes are not aesthetic snobbery. A website that reads as AI-generated reads as *untrustworthy*: generic claims, fake testimonials, stock imagery, and dead buttons signal a business that does not exist or does not care. For the user commissioning this work — founder of a sovereign-engineering company who also runs a YouTube channel and an Instagram presence — the website is the public face of the enterprise, and "looks AI-generated" is a credibility failure, not a style preference.

There is also a legal dimension the research surfaced: the US Federal Trade Commission's Rule on Consumer Reviews and Testimonials (16 CFR Part 465, in force October 2024) explicitly covers AI-generated fake reviews and testimonials. Fabricated social proof is no longer merely sloppy; it is regulated.

### 2.3 The research goal

This programme was commissioned with a specific brief: **research first, then write the cure**. Define *all* the detection parameters — as many as possible, each defined — then design the cure from the diagnosis. The brief also set a distinctiveness bar drawn from web history: in 2002, Google's and Apple's homepages were 1000% different, with no precedent for either. Every site built with the resulting skill must be that distinct. And it set a theme rule: break the market's theme tradition — no more recycled minimalist, glassmorphism, or bento-grid defaults; invent genuinely new themes per project, changing animation methods, themes, and gradients — while never breaking beauty.

The programme's output is a portable skill file ("Web Craft Pro Max") — custom instructions usable in any AI agent or large language model — that makes the agent build websites which are unique, exceptionally beautiful, complete, functional, and optimized for search, answer, and generative engines. This paper is the research synthesis behind that skill: what was found, how it was found, what it means, and what remains unknown.

### 2.4 A note on the "Manus score"

The user's original evidence for the problem was a score of 86–96% AI-generated attributed to "Manus AI". Two independent detection files (X001, X013) investigated this and reached the same correction: **Manus is not a detector**. It is an autonomous agent. An 86–96% "Manus score" is an uncalibrated LLM-as-judge evaluation — one model judging another's output — not a calibrated measurement. The research treats the user's underlying observation (the site was instantly recognizable as AI-generated) as valid and well-supported, but the number itself as uncalibrated. This distinction matters because much of the "AI detection" discourse confuses LLM opinion with measurement; §5.1 lays out what calibrated detection actually looks like.


---

## 3. Methodology

### 3.1 Team structure

The research was conducted on 21 November 2026 by a team of **132 agents** with defined, non-overlapping roles, coordinated through shared files (agents could not message each other directly):

| Layer | Count | Role |
|---|---|---|
| Worker researchers | 100 (W001–W100) | Each owned one specific research topic and wrote one research file, in 7 domains |
| Detection researchers | 15 (X001–X015) | Researched what defines the "AI loop" — every signal that reveals AI generation |
| Minor leads | 10 (ML1–ML10) | Reviewed one domain slice each (7–14 files), wrote verdicts and required fixes |
| Major leads | 7 (M1–M7) | One per domain; finalize their domain's section from worker outputs and reviews; M7 assembles the final skill |

The 7 domains were: **D1** Anti-slop & uniqueness (W001–W015); **D2** Motion & interaction (W016–W030); **D3** Visual craft (W031–W044); **D4** Search & content (W045–W058); **D5** Engineering (W059–W072); **D6** Experience & responsive (W073–W086); **D7** Integration & quality (W087–W100).

The detection squad (X001–X015) was added on the user's direct order — "until detection is identified, nothing can be finalized" — and major lead M1 was instructed to wait for all 15 detection files before finalizing D1. This sequencing (identify first, then cure) is the programme's core methodological commitment.

### 3.2 Evidence base

The synthesis draws on six bodies of material, totalling **155,782 lines**:

| Source | Files | Lines |
|---|---|---|
| Worker research files (`research/D1–D7/`) | 100 | 85,355 |
| Detection research files (`research/detect/`) | 15 | 10,718 |
| Pre-existing specification parts (`parts/`, 00–28, some missing) | 25 | 10,775 |
| Minor-lead reviews (`reviews/minor/`) | 10 of 10 | 3,325 |
| Major-lead finalized domain files (`finalized/`) | 7 of 7 (D1–D7) | 44,871 |
| Major-lead debate files (`debate/`, round R0) | 2 (M5, M7) | 738 |

Workers were instructed to **reuse, not redo**: each worker first read the existing part(s) relevant to its topic, verified the content, reused what was good, fixed what was weak, and added what was missing. Missing parts (17 colour/gradients, 20 navigation, 24 conversion, 27 i18n) were covered by workers W034, W077, W078, and W083 respectively.

### 3.3 Source verification and honest-gap reporting

Two rules governed every research file:

1. **Never invent a source, author, or figure.** Where a web fetch failed, the worker either used an accessible mirror or secondary source (labelled as such) or stated the gap honestly in its Sources section. Nothing in the research is quoted from a page that returned an error.
2. **Every file carries a Gaps section.** Workers listed what their topic still missed, what they could not verify, and what a follow-up worker should do. Minor leads added their own gap lists, and finalized files consolidated them (D3's finalized file lists 33 consolidated gaps; D4's lists its own in Appendix C).

Minor-lead review was substantive, not ceremonial. Reviewers re-counted parameter tables by grep, spot-checked cross-references against the parts on disk, and checked cited statistics against each file's own Sources section. They caught real errors: W001's totals paragraph was wrong (it claimed 112 carried-over and 60 new parameters; the recount showed 100 and 72); W087's section budgets summed to 14,250 lines against a stated 12,000-line hard cap; W024 corrected a WCAG level error (2.3.3 is AAA, not AA); W040 contained a factual error about Firefox View Transitions, corrected at finalize with MDN release notes. Review verdicts were mostly FIX (see §3.5), and fixes were applied or logged at finalize time — D3's finalized file carries a resolutions log of 9 cross-file conflicts (C1–C9), 6 review issues (ML6-1–6), and 15 factual fixes (F-1–F-15); D4's carries a fix log, a preserved-caveats appendix, and a source-honesty note.

### 3.4 How this paper was written

This paper synthesizes the evidence base by reading the highest-value files in full (the parameter catalog, the diagnosis-and-cures part, all 15 detection files' key sections, the skill-architecture and instruction-writing files, the case-study and rubric files, and all finalized files' resolutions logs and gap inventories) and by systematic extraction across the whole corpus: every heading (5,247 lines of headings), every Gaps/Limitations section (5,347 lines), every Sources/References section (6,664 lines), and every URL (904 unique URLs). Figures are cited only where the research files support them; where a figure is single-source, secondhand, or unverified, the paper says so in place (§8 collects them all).

### 3.5 The review record

At the time of writing, all 10 minor-lead reviews were complete. The verdict pattern is informative about the corpus's quality:

| Review | Domain slice | ACCEPT | FIX |
|---|---|---|---|
| ML1 | D1 W001–W008 | 8 (all "ACCEPT with fixes") | 0 |
| ML2 | D1 W009–W015 | 0 | 7 |
| ML3 | D2 W016–W023 | 0 | 8 |
| ML4 | D2 W024–W030 | 3 | 4 |
| ML5 | D3 W031–W037 | 2 | 5 |
| ML6 | D3 W038–W044 | 4 | 3 |
| ML7 | D4 W045–W058 | 8 | 6 |
| ML8 | D5 W059–W072 | 9 | 5 |
| ML9 | D6 W073–W086 | 7 | 7 |
| ML10 | D7 W087–W100 | 0 | 14 |

41 files accepted (8 of them with fixes), 59 marked FIX.

No file was rejected outright. The dominant defect class was **cross-file contradiction**, not fabrication: D7 alone had 20 conflicts between its own workers (on size models, label names, version formats, checklist caps, and example mandates); D2 had 5; D4's only blocker was a meta-description length conflict. The review layer's main value was catching these contradictions before finalization — and the finalized files show the fixes being applied, not merely listed.

### 3.6 Limits of the methodology

The methodology has four limits that shape everything that follows (each is expanded in §8):

1. **Rate-limited web verification.** 72 files in the evidence base mention HTTP 429 (rate limiting) during web research. Several workers — W010, W025, W063, W069, W079, W088 — obtained *zero* or near-zero successful web fetches and say so. Their files make no web-sourced claims (W069's numbers are labelled skill prescriptions, not sourced claims), which is honest, but it means parts of the evidence base rest on the workers' training knowledge and on the pre-existing parts rather than on fresh sources.
2. **No live tool testing.** No detector was run against a test site during this research; all detector figures come from vendor documentation, published benchmarks, and third-party reviews. No live site audit was performed for the colour, spacing, or layout findings.
3. **English-first evidence.** Detection research is overwhelmingly English-first; Hindi/Urdu detection is materially weaker and largely unstudied in the sources consulted.
4. **Single-day, single-pass research.** The programme ran in one day. Figures were verified against the files' own Sources sections by reviewers, but web sources were checked as cited (sample, date, URL, first-hand vs second-hand), not re-fetched by reviewers — no live browser was available to the review layer.


---

## 4. The AI-detection taxonomy

### 4.1 The 178-parameter catalog

The programme's foundational artifact is a catalog of **178 detection parameters across 17 families**, defined in Part 00 of the pre-existing specification and carried verbatim into the worker research:

| Dimension | Code | Count | What it covers |
|---|---|---|---|
| Layout | LAY | 10 | Page shape, hero structure, section order |
| Section | SEC | 8 | Section types and their sequencing |
| Typography | TYP | 10 | Typeface choice, pairing, scale |
| Colour | COL | 12 | Palette, gradients, accent usage |
| Copy | CPY | 15 | Wording, claims, cadence |
| Motion | MOT | 13 | Animation patterns and timing |
| Components | CMP | 18 | Cards, buttons, nav, pricing, forms |
| Imagery | IMG | 10 | Stock vs generated vs real imagery |
| Icons | ICO | 6 | Icon systems and usage |
| Spacing | SPC | 7 | Rhythm, padding, section gaps |
| Code | COD | 20 | Class names, DOM patterns, framework fingerprints |
| Naming | NAM | 8 | Product/brand naming patterns |
| Data | DAT | 7 | Stats, testimonials, social proof |
| Behaviour | BEH | 10 | Interaction and state behaviour |
| Meta | MET | 10 | Metadata, SEO, and head content |
| Cluster | CLU | 6 | Cross-dimension tell combinations |

**A correction, and why it matters.** Part 00's own family list claimed 178 parameters across 17 dimensions, including an "A11Y 8" (accessibility) family — and that 178 figure was repeated through the worker research and D1's finalized file. During the debate round, major lead M7 counted Part 00 by grep and found **178 identified parameter rows in 17 families; no A11Y family exists in Part 00** — no A11Y-01–A11Y-08 parameters are defined anywhere. The 178 figure was a miscount in the catalog's own family list, and D1's list sums to 178 only because it adds the phantom "A11Y 8" (debate contest C-101; M7's position is to fix the count to 178/221, rejecting the alternative of inventing 8 parameters to rescue the miscount). D7's finalized file already uses 178/17 throughout. This paper uses the verified 178/17 figures everywhere and notes the correction wherever the 178 figure would otherwise appear. It is a small error with a real consequence: every parameter-count gate in the skill (G-DES-01, G-QA-03, REV-03) cites the catalog as its denominator, and a wrong denominator means QA counts that never reconcile.

The catalog's scoring method is aggregative: a single signal never convicts. **Three or more visible tells form the "slop fingerprint"; four or more mean "heavy slop"** — the same threshold the Krebs study used (22% of Show HN landings were heavy slop at 4+ patterns). This mirrors how real detectors work (§5.1): weighted aggregation, not single-signal verdicts.

### 4.2 The extended surface: 221 tells

Detection researcher X015, tasked with mapping every catalog parameter to its detection signal and cure, found **43 additional tells (GAP-01–GAP-43)** that the 178-parameter catalog did not cover — including watermark/provenance signals (which have no Part 00 ID at all, a catalog gap X013 also flagged), pasted-chat fingerprints in shipped HTML, and interaction tells visible only through behaviour probing. The reconciled detection surface is therefore **221 tells (178 + 43)**.

Beyond the reconciled 221, the research defined many more *overlapping* signals that await deduplication by the major leads: W001 defined 172 visual parameters (100 carried from Part 00, 72 new, in new categories HERO, SYM, DEN, NAV, GL); W002 defined 93 code/structure parameters; W003 defined 75 copy parameters; W004 catalogued 34 default layouts (AL-01–AL-34); W005 added 18 colour entries (ADC-13–30); W006 added 40 typography entries plus 25 pairing rules; W007 added 41 imagery tells; W008 added 20 animation tells. The detection squad added its own counts per dimension (see §5). These overlap heavily — different researchers covering the same tells from different angles — and minor-lead review ML1 explicitly lists "overlaps to dedupe at merge". This paper does not sum them into a single inflated number; 221 is the reconciled figure, and the rest is raw material for the major leads' merge. (D1's finalized file adds a third reference: a **banned-pattern master list of 197 entries**, authoritative for enforcement — what is forbidden and how severely — while the detection catalog governs auditing and the cure map governs fixing.)

### 4.3 Six detection channels

X015 organized detection into **six channels**, each with its own evidence type and its own self-test procedure:

| Channel | What it inspects | Example evidence |
|---|---|---|
| **R** — Rendered style | The page as the eye sees it | Gradient, typeface, card grid, spacing rhythm |
| **S** — Static source | HTML/CSS/JS as shipped | Class names, framework fingerprints, pasted-chat attributes |
| **T** — Text statistics | Copy as data | Perplexity, burstiness, "delve" frequency, em-dash density |
| **C** — Code statistics | Code as data | Comment density, identifier length, function-size distribution |
| **B** — Behaviour probing | The page as used | Dead buttons, fake forms, broken state transitions |
| **H** — Human review | The page as judged | The 50 ms–3 s gut verdict, the five-second test, paired comparison |

The six-channel model matters because most "AI look" discussions cover only channel R. Channels S, C, and B are invisible in a screenshot and decisive in practice: a page can pass every visual test and still betray itself through a `data-start` attribute pasted from a ChatGPT conversation, a comment density of 18%, or a "Get Started" button that goes nowhere.

### 4.4 Why AI output converges: three forces

Part 01's diagnosis identifies three forces behind the convergence:

1. **Repetitive training data.** Models are trained disproportionately on the same popular templates, tutorials, and starter kits — Tailwind's defaults, shadcn's recipes, Vercel's Geist aesthetic. The most common training examples become the most likely outputs.
2. **A feedback loop.** AI-generated sites are published, indexed, and scraped into the next generation's training data. Each cycle tightens the convergence.
3. **Safety bias.** Models optimize for "acceptable" output. The safest choice — the most common, least objectionable layout, colour, and phrase — is also the most recognizable. Novelty is risk; the model avoids risk by default.

The consequence is distributional: AI output is not *bad* design, it is *modal* design — the statistical centre of the training distribution, repeated. The cure, therefore, cannot be "try harder"; it must be a system that forces the agent *away* from the mode on every dimension simultaneously (§6).

### 4.5 The detection timeline: how fast a human verdict forms

X014 synthesized the human-detection literature into a timeline. The verdict is not one event but a cascade:

| Window | What happens | Evidence |
|---|---|---|
| **0–50 ms** | Gut verdict on visual appeal and "feels off" | Lindgaard et al. 2006: reliable appeal judgments in 50 ms, stable (r = .97–.98); Tuch et al. 2012: prototypicality effects even at 17 ms |
| **0.8–2.6 s** | First fixation — the headline, then the hero | Eye-tracking literature (headline-first); Missouri S&T figures cited as secondary, primary paper not verified |
| **3–5 s** | Constellation verdict — the "three-second slop call" | Practitioner evidence; the tells aggregate into a verdict before any single tell is named |
| **5–30 s** | Copy verdict — wording, claims, cadence | Kobak et al.: "delve" appears 25.2× more often in post-ChatGPT abstracts (14M+ PubMed abstracts) |
| **30 s+** | Interaction verdict — clicking, scrolling, filling forms | Interaction tells are the strongest class (§5.12) because a click is proof |

Two implications follow. First, the 50 ms gut verdict means the *first impression is formed before conscious analysis begins* — the prototypicality paradox (Tuch et al.): the most prototypical design is judged most appealing in 50 ms, which is exactly why AI defaults feel "fine" at first glance and "off" on reflection. Second, the verdict is largely *tacit*: Högemann et al. (2025) found judgments going tacit — "feels off" — as models improved, and the worst human detectors are the most confident (Miller et al. 2023).


---

## 5. Key findings per dimension

### 5.1 Detector mechanics: how detection actually works

**Six families of text detection.** X001 and X013 converge on six families: (1) statistical scoring (perplexity, burstiness, log-likelihood curvature); (2) trained classifiers (fine-tuned models on human/AI pairs); (3) zero-shot probability methods (GLTR, DetectGPT, Fast-DetectGPT, Binoculars, Ghostbuster); (4) stylometry (authorship fingerprints — function-word frequencies, punctuation habits, sentence-length distributions); (5) retrieval (matching against a database of known AI outputs); and (6) watermarking/provenance (cryptographic marks embedded at generation — Kirchenbauer et al.'s green-list watermark, ICML 2023; Google's SynthID, now on 100B+ pieces of content; C2PA provenance manifests, ISO/IEC 22144:2025; Claude watermarking from 2 August 2026, the same date the EU AI Act's Article 50(2) labelling duty took effect).

**The perplexity story is a cautionary tale.** GPTZero — the best-known text detector — stopped using perplexity and burstiness as its detection method in autumn 2023, moving to a deep-learning classifier with sentence-by-sentence scoring; perplexity is now one of seven indicators. Yet public discussion still treats perplexity as *the* detection method. The research documents why: paraphrase destroys perplexity's power (Mıhcı et al., June 2026: perplexity ROC-AUC 0.969 on raw AI text, collapsing under paraphrase) while burstiness holds up better (0.953). Any detection strategy that rests on a single statistic is fragile by construction.

**Website detectors are weighted tell-aggregators.** The website slop detectors surveyed (madewithjev, slop-detect, Briskly, Unslop Me, LandingBoost, SlopTotal, aiwebsitedetector.net) all work the same way: a catalog of tells, each with a weight, summed into a score. Published weights make the hierarchy visible:

- **Heaviest:** builder fingerprints (+55 to +60 in aiwebsitedetector.net's scale), Lucide icons in tiles (−40 in LandingBoost's scale, present on 37% of Lovable sites vs 1% of gallery SaaS), heavy headline (−19).
- **Mid-weight:** purple/indigo gradient (−20 in Unslop Me), generic AI copy (−16), default Tailwind palette (−14), Inter/system-font only (−12), emoji as icons (−12), uniform icon-card grid (−12), glassmorphism (−10), builder badge (−10).
- **Light:** rounded-2xl (−8), default Lucide icons (−8), centered hero (−6), low type-scale contrast (−6).

Two modifiers matter: custom type plus a non-stock palette multiplies deductions by 0.6 (Unslop Me), and LandingBoost's model validated at 84% held-out accuracy (79% on an unseen builder, Bolt) on a 558-homepage calibration set. Madewithjev splits its score 60% holistic ("assembled from defaults?") and 40% top-8 tells, with bands from 0–19 "hand-made" to 80–100 "pure slop".

**Vendor claims are systematically inflated.** The most consistent finding across X001 and X013 is the gap between vendor claims and independent measurement: **15–30 points**. GPTZero claims 99% accuracy; Scribbr's 12-tool benchmark measured 52% overall. Copyleaks claims 99.12%; measured 66%. ZeroGPT claims 98.4%; peer-reviewed measurement found 64.35%. Originality.ai's vendor claim of 99%+ sits against independent measurements of 83–96% with a false-positive rate of 4.8–12%. A June 2026 study (VUB, *International Journal of Educational Integrity*) found Turnitin scored all 40 fully-AI papers below its 20% threshold — and Turnitin's own CPO admitted the company intentionally skips roughly 15% of AI content to reduce false positives. In January 2026 a New York court annulled a 100% Turnitin flag on a human-written essay (the Adelphi case). **Pangram is the exception**: peer-reviewed (arXiv:2402.14873), trained on synthetic mirrors of human text, it scored 99.3% on the RAID benchmark and 97.5% inclusive accuracy in the VUB study, and flagged 0 of 495 human passages in Epoch AI's July 2026 test. It is the strongest verified detector in the survey.

**Accuracy collapses in five situations** (X001): short text; edited, paraphrased, or hybrid text (a Notre Dame study, October 2026, found that after humanizer tools fewer than 4% of texts stayed flagged, and lightly edited text was flagged only 38–80% of the time); style imitation (Epoch AI: 10.1–17.8% of style-imitated passages missed); non-native or formulaic writing (Liang et al. 2023, *Patterns*: 61.22% false-positive rate on 91 TOEFL essays across seven detectors; SlopTotal flagged 15% of TOEFL essays vs 0% of US school essays); and adversarial prompting.

**The honest summary:** detection is a probabilistic, aggregative, decaying capability — not a lie detector. Confidence scores mean different things per vendor (probability of AI authorship, share of text judged AI, or a weighted slop sum), and the same text can score 0% on one tool and 100% on another.

### 5.2 Layout tells: the canonical skeleton

X002 verified the **canonical AI layout skeleton** against five independent sources: centered hero with eyebrow badge, heavy headline, subhead, two CTAs; logo strip; three identical feature cards; "how it works" three steps; testimonial grid; pricing tiers; FAQ accordion; big CTA; footer. The single strongest layout fingerprint is **CMP-01: three identical feature cards** — same icon, same title length, same body length, same card chrome. The cure is structural, not cosmetic: break the skeleton itself (asymmetric grids, editorial layouts, narrative sequencing), not merely restyle it.

W004 catalogued 34 default layouts (AL-01–AL-34) with forced alternatives for each, and W013's case studies show what replaces the skeleton in practice: Lusion v3's camera-through-Z-depth scroll, Bruno Simon's drivable island, Mana Yerba Mate's flavour-per-world structure — each governed by one idea applied to 100% of the page (§5.13).

### 5.3 Typography tells: Inter is not the tell

X003 produced the largest single signal count in the detection squad: **62 new signals plus 2 confirmations**. Its headline finding is a correction: **Inter alone is not a tell**. Linear ships Inter and scores zero on slop detectors; the tell is Inter *plus* the default system stack *plus* low type-scale contrast *plus* the rest of the constellation. The 2026 fingerprint is Geist — Vercel's typeface, adopted by the newest builders — and the tell list decays as builders move on (Inter → Geist → Satoshi in roughly seven months, per W001's Gap 10).

Two figures need honest handling. The widely quoted "roughly 73% of AI-generated frontends use Inter" traces to sailop's "Why Every AI-Generated Website Looks the Same", cited secondhand by two sources; **the original article and its sample/methodology were not reviewed in this research**, and the figure is treated as attributed, not verified. The verified numbers are smaller and better-sourced: Unslop Me's leaderboard (30 AI-builder sites, 17 October 2026) found Inter/system-font-only on 63%; Emblematic's 2026 study of 390 homepages found Inter at 21.5%. A "55–95% eyebrow badge" figure in the literature was flagged unverified by X003 and is not quoted here.

W006's typography catalog (ADT-01–40 plus 25 pairing rules) and W031/W032's finalized D3 sections provide the cure: distinctive pairing rules, variable-font break-even testing (variable fonts are *not* the default — run the test), and a font-payload budget (first-load target ≤100 KB, hard ceiling 150 KB, resolved at finalize from a W031/W032 conflict).

### 5.4 Colour tells: bans create escape clusters

X004 found 16 new colour signals, including the **exact-hex fingerprint** (#6366f1 / #7c3aed / #8b5cf6 — Tailwind's indigo/violet/purple defaults), the 135° `to-br` gradient angle, and the "Claude look" (#F4F1EA warm paper + #D97757 terracotta). But its most important finding is a *second-wave trap*: **banning the obvious defaults produces escape clusters**. Tell an agent "no indigo gradients" and it produces cream-and-terracotta; ban that and it produces near-black-and-acid. The escape cluster is itself detectable. The cure is therefore never a bare ban: **every ban needs a derivation instruction** — the colour must come from a named source object in the subject's world (Lando Norris samples helmet colours; Simply Chocolate derives bar colours from ingredient photos; Mana assigns one colour per flavour as wayfinding). A colour whose source is "looks good" is deleted.

One figure is quarantined: ">50% of YC Spring 2025 startups used indigo" is single-source and flagged do-not-quote by X004. Aurora-gradient severity is disputed between sources and is treated as unsettled.

### 5.5 Copy tells: rhythm beats vocabulary

X005 catalogued 42 copy signals (24 new) and ranked detection strength: **rhythm > structure > voice > vocabulary**. The strongest copy signals are statistical, not lexical:

- **Kobak et al. (2025)** measured excess-word ratios in 14M+ PubMed abstracts: "delves" r = 28.0, underscores r = 13.8, "showcasing" r = 10.7 — and estimated that **≥13.5% of 2024 abstracts were LLM-processed**.
- **The em-dash is not a tell by itself.** Twain used 10.13 em dashes per 1,000 words; GPT-4.1 uses 10.62. Density plus position plus clustering is the signal, not the character.
- **Burstiness survives paraphrase** where perplexity does not (§5.1).

The copy cure is structural: W052's human-voice rules, W011's banned-pattern master list, and above all the **fact sheet** (§5.11) — real, specific, sourced claims replace generic ones. No website-copy-specific detection study exists in the literature surveyed; all copy-detection evidence is from academic text, and the paper flags this as a transfer gap (§8).


### 5.6 Code tells: the invisible fingerprint

X006 produced 53 code signals (X6-01–X6-53), the largest code inventory in the programme. The most damning are **pasted-chat fingerprints** — attributes and markup that survive verbatim from a chat transcript into shipped HTML: ChatGPT's `data-start`/`data-end`, Gemini's `data-sourcepos`, DeepSeek's `ds-markdown-paragraph`, Mistral's `dir="auto"`. These are *proof*, not suspicion: no human author writes them. The inventory also covers builder fingerprints (framework and hosting signatures), git forensics (single-commit histories, uniform commit messages), framework-behaviour tells, and shipped-bundle tells.

Code statistics add a probabilistic layer (Codequiry's study of 1,200 Python submissions): human code perplexity averages 5.1 (σ 1.8) vs AI 2.8 (σ 0.9); AI comment density clusters at 15–22% while human density ranges 0–40%; LLMs prefer 3–8 character identifiers. W002's 93 code/structure parameters and W059's React architecture rules (composition-first, the split test, server/client boundaries) provide the cure: code that looks like it was written by a person with a history, not generated in one pass.

### 5.7 Image tells: the physics shift

X007's 49 image signals document a **2026 shift: tells moved from objects to physics**. Hands and text — the famous 2023 tells — are largely fixed. The reliable signals now are light, shadow, and reflection: inconsistent light direction, impossible shadows, reflections that don't match their objects. The second shift is **attribution**: C2PA provenance manifests and SynthID watermarks make generated imagery cryptographically attributable, and watermarks survive metadata stripping. The hard rule the research derives: **never use generated faces as real people** — synthetic faces are rated 7.7% *more* trustworthy than real ones (Nightingale & Farid 2022), which makes the deception both effective and unethical.

W037's imagery and art-direction file (1,673 lines, the largest worker file) and W007's 41 imagery tells provide the cure: real photography with a named source, art direction from the subject's world, and honest labelling of any generated imagery.

### 5.8 Motion tells: the boilerplate problem

X008 found 20 new motion signals. The core finding: **component libraries' effect lists effectively are the tell list**. The universal `opacity: 0, y: 20` entrance, the universal 300 ms duration, arithmetic stagger delays (0, 100, 200, 300 ms), and the same easing curve everywhere — these are the defaults of the animation libraries AI agents reach for, and they are recognizable as a group. The cure is W016–W023's motion system: spring physics parameterized by element, easing curves per intent, scroll choreography with exact parameters, and the rule that motion is semantic or it is cut (a dissolve means silencing; momentum means racing; a 12 fps step means film — each motion pattern carries one named meaning in the brief, and motion with no meaning is deleted). D2's finalized file adds 12 governing rules, including: every motion must be justified (if its job is "it looks nice", do not add it); feedback within 100 ms; transform and opacity only; interruptibility mandatory; nothing hides content; reduced motion is a first-class mode (reveals instant; opacity-only fades of ≤150 ms allowed only for interactive state-change feedback — M2's ruling resolving the ML4 fade-cap conflict); ceilings are ceilings (600 ms total for any entrance/transition/cascade, 200 ms for micro-interaction feedback, 1 s for scroll lag). Debate contest C-104 harmonized the feedback numbers: acknowledge ≤100 ms, settle ≤200 ms.

One honest caveat: motion is a **minor, noisier signal in automated scoring** — about 1.1% of comments in the vibecoded-design-tells Reddit corpus mention motion tells. It matters more to human judgment (the 3–5 second constellation verdict) than to automated detectors.

### 5.9 Component tells: defaults, not libraries

X009's 21 component signals (11 new, proposed as CMP-19–29) carry a correction parallel to the Inter finding: **shadcn and Tailwind are not the tell — untouched defaults are**. X009 verified the shadcn Button recipe verbatim from the official repository and showed that the tell is the *unmodified* recipe: default radius, default padding, default shadow, default hover state, in the default arrangement. A customized shadcn component is indistinguishable from hand-built work; a default one is a fingerprint. The evidence base includes a vaultless Reddit corpus of ~3.2 million posts (3,033 comments analysed).

### 5.10 Spacing tells: metronomic rhythm

X010's 12 spacing signals narrow to one P0 tell: **metronomic section rhythm** — identical vertical gaps between every section, producing a page that breathes at exactly one tempo. The cure is W035's spacing system (an 11-value scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160 — with 20/40/80 banned, resolved at finalize from a W035/W036 conflict) and deliberate rhythm variation: dense sections against airy ones, following the content's own cadence. Two ratios in the research (3:1 heading spacing, 0.4×/0.6× mobile/tablet scaling) are **single-source working numbers**, labelled provisional at finalize, not measurements. No published study isolates spacing as an AI-detection predictor; the spacing findings are practitioner evidence, honestly labelled as such.

### 5.11 Content tells: the fact sheet

X011's 16 new content signals converge on one cure: **the fact sheet**. Every claim on the page — every statistic, testimonial, logo, date, and number — must trace to a named, real source recorded in a fact sheet before the page is written. If there is no real proof, the page says nothing rather than inventing it (D6's governing principle 4: "Trust is earned with real proof"). The legal stakes are real (§2.2): the FTC's 16 CFR Part 465 covers AI-generated fake reviews, and W078's conversion file verified its law table against primary sources. No published frequency data exists for individual content tells — another honest gap.

### 5.12 Interaction tells: the strongest class

X012's 25 interaction signals are, by the research's own assessment, **the strongest detection class, because a click is proof**. A dead "Get Started" button, a form that submits to nowhere, a pricing toggle that changes nothing, a modal that cannot be closed, a search box that searches nothing — these are not style judgments; they are functional failures, and they are invisible in a screenshot. The unifying cure: **if it looks interactive, it must behave**. X012 provides a 9-step click-through audit; W020–W022 provide button micro-interactions, hover systems, and page transitions; W082/W067 provide forms engineering. No prevalence statistics exist for any individual interaction tell — the class is strong in kind, unmeasured in frequency.

### 5.13 Human blind-test evidence: we are barely above chance

X014's synthesis of the human-detection literature is the paper's most humbling section. The headline numbers:

| Study | n | Finding |
|---|---|---|
| Diel et al. 2024 (meta-analysis, 56 papers) | 86,155 participants | Pooled accuracy **55.54%** (95% CI 48.87–62.10 — includes chance); text hardest at 52.00% |
| Cooke et al. 2024/2025 | 1,276 | 51.2% overall; image-only 49.4%; prior knowledge did **not** improve detection |
| Frank et al. 2024 (3 countries) | 3,002 | Images below 50%; AI media rated **more likely human** than human media |
| Nightingale & Farid 2022 (PNAS) | — | Faces 48.2% untrained, 59% after training with feedback; synthetic faces 7.7% more trustworthy |
| Miller et al. 2023 | — | Worst detectors most confident; the 5 faces rated "most human" were all AI |
| Högemann et al. 2025 | — | 63.7% overall but 29% for FLUX.1-dev; judgments going tacit |
| Kamali et al. 2025 | 50,444 participants, 749,828 observations | 76% synthetic / 74% authentic |

The pattern is consistent: **humans are poor detectors of individual AI artifacts, yet confident in their verdicts about websites**. The resolution is that website judgment is not artifact detection — it is *constellation* detection. No single tell convicts, but the constellation does, and the verdict is largely tacit ("feels off") rather than articulable. This is why the research's blind-test protocols matter more than its metrics: the five-second test, paired comparison, and the Tastra case study (November 2026), in which a render→look→fix loop won 13 of 13 blind comparisons — with the honest caveat that the judge was a single person (the author).

The critical gap: **no peer-reviewed study blind-tests whole websites** for AI-vs-human detection with accuracy numbers (X014 gap G-1). All lab accuracy figures above are for text, image, audio, or video — not pages. Detector scores are likewise **unvalidated against human judgment** on the same pages (G-2). The "94% of first impressions are design-related" figure, widely cited in secondary coverage, was traced to Sillence et al. on health websites but **not verified from primary text** in this research and is excluded from the skill's claims (G-4).

### 5.14 Case studies: what award-winners actually do

W013 profiled 12 award-winning non-template sites (Lusion v3, Don't Board Me, Igloo Inc, the Lando Norris official site, Mana Yerba Mate, KPR, The Other Side of Truth, Persepolis Reimagined, Prometheus Fuels, Bruno Simon's portfolio, Nomadic Tribe, Simply Chocolate) and synthesized 10 patterns:

1. **One governing idea, applied to 100% of the page.** A frozen material world (Igloo), a flavour per world (Mana), a drivable island (Bruno Simon), a truth toggle (Other Side of Truth). No winner mixes two concepts.
2. **Colour is derived, never decorated.** Every colour names its source object.
3. **Palettes are 2–3 tokens.** Lusion: 2. Lando Norris: 2. Opal Tadpole (E-commerce Site of the Year 2024): `#FFDB01` + `#FFFFFF` only.
4. **Scroll is a camera or a journey, never a page moving.** Lusion pushes the camera through true Z-depth; Prometheus runs one continuous cinematic move.
5. **The loader is part of the work.** Don't Board Me (throw a ball), Lando Norris ("Load Norris"), Persepolis (last loader frame = first content frame). A generic spinner is a defect.
6. **Type does image work.** At least one section per page must work with type alone, no image.
7. **Motion is semantic or it is cut.** One named meaning per motion pattern.
8. **Winners score lowest on usability and accessibility — and the skill must not copy that.** Accessibility sub-scores run 5.0–7.67 across the set; the skill's accessibility floors override any case-study technique that violates them.
9. **Spectacle without a maintenance owner dies.** Prometheus Fuels (301), Umami Land (301 to google.com), Simply Chocolate (plain store now), KPR (403), Pioneer Corn Revolutionized (domain no longer resolves). Before building bespoke WebGL, record who maintains it and for how long; if the answer is nobody, build the same idea in DOM + CSS.
10. **Small budgets win on one finished idea, not on scale.** Don't Board Me (Nuxt, no WebGL) beat WebGL showpieces.

A 2026 survey of 16 competitions and ~80 winning sites (blog.lynxflow.co), cited in W013, corroborates the pattern: strong brand consistency, micro-interactions, responsive design, and storytelling as the most frequent winning features; scroll-driven animation on 38 of ~80 sites; 3D/WebGL and minimalism tied at 32 each; accessibility and voice/gesture interaction almost absent.

### 5.15 Search, answer, and generative engines: the replication problem

D4's search research (W045–W058, finalized as D4.md) contains the programme's most important *negative* finding: **the flagship GEO study largely failed to replicate**.

The Princeton GEO study (Aggarwal et al., KDD 2024, arXiv:2311.09735; GEO-bench, 10,000 queries) reported that quotation addition improved citation visibility by 43%, statistics addition by 33%, fluency optimization by 29%, and citing sources by 28%, while keyword stuffing hurt by 8%. These figures are widely quoted in the GEO industry. The research verified them against the paper — and then verified the replications:

- **C-SEO Bench (NeurIPS 2025)** confirmed almost none of the effects: 3 of 54 cases significant, none of them the original GEO methods.
- **A volume-controlled replication (September 2026)** found no pooled effect at all.
- **Ahrefs' schema test (1,885 pages, August 2025–March 2026)** found AI Mode +2.4% and ChatGPT +2.2% — indistinguishable from zero — and AI Overviews −4.6%.

The finalized D4 file preserves the replication caveat *with* the Princeton figures wherever they appear (Appendix B, item B-01) and states the position plainly: **schema is identity hygiene, not a citation lever; percentage lifts must never be presented as forecasts**. W049's §7 is the evidence base, and the paper endorses its discipline: the honest GEO position is that extractable, quotable, well-sourced content is good practice, but no measured lift can be promised.

Other D4 figures are flagged as vendor data, directional only: SparkToro/Similarweb's 68.01% zero-click rate (June 2026, clickstream sample), Profound's claim that 134–167-word passages are cited 4.2× more often, Wellows' 0.664 Spearman correlation, BrightEdge's "50% under 13 weeks" figure. W048's AEO work (answer-first structure, extractability, question-headed structure, featured-snippet formatting, speakable content, FAQ with real questions only) and W053's FAQ research (FAQ rich results restricted August 2023, removed for all sites 7 May 2026, documentation removed 15 June 2026) are corroborated and carried into the finalized file. One genuine tension was resolved in D4 and confirmed in debate (C-111): **AEO vs human voice** — extraction wants a quotable answer block, human voice wants natural prose. D4's resolution: one clearly-marked answer block per page for extraction (first sentence quotable as the primary rule, 40–60-word target secondary); the rest of the page follows human-voice rules.


---

## 6. The detection→cure framework

### 6.1 The master map

X015's master map pairs every catalog parameter with its detection signal and its cure, and Part 01 provides cure rules CV-01–CV-25 (visual), CC-01–CC-10 (copy), CM-01–CM-14 (motion), and CD-01–CD-18 (code/design) covering all 178 catalog parameters (Part 01's text says 178; see the C-101 correction in §4.1), plus 12 new cure principles (GC-01–GC-12) for the 43 gap tells. The framework's structure is uniform: **for each tell class, the cure is not the absence of the tell but the presence of its opposite** — a positive, generative instruction.

| Tell class | Detection signal | Cure principle |
|---|---|---|
| Layout skeleton | Centered hero → logo strip → 3 cards → steps → testimonials → pricing → FAQ | Break the skeleton: asymmetric grids, editorial sequencing, narrative structure; one governing idea per page |
| Typography default | Inter/system-only, low scale contrast, Geist in 2026 | Distinctive pairing from the subject's world; variable-font break-even test; type that does image work |
| Colour default | Exact hex fingerprints, 135° gradients, "Claude look" | Derive every colour from a named source object; palettes of 2–3 tokens; every ban paired with a derivation instruction |
| Copy default | "Delve/elevate/showcase", generic claims, uniform cadence | Fact sheet behind every claim; human voice rules; rhythm variation; real specifics, no invented proof |
| Code fingerprint | Pasted-chat attributes, builder signatures, uniform comment density | Clean the build; code with a history; composition-first architecture |
| Image default | Stock/generic imagery, physics errors, generated faces | Real photography with named sources; art direction from the subject; honest labelling |
| Motion boilerplate | `opacity: 0, y: 20`, universal 300 ms, arithmetic stagger | Spring physics by element; easing per intent; motion semantic or cut |
| Component default | Unmodified shadcn/Tailwind recipes | Customize every recipe: radius, padding, shadow, hover, arrangement |
| Spacing metronome | Identical section gaps | 11-value scale with 20/40/80 banned; rhythm follows content cadence |
| Content fabrication | Fake testimonials, stats, logos, urgency | Fact sheet; if no real proof exists, say nothing |
| Interaction failure | Dead buttons, fake forms, broken state | If it looks interactive it must behave; 9-step click-through audit |

### 6.2 Three framework rules

**Rule 1: Every ban needs a derivation instruction.** X004's escape-cluster finding (§5.4) generalizes: a bare ban ("no indigo") displaces the default to the next most likely choice, which becomes the next tell. The cure for a banned colour is not "pick something else" but "derive the colour from this named object in the subject's world, by this method". W005's colour catalog and W034's gradient-invention method operationalize this: gradients are invented from the subject (a sunset's actual gradient, a material's actual sheen), not selected from a palette of "safe" alternatives.

**Rule 2: Score aggregate, never single-signal.** The W014 rubric scores a site 0–100 across 10 weighted categories (Layout 15, Copy & evidence 15, Colour 10, Typography 10, Imagery & iconography 10, Components 10, Motion & behaviour 10, Code & meta 10, Accessibility 5, Distinctiveness 5), with deduction checklists, anchors, automatic-fail conditions, and a fix loop. A single tell costs points; the constellation fails the build. This mirrors the detectors (§5.1) and the human verdict (§4.5): the unit of judgment is the page, not the element.

**Rule 3: The cure must be checkable.** Every rule in the framework is written to pass W088's checkability tests: a yes/no test answerable in under 60 seconds, a two-agent test (two independent agents reach the same verdict), and a stranger test (a competent person with no project context can apply the rule). "Make it beautiful" fails all three; "every colour names its source object in the brief, field 8" passes all three. W088 bans 40 vague adjectives (including *beautiful*, *seamless*, *premium*) from normative rules precisely because they cannot be checked.

### 6.3 The theme-invention method

W009's 7-step theme-invention method is the framework's generative core — the answer to "break the theme tradition":

1. Extract visual properties from the subject's own world (not from other websites).
2. Apply 3 hard constraints (drawn from the subject, not from taste).
3. Borrow from 2 non-web domains (architecture, film, print, nature, industrial design).
4. Force 3 combinations of the borrowed elements.
5. Name the theme and define its anatomy.
6. Define 3 signature elements that recur across the page.
7. Validate against 4 checks: novelty, coherence, beauty, fitness.

The method is deliberately mechanical: it forces divergence rather than hoping for it. W010's distinctiveness standard operationalizes the 2002 bar — minimum divergence requirements across 6 dimensions, with hard fails (same display + body font family as any of the last 3 own builds = repeated type system; accent hue distance ≥30°; same accent hex + same background kind = hard fail). W015 enforces it through a 15-field mandatory design brief, 12 divergence dimensions, a build log, and 3 enforcement gates.

### 6.4 Self-testing: the six-channel audit

X015 provides self-test procedures for each of the six detection channels (§4.3): render the page and run the five-second test (R); grep the shipped source for pasted-chat attributes and builder fingerprints (S); run copy statistics — burstiness, excess-word counts, em-dash density (T); measure comment density and identifier-length distribution (C); click every interactive element and submit every form (B); and run a blind paired comparison against a known-human site (H). The Tastra case study's render→look→fix loop — 13 of 13 blind wins — is the model: **blind judgment is the gate, metrics are diagnostics**.

### 6.5 What the finalize pass changed

The major leads did not merely concatenate worker files; they edited. The finalize layer's work is itself a finding about how the research matured:

- **D1 (M1):** merged 15 worker files and all 15 detection files; applied 39 targeted edits (W001's totals corrected to 100 carried / 72 new; W003's CPY-W18 study claim reworded as unverified; W006's ADT-35 payload medians dropped; W012's HT-V06 hue shift raised from 3° to ≥15° after ML2 flagged the 3° shift as a loophole; W011's L-28 rewritten to max 2 identical cards); added 11 new rules at finalize (generational novelty, density principle, precedence rules, deliberate-default rule, maintenance rule with re-check intervals, shared build-record format, scoring layering, canonical 15-field brief numbering, grey-box test procedure, series & multi-page rule, D1 master checklist).
- **D2 (M2):** set 12 governing rules (§5.8) and canonical motion tokens; ruled the reduced-motion fade cap at 150 ms.
- **D3 (M3):** resolved 9 cross-file conflicts (C1–C9), 6 review issues, and 15 factual fixes (F-1–F-15), including the Firefox 144 View Transitions correction and the WCAG SC 1.4.1 vs 1.4.11 distinction; consolidated 33 gaps.
- **D4 (M4):** applied the ML7 fix log; preserved the GEO replication caveat with the Princeton figures wherever they appear; verified the FAQ removal timeline against Google's changelog.
- **D5 (M5):** resolved 8 cross-file conflicts (C1–C8: 404 for cross-tenant objects, NIST SP 800-63B-4 password rules, chunked-upload timeouts, one canonical API error envelope with RFC 9457 fields, HTTP 422 for validation failures, single home for client freshness numbers); verified NIST SP 800-63B-4's final publication date (31 July 2025) and the GPC enforcement fines (Sephora $1.2M, Healthline $1.55M, Disney $2.75M, Ford $375,703) by live search at merge time; carried 16 `[VERIFY]` flags (8 each in D5.4/D5.5) as explicit build-time checks rather than silently clearing them.
- **D6 (M6):** set 7 governing principles (design every width; mobile-first as discipline; accessibility as a gate; trust earned with real proof; never lose the user's work; stricter wins; honest labels) and single-statement width classes and touch-target hierarchies.
- **D7 (M7):** resolved all 20 ML10 conflicts plus 27 finalize decisions (§7.3).

The debate round (R0) then stress-tested the finalized files: M7 filed 21 contests (C-101–C-121) and M5 filed 8 items (X1–X8). The most consequential was C-101, the parameter-count correction (§4.1). Others resolved real arithmetic (X1: W061's LCP sub-budgets did not sum to the stated 2,000 ms target — 600+200+800+100 = 1,700 — and D4.12's 800/200/800/200 table won) and real boundaries (X4: the offline/PWA image-cache split — stable brand images cache-first, content images stale-while-revalidate).


---

## 7. The generational-novelty principle and memory-proofing design

### 7.1 Generational novelty

The programme's architecture adds a principle that goes beyond any single build: **every generation must produce a new level of UI/UX**. A build that matches the last generation's level fails; novelty compounds and never repeats. The principle exists because the skill's own success is a threat: if every agent using the skill produces the same "unique" design, the skill's output becomes the new default — and the next generation of detectors will flag it. The novelty log (W033's `palette-log.md`, recording the last three projects' seed hue zones) and W010's hard fails (same font family as any of the last 3 own builds, accent hue distance ≥30°) are the enforcement mechanisms. M1 owns the rule in D1; M7 is instructed to make it a top-level core directive in the assembled skill.

Generational novelty is also the answer to tell decay (§8.5): the skill cannot be a fixed list of bans, because the tells it bans will be replaced by new defaults within months. It must be a *generator* of divergence — a method for producing new themes, new motion systems, and new colour derivations on every project, with the novelty log as its memory.

### 7.2 Memory-proofing: designing a skill the agent will actually follow

The largest single risk to the skill is not that its rules are wrong but that the agent *forgets* them mid-build. D7's research (W087, W088) addresses this directly with an anti-forgetting design:

**Chunked, self-contained sections.** No H3 section exceeds 150 lines; no table exceeds 25 rows; no procedure exceeds 12 steps; no checklist exceeds 15 items. Each section opens with a **CORE ANCHORS block** — a short, fixed-format restatement of the section's critical rules — so that an agent reading any section in isolation encounters its governing rules first.

**Decision-point anchors.** Seven decision points in a build (brief, theme, type, colour, layout, motion, ship) each carry an anchor: the rules that matter *at that moment*, restated where the decision is made.

**Checklists over prose.** Rules are written as checkable checklist items (W088's four-field format: rule, check, evidence, fail condition) rather than as paragraphs, because checklist items are easier to recall and verify than prose.

**Progressive disclosure.** The skill is layered: a CORE layer (≤450 lines) that every agent reads, a WORKING layer for the task at hand, and a REFERENCE layer for detail. The agent is never asked to hold the whole file in working memory.

**Deliberate redundancy.** A capped set of CRITICAL rules (≤12) appears in exactly 4 placements each, within a 150-line restatement budget (W087) — or, in W088's competing system, a Canonical Ban Registry of 8 verbatim bans within a 15% repeat budget. The two systems disagree (see §7.3), and the major-lead debate must pick one.

**Instruction-writing craft.** W088's rules for writing rules: imperative voice; MUST/SHOULD/MAY discipline; one requirement per rule; checkability tests (§6.2, Rule 3); a 20-item rule audit (IW-9); and a banned-adjectives table of 40 words that cannot be checked.

### 7.3 The conflict — and its resolution at finalize

Minor-lead review ML10 found that D7's workers each wrote a coherent system, but the systems disagreed with each other — **20 cross-file conflicts** in D7 alone, including:

- **Anchor format:** W087 mandates a 5-line CORE ANCHORS block with section citations; W088 mandates a verbatim 4-line "ALWAYS ON" blockquote. Both cannot stand.
- **Checklist caps:** W087 says max 15 items; W088 says max 20; W096 says 5–9. A three-way conflict.
- **Checklist-item format:** W088's four-field format differs from W087's trailing-citation format and W096's six-field format — a four-way conflict including W097/W098.
- **Repetition systems:** W088's Ban Registry (8 bans, 15% budget) vs W087's CRITICAL 4 placements (150-line budget).
- **Example mandates:** W088 mandates GOOD/BAD examples for every abstract rule; W087 rations examples (max 2, only where ambiguous); W095 mandates counted minimums (≥90% coverage).
- **Size model:** W087's section budgets sum to 14,250 lines against its own 12,000-line hard cap — an arithmetic error the review caught.
- **Labels:** W090 renames `BLOCKED/UNAVAILABLE` to `BLOCKED`, contradicting W087, Part 14, and five other D7 files.

**All 20 conflicts were resolved at finalize** by M7 (finalized D7 file, §D7.17), together with 27 further finalize decisions:

| Conflict | Resolution |
|---|---|
| Size model (C1) | TOKENS in use, WORDS for authoring; hard cap **40,000 words (~53,000 tokens)**; W087's 12,000-line budget rejected (sums to 14,250) |
| Status label (C2) | Keep `BLOCKED/UNAVAILABLE`; W090's rename rejected |
| Version (C3) | Three-part SemVer, body line `Version: X.Y.Z — YYYY-MM-DD` |
| Keywords (C4) | Uppercase RFC 2119 (verified BCP 14, March 1997) |
| Anchor format (C5) | W087's 5-line CORE ANCHORS with § citations wins; W088's 4-line ALWAYS ON rejected (its wording discipline kept) |
| Checklist caps (C6) | Scoped: 5–9 for gate/pause-point runs; max 15 for in-skill mini-checklists; W088's max 20 rejected |
| Checklist formats (C7) | By construct: 6-field gate / `### Acceptance check` end-of-section / trailing-citation mini-checklist + `— Check:` clause |
| Metadata (C8) | Title 50–60 (max 70), description 120–135 (max 155) — **but reopened in debate as C-102**; M7's debate position is to adopt D4's 120–155/ceiling 160 instead |
| Examples (C11) | Required only where a rule is ambiguous without one; max 30 pairs file-wide, each ≤15 lines |
| Precedence (C15) | One hierarchy: safety > never-cut core > user message > project layer > skill body (non-core) > other sets > agent defaults |
| Gate IDs (C16) | One scheme `G-<DOMAIN>-<nn>` |
| Banned adjectives (D-12) | W088's 40 + "unique" + "exceptional" = 42 |

This paper reports both the conflict and its resolution, because the resolution is itself evidence: the review-and-finalize layer worked as designed. One gap remains genuinely open: **no empirical forgetting test exists** — no protocol in the research measures rule-recall on a real build. The anti-forgetting design is well-reasoned but untested, and the paper flags it as such. D7 also carried 13 gaps to the debate (§D7.18), including the QA content packs (a v1.0 blocker — the three packs do not exist yet), no automated gate enforcement (gates are manual in v1.0), and no distribution channel, maintainer role, feedback intake, or end-of-life policy.

### 7.4 Skill-file architecture

W087's architecture for the assembled skill: one monolithic portable file (not split across files, so it works in any agent), a **40,000-word hard cap (~53,000 tokens)** — replacing W087's 12,000-line budget, which M7 rejected at finalize because its own section budgets summed to 14,250 lines (D7 decision C1) — 13 numbered sections plus 4 appendices in canonical order, frontmatter carrying only name and description (per the Agent Skills standard), override-first ordering (the most important rules first, because agents weight early content), self-directed progressive disclosure, and a single numbering system for all cross-references (§N, XXX-NN, XX-NN, A-NN). Banned structures (22 items) include platform-specific references — the skill must work in any agent, not only in the one that wrote it.

The cap creates the project's sharpest assembly problem, recorded as debate contest C-110: the seven finalized files total **~350,000+ words** of input (D1 95,912 + D3 116,679 + D4 98,820 + D5 134,088 + D6 20,571 + D7 15,951, before D2) against a 40,000-word cap. M7's position is that assembly **cuts ~10:1** per W097 (one rule one home; cite don't paraphrase; numbers live once): every rule compressed to ≤40 words, every threshold once in the registry, every banned list once in Appendix A, every gate once in §12/§13, every worked example within the 30-pair budget. The finalized files are input to assembly, not text to preserve — and M7 flags explicitly that if assembly pastes instead of cutting, the deliverable is unusable.


---

## 8. Limitations & honest gaps

This section is the paper's most important one. The research programme's defining discipline was honest-gap reporting — every file carried a Gaps section, and reviewers added theirs. This section consolidates those gaps. Nothing here is a criticism of the researchers; it is the record of what the research itself says it does not know.

### 8.1 Coverage of this paper

- **Finalized domain files:** all 7 were available (D1–D7, 44,871 lines). One caveat: **D2's finalized file was still being written during the debate round** — M5 read it at 694 lines (§§0–2) growing to 1,149 (§§0–4) while reading, and M7 read it at 2,170 lines (§§0–6) with M2 still writing (debate contest C-113). By the time this paper was finalized, D2.md had grown to 3,201 lines, but the paper's D2 coverage rests on the §0 governing rules and the worker files; the D2-dependent debate items (W023 3D motion, W029 motion performance budgets, W024 reduced motion, W030 motion QA) were unresolved at debate time, and M5 recommended a short second debate round on them.
- **Minor-lead reviews:** all 10 were available (3,325 lines).
- **Debate:** round R0 only, and only two debate files existed (M5, M7). M7 filed 21 contests (C-101–C-121); M5 filed 8 items (X1–X8). The remaining majors' debate files (M1–M4, M6) and the **decisions log** had not yet been delivered. Debate positions reported here are M5's and M7's positions, not settled decisions — the decisions log will record the outcomes.
- **The final SKILL.md** had not been assembled; this paper synthesizes the research, not the finished skill. The assembly compression problem (C-110: ~350,000+ words of finalized input vs a 40,000-word cap) means the assembled skill will be a ~10:1 cut of the finalized material, not a concatenation of it.

### 8.2 Rate-limited verification (the 429 problem)

**72 files** in the evidence base mention HTTP 429 rate limits during web research. The impact was uneven but real:

- **Zero web verification:** W010 (distinctiveness standard), W025 (gesture & touch), W063 (font loading), W069 (API design & data fetching), W079 (checkout funnel), and W088 (instruction-writing craft) obtained no successful web fetches at all. Their files make no web-sourced claims — W069's numbers are labelled skill prescriptions, not sourced claims — which is honest, but their content rests on training knowledge and the pre-existing parts.
- **Partial verification:** W062's streaming research failed entirely (HLS/DASH guidance is a decision rule only, flagged `[VERIFY]`); W047's Google Search Central limits were partially 429-blocked; W064's ASVS 5.0 requirements rest on secondary summaries, not the primary standard; W001/W002/W003 consulted key documents via search-indexed excerpts only (including the avoid-ai-design catalog and the mimesis research document, whose per-tool signature material is recorded as a gap rather than summarized from an excerpt).
- **Review-layer verification:** minor leads checked web sources as cited (sample, date, URL, first-hand vs second-hand) but did not re-fetch them — no live browser was available to the review layer.
- **One figure was caught by review, not by verification:** ML8 flagged an "invented-looking figure" in W061 (performance budgets) and a loose attribution; the debate round then found the underlying error — W061's LCP sub-budget numbers did not match their stated derivation (600+200+800+100 = 1,700 ms, not the 2,000 ms target) — and D4.12's arithmetically correct table (800/200/800/200) was adopted as canonical (debate item X1).

The consequence: any figure in this paper that traces to a single worker file should be treated as the worker's best available evidence, not as independently re-verified fact. The paper flags single-source figures in place.

### 8.3 No live testing was performed

- **No detector was run against a test site.** All detector figures come from vendor documentation, published benchmarks, and third-party reviews. X013's honest gap: a follow-up researcher should run the same test page through slop-detect, madewithjev, Originality.ai, Pangram, and Hive and record the actual scores.
- **No live site audit** was performed for the colour, spacing, or layout findings. X010 notes that no fresh Playwright audit was run; X004 notes that no live site audit was performed.
- **No empirical forgetting test exists** for the memory-proofing design (§7.3). No protocol in the research measures rule-recall on a real build.

### 8.4 Figures that are single-source, secondhand, or unverified

The following figures appear in the research and are **flagged, not asserted**:

| Figure | Status |
|---|---|
| "Roughly 73% of AI-generated frontends use Inter" | Secondhand (sailop, via ReliantAI MASTER-GUIDE and medo.dev); original not reviewed |
| "55–95% of AI sites use an eyebrow badge" | Unverified; not quoted in the skill |
| ">50% of YC Spring 2025 startups used indigo" | Single-source; flagged do-not-quote by X004 |
| "94% of first impressions are design-related" | Traced to Sillence et al. on health websites; not verified from primary text; excluded from skill claims |
| Missouri S&T "2.6 s / 180 ms" figures | Secondary coverage; primary paper not verified |
| WebAIM "83.9%" figure | Unverified in this research |
| Spacing ratios 3:1 and 0.4×/0.6× | Single-source working numbers; labelled provisional at finalize |
| Aurora-gradient severity | Disputed between sources; unsettled |
| EyeSift "75–85% Manus triage accuracy" | Vendor claim; unverified |
| "Single runs vary by about ±5 points" (Lighthouse) | Uncited in W090; flagged for sourcing or softening |
| iOS 26 Home Screen claim (W084) | Single-sourced; flagged for verification |
| GEO vendor figures (Profound 4.2×, Wellows 0.664, BrightEdge 50%) | Vendor data; directional only |
| Em-dash density figures (Twain 10.13 vs GPT-4.1 10.62 per 1k words) | Approximate: the "~1 per 60–70 words" figure comes from a practitioner guide, not a measured corpus; the Twain/GPT-4.1 comparison comes from a preprint read only via a secondary summary (D1.7, source X005). Direction well-supported; exact rates not nailed down |
| arXiv:2601.17406 fingerprinting study (97.2% F1, 44.7%) | Read second-hand via the agent-sh guide, not from the paper itself (D1.7, source X006) |
| CHI '26 deceptive-design paper (55.8% of 1,296 LLM-generated ecommerce components) | Adjacent evidence only — measures deceptive design, not dead controls (D1.7, source X012) |
| NeurIPS hallucinated-citation figure (100+ citations across ~50 papers) | Single-vendor report (GPTZero, January 2026) as relayed by aiforresearch.app; reported case, not independently confirmed count (D1.7, source X011) |
| "500-launch review" | Second-hand: LaunchBuddy cites a 295-upvote r/VibeCodeDevs post; the original post was not read directly (D1.7, source X012) |
| Builder fingerprints (X006 §2) | Taken from cited inventories, not re-verified against live deployments |
| Model paste fingerprints (X006 §1) | From Jademond's 2025 analysis; chat interfaces change copy behaviour without notice — a marker's absence proves nothing |
| All detector accuracy figures | Version-bound: each study describes the tool versions tested at the time; several figures are less than two months old (Turnitin's October 2026 architecture update, Originality.ai 5.0, SlopTotal's September 2026 remeasurement). Re-verify before the skill's next major revision |

### 8.5 Tell lists decay

The research is explicit that **AI-tell content decays in months**. Anthropic rewrote its design instructions three times between November 2025 and September 2026. The typeface fingerprint moved Inter → Geist → Satoshi in roughly seven months. D1's own gap note states that "detector capabilities change monthly — several figures here are less than two months old." The re-verification cadence is contested: **D3's position is every 6 months** against current models; **W092's cadence table sets a 90-day AI-defaults audit**; M7's debate position (C-107) is to keep 90 days, arguing that a 6-month cadence lets the skill's detection content go stale through roughly six model generations. The contest was still open at writing time. Any reader using this paper after mid-2027 should treat the specific tells as stale and the *method* (derive, don't ban; aggregate, don't single-signal; test blind) as the durable content.

### 8.6 The whole-website evidence gap

The deepest evidential gap in the programme (X014 gaps G-1–G-3):

- **No peer-reviewed study blind-tests whole websites** for AI-vs-human detection with accuracy numbers. All lab accuracy figures in §5.13 are for text, image, audio, or video — not pages.
- **Detector scores are unvalidated against human judgment.** No independent study correlates a detector's 0–100 slop score with blind human verdicts on the same pages.
- **The only public website-pair tests publish no aggregate results** (Circuit Biscuit's website round, 6 pairs; Kagi Slop Detective).
- **Small-n practitioner evidence:** Löhrlein eye-tracking n = 10; Tastra blind tests judged by one person; the Goremy test was one company's team. These are tendencies and case evidence, not population estimates.

### 8.7 Conflicts: resolved at finalize, and still open

**Resolved at finalize:**

- **D7:** all 20 cross-file conflicts resolved by M7 plus 27 finalize decisions (§7.3).
- **D1:** 39 targeted edits at merge; W001 totals corrected; W012's 3° hue-shift loophole closed (raised to ≥15°); W011's L-03/L-28 contradiction rewritten; W014's rubric layered with W010's self-check and Part 02's 20-point check (rubric = gate, W010 = module, 20-point folded).
- **D2:** reduced-motion fade cap ruled at 150 ms; 600 ms entrance ceiling; 200 ms micro-interaction ceiling; 12 governing rules set.
- **D3:** 9 cross-file conflicts (C1–C9), 6 review issues, 15 factual fixes.
- **D4:** fix log applied; the meta-description conflict was settled by D7 decision C8 (title 50–60/max 70, description 120–135/max 155) — **but reopened in debate as C-102**, with M7's position to adopt D4's 120–155/ceiling 160 instead. Still open.
- **D5:** all 8 cross-file conflicts resolved (C1–C8); LCP sub-budget arithmetic corrected via debate item X1 (D4.12's 800/200/800/200 table canonical).
- **D6:** width classes and touch-target hierarchy stated once (D6 §0.2/§0.3); debate C-105 adopts D6's hierarchy plus D2's inline-link row.

**Still open at writing time (debate round R0, decisions log not yet written):**

- **C-101 — parameter count (178/221 vs 178/221).** M7's grep count is Tier 1 measured evidence and D7 already uses 178/17; the fix is one line in D1. Awaiting the decisions log to confirm.
- **C-102 — meta description range** (D7 C8 120–135/max 155 vs D4 120–155/ceiling 160). M7's position: adopt D4.
- **C-107 — re-verification cadence** (90 days vs 6 months). M7's position: 90 days.
- **C-109 — Part 23 truncation** (ends at §2.7; §3–§10, including the §10 testing matrix, do not exist). M7's position: strip the dangling references at assembly; writing the missing sections goes to the backlog for a future version.
- **C-110 — assembly compression** (~350,000+ words vs 40,000-word cap). M7's position: cut ~10:1.
- **C-119 / X2 — 3D asset weight** (D5.3's 500 KB before first interaction vs Part 08's 5 MB desktop / 2 MB mobile totals). M5's position: adopt W061's reconciliation (500 KB before first interaction; 5 MB/2 MB total session streaming, progressive and post-interaction only). D3 has no 3D weight position at all; D2's W023 was not yet finalized.
- **X3 — font deferred-total** (D3's 250 KB ceiling vs D5.5's rejection of the loophole). M5's position: 250 KB only for strictly post-interaction deferred subsets; first-load ceiling 150 KB hard.
- **X5 — error budgets/SLOs/runbooks (G-D5-6) and contract testing/CI wiring (G-D5-7).** Assigned to D7 by ML8, but D7 contains none of them — D7 is the skill-assembly domain, not operational engineering. M5 offers D5 addenda; M7 to decide the home or log them as known omissions.
- **D2-dependent items (X6/C-113):** W023 3D motion, W029 motion performance budgets, W024 reduced motion, W030 motion QA were not in D2.md at debate time. M5 recommends a second debate round after D2 completes.
- **Beauty is asserted, never operationalized** (D1 merge log, ML2's hardest gap). D1 offers only the V3 validation proxies; M7 must not let "not slop" substitute for "beautiful".
- **ML2's requested web re-research was NOT re-run at merge:** W014's three statistical claims, W013's jury scores and palette hexes, W012's [WEB] citations, W015's divergence-threshold validation. M7 may re-run in priority order.
- **Agent-process defaults** (file structure, class-naming, scaffolding) are unscored anywhere — needs an owner (D5 or D7).

### 8.8 Dimensions the research still misses

Consolidated from the workers' and reviewers' gap lists (D3's 33-item list is the fullest):

- **Non-Latin typography:** no line-height/measure/tracking rules for CJK, Arabic, or Devanagari; no variable-font guidance for non-Latin scripts; no per-script font-loading guidance beyond subsetting (W063).
- **Colour meaning across cultures:** white=mourning, red=prosperity, gradient hue associations, and image depiction norms vary by market; no localisation method exists.
- **RTL and vertical text:** grid mirroring, optical spacing, and asymmetric whitespace unexamined for RTL.
- **Print/PDF:** CMYK-safe palettes, print contrast, paged-media grids absent — needs a conscious scope decision.
- **Real-time and collaborative state:** WebSocket/SSE updates, presence, live cursors, conflict resolution (CRDT vs OT) not covered (W060).
- **Offline state and sync queues** (W060); **adaptive streaming detail** (W062, 429-blocked); **OAuth 2.1/OIDC client rules, WebAuthn detail, key management beyond rotation** (W064/W065); **per-interaction INP budgets** (W061).
- **Canvas/WebGL/video motion budgets, 120 Hz position, CI regression harness** (D2 gaps).
- **Brand-motion systems:** D2 owns motion mechanics; nobody owns motion as brand expression.
- **Data-dense tables** (sticky headers, row selection, bulk actions, pagination vs infinite scroll) — no dedicated owner.
- **Language coverage:** detection research is English-first; Hindi/Urdu detection is materially weaker and largely unstudied.
- **W010's 2002 history** rests only on Part 02's description (no web verification was possible).
- **QA content packs (D7.18):** the three content packs for testing the skill itself do not exist and are a v1.0 blocker — M7 writes them before the first QA run.
- **No automated gate enforcement** (D7.18): the gates are manual in v1.0; the owner acceptance checklist does not exist yet.
- **No distribution channel, maintainer role, feedback intake, or end-of-life policy** (D7.18, source W092): the skill ships without them in v1.0.
- **i18n / Part 27:** Part 27 (internationalisation) does not exist; G-SCH-11 covers hreflang only. Debate C-118 notes D6 §11 covers i18n as a skill topic, so the gap is a source gap, not a skill gap — but the source material is still missing.
- **Skill-file provenance/tampering and memory-store bound** (D7.18, source W094): open for a future version.
- **Error budgets / SLOs / incident runbooks and contract testing / CI wiring** (G-D5-6, G-D5-7): assigned to D7 by ML8 but not covered there; home undecided (debate X5).
- **No real AI-built codebase was cloned and audited** (X006): the code-pattern signals rest on cited guides, skills, and published findings plus directly checkable technical facts. A follow-up audit against 3–5 real exported builder projects is recommended before the final skill freezes its code thresholds.

### 8.9 The 17 unmeasured gap tells

Of X015's 43 gap tells, **17 are analyst-observed but unmeasured** — the researcher identified the tell by inspection but no prevalence or weight data exists. They are included in the 221-tell surface with their status flagged, not hidden.


---

## 9. References

Only sources cited in the research files are listed here. URLs are reproduced verbatim from the files; where a figure comes from a secondary summary rather than the primary paper, that is stated. No source, author, or figure has been invented for this paper.

### 9.1 Peer-reviewed papers and preprints

- Aggarwal et al. (2024). *GEO: Generative Engine Optimization.* KDD 2024. arXiv:2311.09735. (GEO-bench, 10,000 queries; quotation +43%, statistics +33%, fluency +29%, cite sources +28%, keyword stuffing −8%. Replication caveat: C-SEO Bench, NeurIPS 2025 — 3 of 54 cases significant, none original GEO methods; volume-controlled replication, September 2026 — no pooled effect.)
- Cooke, Edwards, Barkoff & Kelly (2024/2025). "As Good As A Coin Toss." arXiv:2403.16760. https://arxiv.org/abs/2403.16760v1
- Diel et al. (2024). Systematic review and meta-analysis, 56 papers, 86,155 participants. *Computers in Human Behavior Reports.* (Pooled 55.54%; figures via https://synthetic.watch/llms-full.txt and https://warningshots.ai/learn/can-you-spot-a-deepfake/)
- Frank et al. (2024). "A Representative Study on Human Detection of Artificially Generated Media Across Countries." arXiv:2312.05976. https://arxiv.org/html/2312.05976v1
- Gehrmann, Strobelt & Rush (2019). GLTR. (Detection 54% → 72% with colouring.)
- Högemann, Betke & Thomas (2025). *Frontiers in Artificial Intelligence.* https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1707336/full
- Kamali et al. (2025). (50,444 participants, 749,828 observations; as summarized in Högemann et al. 2025.)
- Kirchenbauer et al. (2023). "A Watermark for Large Language Models." ICML 2023. arXiv:2301.10226.
- Kirchenbauer et al. (2024). ICLR. (Paraphrased watermarked text still detectable at 800 tokens, 1e-5 FPR.)
- Kobak et al. (2024/2025). Excess vocabulary in academic publishing, 14M+ PubMed abstracts ("delve" 25.2×). *Science Advances* 11(27) (15.1M abstracts per X015). Via https://www.rewritica.com/blog/signs-of-ai-writing and https://github.com/doodledood/claude-code-plugins/blob/HEAD/claude-plugins/writing/skills/human-writing/references/ai-tells-and-fingerprints.md
- Krishna et al. (2023). Retrieval-based detection proposal.
- Liang et al. (2023). "GPT detectors are biased against non-native English writers." *Patterns.* (61.22% false-positive rate on 91 TOEFL essays across 7 detectors.)
- Lindgaard, Fernandes, Dudek & Brown (2006). "Attention web designers: You have 50 milliseconds to make a good first impression!" *Behaviour & Information Technology* 25(2):115–126. Via https://www.nature.com/news/2006/060109/full/news060109-13.html and https://pmc.ncbi.nlm.nih.gov/articles/PMC4863498/
- Mıhcı et al. (2026). (Perplexity ROC-AUC 0.969, burstiness 0.953; paraphrase destroys perplexity's power.)
- Miller et al. (2023). *Psychological Science.* (AI faces judged more human; worst detectors most confident. Via https://warningshots.ai/learn/can-you-spot-a-deepfake/)
- Mitchell et al. (2023). DetectGPT. (AUROC 0.81 → 0.95 on GPT-NeoX fake news.)
- Nightingale & Farid (2022). *PNAS.* (AI vs real faces, 48.2% → 59%; synthetic faces 7.7% more trustworthy. Figures via https://warningshots.ai/learn/can-you-spot-a-deepfake/ and https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1707336/full)
- Pangram Labs. Technical report. arXiv:2402.14873.
- Tuch et al. (2012). Visual complexity and prototypicality in first impressions (50 ms, 17 ms). https://storage.googleapis.com/gweb-research2023-media/pubtools/pdf/38315.pdf
- Van Vlasselaer et al. (2026). *International Journal of Educational Integrity.* (Turnitin scored all 40 fully-AI papers 0–20%; Pangram 97.5% inclusive accuracy.)
- Weber-Wulff et al. (2023). *International Journal of Educational Integrity.* (14 tools "neither accurate nor reliable".)
- Zhang et al. (2024). ICML. (Strong watermarking impossible under plausible assumptions.)
- "Is it Cake or is it AI?" (2026). Systematic review, 30 studies. https://arxiv.org/pdf/2604.03437
- Fast-DetectGPT (ICLR 2024); Binoculars (ICML 2024); Ghostbuster (zero-shot methods, as cited in X013).

### 9.2 Benchmarks and evaluations

- RAID benchmark (2024). ACL. arXiv:2405.07940 (also cited as arXiv:2409.14285 in X013). 12 detectors, 6M+ generations.
- C-SEO Bench (NeurIPS 2025). GEO replication: 3 of 54 cases significant.
- SlopBench (SlopTotal). 23-engine ensemble, AUC 0.942.
- Epoch AI (July 2026). Pangram/GPTZero flagged 0/495 human passages; Originality 19 (3.8%); style imitation missed 10.1–17.8%.
- Scribbr 12-tool benchmark. (Copyleaks claims 99.12%, measured 66%; GPTZero claims 99%, measured 52%.)
- Notre Dame (October 2026). Humanizer study: <4% stayed flagged after humanizing; lightly edited text flagged 38–80%.
- Krebs, A. (20 April 2026). "Scoring Show HN submissions for AI design patterns." https://adriankrebs.ch/blog/design-slop (1,590 Show HN landing pages; 22% heavy slop, 32% mild, 46% clean.)
- Ahrefs schema test (August 2025–March 2026). 1,885 pages: AI Mode +2.4%, ChatGPT +2.2%, AI Overviews −4.6%.
- Emblematic (2026). 390 homepages; Inter 21.5%.
- Unslop Me leaderboard (17 October 2026). 30 AI-builder sites; average score 46.
- LandingBoost calibration set. 558 homepages; 84% held-out accuracy, 79% on unseen builder Bolt.
- Codequiry. 1,200 Python CS1 submissions. https://dashboard.codequiry.com/blog/what-1200-python-cs1-submissions-reveal-about-ai-written-code-signatures

### 9.3 Detector tools and website scanners

- GPTZero. https://en.wikipedia.org/wiki/GPTZero
- Originality.ai. https://originality.ai/blog/how-does-ai-content-detection-work
- Turnitin AI writing detection. https://guides.turnitin.com/hc/en-us/articles/28477544839821-Turnitin-s-AI-writing-detection-capabilities-FAQs
- Pangram. (Peer-reviewed; RAID 99.3%.)
- Copyleaks; ZeroGPT; Sapling AI Detector. https://saplingaidetector.com/
- madewithjev AI slop detector (34 tells). https://madewithjev.com/free-tools/ai-slop-detector
- slop-detect (71 deterministic rules). https://www.slop-detect.com/docs
- Briskly AI slop detector (11 rules). https://briskly.tools/tools/ai-slop-detector
- Unslop Me (13-point checklist). https://unslop-me.vercel.app/guides/ai-website-design-tells-checklist
- LandingBoost AI check. https://landingboost.app/ai-check
- aiwebsitedetector.net. https://aiwebsitedetector.net/
- SlopTotal (23-engine ensemble). https://github.com/pablocaeg/sloptotal/blob/HEAD/README.md
- ai-design-tells (PyPI; 27-tell taxonomy, validated on 202 real sites). https://pypi.org/project/ai-design-tells/
- Hive; Illuminarty (image detectors). https://www.layer3labs.io/comparisons/ai-image-detectors-compared
- EyeSift Manus screening. https://www.eyesift.com/detect/manus-website-content/ (Vendor claim of 75–85% triage accuracy, unverified.)
- EQBench Slop Score. https://eqbench.com/slop-score.html

### 9.4 Practitioner sources, guides, and case evidence

- sailop. "Why Every AI-Generated Website Looks the Same." (Secondhand via ReliantAI MASTER-GUIDE and medo.dev; original not reviewed. Source of the attributed ~73% Inter figure.)
- sailop. "Detect an AI-Generated Website in 30 Seconds: 21 Objective Signs (2026 Method)." https://sailop.com/blog/detect-ai-generated-site-30-seconds-21-signs-2026
- falia.co. "How to spot an AI-built website: the tells of Claude Code and ChatGPT Codex." https://falia.co/en/insights/web-design/spot-ai-built-website/
- twindesigns.tech. "Why Your Website Looks AI-Generated." https://www.twindesigns.tech/website-looks-ai-generated
- Developers Digest. "AI design slop and how to spot it." https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it
- Tastra (November 2026). Blind-test case study: render→look→fix won 13/13. (Single judge — the author.)
- Goremy. Employee AI-detection test. https://goremy.ai/blog/articles/can-employees-tell-if-content-is-ai-generated-we-tested-it
- Löhrlein (2026). Eye-tracking study, personalized landing pages, n = 10. https://www.jahn-loehrlein.de/en/projects/eye-tracking-study/
- Poynter Institute, *Eyetrack III*. (Headlines first on web. Via https://www.emphasis.co.uk/blog/where-people-look-online/)
- blog.lynxflow.co (2026). Survey of 16 competitions and ~80 winning sites. (Cited in W013.)
- ReliantAI MASTER-GUIDE; medo.dev. (Secondhand citations of sailop.)
- OpenAdaptAI. "Writing That Doesn't Sound Like an LLM." https://github.com/openadaptai/openadapt-herald/blob/HEAD/herald/prompts/writing_guide.md
- ananas-agency. "AI Pattern Catalog." https://github.com/ananas-agency/ai-pattern-detector/blob/HEAD/skills/ai-pattern-detector/references/patterns.md
- evalyze-ai. "Anti-AI Tells: The Field Guide." https://github.com/evalyze-ai/founder-fundraising-outreach/blob/HEAD/references/anti-ai-tells.md
- ssamba1. "AI writing tells — the avoidance catalog." https://github.com/ssamba1/untell/blob/HEAD/untell/references/ai-tells.md
- McKelvey, J. "How to Tell If Code Was Written by AI: 9 Tells (2026)." https://justinmckelvey.com/blog/how-to-tell-if-code-was-written-by-ai

### 9.5 Standards, law, and vendor documentation

- EU AI Act, Article 50(2). Machine-readable marking obligation from 2 August 2026.
- FTC Rule on Consumer Reviews and Testimonials, 16 CFR Part 465. In force October 2024; explicitly covers AI-generated fake reviews.
- C2PA provenance manifests. ISO/IEC 22144:2025.
- Google DeepMind (2024). SynthID-Text. *Nature.* (Tournament sampling; in Gemini since 2024; 100B+ pieces of content.)
- Anthropic. Claude watermarking from 2 August 2026. (Design instructions rewritten 3× November 2025–September 2026.)
- WCAG 2.3.3 (AAA — animation from interactions). Level corrected in W024 (not AA).
- WCAG SC 1.4.1 (use of colour — sets no numeric ratio) and SC 1.4.11 (non-text contrast, 3:1 floor). Distinction corrected at finalize (D3, F-4).
- MDN. Firefox 144 release notes (View Transitions, shipped 14 October 2025; Baseline newly available 16 October 2025). Cited in D3 finalized file, F-1.
- Google Search Central. FAQ rich results: restricted August 2023; removed for all sites 7 May 2026; docs removed 15 June 2026. (Corroborated at finalize against Google's changelog, D4 Appendix B, B-04.)
- Bing Webmaster Guidelines §14. Structured data "may support clearer grounding but does not guarantee visibility or grounding traffic."
- SparkToro/Similarweb (June 2026). 68.01% zero-click rate. (Clickstream sample; vendor data, directional only.)
- Profound; Wellows; BrightEdge. GEO vendor figures (4.2× passage claim; 0.664 Spearman; 50% <13 weeks). Vendor data, directional only.

### 9.6 Internal research files (the evidence base)

The paper's primary evidence is the Web Craft Pro Max research corpus itself, held in `~/workspace/your_files/web-craft-pro-max/`:

- `ARCHITECTURE.md` — team architecture v2.0 (132 agents, 7 domains, 100 worker topics).
- `parts/00-parameter-catalog.md` — the 178-parameter catalog, 17 families (the file's family list says 178/17; M7's grep count corrected it to 178/17 — debate contest C-101).
- `parts/01-diagnosis-and-cures.md` — diagnosis (three forces) and cure rules CV-01–25, CC-01–10, CM-01–14, CD-01–18.
- `research/detect/X001–X015` — detection research (15 files, 10,718 lines).
- `research/D1–D7/W001–W100` — worker research (100 files, 85,355 lines).
- `reviews/minor/ML1–ML10` — minor-lead reviews (10 of 10, 3,325 lines).
- `finalized/D1.md`–`D7.md` — major-lead finalized domain files (7 of 7, 44,871 lines).
- `debate/M5.md`, `debate/M7.md` — major-lead debate files, round R0 (2 files, 738 lines; 21 contests C-101–C-121 from M7, 8 items X1–X8 from M5).

---

*End of paper. Coverage statement: this synthesis covers 100 worker files, 15 detection files, 25 parts, 10 minor-lead reviews, 7 finalized domain files, and 2 debate files, totalling 155,782 lines. The remaining debate files (M1–M4, M6) and the decisions log had not yet been delivered when the paper was written, and D2's finalized file was still being written during the debate round; a revised edition should incorporate them and re-check any figure whose status changes at finalize or debate time.*
