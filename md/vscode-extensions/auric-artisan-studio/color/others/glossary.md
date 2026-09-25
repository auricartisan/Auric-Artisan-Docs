---
title: Auric Color — Glossary
description: Colour and contrast terms used in the Auric Color documentation.
product: VS Code extensions › Auric Artisan Studio › Auric Color
updated: 2026-09-25
---

# Auric Color glossary

**Alpha.** How opaque a colour is, from 0 (transparent) to 1 (solid). Written as the last two digits of 8-digit hex or the last value of `rgb()` and `hsl()`.

**APCA and Lc.** The Accessible Perceptual Contrast Algorithm from the WCAG 3 working draft. It reports lightness contrast as Lc; Auric Color's default target is Lc 60. Experimental.

**Chroma.** How colourful a colour is, as opposed to grey. The C in OKLCH.

**Colour decorators.** VS Code's own small colour squares and picker for colour values.

**Colour literal.** A colour written directly in code, such as `#1d4ed8` or `oklch(0.49 0.22 264)`.

**Colour-vision deficiency (CVD).** Reduced ability to tell some colours apart. Simulated types: protanopia, protanomaly, deuteranopia, deuteranomaly, tritanopia, tritanomaly, achromatopsia and achromatomaly.

**Colour-vision risk.** A pair that meets its contrast target for typical vision but not under a simulated deficiency.

**Confusable hues.** Two project colours that look distinct normally but alike under a simulated deficiency.

**Contrast ratio.** WCAG 2.x's brightness difference between two colours, 1:1 to 21:1. Targets: 4.5:1 for normal text, 3:1 for large text and UI, 7:1 for AAA.

**Custom property.** A CSS variable such as `--brand-ink`, also called a design token.

**ΔE (CIEDE2000).** How different two colours look. Around 1 is barely visible.

**Display-P3.** A wide-gamut colour space used by many modern screens.

**Gamut mapping.** Bringing a colour a screen cannot show to the nearest one it can.

**Harmony.** A rule for choosing related hues: complementary, split complement, analogous, triadic, tetradic, square, double split or monochromatic.

**Hue.** The colour's position on the colour wheel, in degrees.

**Hue-preserving fix.** A fix that changes only lightness, so the colour keeps its hue and chroma.

**Large text.** At least 24 CSS pixels, or 18.66 pixels and bold.

**Nearest CSS name.** The CSS named colour that looks closest, marked `≈` when not exact.

**OKLCH.** A colour model with lightness, chroma and hue designed so equal steps look equal. Used for shade scales.

**Page background.** The background declared on `body`, `html` or `:root`, used for rules that set only a text colour.

**Picker mode.** Whether Auric's picker or VS Code's native picker handles colours.

**Shade scale.** An 11-step tonal scale of one colour, 50 to 950.

**Swatch.** A small square of colour.

For all other terms, see the [Studio glossary](../../others/glossary.md).
