---
title: Public API — Troubleshooting
description: Common problems with the Auric Artisan API — keys, plans, limits, credits, inputs, collections and the analyzer — and how to fix them.
product: Services › Public API
updated: 2026-09-25
---

# Troubleshooting

## Keys and access

| Symptom | Why | What to do |
|---|---|---|
| `401` on every call | No key, a mistyped key, or a revoked key | Send the key in `x-api-key`; check it starts with `aa_`; create a new one if it was revoked or lost |
| `401` right after revoking a key | Revocation takes effect within a minute | Use another key |
| `402 PLAN_UPGRADE_REQUIRED` | Your plan does not include the API | Upgrade to Specialist or Industrial Pro |
| I cannot create a key in the dashboard | Key creation is available from the Specialist plan | Upgrade, or use the public discovery endpoints meanwhile |
| I lost a key | The full key is shown once and stored only as a hash | Create a new key and revoke the old one |
| `403 FORBIDDEN` | The key has no rights for this route | Check the path; use an endpoint listed in the [Reference](reference.md) |

## Limits and credits

| Symptom | Why | What to do |
|---|---|---|
| `429 RATE_LIMITED` | Too many requests this minute | Wait for `Retry-After`; spread calls out |
| `429 IP_RATE_LIMITED` | Too many requests from one address | Slow down, whatever key you use |
| `429 QUOTA_EXCEEDED` | Included credits used up, overage off | Turn on prepaid overage and add credits, or wait for the reset in `details.resets_at` |
| `402 INSUFFICIENT_CREDITS` | Overage on, prepaid balance empty | **Add credits** in the dashboard |
| `402 SPEND_CAP_REACHED` | Your monthly spend cap was reached | Raise the cap in the dashboard |
| `429 HARD_CEILING_REACHED` | Ten times the included allowance used this month | Contact support |
| Adding more keys did not raise my limits | Limits are pooled per account | Upgrade the plan, or use overage |
| Credits drain faster than calls | Heavier endpoints cost more than 1 credit | Read `x-credits-cost`; see [Plans, credits and quotas](plans-credits-and-quotas.md) |

## Requests

| Symptom | Why | What to do |
|---|---|---|
| `400 INVALID_JSON` | The body is not valid JSON | Check quoting, especially in shell commands |
| `400 INVALID_INPUT` | A field is missing or malformed | Read the message, which names the field |
| `405 METHOD_NOT_ALLOWED` | Wrong method, such as `GET` for a `POST` endpoint | Use the method in the `Allow` header |
| `404 NOT_FOUND` | Unknown path or id | `GET /v1` lists every endpoint |
| `413 PAYLOAD_TOO_LARGE` | Image bodies are limited to 4 MB | Resize or compress the image |
| `/v1/vision/simulate` refuses `deuteranopia` | It takes model ids, not condition names | Use a model from `/v1/vision/models`, such as `brettel-deutan`, or use `/v1/vision/palette` |
| A colour is rejected | Unsupported format | Use `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `[r,g,b]` or `{r,g,b}` |

## Collections

| Symptom | Why | What to do |
|---|---|---|
| An empty page with a `next_cursor` | The scan budget ran out before any match (`truncated: true`) | Follow `next_cursor`, or raise `max_scan` |
| Sorted results look out of order across pages | In scanned collections, sorting other than by `id` is within each scan | Check `sorted_within_scan`; sort on your side if you need a global order |

## Analyzer

| Symptom | Why | What to do |
|---|---|---|
| `score` is always `null` | Deliberate: markup alone cannot measure every category | Use `category_scores`, or run the tool for an overall score |
| `400 RENDER_REQUIRED` | Contrast, accessibility, deep, performance, before-and-after and simulation need a browser | Remove those stages, or use the tool |
| `400 EMPTY_SCOPE` | `scope` was `[]` | Omit `scope` for everything, or name stages |
| `502 FETCH_FAILED` | The page could not be read: DNS, TLS, timeout, or a private address | Check the URL is public and reachable |
| Non-Latin text missing from the PDF | The PDF uses standard fonts that cover Latin characters | Use `format: "html"` |

## Getting help

Quote the `request_id` from the error response when you contact Auric Artisan about a specific call.

## Related pages

- [Errors](errors.md)
- [FAQ](faq.md)
