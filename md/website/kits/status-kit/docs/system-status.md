---
title: Status Kit — System status
description: Every live reading in the Status Kit's System status panel, what it means and when it shows a dash.
product: Website › Kits › Status Kit
updated: 2026-09-25
---

# System status

The **System status** panel shows live information about your device, connection and the page, read from your browser. It refreshes every two seconds while the Status Kit is open, and at once when your connection goes on or off line.

## Open, collapse and switch pages

- The panel is expanded when the kit opens. Select its heading (**System status**) or the chevron to collapse or expand it. With the keyboard, focus the heading and press `Enter` or `Space`.
- The pill next to the heading shows **Online** or **Offline**.
- Select a tab to switch between **Network**, **Hardware**, **Memory**, **Display** and **Runtime**.

A reading shows **—** when your browser does not provide it. Some readings exist only in certain browsers, noted below.

## Network

| Reading | What it shows |
|---|---|
| **Connection** | Your connection's effective speed class, such as **4G** or **3G**, or **Online** or **Offline** if the browser does not report a class |
| **Speed** | Estimated download speed in Mbps, with a bar (full at 20 Mbps) and the connection type, such as wifi, when known |
| **Latency** | Estimated round-trip time in milliseconds |
| **Data Saver** | **On** if your browser's data-saving mode is on, otherwise **Off** |

Speed, latency and data saver come from the browser's network information, which Chromium-based browsers provide and others often do not. They are the browser's rough estimates, not a speed test.

## Hardware

| Reading | What it shows |
|---|---|
| **Battery** | Charge level with a bar, and **Charging** or **On battery**. The bar turns to a warning colour at 20% or below when not charging |
| **Device memory** | Approximate memory in GB, as the browser reports it (browsers round this and cap it) |
| **CPU threads** | Number of logical processor threads available to the browser |

Battery information is available only in some browsers.

## Memory

| Reading | What it shows |
|---|---|
| **JS heap** | Memory the page's scripts are using, and the limit, with a bar that turns to a warning colour above 85%. Chromium-based browsers only |
| **Storage** | Space the site uses in your browser's storage, out of the space allowed, with a percentage. The bar turns to a warning colour above 90% |
| **Caches** | Number of caches the site has stored, for example for offline use |

## Display

| Reading | What it shows |
|---|---|
| **Resolution** | Your screen's size in CSS pixels, such as 1920×1080 |
| **Viewport** | The browser window's inner size in CSS pixels |
| **Pixel ratio** | Device pixels per CSS pixel, such as **2×** on a high-density screen |
| **Color** | Colour depth in bits, such as **24-bit**, and the gamut: **P3 gamut** for a wide-gamut display, otherwise **sRGB gamut** |

## Runtime

| Reading | What it shows |
|---|---|
| **Frame rate** | Frames drawn in the last second, with a sparkline of the last 48 seconds |
| **Page load** | Seconds the page took to finish loading |
| **Service worker** | **Active** if the site's offline helper is controlling the page, **Registered** if your browser supports one but it is not controlling this page, **Unsupported** otherwise |
| **App mode** | **Installed app** if you opened the site as an installed app, otherwise **Browser tab** |
| **Language** | Your browser's preferred language, such as **en-GB** |
| **Time zone** | Your device's time zone, such as **Europe/London** |
| **Cookies** | **Enabled** or **Blocked** |

The frame rate is measured only while the Status Kit is open, and measuring stops when you close it. The figure usually matches your display's refresh rate, for example about 60 on a 60 Hz screen, and drops when the page is busy.

## Using the readings for a bug report

When you report a problem, the **Runtime** and **Display** tabs give most of what support needs: browser language, time zone, app mode, screen and window size, pixel ratio and gamut. Copy them by hand; the kit does not send them anywhere. See [Help](../../../../help/README.md) for how to contact support.

## Related

- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Privacy](../others/privacy.md)
