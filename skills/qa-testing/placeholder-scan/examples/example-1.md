# Example 1 — Lorem ipsum and placeholder contacts in the shipped footer

## Before

The static sweep (G-QA-141) runs over the production build and reports:

```
dist/pricing.html:84:  <p>Lorem ipsum dolor sit amet, consectetur
                       adipiscing elit.</p>
dist/index.html:212:   <a href="mailto:support@example.com">
                       support@example.com</a>
dist/index.html:214:   <span>(555) 014-2200</span>
```

The pricing page shipped with filler under two plan tiers, and the footer
carries a template contact block that was never edited. The support address
is unmonitored — it is not a real mailbox at all.

## After

1. The lorem ipsum paragraphs are replaced with the plan descriptions taken
   from the project's fact sheet; where no approved copy exists, the section
   is removed rather than filled.
2. The footer lists the real support address and phone number. A test
   message is sent to the address and the reply is confirmed before release.
3. The sweep is re-run on the rebuilt artifact:

```
$ rg -i -n "lorem|ipsum|dolor sit amet|example\.com|example@|555-01" dist/
(no matches — exit 0)
```

Note: corrects QA-284 — the static fingerprint set (lorem ipsum variants, placeholder contacts) is swept over the shipped artifact, and a hit blocks the release until the real content replaces it.
