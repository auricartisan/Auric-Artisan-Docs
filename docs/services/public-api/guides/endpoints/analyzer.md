---
title: Public API — Analyzer
description: Audit web pages from their markup through the API — stages and scope, what page source can and cannot answer, why there is no overall score, rendering reports, errors, recipes and costs.
product: Services › Public API
updated: 2026-09-25
---

# Analyzer

Three endpoints put the URL Analyzer behind a REST call: ask what it can check, run the checks you want against one page, and turn the result into a document. The full guide is at https://auricartisan.com/library/documentation/api/analyzer/.

| Method | Path | Credits | Purpose |
|---|---|---|---|
| GET | `/v1/analyzer/stages` | 1 | What the analyzer can check, and how much of it markup alone can answer |
| POST | `/v1/analyzer/inspect` | 12 | Audit one page from its markup. No browser, no rendering. |
| POST | `/v1/analyzer/render` | 10 | Turn a report into an HTML or PDF document |

## When to use the API, and when to use the tool

The analyzer on the website and this API differ in one way that decides which you want: the API reads a page's **source**; the tool runs the page in a real browser.

| | The tool | This API |
|---|---|---|
| Runs the page | Yes, in your browser | No: it reads the source |
| Contrast, accessibility engine, deep DOM | Yes | Refused, with a reason |
| SEO, metadata, security headers, sitemap, responsive signals | Yes | Yes |
| Good for | One page, looked at closely | Many pages, on a schedule |
| Paid with | Tool tokens | API credits |

Use the API to watch many pages for what a crawler can see: a title that went missing after a deploy, a canonical pointing at staging, a weakened Content-Security-Policy, an image that returns 404. Use the tool when you need answers that exist only once a page has been laid out and painted. API credits and tool tokens are separate balances, and neither pays for the other.

## Quick start

Audit one page for search-engine metadata:

```bash
curl -X POST "https://api.auricartisan.com/v1/analyzer/inspect" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{ "url": "https://example.com/", "scope": ["seo"] }'
```

Ask what else it can check:

```bash
curl "https://api.auricartisan.com/v1/analyzer/stages" \
  -H "x-api-key: $AURIC_API_KEY"
```

Turn a result into a PDF:

```bash
curl -X POST "https://api.auricartisan.com/v1/analyzer/render" \
  -H "x-api-key: $AURIC_API_KEY" \
  -H "content-type: application/json" \
  -d "{ \"report\": $REPORT, \"format\": \"pdf\" }" \
  --output audit.pdf
```

## Stages and scope

A full audit has fourteen **stages**. `scope` is the list of stage ids you want, and it is how you ask for less: send `["palette"]` and you get the colours, not an audit with the colours in it.

```json
{ "url": "https://example.com/", "scope": ["seo", "security"] }
```

- Omit `scope` to get everything page source can answer.
- Send `[]` and the request is refused (`EMPTY_SCOPE`); an empty list is not treated as "everything".
- `structure`, reading the page at all, is always on. Stages a request depends on are added and echoed back:

```json
"scope": {
  "requested": ["palette"],
  "effective": ["structure", "palette"],
  "added_by_dependency": ["structure"]
}
```

### Sections narrow the response, not the work

The response groups the report into **sections**, such as `core`, `seo`, `palette` and `security`. `sections` in the request narrows what comes back; `core` is always included. It does not make a run cheaper: use `scope` to do less, and `sections` to receive less.

```json
{ "url": "https://example.com/", "scope": ["seo"], "sections": ["seo"] }
```

## What page source can and cannot answer

Every stage carries a `markup` value:

| `markup` | Meaning | Stages |
|---|---|---|
| `full` | Answered completely from the source | `structure`, `project`, `seo`, `security`, `sitemap`, `responsive` |
| `partial` | A real but narrower answer, stated in `incomplete[]` | `palette`, `media` |
| `none` | Refused with `RENDER_REQUIRED`; never returned empty or guessed | `contrast`, `a11y`, `deep`, `performance`, `beforeafter`, `simulation` |

Contrast needs the colour a browser computed for each element after the whole cascade. Reading colours out of stylesheet text would pair colours that may never appear together on screen, which is a confident, wrong report. The same applies to the accessibility engine (which uses layout and visibility), target sizes (measured boxes), performance (a real page load) and the rendered-versus-raw comparison.

For the `partial` stages:

- **palette** returns every colour the stylesheets declare, which is not the same as the colours covering the most pixels;
- **media** returns every image, video and audio file in the markup, with its real size fetched; anything JavaScript inserts is invisible.

```json
"incomplete": [
  {
    "stage": "palette",
    "reason": "Declared colours only. The dominant palette is sampled from rendered pixels, which needs a browser."
  }
]
```

If `incomplete` is empty, nothing was narrowed.

## Why there is no overall score

`/v1/analyzer/inspect` always returns `score: null`. An overall score averages categories, and a markup-only run does not measure some of them; leaving them out makes the score incomparable, and filling them in makes it partly fiction. Instead you get the categories that were measured and a list of those that were not:

```json
"score": null,
"category_scores": { "metadata": 84, "seo": 85, "a11y": 68 },
"unscored_categories": [
  "accessibility", "a11yPlus", "contrast", "performance",
  "reliability", "security", "media", "visual", "deep", "responsive"
],
"scoreCoverage": { "measured": 3, "of": 13, "unmeasured": ["accessibility", "…"] }
```

If you want one number, compute it from `category_scores` with weights you choose. For a comparable overall score, run the audit in the tool.

> **Note:** The `a11y` category is the markup-level accessibility count: heading order, alt text, form labels, landmarks and `lang`. It is not the analyzer's 112-rule accessibility engine, which is `accessibility` and `a11yPlus`, always unscored here.

## GET /v1/analyzer/stages

The vocabulary, generated from the analyzer's own stage table. Call it once, cache it, and build scopes from it. 1 credit, no body.

Returns `checks_per_token`, `always_on`, `stage_ids`, `stages`, `sections` and `notes`. Each stage has `id`, `name`, `does`, `section`, `needs_render`, `markup`, `endpoint`, `caveat` and `why_unavailable`. Filtering on `markup` not equal to `"none"` gives every stage `/inspect` accepts.

```json
{
  "id": "seo",
  "name": "SEO and metadata",
  "does": "Title, description, headings, schema, robots, canonical, keyword density.",
  "section": "seo",
  "needs_render": false,
  "markup": "full",
  "endpoint": "/v1/analyzer/inspect",
  "caveat": null,
  "why_unavailable": null
}
```

## POST /v1/analyzer/inspect

12 credits, one page per call.

| Field | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Absolute `http` or `https`. Private and reserved addresses are refused. |
| `scope` | string array | No | Stage ids. Omit for everything markup can answer; `[]` is refused. |
| `sections` | string array | No | Narrows the response only; `core` is always included |

The response includes `url`, `final_url`, `audit_version`, `scope`, `score` (always `null`), `unscored_categories`, `category_scores`, `timing`, `section_index`, `sections` and `incomplete`. `section_index` summarises each section's findings count and size, so you can log it without keeping the whole report.

Only what was measured comes back. A stage outside your scope contributes nothing: asking for `["seo"]` returns no security section, and no run returns contrast pairs, the accessibility engine's audit or the deep analysis.

## POST /v1/analyzer/render

10 credits. Takes a report, one `/inspect` returned or one you stored, and renders it. No page is fetched, so it works on an old report.

| Field | Type | Required | Description |
|---|---|---|---|
| `report` | object | Yes | An analyzer report |
| `format` | string | No | `html` (default) or `pdf` |

| `format` | Content type | Notes |
|---|---|---|
| `html` | `text/html` | A self-contained document, around 14 KB for a small page |
| `pdf` | `application/pdf` | Laid out on the server, around 7 KB for the same page. Text and rules only, no screenshots. |

The PDF uses the standard PDF fonts, which cover Latin characters; content in other scripts will not appear. Use `html` for pages not in a Latin script. Markdown reports are not offered through the API; the tool still writes them from a saved audit.

## Errors

These are decided before your page is fetched, so a rejected request does no work.

| Code | Status | When |
|---|---|---|
| `UNKNOWN_STAGE` | 400 | A stage id that does not exist; the response lists the fourteen real ones |
| `EMPTY_SCOPE` | 400 | `scope: []`. Omit the field for everything, or name what you want. |
| `RENDER_REQUIRED` | 400 | A stage that needs a browser; names the offenders and what is available |
| `INVALID_INPUT` | 400 | A missing or unusable `url` |
| `UNKNOWN_FORMAT` | 400 | `/render` with a format other than `html` or `pdf` |
| `FETCH_FAILED` | 502 | Your page could not be read: DNS, TLS, a timeout, or a private address |
| `ANALYZER_UNAVAILABLE` | 503 | The analyzer backend is unavailable; `/v1/analyzer/stages` still works |

```json
{
  "error": {
    "code": "RENDER_REQUIRED",
    "message": "contrast needs a rendered page, which this endpoint does not do. GET /v1/analyzer/stages lists what markup alone can answer.",
    "details": {
      "needs_render": ["contrast"],
      "available": ["structure", "project", "palette", "seo", "media", "responsive", "security", "sitemap"]
    }
  },
  "request_id": "7140da9b-0ddf-417d-9c8b-9775a5056a01"
}
```

The shared 401, 403, 404, 405, 413 and 429 responses are on [Errors](../errors.md).

## Recipes

### Watch a page for metadata regressions

```js
const res = await fetch("https://api.auricartisan.com/v1/analyzer/inspect", {
  method: "POST",
  headers: { "x-api-key": process.env.AURIC_API_KEY, "content-type": "application/json" },
  body: JSON.stringify({ url, scope: ["seo"], sections: ["seo"] }),
});
const { sections, category_scores } = await res.json();
const meta = sections.seo.metadataAudit;
if (category_scores.seo < 80) {
  console.error(`${url}: SEO fell to ${category_scores.seo}`);
  for (const finding of sections.seo.seoAudit.findings) console.error(`  ${finding.title}`);
  process.exitCode = 1;
}
```

### Audit every page in a sitemap

One call per page, paced against your rate limit: 300 requests a minute on Specialist, 3,000 on Industrial Pro.

```js
for (const url of urls) {
  const res = await fetch(endpoint, { method: "POST", headers, body: JSON.stringify({ url, scope: ["seo", "security"] }) });
  if (res.status === 429) {                       // slow down and retry this one
    await new Promise((r) => setTimeout(r, Number(res.headers.get("retry-after") || 5) * 1000));
    continue;
  }
  const audit = await res.json();
  results.push({ url, scores: audit.category_scores, findings: audit.sections });
}
```

`x-quota-remaining` comes back on every response, so you can stop before you run out.

### Just the colours

```bash
curl -X POST "https://api.auricartisan.com/v1/analyzer/inspect" \
  -H "x-api-key: $AURIC_API_KEY" -H "content-type: application/json" \
  -d '{ "url": "https://example.com/", "scope": ["palette"], "sections": ["palette"] }'
```

This returns `sections.palette.colors` (the declared colours, grouped by where they are used) and `sections.palette.colorAudit`, with the "declared, not sampled" caveat in `incomplete`.

### A PDF for a client, from a stored audit

```js
const audit  = await inspect(url, ["seo", "security", "responsive"]);
const report = Object.assign({}, ...Object.values(audit.sections));
const pdf = await fetch("https://api.auricartisan.com/v1/analyzer/render", {
  method: "POST",
  headers: { "x-api-key": key, "content-type": "application/json" },
  body: JSON.stringify({ report, format: "pdf" }),
});
await writeFile("audit.pdf", Buffer.from(await pdf.arrayBuffer()));
```

`/render` takes the whole report, so merge the sections back together before sending it.

## What is not here yet

- **A rendered scan.** Contrast, the accessibility engine and the deep DOM comparison need a real browser. Until the API is connected to one, those stages are refused here and available in the tool.
- **A crawl.** Auditing a whole site takes minutes, which needs a job you start and poll. Until then, fetch a sitemap yourself and call `/inspect` per page.

## Credits

The price is per call, not per stage. A scope of one stage and a scope of eight cost the same 12 credits. Narrowing the scope makes a run faster and the response smaller, not cheaper; if you want the whole picture, ask for it in one call.

## Related pages

- [Plans, credits and quotas](../plans-credits-and-quotas.md)
- The website's Analyzer tool: [Analyzer docs](../../../../website/tools/accessibility-and-vision/analyzer/README.md)
