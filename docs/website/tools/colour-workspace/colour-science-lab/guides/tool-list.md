---
title: Color Science Lab — The 45 tools
description: Every Color Science Lab panel tool by domain, with its level, what it is for and its default model.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# The 45 tools

Level **F** means Basic / Foundation (shown when the level is Basic or Both); **R** means Advanced / Research (shown when the level is Advanced or Both). Every tool opens the same panel described in [The Catalogue and its panels](catalogue-and-panels.md); the default model, space and theory differ.

## Colorimetry (5)

| Tool | Level | What it is for |
| --- | --- | --- |
| CIE XYZ and Lab Workbench | F | Convert samples between sRGB, CIE XYZ, xyY and CIE Lab with live white-point context. |
| Chromaticity Diagram | F | Plot samples, white points and approximate sRGB gamut positions on the CIE xy diagram. |
| Delta E Comparator | F | Compare two colours by Lab distance, luma drift, chroma drift and hue direction. |
| Standard Observer Lab | R | Compare 2° and 10° observers, xy chromaticity and u'v' uniform chromaticity. Default model: CIE 1931 observer. |
| Color Difference Suite | R | Audit Delta E 76 distance, chroma drift, luma drift and perceptual proxy spaces side by side. Default space: DIN99. |

## Chromatic Adaptation (6)

| Tool | Level | What it is for |
| --- | --- | --- |
| Bradford Adaptation | F | Move a colour from one reference white to another with a Bradford transform. |
| CAT02 and CAT16 Bench | R | Compare modern adaptation transforms with source and target whites. |
| Illuminant Match Bench | R | Study a colour under A, D50, D65, D75 and equal-energy whites. |
| Von Kries Adaptation Lab | F | Compare classic von Kries scaling with Bradford-style transforms. |
| CAT Matrix Comparison | R | Switch between XYZ scaling, von Kries, Bradford, CMCCAT, Sharp, CAT02, CAT16 and Bianco-Schettini. Default: CAT16. |
| White Point Reference Atlas | R | Inspect A, B, C, D-series, equal-energy, fluorescent, DCI and ACES D60 whites. |

## Spectral Analysis (6)

| Tool | Level | What it is for |
| --- | --- | --- |
| Visible Spectrum Explorer | F | Sweep wavelengths from violet to red and inspect approximate sRGB mapping. |
| Blackbody Radiation | F | Explore colour temperature from incandescent to daylight and blue sky. |
| Emission Line Mixer | R | Mix narrow spectral lines and compare against a broadband reference. |
| Metamerism Workspace | R | Compare similar colours under several illuminants and estimate metameric instability. |
| Daylight and Planckian Locus | R | Compare CIE daylight and Planckian blackbody behaviour and chromaticity drift. |
| Observer Sensitivity Curves | R | Explore wavelength bands through cone-like, CIE-like and opponent sensitivity proxies. |

## Appearance Models (6)

| Tool | Level | What it is for |
| --- | --- | --- |
| CIECAM16 Sandbox | R | Adjust luminance, surround and adaptation strength to see appearance behaviour. |
| HDR Appearance Lab | R | Push samples through high-dynamic-range viewing assumptions. |
| Surround Adaptation Study | F | Place a sample on dark, dim and average surrounds. |
| Fairchild Appearance Lab | R | Fairchild-style appearance ideas: media white, adapting luminance, colourfulness, context. |
| Hunt and Nayatani Models | R | Compare the Hunt and Nayatani models with modern CAM-style controls. |
| CIECAM02 and CAM16 Comparison | R | Compare CIECAM02, CAM16, CAT02 and CAT16 assumptions. |

## Perceptual Spaces (6)

| Tool | Level | What it is for |
| --- | --- | --- |
| Jzazbz Slice Visualizer | R | Inspect a perceptual slice for HDR and high-chroma relationships. |
| CAM02-UCS Distance | R | Compare uniformity estimates across Lab-like and CAM-derived coordinates. |
| Uniformity Stress Test | F | Generate hue and chroma ramps to see where equal numeric steps stop looking equal. |
| Oklab and Oklch Workbench | F | Oklab and Oklch coordinates for UI gradients, gamut checks and hue paths. |
| CIELAB, CIELUV, and LCh Suite | F | Compare Lab, Luv, LCh(ab), LCh(uv), Hunter Lab, DIN99 and related coordinates. |
| HDR Uniform Space Bench | R | Compare Jzazbz, JzCzhz, ICtCp, IPT, CAM02-UCS and CAM16-UCS. |

## Color Spaces (7)

| Tool | Level | What it is for |
| --- | --- | --- |
| 40+ Color Space Atlas | F | Browse RGB, CIE, perceptual, print, video, HDR and colour-order spaces from one panel. |
| RGB Working Space Matrix Lab | F | Compare sRGB, linear sRGB, Display P3, Adobe RGB, ProPhoto RGB, Rec.2020, ACES and classic RGB profiles. |
| Wide Gamut and HDR Space Lab | R | Rec.2020, ACES2065-1, ACEScg, ICtCp, Jzazbz, PQ, HLG and scene-linear workflows. |
| Video Component Space Lab | F | YCbCr, YPbPr, YUV, YIQ, Rec.601, Rec.709, Rec.2020 and HDR encodings. |
| Artist Cylindrical Space Lab | F | HSL, HSV, HSI, HWB, HSLuv, HPLuv, LCh, Oklch and Munsell-like hue systems. |
| Print and Process Space Lab | F | CMY, CMYK, ECI RGB v2, ColorMatch RGB, Best RGB, Beta RGB, Don RGB and D50 print workflows. |
| CIE and Perceptual Space Map | R | XYZ, xyY, u'v'Y, LMS, Lab, Luv, Hunter Lab, DIN99, Oklab, IPT, CAM02-UCS and CAM16-UCS. |

## Theory and History (4)

| Tool | Level | What it is for |
| --- | --- | --- |
| Newton Color Theory Studio | F | Newton's prism spectrum, colour circle and hue ordering, linked to modern wavelength and RGB views. |
| Classic Theory Comparison | F | Compare Newton, Goethe, Young-Helmholtz, Hering, Maxwell, Munsell, Ostwald and Grassmann. |
| Opponent and Color Constancy Lab | R | Hering opponent channels, von Kries adaptation, Retinex, NCS notation and colour constancy. |
| Fairchild and CAM Theory Lab | R | Trace Fairchild, Hunt, Nayatani, RLAB, LLAB, CIECAM02, CAM16, iCAM, IPT and Oklab ideas. |

## Gamut and Rendering (5)

| Tool | Level | What it is for |
| --- | --- | --- |
| Gamut Map | F | Compare samples against sRGB, Display P3 and Rec.2020 gamut boundaries. |
| Tone Curve Compression | R | Apply tone and chroma compression to see rendering trade-offs. |
| ACES Rendering Pipeline | R | ACES scene-linear, AP0/AP1, look, output transform and display rendering. |
| HDR Tone Mapping Lab | R | Compare PQ, HLG, Rec.2020, ICtCp and Jzazbz-style HDR compression. |
| ICC Rendering Intent Lab | F | Compare perceptual, relative colorimetric, absolute colorimetric and saturation intents. |

## The colour-space registry

**Color space / standard** lists 63 spaces: 30 RGB working spaces (sRGB, linear sRGB, scRGB, Display P3, DCI-P3, P3-D65, Adobe RGB (1998), ProPhoto RGB / ROMM, Rec.2020, Rec.2100 PQ and HLG, Rec.709, Rec.601 525 and 625, NTSC (1953), SMPTE-240M, Apple RGB, ColorMatch RGB, Adobe Wide Gamut RGB, CIE RGB, Best RGB, Beta RGB, Bruce RGB, Don RGB 4, ECI RGB v2, Ekta Space PS5, ACES2065-1, ACEScg, ACEScc, ACEScct), the CIE spaces (XYZ, xyY, u'v'Y), LMS, perceptual spaces (CIELAB, CIELCh(ab), CIELUV, CIELCh(uv), Hunter Lab, DIN99, DIN99o, Oklab, Oklch, HSLuv, HPLuv, IPT), HDR spaces (ICtCp, Jzazbz, JzCzhz), appearance spaces (CAM16-UCS, CAM02-UCS), cylindrical RGB (HSL, HSV / HSB, HSI, HWB), print (CMY, CMYK), video (Y'CbCr (709), Y'PbPr, Y'UV, Y'IQ) and colour-order systems (Munsell HVC, Natural Color System).

## Related

- [The Catalogue and its panels](catalogue-and-panels.md)
- [Catalogue Compare and Analytics](catalogue-compare-and-analytics.md)
