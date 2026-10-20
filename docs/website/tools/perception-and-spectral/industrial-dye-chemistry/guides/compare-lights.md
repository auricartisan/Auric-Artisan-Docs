---
title: Industrial Dye Chemistry (Dye in Solution) — Compare lights
description: Choose the illuminant, read the colour readouts, compare the bath under every light, and understand colour inconstancy, metamerism, dominant wavelength and purity.
product: Website › Tools › Perception and spectral › Industrial Dye Chemistry
updated: 2026-09-25
---

# Compare lights

## Why the light matters

A dye does not have a colour on its own. The colour you see is the light that the bath lets through, and that depends on what light went in. The page computes it wavelength by wavelength: the illuminant's power × the bath's transmittance × the CIE 1931 2° standard observer's colour-matching functions, summed over 81 samples from 380 to 780 nm at 5 nm. The observer is used at the 5 nm spacing it is published at, so no sample is interpolated.

## Choose the illuminant

Under **The light**:

| Option | What it is |
|---|---|
| **D65 — daylight, 6504 K** (default) | CIE standard average daylight, reconstructed from the published CIE daylight basis |
| **D50 — daylight, 5003 K** | Warmer daylight, the usual reference in graphic arts |
| **A — a blackbody at 2856 K** | Incandescent (tungsten) light, from Planck's law |
| **E — equal energy** | Equal power at every wavelength; a theoretical reference |

**F11 is not offered.** Fluorescent lamps such as F11, the light most often used in shops and the one a dyer most wants, have narrow mercury emission lines. The CIE publishes them as measured tables that cannot be computed from a formula, and the page does not hold them. It shows F11 as a card marked **not held** rather than offering a smooth imitation under that name.

## Read the colour readouts

| Readout | Meaning |
|---|---|
| **sRGB** | The hex colour of the light leaving the bath under the chosen illuminant, not adapted to it, so a bath under A looks warmer |
| **CIE L\*** | Lightness from 0 to 100 |
| **a\*, b\*** | Red–green and yellow–blue coordinates |
| **Inside sRGB** | Whether the colour fits the sRGB range; **no** (highlighted) means the swatch is the nearest colour a screen can show |
| **Observer** | CIE 1931 2° |

L\*, a\* and b\* are CIE L\*a\*b\* taken against the white of the **chosen illuminant itself**, not against D65. That way, when you switch lights, a change in L\*a\*b\* measures the dye's colour moving relative to the light, not simply the fact that the lamp is a different colour.

The swatch is un-adapted on purpose: it shows how the bath would look if the light changed while your eyes stayed adapted to the screen. The two answer different questions, and the page labels both.

## Compare the bath under every light

**The same bath under every light this tool holds** shows one swatch per illuminant. The current light is labelled **— this bath** with its hex; the others show **ΔE₀₀**, the colour difference from the current light.

**ΔE₀₀** (CIEDE2000, CIE 142-2001) is the CIE's recommended measure of how different two colours look; the page uses the full formula including its rotation term for blues. A difference around 1 is at the edge of what most people notice side by side under good conditions; several units is plainly visible.

With the default bath under D65, the differences are about 1.60 to D50, 6.57 to A and 0.74 to E.

## Colour inconstancy is not metamerism

What the lights row measures is **colour inconstancy**: how far one bath's colour moves between two lights.

**Metamerism** is a property of a **pair**: two samples with different spectra that match under one light and stop matching under another. It is the everyday failure in industrial dyeing, where a dyed batch matches the standard in the dyehouse and not in the shop. It needs two baths. The **Method** tab's **The light** view explains the difference. The current interface compares one bath across lights and has no control for comparing two baths, so it does not report a metamerism index.

## Dominant wavelength and excitation purity

| Readout | Meaning |
|---|---|
| **Dominant λ** | The wavelength of the spectral colour that, mixed with the illuminant's white, would match the bath; found by drawing a line on the chromaticity diagram from the white point through the bath's colour to the edge of the diagram |
| **Excitation purity** | How far the bath's colour lies along that line, from 0% at the white point to 100% at the spectral edge |

For purples, the line meets the straight "purple line" at the bottom of the diagram instead, where there is no spectral colour. The page then gives the **complementary** wavelength with a `c` prefix (for example `c540 nm`), shows purity as **—**, and explains in a note under the readouts. A bath whose colour sits exactly on the white point has no dominant wavelength, and a note says so.

The default bath reads **Dominant λ** about 592 nm and **Excitation purity** about 36.7%.

## Try it

1. With the default bath, switch **The light** to **A — a blackbody at 2856 K**.
2. The swatch and **sRGB** turn a strong orange (`#FFB535`). **CIE L\*** and **a\*, b\*** move less, to about 89.3 and 27.3, 39.7, because they are taken against illuminant A's own white; what remains is the dye's own colour inconstancy.
3. In the lights row, the D65 swatch now shows about 6.57 ΔE₀₀: the same size of shift, seen from the other side.
4. Add the **Anthraquinone blue, pH-stable** and compare the differences again: mixtures can be more or less constant than their components.

You should now be able to say how far a bath's colour moves between lights, and why that number is not a metamerism index.
