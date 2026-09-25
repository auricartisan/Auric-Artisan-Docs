---
title: Gradient Library — Inspect a gradient
description: Read the Inspect tab: the preview, twelve quick facts, the CSS, the colour stops, the generator metrics and quick exports.
product: Website › Library › Colour libraries › Gradient Library
updated: 2026-09-25
---

# Inspect a gradient

## Open a gradient

- Select a card, or focus it and press `Enter` or `Space`.
- Select **Open a random gradient**.
- Select a card on the **Saved** tab.
- Open a share link (see [Copy, export and share](copy-export-and-share.md)).

Before you open one, the tab says **No gradient selected** and describes what you will see.

## Preview and quick facts

At the top, a large preview of the gradient with its name and a line "scheme / interpolation space / easing", and a **Copy CSS** button.

Beside it, twelve quick facts:

| Fact | Meaning |
| --- | --- |
| **Type** | **Linear**. Every gradient in the collection is linear. |
| **Angle** | The direction in degrees, as in CSS (`0deg` points up, `90deg` to the right). |
| **Stops** | Number of colour stops. |
| **Method** | How the colours were chosen. |
| **Complexity** | **Simple**, **Detailed** or **Extreme**. |
| **Score** | Quality score from 0 to 1, three decimals. |
| **Space** | The interpolation space used when the gradient was generated. |
| **Easing** | The easing curve used between stops. |
| **Banding** | **Smooth**, **Subtle Compression** or **Visible Step Risk**. |
| **White min** | The lowest contrast ratio between white and any of 24 samples along the gradient. |
| **Black min** | The same against black. |
| **Hue** | The dominant hue in degrees. |

## CSS

The **CSS** card shows the gradient as a CSS value, for example:

```css
linear-gradient(0deg, #723c2d 0%, #7b3600 100%)
```

Buttons: **Copy CSS**, **Download CSS** (a CSS class) and **Download SVG**.

## Color Stops

Every stop, numbered from `01`, with a swatch, its hex code (select it to copy) and its position along the gradient as a percentage.

## Generator Metrics

Figures recorded when the gradient was generated. They appear a moment after the tab opens.

| Row | Meaning |
| --- | --- |
| **Scheme** | The scheme family. |
| **Interpolation** | The interpolation space. |
| **Easing** | The easing curve. |
| **Sample Count** | How many samples the gradient was measured with. |
| **Complexity Score** | A number behind the **Complexity** label; higher is more elaborate. |
| **DeltaE Mean** | The average colour difference between neighbouring samples. |
| **Uniformity** | A measure of how evenly the gradient changes. |
| **Banding** | The measured verdict. |
| **Seed** | The number the generator started from. |

## Quick Export

"Export this gradient or save it locally for this browser." Buttons: **Download JSON**, **Download Tailwind**, **Download PNG**, **Copy share link**, **Design tokens…** and **Save gradient** (or **Remove saved**). See [Copy, export and share](copy-export-and-share.md) and [Save gradients](save-gradients.md).

## Result

You know how the gradient is built, how it was measured, and how readable white and black are on it — and you have its CSS one click away.
