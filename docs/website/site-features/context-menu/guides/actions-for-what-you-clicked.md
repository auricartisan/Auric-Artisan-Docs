---
title: Right-click menu — Actions for what you clicked
description: How the menu decides what you clicked, and the actions it offers for a page, a link, an image, a selection and a colour.
product: Website › Site features › Right-click menu
updated: 2026-09-25
---

# Actions for what you clicked

## How the menu decides what you clicked

The menu checks, in this order, and uses the first that fits:

1. **Colour** — you right-clicked a colour: a selected hex code (such as `#d3af37`, or six hex characters that include at least one digit), a swatch or chip that carries a colour, or a short piece of text that is a hex code starting with `#`.
2. **Selection** — you right-clicked on text you have selected. A selection made earlier elsewhere on the page does not count unless your click lands on it.
3. **Image** — you right-clicked an image.
4. **Link** — you right-clicked a link.
5. **Page** — anything else.

Plain words that happen to be valid hex, such as "decade" or "facade", are not treated as colours.

## Page

The actions for a page appear first when you right-click an empty area. For the other kinds, the same actions are in the **Page** row under **More**.

| Action | Short label | What it does |
|---|---|---|
| **Copy page URL** | Copy URL | Copies the page's full address. Message: "Page URL copied". |
| **Copy page title** | Title | Copies the page title. Message: "Page title copied". |
| **Copy as Markdown link** | Markdown | Copies `[Page title](address)`. Message: "Markdown link copied". |
| **Share page…** | Share | Opens your device's share sheet. Without one, copies the address ("Link copied"). |
| **Print…** | — | Opens your browser's print dialog (`Ctrl` + `P`). |
| **Analyze this page** | Analyze | Opens the URL Analyzer panel with this page's address, ready to audit. |

Some pages add actions of their own at the top of this list, and some remove actions that do not apply. For example, a published portfolio page shows fewer site actions.

## Link

| Action | What it does |
|---|---|
| **Open in new tab** | Opens the link in a new tab (same as `Ctrl` + click) |
| **Open in new window** | Opens the link in a new window (same as `Shift` + click) |
| **Copy link address** | Copies the link's full address ("Link address copied") |
| **Copy link text** | Copies the visible text of the link (shown only when the link has text) |
| **Copy as Markdown** | Copies `[link text](address)` ("Markdown link copied") |
| **Share link…** | Shares the link through your device's share sheet, or copies it |

The header says **This site** for a link on auricartisan.com and **Another site** for an external link.

## Image

| Action | What it does |
|---|---|
| **Open image in new tab** | Opens the image file on its own |
| **Copy image** | Copies the picture itself as a PNG, or its address when the browser does not allow that (see below) |
| **Copy image address** | Copies the image's address |
| **Copy alt text** | Copies the image's text alternative, shown beside the action. Greyed out with "None" when the image has none. |
| **Copy its palette** | Copies up to four main colours of the image as HEX codes, separated by commas. Four small swatches preview them. |
| **Save image** | Downloads the image under its own file name |

**Copy its palette** appears only when the browser allows the site to read the image's pixels, which is true for images on auricartisan.com and for images from sites that permit it.

When **Copy image** cannot copy the picture, it copies the address and shows "Image address copied (the image itself can’t be copied)".

If the image is inside a link, two more actions follow: **Open link in new tab** and **Copy link address**.

## Selection

| Action | What it does |
|---|---|
| **Copy** | Copies the selected text (`Ctrl` + `C`) |
| **Copy as plain text** | Copies the selection with all line breaks and extra spaces collapsed to single spaces |
| **Search this site** | Opens the site's search page in a new tab with your selection as the query |
| **Search the web** | A submenu: **Google**, **Bing**, **DuckDuckGo**, **Wikipedia**, **YouTube**. Each opens a new tab. |
| **Translate** | Opens Google Translate in a new tab, translating the selection into the page's language |
| **Read aloud** / **Stop reading** | Reads the selection with your device's speech voice; selecting it again while speaking stops it |
| **Share…** | Shares the page with the selection as its text |

**Read aloud** appears only if your browser offers speech. If speech fails, the message reads "Reading aloud is not available".

## Colour

The header shows a swatch of the colour, its RGB value and its hex code.

| Action | Example of what is copied |
|---|---|
| **Copy HEX** | `#D3AF37` |
| **Copy RGB** | `rgb(211 175 55)` |
| **Copy HSL** | `hsl(46 64% 52%)` |
| **Copy OKLCH** | `oklch(76.6% 0.138 91.6)` |
| **Check its contrast** | Opens the contrast tool with this colour |
| **Build harmonies** | Opens the harmony tool with this colour |
| **Find its name** | Opens the colour-name tool with this colour |
| **Inspect in Colour Tools** | Opens the colour inspector with this colour |

Each copy row shows the value it will copy, in a fixed-width font. The examples are the values for the site's gold, `#D3AF37`; the menu computes them for the colour you clicked.

**OKLCH** is a way of writing colour as lightness, chroma (colourfulness) and hue that matches how people perceive colour more closely than HSL.

## The groups under More

### Colour tools

Shown on pages where the site's colour tools are available.

- **All colour tools…** (short label **Colour tools**, `Ctrl` + `Shift` + `C`) opens the colour tools menu at the spot you clicked.
- **Contrast System**, **Accessibility Lab**, **Harmony Studio**, **Color Space Converter**, **Color Name Finder**, **Gradient Library**, **Color Library** open that tool as a floating panel.

If you right-clicked a colour, the tool opens with that colour already loaded. If the tools cannot open on the page, you are taken to the Basic Tools page instead.

### View

| Action | What it does |
|---|---|
| **Scroll to top** | Scrolls to the top of the page (`Home`) |
| **Scroll to bottom** | Scrolls to the end of the page (`End`) |
| **Reading mode** / **Leave reading mode** | Turns reading mode on or off (`Alt` + `R`) |
| **Split view** | Opens or closes split view (`Ctrl` + `Shift` + `D`) |
| **Full screen** / **Exit full screen** | Enters or leaves full screen (`F11`) |
| **Switch theme** | Toggles light and dark. The row shows the current theme, **Light** or **Dark**. |

### Site

| Action | What it does |
|---|---|
| **Home** | Goes to the homepage |
| **Search the site** | Opens Spotlight search (`Ctrl` + `K`), or the search page if Spotlight is not available |
| **Settings** | Opens the Settings panel |
| **Keyboard shortcuts** | Opens the Settings panel on its Shortcuts section |
| **Update website** | Checks for a newer version of the site and applies it (`Ctrl` + `Shift` + `U`) |

The **Update website** row changes with the update state: **Update available** with a version number and "Ready", **Updating website** while it runs, and **Retry update** after an error. A message reads "Checking for updates…" when you start it. The update itself is handled by the Update Kit (see [Kits](../../../kits/README.md)).

### Navigation actions

**Back** (`Alt` + `Left`), **Forward** (`Alt` + `Right`) and **Reload page** (`F5`) do not have a group of their own. They are in the default quick bar and can be found with the filter.

### Browser’s own menu

The last row, **Browser’s own menu** (`Shift` + right-click), closes the site menu and shows the message "Right-click again for the browser’s menu". Your next right-click opens the browser's menu; the one after that opens the site menu again.

## Actions that depend on the page

Some rows appear only where the page supports them. **Settings**, **Keyboard shortcuts** and **Reading mode** need the Settings panel; the **Colour tools** group needs the colour tools; **Switch theme** needs a theme control. Pages that do not load these, such as published portfolios, show a shorter menu.
