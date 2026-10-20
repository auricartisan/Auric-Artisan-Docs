---
title: Harmony Library — Reference
description: Every control, filter, sort order, tab, output and message in the Harmony Library.
product: Website › Library › Colour libraries › Harmony Library
updated: 2026-09-25
---

# Harmony Library reference

Everything on https://auricartisan.com/library/harmony/.

## Heading

| Item | Content |
| --- | --- |
| Kicker | **Auric Artisan · Harmony** |
| Headline | **Eight thousand schemes, and none of them stored.** |
| Facts | **Collection 8,192**, **23 methods**, **Derived, not stored** |
| **Read the API guide →** | The Harmony Library API guide. |
| **Automate this** note | **3 API credits per call to GET /v1/harmony/library**; **API docs**; × dismisses. |

## What harmony is this?

| Control | What it does | Default |
| --- | --- | --- |
| Colour swatch | Opens a colour picker. | — |
| Colour field | Any CSS colour. | `#E4572E`, `#2EE457`, `#572EE4` |
| × | Removes a colour; hidden at two. | — |
| **Add a colour** | Adds the opposite of the first colour; up to 12. | — |
| **Identify it** | Runs the match again. | — |

| Output | Meaning |
| --- | --- |
| Verdict | Scheme name (fit ≥ 0.85), **Close to** … (0.65 to 0.85), **Not one of the 23** (below 0.65). |
| **fit** | 0 to 1, three decimals. |
| Note | Angle error, or schemes indistinguishable by hue. |
| **Family**, **Base colour**, **Worst pair**, **Best pair** | Family, best base, lowest and highest pair contrast (**(AA)** at 4.5:1). |
| **Also considered** | Up to four runners-up with fit. |

## Browse controls

| Control | What it does |
| --- | --- |
| **Search by id, hex or method…** | An id (`har_…`) or number shows that harmony; other words must match id, method, family or a hex. |
| **Shuffle** | Sort **Random**. |
| **Open a random harmony** | Opens any harmony on **Inspect**. |
| **Filter inside results** (**id, hex, method…**) | Second search. |
| **Clear** | Empties the second search. |

## Tabs

**Library** (badge: matches), **Inspect**, **Theory**, **Accessibility**, **Stats**, **Export**, **Saved** (badge: saved).

## Filters

| Filter | Options |
| --- | --- |
| **Base hue** | **All hues**, **Red** (340° to under 20°), **Orange** (20–50°), **Yellow** (50–80°), **Green** (80–160°), **Cyan** (160–200°), **Blue** (200–260°), **Purple** (260–300°), **Pink** (300–340°) |
| **Chroma** | **Any chroma**, **Muted (< 0.07)**, **Balanced**, **Vivid (> 0.15)** |
| **Lightness** | **Any lightness**, **Dark** (< 0.40), **Mid** (0.40–0.70), **Light** (> 0.70) |
| **Method** | **All methods** and 23 methods (does not currently narrow the grid; search the method name instead) |
| **Family** | **All families**, **Complementary**, **Polyadic**, **Analogous**, **Monochromatic**, **Compound** |

## Sort by

**Sort: original** (default), **Lightness ↑**, **Lightness ↓**, **Chroma ↑**, **Chroma ↓**, **Hue (rainbow)**, **Color count ↑**, **Color count ↓**, **Random**.

## Library tab buttons

**Reset** (clears searches, filters and sort), **Export visible** (opens **Export**), **Back to top**.

## Card

Swatches (select to copy), id, scheme, **Inspect**, **Copy** (all hexes), **Save** / **Saved**. Select the card to inspect.

## Inspect tab

| Block | Contents |
| --- | --- |
| Colour strip | Role, descriptive name, hex; select to copy. |
| **Harmony summary** | **Harmony ID**, **Global index**, **Scheme**, **Family**, **Colors**, **Base hue**, **Avg L\* (OKLCH)**, **Avg chroma**, **Hue span**, **DeltaE avg**, **Adherence**, **Entropy**, **Min pair contrast**, **Max pair contrast** |
| **Color-theory scheme** | Description, **Canonical angles**, **Color roles**, **Base HSL** |
| **Pair-by-pair WCAG contrast** | Every pair by role. |
| **Quick export** | **Copy HEX**, **Copy CSS vars**, **Copy SCSS**, **Copy Tailwind**, **Download JSON**, **Download ASE**, **Download SVG**, **Download PNG**, **Open in Coolors**, **Save to library** / **Unsave**, **Copy share link**, **Design tokens…** |
| Colour cards | **Role**, **HEX**, **RGB**, **HSL**, **OKLCH**, **CIE L\*a\*b\***, **WCAG vs white**, **WCAG vs black** |

## Analysis tabs

| Tab | Cards |
| --- | --- |
| **Theory** | **Color-theory scheme**, **Family**, **Dominant hue bucket**, **Color count**, **Adherence to canonical scheme**, **Lightness & chroma profile** |
| **Accessibility** | **Harmony-level WCAG summary**, **Pair-level WCAG breakdown**, **Visible harmonies where every pair passes AA** |
| **Stats** | **Avg lightness (OKLCH L)**, **Avg chroma (OKLCH C)**, **Hue spread**, **Min pair contrast**, **Adherence**, **Colors per harmony** |

## Export tab

| Card | Buttons |
| --- | --- |
| **Selection · id** | **HEX list**, **CSS variables**, **SCSS variables**, **Tailwind config**; **JSON**, **Adobe ASE**, **SVG strip**, **PNG strip**; **Open in Coolors** |
| **Visible page** | **Download JSON (visible page)**, **Download CSV (visible page)**, **Download CSS variables**, **Download SCSS variables**, **Download compact JSON**; **Download .txt hex list**, **Download tailwind.config.js fragment** |

## Files

| Output | Name |
| --- | --- |
| One harmony | `<id>.json`, `<id>.ase`, `<id>.svg`, `<id>.png` |
| Bulk | `harmony-page-<count>-<date>.<ext>` |
| Design tokens ZIP | `harmony-<id>.zip` |

## Messages

| Message | When |
| --- | --- |
| **Loading harmony database…** | While loading. |
| **Could not load harmony database** | Loading failed. |
| **No harmonies match** | Nothing matches. |
| **No harmony selected** | **Inspect** before opening one. |
| **No harmonies** | An analysis tab with nothing matching. |
| **No saved harmonies yet** | Nothing saved. |
| **No scheme uses N colours** | The identifier has a colour count no scheme uses. |
| **Colour N is not a colour yet** | An identifier field is not a colour. |
| **#HEX copied**, **Harmony hexes copied**, **HEX list copied**, **CSS variables copied**, **SCSS variables copied**, **Tailwind config copied**, **Copied** | After copying. |
| **Downloaded** and a file name | After a download. |
| **Saved**, **Removed** | After saving or unsaving on **Inspect**. |
| **Nothing to export** | Bulk export with no matches. |
| **Shared harmony not found in current dataset** | A share link could not be matched. |

## Keyboard

`/` focuses search; `Enter` or `Space` on a focused swatch opens its harmony; `Escape` closes the share and design tokens dialogs.
