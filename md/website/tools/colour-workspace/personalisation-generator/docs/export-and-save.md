---
title: Personalization Generator — Export, save and share
description: Copy CSS, download the JSON snapshot, save results to your Library, bring Library colours in, and automate the generator through the Public API.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Export, save and share

Results live only in the open page; a reload starts a fresh sweep. Copy, download or save anything you want to keep.

## The Export tab

The **Export** tab has two buttons at the top and two cards.

| Control | What it does |
| --- | --- |
| **Copy CSS** (top) | Copies the CSS shown in the **CSS tokens** card. |
| **Download JSON** | Downloads the full snapshot as `auric-personalization-generator.json`. |
| **Copy** (CSS tokens card) | The same as **Copy CSS**. |
| **Copy JSON** (JSON snapshot card) | Copies the full snapshot as text. |

The **JSON snapshot** card previews only the start of a long snapshot and marks it *(truncated, full file in download)*. The copy and the download are always complete.

### What the CSS contains

A `:root` block with:

- `--aa-personal-1`, `--aa-personal-2` and so on: the leader's colours, in order (if there are no results yet, the first six pool colours);
- `--aa-personal-gradient`: the first gradient;
- `--aa-font-display`, `--aa-font-body` and `--aa-font-mono`: the first typography card's three font stacks;

followed by the design tokens for the light, dark and high-contrast themes, as described in [Design tokens](design-tokens.md).

### What the JSON contains

- `preferences`: your pool, styles, use case, brief, and the search settings (palette size, depth, keep, the three weights and the three filters);
- `results`: every palette (with its relationship, source and score breakdown), gradient, typography card, UI pair and poster, and the full token system;
- the time it was made.

There is no way to load a JSON snapshot back into the generator. Keep it as a record, or use it in your own code.

## Copy single results

Every result card has its own copy buttons. See [Palettes, gradients, typography, UI pairs and posters](result-tabs.md) for exactly what each one copies. In short:

| Where | Button | Copies |
| --- | --- | --- |
| Palette card | **Copy hex** | HEX values separated by spaces |
| Overview | **Copy hex list** | the leader's HEX values |
| Any swatch or role chip | select it | that HEX |
| Gradient card | **Copy CSS**, **Copy stops** | a `background:` line, or the stop colours |
| Typography card | **Copy CSS** | five custom properties |
| UI pair card | **Copy CSS** | five custom properties |
| Poster card | **Copy CSS** | a short `.poster` rule |
| Tokens tab | **Copy CSS**, **Copy JSON**, scale **Copy** | the token system, or one scale |

A short message confirms each copy.

## Save to your Library

**Save** on a palette, gradient, typography, UI pair or poster card, and **Save brand system** in the Studio, store the item in your Auric Artisan Library with a preview image.

- The message reads, for example, **Saved “Balanced Analogous” to Library**.
- Saving the same card twice from the same sweep shows **Already saved** instead of making a copy.
- If the Library is not available, the message reads **Save failed**.

| Saved from | Saved as | Holds |
| --- | --- | --- |
| Palette card | palette | colours, relationship, source and score |
| Gradient card | gradient | CSS, stops, style and score |
| Typography card | typography | fonts, colours and score |
| UI pair card | preset | the four colours, accent text colour, contrast and colour-vision score |
| Poster card | preset | layout, colours, fonts and score |
| Studio | preset | palette, brand system, overrides, theme and density |

The Library's own **Save to Library** captures the leader palette (or, before any sweep, your pool) and the first gradient. See the [Library Kit](../../../../kits/library-kit/README.md) for managing saved items.

## Bring colours in from your Library

A palette, gradient, colour or shade saved in any Auric Artisan tool can be opened in the Personalization Generator from your Library. Its colours are added to the front of your pool and the **Pool** tab opens, ready for a sweep. See the [Library Kit](../../../../kits/library-kit/README.md).

## Automate it

The page notes the matching Public API call: **POST /v1/personalize/system**, at 14 API credits per call. API credits are a separate balance from your tool tokens. See the [Public API](../../../../../services/public-api/README.md) and the API reference at https://auricartisan.com/library/documentation/api/.

## Related

- [Design tokens](design-tokens.md)
- [Brand Studio](brand-studio.md)
- [Privacy](../others/privacy.md)
