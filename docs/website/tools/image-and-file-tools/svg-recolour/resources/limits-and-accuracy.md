---
title: SVG Recolour — Limits and accuracy
description: What SVG Recolour finds and writes, how precise its figures are, and what it does not hold.
product: Website › Tools › Image and file tools › SVG Recolour
updated: 2026-09-25
---

# Limits and accuracy

## What is found and written

- Eight paint properties: `fill`, `stroke`, `stop-color`, `flood-color`, `lighting-color`, `color`, `solid-color` and `text-decoration-color`.
- In presentation attributes, style attributes and `<style>` elements.
- Colours written as hex (with or without alpha), shorthand hex, `rgb()`, `rgba()`, `hsl()`, `hsla()` and all 148 CSS names.
- The count beside each colour is the number of occurrences, and the written count is the number actually rewritten. The colour list, the **Mapping** tab, the report and the exported file all use the same list, so they always agree.
- Every change is planned from the original file before anything is written, so no change can be caught by another.

## What is not found or not changed

| Item | What happens |
|---|---|
| `currentColor` and other inherited keywords | Counted and left alone; the colour comes from outside the file |
| `none`, `transparent`, `url()` references | Counted and left alone |
| Colours in other CSS functions or variables (`oklch()`, `lab()`, `var()`) | Not recognised, not counted, not changed |
| Embedded raster images | Not read; their pixels are not changed |
| Colours set by CSS outside the file | Not visible to the tool |

## Precision and choices

| Item | Detail |
|---|---|
| Colour values | Parsed to 8-bit sRGB; an unrecognised value is never guessed as black |
| Alpha | Kept for `rgba()` and `hsla()` with **Keep the source form**; lost for hex with alpha when changed |
| Three-digit hex | Written back as six digits |
| Grouping | Only identical colours share a row; near-identical colours are kept apart |
| Colour names | The nearest CSS name by CIEDE2000, prefixed "near"; a label, not a classification |
| Harmony angles | A colour-wheel convention, applied in OKLCH with lightness and chroma kept |
| Contrast | WCAG 2.2 ratio, exact; APCA-W3 0.1.9 with all its constants |
| CIEDE2000 | ISO/CIE 11664-6:2014, agreeing with published test data to within 0.00004 |
| Colour-vision simulation | Machado, Oliveira and Fernandes (2009), full severity, in linear light; no milder forms |

## Limits

- One file at a time; there is no batch mode.
- The previews have active content removed; the exported file does not.
- Only the `<svg>` element is exported: anything before it, such as an XML declaration or DOCTYPE, is not carried across, and the browser may normalise small formatting details.
- Nothing is stored between visits.

## What it is not

SVG Recolour changes colour values in the markup. It does not edit shapes, text or structure, does not sanitise files for publishing, and does not judge whether a palette is attractive.
