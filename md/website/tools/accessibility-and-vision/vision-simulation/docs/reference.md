---
title: Vision Lab — Reference
description: Every control, option and output of the Vision Lab in one place.
product: Website › Tools › Accessibility and vision
updated: 2026-09-25
---

# Vision Lab reference

## Page

| Item | Detail |
| --- | --- |
| Address | https://auricartisan.com/tool/vision-simulation/ |
| Masthead facts | Conditions 78, Categories 11, Brettel 1997 · Viénot 1999 · Machado 2009 |
| API hint | 5 API credits per call to `POST /v1/vision/audit` |
| Views | **Workbench**, **Catalogue**, **Compare**, **Palette audit**, **Analytics** |
| Notice | Educational visualisation only; not a medical simulation or diagnostic tool; screens are not calibrated |

## Workbench

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Specimen** | What the stage shows | **Interface**, **Palette**, **Image** | Interface |
| **Base colour** | The colour to simulate | Hex, up to 7 characters | `#E53E3E` |
| Reference strip | Ten swatches, each with a **Use** button | — | — |
| **Severity** | Strength of the condition | 0–100% | The condition's clinical default |
| **Model** | Colour-vision model | **Brettel**, **Viénot**, **Machado** | Brettel |
| **Stage** | Layout of the stage | **Split**, **Simulated only** | Split |
| **Search 78 conditions** | Filters the condition list | Text | — |
| List filters | Narrow the list | **All 78**, **Colour**, **Field**, **Basic only** | All 78 |
| **Open the full panel** | Opens the condition as a floating panel | — | — |
| **Compare this** | Adds the condition to Compare | — | — |
| **Copy link to this view** | Copies a `?vw=` link | — | — |

Readouts: **What collapses** (reference pairs that fall under ΔE2000 8 from 12 or more) and **Measured · base colour** (**ΔE76**, **ΔE2000**, **pairs lost / 45**, **button label / fill**).

## Catalogue

| Control | What it does | Values |
| --- | --- | --- |
| **Search simulations…** | Filters cards | Text; `/` to focus, `Esc` to clear |
| Scope button | Chooses a category | All conditions, Favourites, 11 categories, Source image, Open panels |
| **Filter** › **Kind** | Per-colour or field conditions | **All**, **Per-colour**, **Field** |
| **Filter** › **Level** | Basic or advanced conditions (linked to the site-wide preference) | **All**, **Basic**, **Advanced** |
| **About this catalogue** | Explains the cards | — |
| **Copy link** | Copies a `#v=` workspace link | — |
| Daily tally | Simulations opened today (free plan) | Up to 25 |
| Card | Opens a floating panel; star adds to Favourites | `Enter` or `Space`; `Shift` or `Ctrl` + click duplicates |

## Floating panel

| Control | Values | Default |
| --- | --- | --- |
| Title bar | **Link panel**, **Duplicate**, **Pin panel**, **Minimize**, **Maximize panel**, **Close panel** | — |
| **Base color** | Picker, hex, **Random** | `#D3AF37` |
| **Severity** | 0–100% | 100% |
| **Perceptual severity curve**, **Multi-pass deep** | On, off | Off |
| **Model** | Brettel (1997), Viénot (1999), Machado-like | Brettel (1997) |
| Workflow preset | Custom (no preset), Default, Beginner mode, Material testing, Color matching, Print proof, Photography (D65); **Apply** | Custom |
| **Copy HEX**, **Copy CSS** | — | — |
| **Show advanced controls** | Cone channel weights L, M, S (0–2); **Export all CVD** | Off; weights 1 |
| Illuminant | Standard illuminants | D65 |
| CAM model | CAT16 adaptation, CAM16-UCS perceptual, CIECAM02 surround, Hunt-Stevens brightness | CAT16 adaptation |
| White point | D65, D50, A, F2, F7, F11, LED warm, neutral, cool | D65 |
| Correlated color temperature | 1,667–25,000 K | 6517 K |
| Perceived brightness | 5–400% | 100% |
| Observer | 2°, 10° | 2° |
| Surround | Average, Dim, Dark | Average |
| Viewing distance | Near, Normal, Far | Normal |
| **Snapshots** | Name and **Save** | — |
| **Recent changes** | **Undo last**, **Clear** | — |
| Readout tabs | **Chromaticity**, **Metrics**, **Image**, **Mindmap**, **Model audit** | Chromaticity |

Up to 5 panels can be open. A sixth replaces the oldest unpinned panel.

## Vision Control

| Control | What it does |
| --- | --- |
| Arrange | Tile in a grid, split left and right, split top and bottom, cascade, or stack centred |
| Panel tabs | Bring a panel forward |
| **More panel actions** | Sync, minimise or restore all; export a comparison PNG; verification panel; close all but pinned |
| Minimised dock | Restore or close a minimised panel |

## Universal Source Image

| Control | Values | Default |
| --- | --- | --- |
| Drop area | Drop, paste or click to upload an image | A built-in reference chart |
| **Apply to all panels** | — | — |
| **Quality** | Fast · 1024px, Balanced · 1600px, Full · 4096px | Fast · 1024px |
| **Auto-apply to new panels** | On, off | On |
| **Pause auto**, **Clear** | — | — |
| **What this image loses** | Conditions ranked by effect on the image; **Open most-affected →** | — |
| Samples | 15 images | — |
| Test charts | Color bars, Spectrum, Red–Green, Chromatic grid | — |

## Compare

| Control | Values | Default |
| --- | --- | --- |
| Tiles | Normal vision control, plus one per condition; reorder by dragging or with arrow keys; **×** removes | — |
| **Add a condition** | Any of the 78 | — |
| **Severity for every tile** | 0–100% | 100% |
| **Order** | **By impact**, **By severity**, **As arranged** | — |
| **Columns** | **3**, **4**, **5** | — |
| **Copy link to this sheet** | — | — |
| **Send the worst to the workbench** | — | — |

## Palette audit

| Control | Values | Default |
| --- | --- | --- |
| Palette | Up to 24 colours: swatch, hex field, **Remove**; **Add colour** | A 5-colour sample |
| **Merge below** (CIEDE2000 ΔE) | 1–15, steps of 0.5 | 5 |
| **Search 17 conditions** | Text | — |
| Condition filter | **All 17**, **Only failing** | All 17 |
| **Suggest a fix** | Smallest lightness change that separates a merged pair | — |
| **Open this condition in the workbench**, **Copy the palette** | — | — |

## Analytics

| Control | Values |
| --- | --- |
| **View** | **Matrix**, **Map**, **Statistics** |
| Matrix cell | Lists the conditions in it |
| **Open a random condition** | — |
| **Export JSON**, **Export CSV** | `vd-catalog-<date>.json`, `vd-severity-<date>.csv` |
| **Keyboard shortcuts** | Opens the shortcuts overlay |

## Numbers used throughout

| Item | Value |
| --- | --- |
| Conditions | 78 (17 per-colour, 61 field) |
| Categories | 11 |
| Reference swatches | 10, making 45 pairs |
| Collapse rule (Workbench, Compare) | A pair 12 or more apart (CIEDE2000) that falls within 8 |
| Severity score | 1 to 10, an estimated visual-impact score |
| Open panels | Up to 5 |
| Free plan | 25 simulations a day from the Catalogue |
