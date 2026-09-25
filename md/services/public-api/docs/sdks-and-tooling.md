---
title: Public API — SDKs and tooling
description: The official clients and integrations for the Auric Artisan API — JavaScript, Python, the CLI, an MCP server, a Postman collection and GraphQL.
product: Services › Public API
updated: 2026-09-25
---

# SDKs and tooling

The API documentation lists these official clients and integrations. All of them use the same `/v1` endpoints.

| Client | Package or location | Notes |
|---|---|---|
| JavaScript | `@auric-artisan/api` | Node 18 and later, browsers and Workers. Typed methods for every endpoint. |
| Python | `auric-artisan` | Python 3.8 and later, standard library only, no dependencies |
| CLI | `@auric-artisan/cli` | For example `auric contrast '#222' '#fff'` in your terminal |
| MCP server | Listed on the API page | Gives Claude, Cursor or any MCP host direct access to the colour tools |
| Postman | Listed on the API page | A ready-made collection covering the whole API |
| GraphQL | `POST /v1/graphql` | A single-endpoint alternative, with a playground at `GET /v1/graphql` |

> **Note:** The documentation names these packages; check your package registry for their availability and current versions before depending on them.

## The CLI and OAuth

The `auric` CLI signs in with a device flow and sends an OAuth bearer token (`Authorization: Bearer <token>`) instead of an API key. See [Authentication](authentication.md).

## Generating your own client

`GET /v1/openapi.yaml` returns the OpenAPI 3.1 document, which most API tools can import or use to generate a client. `GET /v1/catalog` returns the same information as JSON, with parameters and examples.

## Retries

The official SDKs retry automatically on `429` responses. If you write your own client, honour `retry-after`; see [Errors](errors.md).

## Related pages

- [Getting started](getting-started.md)
- [Request examples](examples.md)
