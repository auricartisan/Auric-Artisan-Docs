---
title: Personalization Generator — Palettes, gradients, typography, UI pairs and posters
description: What each result tab of the Personalization Generator shows, how the cards are scored, and what every card button copies or saves.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Palettes, gradients, typography, UI pairs and posters

Five tabs hold the results of the last sweep. Palettes come straight from the sweep; the other four are built from the kept palettes, in rank order.

| Tab | Built from | Most cards |
| --- | --- | --- |
| **Palettes** | the sweep | up to 96 |
| **Gradients** | the top 28 palettes | 28 |
| **Typography** | the top 24 palettes | 24 |
| **UI Pairs** | the top 28 palettes | 28 |
| **Posters** | the top 28 palettes | 28 |

Every card has **Save**, which saves it to your Library, and **Add to pool**, which puts its colours at the front of your pool. See [Export, save and share](export-and-save.md).

## Palettes

The heading summarises the set, for example **24 kept · best 81 (Balanced Analogous) · avg 74 · most common Analogous**, with **Top**, **Average**, **Kept** and **Sweeps** figures.

Each card shows:

- the palette name, such as **Balanced Analogous**: a mood word (**Vivid**, **Deep**, **Soft** or **Balanced**, from the average saturation and lightness) and the colour relationship;
- a line such as **Analogous · from Soft Product**. The first part is the colour relationship the palette was built on (19 relationships, from **Analogous** to **Brand trio**; see the [Reference](reference.md)). The second is the built-in reference palette it drew on;
- the score, from 0 to 100 (highlighted from 60 and again from 80);
- the swatches with their HEX values. Select a swatch to copy its HEX;
- tags: the number of stops, the relationship and **BG/FG** with the best contrast ratio in the palette;
- four scores: **Preference**, **Harmony**, **Contrast** and **CVD / UI**;
- three contrast bars, **AAA text**, **AA UI** and **Large text**.

The three contrast bars all use the same number, the highest WCAG ratio between any two colours in the palette, measured against 7:1, 4.5:1 and 3:1 respectively. They tell you whether the palette has a pair that clears each bar, not how every pair performs.

Buttons: **Copy hex** (the HEX values separated by spaces), **Add to pool**, **Open in Studio** and **Save**.

### How a palette is scored

The total blends six parts. The card shows four of them.

| Part | What it measures |
| --- | --- |
| Preference | How close each colour is to the nearest pool colour (CIEDE2000), with a small reward for not copying the pool exactly. |
| Harmony | How well the hues fit the palette's relationship, and how evenly lightness and chroma are spread. |
| Style | How well the colours fall inside the ranges of your style chips. Not shown on the card. |
| Diversity | How clearly the colours differ from one another. Weighted by the **Diversity** slider. Not shown on the card. |
| Contrast | The best contrast pair and the overall light-to-dark range. Weighted by the **Accessibility** slider. |
| CVD / UI | How distinct the colours stay under three colour-vision simulations, plus whether a pair reaches 4.5:1 (or 3:1 with **Contrast** off). Weighted by the **Accessibility** slider. |

The score ranks palettes against your settings. It is not a measure of quality in general. See [Limits and accuracy](../others/limits-and-accuracy.md).

## Gradients

Each kept palette in the top 28 becomes one gradient, in one of twelve styles taken in turn: **linear**, **radial**, **conic**, **mesh**, **layered**, **sharp**, **soft-mesh**, **diagonal**, **spot**, **duotone**, **prism** and **halo**. Stops are the palette's colours sorted by hue, six at most.

Filter chips above the grid (**All · 28**, **linear · 3** and so on) show one style at a time. Each card has a large preview with the style and score, the stops, the CSS, and:

- **Copy CSS**: a line such as `background: linear-gradient(…);`
- **Copy stops**: the stop colours separated by spaces
- **Add to pool** and **Save**

A gradient's score is its palette's score.

## Typography

Each card pairs one palette with a type system: a display face, a body face and an accent face. The preview shows **H1**, **H2**, **Body** and **Mono** lines on the palette's most readable background and text pair, with the palette's most colourful colour as the accent, and lists the three faces. The header line gives the palette name and the **BG/FG** ratio.

The type systems offered are the ones whose tags best match your use case and style chips; when several match equally, the cards rotate through them. There are 17 systems in all, such as **Product Grotesk**, **Editorial Serif**, **Luxury Contrast** and **Console Stack**.

The fonts are named as CSS font stacks and are not downloaded by the page. If a named font is not installed on your device, the preview uses the next font in the stack. Check the faces on your own system before relying on the preview.

Buttons: **Copy CSS** copies five custom properties, `--font-display`, `--font-body`, `--color-bg`, `--color-text` and `--color-accent`; **Add to pool** adds the background, text and accent; **Save**.

## UI Pairs

Each card is a small interface in the palette's colours: a title bar, **Background**, **Text**, **Surface** and **Accent** with their HEX values, a search field and three buttons (**Primary action**, **Surface button**, **Ghost button**), and a contrast meter.

- The meter and the first tag grade the text on the background: **AAA** (7:1 or more), **AA** (4.5:1), **Large** (3:1) or **Fail**.
- The header line gives **WCAG** ratio, **APCA Lc** and **CVD**, the palette's colour-vision score out of 100.
- The APCA tag also names the use the value supports, from **Body text** (Lc 75 or more) down to **Insufficient**.

The heading counts how many pairs pass WCAG AA, AAA and APCA 60 or more.

Buttons: **Copy CSS** copies `--ui-bg`, `--ui-text`, `--ui-surface`, `--ui-accent` and `--ui-accent-ink`; **Add to pool** adds the four colours; **Save**.

## Posters

Each card is a poster in one of twelve layouts, taken in turn: **bauhaus**, **type-dominant**, **asymmetric**, **magazine**, **minimal-centered**, **brutalist**, **festival**, **swiss**, **collage**, **kinetic**, **archive** and **gradient-poster**. Each uses the palette's background, text and two accent colours, and a type system.

Filter chips show one layout at a time. The text on the posters is fixed sample copy.

Buttons: **Copy CSS** copies a short `.poster` rule with background, colour and font, plus `.poster-accent` and `.poster-accent-2` colours; **Add to pool** adds the text and accent colours; **Save**. There is no image download for posters. **Save** stores the poster's colours, layout and fonts in your Library, with a swatch strip of its colours as the preview, not a picture of the poster.

## Related

- [Design tokens](design-tokens.md)
- [Brand Studio](brand-studio.md)
- [Export, save and share](export-and-save.md)
