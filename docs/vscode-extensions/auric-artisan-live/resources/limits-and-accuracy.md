---
title: Auric Artisan Live — limits and safeguards
description: The built-in limits of Auric Artisan Live, why they exist, which ones you can change, and how to read its measurements.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Limits and safeguards

Auric Live keeps memory bounded and protects your data by design. Most limits can be changed; the safeguards around privacy and workspace trust are deliberate.

## Built-in limits

| Limit | Default | Change it with |
| --- | --- | --- |
| Requests kept by the inspector | 500 | `auricLive.inspector.maxEntries` (20–10000) |
| Requests shown in the control panel | Newest 200 | — |
| Body captured per request or response | 256 KiB | `auricLive.inspector.maxBodyBytes` (0–8388608) |
| Incoming request body | 8 MiB; larger bodies get 413; `0` rejects all non-empty bodies | `auricLive.maxRequestBodyBytes` |
| Time to receive a request body | 30 seconds; stalled bodies get 408; `0` disables it | `auricLive.requestBodyTimeoutMs` |
| Console capture | Off; when on, 200 entries, 2,000 characters per message, 20 messages per second | `auricLive.console.*` |
| Session records | On; 200 request summaries, 12 sessions, about 5 MiB per session | `auricLive.records.*` |
| Reloads before storm protection | 3 in 10 seconds | `auricLive.liveReload.stormLimit`, `auricLive.liveReload.stormWindowMs` |
| Dev server restarts | 5 | `auricLive.devServer.maxRestarts` (0–50) |
| Wait for a starting backend | 25 seconds | `auricLive.upstream.waitTimeoutMs` |
| Proxy request timeout | 30 seconds per rule | `timeoutMs` in a proxy rule |
| CGI script run time | 30 seconds | `cgi.timeoutMs` in the project file |

## Deliberate boundaries

- **Development only.** Auric Live is not public or production hosting.
- **Virtual workspaces are not supported.** It needs files on disk and a local port.
- **Runtimes are not installed for you.** Executables and framework packages must already be installed. Diagnostics report what is missing without installing or running anything.
- **Detection suggests, it does not certify.** A detected run target is based on files in the folder. It does not guarantee every framework configuration will work.
- **Workspace trust.** Untrusted project files cannot turn on running commands, proxying, CGI, file-backed mocks, custom certificates or listening on your network.
- **Symbolic links.** Links or junctions that lead outside the served folder are not followed.
- **Certificates.** Generating or importing a certificate never installs trust on a device.
- **Platform coverage.** Automated tests do not certify every operating system, framework or VS Code installation.

## Network simulation accuracy

- Latency and bandwidth are applied per transfer, not as a shared budget across all connections.
- There is no packet loss and no packet-level emulation.
- WebSocket messages are not bandwidth-shaped.
- Treat results as an approximation of a slow connection, not a measurement of a real network.

## Reading the measurements

- **p95 latency** in the control panel is calculated from the recent requests shown (up to 200), not from the whole session. Inspector totals count everything captured since the inspector was cleared.
- **Dashboard metrics** come from browser APIs. A browser that does not provide one shows **Unavailable**, not an estimate.
- **Cache results** in the dashboard are labelled either as the browser's estimate (**Likely cached**) or as confirmed by the server (304 or cached responses).
- **Storage figures** are sizes and counts reported by the browser; stored values are never read.
- **Frame rate and timings** are sampled while the dashboard is open and the tab is visible, so they describe that moment, not the page's lifetime.

## Redaction

Credential headers are always masked. Common sensitive query parameters and JSON or form fields are redacted by default, and you can add your own field names. Redaction is not a general personal-data detector: names, addresses and free text in bodies may still be sensitive. Review exports before sharing them.
