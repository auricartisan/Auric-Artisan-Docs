---
title: Illuminants — Overview
description: What the Standard Illuminants lab does, who it is for, where to find it and how to take your first reading.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Illuminants

The Standard Illuminants lab shows you what a light source is made of and what that does to colour. You pick one of 18 CIE standard illuminants (A, D50, D55, D65, D75, equal-energy E and the fluorescent series F1 to F12) or a blackbody radiator at any colour temperature from 1,500 K to 25,000 K. The lab draws its spectral power distribution, integrates it against the CIE 1931 2° standard observer, and reports its white point, correlated colour temperature (CCT), Duv, colour rendering, how surfaces look under it, and how a set of colours adapts from one white point to another.

Around that core it adds views for the chromaticity diagram (in three planes), a Monte Carlo estimate of how measurement error propagates into x, y, CCT and Duv, a comparison of calculation methods, a small query console for comparing many illuminants at once, and a data register that says where every table comes from. Every reading carries a line naming the dataset, observer and interval behind it.

The lab is honest about its limits. The CIE fluorescent tables and the CIE 13.3 test colour samples are not held, so fluorescent spectra and colour rendering figures are built from stand-ins and labelled as such. IES TM-30 is not computed at all. See [Limits and accuracy](others/limits-and-accuracy.md).

## Who it is for

- Designers and photographers who want to know why a colour looks different under office, shop or home lighting.
- Developers and colour-management practitioners working with D50 and D65 white points (ICC workflows, sRGB, print).
- Students learning how illuminants, CCT, Duv and chromatic adaptation fit together.
- Lighting and measurement people who want a quick, traceable reference calculation — not a certified one.

## Where to find it

- Address: https://auricartisan.com/tool/general/colorimetry/illuminants/
- In the tool collection (https://auricartisan.com/collections/) under **Colorimetry**, as **Illuminants**.
- It works in any current desktop or mobile browser. No account is needed.

## Quick start

1. Open https://auricartisan.com/tool/general/colorimetry/illuminants/. The **Lab** tab opens with CIE D65 selected.
2. Read the **Illuminant Summary** at the top of the results: CCT, Duv, CIE x and y, CRI Ra and XYZ.
3. Open the **Illuminant** list and choose **CIE A (2856 K) — Incandescent**. Watch the spectrum tilt towards red.
4. Tick **Enable comparison** and leave the comparison illuminant on D65 (choose **CIE D65 (6504 K)** in the list). The chart overlays both curves and a comparison table appears at the bottom.
5. Look at **Surface appearance** to see how skin, paint and ink samples shift under the new light.
6. Open the **Chromaticity** tab to see where the light sits against the Planckian locus.
7. Open **Export** and select **Export SPD CSV** to download the spectrum.

## What you can do

- Plot the spectrum of any of 18 standard illuminants or a blackbody at a custom CCT.
- Read white point (x, y, XYZ), CCT and Duv computed by Ohno's method, with a validity check.
- Compare two illuminants and get a metamerism index.
- See how eight sample surfaces render under the light, with CIEDE2000 differences.
- Adapt a 24-colour chart between white points with six chromatic adaptation transforms (or none) and inspect the matrix.
- View chromaticity in CIE 1931 xy, CIE 1976 u′v′ or CIE 1960 uv, with the Planckian locus, isotemperature lines, the daylight locus and RGB primaries.
- Read the dominant wavelength and purity.
- Propagate an instrument uncertainty budget into x, y, CCT and Duv by Monte Carlo simulation.
- Compare interval and interpolation choices, and the Ohno and McCamy CCT methods.
- Query many illuminants at once and export the results as CSV or JSON.
- Export the spectrum as CSV, JSON or PNG, copy the white as HEX, and share a link to your settings.

## In this folder

- [docs/](docs/README.md) — how to use the lab
  - [Getting started](docs/getting-started.md)
  - [Compare two light sources](docs/compare-light-sources.md)
  - [Adapt colours between white points](docs/adapt-between-white-points.md)
  - [Estimate measurement uncertainty](docs/estimate-uncertainty.md)
  - [Query many illuminants at once](docs/query-console.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — background and supporting pages
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related tools](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
