---
title: Gamut Lab — Compare colour spaces
description: Compare RGB spaces by triangle, slice, CIELAB volume, u′v′ overlap and share of the spectral locus.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Compare colour spaces

The Gamut Lab gives four ways to compare spaces. Each answers a different question.

| Measure | Question it answers | Where |
| --- | --- | --- |
| Triangle area and share of the locus | How much of the range of visible chromaticities does the space cover? | Lab panel, Compare tab |
| Constant-lightness slice | At a given lightness, which hues can each space make vivid? | Lab › Gamut slice |
| CIELAB volume | How many distinguishable colours, including lightness, does the space hold? | Lab › Volume comparison, Compare tab |
| Overlap in u′v′ | How much of one space's triangle lies inside another's? | Lab › Volume comparison |

## Compare two spaces in the Lab

1. On the **Lab** tab, find **Volume comparison**.
2. In the first list, choose the reference: **sRGB** (default), **Display P3**, **Rec. 2020** or **ACEScg**.
3. In the second list, choose **Active space** (the working space selected at the top) or one of the same four spaces.
4. Select **Compute volume**. The panel shows "Computing…" and then:
   - each space's CIELAB volume in Lab³, with a ± spread against a run at half the samples and the half-width of the sampling box;
   - **Overlap in u′v′** — the share of space A inside B ("of A") and of B inside A ("of B");
   - **Jaccard** — the area both share divided by the area either covers.

These figures use 10,000 quasi-random (Halton) samples for volume and 5,000 for overlap.

## Slice at constant lightness

1. Under **Gamut slice**, choose **Constant L\* (CIELAB)**.
2. Move **Level** from 0 to 100 (default 50). The slice canvas outlines up to five drawn spaces at that lightness.
3. Choose **Constant L (OKLab)** to see the slice in OKLab, which keeps hue lines straighter and makes boundaries easier to read. In the current version the OKLab slice is always drawn at L = 0.5; the Level slider changes its label but not the slice.

## Measure every space at once

1. Open the **Compare** tab.
2. Under **Measure in**, choose **u′v′ share** (default) or **xy share (legacy)** for the share column. The xy figure is kept because other tools quote it; it overstates green.
3. Set **Samples** (**n**) from 5,000 to 200,000 (default 40k).
4. Select **Measure them all**. The button reads "Measuring…" while it works.
5. Read the table, sorted from smallest to largest volume:

| Column | Meaning |
| --- | --- |
| Space | Name and colour swatch |
| White | D65, D50, ACES, DCI, C, or the coordinates for others |
| Lab volume ± spread | CIELAB volume, and how much it changed against a half-size run |
| vs sRGB | Volume as a multiple of sRGB's |
| u′v′ share or xy share | The triangle's area as a percentage of the spectral locus in that plane; "> 100%" when the primaries lie outside the locus |

The note above the table records the sample count and that each space is measured against its own white.

## Why "> 100%" appears

ACES AP0 and ProPhoto RGB use imaginary primaries outside the spectral locus. Part of their triangle is colour no light can make, so their share cannot be read as coverage. The lab prints "> 100%" instead of a misleading percentage.

## Why the figures differ from published percentages

The locus area here is computed from the CIE 1931 2° observer data the lab holds, from 380 to 715 nm, in the plane named. Shares quoted elsewhere are often against a slightly different locus area. For example, the lab measures Rec. 2020 at 63.4% of the xy locus rather than the 75.8% often quoted.

## Result

You can say how two or more spaces differ in chromaticity coverage, in vivid hues at a given lightness, and in total CIELAB volume.
