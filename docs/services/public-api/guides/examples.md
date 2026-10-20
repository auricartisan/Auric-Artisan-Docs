---
title: Public API — Request examples
description: Ready-to-run requests for common tasks with the Auric Artisan API.
product: Services › Public API
updated: 2026-09-25
---

# Request examples

Replace `aa_YOUR_KEY` with your key, or set `AURIC_API_KEY` in your shell and use `$AURIC_API_KEY`.

## Convert a colour to OKLCH

```bash
curl -X POST https://api.auricartisan.com/v1/color/convert \
  -H "x-api-key: aa_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"color": "#d3af37", "to": "oklch"}'
# → {"input":{"rgb":[211,175,55],"hex":"#d3af37"},"to":"oklch",
#    "value":[0.7655,0.1384,91.55]}
```

## Check contrast

```bash
curl -X POST https://api.auricartisan.com/v1/color/contrast \
  -H "x-api-key: aa_YOUR_KEY" -H "Content-Type: application/json" \
  -d '{"fg": "#1a1712", "bg": "#d3af37"}'
```

For WCAG 2.2 and APCA together:

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/check" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"fg":"#767676","bg":"#ffffff"}'
```

## Fix a failing pair

```bash
curl -X POST "https://api.auricartisan.com/v1/accessibility/recommend" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"fg":"#c9a227","bg":"#ffffff","target":"foreground","minRatio":4.5}'
```

## Generate a palette

```bash
curl -X POST https://api.auricartisan.com/v1/palette/generate \
  -H "x-api-key: aa_YOUR_KEY" -H "Content-Type: application/json" \
  -d '{"method": "analogous", "count": 5, "hue": 45}'
```

## Simulate colour-vision deficiency

```bash
curl -X POST "https://api.auricartisan.com/v1/vision/simulate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"color":"#c9a227","model":"brettel-deutan","severity":1}'
```

`model` takes a model id from `GET /v1/vision/models`. To work with condition names such as `protanopia`, use `/v1/vision/palette`:

```bash
curl -X POST "https://api.auricartisan.com/v1/vision/palette" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"colors":["#D3AF37","#2E8B57"],"conditions":["deuteranopia","tritanopia"]}'
```

## Build a token system and export it

```bash
curl -X POST "https://api.auricartisan.com/v1/tokens/generate" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"seed":"#c9a227","name":"Auric","harmony":"analogous"}'

curl -X POST "https://api.auricartisan.com/v1/tokens/export" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"format":"css","tokens":[{"name":"--color-primary","value":"#c9a227"}]}'
```

## Audit a page's metadata

```bash
curl -X POST "https://api.auricartisan.com/v1/analyzer/inspect" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{ "url": "https://example.com/", "scope": ["seo"] }'
```

## Check your usage

```bash
curl https://api.auricartisan.com/v1/usage/me -H "x-api-key: aa_YOUR_KEY"
# → {"tier":"pro","plan":"specialist","auth_type":"api_key",
#    "limits":{"rate_per_minute":300,"monthly_quota":1000000},
#    "this_month":{"slot":"2026-08","used":412}}
#
# `used` counts credits, not calls.
```

## From JavaScript

```js
const res = await fetch("https://api.auricartisan.com/v1/color/contrast", {
  method: "POST",
  headers: { "x-api-key": process.env.AURIC_API_KEY, "content-type": "application/json" },
  body: JSON.stringify({ fg: "#767676", bg: "#ffffff" }),
});
if (!res.ok) throw new Error((await res.json()).error.code);
const { ratio, aa, aaa, aa_large } = await res.json();
console.log(ratio, aa, aaa, aa_large, res.headers.get("x-credits-cost"));
```

## Related pages

- [Endpoints](endpoints/README.md)
- [SDKs and tooling](sdks-and-tooling.md)
