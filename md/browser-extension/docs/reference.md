---
title: Browser extension — Reference
description: Every control, option, output, setting, shortcut and limit of the Auric Artisan browser extension in one place.
product: Browser extension
updated: 2026-09-25
---

# Reference

This page lists every part of the extension in tables, for quick lookup. Each section links to the page that explains it in full. It describes version 1.0.2.

## Product facts

| Fact | Value |
|---|---|
| Name | Auric Artisan |
| Version described | 1.0.2 |
| Extension format | Manifest V3 |
| Browsers | Chrome, Edge, Opera, Brave, Vivaldi and other Chromium browsers; Firefox 115 and later |
| Interface languages | English, हिन्दी (Hindi) |
| Price | Free |
| Account | None |
| Network requests | None of its own; only pages you choose to open |
| Tools | 18 |
| Accessibility rules | 80 in the engine; 78 run by the audit (WCAG 2.2 A and AA) |
| Vision simulations | 12 (8 colour-vision, 4 low-vision) |
| Colour formats in the Picker | 12 |

## Header and navigation ([The popup](surfaces/popup.md))

| Control | What it does |
|---|---|
| **Auric Artisan** wordmark | Opens auricartisan.com |
| Search field | Finds tools, settings and web pages (`/` or `Ctrl` + `K`) |
| **Open the side panel** | Docks the workspace; hidden in the side panel |
| **Open in its own window** | A 620 × 700 resizable window; hidden at Compact size |
| **Switch between light and dark** | Flips the theme |
| **Settings** | Opens Settings |
| Spaces | Home, Colour, Check, Code, Saved |
| Site chip | The site the page tools act on, or **No page** |
| **Take the tour** (?) | Replays the tour |
| Tool chips | The tools of the current space |

## Home ([Home](surfaces/home.md))

| Block | Contents |
|---|---|
| Colour of the day | Swatch, date, HEX, OKLCH, name; **Open in picker**; copy |
| On this page | **Pick a colour**, **Inspect**, **Audit**, **Palette** |
| Recent | Up to 12 recent colours; **History** link |
| Continue | The last tool and what you were doing |
| Pinned | Up to 8 tools; **Edit** / **Done** |
| On auricartisan.com | Collections, Accessibility Library, Learning Library, Documentation |

## Tools

| Tool | Space | Page |
|---|---|---|
| Picker | Colour | [Picker](colour/picker.md) |
| Page palette | Colour | [Page palette](colour/page-palette.md) |
| Image | Colour | [Image](colour/image.md) |
| Gradient | Colour | [Gradient](colour/gradient.md) |
| Mix | Colour | [Mix](colour/mix.md) |
| Harmony | Colour (from the Picker) | [Harmony](colour/harmony.md) |
| Scale | Colour (from the Picker) | [Scale](colour/scale.md) |
| Convert | Colour (from the Picker) | [Convert](colour/convert.md) |
| Contrast | Check | [Contrast](check/contrast.md) |
| Vision | Check | [Vision](check/vision.md) |
| Audit | Check | [Audit](check/audit.md) |
| Findings | Check | [Findings](check/all-findings.md) |
| Inspect | Code | [Inspect](code/inspect.md) |
| Tokens | Code | [Tokens](code/tokens.md) |
| Snippets | Code | [Snippets](code/snippets.md) |
| Library | Saved | [Library](saved/library.md) |
| History | Saved | [History](saved/history.md) |
| On the web | Saved (from search) | [On the web](saved/on-the-web.md) |

## Picker

| Control | Values |
|---|---|
| Formats | HEX, RGB, HSL, HSV, HWB, CMYK, LAB, LCH, OKLAB, OKLCH, XYZ, P3 |
| Panes | Specs, Harmony, Scale, Contrast, Vision, Code; Page and Recent in the side panel |
| Harmony rotation | HSL or OKLCH |
| Contrast background | White, Black, Page |
| Code rows | CSS, CSS · wide gamut, Tailwind v4, SwiftUI, Jetpack Compose, Android XML |
| Actions | **Pick from page**, **Save to library**, **Check as text**, **Check as background** |

## Page palette and Image

| Control | Values |
|---|---|
| **Read the page's colours** | Up to 6 000 elements, 12 colour properties, up to 48 colours |
| View | Strip or grid |
| Mode | Most used, Dominant (k-means), Sort by hue, Sort by lightness |
| Copy | HEX, CSS, oklch(), JSON, ASE (downloaded) |
| Framework | Tailwind, @theme, SCSS, Tokens |
| Export | SVG (copied), PNG (downloaded), Save, Open |
| Image input | Drop, paste, browse (PNG, JPG, WebP, GIF), **Capture the visible tab** |
| Image colours | 6, 8 (default), 12, 16 |
| Image actions | **Open in Page palette**, **Copy HEX**, **Save palette** |

## Gradient, Mix, Harmony, Scale, Convert

- **Gradient**: Stops (at least 2) with colour and 0–100% position; **+ Stop**; type Linear, Radial, Conic; angle 0–360°; space sRGB, OKLCH, HSL; **Copy**, **Save snippet**, **Random**, **Reverse**
- **Mix**: Colours A and B; Mix 0–100% (50%); space sRGB, Linear RGB, LAB (default), OKLAB, HSL; blend Normal, Multiply, Screen, Overlay, Darken, Lighten
- **Harmony**: Base colour; Complementary, Split complement, Analogous, Triadic (default), Tetradic, Square, Monochromatic, Double split, Compound; **Copy**, **Send**, **Save**
- **Scale**: Base; Tailwind 50–950 (default), Material 50–900, Tints, Shades, Tones; **Scale name** (32 characters, `brand`); CSS, SCSS, oklch(), JSON, Tailwind, @theme, Tokens, SVG, PNG, Save
- **Convert**: HEX, RGB, HSL, HSV, CMYK, LAB, LCH, OKLCH, HWB, Name; **Random**, **Invert**, **Complement**

## Contrast

| Control | Values |
|---|---|
| Inputs | **Text**, **Background** |
| Verdict | AAA, AA, AA Large, Fail |
| WCAG checks | AA Body 4.5, AA Large 3, AAA Body 7, AAA Large 4.5, AA UI 3, Gfx 3 |
| APCA tiers | Lc 90 Any, Lc 75 Body, Lc 60 Large, Lc 45 XL/Bold, Lc 30 UI |
| APCA readable sizes | 14, 16, 18, 24, 36, 48 px at normal and bold |
| Colour-vision check | Normal, Protan, Deutan, Tritan |
| Fix target | AA 4.5:1 (default), AA Large 3:1, AAA 7:1, APCA Lc 60, APCA Lc 75 |
| Buttons | **Swap**, **Fix text**, **Fix background**, **Copy report** |
| Suggestions | Up to 6 on-brand text and 6 on-brand background colours |

## Vision

- **Simulations**: Protanopia, Deuteranopia, Tritanopia, Achromatopsia, Protanomaly, Deuteranomaly, Tritanomaly, Achromatomaly, Cataracts, Low vision, Glaucoma, AMD
- **Strength**: 0–100% (100%); colour-vision types only
- **Buttons**: **Clear**, **Side-by-side**, **Capture** (PNG)

## Audit and Findings

| Item | Values |
|---|---|
| Buttons | **Run the audit** (then **Run audit**), **Outline on page**, **Export JSON**, **Export CSV** |
| Counts | Tested, Failing, Borderline, Review |
| Thresholds | 4.5:1 body, 3:1 large; borderline within 1.5 |
| Outlines | Red failing, amber borderline; clear after 15 seconds |
| Findings counts | Failing, Warnings, Total |
| Finding actions | **Show on page**, **Copy selector**, **Inspect**, **Check contrast** |
| Impacts | critical, serious, moderate, minor |

## Inspector and Inspect

| Item | Values |
|---|---|
| Hover card | Name, size, display/role/landmark, contrast with AA and AAA, Font, Size, Text, Background, Padding |
| Pinned card sections | Box model, Colours, Layout, Typography, Effects, Accessibility, CSS |
| Inspector keys | Arrows, `P`, `C`, `S`, `J`, `Enter`, `Esc` |
| Inspect views | Overview, Styles, A11y, DOM, Live CSS |
| Inspect navigation | Breadcrumbs, **Parent**, **Child**, **Prev**, **Next** |
| Inspect actions | **Show on page**, **Selector**, **JSON**, **Use text colour**, **Use background** |
| Locators | CSS, JavaScript, Playwright |
| Live CSS | **Apply to page**, **Reset**, **Copy CSS**, **Save snippet** |

## Tokens and Snippets

| Item | Values |
|---|---|
| Tokens scan | Up to 240 variables, 8 fonts, 16 sizes; 4 000 elements |
| Tokens export | CSS vars, W3C tokens, Tailwind @theme, JSON, Save snippet |
| Snippet sources | Gradient, Scale, Tokens, Live CSS, **+ New** |
| Snippet types | CSS, Gradient, Shades, Tokens, Palette, Contrast, Note |
| Snippet actions | Search, **This site**, Copy, Delete, **Copy all**, **Export file**, **Clear all** |

## Settings

| Section | Setting | Values | Default |
|---|---|---|---|
| Appearance | Theme | System, Light, Dark | Dark |
| Appearance | Accent | 12 presets or custom hex | Auric gold `#d3af37` |
| Appearance | Popup size | Compact 460 × 520, Standard 560 × 600, Large 760 × 600 | Standard |
| Appearance | Language | English, हिन्दी | English |
| Pickers | Auric pickers on websites | On, off | Off |
| Pickers | Leave designed controls alone | On, off | On |
| Pickers | Picker types | 13 chips | All on |
| Pickers | Never on | Up to 100 sites; auricartisan.com locked | Empty |
| Right-click | Custom right-click menu | On, off | Off |
| Right-click | Step aside for a site's own menu | On, off | On |
| Right-click | Items in the browser's menu | On, off | On |
| Right-click | Quick bar | Up to 6 actions; **Reset** | Back, Forward, Reload, Copy page URL, Copy screenshot |
| Right-click | Menu layout | Focused, Everything | Focused |
| Right-click | Row height | Standard, Compact | Standard |
| Right-click | Never on | Up to 100 sites; auricartisan.com locked | Empty |
| Right-click | Permissions | Paste, Save as…, Reopen closed tab | Not granted |
| Tools | Copy colours as | HEX, RGB, HSL, OKLCH | HEX |
| Tools | Colour names | CSS names, XKCD, Off | CSS names |
| Tools | Show APCA beside WCAG | On, off | On |
| Tools | Keep a colour history | On, off | On |
| Tools | Sound on pick | On, off | Off |
| Tools | Deep page audit | On, off | On |
| Tools | Outline issues after an audit | On, off | Off |
| Data | Backup | **Download a backup**, **Restore from a file** | — |
| Data | Settings only | **Copy settings**, **Paste settings** | — |
| Data | Start over | **Clear history & library**, **Reset all settings** | — |
| Shortcuts | Buttons | **Change them in the browser**, **Replay the tour** | — |

## Keyboard shortcuts

| Keys | Action |
|---|---|
| `Alt` + `Shift` + `A` | Open Auric Artisan |
| `Alt` + `Shift` + `C` | Open the contrast checker |
| `Alt` + `Shift` + `E` | Extract the page palette |
| `Alt` + `Shift` + `V` | Toggle the deuteranopia simulation |
| Unassigned | Inspect an element on the page |
| Unassigned | Run a full accessibility audit |

All keys, including the inspector and menu keys, are in [Keyboard shortcuts](../others/shortcuts.md).

## Limits

| What | Limit |
|---|---|
| History | 50 colours |
| Library colours | 500 |
| Saved palettes | 30 (100 in a restored backup) |
| Colours per palette | 64 (restored backup) |
| Pinned tools | 8 |
| Quick bar | 6 actions |
| Snippets | 200, 20 000 characters each, titles 80 |
| Never on lists | 100 sites each |
| Contrast scan | 3 500 elements and 160 issues (deep); 1 800 and 80 (normal) |
| Rule audit | 25 000 elements and 250 issues per rule; 30 seconds |
| Page palette | 6 000 elements; 48 colours |
| Tokens | 4 000 elements; 240 variables, 8 fonts, 16 sizes |
| Inspector markup | 12 KB |
| Queued shortcut or menu command | Dropped after 30 seconds |

## Files the extension writes

| File | From |
|---|---|
| `auric-artisan-backup-YYYY-MM-DD.json` | Settings › Data › **Download a backup** |
| `auric-snippets-YYYY-MM-DD.txt` | Snippets › **Export file** |
| `auric-palette-YYYY-MM-DD.ase` | Page palette › **ASE** |
| `palette-….png` | Page palette › **PNG** |
| `aa-vision-<simulation>-….png` | Vision › **Capture** |
