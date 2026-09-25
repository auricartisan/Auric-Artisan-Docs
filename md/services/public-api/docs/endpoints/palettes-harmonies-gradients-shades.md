---
title: Public API — Palettes, harmonies, gradients and shades
description: Generate, score, classify, analyse, export and render palettes, harmonies, gradients and shade scales.
product: Services › Public API
updated: 2026-09-25
---

# Palettes, harmonies, gradients and shades

These endpoints build colour sets and measure the ones you already have. Valid `method` values come from `GET /v1/methods/:tool`, and valid export `format` values from `GET /v1/formats`.

## Palettes

### POST /v1/palette/generate

Generate a palette from a seed colour. 2–4 credits.

| Field | Type | Required | Description |
|---|---|---|---|
| `method` | string | No | See `/v1/methods/palette`. Default `triadic`. |
| `hue` | number | No | Base hue, 0–360. Random when omitted. |
| `saturation` | number | No | 0–1. Default 0.7. |
| `lightness` | number | No | 0–1. Default 0.55. |
| `count` | integer | No | How many colours, 1–64. Default 5. |
| `seed` | integer | No | For a repeatable palette |

```bash
curl -X POST "https://api.auricartisan.com/v1/palette/generate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"method":"triadic","hue":45,"saturation":0.7,"lightness":0.55,"count":5}'
```

### POST /v1/palette/evaluate

Score a palette for harmony, contrast and accessibility.

| Field | Type | Required | Description |
|---|---|---|---|
| `palette` | object | Yes | `{ colors: [{ rgb: [r,g,b] }, ...] }`, the shape `/v1/palette/generate` returns |

```bash
curl -X POST "https://api.auricartisan.com/v1/palette/evaluate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"palette":{"colors":[{"rgb":[201,162,39]},{"rgb":[29,42,62]},{"rgb":[255,252,247]}]}}'
```

### POST /v1/palette/export

Render a palette into a file format.

| Field | Type | Required | Description |
|---|---|---|---|
| `format` | string | Yes | `hex`, `json`, `css`, `scss`, `tailwind`, `ase-json` or `svg`; see `/v1/formats` |
| `data` | object | Yes | `{ colors: [{ rgb: [r,g,b] }, ...] }` |
| `options` | object | No | Format-specific options |

```bash
curl -X POST "https://api.auricartisan.com/v1/palette/export" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"format":"css","data":{"colors":[{"rgb":[201,162,39]},{"rgb":[29,42,62]}]}}'
```

### POST /v1/palette/from-image

Extract a palette from an uploaded image. 10–12 credits.

| Field | Type | Required | Description |
|---|---|---|---|
| `image` | string | Yes | Base64 or a data URL. Image bodies are limited to 4 MB. |
| `count` | integer | No | Colours to extract |

### POST /v1/palette/png

Render a palette as a PNG swatch sheet. 10–12 credits. Returns `image/png`.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | colour array | Yes | The palette to draw |

## Harmonies

### POST /v1/harmony/generate

Build a harmony set (complementary, triadic, analogous and others) from a base colour. 2–4 credits.

| Field | Type | Required | Description |
|---|---|---|---|
| `method` | string | Yes | See `/v1/methods/harmony` |
| `hue` | number | Yes | Base hue, 0–360 |
| `saturation` | number | Yes | 0–1 |
| `lightness` | number | Yes | 0–1 |

```bash
curl -X POST "https://api.auricartisan.com/v1/harmony/generate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"method":"triadic","hue":45,"saturation":0.7,"lightness":0.55}'
```

### POST /v1/harmony/classify

Identify which harmony an existing set of colours follows.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | colour array | Yes | The colours to classify |

### POST /v1/harmony/identify

Name the scheme your colours form. It takes 2 to 12 colours and matches their hue pattern against all 23 schemes. Each colour is tried as the anchor in turn, so the order you send them in does not matter. Schemes with the same shape on the hue circle that differ only in lightness or saturation come back together in `ties`.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | array | Yes | 2 to 12 colours as `["#rrggbb", ...]` |

Returns `verdict`, `best_match`, `ties`, `candidates`, `hue_offsets`, `min_pair_contrast` and `carries_body_text`.

```bash
curl -X POST "https://api.auricartisan.com/v1/harmony/identify" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#FF0000","#00FF00","#0000FF"]}'
```

### POST /v1/harmony/export

Export a harmony set.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | colour array | Yes | The harmony set |
| `format` | string | Yes | See `/v1/formats` |

## Gradients

### POST /v1/gradient/generate

Interpolate a gradient between stops, in a chosen space. 2–4 credits.

| Field | Type | Required | Description |
|---|---|---|---|
| `stops` | colour array | Yes | Two or more colours |
| `steps` | integer | No | Samples to return |
| `space` | string | No | Interpolation space; `oklab` avoids the grey dip that `srgb` produces |

```bash
curl -X POST "https://api.auricartisan.com/v1/gradient/generate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"stops":["#c9a227","#1d2a3e"],"steps":7,"space":"oklab"}'
```

### POST /v1/gradient/analyse

Measure a gradient you already have: will it band, and where? It samples the ramp, converts each sample to OKLab and measures the perceptual distance between neighbouring samples. The verdict compares the worst step with the average one, so it does not change when you ask for more samples. Measured across 3,000 labelled gradients, that ratio has a median of 1.55 for smooth gradients and 5.09 for step-risk ones.

| Field | Type | Required | Description |
|---|---|---|---|
| `stops` | array | Yes | 2 to 64 stops, as `["#rrggbb", ...]` (evenly spaced) or `[{pos, hex}, ...]` with `pos` 0–1 |
| `steps` | number | No | Samples along the ramp, 8–1024. Default 96. |

Returns `banding`, `step_ratio`, `delta_e_mean`, `delta_e_max`, `worst_transition_at` (where the worst step is) and `note`.

```bash
curl -X POST "https://api.auricartisan.com/v1/gradient/analyse" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"stops":["#001a33","#003d66","#ffcc00"]}'
```

### POST /v1/gradient/export

Export a gradient as CSS, SVG or a design-tool format.

| Field | Type | Required | Description |
|---|---|---|---|
| `stops` | colour array | Yes | The gradient stops |
| `format` | string | Yes | See `/v1/formats` |

### POST /v1/gradient/png

Render a gradient as a PNG. 10–12 credits. Returns `image/png`.

| Field | Type | Required | Description |
|---|---|---|---|
| `stops` | colour array | Yes | The gradient stops |

## Shades

### POST /v1/shade/scale

Build a tint and shade scale from one colour. 2–4 credits.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | The base colour |
| `steps` | integer | No | Steps in the scale |

```bash
curl -X POST "https://api.auricartisan.com/v1/shade/scale" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#c9a227","steps":9}'
```

### POST /v1/shade/evaluate

Measure a scale you already have: does it work as a token ramp? A scale fails in one of three ways, each with a different fix, and the response says which: it **turns round** (two steps read as the same tone), its steps are **lumpy** (the largest is several times the average), or its extremes are **too close** to set text between.

| Field | Type | Required | Description |
|---|---|---|---|
| `steps` | array | Yes | 3 to 64 colours as `["#rrggbb", ...]`, in scale order |

Returns `verdict`, `notes`, `monotonic`, `step_ratio`, `evenness`, `usable_span` and `text_pairs`.

```bash
curl -X POST "https://api.auricartisan.com/v1/shade/evaluate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"steps":["#FFFFFF","#E0E0E0","#A0A0A0","#606060","#202020"]}'
```

### POST /v1/shade/export

Export a shade scale.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | Base colour of the scale |
| `format` | string | Yes | See `/v1/formats` |

## Related pages

- [Collections](collections.md), to browse ready-made palettes, harmonies, gradients and scales
- [Design tokens and personalisation](tokens-and-personalisation.md)
