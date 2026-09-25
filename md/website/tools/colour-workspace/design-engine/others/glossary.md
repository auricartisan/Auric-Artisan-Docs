---
title: Design System Generator — Glossary
description: Plain-language definitions of the terms used in the Design System Generator documentation.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Glossary

| Term | Meaning |
| --- | --- |
| APCA / Lc | Accessible Perceptual Contrast Algorithm, a contrast method proposed for WCAG 3; Lc is its lightness-contrast value, shown here without its sign. |
| Brief | The set of inputs (industry, style, target and overrides) a system is generated from. |
| Chroma | How colourful a colour is; in OKLCH, the C value. |
| Colour mode | Whether the system builds light roles, dark roles or both. |
| Contrast target | The minimum WCAG contrast body text must reach: 3:1, 4.5:1 or 7:1. |
| Density | How compact the type and spacing are. |
| Design system | A shared set of design decisions (colours, type, spacing and more) and the components built from them. |
| Design token | One named design decision stored as data, such as `--space-4: 16px`. |
| Deterministic | Always producing the same output from the same inputs. |
| Gamut mapping | Reducing a colour's chroma until it can be shown in sRGB. |
| Harmony | The positions of the secondary and accent hues relative to the primary. |
| Headroom | How far body text's contrast clears the target. |
| Hierarchy | Body, muted and subtle text reading as three distinct levels. |
| Modular scale | Font sizes that grow by a fixed ratio, such as 1.25. |
| Neutral ramp | A ramp of greys, here tinted slightly towards the brand hue. |
| OKLCH | A perceptual colour space with lightness (L), chroma (C) and hue (H), where equal steps look roughly equal. |
| Ramp | A series of steps of one hue from light to dark, such as 50 to 950. |
| Ramp shape | How far a ramp travels in lightness (span) and where its chroma peaks (peak). |
| Role | A token named for its job, such as `text-muted` or `surface`, rather than its colour. |
| Seed | The brand colour a system's hue and chroma come from. |
| Semantic colour | A colour with a fixed meaning: success, warning, danger or info. |
| Token naming | The prefix and case (kebab, camel, snake, Pascal) applied to every token name. |
| W3C Design Tokens | A standard JSON format for tokens, readable by Figma Variables and Tokens Studio. |
| WCAG contrast ratio | The luminance ratio between two colours, from 1:1 to 21:1, used by WCAG 2.x. |

## Related

- [Supporting material](README.md)
- [Basic Color Tools glossary](../../basic-colour-tools/others/glossary.md) for general colour terms
