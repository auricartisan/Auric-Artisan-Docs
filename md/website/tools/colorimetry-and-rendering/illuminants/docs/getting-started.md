---
title: Illuminants — Getting started
description: Open the Standard Illuminants lab, learn its eight tabs and take your first reading of a light source.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Getting started with Illuminants

## Open the lab

Go to https://auricartisan.com/tool/general/colorimetry/illuminants/. The page title is **Standard Illuminants**. Nothing needs installing and you do not need to sign in. All calculations run in your browser.

## Key ideas before you start

- An **illuminant** is a light source described by its **spectral power distribution (SPD)**: the relative power it emits at each wavelength from 380 nm (violet) to 780 nm (deep red).
- The lab turns an SPD into colour by weighting it with the **CIE 1931 2° standard observer** — three curves that describe how an average observer matches colours in a small (2°) field of view. The result is the tristimulus values **X, Y, Z**, and from them the chromaticity **x, y** — the illuminant's **white point**.
- **Correlated colour temperature (CCT)** is the temperature, in kelvin, of the blackbody (Planckian) radiator whose colour is closest to the light. Low CCT is warm (candle, tungsten); high CCT is cool (north sky).
- **Duv** is how far the light's chromaticity sits from the blackbody curve, in the CIE 1960 uv plane. Positive Duv is greenish; negative is pinkish. CCT only means something when Duv is small.

## A tour of the screen

A note at the top of the tool explains that every figure is traceable: the line under each result names the dataset, observer and interval behind it.

The tabs across the top are:

| Tab | What it is for |
| --- | --- |
| **Lab** | Choose the light, compare it, see surfaces and chromatic adaptation. The main working view. |
| **Chromaticity** | The chromaticity diagram in three planes, with loci, isotemperature lines and the dominant wavelength. |
| **Uncertainty** | Monte Carlo propagation of an instrument uncertainty budget into x, y, CCT and Duv. |
| **Methods** | How much the interval and interpolation choices move the result, and how two CCT methods compare. |
| **Console** | A small query language for comparing many illuminants in one table and plot. |
| **Data** | The register of every dataset the lab uses, with its status. The tab label shows the count (15). |
| **Export** | Downloads, the share link and the all-illuminant comparison table. |
| **Reference** | Standards, formulas, citations and research notes, with a search filter. |

### The Lab tab

The left rail holds the controls, grouped as **Source mode**, **Illuminant**, **CCT**, **Comparison illuminant**, **Surface reflectance samples** and **Chromatic adaptation**. The results column on the right shows, from top to bottom:

1. **Illuminant Summary** — a swatch of the white, its name, type and HEX, then CCT, Duv, CIE x, CIE y, CRI Ra and XYZ.
2. **SPD — Spectral Power Distribution (380–780 nm)** — the spectrum. Gold is the selected light; blue is the comparison light when comparison is on.
3. **CRI — Colour Rendering Index (R1–R14)** — one bar per test sample and the Ra figure.
4. **Surface appearance — D65 reference vs test illuminant** — one row per ticked surface.
5. **Chromatic adaptation preview (24 patches)** — original colours on top, adapted colours below.
6. **Adaptation matrix details** — the transform matrix and cone scaling.
7. **Illuminant comparison** — metrics side by side when comparison is on.

## Take your first reading

1. On the **Lab** tab, make sure **Standard** is selected under **Source mode**.
2. Open the **Illuminant** list and choose **CIE D50 (5003 K) — Daylight, ICC PCS**.
3. Read the **Illuminant Summary**. CIE x and y should be close to 0.3457 and 0.3585, the published D50 white point.
4. Click anywhere on the SPD chart. The line under the chart shows the nearest wavelength and its relative power, with a colour chip for that wavelength.
5. Select the **Fullscreen** button on the chart (or double-click the chart) to see it larger. Press `Esc` or select the close button to return.
6. Drag the **CCT** slider to 3000 K. The lab switches to **Blackbody** mode and the spectrum becomes a smooth Planckian curve rising towards red.
7. Select **Reset to D65** to go back to standard D65 at 6500 K.

You should now see the D65 spectrum, a CCT of about 6504 K and a Duv close to zero.

## Where the numbers come from

Under several results you will see a provenance line such as "CIE 15:2018 Table 5, verbatim · CIE 1931 2° · 5 nm · Ohno 2014, parabolic · ∑ 380–780 nm". It tells you the dataset and its status, the observer, the wavelength interval, the method and the range summed over. When a reading rests on a stand-in, the line says "not a standard value". The [Data tab](reference.md#data-tab) explains each dataset.

## Next steps

- [Compare two light sources](compare-light-sources.md)
- [Adapt colours between white points](adapt-between-white-points.md)
- [Estimate measurement uncertainty](estimate-uncertainty.md)
- [Query many illuminants at once](query-console.md)
