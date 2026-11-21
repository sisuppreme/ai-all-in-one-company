# Example 3 — The promo bar that pushed the page under the reader's finger

## Before

A marketing promo bar is injected by a third-party script once it loads, with no space reserved for it:

```html
<script src="https://promo.example.com/bar.js" async></script>
<!-- bar.js document.write-style injects a 56px bar above <main> on load -->
```

On real visits the bar arrives one to two seconds after first paint and shoves the article — and the button the reader is about to tap — down by its full height. Field CLS p75 on the article template is 0.31, deep in the poor band, and support gets "the page jumped and I tapped the wrong thing" reports.

## After

The slot is part of the layout from the first paint, with its space reserved whether or not the campaign is active:

```html
<div class="promo-slot" style="min-height: 56px" aria-live="off">
  <!-- promo content, when a campaign is active, renders inside this slot;
       an inactive campaign leaves the reserved slot collapsed by the
       server-rendered page, never by late client-side injection -->
</div>
```

The script may fill the slot but can never change its height after render, and the field report over the following window confirms article-template CLS p75 back under 0.1 before the defect closes.

Note: the Before violates AN-228 (CLS fixes are structural: reserve space before load and never inject above rendered content); the After corrects it.
