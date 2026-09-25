---
title: Public API — Colour and colour science
description: Convert colours, check a contrast ratio, and use the 63-space colour registry, dossiers, Delta E, colour temperature, illuminants and difference metrics.
product: Services › Public API
updated: 2026-09-25
---

# Colour and colour science

## POST /v1/color/convert

Convert one colour between the common spaces. 1 credit. For the full 63-space registry with white-point control, use `/v1/science/convert`.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `[r,g,b]` or `{r,g,b}` |
| `to` | string | No | One target space. Omit it to get every common space at once. |

```bash
curl -X POST "https://api.auricartisan.com/v1/color/convert" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#c9a227","to":"lab"}'
```

## POST /v1/color/contrast

The WCAG contrast ratio between two colours, with pass or fail at each level. 1 credit.

| Field | Type | Required | Description |
|---|---|---|---|
| `fg` | colour | Yes | Foreground colour |
| `bg` | colour | Yes | Background colour |
| `deltaE` | number | No | Difference formula: 76, 94 or 2000 (the default) |

Returns `ratio` (number), `aa`, `aaa` and `aa_large` (booleans).

```bash
curl -X POST "https://api.auricartisan.com/v1/color/contrast" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"fg":"#767676","bg":"#ffffff"}'
```

For WCAG 2.2 and APCA together, use [`/v1/accessibility/check`](accessibility.md).

## GET /v1/science/spaces

Every colour space the platform knows, with provenance: sixty-three spaces across RGB working spaces, CIE spaces, perceptual and appearance models, HDR containers, print and video.

| Parameter | In | Required | Description |
|---|---|---|---|
| `category` | query | No | `rgb`, `cie`, `perceptual`, `cylindrical`, `appearance`, `hdr`, `print`, `video`, `order` or `opponent` |
| `full` | query | No | `true` to include matrices, primaries and transfer functions |

```bash
curl "https://api.auricartisan.com/v1/science/spaces?category=perceptual" \
  -H "x-api-key: $AURIC_API_KEY"
```

## GET /v1/science/spaces/:key

One colour space in full, including its conversion matrices.

| Parameter | In | Required | Description |
|---|---|---|---|
| `key` | path | Yes | For example `oklch`, `display-p3` or `acescct` |

An unknown key returns `404 UNKNOWN_SPACE`, and the response suggests near matches.

```bash
curl "https://api.auricartisan.com/v1/science/spaces/oklch" \
  -H "x-api-key: $AURIC_API_KEY"
```

## POST /v1/science/convert

Convert a colour into any registry space, or several at once. 1 credit.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | The colour to convert |
| `to` | string or string array | Yes | One space key, or an array of them |
| `white_point` | string | No | Reference white; default D65 |

```bash
curl -X POST "https://api.auricartisan.com/v1/science/convert" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#c9a227","to":["lab","oklch","display-p3"]}'
```

## POST /v1/science/dossier

One colour in every space at once, plus its colour temperature. 5 credits. It is expensive compared with convert: use it when you want everything, not three spaces.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | The colour |
| `white_point` | string | No | Reference white; default D65 |
| `category` | string | No | Restrict to one category |

```bash
curl -X POST "https://api.auricartisan.com/v1/science/dossier" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#c9a227"}'
```

## POST /v1/science/delta-e

The perceptual difference between two colours, 2–4 credits. It returns CIE76, CIE94, CIEDE2000 and CMC together, with a plain-language band. CIEDE2000 is the headline figure and is verified against the Sharma reference set.

| Field | Type | Required | Description |
|---|---|---|---|
| `from` | colour | Yes | First colour |
| `to` | colour | Yes | Second colour |
| `metric` | string | No | `ciede2000` (the default headline), `cie94`, `cie76`, `cmc` or `all` |
| `application` | string | No | CIE94 only: `graphic` (default) or `textile` |
| `l` | number | No | CMC lightness weight; default 2 |
| `c` | number | No | CMC chroma weight; default 1 |

Returns `delta_e` (number), `band` (string) and `metrics` (object).

```bash
curl -X POST "https://api.auricartisan.com/v1/science/delta-e" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"from":"#c9a227","to":"#d3af37"}'
```

## POST /v1/science/temperature

The correlated colour temperature (CCT) of a colour, or the colour of a temperature. 2–4 credits. Send `color` to measure or `kelvin` to render. It always returns Duv alongside the CCT: beyond about ±0.05 the colour is too far from the Planckian locus for a temperature to describe it, and `meaningful` says so.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | No | Measure this colour; not with `kelvin` |
| `kelvin` | number | No | Render this temperature, 1667–25000 K |

Returns `cct_kelvin` (number), `duv` (number), `meaningful` (boolean) and `tint` (string).

```bash
curl -X POST "https://api.auricartisan.com/v1/science/temperature" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#fff5e1"}'
```

## GET /v1/science/illuminants

Standard reference illuminants with their chromaticities.

```bash
curl "https://api.auricartisan.com/v1/science/illuminants" \
  -H "x-api-key: $AURIC_API_KEY"
```

## GET /v1/science/metrics

The difference formulae, their options, and when to use each.

```bash
curl "https://api.auricartisan.com/v1/science/metrics" \
  -H "x-api-key: $AURIC_API_KEY"
```

## Related pages

- [Collections](collections.md), including the colour atlas and nearest-colour search
- [Glossary](../../others/glossary.md)
