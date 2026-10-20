---
title: Public API — Reference
description: Every customer endpoint of the Auric Artisan REST API with its method, authentication, credit cost and purpose, plus the headers, input formats, plans and limits.
product: Services › Public API
updated: 2026-09-25
---

# Reference

## Essentials

| Item | Value |
|---|---|
| Base URL | https://api.auricartisan.com |
| Version prefix | `/v1` |
| Format | JSON over HTTPS |
| Authentication | `x-api-key` header (or `?key=` query), or `Authorization: Bearer` from the CLI |
| Key prefix | `aa_` |
| Keys per account | Up to 10 active |
| Revocation | Takes effect within a minute |
| Specification | `GET /v1/openapi.yaml` (OpenAPI 3.1); `GET /v1/catalog` (JSON) |
| Interactive reference | `GET /v1/docs` |

## Colour input

Unless a field says otherwise, a colour can be sent as `#rrggbb`, `#rgb`, `rgb(r,g,b)`, an array `[r,g,b]` or an object `{r,g,b}`. Image fields take Base64 or a data URL.

## Endpoints

Auth "None" means public and unmetered; "Key" needs an API key or bearer token. Credits are per call; see [Plans, credits and quotas](plans-credits-and-quotas.md). The documentation gives some costs as ranges (2–4, 10–12); the exact cost of every call is returned in `x-credits-cost`. Endpoints the documentation does not weight separately bill as standard work, 1 credit.

| Method | Path | Auth | Credits | Summary |
|---|---|---|---|---|
| GET | `/v1` | None | — | Index of every endpoint, with the current version |
| GET | `/v1/health` | None | — | Liveness probe; always cheap, never touches storage |
| GET | `/v1/ready` | None | — | Readiness probe: whether each backing store is bound |
| GET | `/v1/methods/:tool` | Key | 1 | The algorithms a given tool supports |
| GET | `/v1/formats` | None | — | Every export format, across every exportable resource |
| GET | `/v1/tiers` | None | — | Rate limit and monthly quota for each tier |
| GET | `/v1/metrics` | None | — | Process-level counters in Prometheus format |
| GET | `/v1/status` | None | — | Human-readable status page |
| GET | `/v1/catalog` | None | — | Every endpoint with its parameters and examples, as JSON |
| GET | `/v1/docs` | None | — | Interactive reference (Redoc) |
| GET | `/v1/openapi.yaml` | None | — | The OpenAPI 3.1 document |
| GET | `/v1/graphql` | None | — | GraphQL playground |
| POST | `/v1/graphql` | Key | 2–4 | Run a GraphQL query against the same resolvers as the REST endpoints |
| POST | `/v1/color/convert` | Key | 1 | Convert one colour between the common spaces |
| GET | `/v1/color/atlas` | Key | 1 | Browse the 8,192-colour atlas under a filter |
| GET | `/v1/color/atlas/stats` | Key | 1 | What the atlas actually contains |
| GET | `/v1/color/atlas/:id` | Key | 1 | Resolve one sample, whole |
| POST | `/v1/color/nearest` | Key | 1 | The catalogued colours closest to one you already have |
| POST | `/v1/color/contrast` | Key | 1 | WCAG contrast ratio between two colours, with pass or fail at each level |
| GET | `/v1/science/spaces` | Key | 1 | Every colour space the platform knows, with provenance |
| GET | `/v1/science/spaces/:key` | Key | 1 | One colour space in full, including its conversion matrices |
| POST | `/v1/science/convert` | Key | 1 | Convert a colour into any registry space, or several at once |
| POST | `/v1/science/dossier` | Key | 5 | One colour in every space at once, plus its colour temperature |
| POST | `/v1/science/delta-e` | Key | 2–4 | Perceptual difference between two colours |
| POST | `/v1/science/temperature` | Key | 2–4 | Correlated colour temperature from a colour, or the colour of a temperature |
| GET | `/v1/science/illuminants` | Key | 1 | Standard reference illuminants with their chromaticities |
| GET | `/v1/science/metrics` | Key | 1 | The difference formulae, their options, and when to use each |
| POST | `/v1/palette/generate` | Key | 2–4 | Generate a palette from a seed colour |
| POST | `/v1/palette/evaluate` | Key | 1 | Score a palette for harmony, contrast and accessibility |
| POST | `/v1/palette/export` | Key | 1 | Render a palette into a file format |
| POST | `/v1/palette/from-image` | Key | 10–12 | Extract a palette from an uploaded image |
| POST | `/v1/palette/png` | Key | 10–12 | Render a palette as a PNG swatch sheet |
| POST | `/v1/harmony/generate` | Key | 2–4 | Build a harmony set from a base colour |
| POST | `/v1/harmony/classify` | Key | 1 | Identify which harmony an existing set of colours follows |
| POST | `/v1/harmony/export` | Key | 1 | Export a harmony set |
| POST | `/v1/gradient/generate` | Key | 2–4 | Interpolate a gradient between stops, in a chosen space |
| GET | `/v1/shade/library` | Key | 1 | Browse 8,192 measured shade scales under a filter |
| GET | `/v1/shade/library/stats` | Key | 1 | What the shade collection contains |
| GET | `/v1/shade/library/:id` | Key | 1 | One scale, whole, with every measurement |
| POST | `/v1/shade/evaluate` | Key | 1 | Measure a scale you already have: does it work as a token ramp? |
| GET | `/v1/palette/library` | Key | 1 | Browse five million generated palettes under a filter |
| GET | `/v1/palette/library/stats` | Key | 1 | What the palette collection looks like, measured on a stated sample |
| GET | `/v1/palette/library/:id` | Key | 1 | One palette, whole, with the derivation that reproduces it |
| GET | `/v1/harmony/library` | Key | 1 | Browse the 8,192-harmony collection under a filter |
| GET | `/v1/harmony/library/stats` | Key | 1 | What the harmony collection contains |
| GET | `/v1/harmony/library/:id` | Key | 1 | One harmony, whole, with the derivation that reproduces it |
| POST | `/v1/harmony/identify` | Key | 1 | Name the scheme your colours form |
| GET | `/v1/gradient/library` | Key | 1 | Browse the 8,192-gradient collection under a filter |
| GET | `/v1/gradient/library/stats` | Key | 1 | What the gradient collection contains |
| GET | `/v1/gradient/library/:id` | Key | 1 | One gradient, whole |
| POST | `/v1/gradient/analyse` | Key | 1 | Measure a gradient you already have: will it band, and where? |
| POST | `/v1/gradient/export` | Key | 1 | Export a gradient as CSS, SVG or a design-tool format |
| POST | `/v1/gradient/png` | Key | 10–12 | Render a gradient as a PNG |
| POST | `/v1/shade/scale` | Key | 2–4 | Build a tint and shade scale from one colour |
| POST | `/v1/shade/export` | Key | 1 | Export a shade scale |
| POST | `/v1/tokens/generate` | Key | 2–4 | Turn one seed colour into a complete, contrast-checked token system |
| POST | `/v1/tokens/export` | Key | 1 | Render a token deck for a specific platform |
| GET | `/v1/tokens/formats` | Key | 1 | The ten token export targets |
| GET | `/v1/personalize/vocabulary` | Key | 1 | Everything a brief may name, with the ranges the engine applies |
| GET | `/v1/personalize/presets` | Key | 1 | The 17 briefs the tool ships, in request shape |
| POST | `/v1/personalize/pool` | Key | 1 | Grow a working set of colours from seeds and a brief |
| POST | `/v1/personalize/score` | Key | 1 | Rank a palette you already have on the search's six scores |
| POST | `/v1/personalize/palettes` | Key | 1 | Search: N candidates in, the best K out, each with its breakdown |
| POST | `/v1/personalize/system` | Key | 1 | One brief in, an entire design system out |
| POST | `/v1/accessibility/check` | Key | 1 | Check a foreground and background pair against WCAG 2.2 and APCA |
| POST | `/v1/accessibility/recommend` | Key | 1 | Suggest the nearest accessible alternative to a failing pair |
| POST | `/v1/accessibility/from-image` | Key | 10–12 | Audit the colour contrast present in an image |
| POST | `/v1/accessibility/map` | Key | 1 | The whole territory of foreground colour a background leaves you |
| POST | `/v1/accessibility/picks` | Key | 1 | A ready set of foregrounds that clear a target on one background |
| POST | `/v1/accessibility/audit` | Key | 1 | Audit a palette against one background, with a fix for each failure |
| GET | `/v1/accessibility/corpus` | Key | 1 | Browse the five-million-pair corpus under a filter, with a cursor |
| GET | `/v1/accessibility/corpus/stats` | Key | 1 | The measured distribution of contrast across the corpus |
| GET | `/v1/accessibility/corpus/:record_id` | Key | 1 | Resolve one record by id or index |
| GET | `/v1/analyzer/stages` | Key | 1 | What the analyzer can check, and how much markup alone can answer |
| POST | `/v1/analyzer/inspect` | Key | 12 | Audit one page from its markup; no browser, no rendering |
| POST | `/v1/analyzer/render` | Key | 10 | Turn a report into an HTML or PDF document |
| GET | `/v1/vision/models` | Key | 1 | The colour-vision deficiency models available |
| POST | `/v1/vision/simulate` | Key | 1 | Simulate how a colour appears under a vision deficiency |
| GET | `/v1/vision/conditions` | Key | 1 | Every documented vision condition, and what can simulate it |
| GET | `/v1/vision/conditions/:slug` | Key | 1 | One condition, with its severity, prevalence and a worked example |
| GET | `/v1/vision/matrices` | Key | 1 | The CVD matrices, for applying the transform yourself |
| POST | `/v1/vision/palette` | Key | 1 | Run a whole palette through many conditions in one call |
| POST | `/v1/vision/audit` | Key | 1 | Find which pairs in a palette stop being distinguishable |
| POST | `/v1/vision/simulate-image` | Key | 10–12 | Simulate a vision deficiency across a whole image |
| POST | `/v1/ishihara/plate` | Key | 1 | Generate an Ishihara test plate as structured data |
| POST | `/v1/ishihara/png` | Key | 10–12 | Render an Ishihara plate as a PNG |
| GET | `/v1/usage` | Key | 1 | Per-day, per-endpoint usage history |
| GET | `/v1/usage/me` | Key | 1 | Your tier, limits and month-to-date consumption |
| GET | `/v1/usage/live` | Key | 1 | The last 100 calls, with rolling latency and error stats |
| GET | `/v1/usage/stream` | Key | 5 | The same live feed over Server-Sent Events (charged once per stream) |
| GET | `/v1/jobs` | Key | 1 | The async job types available |
| POST | `/v1/jobs/:type` | Key | 25 | Queue a long-running job and get an id back immediately |
| GET | `/v1/jobs/id/:id` | Key | 1 | Poll one job |
| GET | `/v1/jobs/id/:id/stream` | Key | 1 | Follow a job to completion over SSE |
| GET | `/v1/webhooks/events` | None | — | Event types you can subscribe to |
| GET | `/v1/webhooks` | Key | 1 | List your webhook subscriptions |
| POST | `/v1/webhooks` | Key | 1 | Subscribe a URL to one or more events |
| GET | `/v1/webhooks/:id` | Key | 1 | Fetch one subscription |
| DELETE | `/v1/webhooks/:id` | Key | 1 | Revoke a subscription |

The groups are explained, with parameters and examples, in [Endpoints](endpoints/README.md).

## Response headers

| Header | Meaning |
|---|---|
| `x-ratelimit-limit` | Requests allowed per minute |
| `x-ratelimit-remaining` | Requests left this minute |
| `x-ratelimit-reset` | Minute reset, in Unix seconds |
| `x-quota-limit` | Included credits this month |
| `x-quota-used` | Credits used this month |
| `x-quota-remaining` | Included credits left |
| `x-quota-reset` | Monthly reset, in Unix seconds |
| `x-credits-cost` | Credits this call consumed |
| `x-credits-overage` | Overage credits this call used (only when paid from the prepaid balance) |
| `x-overage-cost-usd` | 1.00 when the call opened a new 100,000-credit block, otherwise 0.00 |
| `x-credits-ceiling` | The account's hard ceiling |
| `Retry-After` | With 429: when to retry |
| `Allow` | With 405: the accepted methods |

## Plans

| Plan | API | Requests per minute | Credits per month | Hard ceiling | Max keys |
|---|---|---|---|---|---|
| Apprentice (free) | Not included | — | — | — | — |
| Artisan | Not included | — | — | — | — |
| Specialist | Included | 300 | 1,000,000 | 10,000,000 | 10 |
| Industrial Pro | Included | 3,000 | 10,000,000 | 100,000,000 | 10 |

Overage is opt-in and prepaid at $1.00 (₹85) per 100,000 credits, with a monthly spend cap of up to $10,000.

## Limits stated in the documentation

| Limit | Value |
|---|---|
| Request body for image endpoints | 4 MB |
| `/v1/usage/live` | The last 100 calls; `limit` 1–100 |
| `/v1/usage/stream` | Heartbeat every 15 s; connections capped at 10 minutes |
| `/v1/palette/generate` | 1–64 colours |
| Vision palette and audit | Up to 64 colours |
| Accessibility audit | 1–64 colours |
| Ishihara plate | 64–1024 px; 50–5000 dots |
| Collection page size | Up to 200 (atlas, corpus) or 100 (libraries) |
| Corpus scan budget | `max_scan` up to 1,000,000 |
| Palette library scan budget | `max_scan` 1,000–500,000 |

## Related pages

- [Errors](errors.md)
- [Endpoints](endpoints/README.md)
