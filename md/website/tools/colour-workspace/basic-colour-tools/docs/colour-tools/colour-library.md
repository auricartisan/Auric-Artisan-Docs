---
title: Color Library — Browse more than a thousand named colours
description: Search and filter 1,058 named colours by family, open any colour's detail view with sixteen formats, a triadic harmony and similar colours, and download a swatch as SVG or PNG.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Library

Color Library is a browsable catalogue of 1,058 named colours, such as *Crimson*, *Dusty Rose* or *Gunmetal*, grouped into 13 families. You can search by name or HEX code, filter by family, page through the results, and open any colour for a detail view with every common format, its temperature, contrast against white and black, a triadic harmony and the twelve most similar named colours.

This in-panel library is different from the site's large colour collections (palettes, shades, gradients and the colour atlas) in the library area; for those, see [Colour libraries](../../../../../library/colour-libraries/README.md).

Color Library is in the launcher's **Explore** group.

## Open it

Open the launcher and select **Color Library**, or pick it from the right-click menu's **Colour tools** group. See [Open the Colour Tools](launcher-and-panels.md). If you open it with a colour (for example from another tool), it starts on that colour's detail view; otherwise it starts on the list.

## Screen tour

### Toolbar

- A search box (*Search by name or hex…*).
- A **Category** list: **All** and the 13 families.
- A count of matching colours, for example **146 colors**.

### List view

- A grid of up to 60 colour cells per page, each with a swatch, name and HEX code.
- A pager: **‹ Prev**, **Page N of M** (the page number is a box you can type in) and **Next ›**.

### Detail view

- **← Back to library**, **Copy HEX**, **Download SVG** and **Download PNG**.
- A large chip with the name and HEX code.
- A grid with **Hue category**, **HSL**, **OKLCh**, **Temperature** (an estimated colour temperature in kelvin and a label such as *Warm* or *Neutral cool*), **vs White** and **vs Black** (WCAG contrast ratios).
- **Formats** (*Click to copy*): sixteen rows.
- **Harmony — triadic**: three colours 120° apart in OKLCH hue.
- **Similar colors** (*by ΔE2000*): the twelve closest named colours with their ΔE.

## Families

| Family | Colours |
| --- | --- |
| Red | 119 |
| Pink | 83 |
| Orange | 82 |
| Yellow | 86 |
| Green | 136 |
| Blue | 146 |
| Purple | 98 |
| Brown | 92 |
| Gray | 79 |
| White | 47 |
| Black | 31 |
| Metallic | 33 |
| Neon | 26 |

## Tasks

### Find a named colour

1. Type part of a name (for example `sage`) or a HEX code (for example `#8a`) in the search box. The grid filters as you type and the page resets to 1.
2. Optionally choose a family in **Category**.
3. Use **Next ›**, **‹ Prev** or the page box to move through the results.

Result: the named colours that match, 60 per page.

### Read a colour in full

1. Select a colour cell. The detail view opens.
2. Select any row under **Formats** to copy it. The rows are **HEX**, **HEX (short)**, **RGB**, **RGBA**, **RGB %**, **HSL**, **HSLA**, **HSV**, **CMYK**, **CIE XYZ (D65)**, **CIELAB (D65)**, **CIELCh (D65)**, **OKLab**, **OKLCh**, **Linear sRGB** and **CSS keyword** (the lower-case HEX code).
3. Select a harmony or similar colour to open its detail view.
4. Select **← Back to library** to return to the list.

Result: the colour's values on your clipboard, and related colours to explore.

### Download a swatch

In the detail view, select **Download SVG** or **Download PNG**. You get a 512 by 512 pixel square of the colour, named after the colour (for example `Dusty_Rose.svg`).

### Send a colour to another tool

1. In the list, right-click a colour cell to get the site's colour menu (copy options, **Check its contrast**, **Build harmonies**, **Find its name**, **Inspect in Colour Tools**).
2. Hold `Shift` while you right-click for the Color Library's own menu: **Copy HEX**, **Download SVG**, **Download PNG**, **Open in Spaces**, **Find name**, **Open Accessibility** and **Open Psychology**.

Result: the colour opens as the starting colour of the tool you chose.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Search box | Filters by name or HEX text | Free text | Empty |
| **Category** | Filters by family | All and 13 families | All |
| Colour cell | Opens the detail view | — | — |
| **‹ Prev** / **Next ›** / page box | Moves between pages | 60 colours per page | Page 1 |
| **← Back to library** | Returns to the list | — | — |
| **Copy HEX** | Copies the HEX code | — | — |
| **Download SVG** / **Download PNG** | Downloads a 512 × 512 swatch | — | — |
| Format row | Copies that format | 16 rows | — |
| `Shift` + right-click a list cell | Opens the tool's colour menu | 7 actions | — |

## Accuracy and limits

- The names are descriptive and come from a general list. Different sources use different names for the same colour.
- **Temperature** is estimated from the colour's chromaticity with a standard approximation for light sources. For strongly coloured or very dark colours the figure is rough, and some colours show *Indeterminate*.
- The search matches names and HEX text exactly as typed (not colour similarity). To find names by similarity, use [Color Name Finder](colour-name-finder.md).
- The library is not a licensed colour system. For Pantone, RAL, NCS and similar matches, use [Pantone & Named Lookup](pantone-and-named-lookup.md).

## Related

- [Colour Tools documentation](README.md)
- [Color Name Finder](colour-name-finder.md)
- [Pantone & Named Lookup](pantone-and-named-lookup.md)
- [Color Psychology](colour-psychology.md)
- [Basic Color Tools](../../README.md)
