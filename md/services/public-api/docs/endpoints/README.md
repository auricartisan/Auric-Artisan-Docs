---
title: Public API — Endpoints
description: The groups of endpoints in the Auric Artisan REST API, with a page for each group.
product: Services › Public API
updated: 2026-09-25
---

# Endpoints

Everything lives under `/v1` on https://api.auricartisan.com. Each page below covers one group of endpoints: what each does, its parameters, what it returns and an example. The [Reference](../reference.md) lists them all in one table.

## Conventions

- **Colours** in request bodies can be written as `#rrggbb`, `#rgb`, `rgb(r,g,b)`, an array `[r,g,b]` or an object `{r,g,b}`, unless a field says otherwise.
- **Tool endpoints** take JSON through `POST`, with `content-type: application/json`.
- **Collection endpoints** take query parameters through `GET` and page with `offset` and `next_offset`, or with `cursor` and `next_cursor` for the scanned collections.
- **Path parameters** are written `:name`, for example `/v1/science/spaces/:key`.
- Examples use `$AURIC_API_KEY` for your key.
- **Auth** "None" means the endpoint is public and unmetered. Everything else needs a key; see [Authentication](../authentication.md).

## Pages

| Page | Endpoints |
|---|---|
| [Discovery](discovery.md) | Index, health, readiness, methods, formats, tiers, status, metrics, catalogue, docs, OpenAPI |
| [Colour and colour science](colour-and-science.md) | Convert, contrast, the 63-space registry, dossier, Delta E, colour temperature, illuminants, metrics |
| [Palettes, harmonies, gradients and shades](palettes-harmonies-gradients-shades.md) | Generate, evaluate, classify, analyse, export and render |
| [Collections](collections.md) | The colour atlas, nearest colour, and the palette, harmony, gradient and shade libraries |
| [Design tokens and personalisation](tokens-and-personalisation.md) | Token systems and exports; brief-driven palette search and design systems |
| [Accessibility](accessibility.md) | WCAG and APCA checks, recommendations, image audits, maps, picks, palette audits, the contrast corpus |
| [Vision and Ishihara](vision-and-ishihara.md) | Colour-vision models, conditions, matrices, simulations and audits; Ishihara plates |
| [Analyzer](analyzer.md) | Stages, markup-only page audits, and rendering reports to HTML or PDF |
| [Usage, jobs, webhooks and GraphQL](usage-jobs-webhooks-graphql.md) | Usage history and live feed, async jobs, webhooks, GraphQL |
