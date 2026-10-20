---
title: Public API — Collections
description: Browse the colour atlas, find the nearest catalogued colour, and filter the palette, harmony, gradient and shade-scale collections.
product: Services › Public API
updated: 2026-09-25
---

# Collections

The API exposes large, measured collections you can filter and cite. Two kinds exist:

- **Finite catalogues** of 8,192 records (the colour atlas and the harmony, gradient and shade libraries). A filtered browse reports `matched`, a real total, and pages with `offset` and `next_offset`.
- **Scanned collections** too large to count in one request (five million palettes, and the five-million-pair accessibility corpus described in [Accessibility](accessibility.md)). A filtered browse scans a budget of records and reports `scanned`, `hit_rate`, `next_cursor`, `exhausted` and `truncated`.

> **Important:** In a scanned collection, `truncated: true` means the scan budget ran out before the page filled, not that nothing matches. Follow `next_cursor`, or raise `max_scan`, before concluding a filter is empty. `exhausted: true` means the collection really ended.

Records in the libraries are derived from a published seed and their index rather than stored, so an id such as `pal_1z` or `har_5k` is citable: anyone can recompute the same record.

## Colour atlas

### GET /v1/color/atlas

Browse the 8,192-colour atlas under a filter. Hue ranges wrap, so `hue_from=340&hue_to=20` gives the reds.

| Parameter | Description |
|---|---|
| `hue_from`, `hue_to` | Hue range, 0–360; wraps past 360 |
| `min_lightness`, `max_lightness` | OKLCH lightness bounds, 0–1 |
| `min_chroma` | Chroma floor, 0–1 |
| `min_contrast_on_white`, `min_contrast_on_black` | Keep only colours readable on white or black at this ratio |
| `emotion`, `art_movement`, `ai_mood`, `ai_design_usage`, `design_tag` | Label filters, for example `calm`, `Fauvism`, `serene`, `data-viz`, `pastel`; see the stats |
| `sort` | `id` (default), `hue`, `lightness`, `chroma` or `contrast_on_white` |
| `order` | `asc` (default) or `desc` |
| `limit` | Colours per page, 1–200. Default 24. |
| `offset` | Where to start; use `next_offset` |
| `full` | `true` adds the vision simulations and labels |

Returns `matched`, `share_of_atlas`, `next_offset` and `colors`.

```bash
curl "https://api.auricartisan.com/v1/color/atlas?min_contrast_on_white=4.5&sort=chroma&order=desc&limit=5" \
  -H "x-api-key: $AURIC_API_KEY"
```

### GET /v1/color/atlas/stats

What the atlas contains: hue occupancy, the lightness spread, the label vocabulary, and how much of it works as text on white or black. Returns `readable_as_text`, `hue_distribution`, `lightness_distribution` and `labels`.

### GET /v1/color/atlas/:id

One sample, whole. `:id` is an id from 0 to 8191, or a hex the atlas contains (URL-encoded, such as `%2376cdf6`). An unknown id or hex returns `VALIDATION_ERROR`. Returns `color`.

### POST /v1/color/nearest

The catalogued colours closest to one you have. Distance is CIE76 in Lab, and the response names the metric.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | The colour to match |
| `count` | number | No | How many matches, 1–50. Default 5. |
| `full` | boolean | No | `true` for the complete record on each match |

Returns `metric` and `matches`.

```bash
curl -X POST "https://api.auricartisan.com/v1/color/nearest" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#D3AF37","count":5}'
```

## Palette library (five million palettes)

### GET /v1/palette/library

| Parameter | Description |
|---|---|
| `method` | `complementary`, `triadic`, `analogous`, `tetradic`, `golden_ratio`, `monochromatic` or `random` |
| `character` | Measured character: `neutral`, `monochrome`, `analogous`, `triadic` or `diverse` |
| `hue` | First colour's hue band, red through pink |
| `min_contrast`, `max_contrast` | Bounds on the worst pair's contrast, 1–21 |
| `min_lightness`, `max_lightness` | Mean OKLCH lightness bounds, 0–1 |
| `min_chroma` | Mean OKLCH chroma floor, 0–0.5 |
| `carries_body_text` | `true` for palettes with a pair at 4.5:1 or better |
| `sort` | `id` (default), `contrast`, `spread`, `lightness` or `chroma`; other than `id`, sorting is within the scan |
| `order` | `asc` (default) or `desc` |
| `limit` | Per page, 1–100. Default 24. |
| `cursor` | Where to resume; use `next_cursor` |
| `max_scan` | Scan budget, 1,000–500,000. Default 20,000. Raise it for a rare filter. |
| `full` | `true` for per-colour RGB and OKLCH and the palette metrics |

Returns `scanned`, `hit_rate`, `next_cursor`, `exhausted`, `truncated` and `palettes`.

```bash
curl "https://api.auricartisan.com/v1/palette/library?carries_body_text=true&limit=5" \
  -H "x-api-key: $AURIC_API_KEY"
```

### GET /v1/palette/library/stats

Measured on a stated sample (70 runs of 600 consecutive palettes). Returns `measured_on`, `with_an_aa_pair`, `method` and `character`. About 55% of the palettes contain a pair that carries body text.

### GET /v1/palette/library/:id

One palette, whole, with the seed and batch that recompute it. `:id` is a palette id (`pal_1z`) or a number from 0 to 4999999.

## Harmony library (8,192 harmonies)

### GET /v1/harmony/library

| Parameter | Description |
|---|---|
| `method` | One of the 23 methods, for example `triadic`; see the stats |
| `family` | `complementary`, `analogous`, `polyadic`, `monochromatic` or `compound` |
| `hue` | Base hue band: red, orange, yellow, green, cyan, blue, purple, pink |
| `colors` | How many members, 2–7 |
| `min_contrast` | The worst pair must clear this ratio, 1–21 |
| `min_adherence` | How closely it holds its canonical angles, 0–1 |
| `sort` | `id` (default), `contrast`, `spread`, `adherence` or `colors` |
| `order`, `limit`, `offset`, `full` | As in the other catalogues; `limit` 1–100, default 24 |

Returns `matched`, `share_of_collection`, `next_offset` and `harmonies`. Only about a quarter of the collection contains a pair that carries body text, so `min_contrast` is the filter worth using.

### GET /v1/harmony/library/stats

Returns `with_an_aa_pair`, `method`, `family` and `color_count`.

### GET /v1/harmony/library/:id

One harmony, whole, with its derivation. `:id` is a harmony id (`har_5k`) or a number from 0 to 8191.

## Gradient library (8,192 gradients)

### GET /v1/gradient/library

| Parameter | Description |
|---|---|
| `scheme` | For example `Aurora`, `Spectral`, `Terrain`; see the stats |
| `complexity` | `simple`, `detailed` or `extreme` |
| `banding` | `smooth`, `subtle-compression` or `visible-step-risk` |
| `type` | `linear`, `radial` or `conic` |
| `min_score` | Quality floor, 0–1 |
| `min_stops`, `max_stops` | Bounds on the number of colour stops |
| `sort` | `id` (default), `score` or `stops` |
| `order`, `limit`, `offset`, `full` | `limit` 1–100, default 24; `full` adds interpolation space, easing and metrics |

Returns `matched`, `share_of_collection`, `next_offset` and `gradients`. About one gradient in five steps visibly somewhere; `banding` is the filter worth using.

### GET /v1/gradient/library/stats

Returns the `banding`, `scheme` and `interpolation_space` tallies.

### GET /v1/gradient/library/:id

One gradient, whole. `:id` is a row number from 0 to 8191.

## Shade library (8,192 scales)

### GET /v1/shade/library

| Parameter | Description |
|---|---|
| `method` | One of ten, for example `tailwind-like`, `oklch-ramp`, `ink-paper` |
| `evenness` | `even`, `slightly-uneven` or `lumpy` |
| `hue` | Base hue band, red through pink |
| `steps` | Exactly this many steps, 2–64 |
| `min_span` | Contrast between the extremes, 1–21 |
| `min_score` | Quality floor, 0–1 |
| `monotonic` | `true` for scales that never turn round |
| `carries_body_text` | `true` for scales with a pair at 4.5:1 or better |
| `sort` | `id` (default), `score`, `steps`, `span` or `evenness` |
| `order`, `limit`, `offset`, `full` | `limit` 1–100, default 24 |

Returns `matched`, `share_of_collection`, `next_offset` and `scales`. Every scale is monotonic and can carry text; evenness is what separates them, and only 8.2% are clean.

### GET /v1/shade/library/stats

Returns `evenness`, `monotonic`, `carries_body_text` and `method`.

### GET /v1/shade/library/:id

One scale with every measurement. `:id` is a shade id (`shade_000000`) or a row number from 0 to 8191.

## Related pages

- [Accessibility](accessibility.md), for the contrast corpus
- [Palettes, harmonies, gradients and shades](palettes-harmonies-gradients-shades.md)
