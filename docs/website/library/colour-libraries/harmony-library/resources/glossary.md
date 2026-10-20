---
title: Harmony Library — Glossary
description: Definitions of the terms and all 23 colour-theory schemes used in the Harmony Library.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Harmony Library glossary

## Terms

| Term | Meaning |
| --- | --- |
| Adherence | How closely a harmony's actual hues keep to its scheme's canonical angles, from 0% to 100%. |
| Base | The colour a scheme is built around. Other colours are placed at angles from its hue. |
| Canonical angles | A scheme's ideal hue offsets from the base, such as 120° and 240° for triadic. |
| Colour wheel | Hues arranged in a circle from 0° to 360° (red, yellow, green, cyan, blue, magenta and back to red). |
| Contrast ratio | The WCAG 2 lightness-difference measure between two colours, from 1:1 to 21:1. 4.5:1 is AA for body text. |
| Family | A group of related schemes: complementary, polyadic, analogous, monochromatic or compound. |
| Fit | In **What harmony is this?**: 1 minus the average angle error divided by 60°, never below 0. |
| Harmony id | `har_` followed by the harmony's number in base 36. |
| Hue span | The widest angle between two of a harmony's hues. |
| Role | What a colour does in its scheme: base, complement, ally, accent and so on. |
| Scheme (method) | One of the 23 rules for placing hues. |

## The 23 schemes

| Scheme | Family | Colours | Canonical angles | Description (as the page gives it) |
| --- | --- | --- | --- | --- |
| complementary | complementary | 2 | 180° | Base hue and its 180° opposite — the strongest possible contrast pair. |
| split_complementary | complementary | 3 | 150°, 210° | Base plus two hues flanking its complement — softer than complementary. |
| double_complementary | complementary | 4 | 30°, 180°, 210° | Two pairs of complements offset by a small angle. |
| triadic | polyadic | 3 | 120°, 240° | Three hues spaced 120° apart — vibrant and well-balanced. |
| triad_shifted | polyadic | 3 | 120°, 240° | Triadic with chroma + lightness shifts for hierarchy. |
| tetradic | polyadic | 4 | 60°, 180°, 240° | Two complementary pairs forming a rectangle on the wheel. |
| square | polyadic | 4 | 90°, 180°, 270° | Four hues spaced 90° apart — bold and evenly weighted. |
| pentadic | polyadic | 5 | 72°, 144°, 216°, 288° | Five hues equally spaced (72°). |
| hexadic | polyadic | 6 | 60°, 120°, 180°, 240°, 300° | Six hues at 60° intervals — full color-wheel coverage. |
| analogous_3 | analogous | 3 | −24°, 24° | Three neighbouring hues — harmonious, low-tension. |
| analogous_5 | analogous | 5 | −44°, −22°, 22°, 44° | Five neighbouring hues for richer analogous palettes. |
| analogous_7 | analogous | 7 | −54° to 54° in 18° steps | Seven analogous hues — long ramp suitable for illustration. |
| accented_analogous | analogous | 4 | −24°, 24°, 180° | Three analogous hues plus one complementary accent. |
| monochromatic_3 | monochromatic | 3 | 0° | Three lightness/saturation steps of one hue. |
| monochromatic_5 | monochromatic | 5 | 0° | Five-step single-hue ramp. |
| monochromatic_7 | monochromatic | 7 | 0° | Seven-step single-hue ramp — UI-friendly tonal scale. |
| shades | monochromatic | 5 | 0° | Five-step ramp from base toward black. |
| tints | monochromatic | 5 | 0° | Five-step ramp from base toward white. |
| neutral | monochromatic | 5 | 0° | Desaturated greyscale tinted toward the base hue. |
| compound | compound | 5 | 24°, 180°, 156°, 210° | Base + warm/cool shifts + complement + accent. |
| warm_cool | compound | 2 | 180° | Base paired with its temperature-flipped counterpart. |
| golden_ratio | compound | 5 | 137.5°, 275.01°, 52.51°, 190.01° | Hues rotated by the golden angle (137.5°). |
| fibonacci_hue | compound | 5 | 34.4°, 68.8°, 103.1°, 171.9° | Fibonacci-indexed golden-angle distribution. |

Analogous angles are measured from the middle colour. Monochromatic schemes keep one hue and vary lightness and saturation.
