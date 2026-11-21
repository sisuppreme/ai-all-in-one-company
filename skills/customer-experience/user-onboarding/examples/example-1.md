# Example 1 — Binding a checklist item to its real event

## Before

The setup checklist item "Create your first report" is wired to the tour:
clicking "Next" on the slide that describes reports marks the item complete
and advances the progress bar to 60%.

Users finish onboarding with a full checklist and no report. Support tickets
ask where the reports they "created" went, and the activation dashboard
shows a healthy completion rate for an event that never happened.

## After

The item is rebound to the product event named in the tracking plan:

1. The checklist definition names the event: `report_created`.
2. Clicking through the tour slide now only dismisses the slide; the item
   stays open.
3. The item ticks at the moment the user's first real report is saved and
   the `report_created` event fires — verified by the fresh-account
   walkthrough asserting the analytics event and the tick arrive together.

Progress is slower to fill and means something: a ticked item is a user who
actually received the value.

Note: corrects CX-064 — a checklist item completes only when its real product event fires, never on a page view or a "Next" click.
