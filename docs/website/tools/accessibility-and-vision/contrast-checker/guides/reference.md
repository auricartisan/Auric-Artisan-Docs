---
title: Contrast Checker — Reference
description: Every control, input, threshold, output, message and keyboard behaviour of the Contrast Checker.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Contrast Checker reference

## Controls

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Text colour** swatch | Opens the system colour picker; writes uppercase hex into the field | Any colour | `#1a1400` |
| **Text colour** hex field | Typed or pasted text colour | 3- or 6-digit hex, with or without `#` | `#1A1400` |
| Swap button | Exchanges text and background | — | — |
| **Background colour** swatch | Opens the system colour picker | Any colour | `#f7f3e6` |
| **Background colour** hex field | Typed or pasted background colour | 3- or 6-digit hex, with or without `#` | `#F7F3E6` |
| **Make it pass AA** | Moves the text colour to the nearest value that reaches 4.5:1 | Shown only when body text fails AA | — |
| **Copy link** | Copies the address, which carries both colours | — | — |

The swatches are your browser's own colour input, not the site's custom colour picker, so the swatch always shows the value that is being graded.

## Outputs

| Output | What it shows |
| --- | --- |
| **Contrast ratio** | The WCAG 2.1 ratio to two decimals, from 1.00:1 to 21.00:1. Shows a dash until the first grading. |
| Grade badges | **Pass** or **Fail** for each of the five thresholds below |
| Status line | The result of **Make it pass AA** or **Copy link** |
| Preview | Your pair as large text, a body-text paragraph and an "Interface element" chip |

## Thresholds

| Row | Threshold |
| --- | --- |
| **Body text · AA** | 4.5:1 |
| **Body text · AAA** | 7:1 |
| **Large text · AA** | 3:1 |
| **Large text · AAA** | 4.5:1 |
| **UI & graphics** | 3:1 |

A ratio equal to a threshold passes. Badges use the exact ratio; the display is rounded to two decimals. Large text means at least 18.66px bold or 24px regular.

## Status messages

| Message | When |
| --- | --- |
| "Adjusted text to #RRGGBB (N.NN:1)." | After **Make it pass AA** |
| "Share link copied." | After **Copy link**, when the clipboard accepted it |
| The full address | After **Copy link**, when the clipboard is unavailable |

## Address parameters

| Parameter | Meaning | Example |
| --- | --- | --- |
| `fg` | Text colour, hex without `#` | `fg=1A1400` |
| `bg` | Background colour, hex without `#` | `bg=F7F3E6` |

Invalid values are ignored and the default is used for that colour. The address updates shortly after each change, replacing the current history entry.

## Keyboard and screen readers

- `Tab` order: text swatch, text hex field, swap button, background swatch, background hex field, then the action buttons.
- The focus ring is drawn around the whole hex row, so you can always see which field you are in.
- The ratio is a polite live region: a screen reader reads the new ratio after a change without interrupting.
- The status line is a status region, so the outcome of both buttons is announced.
- The swap button is labelled "Swap text and background colours".
- The questions under **Questions people actually ask** are native disclosures: press `Enter` or `Space` to open one.

There are no custom keyboard shortcuts on this page.

## Layout

- Wide screens: controls and result side by side, preview across the full width below.
- Under 720 pixels: one column (controls, result, preview), with the swap button turned a quarter turn.
- The page follows the site's light or dark theme. The preview always shows your own two colours.

## Content below the tool

| Section | Contents |
| --- | --- |
| **What the numbers mean** | 4.5:1, 3:1, 7:1 and the definition of large text |
| **Questions people actually ask** | Four questions: the ratio you need, large text, readability, and disabled controls and logos |
| **Next** | **Check a whole page** (the Analyzer), **Build a palette** (Basic tools) and **Learn the rules** (the Learn library) |
