---
title: Color Science Lab — Gamut audit
description: Check a palette against sRGB, Display P3, Adobe RGB and Rec. 2020, see how much headroom its tightest colour has, and what clipping would cost.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Gamut audit

The **Gamut audit** view checks a palette against four RGB working spaces. A **gamut** is the range of colours a space can hold. A palette written in HEX is sRGB by definition, so it always fits sRGB; the useful number is **headroom** (margin): how far the palette's tightest colour is from the edge of each space. At 0 % a colour already sits on a primary, and any adjustment clips it.

## Layout

### Palette under audit

The palette (*N colours · target sRGB*): each colour with its HEX code and a line saying its sRGB margin (for example *12% margin*) or, for a colour from a wider space, *clips ΔE N*. Each has a **×** to remove it. Below: a colour well and **Add to palette**.

The starting palette has eight colours: #4F7FE0, #D3AF37, #00C264, #C4562C, #2F6D3A, #00E07A, #8F3B22 and #2B6F8F. A palette holds from 1 to 16 colours.

### Coverage by working space

A table with one row per space (**sRGB**, **Display P3**, **Adobe RGB**, **Rec. 2020**):

- **Tightest headroom**: a bar for the smallest margin in the palette.
- **In gamut**: how many colours fit, for example **8 / 8**.
- **Margin**: the tightest margin as a percentage. Red if any colour falls outside, amber if the margin is under 2 %, green otherwise.

### The verdict and the cost of clipping

- A large figure such as **8/8** with *Every colour survives sRGB unchanged.*, or how many clip and whether they fit Display P3 instead.
- **What clipping costs** (*ΔE00 after clip*): for each colour that clips, its clipped HEX code and the ΔE 2000 lost. With nothing clipping, it names the colour closest to the edge and its margin.

## Tasks

### Find the palette colour most at risk in conversion

1. Replace the palette with yours: remove the starting colours with **×** and add yours with the colour well and **Add to palette**.
2. Read the **Margin** column. The space with the lowest margin, and the colour named under **What clipping costs**, is where trouble will start.

Result: you know which colour to watch when converting or adjusting the palette.

## Controls

| Control | Values | Default |
| --- | --- | --- |
| **×** on a colour | Removes it | At least 1 colour remains |
| Colour well + **Add to palette** | Adds a colour | Up to 16 colours |

## Related

- [The Workbench](workbench.md) for one colour's gamut
- [Colorimetry and rendering tools](../../../colorimetry-and-rendering/README.md) for gamut mapping
