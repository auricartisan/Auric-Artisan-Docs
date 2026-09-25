---
title: Analyzer — Colour, contrast and vision
description: Read the Contrast, Palette, Simulation and Before / After panels, and understand the WCAG contrast ratio and the APCA Lc value.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Colour, contrast and vision

Four sections deal with colour: **Contrast** measures every text colour pair on the page, **Palette** extracts the page's colours, **Simulation** shows the page through colour-vision filters, and **Before / After** previews the contrast fixes. The **Vision** view of the A11y+ panel adds a table of every pair under four colour-vision deficiencies (see [The accessibility engine](accessibility-engine.md)).

## Two ways to measure contrast

### The WCAG contrast ratio

WCAG 2.x measures contrast as a ratio between two colours' **relative luminance**, which is how much light a colour gives off on a scale from 0 (black) to 1 (white). Green counts most towards it and blue least, as in human vision. The ratio is the lighter luminance plus 0.05, divided by the darker plus 0.05. It runs from 1:1 (the same colour twice) to 21:1 (black on white), and it does not matter which colour is the text.

| What | Needs at least | Level |
| --- | --- | --- |
| Normal text | 4.5:1 | AA |
| Large text | 3:1 | AA |
| The visible edge of a control, focus indicators, meaningful graphics | 3:1 | AA |
| Normal text, enhanced | 7:1 | AAA |
| Large text, enhanced | 4.5:1 | AAA |

**Large text** means at least 24 CSS pixels, or at least 18.66 CSS pixels in bold. It is a size threshold, not a heading rule.

### The APCA Lc value

APCA, the Accessible Perceptual Contrast Algorithm, is a newer contrast model being developed for a future version of WCAG. It gives a **lightness contrast** value, written **Lc**, that tracks how people actually perceive contrast more closely than the ratio, especially for light text on dark backgrounds and thin type.

- Lc runs from 0 (no contrast) to a little over 100 for black on white.
- It has a direction: dark text on a light background gives a positive value, light text on a dark background a negative one. Compare the size of the number, not its sign.
- A larger number is needed for smaller or thinner text.

The Analyzer shows Lc beside the ratio for reference, for example "needs 4.5:1 · 12px · APCA Lc 22.9 (needs 90)". The "needs" value comes from this size-and-weight guide:

| Text size | Normal weight | Bold (700 and above) |
| --- | --- | --- |
| 24px and above | Lc 60 | Lc 45 |
| 18px to under 24px | Lc 75 | Lc 60 |
| 16px to under 18px | Lc 90 | Lc 75 |
| Under 16px | Lc 90 | Lc 90 |

> **Note:** APCA is advisory. It is not part of any current conformance requirement, so it never affects a pass, a fail or a score. Use it for judgement calls, and use the WCAG ratio for compliance.

## The Contrast section

The Contrast section lists every text colour pair the page actually paints, measured against its effective background. Semi-transparent colours are blended with what is behind them first, because that blend is what a reader sees.

### Blocks in the section

| Block | What it shows |
| --- | --- |
| **What is contrast?** | A short explanation of the ratio and the AA, AAA and FAIL labels |
| **Statistics (unique pairs)** | Counts of **Failing**, **AA Pass** and **AAA Pass** pairs |
| **Pair Count Breakdown** | Raw, duplicate, unique, shared and same-colour pair counts, and total fail occurrences |
| **Impact-Based Contrast Score** | The section's score, with text, UI and decorative failures counted separately |
| **Rendered Scene Contrast** | When canvas or rendered layers were sampled: scene samples, low-contrast regions, contrast range and penalty |
| **Detected Brand Colors** | The page's dominant colours. Suggested fixes keep these where they can and adjust the text or UI colour instead. |
| **Contrast Pairs** | Every pair, grouped as **Failing Combinations**, **AA Passes** and **AAA Passes** |
| Live page preview | The analysed page, with reload, open in a new tab, zoom and full-screen controls |

The **Pair Count Breakdown** lists **Raw candidate pairs**, **Duplicate pairs removed**, **Unique pairs retained**, **Shared across ≥2 pages**, **Same-colour (no contrast)** and **Total fail occurrences**. A pair from a shared stylesheet is counted once, with the pages it appears on, not once per page.

### How the section is scored

The Contrast score starts at 100 and loses points for each failing pair, weighted by what it is: text failures count most (×12), then interface components (×9), then decorative colour (×3). Critical failures and low contrast in the rendered scene cost extra. The **Why this score?** box shows the breakdown.

### Read a pair

Each pair shows:

- the ratio and its grade, for example "4.6:1 AA", and what it needs ("needs 4.5:1", or "needs 3:1 · large" for large text);
- the element type and a sample of its text;
- a sentence such as "Text colour #15803d is rendered on its effective background #ecf8f1 (e.g. `<span>`). Ratio 4.6:1 meets WCAG AA for normal text (AA needs 4.5:1)."

A failing pair also offers a suggested replacement colour. Select it ("Click to copy fix") to copy the corrected colour. The suggestion keeps your hue and changes only the lightness, so the result still looks like your brand.

### What the section does not measure

- **Text over gradients, photographs and video.** There is no single background colour, so no honest ratio exists. The accessibility engine reports these as needs review.
- **Text nobody can see.** Empty layout boxes, decorative bars and hidden controls are skipped.

## The Palette section

The Palette section extracts the colours the page uses and generates accessible alternatives.

| Block | What it shows |
| --- | --- |
| **What is this?** | A short explanation. Select any swatch to copy its hex code. |
| **Extracted Dominant Colors** | The most-used colours, with a count |
| **Theme Mode Detection** | Whether light, dark or both modes were detected, with the signals and colour references counted |
| **All Text Colors** and **All Background Colors** | Every text and background colour found |
| **Fonts** | The font families the page uses |
| **Export as CSS** and **Export as JSON** | Download the extracted palette as `palette.css` or `palette.json` |
| **CVD Previews** | The palette under deuteranopia, protanopia, tritanopia and achromatopsia |
| **Color Usage Frequency** | Each colour with how many times it is used, split into computed styles and colours written in the HTML |
| **Generated Accessible Palettes** | Twelve AA-tuned palettes: Complementary, Triadic, Split-Comp and Analogous, three of each |

Select **Save** on a generated palette to keep it in the **Workspace** section's **Saved Palettes** list.

If you open the Analyzer with a palette sent from your library, the Palette section shows that palette's contrast audit even before a page has been analysed.

## The Simulation section

The Simulation section shows the analysed page through colour-vision and low-vision filters, so you can see whether information carried by colour survives.

The panel explains that about 8% of males and 0.5% of females have some form of colour blindness. Choose a **Vision Type**:

| Vision Type | What it shows |
| --- | --- |
| **Normal Vision** | The page unfiltered |
| **Deuteranopia** | No working green-sensitive cones: reds and greens are hard to tell apart |
| **Protanopia** | No working red-sensitive cones: reds look darker and merge with greens |
| **Tritanopia** | No working blue-sensitive cones: blues and yellows are confused |
| **Achromatopsia** | No colour at all: the page in greyscale |
| **Low Vision** | A slight blur with reduced saturation |

The live preview has buttons to reload, open the page in a new tab, zoom out, zoom in and go full screen. The active filter is named under the preview.

A strip at the top says how the preview is running, for example "Live preview — This page is on our origin, so it runs here exactly as it does for a visitor."

### When the page will not embed

Many sites send headers that forbid other sites from showing them in a frame. The preview then shows **Couldn't embed this page** and explains that the site is blocking embedding with X-Frame-Options or a Content-Security-Policy frame-ancestors rule. You have four choices:

- **Run in browser** opens a real pop-up window with the page as it was captured, with the active filter applied. It works whatever the site's framing policy. Allow pop-ups for auricartisan.com if nothing opens.
- **Open in new tab** opens the live site, without a filter.
- **Try again** reloads the preview.
- **View CSP setup** opens the **CSP Setup** section, which explains how a site you own can allow Auric Artisan to embed it. See [Fix and preview](fix-and-preview.md).

These filters are quick previews. For the full range of conditions, severities and models, use the [Vision Lab](../../vision-simulation/README.md).

## The Before / After section

Before / After shows the page as it is beside the page with the Analyzer's contrast fixes applied, so you can judge the fixes before you change your CSS.

- **BEFORE (Original)** and **AFTER (Fixed)** previews sit side by side under **Original vs. Fixed**.
- **Applied Fixes** lists every colour change, with **Locate** to find the element and **Highlight all** to mark them all.
- **Score Comparison** shows the score now and the estimated score after the fixes.
- **Regression Check (after applying fixes)** is a list to tick through by hand after you apply the fixes to your real site: the page still loads without errors, critical user paths still work, keyboard navigation still works, the mobile breakpoint is still responsive, performance has not regressed, the visual layout looks correct, and the score went up or stayed the same. **Mark all validated** ticks them all.

If every pair already passes, the section says "No fixes needed" and "All contrast pairs pass WCAG requirements. Your colors are accessible!"

## A practical workflow for colour

1. Run an audit with **Colour contrast**, **Palette** and **Vision simulation** switched on, or apply the **Colour and vision** layout in Advanced mode.
2. In **Contrast**, open **Failing Combinations** and note which components the failing pairs belong to.
3. Copy a suggested colour, or take it to the [Contrast Checker](../../contrast-checker/README.md) to adjust it by hand.
4. Check **Before / After** to see the fixes in place.
5. Look at the page under **Protanopia**, **Deuteranopia** and **Achromatopsia** in **Simulation**, and make sure no information is carried by colour alone.
6. Check both your light and dark themes: a colour that passes on one often fails on the other.
