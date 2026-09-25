---
title: Auric Artisan Studio — Accessibility of the Studio
description: Use the Studio's own screens with a keyboard, a screen reader, zoom, reduced motion and high-contrast themes.
product: VS Code extensions › Auric Artisan Studio
updated: 2026-09-25
---

# Accessibility of the Studio

An accessibility tool should be accessible itself. The Studio's own screens (the Overview, the Studio tab and the colour pickers) are built to meet WCAG 2.2 level AA. This page describes how to use them without a mouse, with a screen reader, and with high-contrast, zoom and reduced-motion settings. If you meet a barrier, it is a bug: report it through https://auricartisan.com.

## Keyboard

Every control can be reached and operated from the keyboard.

| Where | Keys | What they do |
| --- | --- | --- |
| Anywhere in a Studio screen | `Tab`, `Shift` + `Tab` | Move between controls |
| Studio rail | Arrow keys, `Home`, `End` | Move between spaces; the space opens as you move |
| A space's tab row (Color, Check) | Arrow keys, `Home`, `End` | Move between tools |
| Findings and Health tools | `/` | Jump to the search box and select its text |
| Findings and Health tools | `Escape` | Close an open picker, menu or tooltip; if none is open, clear the search |
| Swatches, finding rows, file rows and other tiles | `Enter`, `Space` | Activate, as a click would |
| Dropdown menus | `Down` or `Up` on the button, then arrow keys, `Home`, `End`; `Escape` | Open the menu, move through options; close and return to the button |
| Accent swatches (Settings › Appearance) | Arrow keys, `Home`, `End` | Move and select; on the custom swatch, `Enter` opens the picker |
| Colour picker hue and opacity bars | Arrow keys (`Shift` for steps of 10), `Page Up`, `Page Down`, `Home`, `End` | Change the value |
| Colour picker spectrum | `Left`, `Right` for saturation; `Up`, `Down` for brightness; `Shift` for steps of 10; `Home`, `End` | Change the colour |
| Studio colour picker pop-up | `Tab` | Stays inside the picker while it is open |
| Studio colour picker pop-up | `Escape` or **Done** | Close it and return focus to the swatch that opened it |
| Standalone colour picker beside the editor | `Escape` | Close it |

Keyboard changes in a picker are written to your file after you pause for about 0.6 seconds, so holding an arrow key does not create hundreds of edits.

VS Code's own keyboard support applies to everything VS Code draws: hovers (`Ctrl` + `K`, `Ctrl` + `I` shows the hover at the cursor), quick fixes (`Ctrl` + `.`), the Command Center list and the Project Issues tree.

## Focus

- Every interactive element shows a visible focus ring, in every theme.
- When a Studio screen refreshes (a scan result arrives, a filter changes, you switch tools), keyboard focus and text selection stay where they were.
- Closing a picker or menu returns focus to the control that opened it.
- `Escape` dismisses a tooltip without moving focus.

## Screen readers

- Controls have accessible names, and dropdowns report whether they are expanded and which option is selected.
- The rail and tab rows are real tab lists; the colour bars are real sliders that announce values such as `Hue 210 degrees` and `85 percent opaque`.
- Tooltips are attached to their control while visible, so their text is read as a description.
- Changes are announced politely without moving focus: tab changes (for example **Palette tab**), **Search focused**, **Search cleared**, new suggestions, updated scores (for example `Score 82 of 100, 42 findings`) and the results of actions such as copying a colour.
- The decorative before-and-after mock-ups in the Preview tool that deliberately show failing contrast are hidden from screen readers; the numeric verdicts next to them are read instead.
- In VS Code's own views, rows in the Project Issues tree and the **Auric: N in this file** status-bar item have full spoken labels, for example `serious WCAG 1.1.1 Non-text Content in src/index.html line 12`.

## Colour and contrast

- Every text colour and status colour in the dark and paper themes has been checked against the surfaces it sits on to hold at least 4.5:1.
- Pass, warning and fail colours are defined per theme and checked to hold 4.5:1.
- A custom accent colour is adjusted until its text reaches 4.5:1 on every surface, including its own tint. See [Appearance](appearance.md).
- Colour is never the only signal. Verdicts carry ✓ or ✕ and the words **Pass** or **Fail**; scores carry a number and a grade; severity carries a label; the Branding group carries a heart icon, the word **branding** and a border.

## High contrast and forced colours

- In VS Code's high-contrast themes (dark and light), the Studio uses the theme's own colours and borders instead of its own palette.
- When your operating system forces colours, for example Windows contrast themes, the Studio's screens follow the forced colours.

## Motion and zoom

- When your system asks for reduced motion, the Studio turns off its transitions and ambient animation.
- Interactive targets are at least 24 by 24 CSS pixels.
- The Studio reflows from a narrow sidebar to a full-width editor tab, and works with VS Code's zoom (`Ctrl` + `=` and `Ctrl` + `-`).

## Related

- [The Studio](studio.md)
- [The Overview view](overview-view.md)
- [Appearance](appearance.md)
