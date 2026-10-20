---
title: Contrast Checker — Check a colour pair
description: Enter a text and background colour, read the WCAG 2.1 ratio, and work out which of the five grades applies to what you are colouring.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Check a colour pair

## Enter the colours

Each colour has two controls that stay in step: a colour swatch and a hex field. Use the swatch to explore and the field to paste a value from a stylesheet or a design file.

| Control | What it does | Starts at |
| --- | --- | --- |
| **Text colour** swatch | Opens your system's colour picker. Moving it writes the hex into the field and re-grades as you go. | `#1a1400` |
| **Text colour** hex field | Accepts a typed or pasted hex value and re-grades on every keystroke | `#1A1400` |
| Swap button | Exchanges the two colours and re-grades | — |
| **Background colour** swatch | The same picker for the background | `#f7f3e6` |
| **Background colour** hex field | The same typed entry for the background | `#F7F3E6` |

### What the hex fields accept

Hex only, in three or six digits, with or without a leading `#`. These are all the same colour to the checker: `#1A1400`, `1A1400`. Three digits are expanded, so `#f00` and `f00` both mean `#FF0000`.

When you leave a field, a value it understood is rewritten in full: uppercase, six digits, with a `#`. Anything else is not accepted: `rgb()`, `hsl()`, colour names such as `rebeccapurple`, and eight-digit hex with an alpha channel.

> **Important:** While a field holds something it cannot read, such as a half-typed `#1A`, the checker grades pure black in its place (for the text) or pure white (for the background). The ratio you see then is not yours. Finish typing, or press `Tab` to leave the field, before you trust the number.

## Read the ratio

The large number under **Contrast ratio** is the WCAG 2.1 contrast ratio, to two decimal places, for example **4.53:1** or **21.00:1**.

- **Range:** from 1:1 (two identical colours) to 21:1 (black on white).
- **Updates:** on every keystroke and every movement of a swatch. There is no Calculate button.
- **Direction:** none. Dark on light and light on dark give the same number, so swapping never changes it.

### How the ratio is worked out

WCAG measures each colour's **relative luminance**, which is how much light it gives off on a scale from 0 (black) to 1 (white), with green counting most and blue least, as in human vision. The ratio is the lighter luminance plus 0.05, divided by the darker luminance plus 0.05. This is the sRGB formula in WCAG 2.1, and it is the number an auditor will quote.

### Rounding at the threshold

The badges compare the exact, unrounded ratio with each threshold, but the number on screen is rounded to two decimals. A pair measuring 4.4996 prints **4.50:1** beside a **Fail** badge for body text AA. The badge is right. If a pair lands that close, treat it as failing and give yourself some margin.

A ratio exactly equal to a threshold passes: a true 4.5 reads **Pass**.

## Read the five grades

Every pair is graded against five thresholds at once, so you never have to choose a mode first.

| Row | Threshold | Covers |
| --- | --- | --- |
| **Body text · AA** | 4.5:1 | Ordinary running text at Level AA, the level most laws and contracts point at |
| **Body text · AAA** | 7:1 | Body text at Level AAA, worth aiming for on long-form reading |
| **Large text · AA** | 3:1 | Text at or above the large-text size, at Level AA |
| **Large text · AAA** | 4.5:1 | Large text at Level AAA |
| **UI & graphics** | 3:1 | Interface components, focus indicators and meaningful graphics, against what sits next to them |

### Which row applies to you

Choose the row by what you are colouring, not by which badge is greenest.

- **Paragraphs, labels, table cells, help text:** body text. Use the 4.5:1 row, with 7:1 as a stretch goal.
- **Headings and display type:** large text, but only if the size qualifies (below).
- **Input borders, toggle states, icon buttons, focus rings, the meaningful parts of a chart:** the **UI & graphics** row at 3:1. Measure against the colour actually next to the component, which may not be the page background.

### What counts as large text

At least 18.66 pixels in bold, or at least 24 pixels otherwise. It is a size threshold, not a heading rule: a 20-pixel heading in a light weight is body text as far as WCAG is concerned, and must reach 4.5:1.

### What is out of scope

WCAG 2.1 exempts inactive (disabled) controls, pure decoration, text that is part of a logo, and text inside a picture of something else. The checker grades whatever pair you give it, so a **Fail** on a disabled button's label is not automatically a defect. Everything a person has to read or operate is in scope.

## Use the preview

The panel under the controls is painted in your pair and holds:

- a large line, "Large text looks like this", at the large-text size;
- a body-text paragraph at a realistic line length, so you can judge the pair over several lines;
- an "Interface element" chip with a border in the text colour, so you can see the pair as a control outline.

Look at it. The ratio is a floor, not a verdict. The WCAG 2.1 formula ignores font weight, ignores size beyond the large-text threshold, and does not model the way light text on a dark background appears to spread. A thin weight at 4.6:1 can be tiring to read; a heavy weight at 4.3:1 can look crisp and still fail an audit.

The preview always shows your two colours, in both light and dark site themes.

## A check in five steps

1. Enter the text colour.
2. Enter the background colour.
3. Read the ratio.
4. Find the row that matches what you are colouring, and read its badge.
5. If it fails, see [Make a pair pass](make-a-pair-pass.md). Either way, [share the pair](share-a-pair.md) if someone else needs to see it.
