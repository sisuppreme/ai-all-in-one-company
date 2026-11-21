# Example 2 — The outage draft that was never written by AI

> Hypothetical product: "ClinicDesk," a live appointment-and-letters tool
> for small clinics. An "AI draft" button is being added to the existing
> referral-letter editor, which reception staff already use daily.

## Before

```text
Editor → [AI draft] button behaviour:
  - Click → full-screen spinner ("Writing your letter…").
  - Provider timeout after 30 s → spinner resolves to one of four stock
    paragraphs chosen by letter type, with a green toast: "Draft ready ✓"
  - The stock text is inserted into the letter body, indistinguishable
    from a model draft written from this patient's notes.
  - If the user had already typed half the letter, generating a draft
    replaces the editor contents.
```

During a provider outage, staff send referral letters containing generic
stock wording they believe was drafted from the patient's case notes.
Nobody can tell afterwards which letters were AI-drafted, which were
stock, and which were typed by hand — and two staff members lose typed
work to the replace-on-generate behaviour.

## After

Fallback is designed per failure mode before the button ships
(AI-206), and every failure leaves the non-AI path fully usable
(AI-202):

| Failure | What the user sees | What the user can do |
|---|---|---|
| Provider down / timeout | Panel: "AI drafting is unavailable right now. Your text is unchanged." | Keep typing in the normal editor; retry later |
| Model refuses (e.g. notes contain content it won't draft from) | Panel: "AI couldn't draft from these notes — no draft was used." | Write manually, exactly as before the retrofit |
| Output fails schema validation (missing salutation, wrong patient name field) | Draft is discarded, never inserted; panel: "That draft didn't pass checks and was not used." | Request a new draft or write manually |
| Clinic's monthly AI budget exhausted (AI-210 ceiling reached) | Panel: "AI drafting is paused until the next budget period." | Write manually; no degraded fake draft is offered |
| Empty / low-quality output | Draft shown only as a proposal with "Not useful? Discard" one click away | Discard and write manually; nothing is auto-inserted |

Behaviour rules that make the table real:

- The AI panel loads **asynchronously** beside the editor; it never
  blocks opening, editing, or saving the letter (AI-206 latency rule).
- A draft is a **proposal, not a mutation** (AI-204): it sits in the
  panel, marked AI-generated with model ID and timestamp, and enters
  the letter only when the staff member clicks "Insert draft" — through
  the editor's normal insert path, never by replacing existing text.
  Text the user already typed is never touched by generation, failure,
  or retry.
- There is **no stock-paragraph path at all**. If the model did not
  write it, the UI never presents it as a draft; the only fallback is
  the honest unavailable state plus the manual editor.
- Users are told in the surface, at first use, that the panel is
  AI-assisted and that drafts must be checked against the patient's
  notes before sending (AI-205).

The failure drill is run in staging before shipment (G-AI-103): the
provider is forced to time out, refuse, return schema-invalid output,
and hit the budget ceiling in turn, and a tester completes a referral
letter manually under each failure with no work lost.

## Note

Violates AI-206 (BAN-AI-102, fake fallback presented as AI or as
success). Corrected by designing an honest fallback state for each
failure mode, keeping the user's existing text and the manual editor
intact in every case (AI-202), treating drafts as provenance-marked
proposals (AI-204), and proving the behaviour with the G-AI-103
failure drill.
