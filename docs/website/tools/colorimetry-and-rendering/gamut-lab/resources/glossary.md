---
title: Gamut Lab — Glossary
description: Plain-language definitions of the terms used in the Gamut Lab.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Gamut Lab glossary

**ACES (AP0, AP1)** — the Academy Color Encoding System. AP0 (ACES 2065-1) is an archival space with imaginary primaries; AP1 (ACEScg) is a working space with primaries inside the locus. Both are linear.

**Chromaticity diagram** — a map of colour without brightness. CIE 1931 xy is the classic form; CIE 1976 u′v′ is more uniform.

**CIELAB** — a colour space with lightness L* and axes a* (green–red) and b* (blue–yellow), used here to measure gamut volume and slices.

**EOTF** — electro-optical transfer function: turns a signal into light on a display.

**Gamma** — shorthand for a power-law transfer curve, such as 2.2 or 2.6.

**Gamut** — the colours a space can represent. On a chromaticity diagram, an RGB gamut is a triangle.

**Gamut volume** — the size of a gamut in CIELAB, in Lab³ (units cubed).

**Halton sampling** — quasi-random sampling that covers space evenly; its error shrinks faster than random sampling.

**HLG (hybrid log-gamma)** — a relative HDR transfer curve (ARIB STD-B67, ITU-R BT.2100).

**Imaginary primary** — a primary outside the spectral locus: a mathematical colour no light can produce.

**Jaccard index** — the overlap of two areas divided by their combined area.

**Line of purples** — the straight edge of the chromaticity diagram between violet and red.

**MacAdam ellipses** — regions on the chromaticity diagram within which colours look the same to an observer, measured by MacAdam in 1942.

**OETF** — opto-electronic transfer function: encodes light as a signal.

**OKLab** — a perceptual colour space (Ottosson, 2020) with straighter hue lines than CIELAB.

**PQ (perceptual quantiser)** — the absolute HDR transfer curve of SMPTE ST 2084, mapping signal to 0–10,000 cd/m².

**Primaries** — the three reddest, greenest and bluest colours an RGB space mixes from.

**RGB ↔ XYZ matrix** — the 3 × 3 matrices that convert linear RGB of a space to CIE XYZ and back.

**ROMM RGB** — the ISO 22028-2 encoding behind ProPhoto RGB: a 1.8 power with a linear toe.

**Shoelace formula** — the method used to compute a polygon's area from its corners.

**Spectral locus** — the curved edge of the chromaticity diagram, made by single wavelengths.

**Spread** — here, how much a volume estimate changed against a run at half the samples. Not a confidence interval.

**Transfer function** — the curve between stored values and light.

**u′v′ share** — a triangle's area as a percentage of the spectral locus area in the u′v′ diagram.

**White point** — the chromaticity a space treats as white, such as D65 or D50.
