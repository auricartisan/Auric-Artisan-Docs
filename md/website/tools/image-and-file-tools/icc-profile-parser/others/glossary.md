---
title: ICC Profile Parser — Glossary
description: Definitions of the terms used in the ICC Profile Parser.
product: Website › Tools › Image and file tools › ICC Profile Parser
updated: 2026-09-25
---

# ICC Profile Parser glossary

| Term | Meaning |
|---|---|
| A2B / B2A table | Tables converting device values to the PCS (A2B) or back (B2A); 0, 1, 2 are perceptual, colorimetric, saturation |
| Area ratio | The area of one gamut triangle divided by another's; can exceed 100% |
| Bradford transform | The standard chromatic adaptation method, from Lam (1985), carried by the `chad` tag |
| `chad` tag | A 3×3 matrix recording how the colorants were adapted to D50 |
| Chromatic adaptation | Converting colour values from one white point to another |
| Chromaticity diagram | A plot of colour without brightness; the tool uses CIE 1931 xy for drawing |
| CIE 1976 u′v′ | A chromaticity diagram in which equal distances look more nearly equal than in xy |
| CIELAB | A colour space with lightness L* and two colour axes, a* (green to red) and b* (blue to yellow) |
| Clause | A numbered section of ICC.1:2010 that a conformance rule enforces |
| CLUT | Colour lookup table: a grid of output values sampled at points across the input |
| CMM | Colour management module, the software that performs conversions; named in the header |
| Colorant | The stored XYZ value of a primary, already adapted to D50 |
| Conformant | Breaking no rule graded as an error |
| Coverage | The share of a reference gamut that lies inside the profile's gamut; at most 100% |
| D50 / D65 | Standard daylight whites at about 5000 K and 6500 K; D50 is the ICC connection-space white |
| Data colour space | The colour space of the device values, such as RGB or CMYK |
| Device class | What the profile describes: Input, Display, Output, DeviceLink, ColorSpace, Abstract or NamedColor |
| Finding | A rule that did not hold for the loaded profile, with severity, clause and detail |
| Gamut | The range of colours a device or colour space can reproduce |
| Header | The first 128 bytes of a profile, describing its kind |
| House preference | A rule the tool applies that no clause requires |
| ICC profile | A file, defined by the International Color Consortium, describing how a device or space reproduces colour |
| Matrix/TRC | A profile built from three colorants and three tone response curves |
| Media white point | The white of the display or paper, in the `wtpt` tag |
| MD5 | A checksum algorithm (RFC 1321) used for the profile ID |
| PCS | Profile connection space: CIE XYZ or CIELAB at D50, through which profiles are joined |
| Primaries | The red, green and blue chromaticities that define an RGB colour space |
| Profile ID | An MD5 checksum of the profile, stored in bytes 84 to 99 of the header |
| Rendering intent | The strategy for out-of-gamut colours: perceptual, media-relative, saturation or absolute |
| Spectral locus | The horseshoe outline of pure spectral colours on a chromaticity diagram |
| Tag | A four-character signature pointing to a block of data in the profile |
| Tag type | The four-character code at the start of a tag's data that says how to read it |
| TRC | Tone response curve: how a channel's values map to linear light |
| Transfer function | The published curve relating encoded values to light for a colour space |
| XYZ | The CIE 1931 tristimulus values, the basis of colorimetry |
| XYZ scaling | A simple adaptation that scales X, Y and Z directly; used by some older profiles |
