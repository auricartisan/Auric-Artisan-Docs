---
title: CMYK Soft-Proof — Preview how a colour or image may print
description: Simulate a screen colour or an image on five press and paper conditions, see the CMYK separation after dot gain and ink limits, spot colours that will shift, and copy CMYK values.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# CMYK Soft-Proof

Screens mix light; printing presses lay down ink on paper. Many bright screen colours cannot be printed, paper is never pure white, printed black is never pure black, and ink spreads as it soaks in. CMYK Soft-Proof gives you a quick feel for these effects. It takes a colour, or an image you drop in, and shows how it may look on one of five print conditions, the CMYK ink amounts involved, and which parts of an image will change most.

**Soft-proofing** means previewing on screen how something will print. **CMYK** is the four-ink process (cyan, magenta, yellow and black). **Dot gain** is the darkening of mid-tones as ink spreads on paper. **TAC** (total area coverage) is the maximum combined ink a press allows, in percent (C + M + Y + K, up to 400 %).

This tool is an intuition builder, not a colour-managed proof. It does not use ICC profiles.

CMYK Soft-Proof is in the launcher's **Design** group.

## Open it

Open the launcher and select **CMYK Soft-Proof**. See [Open the Colour Tools](launcher-and-panels.md). It starts with the colour you opened with, or a process blue (#0085CA).

## Screen tour

1. **Source** (*Soft-proof preview*): a colour field, the **Press condition** list, and a note describing the condition (its TAC limit, paper colour, black point and typical use).
2. **Side-by-side preview** (*Screen vs. simulated press*): **Screen (sRGB)** and **Press simulation** chips with their HEX codes, a ΔE pill with a label, and a TAC pill such as *TAC 173% / 330%* (the ink used against the limit). When the ink limit is exceeded, a note says how much cyan, magenta and yellow were reduced.
3. **CMYK separation** (*After dot gain & TAC*): bars for **Cyan**, **Magenta**, **Yellow** and **Black** with percentages, and three copy buttons: **CSS cmyk()**, **Channel values** and **Simulated hex**.
4. **Image soft-proof**: a drop area (*Drop an image here, or paste from clipboard*) with **Choose file**. Once an image is loaded, three versions side by side and **Clear**.

## Press conditions

| Condition | TAC limit | Paper | Black point | Note shown |
| --- | --- | --- | --- | --- |
| **ISO Coated v2 (FOGRA39)** | 330 % | #F4F2E8 | #1B1814 | European coated commercial offset. The most common print spec. |
| **SWOP (US Web Coated)** | 300 % | #F1EFE3 | #1F1B16 | US web offset on coated stock. |
| **ISO Uncoated (FOGRA52)** | 320 % | #EFEBD8 | #252118 | Premium uncoated stock; higher dot gain, warmer paper. |
| **ISO Newsprint 26v5** | 240 % | #EAE3CE | #2B2719 | Heavy dot gain, low TAC. |
| **Fine art / cotton rag** | 360 % | #F8F3DF | #1C1610 | Inkjet on cotton rag; closer to a monitor's range than offset. |

Each condition also has its own dot-gain amount: lowest for fine art, highest for newsprint.

## How the simulation works

1. The screen colour is split into CMYK with a simple formula.
2. Dot gain darkens the mid-tones of each ink.
3. If the total ink exceeds the TAC limit, cyan, magenta and yellow are reduced evenly and black is kept, which preserves contrast.
4. The inks are recombined over the condition's paper colour, with its practical black point, to give the simulated screen colour.
5. The difference between the original and the simulation is measured with ΔE2000.

| ΔE2000 | Label |
| --- | --- |
| Below 2 | **Match** |
| 2 to 5 | **Close** |
| 5 to 10 | **Shift** |
| 10 and above | **Lost** |

## Tasks

### Check a brand colour for print

1. Enter the colour.
2. Choose the **Press condition** your printer uses (ask them; FOGRA39 is common in Europe, SWOP in the US).
3. Compare **Screen (sRGB)** and **Press simulation**, and read the ΔE label.
4. Check the TAC pill. Red means the colour needed more ink than the press allows.

Result: a warning if the colour will shift noticeably or is too ink-heavy, before you send files.

### Copy CMYK values

Under **CMYK separation**:

- **CSS cmyk()** copies the separation as a CSS function. For the starting blue (#0085CA) on FOGRA39 it reads `cmyk(100%, 45%, 0%, 28%)`.
- **Channel values** copies the same numbers as `C100 M45 Y0 K28`.
- **Simulated hex** copies the HEX code of the press simulation.

These values are after dot gain and the ink limit. Use them as a starting point to discuss with your printer, not as final separations.

### Soft-proof an image

1. Drop an image on the drop area, select **Choose file**, or paste an image while the panel has focus.
2. Three versions appear: **Original**, the **Press simulation**, and an **Out-of-gamut warning** view where pink marks pixels that change by more than ΔE 10.
3. Change **Press condition** to compare conditions.
4. Select **Clear** to remove the image.

The image is scaled to at most 360 pixels on its longest side for the preview. Large images (the drop area suggests about 2 megapixels at most) are processed fastest.

Result: you see which areas of the image, typically bright blues, greens and saturated oranges, will print noticeably differently.

## Controls

| Control | What it does | Values or range | Default |
| --- | --- | --- | --- |
| Colour field | Colour to simulate | HEX, colour well, dice | #0085CA, or the colour you opened with |
| **Press condition** | Paper, ink limit and dot gain | 5 conditions | ISO Coated v2 (FOGRA39) |
| **CSS cmyk()** | Copies the separation as `cmyk()` | — | — |
| **Channel values** | Copies `C… M… Y… K…` | — | — |
| **Simulated hex** | Copies the simulated colour | — | — |
| Drop area / **Choose file** / paste | Loads an image | Image files | — |
| **Clear** | Removes the image | — | — |

## Accuracy and limits

- This is not colour-managed soft-proofing. The CMYK split is a naive formula, and the press conditions are simple models (paper colour, black point, dot gain and ink limit) named after common standards. They do not use the official characterisation data or ICC profiles.
- Your screen's own calibration affects what you see.
- Real separations depend on the printer's profile, rendering intent, black generation and more. Ask for a contract proof for colour-critical work.
- Images are processed in your browser and are not uploaded.

## Related

- [Colour Tools documentation](README.md)
- [Pantone & Named Lookup](pantone-and-named-lookup.md)
- [Color Formulation](colour-formulation.md)
- [CMYK and the Four-Color Printing Process](https://auricartisan.com/library/learn/articles/2026-06-03-cmyk-four-color-printing-process) on Learn
- [Basic Color Tools](../../README.md)
