---
title: Tonal Steps — FAQ
description: Short answers to common questions about Tonal Steps, Tints and Shades.
product: Website › Tools › Colorimetry and rendering
updated: 2026-09-25
---

# Tonal Steps FAQ

## Which engine should I use?

Use **HSL lightness** for a quick, familiar ramp. Use **Equal luminance** when you want steps tied to WCAG contrast, and adjust easing so the steps look even. The Ramps tab measures how even each one is.

## Why are there two engines, not three?

Equal steps in WCAG contrast ratio are, mathematically, equal steps in relative luminance. The third engine produced the same colours as Equal luminance, so it is not offered as a separate choice.

## Why is OKLab used to measure the steps?

OKLab lightness tracks perceived lightness well, so gaps in OKLab L show whether a ramp looks evenly spaced. You can switch to CIELAB L* or relative Y on the Ramps tab.

## What is the difference between tints, shades and tones?

A tint adds white, a shade adds black, and a tone adds grey. All three start from your base colour.

## Are the 50–950 keys the Tailwind colours?

No. They are this tool's ladder with Tailwind's key names: mixed towards white below 500 and towards black above. Tailwind's own colours are tuned by hand per hue.

## Is APCA a requirement?

No. APCA is a working draft of what WCAG 3 may adopt. WCAG 2.2 ratios remain the published requirement. The tool shows both.

## Why does the APCA sign change?

APCA Lc is signed. Positive and negative values mark which colour is lighter, because APCA treats dark text on light backgrounds differently from light text on dark.

## Can I use more than 21 steps?

No. The range is 3 to 21.

## Does anything leave my browser?

No. Ramps, contrast and exports are computed and created on your device.
