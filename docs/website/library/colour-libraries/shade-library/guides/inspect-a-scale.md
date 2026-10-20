---
title: Shade Library — Inspect a scale
description: Read the Inspect tab: token strip, shade summary, token contrast ladder and each token's values.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Inspect a scale

Open a scale with **Inspect**, by selecting the card, with `Enter` or `Space` on a focused swatch, with **Open a random scale**, or from a share link. Until then the tab shows **No shade system selected**.

## The token strip

One column per token, labelled with the token name and a descriptive colour name — for example **500 - soft vivid orange** — and the hex code. Select a column to copy its hex.

## Shade summary

The badge gives the scale's profile:

| Badge | When |
| --- | --- |
| **Neutral** | Average chroma below 0.035. |
| **Hue Shift** | Its hues span more than 35°. |
| **Light** | Average lightness above 0.72. |
| **Deep** | Average lightness below 0.38. |
| **Balanced** | Anything else. |

The badges are checked in that order, so a scale is **Neutral** before it can be **Hue Shift**, and so on.

| Row | Meaning |
| --- | --- |
| **Shade ID** | For example `shade_000000`. |
| **Global index** | The scale's number. |
| **Method** | For example **Material Like**. |
| **Base** | The base colour the scale is built around. |
| **Tokens** | Number of steps. |
| **Avg L (OKLCH)** | Average lightness, 0 to 1. |
| **Avg chroma** | Average OKLCH chroma. |
| **Hue span** | Widest hue difference between two tokens. |
| **Score** | The quality score recorded for the scale. |
| **Auto AA tokens** | How many tokens reach 4.5:1 with automatic text (near-black on light tokens, white on dark ones), for example **4 / 7**. All tokens is good; 70% or more is a warning; less is poor. |
| **Min adjacent contrast** | The lowest contrast between two neighbouring tokens — how close the two most similar steps are. |

## Token contrast ladder

Each token with its hex and its contrast with automatic text, for example **500 #FF724C 2.71 : 1 auto text**. Automatic text is near-black (`#111111`) on tokens whose luminance is above 0.5, and white otherwise. Use the ladder to decide which steps can hold body text (4.5:1 or more), large text (3:1 or more), or should be used only as fills.

## Quick export

**Copy HEX**, **Copy CSS vars**, **Copy SCSS**, **Copy Tailwind**, **Download JSON**, **Download SVG**, **Download PNG**, **Save to library** / **Unsave**, **Copy share link** and **Design tokens…**. See [Copy, export and share](copy-export-and-share.md).

## One card per token

Headed **Token** and the name and hex, for example **Token 500 - #FF724C**, with a badge of its contrast on white and on black. Rows: **HEX**, **RGB**, **OKLCH**, **CIE L\*a\*b\***, **WCAG vs white**, **WCAG vs black**, and buttons to copy the hex and `rgb()` value.

## Example

The first scale, **Material Like #FF724C #00001**, has seven tokens: `50`, `100`, `300`, `500`, `700`, `900` and `950`. Its ladder shows `50`, `100`, `900` and `950` well above 4.5:1 with automatic text, while `300`, `500` and `700` fall below it — those middle steps are for fills, borders and large accents, not body text.
