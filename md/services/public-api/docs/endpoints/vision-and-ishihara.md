---
title: Public API — Vision and Ishihara
description: Simulate colour-vision deficiencies for a colour, a palette or an image, find pairs that become indistinguishable, and generate Ishihara plates.
product: Services › Public API
updated: 2026-09-25
---

# Vision and Ishihara

The vision endpoints distinguish two kinds of identifier:

- **Models** are simulation engines, such as `brettel-deutan`. List them with `GET /v1/vision/models`.
- **Conditions** are documented vision conditions, such as `deuteranopia` or `glaucoma`. List them with `GET /v1/vision/conditions`.

`/v1/vision/simulate` takes a model. The palette and audit endpoints take conditions.

## GET /v1/vision/models

The colour-vision deficiency models available.

## GET /v1/vision/conditions

Every documented vision condition, and what can simulate it.

## GET /v1/vision/conditions/:slug

One condition, with its severity, prevalence and a worked example. `:slug` is a condition slug such as `deuteranopia` or `glaucoma`. An unknown slug returns `UNKNOWN_CONDITION`.

```bash
curl "https://api.auricartisan.com/v1/vision/conditions/deuteranopia" \
  -H "x-api-key: $AURIC_API_KEY"
```

## GET /v1/vision/matrices

The colour-vision deficiency matrices, for applying the transform yourself.

## POST /v1/vision/simulate

How one colour appears under a vision deficiency. 1 credit.

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | colour | Yes | The colour |
| `model` | string | Yes | A model id such as `brettel-deutan`; see `/v1/vision/models` |
| `severity` | number | No | 0–1, for anomalous trichromacy |

A condition slug such as `deuteranopia` is refused here; the error names the model it maps to. To work with conditions, use `POST /v1/vision/palette`.

```bash
curl -X POST "https://api.auricartisan.com/v1/vision/simulate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#c9a227","model":"brettel-deutan","severity":1}'
```

## POST /v1/vision/palette

Run a whole palette through many conditions in one call.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | array | Yes | Up to 64 colours |
| `conditions` | array | No | Condition slugs. Omit for all 17 colour conditions. Spatial conditions are listed under `refused`. |
| `severity` | number | No | 0–1, overriding each condition's default |
| `passes` | number | No | 1–8; repeats the transform |

```bash
curl -X POST "https://api.auricartisan.com/v1/vision/palette" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#D3AF37","#2E8B57"],"conditions":["deuteranopia","tritanopia"]}'
```

## POST /v1/vision/audit

Find which pairs in a palette stop being distinguishable under each condition.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | array | Yes | At least 2, up to 64 |
| `conditions` | array | No | Omit for all 17 colour conditions |
| `threshold` | number | No | CIEDE2000 difference below which a pair counts as collapsed. Default 5. |

```bash
curl -X POST "https://api.auricartisan.com/v1/vision/audit" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#B22222","#228B22"],"conditions":["deuteranopia"]}'
```

## POST /v1/vision/simulate-image

Simulate a vision deficiency across a whole image. 10–12 credits. Returns `image/png`.

| Field | Type | Required | Description |
|---|---|---|---|
| `image` | string | Yes | Base64 or a data URL (up to 4 MB) |
| `model` | string | Yes | The deficiency to simulate |

## POST /v1/ishihara/plate

Generate an Ishihara test plate as structured data.

| Field | Type | Required | Description |
|---|---|---|---|
| `figure` | string | Yes | Digits to hide in the plate, for example `74` |
| `axis` | string | No | Deficiency to discriminate: `protan`, `deutan` (default) or `tritan` |
| `size` | integer | No | Plate size in pixels, 64–1024. Default 400. |
| `dots` | integer | No | Dot count, 50–5000. Default 800. |
| `seed` | integer | No | For a repeatable plate |

```bash
curl -X POST "https://api.auricartisan.com/v1/ishihara/plate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"figure":"74","axis":"deutan","size":400}'
```

## POST /v1/ishihara/png

Render an Ishihara plate as a PNG. 10–12 credits. Returns `image/png`.

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | string | No | Digits to hide in the plate |

> **Note:** Generated plates are for design, teaching and demonstration. They are not a clinical colour-vision test.

## Related pages

- [Accessibility](accessibility.md)
- [Limits and accuracy](../../others/limits-and-accuracy.md)
