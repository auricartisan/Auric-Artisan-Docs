---
title: Design System Generator — Share, save and connect
description: Share a link that rebuilds a system, save systems to your Library and restore them, and send the palette, fonts and icons to other Auric Artisan tools.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Share, save and connect

The generator is deterministic: the same inputs always produce the same system. That makes a system easy to share and keep, because only its inputs need to travel.

## Share a link

1. Select **Share** in the masthead.
2. The link is copied, **Shareable link copied ✓** appears, and the address bar updates to the same link.

The link lists your inputs as address parameters. Settings left on **Auto** are left out. For example:

```text
https://auricartisan.com/tool/design-engine/?industry=wellness&rampSpan=default&rampPeak=default&tokenPrefix=&tokenCase=kebab&style=elegant&a11y=AA&mode=both&density=spacious
```

When someone opens the link, the page applies these parameters before generating, so they see the same system. You can also write a link by hand with only the parameters you need, for example `?industry=wellness&style=elegant&a11y=AA`.

| Parameter | Values |
| --- | --- |
| `industry` | `fintech`, `healthcare`, `saas`, `ecommerce`, `education`, `creative`, `gaming`, `luxury`, `food`, `travel`, `realestate`, `nonprofit`, `crypto`, `wellness` |
| `style` | `modern`, `minimal`, `classic`, `bold`, `playful`, `elegant`, `corporate`, `brutalist`, `organic`, `futuristic` |
| `a11y` | `AA-large`, `AA`, `AAA` |
| `mode` | `light`, `dark`, `both` |
| `density` | `compact`, `comfortable`, `spacious` |
| `harmony` | `complementary`, `analogous`, `triadic`, `split`, `tetradic`, `monochrome` |
| `ratio` | `1.125`, `1.2`, `1.25`, `1.333`, `1.414`, `1.5`, `1.618` |
| `corner` | `sharp`, `soft`, `rounded`, `pill` |
| `seedHex` | A HEX colour, for example `%231f6feb` or `1f6feb` |

The link also lists the ramp shape and token naming (`rampSpan`, `rampPeak`, `tokenPrefix`, `tokenCase`), but opening a link does not apply them: those settings open at their defaults (**Even**, **Natural**, no prefix, **kebab**). Tell the recipient if you changed them.

## Your last settings

The page remembers the inputs you used last in this browser and restores them on your next visit, unless you arrive through a shared link. Like shared links, this restores the industry, style, target, colour mode, density, harmony, type ratio, corner style and seed, but not the ramp shape or token naming. The **Expand** choice is also remembered.

## Save to your Library

Two buttons save the current system to your Auric Artisan Library:

- **Save** in the masthead (message: **Saved to workspace ⭐**);
- the site's floating save button, labelled **Save design system** on this page, which opens the Library's save window so you can name the item and file it.

A saved system stores its name (industry and style), a colour strip, a summary with the target, fonts and score, and its full set of inputs. If the Library is not available on the page, a message says so instead.

## The Workspace view

Select **Workspace** in the masthead. **← Back to the system** returns you to your tab. The view has two parts.

### Saved systems

Each saved system shows its colour strip, name and summary, with three buttons:

- **Restore** applies the saved inputs, regenerates and returns to **Overview** (**Restored from workspace ✓**). As with shared links, the ramp shape and token naming are not re-applied.
- **Open** shows the item in your Library.
- **Delete** removes it (**Removed from workspace**).

With nothing saved it shows **No saved systems yet**. If the Library did not load, it shows **Workspace unavailable** with an **Open workspace** button.

### Connect

Four cards send the system to other tools:

- **Send the brand color into a tool**: **Harmony Studio**, **Gradient Library**, **Accessibility Lab**, **Contrast System**, **Color Spaces** and **Color Psychology**. Each opens that Colour Tool as a floating panel on this page, seeded with your primary colour. See the [Colour Tools](../../basic-colour-tools/docs/colour-tools/README.md).
- **Open a full generator with this palette**: a strip of the twelve-colour palette, and links to nine tools that receive your seed and palette in the address: **Palette Generator**, **Harmony Generator**, **Gradient Generator**, **Shade Generator**, **Accessibility Generator**, **Personalization Gen**, **Color Science Lab**, **Vision Simulation** and **URL Analyzer**.
- **Libraries & workspace**: **Font Library** (opens the Font Library searching for your heading family), **Icon Library** (opens the Icon Library on your recommended set), **Save to Workspace** and **Open Workspace** (opens your Library).
- **Copy palette for anywhere** (folded): **Copy palette (HEX)** (comma-separated), **Copy as JSON array** and **Copy as URL slug** (codes without `#`, joined by hyphens).

> **Note:** At the time of writing, the Palette, Harmony, Gradient, Shade and Accessibility Generator links lead to pages that are not available on the site. Their collections are in the library area instead; see [Colour libraries](../../../../library/colour-libraries/README.md).

The twelve-colour palette is: primary, secondary 500, accent 500, neutral 700, the four semantic solids, primary 200, primary 700, secondary 300 and accent 700.

## Related

- [Export tokens](export-tokens.md)
- [Library Kit](../../../../kits/library-kit/README.md)
- [Font Library](../../font-library/README.md) and [Icon Library](../../icon-library/README.md)
- [Privacy](../others/privacy.md)
