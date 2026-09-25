---
title: Public API — Overview
description: What the Auric Artisan REST API is, who it is for, where to find it, and how to make a first call.
product: Services › Public API
updated: 2026-09-25
---

# Auric Artisan REST API

The Auric Artisan REST API exposes the platform's colour-science toolkit as JSON over HTTPS: colour conversions across 63 colour spaces, palettes, harmonies, gradients, shade scales and design tokens, WCAG and APCA accessibility checks, colour-vision deficiency simulation, Ishihara plates, a URL analyzer, and large browsable collections of colours, palettes, harmonies, gradients, shade scales and accessible colour pairs. Every endpoint lives under `/v1`.

You authenticate with an API key you create in your Auric Artisan account dashboard. Usage is metered in **credits**: one credit for a standard request, more for heavier work such as rendering images. API access is included from the **Specialist** plan upward, with a monthly credit allowance, a per-minute rate limit and optional prepaid overage. Discovery endpoints, such as the index, the catalogue and the OpenAPI document, are open to everyone so you can evaluate the API before buying.

The API is documented on the site at https://auricartisan.com/library/documentation/api/, with a separate guide to the analyzer endpoints at https://auricartisan.com/library/documentation/api/analyzer/. The API also serves its own interactive reference and OpenAPI 3.1 document.

## Who it is for

- **Developers** building colour or accessibility features into products, design tools, CMSs or build pipelines.
- **Design-system teams** generating and checking tokens, scales and palettes automatically.
- **Accessibility and QA teams** checking colour pairs and watching many pages for metadata, security-header and markup regressions.
- **Data and research users** browsing the colour, palette and contrast collections with citable record ids.

## Where to find it

| What | Where |
|---|---|
| Base URL | https://api.auricartisan.com |
| Documentation | https://auricartisan.com/library/documentation/api/ |
| Analyzer API guide | https://auricartisan.com/library/documentation/api/analyzer/ |
| Interactive reference | https://api.auricartisan.com/v1/docs |
| OpenAPI 3.1 document | https://api.auricartisan.com/v1/openapi.yaml |
| API keys | Your account dashboard, https://auricartisan.com/auth/dashboard/ |

## Quick start

1. Make sure your account is on a plan that includes API access: **Specialist** or **Industrial Pro**.
2. Open your dashboard, find **Your API Keys**, and choose **Create your first key** (or **Create key**).
3. Name the key, for example "CI pipeline", and choose **Create**.
4. Copy the key straight away. "This is the only time the full key is shown."
5. Send it in the `x-api-key` header with a request:

   ```bash
   curl -X POST https://api.auricartisan.com/v1/color/convert \
     -H "x-api-key: aa_YOUR_KEY" \
     -H "Content-Type: application/json" \
     -d '{"color": "#d3af37", "to": "oklch"}'
   ```

6. Read the JSON response, and the `x-credits-cost` and `x-quota-remaining` headers that say what the call cost and what you have left.
7. Call `GET /v1` or `GET /v1/catalog` to see everything else the API can do.

## What you can do

- Convert colours between common spaces, or any of 63 registry spaces with white-point control.
- Measure perceptual colour difference (CIEDE2000, CIE94, CIE76, CMC) and correlated colour temperature.
- Generate, score and export palettes, harmonies, gradients and shade scales, and render them as PNG.
- Turn one seed colour into a complete, contrast-checked design-token system and export it for ten platforms.
- Check foreground and background pairs against WCAG 2.2 and APCA, get the nearest accessible alternative, map where accessible colours lie on a background, and audit a palette.
- Simulate colour-vision deficiencies for colours, palettes and images, and find pairs that stop being distinguishable.
- Generate Ishihara test plates.
- Audit a web page's markup for SEO, metadata, security headers, sitemap and responsive signals, and render the report as HTML or PDF.
- Browse the colour atlas and the palette, harmony, gradient, shade and accessibility collections.
- Track usage, run long jobs asynchronously, subscribe to webhooks, and query everything through GraphQL.

## In this folder

- [docs/](docs/README.md)
  - [Getting started](docs/getting-started.md)
  - [Authentication](docs/authentication.md)
  - [Plans, credits and quotas](docs/plans-credits-and-quotas.md)
  - [Endpoints](docs/endpoints/README.md)
  - [Request examples](docs/examples.md)
  - [Errors](docs/errors.md)
  - [SDKs and tooling](docs/sdks-and-tooling.md)
  - [Reference](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md)
  - [Glossary](others/glossary.md)
  - [Limits and accuracy](others/limits-and-accuracy.md)
  - [Related](others/related.md)
  - [Release notes](others/release-notes.md)
  - [Privacy](others/privacy.md)
