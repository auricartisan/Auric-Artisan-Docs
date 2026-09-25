---
title: Browser extension — Getting started
description: Open the extension, learn the layout of the workspace, take the tour and complete a first task in each space.
product: Browser extension
updated: 2026-09-25
---

# Getting started

This page takes you from a fresh install to your first result in each part of the extension. If the extension is not installed yet, follow [Install](install/README.md) first.

## Before you start

- **Pin the icon.** Browsers hide new extensions behind a puzzle-piece or extensions menu. Pin **Auric Artisan** so its icon stays on the toolbar.
- **Use an ordinary web page.** Browsers do not let extensions run on their own pages, such as settings pages, the new-tab page, `chrome://` and `about:` addresses, or the extension stores. Page tools also cannot reach `file://` pages unless you allow file access for the extension in the browser. Open any normal `http` or `https` site to try the page tools.
- **Nothing on websites changes until you ask.** The website pickers and the custom right-click menu are off after install. You turn them on in Settings when you want them.

## Open the extension

You have three ways to open the same workspace:

| Where | How | Best for |
|---|---|---|
| The popup | Click the toolbar icon, or press `Alt` + `Shift` + `A` | Quick checks; it closes when you click elsewhere |
| The side panel (Chromium) or sidebar (Firefox) | Choose **Open the side panel** in the header, or open it from the browser's own side panel or sidebar menu | Longer sessions; it stays open while you browse |
| Its own window | Choose **Open in its own window** in the header | A resizable 620 × 700 window that stays open |

Installing the extension also opens auricartisan.com once, in a new tab.

## Take the tour

The first time you open the extension, a five-step tour starts:

1. **Search anything:** press `/` or `Ctrl` + `K` and type to find any tool, setting or page on auricartisan.com.
2. **Pick & convert:** the Colour space opens the Picker, which samples any pixel and reads it in twelve formats.
3. **Inspect the page:** Code › Inspect reads any element's colours, type, box model and contrast.
4. **Grab design tokens:** Code › Tokens reads a site's CSS variables, type scale and fonts.
5. **Check accessibility:** the Check space holds Contrast, Vision and the Audit.

Choose **Next** to move on, **Skip** to close it, or **Get started** on the last step. You can replay it any time with the **?** button (**Take the tour**) beside the spaces, or from Settings › Shortcuts › **Replay the tour**.

## The layout

From top to bottom, the popup shows:

1. **The header.**
   - The **Auric Artisan** wordmark opens auricartisan.com in a new tab.
   - The search field (**Search tools, colours, settings**). Press `/` or `Ctrl` + `K` to jump into it.
   - Four buttons: **Open the side panel**, **Open in its own window**, **Switch between light and dark** and **Settings**.
2. **The spaces bar.**
   - **Home**, **Colour**, **Check**, **Code** and **Saved**.
   - The site chip names the site the page tools act on, or says **No page** where the tools cannot reach.
   - The **?** button replays the tour.
3. **The main area.** Home shows a dashboard. In a space, a row of tool chips sits at the top and the chosen tool fills the rest.

The spaces hold these tools:

| Space | Tools |
|---|---|
| **Colour** | Picker, Page palette, Image, Gradient, Mix. Harmony, Scale and Convert open from inside the Picker or from search. |
| **Check** | Contrast, Vision, Audit, Findings |
| **Code** | Inspect, Tokens, Snippets |
| **Saved** | Library, History. On the web opens from search. |

Each space remembers the last tool you used in it. The full tour of each surface is in [Surfaces](surfaces/README.md).

## A first task in each space

### Colour: pick a colour from the page

1. Open a web page and open the extension.
2. On **Home**, choose **Pick a colour**.
3. Click any pixel on the screen. Press `Esc` to cancel.

The colour opens in the Picker, with its value in twelve formats and tabs for specs, harmony, scale, contrast, vision and code. It is also added to your history. In Firefox the screen eyedropper is not available; see [Picker](colour/picker.md) for the alternative.

### Check: audit the page

1. On **Home**, choose **Audit**. The audit starts at once.
2. Read the four counts: **Tested**, **Failing**, **Borderline** and **Review**.
3. Choose **Outline on page** to mark the failing text on the page for 15 seconds.
4. Click a finding to load its colour pair into **Contrast**, then choose **Fix text**.

The rest of the audit's findings, beyond contrast, are listed in **Check › Findings**. See [Audit](check/audit.md).

### Code: inspect an element

1. On **Home**, choose **Inspect**.
2. Move the pointer over the page. A small card follows it with the element's name, size, contrast, font and colours.
3. Click the element, or press `P`, to pin the full card.
4. Press `C` to copy its CSS, `S` for its selector or `J` for its data as JSON. Press `Esc` to unpin, and `Esc` again to stop.

When you open the extension again, **Code › Inspect** shows the same element in depth. See [Element inspector](surfaces/inspector.md).

### Saved: keep a colour

1. In the Picker, choose the bookmark button (**Save to library**).
2. Open **Saved › Library**. The colour is there; click it to copy it.

The toolbar icon's badge counts the colours in your library.

## Next steps

- Dock the workspace: [Side panel](surfaces/side-panel.md).
- Turn on the pickers or the right-click menu for websites: [On websites](on-websites/README.md).
- Choose a theme, accent colour, popup size or language: [Appearance settings](settings/appearance.md).
- Learn every key: [Keyboard shortcuts](../others/shortcuts.md).
