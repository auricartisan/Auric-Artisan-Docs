---
title: Material Lighting (Material Under Light) — Overview
description: What the Material Under Light tool does, who it is for, where to find it and how to render a first material under a chosen light.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Material Lighting (Material Under Light)

The Material Lighting tool, whose page is titled **Material under light**, computes the colour of a surface the way light actually produces it: one wavelength at a time. It multiplies three things at each of 81 wavelengths from 380 to 780 nm: the power of a light source (the illuminant), the share of that light the material reflects (its reflectance spectrum), and how much of the reflected light travels towards your eye at the angles you set (the reflectance lobe). It then turns the result into a colour with the CIE 1931 standard observer and shows it as a shaded sphere, a swatch and a set of numbers.

Because the calculation is spectral, the tool can show things a three-channel RGB renderer cannot: why the same material looks different under daylight and tungsten, and why two materials that match under one light can part under another (metamerism). It also compares your material under your chosen light with the same material under the reference light the CIE rule names for that light's colour temperature, and reports the difference as a CIEDE2000 colour difference.

The twenty material presets are the tool's own curves, built from a flat level plus bell-shaped bumps; none is a measurement. You can load a measured reflectance file instead. The two colour rendering scores an earlier version printed (CRI and TM-30) are withdrawn, and the **Metrics** tab explains why. Everything runs in your browser.

## Who it is for

- Designers, 3D artists and lighting designers who want to see how a light source changes a material's colour.
- Students of colour science learning spectral power distributions, reflectance, colour temperature and reference illuminants.
- Anyone curious why gold, skin or a leaf look different under a warm lamp.

## Where to find it

Open https://auricartisan.com/tool/general/spectral-tools/material-lighting/ in a current browser. It is listed as **Material Lighting** on the Collections page (https://auricartisan.com/collections/) and in the site menu.

## Quick start

1. Open the tool. The scene is **Gold** under **D65 — daylight, 6504 K**, with the **GGX** lobe, roughness 0.40, light from 30° and view from 20°.
2. Look at the spectrum plot: the illuminant (dashed), the reflectance, and the light leaving the surface (filled).
3. Switch **The light** to **A — a blackbody at 2856 K** and watch the sphere and swatch warm up.
4. Read **Measured temperature** and **Reference for it**, and the ΔE₀₀ between **Under your source** and **Under its reference**.
5. Choose **Skin** under **The material**, then select **Conductor** and back to **Dielectric**.
6. Pick a different lobe card, such as **Oren-Nayar**, and move **Roughness**.
7. Select **Save the spectrum** to download the 81-row CSV.

## What you can do

- Light a material with D65, D50, D55, D75, A, E, or a blackbody or daylight at a temperature you choose.
- Choose from twenty materials, or load a measured reflectance file.
- Set the surface as a dielectric with a refractive index, or a conductor (metal), and its roughness.
- Choose one of five published reflectance lobes: GGX, Beckmann, Ward, Ashikhmin-Shirley or Oren-Nayar.
- Set the light angle, the view angle and the azimuth between them.
- Read the colour as sRGB, CIE L\*a\*b\* and Jz, with the gamut flag.
- Read the source's measured colour temperature with its error band, and compare the material with its CIE reference light.
- Run a sensitivity sweep that perturbs the reflectance curve.
- Export the spectrum as CSV, the whole scene as JSON, or a link.

## In this folder

- [docs/](docs/README.md) — how to use the tool.
  - [Getting started](docs/getting-started.md) — open it, the screen tour, the first scene.
  - [Set up a scene](docs/set-up-a-scene.md) — the light, the material, the surface, the lobes and the geometry.
  - [Compare with the reference light](docs/compare-with-the-reference.md) — colour temperature, the reference rule, the colour difference and the two white points.
  - [Run a sensitivity sweep](docs/run-a-sensitivity-sweep.md) — the Metrics tab and the withdrawn rendering indices.
  - [Use a measured reflectance](docs/use-a-measured-reflectance.md) — load your own reflectance file.
  - [Export and share](docs/export-and-share.md) — the spectrum CSV, the scene JSON and links.
  - [Reference](docs/reference.md) — every control, readout, tab and file format.
  - [Troubleshooting](docs/troubleshooting.md) — symptoms, causes and fixes.
  - [FAQ](docs/faq.md) — short answers to common questions.
- [others/](others/README.md) — background material.
  - [Glossary](others/glossary.md) — terms used in this tool.
  - [Shortcuts](others/shortcuts.md) — keyboard and pointer actions.
  - [Limits and accuracy](others/limits-and-accuracy.md) — what is published, what is the tool's own, what is not held.
  - [Related](others/related.md) — related tools and Learn articles.
  - [Release notes](others/release-notes.md) — user-facing history.
  - [Privacy](others/privacy.md) — what stays in your browser.
