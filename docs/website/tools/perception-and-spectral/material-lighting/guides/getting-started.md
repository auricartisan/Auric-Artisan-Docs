---
title: Material Lighting (Material Under Light) — Getting started
description: Open Material Under Light, learn the layout of the Lab tab and read the default gold-under-daylight scene.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Getting started with Material Under Light

## Open the tool

Go to https://auricartisan.com/tool/general/spectral-tools/material-lighting/. The page opens on the **Lab** tab with a default scene: **Gold**, as a dielectric with refractive index 1.50, under **D65 — daylight, 6504 K**, with the **GGX** lobe at roughness 0.40, the light 30° and the eye 20° from the surface normal, and 0° between them.

A note strip above the tabs, which cannot be closed, says that two rendering figures from an earlier version were withdrawn and links to the **Metrics** and **Method** tabs.

## The six tabs

| Tab | What it is for |
|---|---|
| **Lab** | Set up the scene, see the spectrum and the sample, read the colour, compare with the reference light |
| **Method** | How a spectrum becomes a colour, how the reference is chosen, the five lobes, the two white points |
| **Metrics** | The sensitivity sweep, and the two withdrawn rendering indices |
| **Data** | The register of 17 tables and formulas, with a status for each; load a measured reflectance here |
| **Export** | The spectrum CSV, the scene JSON and a link |
| **Reference** | Fourteen sources, filterable |

## A tour of the Lab tab

**The rail (left)**, top to bottom:

- **The light** — the illuminant menu and **Temperature** (used only by the last two options).
- **The material** — the material menu, **Dielectric** / **Conductor**, and **Refractive index**.
- **The surface** — **Roughness**.
- **The geometry** — **Light from**, **Seen from** and **Between them**.
- **Save the spectrum** and **Reset the scene**.

**The stage (right)**:

- **The spectrum** — three curves against wavelength: **Illuminant** (dashed), **Reflectance** (solid) and **What leaves the surface** (filled), each scaled to its own maximum. The legend names the illuminant, the material and whether it is synthesised or measured.
- **The sample** — a sphere of the material lit from your light angle, with the note **scaled so a white card here would read Y = 1** and, when colours had to be clipped, a **clipped to sRGB** badge.
- Five lobe cards: **GGX**, **Beckmann**, **Ward**, **Ashikhmin-Shirley** and **Oren-Nayar**, each with a one-line description and its source.
- Two rows of readouts: **sRGB**, **CIE L\***, **a\*, b\***, **Jz**; **Measured temperature**, **Reference for it**, **Reflectance**, **Inside sRGB**.
- **Against the reference the standard names** — two swatches, **Under your source** and **Under its reference**, with the ΔE₀₀ between them.

## Read the default scene

1. In the plot, the dashed D65 curve is fairly flat, the gold reflectance rises from low values in the blue to a plateau in the orange and red, and the filled product follows the reflectance.
2. The swatch reads **sRGB** `#FFD026`, with **CIE L\*** 87.2 and **a\*, b\*** 9.6, 82.9: a strong yellow.
3. **Inside sRGB** reads **no** and the sphere shows **clipped to sRGB**: this gold is more saturated than sRGB can show, so the screen shows the nearest colour it can.
4. **Measured temperature** reads **6500 K +/- 11 K**: the page measured the D65 spectrum's colour temperature back out of it. **Reference for it** reads **daylight 6500 K**.
5. **Under your source** and **Under its reference** look the same, and the difference reads about 0.01: D65 is its own reference.
6. **Reflectance** reads **synthesised**: the gold curve is the tool's own.

Now switch **The light** to **A — a blackbody at 2856 K**. The sphere and swatch turn orange (`#FFC500`), **Measured temperature** reads about 2860 K, and **Reference for it** becomes **blackbody 2860 K**.

You should now see a scene whose spectrum, sample and numbers follow every control.

## Next steps

- [Set up a scene](set-up-a-scene.md) covers every control.
- [Compare with the reference light](compare-with-the-reference.md) explains the colour temperature and the reference swatches.
