---
title: Color Science Lab — Reference
description: Every view, control, option, default, output and file of the Color Science Lab in one place.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Color Science Lab reference

## Page

| Item | Value |
| --- | --- |
| Address | https://auricartisan.com/tool/color-science-lab/ (also /model) |
| Views | Workbench, Catalogue, Compare, Gamut audit, Illuminants |
| Tools | 45 in 8 domains (20 Foundation, 25 Research) |
| Colour spaces | 63 |
| Theories and models | 24 |
| White points (panels) | 13 |
| Maximum open panels | 5 |
| API equivalent | POST /v1/science/dossier, 5 API credits per call |

## Workbench

| Control | Values | Default |
| --- | --- | --- |
| Specimen HEX / colour well | `#RRGGBB` | #4F7FE0 (then remembered) |
| Presets | #4F7FE0, #D3AF37, #2F6D3A, #C4562C, #8F3B22, #2B6F8F, #B0169A, #F0E6D2 | — |
| Observer | 2° 1931, 10° 1964 | 2° 1931 |
| Illuminant | D65, D50, D55, C, A, F2, F11 | D65 |
| Adaptation | Bradford, CAT02, CAT16 | Bradford |

Outputs: CIE XYZ, CIE xyY, `CIE L*a*b*`, CIE LCh, Oklab, Oklch, sRGB, HSL, CMYK; xy plot with L, C and hue angle; gamut in sRGB, Display P3, Adobe RGB, Rec. 2020; ΔE 2000 under each other illuminant.

## Compare (view)

| Control | Default |
| --- | --- |
| Reference (A) | The specimen |
| Candidate (B) | #5A86D8 |

Outputs: coordinates in CIE XYZ, Lab, LCh and Oklab for each; ΔE 2000, ΔE 1976, ΔE 1994, Oklab distance; Δ lightness, Δ chroma, Δ hue angle with a verdict sentence.

## Gamut audit

| Control | Values | Default |
| --- | --- | --- |
| Remove (×) | — | At least 1 colour |
| Add to palette | Up to 16 colours | 8 starting colours |

Outputs: per-colour sRGB margin or clip ΔE; per-space tightest headroom, in-gamut count and margin; verdict; ΔE 2000 cost of clipping.

## Illuminants

Seven illuminants (D65, D50, D55, C, A, F2, F11) with temperature and ΔE 2000 from D65, Bradford transform, 2° observer.

## Catalogue filter bar

| Control | Values | Default |
| --- | --- | --- |
| Search | Free text, applied after a short pause | Empty |
| Domain list | All, Colorimetry, Chromatic Adaptation, Spectral Analysis, Appearance Models, Perceptual Spaces, Color Spaces, Theory and History, Gamut and Rendering, Favorites, Compare, Analytics, Open Panels | All (then remembered) |
| Level | Basic, Advanced, Both | Both (shared with the site's complexity mode) |
| Copy link, Quick start | — | — |

## Panel controls

| Control | Values or range | Default |
| --- | --- | --- |
| Sample color | Colour well, HEX, Random | #D3AF37 |
| Compare color | Colour well, HEX | #2FA7D8 |
| Model | Per domain (see [catalogue-and-panels.md](catalogue-and-panels.md)) | Tool default |
| Color space / standard | 63 spaces | Tool default |
| Theory / observer | 24 entries | Tool default |
| Source white / Target white | A, B, C, D50, D55, D60 / ACES, D65, D75, DCI, E (Equal Energy), F2, F7, F11 | D65 / D50 |
| Experiment strength | 0–100 % | 72 % |
| Color temperature | 1800–12000 K, step 100 | 6500 K |
| Show reference guides | On/off | On |
| Apply adaptation preview | On/off | On |

Tabs: Experiment, Metrics, Chart, Graph, Diagram, Audit.

Theories and models: Newton prism and color circle, Goethe theory of colors, Young-Helmholtz trichromacy, Hering opponent process, Grassmann color laws, Maxwell color triangle, Munsell color order, Ostwald color system, CIE 1931 standard observer, MacAdam ellipses, Judd-Vos correction, Von Kries coefficient law, Land Retinex, Hunt appearance model, Nayatani model, RLAB, LLAB, Fairchild color appearance, CIECAM02, CAM16, Image color appearance / iCAM, IPT hue linearity, Oklab modern uniformity, Basic color terms.

## Panel windows

| Control | What it does |
| --- | --- |
| Link, Duplicate, Pin, Minimize, Maximize, Close | See [arrange-link-save-export.md](arrange-link-save-export.md) |
| Drag title bar / double-click | Move / maximise |
| Corner handle | Resize (minimum 520 × 420) |
| `Escape` | Restore if maximised, otherwise close |

## Open Panels toolbar and Color Control

| Open Panels | Color Control |
| --- | --- |
| Tile, Cascade, Stack, Link all / Unlink all, Export image, Close unpinned | Grid, Split H, Split V, Cascade, Stack, Sync all, Minimize, Restore, Export, Close all; per panel Sync, Keep, Min / Open, Max, Copy, Close |

## Catalogue Compare and Analytics

| Item | Values |
| --- | --- |
| Compare selection buttons | Basic, Advanced, Filtered, Clear; Quick Start: Core Lab |
| Compare columns | Up to 8 tools |
| Test palette | Auric gold, Signal red, Cyan blue, Forest green, Violet, Skin tone |
| Analytics tabs | Heat Map, Mind Map, Stats, Catalog |
| Analytics buttons | Random tool, JSON, CSV, ? |

## Files

| File | From |
| --- | --- |
| `color-science-lab-<date-time>.png` | Export image / Export |
| `color-science-lab-catalog-YYYY-MM-DD.json` | Analytics → JSON |
| `color-science-lab-catalog-YYYY-MM-DD.csv` | Analytics → CSV |

## Remembered in your browser

Last view, Workbench specimen, domain, level (site-wide), favourites, recently opened tools (10), quick-start note dismissal.

## Related

- [Shortcuts](../others/shortcuts.md)
- [Glossary](../others/glossary.md)
