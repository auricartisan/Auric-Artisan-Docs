---
title: Public API — Design tokens and personalisation
description: Generate a contrast-checked design-token system from one colour, export it for ten platforms, and run the brief-driven palette search and design-system generator.
product: Services › Public API
updated: 2026-09-25
---

# Design tokens and personalisation

## Design tokens

### POST /v1/tokens/generate

Turn one seed colour into a complete, contrast-checked token system. 2–4 credits. Ramps are stepped in OKLCH so every hue is perceptually even, chroma follows a gamut-aware envelope so the light and dark ends stay distinct, and foreground roles are measured: `--color-on-primary` is whichever of white or ink actually clears 4.5:1.

| Field | Type | Required | Description |
|---|---|---|---|
| `seed` | colour | Yes | The seed colour |
| `name` | string | No | System name used in file headers |
| `harmony` | string | No | `analogous` (default), `complementary`, `triadic` or `mono` |
| `include` | string array | No | Any of `color`, `space`, `radius`, `type`. Default all. |
| `dark` | boolean | No | Include dark-mode roles. Default `true`. |

Returns `meta`, `contrast`, `out_of_gamut` and `tokens`.

```bash
curl -X POST "https://api.auricartisan.com/v1/tokens/generate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"seed":"#c9a227","name":"Auric","harmony":"analogous"}'
```

### POST /v1/tokens/export

Render a token deck for a platform. There are ten targets, from CSS custom properties to Jetpack Compose.

| Field | Type | Required | Description |
|---|---|---|---|
| `tokens` | array | Yes | Objects of `{ name, value, group? }`: the `tokens` array from generate, or your own |
| `format` | string | Yes | See `/v1/tokens/formats` |
| `name` | string | No | System name for the file header |
| `raw` | boolean | No | `true` returns the file itself, as a download, instead of a JSON envelope |

```bash
curl -X POST "https://api.auricartisan.com/v1/tokens/export" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"format":"css","tokens":[{"name":"--color-primary","value":"#c9a227"}]}'
```

### GET /v1/tokens/formats

The ten token export targets.

## Personalisation

These endpoints drive the palette search behind the website's personalisation generator. A **brief** combines seed colours, style keys, an intent and weights.

### GET /v1/personalize/vocabulary

Everything a brief may name, with the ranges the engine really applies: the 18 style profiles with their chroma, lightness and saturation windows, the five intents, the 19 hue relationships and their offsets, the 17 type systems, and the gradient and poster catalogues. Read it before writing a brief. Returns `styles`, `intents`, `relationships`, `type_systems` and `limits`.

### GET /v1/personalize/presets

The 17 briefs the tool ships, in request shape; each can be posted straight to the endpoints below. Returns `count` and `presets`.

### POST /v1/personalize/pool

Grow a working set of colours from seeds and a brief. The search works within this pool. The response also returns the brief resolved to numbers.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors` | string array | No | Seed colours, up to 64. Defaults to the tool's own eight. |
| `styles` | string array | No | Style keys from the vocabulary |
| `intent` | string | No | `ui` (default), `brand`, `poster`, `editorial` or `dashboard` |
| `target` | integer | No | Pool size, 1–240. Default 64. |
| `warmth` | number | No | 0–100. Default 52. |
| `seed` | integer | No | Omit for a random one; it is always returned |

Returns `brief`, `pool` and `profile`.

```bash
curl -X POST "https://api.auricartisan.com/v1/personalize/pool" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#0F172A","#D3AF37"],"styles":["luxe","editorial"],"target":24}'
```

### POST /v1/personalize/score

Rank a palette you already have on the search's six scores: preference, harmony, diversity, contrast, style fit and accessibility. Omit `relationship` and every hue geometry is tried, with the best fit reported.

| Field | Type | Required | Description |
|---|---|---|---|
| `palette` | string array | Yes | 2–12 colours |
| `relationship` | string | No | A relationship id to measure against |
| `styles` | string array | No | The brief it is judged for |
| `intent` | string | No | One of the five intents |
| `accessibility` | number | No | 0–100, how hard accessibility is weighted. Default 72. |

Returns `score`, `measured_as`, `best_pair` and `alternatives`.

### POST /v1/personalize/palettes

Search: N candidates in, the best K out, each with its breakdown. The response reports what the sweep did: how many candidates were sampled, how many survived de-duplication and where the cut fell. Contrast and colour vision are weights in the score, not filters, so a candidate that reads badly is ranked down rather than removed.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors`, `styles`, `intent` | — | No | The brief |
| `note` | string | No | Free text, matched against curated colour memories |
| `depth` | integer | No | Candidates to sample, 8–1200. Default 320. |
| `keep` | integer | No | How many to return, 1–120. Default 24. |
| `palette_size` | integer | No | Colours per palette, 5–12. Default 6. |
| `diversity` | number | No | 0–100. Default 68. |
| `accessibility` | number | No | 0–100. Default 72. |
| `cvd_safe` | boolean | No | Weight colour-vision separation. Default `true`. |
| `unique` | boolean | No | Drop repeated signatures. Default `true`. |
| `seed` | integer | No | The same seed and brief always give the same result |

Returns `brief`, `sweep` and `palettes`.

```bash
curl -X POST "https://api.auricartisan.com/v1/personalize/palettes" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#0F172A","#D3AF37"],"styles":["luxe","editorial"],"intent":"brand","depth":400,"keep":12}'
```

### POST /v1/personalize/system

One brief in, a design system out: the sweep, then from its leading palette, gradients, type pairings, UI colour pairs with WCAG and APCA measured, poster compositions, and a token deck with tonal ramps, light, dark and high-contrast themes and a contrast matrix. `include` trims both the response and the work.

| Field | Type | Required | Description |
|---|---|---|---|
| `colors`, `styles`, `intent` | — | No | The brief |
| `include` | string array | No | Any of `palettes`, `gradients`, `typography`, `ui_pairs`, `posters`, `tokens`. Default all. |
| `derived` | integer | No | Palettes each derived section covers, 1–24. Default 8. |
| `depth` | integer | No | Candidates to sample, 8–1200. Default 320. |
| `keep` | integer | No | Palettes to keep, 1–120. Default 24. |
| `seed` | integer | No | Omit for a random one; it is always returned |

Returns `leader`, `palettes`, `gradients`, `typography`, `ui_pairs`, `posters` and `tokens`.

```bash
curl -X POST "https://api.auricartisan.com/v1/personalize/system" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#0F172A","#D3AF37"],"styles":["tech","minimal"],"intent":"ui","include":["tokens","ui_pairs"]}'
```

## Related pages

- [Palettes, harmonies, gradients and shades](palettes-harmonies-gradients-shades.md)
- [Accessibility](accessibility.md)
