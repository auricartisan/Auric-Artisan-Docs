---
title: Color Name Finder — Find the nearest named colour
description: Enter a colour and find the closest of more than a thousand named colours, with seventeen similar colours and ten copyable formats.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Name Finder

Color Name Finder answers "what is this colour called?". You give it one colour and it finds the nearest match in a built-in list of 1,058 named colours, shows seventeen more close matches, and lists the colour in ten copyable formats. It is the quickest tool in the workbench: one input, three result sections.

The names come from a general-purpose colour-name list grouped into 13 families: red, pink, orange, yellow, green, blue, purple, brown, gray, white, black, metallic and neon. For matches against formal systems such as Pantone, RAL or NCS, use [Pantone & Named Lookup](pantone-and-named-lookup.md).

Color Name Finder is in the launcher's **Essentials** group.

## Open it

Open the launcher and select **Color Name Finder**, pick it from the right-click menu's **Colour tools** group, or right-click a colour value and select **Find its name**. See [Open the Colour Tools](launcher-and-panels.md). It starts with the colour you opened it with, or gold (#D3AF37).

## Screen tour

1. **Source**: the colour field (a colour well, a HEX box and a dice button for a random colour).
2. **Nearest match** (with the note **ΔE2000**):
   - two large chips side by side: your colour with its HEX code and hue family, and the nearest named colour with its name, HEX code, **ΔE** distance and name family;
   - a small grid with **HSL**, **OKLCh**, **RGB** and **Hue family**.
3. **Similar colors**: a grid of the next seventeen closest named colours, each with a swatch, its name, HEX code and ΔE.
4. **Full color spaces** (with the note **Click to copy**): ten rows you can select to copy.

## Tasks

### Name a colour

1. Type a HEX code in the Source box, or use the colour well.
2. Read the second chip under **Nearest match**. Its label is the colour's nearest name.
3. Check the **ΔE** figure under it. Below about 2 the name is a close match; above about 5 it is only the nearest of the names available.

Result: a name you can use in conversation, a style guide or a token name.

### Walk to a nearby named colour

1. Under **Similar colors**, select any cell.
2. The Source changes to that named colour and every section updates.

Result: you can step through related names until you find the one you want.

### Copy a format

Select a row under **Full color spaces**. The value is copied and a short **Copied** message appears. The rows are:

| Row | Example for #D3AF37 |
| --- | --- |
| **HEX** | `#D3AF37` |
| **HEX (short)** | `#D3AF37` (a three-digit form when one exists, such as `#FA0` for #FFAA00) |
| **RGB** | `rgb(211, 175, 55)` |
| **RGBA** | `rgba(211, 175, 55, 1)` |
| **RGB %** | `rgb(82.7% 68.6% 21.6%)` |
| **HSL** | `hsl(46.2, 63.9%, 52.2%)` |
| **HSLA** | `hsla(46.2, 63.9%, 52.2%, 1)` |
| **HSV** | `hsv(46.2, 73.9%, 82.7%)` |
| **CMYK** | `cmyk(0%, 17.1%, 73.9%, 17.3%)` |
| **CIE XYZ (D65)** | `xyz(0.4289, 0.4479, 0.1)` |

## How matching works

The tool converts your colour and every named colour to CIELAB and measures the difference with **ΔE2000**, the CIE's standard formula for how different two colours look. The list is sorted by that difference: the smallest is the nearest match, the next seventeen are the similar colours.

The **Hue family** is a plain-language label worked out from the colour's HSL values: Black, White or Gray for very dark, very light or unsaturated colours, otherwise Red, Orange, Yellow, Lime, Green, Teal, Cyan, Blue, Purple, Magenta or Pink by hue.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Colour well | Sets the source colour with your browser's picker | Any sRGB colour | #D3AF37, or the colour you opened with |
| HEX box | Sets the source colour as you type | 3, 4, 6 or 8 hex digits, with or without `#` | Same |
| Dice (**Random color**) | Picks a random colour | — | — |
| Similar colour cell | Makes that named colour the source | 17 cells | — |
| Format row | Copies that value | 10 rows | — |

## Outputs and exports

- Copy any of the ten formats from **Full color spaces**.
- The tool has no file export. For code snippets and scales, open the colour in the [Color Inspector](colour-inspector.md).

## Accuracy and limits

- The name list is a general one. Names are descriptive, not standards; two lists can call the same colour different things.
- ΔE2000 is computed from sRGB values with a D65 white point. It predicts differences seen side by side under good viewing conditions.
- The nearest match is only as near as the list allows. Check the ΔE before relying on a name.
- A colour's transparency is ignored.

## Related

- [Colour Tools documentation](README.md)
- [Pantone & Named Lookup](pantone-and-named-lookup.md) for Pantone, RAL, NCS, Crayola and CSS names
- [Color Library](colour-library.md) to browse the same named colours by family
- [Color Inspector](colour-inspector.md)
- [Basic Color Tools](../../README.md)
