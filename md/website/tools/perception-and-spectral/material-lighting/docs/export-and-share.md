---
title: Material Lighting (Material Under Light) — Export and share
description: Download the 81-row spectrum CSV and the whole-scene JSON, and copy a link that rebuilds the scene.
product: Website › Tools › Perception and spectral › Material Lighting
updated: 2026-09-25
---

# Export and share

Nothing leaves the page until you press a button. **Save the spectrum** on the Lab tab and **Download the spectrum** on the **Export** tab save the same file.

On the Export tab, **What to take** switches the preview between **The spectrum** (the first lines of the CSV), **The whole scene** (the first part of the JSON) and **A link to this**; the note above it gives the row count.

| Button | Result |
|---|---|
| **Download the spectrum** | Saves `material-under-light-spectrum.csv` |
| **Download the scene** | Saves `material-under-light-scene.json` |
| **Copy a link to this scene** | Copies a link; **Link copied** confirms it, or the link is shown if the clipboard is unavailable |

## The spectrum CSV

The file starts with `#` header lines:

| Line | Contents |
|---|---|
| `sampling` | 380–780 nm at 5 nm, 81 samples |
| `observer` | CIE 1931 2°, published at 10 nm, interpolated to 5 |
| `illuminant` | The light and its definition |
| `measured_cct` | The measured colour temperature and its error band |
| `reference` | The reference light's kind, temperature and the reason |
| `material`, `reflectance` | The material, and whether its curve is MEASURED (with the file name) or SYNTHESISED |
| `surface` | Conductor, or dielectric with its refractive index; the lobe; the roughness |
| `geometry` | Light, view and azimuth angles |
| `exposure` | The scale that makes a white diffuser read Y = 1 |
| `swatch_white`, `lab_white` | That the swatch is un-adapted and L\*a\*b\* uses the light's own white |
| `rendering_shift` | ΔE₀₀ for this sample between the source and its reference |
| `NOT_A_RENDERING_INDEX` | That this is one sample, and that CRI and TM-30 are withdrawn |
| `sensitivity` | The sweep's median and 95th percentile, if you ran one |

Then 81 rows:

| Column | Meaning |
|---|---|
| `wavelength_nm` | 380 to 780 in steps of 5 |
| `illuminant_relative` | The illuminant's power, scaled to peak at 1 |
| `reflectance` | The material's reflectance |
| `radiance_relative` | The light leaving the surface at your geometry, scaled by the exposure |
| `observer_xbar`, `observer_ybar`, `observer_zbar` | The CIE 1931 2° colour-matching functions |

## The scene JSON

| Field | Contents |
|---|---|
| `tool`, `generated` | The tool name and time |
| `sampling`, `observer` | The grid, and the observer's published and used steps with a note on interpolation |
| `illuminant`, `measured_cct`, `reference` | The light, its measured temperature and band, and the reference chosen |
| `material` | Its id, reflectance status and source, conductor flag and refractive index |
| `surface`, `geometry`, `exposure` | Lobe and roughness; the three angles; the exposure scale |
| `colour` | sRGB hex (un-adapted), L\*a\*b\*, the white used, JzAzBz, gamut flag |
| `rendering_shift` | ΔE₀₀, marked `is_rendering_index: false` |
| `withdrawn` | CRI and TM-30, each with why and what it would take |
| `sensitivity` | The sweep result, or `null` |
| `spectrum` | Wavelength, illuminant, reflectance and radiance arrays |
| `register` | Every Data register entry with its source and status |

## Links

A link rebuilds the scene with these parameters: `illuminant` (`d65`, `d50`, `d55`, `d75`, `a`, `e`, `planck`, `daylight`), `cct`, `material` (for example `gold`), `ior`, `roughness`, `thetaL`, `thetaV`, `phi`, `lobe` (`ggx`, `beckmann`, `ward`, `ashikhmin-shirley`, `oren-nayar`) and `metal` (`1` for conductor, `0` for dielectric). For example:

```text
https://auricartisan.com/tool/general/spectral-tools/material-lighting/?illuminant=a&cct=2700&material=skin&ior=1.5&roughness=0.4&thetaL=30&thetaV=20&phi=0&lobe=ggx&metal=0
```

A link does not carry a measured reflectance file or the sweep settings.

You should now have a file that records the light, the material's provenance and the geometry along with the numbers.
