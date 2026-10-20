---
title: Auric Artisan Live — simulate a slow network
description: Slow down every client of the Auric Live server, including a phone, to test how your site behaves on slow connections.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Simulate a slow network

*Network shaping* makes the server answer as if the connection were slower: it adds latency (a delay before each response) and limits bandwidth (how fast bytes flow). Because it happens in the server, it applies to every client, including a phone on your network where browser developer tools are not available.

## Choose a profile

1. Run **Auric Live: Simulate Network Profile…**, choose **Simulate a network profile** in the Auric Live menu, or use **Network shaping** in the control panel's **Overview**.
2. Pick a profile. The current one is ticked.

| Profile | Latency | Download | Upload |
| --- | --- | --- | --- |
| `off` | none | unlimited | unlimited |
| `slow-3g` | 400 ms | 400 kbps | 400 kbps |
| `3g` | 150 ms | 1600 kbps | 750 kbps |
| `4g` | 40 ms | 9000 kbps | 3000 kbps |
| `cable` | 8 ms | 30000 kbps | 10000 kbps |
| `custom` | your value | your value | your value |

Rates are in kilobits per second. The choice lasts for the session. To keep it, set `auricLive.throttle.profile` in settings or `throttle.profile` in `auric.live.json`.

## A custom profile

Set the profile to `custom` and choose the numbers:

| Setting | Default | Range | Meaning |
| --- | --- | --- | --- |
| `auricLive.throttle.latencyMs` | 0 | 0–60000 | Delay added before each response |
| `auricLive.throttle.downloadKbps` | 0 | 0 or more | Download ceiling; `0` means unlimited |
| `auricLive.throttle.uploadKbps` | 0 | 0–1000000 | Upload ceiling; `0` means unlimited |

In the project file:

```json
{
  "throttle": {
    "profile": "custom",
    "latencyMs": 150,
    "downloadKbps": 1600,
    "uploadKbps": 750
  }
}
```

## What is shaped

- Static files, proxied responses, injected HTML, mock endpoints and REST responses are slowed down.
- Uploads (request bodies) are paced as well as downloads.
- Auric Live's own dashboard and status requests stay responsive.

## What it is not

- It shapes each transfer separately. It is not a shared bandwidth budget across all connections.
- It does not drop packets and is not a packet-level network emulator.
- WebSocket messages are not bandwidth-shaped.
- The time a request spends in simulated latency does not count towards the request-body timeout (`auricLive.requestBodyTimeoutMs`).

When a profile is active, pages load visibly slower, the status bar tooltip lists the throttle, and the dashboard's **Server** tab shows the profile.
