---
title: Gradient Library — Browse 512 curated gradients
description: Browse and filter 512 curated linear gradients by colour scheme and number of stops, open any gradient's details, and copy it as CSS, a CSS variable, a Tailwind class, SVG or JSON, or download it as SVG or PNG.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Gradient Library

Gradient Library is a collection of 512 ready-made linear gradients. Each has a name, an angle, two to four colour stops and a colour scheme it was built from. You can filter by scheme and number of stops, search by name, and open any gradient to see its stops in detail and copy it in five code formats or download it as an image.

When you want to build your own gradient instead, use [Gradient Maker](../panel-tools/gradient-maker.md) in the Basic Color Tools workspace. For the site's full gradient collection, see [Colour libraries](../../../../../library/colour-libraries/README.md).

Gradient Library is in the launcher's **Design** group.

## Open it

Open the launcher and select **Gradient Library**, or pick it from the right-click menu's **Colour tools** group. See [Open the Colour Tools](launcher-and-panels.md). It shows **Loading gradients…** while it downloads the collection from the site the first time you open it.

## Screen tour

### Toolbar

- A search box (*Search gradients…*).
- A **Scheme** list.
- A **Stops** list: **Any stops**, **2 stops**, **3 stops** or **4 stops**.
- A count of matching gradients, for example **72 gradients**.

### List view

A grid of up to 24 gradient cards per page. Each shows the gradient, its name, and its number of stops and scheme. A pager with **‹ Prev**, **Page N of M** and **Next ›** sits underneath.

### Detail view

- **← Back to library**, **Download SVG** and **Download PNG**.
- A large preview, and **Name**, **Scheme**, **Angle** and **Stops**.
- **Stops**: one card per stop with its HEX code, OKLCH lightness, chroma and hue, and its position.
- **Export**: five rows, each with the code and a **Copy** button.

## The collection

| Scheme | Gradients |
| --- | --- |
| Analogous | 76 |
| Complement | 76 |
| Triadic | 72 |
| Tetradic | 72 |
| WarmCool | 72 |
| Sunset | 72 |
| Mono | 72 |

By number of stops: 128 gradients have two stops, 128 have three and 256 have four. Names follow the pattern *Duo Analogous #001*.

## Tasks

### Find a gradient

1. Choose a **Scheme**, for example **Sunset**.
2. Choose a number of **Stops**.
3. Optionally type part of a name in the search box.
4. Page through the results.

Result: a grid of matching gradients, 24 at a time.

### Copy a gradient into your project

1. Select a gradient card to open its detail view.
2. Under **Export**, select **Copy** beside the format you need:

| Row | Example |
| --- | --- |
| **CSS** | `linear-gradient(15deg, #9A0076 0.0%, #FFBBCF 100.0%)` |
| **CSS variable** | `--gradient: linear-gradient(15deg, …);` |
| **Tailwind arbitrary** | `bg-[image:linear-gradient(15deg,_#9A0076_0.0%,_#FFBBCF_100.0%)]` |
| **SVG** | An SVG with a left-to-right linear gradient |
| **JSON** | The gradient's full record: angle, stops (position, HEX and OKLCH), name and scheme |

**Copied** appears after each copy.

Result: the gradient in the format your code expects.

### Download an image

In the detail view, select **Download SVG** or **Download PNG**. You get a 1280 by 320 pixel image named after the gradient (for example `Duo_Analogous__001.png`), drawn at the gradient's angle.

The SVG code under **Export** always runs left to right; the downloaded SVG follows the gradient's angle.

### Work with a single stop colour

1. In the detail view, right-click a stop card for the site's colour menu (copy options, **Check its contrast**, **Build harmonies**, **Find its name**, **Inspect in Colour Tools**).
2. Hold `Shift` while you right-click for the Gradient Library's own menu: **Copy HEX**, **Open in Spaces** and **Find name**.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Search box | Filters by name | Free text | Empty |
| **Scheme** | Filters by scheme | All, Analogous, Complement, Triadic, Tetradic, WarmCool, Sunset, Mono | All |
| **Stops** | Filters by number of stops | Any, 2, 3, 4 | Any |
| Gradient card | Opens the detail view | — | — |
| Pager | Moves between pages | 24 per page | Page 1 |
| **← Back to library** | Returns to the list | — | — |
| **Copy** (Export rows) | Copies that format | 5 formats | — |
| **Download SVG** / **Download PNG** | Downloads a 1280 × 320 image | — | — |
| `Shift` + right-click a stop | Opens the tool's colour menu | 3 actions | — |

## Accuracy and limits

- All gradients are linear and blend in sRGB, as CSS does by default.
- The collection needs a network connection the first time it loads in a session. If it cannot load, the panel shows a message that the gradient data could not be loaded.
- Gradients were generated from colour-scheme rules; they are starting points, not checked for text contrast. Check any text you place on a gradient with [Contrast System](contrast-system.md) or [Animation Contrast](animation-contrast.md).

## Related

- [Colour Tools documentation](README.md)
- [Gradient Maker](../panel-tools/gradient-maker.md)
- [Color Gradients and Interpolation](https://auricartisan.com/library/learn/articles/2026-06-07-color-gradients-and-interpolation) on Learn
- [Basic Color Tools](../../README.md)
