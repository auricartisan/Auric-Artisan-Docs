---
title: Public API — Usage, jobs, webhooks and GraphQL
description: Read your usage history and live feed, run long work as asynchronous jobs, subscribe to webhooks, and query the API through GraphQL.
product: Services › Public API
updated: 2026-09-25
---

# Usage, jobs, webhooks and GraphQL

## Usage

### GET /v1/usage

Per-day, per-endpoint usage history.

| Parameter | In | Description |
|---|---|---|
| `since` | query | Earliest day to include, `YYYY-MM-DD`. Defaults to seven days back. |

```bash
curl "https://api.auricartisan.com/v1/usage" \
  -H "x-api-key: $AURIC_API_KEY"
```

### GET /v1/usage/me

Your tier, limits and month-to-date consumption.

```bash
curl "https://api.auricartisan.com/v1/usage/me" \
  -H "x-api-key: $AURIC_API_KEY"
```

```json
{"tier":"pro","plan":"specialist","auth_type":"api_key",
 "limits":{"rate_per_minute":300,"monthly_quota":1000000},
 "this_month":{"slot":"2026-08","used":412}}
```

`used` counts credits, not calls.

### GET /v1/usage/live

The last 100 individual calls, with rolling latency and error statistics. It answers "what is happening right now", where `/v1/usage` answers "how much have I used". Pass the returned `cursor` back as `since` to poll for new calls only.

| Parameter | In | Description |
|---|---|---|
| `limit` | query | 1–100. Default 50. |
| `since` | query | Sequence number from a previous cursor |

Returns `cursor`, `stats` and `events`.

### GET /v1/usage/stream

The same live feed, pushed over Server-Sent Events (SSE). It emits `hello` on connect with current stats, `usage` for each request, and `heartbeat` every 15 seconds. Connections are capped at 10 minutes; a browser `EventSource` reconnects on its own. 5 credits, charged once when the stream opens; events are free.

```bash
curl "https://api.auricartisan.com/v1/usage/stream" \
  -H "x-api-key: $AURIC_API_KEY"
```

## Async jobs

Long-running work runs as a job: you queue it, get an id back at once, then poll or follow it.

### GET /v1/jobs

The job types available, and what each accepts.

### POST /v1/jobs/:type

Queue a job. 25 credits. The body is the parameter set for the chosen job type, so its shape varies; `GET /v1/jobs` documents each type.

```bash
curl -X POST "https://api.auricartisan.com/v1/jobs/palette-batch" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"count":500}'
```

### GET /v1/jobs/id/:id

Poll one job. 1 credit per poll.

```bash
curl "https://api.auricartisan.com/v1/jobs/id/<id>" \
  -H "x-api-key: $AURIC_API_KEY"
```

### GET /v1/jobs/id/:id/stream

Follow a job to completion over SSE instead of polling.

## Webhooks

### GET /v1/webhooks/events

The event types you can subscribe to. Public, so you can check whether the API fits before you buy. Events mentioned in the documentation include `job.succeeded` and `quota.threshold`, which fires when you cross 80% of your included credits.

```bash
curl "https://api.auricartisan.com/v1/webhooks/events"
```

### POST /v1/webhooks

Subscribe a URL to one or more events. Deliveries are signed: verify the signature header before trusting a payload.

| Field | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | HTTPS endpoint to deliver to |
| `events` | string array | Yes | From `/v1/webhooks/events` |

```bash
curl -X POST "https://api.auricartisan.com/v1/webhooks" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"url":"https://example.com/hook","events":["job.succeeded"]}'
```

### GET /v1/webhooks, GET /v1/webhooks/:id, DELETE /v1/webhooks/:id

List your subscriptions, fetch one, or revoke one.

```bash
curl -X DELETE "https://api.auricartisan.com/v1/webhooks/<id>" \
  -H "x-api-key: $AURIC_API_KEY"
```

## GraphQL

### GET /v1/graphql

The GraphQL playground. Public.

### POST /v1/graphql

Run a GraphQL query against the same resolvers as the REST endpoints. 2–4 credits. Useful when one round trip should answer several questions, such as converting a colour, checking its contrast and simulating it at once.

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The GraphQL document |
| `variables` | object | No | Variable values |

```bash
curl -X POST "https://api.auricartisan.com/v1/graphql" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{"query":"{ contrast(foreground: \"#000\", background: \"#fff\") { ratio wcag_aa } }"}'
```

## Related pages

- [Plans, credits and quotas](../plans-credits-and-quotas.md)
- [Reference](../reference.md)
