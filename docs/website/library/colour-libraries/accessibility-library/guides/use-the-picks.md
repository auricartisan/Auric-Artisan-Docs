---
title: Accessibility Library — Use the picks
description: Take up to twelve passing foreground colours for your ground, preview them, and copy them as CSS custom properties.
product: Website › Library › Colour libraries › Accessibility Library
updated: 2026-09-25
---

# Use the picks

The section headed **N that work on this ground** (for example **12 that work on this ground**) is the page's concrete answer: foreground colours that clear your target on your ground.

## How the picks are chosen

- One pick per 30° of hue, starting at 15°, so up to twelve picks cover the whole colour wheel.
- Each is placed a little inside its hue's line — 10% of lightness into the passing region — so you have room to adjust it later without it dropping out.
- Every pick clears the target. If a hue cannot reach the target on this ground, or a pick would land just under it, that hue is left out, so you may see fewer than twelve.

The text under the heading repeats the target and ground, for example "everything here clears **4.5:1** on **#1D2A3E**".

## Steps

1. Choose your ground and target in the control bar (see [Read the contrast map](read-the-contrast-map.md)).
2. Scroll to the picks. Each card shows **Readable** and a sample sentence in the pick on your ground, with its ratio and hex code. Hover a card to see its ratio and hue.
3. Select a card to move the map's caret onto that colour and read its full figures.
4. Select **Copy as CSS** to copy the whole set. The button reads **Copied** (or **Copy failed** if your browser blocked the clipboard).

**Result:** CSS like this on your clipboard:

```css
/* Auric Artisan — foregrounds that clear 4.5:1 on #1D2A3E
   sampled across the passing region, one per 30° of hue */
:root {
  --ground: #1D2A3E;
  --fg-01: #…;  /* 7.12:1 · hue 15° */
  --fg-02: #…;  /* 6.98:1 · hue 45° */
}
```

Each `--fg-NN` line carries its ratio and hue as a comment. The exact colours depend on your ground and target.

> **Tip:** Rename the properties after pasting, for example `--text-accent-red`, and keep the comment so reviewers can see the ratio each was chosen for.
