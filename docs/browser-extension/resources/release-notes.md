---
title: Browser extension — Release notes
description: What changed in each version of the Auric Artisan browser extension, and what is built for the next release.
product: Browser extension
updated: 2026-09-25
---

# Release notes

The user-facing history of the Auric Artisan browser extension, newest first. Store listings update after each store's review, so your browser may show an earlier version for a while; check your version on the browser's extensions page.

## Upcoming (built, not yet released)

A redesign called "one studio, four surfaces" lays out the same spaces (Home, Colour, Check, Code, Saved) for where you are: docked beside the page, drawn over it, and in a quick popup.

### The side panel becomes the home base

- The spaces become a **rail** down the left edge, with the theme, Settings and the tour at its foot, so the whole width goes to the tool.
- Each space names itself and the tab its tools act on.
- Home leads with **This tab**: the site the panel is linked to, whether the page tools reach it, and **Pick**, **Inspect**, **Audit** and **Vision** in one click. After an audit it says when it ran and what failed, with **Show on page**.
- Home lists the page's own colours; a click opens one in the Picker.
- The panel follows the tab: switching tabs refreshes Home.

### The popup becomes a quick launcher

**Pick a colour**, **Contrast** (with its shortcut), **Inspect** and **Audit this page**; the last contrast pair; recent colours; **Page palette**, **Vision** and **Search**; and **Open the side panel**, shown only where the browser has one.

### The audit reads like a report

- A score from the rule engine, what was checked and when, a bar of failing, borderline, review and passed, and the four counts.
- Findings are numbered rows with their colour pair. The selected row offers **Fix in Contrast** and **Copy selector**.
- The run button says **Run again** after the first run.

### Outlines drawn over the page, not on it

- A layer over the page draws a box and a numbered pin for each finding. Pin 2 is row 2 in the list, and selecting either selects both.
- The selected finding opens a card with the nearest passing text colour, **Try the fix** (a preview on the page, undone on close), **Copy CSS** and Next.
- A **page dock** at the bottom counts what failed, steps through findings and closes with **Done** or `Esc`.
- The overlay stays until you close it; a switch in Check › Audit shows and hides it. Nothing on the site itself is changed.

### Inspector and right-click menu

- With the side panel open, a pinned element keeps a compact card on the page ("Details in the side panel") and the panel opens Code › Inspect with everything else.
- The right-click menu's header shows the clicked element's text contrast (for example "16.5 AAA", red when it fails).
- In Chromium browsers the first element action becomes **Inspect in side panel**. Firefox keeps **Inspect element**, because its sidebar opens only from the browser's own controls.
- Hindi covers every new string.

## 1.0.2 — 2026-09-23

Hindi throughout the product, and the Auric Studio redesign.

### New

- **A new workspace.** Home plus four spaces, Colour, Check, Code and Saved, replace the old grid of tabs. `/` or `Ctrl` + `K` searches every tool, setting and auricartisan.com page.
- **Home:** a colour of the day, four on-this-page actions that start the work, recent colours, **Continue**, and editable pinned tools.
- **The Picker is auricartisan.com's own colour picker**, with twelve formats, contrast with the closest passing colour, colour-vision previews (Machado 2009), code for CSS, wide-gamut CSS, Tailwind v4, SwiftUI, Compose and Android, the page's own colours, chroma room in sRGB and P3, harmonies in HSL or OKLCH, an 11-step OKLCH scale, and opacity in every copied value.
- **Settings is a two-pane view** (Appearance, Pickers, Right-click, Tools, Data, Shortcuts), with a switch for each of the 13 picker types, **Leave designed controls alone**, **Never on** lists, and **Change them in the browser**.
- **Search in dropdowns with more than seven options**, on web pages and in the extension: typing filters and underlines matches, groups keep their headings, and "No options match" offers to clear the search.
- **Multi-select as a dropdown**, with chips, an "N/M chosen" count, **Select all** and **Clear**.
- **The inspector** has a light hover card and a pinned card that leads with contrast, shows the nearest passing colour, and explains every accessibility problem it finds, in seven sections with summaries.
- **The right-click menu, redesigned:** a header naming what you clicked; its own actions first; Auric tools, Page, Tab & window and View as one row each; a quick bar of up to six pinned actions; typing to filter everything; copy selector as CSS, JavaScript, Playwright or XPath; copy a selected colour as HEX, RGB, HSL or OKLCH; copy an image's palette; pick a colour from an image; side-by-side colour vision; Google Images search; **Allow** chips for actions that need a permission; and a gear for the quick bar, layout and row height.
- **Settings › Right-click** gains **Step aside for a site's own menu**, the quick bar, layout, row height, a **Never on** list and the three permissions.
- **Hindi (हिन्दी)** across the popup, side panel, website pickers, right-click menu, inspector and every accessibility finding. The store description, toolbar tooltip and shortcut names follow the browser's language.
- The Auric Artisan wordmark links to auricartisan.com.

### Changed

- One colour picker in three shapes: a compact popover on web pages, split in the popup, stacked in the side panel.
- The colour picker on web pages is a compact 296 px popover with five panes, at most one open, a searchable format menu, and it opens upward near the bottom of the window.
- Number, range, checkbox and radio controls follow your theme. The number stepper disables its buttons at the minimum and maximum, and the range slider gets an editable value.
- On Dark or Light every in-page control uses that theme; on System they match the page.
- Search puts an exact title first and groups results as Best match, Tools, Settings, Actions and On the web.
- The default accent is Auric gold `#d3af37` everywhere.
- The inspector's bar sits at the bottom and names what is being inspected.

### Fixed

- The right-click menu no longer takes over sites that have their own menu, such as Figma and Google Docs, unless you turn off Step aside. Shift + right-click is always the browser's menu.
- The inspector no longer closes when you click an element on sites that rewrite their address on every click, such as auricartisan.com. If the page removes the pinned element, the card lets go.
- The website colour picker no longer shows its light theme while Settings says Dark.
- The popup passes its own accessibility audit again.
- Typing "Settings" in search and pressing Enter no longer runs "Reset all settings".
- The audit no longer reports roving-tabindex items (such as inactive tabs) as unreachable.
- English text left in the Hindi popup is translated.
- Recent colours are no longer thin pills in a narrow side panel, and no longer list one colour twice in different letter cases.

## 1.0.1 — 2026-07-31

### New

- **Universal form pickers** for a page's date, month, week, date-and-time, time, number, range and colour inputs, behind one switch. They set values the way the page expects and fire real events.
- **A custom in-page right-click menu**, on demand, over the extension's tools.
- **Search over settings and features** in the popup.
- **QR codes** for the current page or a selection.

### Changed

- Everything the extension draws on a page is isolated from the site's styles.
- The popup and side panel adapt to their width instead of clipping.
- Packages for Edge and Opera, identical to the Chrome package.
- The Firefox package declares that it collects no data.

## 1.0.0 — 2026-07-22

### New

- **An accessibility engine with 80 rules across 32 WCAG success criteria**, covering ARIA, accessible names, structure, forms, media, keyboard, contrast and page-level criteria. Before, the scan checked text contrast only.
- The engine checks against bundled WCAG 2.2, ARIA 1.2 and HTML accessibility data, and computes accessible names with the standard algorithm.
- Audits run in slices so the page stays responsive, with limits per rule instead of a fixed cap.
- APCA Lc beside WCAG ratios in the scanner, the popup and the inspector.
- A new icon family.

### Changed

- Scoring counts each failing rule, weighted by impact, instead of each failing element, so a large page no longer scores worse for being large.
- Only one extension, **Auric Artisan**, is published.

### Fixed

- Invalid boolean ARIA values are reported instead of breaking the check.
- The focus-indicator rule no longer reports every control; it looks for stylesheets that remove the outline with no replacement.
- Target size respects WCAG 2.5.8's spacing exception.
- Browser-drawn checkboxes and radios are no longer flagged for non-text contrast.

## 0.9.52

- **Snippets**, a vault of saved code: **Save snippet** in Gradient, Shades, Inspect and Tokens, **+ New**, search, **This site**, **Copy all**, **Export** and **Clear all**, up to 200 snippets.
- **Backup and restore** of settings, history, library and snippets in one `.json` file.
- A storage meter with counts in Settings › Data.
- Lists update live across windows.

## 0.9.51

- The Auric colour picker can replace a page's colour inputs.
- APCA tiers (Lc 90, 75, 60, 45, 30) beside the WCAG ratio.
- A choice of auto-fix target: AA 4.5:1, AA Large 3:1, AAA 7:1, APCA Lc 60 or Lc 75.
- A deep scan mode for the page audit, with manual-review flags for text over images, gradients and shadows.
- **Inspect element** in the right-click menu, and a grouped inspector read-out with keyboard DOM navigation, following your accent colour.

## 0.2.1

- The element inspector, with copy-as-CSS.
- Design tokens from any page, exported as CSS, W3C tokens, a Tailwind v4 `@theme` block or JSON.
- Code export for every picked colour: `oklch()`, Tailwind, SwiftUI, Compose and Android.
- A first-run tour.

## 0.2.0

A rebuild into a colour, design and accessibility toolkit: harmonies on a colour wheel, shades and tints, a gradient builder, mixing and blending, a converter, a page contrast scan with outlines and JSON and CSV export, history and library, themes, keyboard shortcuts and right-click entries, APCA, OKLCH maths and a vision simulator.

## 0.1.0

The first release: a popup colour picker with an eyedropper, an eight-format read-out, basic palette extraction and WCAG contrast checking.
