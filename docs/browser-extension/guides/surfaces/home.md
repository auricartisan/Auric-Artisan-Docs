---
title: Browser extension — Home
description: What Home shows — colour of the day, one-click actions for the current page, recent colours, Continue, pinned tools and links to auricartisan.com.
product: Browser extension › Surfaces
updated: 2026-09-25
---

# Home

Home is the first screen in the popup, the side panel and the separate window. It starts work on the current page in one click and brings back what you were doing.

## Colour of the day

A card at the top shows one colour, the same for everyone on a given date, with its date, HEX value, OKLCH value and nearest colour name.

- Choose the swatch or **Open in picker** to open it in the Picker.
- Choose the copy button to copy its HEX value.

## On this page

Four actions that do the work, not just open a tool. Each acts on the tab named in the site chip.

| Action | Subtitle | What happens |
|---|---|---|
| **Pick a colour** | Any pixel on screen | Opens the Picker and starts the screen eyedropper |
| **Inspect** | Styles, box, contrast | Opens Code › Inspect and starts selecting an element on the page |
| **Audit** | Contrast and WCAG | Opens Check › Audit and runs the audit |
| **Palette** | Every colour used | Opens Colour › Page palette and reads the page's colours |

In Firefox, **Pick a colour** opens the Picker, which explains that the screen eyedropper is not available. See [Picker](../colour/picker.md).

## Recent

Up to twelve of the colours you picked or copied most recently, newest first. Choose one to open it in the Picker. **History** opens the full list of 50. Until you pick a colour, this reads "Colours you pick or copy collect here."

## Continue

After you have used a tool, a **Continue** row names it and what you were doing, so one click takes you back. For example:

- Contrast: the pair and its ratio, such as `#1f1b14 on #d3af37 · 8.19 : 1, AA`;
- Picker: the colour and its nearest name;
- Scale: the base colour and scale type;
- Harmony: the base colour and harmony type.

## Pinned

Shortcuts to the tools you use most. The defaults are Colour Picker, Page Palette, Contrast Checker and Scale Generator.

1. Choose **Edit**. Every tool appears as a checkbox chip.
2. Tick the tools to pin, and untick the ones to remove. Up to 8 tools stay pinned; pinning a ninth drops the oldest.
3. Choose **Done**.

If you unpin everything, Home reads "Pin the tools you use most. Choose Edit."

## On auricartisan.com

Links that open in a new tab: **Collections**, **Accessibility Library**, **Learning Library** and **Documentation**.

## Related pages

- [The popup](popup.md)
- [Search](search.md)
- [Picker](../colour/picker.md)
- [Audit](../check/audit.md)
