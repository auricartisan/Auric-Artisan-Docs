---
title: Browser extension — The popup
description: A tour of the popup — header, search, spaces, the site chip, tool chips, sizes, the separate window and keyboard movement.
product: Browser extension › Surfaces
updated: 2026-09-25
---

# The popup

The popup is the workspace that opens from the toolbar icon or with `Alt` + `Shift` + `A`. It closes when you click outside it. Everything in it is also available in the [side panel](side-panel.md) and in a separate window.

## Header

- **Auric Artisan** wordmark (with the line "Colour intelligence studio"): Opens auricartisan.com in a new tab
- Search field (**Search tools, colours, settings**): Finds any tool, setting or auricartisan.com page. Press `/` or `Ctrl` + `K` to focus it. See [Search](search.md).
- **Open the side panel**: Docks the workspace in the browser's side panel or sidebar, then closes the popup. Hidden when you are already in the side panel.
- **Open in its own window**: Opens the workspace in a separate, resizable 620 × 700 window and closes the popup. Hidden at the Compact popup size.
- **Switch between light and dark**: Flips the theme. Settings › Appearance adds a third choice, System.
- **Settings**: Opens the two-pane Settings view. See [Settings](../settings/README.md).

## Spaces bar

Below the header:

- **Home**, **Colour**, **Check**, **Code** and **Saved**. Each is a tab; use the arrow keys, `Home` and `End` to move between them when one has focus.
- **The site chip** names the site the page tools will act on, for example `fieldnote.app`. It reads **No page** on pages extensions cannot reach, such as browser settings pages and the web stores. Hover it for the reason.
- **Take the tour** (the **?** button) replays the five-step tour.

## Tool chips

When you open a space, a row of chips shows its tools. Choose a chip to switch tools. Chips can carry a count badge. The space remembers the tool you last used in it, so returning to Colour reopens the tool you left.

| Space | Chips | Also in this space |
|---|---|---|
| **Colour** | Picker, Page palette, Image, Gradient, Mix | Harmony, Scale and Convert open from links inside the Picker, or from search |
| **Check** | Contrast, Vision, Audit, Findings | — |
| **Code** | Inspect, Tokens, Snippets | — |
| **Saved** | Library, History | On the web opens from search |

Harmony, Scale and Convert each have a **Picker** back button at the top that returns you to the Picker.

## Sizes

Settings › Appearance › **Popup size** sets the popup's size:

| Size | Width × height |
|---|---|
| Compact | 460 × 520 |
| Standard (the default) | 560 × 600 |
| Large | 760 × 600 |

Browsers cap a popup's size, so Large may be limited by your browser. The side panel and the separate window have no fixed size.

## Moving around with the keyboard

- `/`: Focus the search field (when you are not typing in a field)
- `Ctrl` + `K`: Focus the search field, from anywhere, and close Settings if it is open
- `Esc`: Steps back one level: closes an open colour picker panel first, then Settings, then clears a search, then returns from a tool to Home
- Arrow keys, `Home`, `End`: Move between spaces, or between Settings sections

## Toasts

Short messages appear at the bottom of the popup to confirm an action, such as "Saved to library", "Palette saved" or "Settings reset", or to explain a failure, such as "Could not scan".

## The toolbar badge

The number on the toolbar icon is the count of colours in your library. It shows up to 99, then "99+". It is empty when the library is empty.

## Related pages

- [Home](home.md)
- [Search](search.md)
- [Side panel](side-panel.md)
