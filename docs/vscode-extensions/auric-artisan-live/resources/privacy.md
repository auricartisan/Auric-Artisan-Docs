---
title: Auric Artisan Live — privacy
description: What Auric Artisan Live keeps on your machine, what can reach the network, and how captured data is protected.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Privacy

## What stays on your machine

- **No telemetry.** Auric Live sends no usage data anywhere.
- **The server runs locally.** Your files are served from your computer.
- **Requests are recorded locally** in the inspector, in memory, and optionally as local session records under `.auric-live/`.
- **The phone QR code is generated locally.** No address goes to a QR service.
- **The translation into Hindi is bundled.** No translation service receives your data.
- **The dashboard makes no external requests** for fonts or branding.

## What can reach the network

- **Other devices on your network.** With the default host `0.0.0.0` in a trusted workspace, devices on your local network can open the served site, subject to your firewall. Set `auricLive.host` to `127.0.0.1` to prevent this, or require a login with `auricLive.auth.enabled`.
- **Proxy targets.** Requests for proxied paths go to the targets you configure.
- **Run targets.** Commands you run as run targets do whatever they are written to do.
- **Links you choose.** Links to auricartisan.com in the panel, preview and dashboard open in your browser.

## How captured data is protected

| Data | Protection |
| --- | --- |
| Credential headers (`Authorization`, `Cookie`, `Set-Cookie` and similar) | Always masked before storage |
| Sensitive query parameters and JSON or form fields | Redacted by default (`auricLive.inspector.redactSensitive`); add names with `auricLive.inspector.sensitiveFields` |
| Incomplete JSON bodies | Left out rather than partly exposed |
| Request and response bodies in HAR exports | Left out unless `auricLive.inspector.harIncludeBodies` is on |
| Session records | Never store query strings, headers, bodies, cookies, IP addresses, user agents or storage values |
| Browser console capture | Off by default; redacted and rate-limited when on; not saved to session records |
| Dashboard storage summary | Counts and sizes only; stored values are never read |
| Log output | Credential-like values masked; paths written relative to the served root |
| Environment variables in run commands | Values of sensitive-looking names are redacted in displays and diagnostics |
| Certificate passphrases | Kept for the session only |
| Basic-authentication password | Stored in plain settings; do not use a real password |

Redaction cannot recognise every kind of personal data. Review any HAR file, diagnostic report or session record before sharing it.
