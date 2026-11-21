# Example 3 — An invented logo cloud removed and replaced with real proof

## Before

```html
<section class="trusted-by">
  <p>Trusted by teams at</p>
  <div class="logo-row">
    <span class="logo">NorthPeak</span>
    <span class="logo">VANTA&nbsp;LABS</span>
    <span class="logo">Corelink</span>
    <span class="logo">Datastream</span>
    <span class="logo">Helios</span>
    <span class="logo">Quantia</span>
  </div>
</section>
```

Six wordmarks in a default font. None of the six companies is a customer;
two do not exist at all. The component was built once and reused on every
page, so the fabrication is systematic, not incidental (DET-VIS-034).

## After

The component is changed so it can only render what it is given:

```html
<!-- trusted-by renders only entries from the customers data file.
     Each entry requires: the real logo file, the customer's name, and
     a permission note with a date. No entries -> the section does not
     render at all. -->
<section class="trusted-by" data-customers="3">
  <p>Trusted by dispatch teams at</p>
  <div class="logo-row">
    <img src="/logos/harbor-freight-lines.svg" alt="Harbor Freight Lines" width="132" height="28">
    <img src="/logos/citylink-couriers.svg" alt="CityLink Couriers" width="118" height="28">
    <img src="/logos/northgate-foods.svg" alt="Northgate Foods" width="126" height="28">
  </div>
</section>
```

Three real customers instead of six invented ones, drawn correctly,
optically sized, each with permission recorded. When the list is empty,
the section disappears rather than filling itself.

Note: corrects FE-022 via BAN-FE-012 — system components render only real, permitted proof; invented marks never ship.
