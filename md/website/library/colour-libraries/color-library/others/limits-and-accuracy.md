---
title: Color Library — Limits and accuracy
description: What the Color Library's figures measure, how precisely, and what they are not.
product: Website › Library › Colour libraries › Color Library
updated: 2026-09-25
---

# Limits and accuracy

## What is measured

- **Contrast ratios** use the WCAG 2 formula against pure white and pure black. They are exact for those two backgrounds, rounded to two decimals. They say nothing about any other background.
- **Relative luminance, Lab, OKLab, OKLCH and HSL** are standard conversions from each colour's sRGB value, assuming a D65 white point.
- **CMYK** is a simple arithmetic conversion. It is not a print separation and does not account for paper, ink or a print profile. Use a proper colour-managed workflow for print.
- **Colour-blindness values** are simulations of complete protanopia, deuteranopia and tritanopia. People with milder colour vision deficiencies see something between the original and the simulation. Simulations are a design aid, not a diagnosis.

## How distance is measured

- **ΔE** in the Color Library is CIE76: the straight-line distance in Lab. It is fast enough to recompute as you type, and the page names it so it is not mistaken for a newer formula. CIE76 over-states differences between very saturated colours compared with CIEDE2000, so treat the words **a close match** and **visibly different** as guides.
- The 2.3 threshold for **indistinguishable** is a commonly quoted just-noticeable difference for CIE76, not a guarantee for every viewer or screen.

## What the labels are

The emotion, art movement, mood, design usage and design tag labels were assigned when the atlas was generated. They are descriptive aids for browsing. They are not survey data and do not describe how any particular audience responds to a colour.

## The atlas is a sample

The atlas holds 8,192 colours, not every colour. A colour you need may sit between two atlas colours. Counts and percentages (for example "36.6% of colours are readable on white") describe the atlas, not all possible colours.

## Your screen

What you see depends on your display, its settings and the room's light. The numbers are the same on every screen; the swatches are not. Colours you enter outside sRGB are moved to the nearest sRGB colour before matching, and the page tells you when it does this.

## What the Color Library is not

- It is not an accessibility audit. A passing contrast ratio is one requirement among many; text size, weight, focus styles and context also matter.
- It is not a certified colour measurement. Nothing here replaces a spectrophotometer or a calibrated proof.
