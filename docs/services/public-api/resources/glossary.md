---
title: Public API — Glossary
description: Definitions of the API, colour-science and accessibility terms used in the public API documentation.
product: Services › Public API
updated: 2026-09-25
---

# Glossary

## API terms

**API key.** A secret string, starting `aa_`, that identifies your account on each request. Created in the dashboard and shown once.

**Async job.** Work that takes too long for one request. You queue it, receive an id, then poll it or follow it over SSE.

**Credit.** The unit your monthly quota is counted in. A standard call costs 1; heavier calls cost more.

**Cursor.** A position in a scanned collection. Pass `next_cursor` back as `cursor` to continue.

**Discovery endpoint.** A public, unmetered endpoint that describes the API, such as `/v1/catalog`.

**GraphQL.** A query language that lets one request ask several questions at once, through `/v1/graphql`.

**Hard ceiling.** The absolute monthly limit, ten times the included allowance, that stops runaway usage.

**OpenAPI.** A standard, machine-readable description of an HTTP API, served at `/v1/openapi.yaml`.

**Overage.** Usage beyond the included credits, paid from a prepaid credit balance, and only if you turn it on.

**Quota.** Your included credits for the month.

**Rate limit.** How many requests you may make per minute.

**Scope and stage.** In the analyzer, a stage is one group of checks; `scope` is the list of stages you ask for.

**Server-Sent Events (SSE).** A way for a server to push a stream of events over one HTTP connection, used by the usage and job streams.

**Spend cap.** A monthly limit, in money, you set on overage.

**Truncated.** A scanned-collection response whose scan budget ran out before the page filled; it does not mean nothing matches.

**Webhook.** A URL you register to receive signed event notifications, such as `job.succeeded`.

## Colour science

**CCT and Duv.** Correlated colour temperature, in kelvin, describes a near-white light by the temperature of the closest black-body colour. Duv is how far the colour sits from that black-body curve (the Planckian locus); beyond about ±0.05 a temperature no longer describes it.

**CIEDE2000, CIE94, CIE76, CMC.** Formulae for Delta E, the perceptual difference between two colours. CIEDE2000 is the most accurate and the API's headline figure.

**Colour space.** A system for describing colours with numbers. The API's registry has 63.

**Illuminant.** A standard reference light, such as D65 (average daylight), used to define white.

**OKLab and OKLCH.** Perceptual colour spaces in which equal numeric steps look like equal visual steps. OKLCH writes OKLab as lightness, chroma and hue.

**Planckian locus.** The curve of colours a black body glows at different temperatures.

**White point.** The colour a space treats as white, such as D65.

## Accessibility

**APCA.** The Accessible Perceptual Contrast Algorithm from the WCAG 3 drafts, which scores contrast as Lc with polarity.

**Auric SD.** Auric Artisan's own contrast grading, with Flexible and Strict variants and grades from A+ to F.

**Banding.** Visible steps in a gradient that should look smooth.

**Colour-vision deficiency (CVD).** Reduced ability to tell some colours apart, such as protanopia or deuteranopia.

**Contrast ratio.** WCAG's measure of the difference in luminance between two colours, from 1:1 to 21:1. Body text needs 4.5:1 at level AA.

**Polarity.** Whether text is dark on light (BoW) or light on dark (WoB).

**WCAG.** The Web Content Accessibility Guidelines.
