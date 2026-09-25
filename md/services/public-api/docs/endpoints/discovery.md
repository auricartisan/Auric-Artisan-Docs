---
title: Public API — Discovery endpoints
description: The public endpoints that describe the API itself — index, health, readiness, methods, formats, tiers, status, metrics, catalogue and documentation.
product: Services › Public API
updated: 2026-09-25
---

# Discovery endpoints

These endpoints describe the API. All but one are public and unmetered, so you can evaluate the API before buying.

| Method | Path | Auth | Purpose |
|---|---|---|---|
| GET | `/v1` | None | Index of every endpoint, with the current version |
| GET | `/v1/health` | None | Liveness probe; always cheap, never touches storage |
| GET | `/v1/ready` | None | Readiness probe: whether each backing store is bound |
| GET | `/v1/methods/:tool` | Key | The algorithms a given tool supports |
| GET | `/v1/formats` | None | Every export format, across every exportable resource |
| GET | `/v1/tiers` | None | Rate limit and monthly quota for each tier |
| GET | `/v1/metrics` | None | Process-level counters in Prometheus format |
| GET | `/v1/status` | None | Human-readable status page |
| GET | `/v1/catalog` | None | Every endpoint with its parameters and examples, as JSON |
| GET | `/v1/docs` | None | Interactive reference (Redoc) |
| GET | `/v1/openapi.yaml` | None | The OpenAPI 3.1 document |

## GET /v1

Returns `version` (string) and `endpoints` (string array).

```bash
curl "https://api.auricartisan.com/v1"
```

## GET /v1/health

Returns `ok` (boolean) and `time` (ISO 8601).

```bash
curl "https://api.auricartisan.com/v1/health"
```

## GET /v1/ready

Returns `ready` (boolean) and `checks` (object). Use it in a deployment gate: `/v1/health` says the service is up, while `/v1/ready` says it can actually serve.

```bash
curl "https://api.auricartisan.com/v1/ready"
```

## GET /v1/methods/:tool

The algorithms a tool supports. Use it to find valid `method` values, for example for `/v1/palette/generate` or `/v1/harmony/generate`.

| Parameter | In | Required | Description |
|---|---|---|---|
| `tool` | path | Yes | For example `palette`, `harmony` or `vision` |

```bash
curl "https://api.auricartisan.com/v1/methods/harmony" \
  -H "x-api-key: $AURIC_API_KEY"
```

## GET /v1/formats

Every export format for every exportable resource. The export endpoints refer to it for valid `format` values.

```bash
curl "https://api.auricartisan.com/v1/formats"
```

## GET /v1/tiers

The machine-readable plan table: rate limit and monthly quota for each tier. See [Plans, credits and quotas](../plans-credits-and-quotas.md).

```bash
curl "https://api.auricartisan.com/v1/tiers"
```

## GET /v1/catalog

The catalogue as JSON: every endpoint with its parameters and examples. It is generated from the same source as the OpenAPI document, so a client can build its own reference or check its coverage.

```bash
curl "https://api.auricartisan.com/v1/catalog"
```

## GET /v1/docs and GET /v1/openapi.yaml

`/v1/docs` is the interactive reference in the browser. `/v1/openapi.yaml` is the OpenAPI 3.1 document, for generating clients or importing into API tools.

```bash
curl "https://api.auricartisan.com/v1/openapi.yaml"
```

## GET /v1/status and GET /v1/metrics

`/v1/status` is a human-readable status page. `/v1/metrics` exposes process-level counters in Prometheus format.

## Related pages

- [Reference](../reference.md)
- [Getting started](../getting-started.md)
