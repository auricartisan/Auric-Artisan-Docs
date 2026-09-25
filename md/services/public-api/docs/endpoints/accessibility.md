---
title: Public API — Accessibility
description: Check colour pairs against WCAG 2.2 and APCA, get accessible alternatives, audit images and palettes, map accessible foregrounds on a background, and browse the contrast corpus.
product: Services › Public API
updated: 2026-09-25
---

# Accessibility

## POST /v1/accessibility/check

Check a foreground and background pair against WCAG 2.2 and APCA. 1 credit.

| Field | Type | Required | Description |
|---|---|---|---|
| `fg` | colour | Yes | Text colour. `foreground` is accepted too. |
| `bg` | colour | Yes | The surface behind the text. `background` is accepted too. |
| `standard` | string | No | `WCAG 2.1`, `WCAG 2.2`, `WCAG 3.0`, `Auric SD Flexible`, `Auric SD Strict`, or `all` (the default) |

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/check" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"fg":"#767676","bg":"#ffffff"}'
```

## POST /v1/accessibility/recommend

Suggest the nearest accessible alternative to a failing pair. It keeps the hue and moves the lightness, so the fix still looks like the brand. `target` chooses which colour may move; set the level with `minRatio`.

| Field | Type | Required | Description |
|---|---|---|---|
| `fg` | colour | Yes | Text colour (`foreground` also accepted) |
| `bg` | colour | Yes | Surface colour (`background` also accepted) |
| `target` | string | No | Which side to move: `foreground` (default) or `background` |
| `minRatio` | number | No | Contrast ratio to reach. Default 4.5. |

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/recommend" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"fg":"#c9a227","bg":"#ffffff","target":"foreground","minRatio":4.5}'
```

## POST /v1/accessibility/from-image

Audit the colour contrast present in an image. 10–12 credits.

| Field | Type | Required | Description |
|---|---|---|---|
| `image` | string | Yes | Base64 or a data URL (up to 4 MB) |

## POST /v1/accessibility/map

The whole territory of foreground colour a background leaves you. For each hue, it returns the lightness at which the most saturated colour of that hue just reaches the target on this background. `territory_pct` is the share of the slice that qualifies, so one background can be compared with another. A `null` lightness means that hue never reaches the target at any lightness.

| Field | Type | Required | Description |
|---|---|---|---|
| `ground` | colour | Yes | The background colour |
| `targets` | number array | No | Contrast ratios to contour. Default `[3, 4.5, 7]`, at most 6. |
| `resolution` | number | No | Hues sampled around the circle, 12–360. Default 72. |

Returns `ground`, `polarity` and `contours`.

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/map" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"ground":"#1D2A3E","targets":[4.5,7]}'
```

## POST /v1/accessibility/picks

A ready set of foreground colours that clear a target on one background. It walks the hue circle, takes each hue to its boundary lightness, then steps a margin past it so rounding cannot land a pick under the target. Hues that cannot make it are dropped and counted.

| Field | Type | Required | Description |
|---|---|---|---|
| `ground` | colour | Yes | The background colour |
| `target` | number | No | Contrast ratio to clear. Default 4.5. |
| `count` | number | No | Hues to try, 1–72. Default 12. |
| `margin` | number | No | Lightness held back from the boundary, 0–0.5. Default 0.10. |

Returns `count`, `dropped` and `picks`.

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/picks" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"ground":"#1D2A3E","target":4.5,"count":12}'
```

## POST /v1/accessibility/audit

Audit a palette against one background, with a fix for each failure. The fix keeps the hue and moves the lightness onto the contour. Where a hue cannot reach the target on that background at all, the response says so instead of returning a colour that does not work.

| Field | Type | Required | Description |
|---|---|---|---|
| `ground` | colour | Yes | The background everything sits on |
| `colors` | colour array | Yes | The palette, 1–64 colours |
| `target` | number | No | Contrast ratio to clear. Default 4.5. |

Returns `verdict`, `passing`, `failing` and `results`.

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/audit" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"ground":"#1D2A3E","colors":["#D3AF37","#4A5568","#F7FAFC"],"target":4.5}'
```

## The contrast corpus

A corpus of five million colour pairs, derived from a seed rather than stored, so paging is cheap and any record can be recomputed. Most pairs are unusable: 88% of the corpus fails AA for body text, so a filter for rare pairs scans many records per result.

### GET /v1/accessibility/corpus

| Parameter | Description |
|---|---|
| `min_ratio`, `max_ratio` | Contrast ratio bounds, 1–21 |
| `level` | `AA`, `AAA`, `fail` or `any` (default) |
| `grade` | Auric SD grade: `A+`, `A`, `B`, `C`, `D`, `F` |
| `polarity` | `BoW` (dark on light), `WoB` or `any` |
| `limit` | Records per page, 1–200. Default 24. |
| `cursor` | Corpus index to resume from; use `next_cursor` |
| `max_scan` | Records this call may examine. Default 100,000, maximum 1,000,000. |
| `full` | `true` for the complete record, including all ten vision models |

Returns `count`, `scanned`, `hit_rate`, `next_cursor`, `exhausted`, `truncated` and `records`. When `truncated` is `true`, the scan budget ran out before the page filled: follow `next_cursor`.

```bash
curl "https://api.auricartisan.com/v1/accessibility/corpus?level=AAA&limit=5" \
  -H "x-api-key: $AURIC_API_KEY"
```

### GET /v1/accessibility/corpus/stats

The measured distribution of contrast across the corpus, from a deterministic sample, so the same sample always gives the same numbers.

| Parameter | Description |
|---|---|
| `sample` | Records to measure, 1,000–1,000,000. Default 200,000. |

Returns `sample`, `mean_contrast_ratio`, `share_at_least`, `share_failing_aa_body` and `distribution`.

### GET /v1/accessibility/corpus/:record_id

Resolve one record, for citation: put `acc_2j` in a report and anyone can recover the same two colours. `:record_id` is a record id such as `acc_2j`, or a corpus index such as `91`. An id that does not parse, or an index outside the corpus, returns `VALIDATION_ERROR`. Returns `record`, `cite` and `recompute`.

```bash
curl "https://api.auricartisan.com/v1/accessibility/corpus/acc_2j" \
  -H "x-api-key: $AURIC_API_KEY"
```

## Related pages

- [Vision and Ishihara](vision-and-ishihara.md)
- [Colour and colour science](colour-and-science.md), for `/v1/color/contrast`
- [Limits and accuracy](../../others/limits-and-accuracy.md)
