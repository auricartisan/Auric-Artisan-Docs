---
title: Shade Library — Reference
description: Every control, filter, sort order, tab, output and message in the Shade Library.
product: Website › Library › Colour libraries › Shade Library
updated: 2026-09-25
---

# Shade Library reference

Everything on https://auricartisan.com/library/shades/.

## Heading

| Item | Content |
| --- | --- |
| Kicker | **Auric Artisan · Shades** |
| Headline | **Eight thousand ramps, and 8% of them even.** |
| Facts | **Collection 8,192**, **10 methods**, **Measured in OKLab** |
| **Read the API guide →** | The Shade Library API guide. |
| **Automate this** note | **3 API credits per call to GET /v1/shade/library**; **API docs**; × dismisses. |

## Browse controls

| Control | What it does |
| --- | --- |
| **Search by id, hex, token or method…** | Every word must match id, name, base, method, base hue name, a token name or a hex. |
| **Shuffle** | Sort **Random**. |
| **Open a random scale** | Opens any scale on **Inspect**. |
| **Filter inside results** (**id, hex, method…**) | Second search, combined. |
| **Clear** | Empties the second search. |

## Tabs

**Library** (badge: matches), **Inspect**, **Harmony**, **Accessibility**, **Stats**, **Export**, **Saved** (badge: saved).

## Filters

| Filter | Options |
| --- | --- |
| **Base hue** | **All hues**, **Red** (340° to under 20°), **Orange** (20–50°), **Yellow** (50–80°), **Green** (80–160°), **Cyan** (160–200°), **Blue** (200–260°), **Purple** (260–300°), **Pink** (300–340°) |
| **Chroma** | **Any chroma**, **Muted (< 0.07)**, **Balanced** (0.07–0.15), **Vivid (> 0.15)** |
| **Lightness** | **Any lightness**, **Dark** (< 0.40), **Mid** (0.40–0.70), **Light** (> 0.70) |
| **Method** | **All methods**, **Accessible Ui**, **Brand System**, **Duotone Shift**, **Ink Paper**, **Material Like**, **Neutral System**, **Oklch Ramp**, **Tailwind Like**, **Temperature Shift**, **Vivid Product** |

## Sort by

**Sort: original** (default), **Lightness up**, **Lightness down**, **Chroma up**, **Chroma down**, **Hue (rainbow)**, **Score high to low**, **Tokens high to low**, **Random**.

## Library tab buttons

**Reset**, **Export visible**, **Back to top**. Counter: `first–last of total scales`, or **Nothing to show**.

## Card

| Part | Action |
| --- | --- |
| Swatch (token and hex) | Copies the hex. `Enter` / `Space` when focused opens the scale. |
| Id and method | For example `shade_000000`, **Material Like**. |
| **Inspect** | Opens the scale. |
| **Copy** | Copies all hexes (**Shade hexes copied**). |
| **Save** / **Saved** | Saves or unsaves (**Shade saved** / **Shade removed**). |

## Inspect tab

| Block | Contents |
| --- | --- |
| Token strip | Token, descriptive name, hex; select to copy. |
| **Shade summary** | Badge (**Neutral**, **Hue Shift**, **Light**, **Deep**, **Balanced**); **Shade ID**, **Global index**, **Method**, **Base**, **Tokens**, **Avg L (OKLCH)**, **Avg chroma**, **Hue span**, **Score**, **Auto AA tokens**, **Min adjacent contrast** |
| **Token contrast ladder** | Each token's contrast with automatic text. |
| **Quick export** | **Copy HEX**, **Copy CSS vars**, **Copy SCSS**, **Copy Tailwind**, **Download JSON**, **Download SVG**, **Download PNG**, **Save to library** / **Unsave**, **Copy share link**, **Design tokens…** |
| Token cards | **HEX**, **RGB**, **OKLCH**, **CIE L\*a\*b\***, **WCAG vs white**, **WCAG vs black** |

## Analysis tabs

| Tab | Cards |
| --- | --- |
| **Harmony** | **Generation method**, **Dominant hue bucket**, **Shade profile**, **Token count**, **Lightness & chroma profile** |
| **Accessibility** | **Shade-level WCAG summary** (**All tokens auto-AA**, **75%+ tokens auto-AA**, **White text coverage**, **Black text coverage**), **Active shade checks**, **Visible shade systems where every token gets AA auto text** |
| **Stats** | **Avg lightness (OKLCH L)**, **Avg chroma (OKLCH C)**, **Hue spread**, **Token count**, **Score** |

## Export tab

| Card | Buttons |
| --- | --- |
| **Selection - id** | **HEX list**, **CSS variables**, **SCSS variables**, **Tailwind config**; **JSON**, **SVG strip**, **PNG strip** |
| **Visible page** | **Download JSON (visible page)**, **Download CSV (visible page)**, **Download CSS variables**, **Download SCSS variables**, **Download compact JSON**; **Download .txt hex list**, **Download tailwind.config.js fragment** |

## Files

| Output | Name | Detail |
| --- | --- | --- |
| JSON | `<id>.json` (for example `shade-000000.json`) | Scale with token contrast and metrics. |
| SVG | `<id>.svg` | 1200 × 260. |
| PNG | `<id>.png` | 1600 × 420. |
| Bulk | `shade-library-<count>-<date>.<ext>` | `json`, `csv`, `css`, `scss`, `txt`. |
| Design tokens ZIP | `shade-<id>.zip` | Eight formats. |

## Messages

| Message | When |
| --- | --- |
| **Loading shade library...** | While loading. |
| **Could not load shade library** | Loading failed. |
| **No shade systems match** | Nothing matches. |
| **No shade system selected** | **Inspect** or **Export** before opening a scale. |
| **No shade systems** | An analysis tab with nothing matching. |
| **No saved shade systems yet** | Nothing saved. |
| **#HEX copied**, **Shade hexes copied**, **HEX list copied**, **CSS variables copied**, **SCSS copied**, **Tailwind copied**, **Copied** | After copying. |
| **Shade saved**, **Shade removed** | After saving or unsaving. |
| **PNG export failed** | The browser could not make the PNG. |
| **Shared shade not in current library** | A share link could not be matched. |

## Keyboard

`/` focuses search; `Enter` or `Space` on a focused swatch opens its scale; `Escape` closes the share and design tokens dialogs.
