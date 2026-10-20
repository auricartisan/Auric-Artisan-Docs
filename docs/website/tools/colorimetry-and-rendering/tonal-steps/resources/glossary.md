---
title: Tonal Steps — Glossary
description: Plain-language definitions of the terms used in Tonal Steps, Tints and Shades.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tonal Steps glossary

**AA, AAA, AA large** — WCAG 2.2 contrast ratings: AAA at 7:1 or more, AA at 4.5:1 or more, AA large at 3:1 or more (for large text). Below 3:1 the tool shows **Fail**.

**APCA (Accessible Perceptual Contrast Algorithm)** — a contrast method by Myndex; the tool runs version APCA-W3 0.1.9. Its result, **Lc**, is signed.

**CIELAB (L\*a\*b\*)** — a CIE colour space with lightness L* and opponent axes a* and b*, computed here against the D65 white.

**Easing γ** — an exponent that bends where steps fall in the Equal luminance engine and the neutral ladder.

**Evenness** — how much the gaps between neighbouring steps stray from their average, as ±%. Smaller is more even.

**HSL** — hue, saturation and lightness: a simple rearrangement of RGB. HSL lightness is a coordinate, not a measure of perceived lightness.

**Key set** — a ladder of colours named by keys such as 50, 100 … 900, as used in design-system palettes.

**LCh** — CIELAB expressed as lightness, chroma and hue angle.

**Linear sRGB** — sRGB values with the transfer curve removed, proportional to light. OKLab and luminance need it as input.

**Mixing space** — the colour space in which two colours are interpolated. It changes the middle of a mix.

**Neutral ladder** — a scale of greys from black to white.

**OKLab** — a perceptual colour space (Ottosson, 2020). **OKLab L** is its lightness, from 0 (black) to 1 (white).

**Ramp** — a sequence of steps from light to dark built from one colour.

**Relative luminance (Y)** — the brightness of a colour on a 0 to 1 scale, computed from linear sRGB with the BT.709 weights 0.2126, 0.7152 and 0.0722.

**Shade** — a colour mixed with black.

**Tint** — a colour mixed with white.

**Tone** — a colour mixed with grey (here #808080).

**WCAG contrast ratio** — (L1 + 0.05) ÷ (L2 + 0.05) for the lighter and darker luminances, from 1:1 to 21:1.
