---
title: Pantone & Named Lookup — Find the nearest colour in named colour systems
description: Enter a colour and find its nearest matches in HTML/CSS named colours, a Pantone Solid Coated subset, RAL Classic, NCS and Crayola, ranked by ΔE2000 with a plain-language closeness label.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Pantone & Named Lookup

Pantone & Named Lookup finds the closest matches for a colour in five named colour systems at once. It shows the single closest match across all systems, the top matches in each system, and a small list of values to copy. Each match carries its ΔE2000 distance and a label that says in plain words how close it is.

Designers use named systems to talk to printers, paint suppliers and manufacturers. This tool helps you find a starting reference, for example "which Pantone is nearest to our brand blue?", before you check a physical swatch book.

Pantone & Named Lookup is in the launcher's **Explore** group.

## Open it

Open the launcher and select **Pantone & Named Lookup**. See [Open the Colour Tools](launcher-and-panels.md). It starts with the colour you opened with, or #0F4C81 (a classic blue).

## The systems

| System | Entries | Example name |
| --- | --- | --- |
| **HTML/CSS** | 141 | aliceblue |
| **Pantone Solid C** | 105 | PANTONE Yellow C |
| **RAL Classic** | 148 | RAL 1000 Green beige |
| **NCS** | 56 | NCS S 0500-N |
| **Crayola** | 111 | Crayola Red |

The HTML/CSS list holds the named colours of CSS. The Pantone, RAL, NCS and Crayola lists are curated subsets, not complete systems, with widely published approximate screen (sRGB) renderings of each colour.

## Screen tour

1. **Source color** (*ΔE2000 nearest-match*): a colour field and a **Filter** list (**All systems** or one system).
2. **Closest overall**, labelled with the winning system: your colour and the best match side by side, a pill such as *ΔE 1.84 · Very close*, and your colour's OKLCH, HSL and CMYK values.
3. One section per system (*N chips · top 5*):
   - the top match as a wide button with its swatch, name, HEX code, ΔE and closeness label;
   - the next matches as smaller cells with name, ΔE and label.
4. **Quick copy** (*Click to copy*): **HEX**, **RGB**, **CMYK (naive)** and **Nearest overall**.

## Closeness labels

| ΔE2000 | Label |
| --- | --- |
| Below 1 | **Imperceptible** |
| 1 to 2 | **Very close** |
| 2 to 5 | **Close** |
| 5 to 10 | **Noticeable** |
| 10 to 20 | **Distinct** |
| 20 and above | **Far** |

**ΔE2000** is the CIE's standard measure of how different two colours look. Under about 1, most people cannot see a difference side by side.

## Tasks

### Find the nearest Pantone to a brand colour

1. Enter your brand colour in the colour field.
2. Set **Filter** to **Pantone Solid C**. The section now lists the top 18 Pantone matches instead of 5.
3. Read the top match's name and closeness label.
4. Select any match to make it the source colour; **Selected** and the name appear.

Result: a Pantone reference to look up in a physical guide.

### Compare all systems at a glance

1. Leave **Filter** on **All systems**.
2. Read **Closest overall** and then the top five in each system.

Result: the nearest CSS name, Pantone, RAL, NCS and Crayola colour for the same input.

### Copy a value

Select a row under **Quick copy**. **CMYK (naive)** is a simple formula conversion; **Nearest overall** copies the match's name followed by its HEX code in brackets.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Colour field | The colour to match | HEX, colour well, dice | #0F4C81, or the colour you opened with |
| **Filter** | Shows all systems or one | All systems, HTML/CSS, Pantone Solid C, RAL Classic, NCS, Crayola | All systems |
| Match (top or cell) | Makes that match the source colour | — | — |
| **Quick copy** rows | Copy a value | 4 rows | — |

With **All systems**, each system shows its top 5 matches; with one system selected, it shows the top 18.

## Accuracy and limits

- The Pantone, RAL and NCS entries are approximate sRGB renderings of printed or painted colours. Real swatches vary with paper, ink, finish and lighting, and a screen cannot show some of them accurately at all.
- The lists are subsets. A closer official colour may exist that this tool does not know about.
- Matching uses ΔE2000 from sRGB under a D65 white point. It predicts side-by-side differences under good viewing, not how a colour will print.
- Always confirm with the official physical guide before specifying a colour for production.

## Related

- [Colour Tools documentation](README.md)
- [Color Name Finder](colour-name-finder.md) for general colour names
- [CMYK Soft-Proof](cmyk-soft-proof.md) for a print preview
- [Color Order Systems: Munsell, NCS, Pantone, and RAL](https://auricartisan.com/library/learn/articles/2026-06-09-color-order-systems-munsell-ncs-pantone-ral) on Learn
- [Basic Color Tools](../../README.md)
