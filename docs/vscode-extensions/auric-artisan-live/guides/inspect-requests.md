---
title: Auric Artisan Live — inspect requests
description: See every request the Auric Live server handles, find slow or failing ones, and copy, replay or export them.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Inspect requests

The *request inspector* records each request the Auric Live server handles: method, path, status, which handler answered, time taken, size, and (by default) headers and bodies. Credentials are masked before anything is stored.

You can inspect requests in three places:

- the **Requests** view in the Auric Live sidebar;
- the **02 / Requests** section of the control panel (**Auric Live: Open Control Panel** or **Auric Live: Open Request Inspector**);
- the **Requests** tab of the in-page browser dashboard.

## The Requests view

Each row reads `METHOD /path` with `status · handler · time` beside it, for example `GET /api/users` — `200 · proxy · 34ms`. Select a row to open **Show Request Detail**. Right-click a row for:

- **Replay Request**
- **Copy Request as curl**
- **Copy Request as fetch**

The title bar has **Clear Request Log** and **Export Requests as HAR**.

## The control panel's Requests section

The section searches the latest 200 captured requests.

### Filter and sort

| Control | Options |
| --- | --- |
| Search | Type part of a path, method, status or handler. `Ctrl` + `F` (`Cmd` + `F` on macOS) focuses it |
| **Status** | **All statuses**, **2xx**, **3xx**, **4xx**, **5xx** |
| **Method** | **All methods**, `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS` |
| **Handler** | **All handlers**, `static`, `proxy`, `mock`, `rest`, `cgi`, `listing`, `redirect`, `error`, `client`, `live-reload` |
| **Sort** | **Newest first**, **Slowest first**, **Largest first** |

Filters combine. Results are paged with **Previous** and **Next**. **Reset filters** clears them. The filters and your place in the list are kept while new requests arrive, and they survive switching the panel's language.

### Pause the display

**Pause feed** freezes the list so you can read it; the server keeps capturing in the background. **Resume feed** catches up.

### Totals

The section shows **Captured requests**, **Failed responses**, **Response bytes recorded** and a **p95 latency**. The p95 is the time within which 95 per cent of the *recent* requests shown were answered. It is a sample of the latest requests, not a figure for the whole session.

### Request details

Open a path to see:

- the method, address, status, handler and timing;
- **Request headers**, **Request body**, **Response headers** and **Response body**, as far as they were captured;
- **Copy curl** and **Copy fetch**;
- **Replay request**.

`Escape` closes the details and returns focus to the list. Details load on demand, so a request that has since dropped out of the inspector shows **This request has expired or was cleared. Select a newer request.**

## Copy as curl or fetch

**Copy curl** gives a command you can paste into a terminal; **Copy fetch** gives a JavaScript `fetch()` call you can paste into a browser console or code. Values that were redacted or not captured are missing from the copy; fill them in yourself.

## Replay a request

**Replay request** sends the captured request to the server again.

- Methods other than `GET` and `HEAD` ask for confirmation first.
- A capture whose data was redacted, truncated, omitted or binary cannot be replayed safely. Auric Live refuses with **This capture was redacted, truncated, or contains a binary body. Copy as fetch or curl and supply the missing values before sending it.**

## Export HAR

A *HAR file* (HTTP Archive) is a standard JSON format for a list of requests and responses that browsers and many tools can open.

1. Run **Auric Live: Export Requests as HAR**, or select **Export HAR**.
2. Choose where to save the file.
3. Auric Live reports **Exported *N* requests.** and offers **Open**.

HAR exports leave out request and response bodies unless you turn on `auricLive.inspector.harIncludeBodies`, because bodies often hold personal or application data. Review a HAR file before sharing it.

## Privacy and limits

| Safeguard | Default | Setting |
| --- | --- | --- |
| Requests kept | 500; the panel shows the newest 200 | `auricLive.inspector.maxEntries` |
| Bodies captured | On, up to 256 KiB per body | `auricLive.inspector.captureBodies`, `auricLive.inspector.maxBodyBytes` |
| Credential headers | Always masked (`Authorization`, `Cookie`, `Set-Cookie` and similar) | — |
| Sensitive query and body fields | Redacted | `auricLive.inspector.redactSensitive` |
| Extra field names to redact | None | `auricLive.inspector.sensitiveFields` (case insensitive) |
| Bodies in HAR | Off | `auricLive.inspector.harIncludeBodies` |
| Recording | On | `auricLive.inspector.enabled` |

Incomplete JSON is left out rather than risk exposing part of a credential. Redaction is not a general personal-data detector: names, addresses and free text can still be sensitive.

Traffic is kept separate per workspace folder. With several servers running, **Auric Live: Select Active Server** chooses which one the inspector shows.

**Auric Live: Clear Request Log** (or **Clear history** in the panel) empties the inspector.

## Output channel logging

Separately from the inspector, `auricLive.requestLogging` writes one line per request to the **Auric Artisan Live** output channel (at debug level for successes, higher for failures). `auricLive.logLevel` sets how much reaches the channel: `off`, `error`, `warn`, `info` (default) or `debug`. Credential-like values are masked and paths are written relative to the served root.

When you load a page with the inspector open, its requests appear within a moment, each labelled with the handler that answered it.
