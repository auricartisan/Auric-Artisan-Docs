---
title: Browser extension — Check tools
description: The tools in the Check space — Contrast, Vision, Audit and Findings — and the rules the audit applies.
product: Browser extension › Check
updated: 2026-09-25
---

# Check tools

The **Check** space holds the accessibility tools. **Contrast** checks any colour pair and fixes it. **Vision** shows the live page through twelve simulations. **Audit** checks the current page against WCAG 2.2, and **Findings** gathers everything wrong into one list.

## Files in this folder

| Page | What it covers |
|---|---|
| [Contrast](contrast.md) | Check a pair in WCAG and APCA, read the verdict, and find the nearest passing colour |
| [Vision](vision.md) | Colour-vision and low-vision simulations on the live page, side by side, and capture |
| [Audit](audit.md) | Run an audit, read the contrast results, outline problems on the page, and export |
| [Audit rules](audit-rules.md) | The 80 rules of the accessibility engine, by category, with their WCAG criteria |
| [Findings](all-findings.md) | The pooled list of problems, by severity, with actions for each |

## Key ideas

- **WCAG contrast ratio** compares the relative luminance of two colours, from 1:1 (no contrast) to 21:1 (black on white). WCAG 2.2 asks for 4.5:1 for body text and 3:1 for large text at level AA, and 7:1 and 4.5:1 at AAA.
- **APCA Lc** (Accessible Perceptual Contrast Algorithm, lightness contrast) is the contrast method in the WCAG 3 drafts. It gives a signed score, where a higher absolute value reads more easily, and its guidance depends on font size and weight.
- **Large text** means at least 24 px, or at least 18.66 px when bold.

The [glossary](../../others/glossary.md) defines these and other terms, and [Limits and accuracy](../../others/limits-and-accuracy.md) explains what the checks can and cannot tell you.
