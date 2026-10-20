---
title: Download and offline — Prepare the offline version
description: Choose an offline profile and download the site into your browser so it works without a connection.
product: Website › Download and offline
updated: 2026-09-25
---

# Prepare the offline version

## What is stored automatically

On your first visit, your browser keeps a small core of the site, called the **app shell**: the main pages (such as the homepage, Download, the tools index, Basic Tools, the Colour Science Lab, the Personalization Generator, the colour libraries, Search and Security), the site's styles and scripts, and the offline page. That is enough for an offline visit to show something useful, but not the whole site.

Everything beyond the shell is downloaded only when you ask for it.

## Choose a profile

On the Download page, under **Profile — How much to keep**:

| Profile | Description on screen | What it keeps | Suits |
|---|---|---|---|
| **Auto** (default) | Device-aware cache choice | Chooses Lite, Balanced or Full from what the device reports | Almost everyone |
| **Lite** | Smallest offline footprint | The app shell and the core tools, and little else | Phones, tight storage, metered connections |
| **Balanced** | Core tools plus active libraries | Shell, core tools and the colour libraries and their data | A laptop you also use for other things |
| **Full** | Download the widest local cache | Every file the site lists for offline use | A desktop that will be offline for a while |

Selecting **Lite**, **Balanced** or **Auto** only sets the profile ("Updated offline hardware profile."). Selecting **Full** sets it **and starts downloading** at once: "Full profile selected. Downloading the full offline cache...".

### How Auto chooses

| Condition | Auto picks |
|---|---|
| **Limit background cache work on low-power hardware** is on, the browser reports Data Saver, or the connection is 2G | Lite |
| 4 or fewer processor threads, 4 GB or less memory, or less than about 650 MB of storage available to the site | Balanced |
| Otherwise | Full |

The **Offline profile** metric and the summary (**Selected**, **Effective profile**) show the result, for example "Auto selected Balanced for this device."

### Limit background work

The switch **Limit background cache work on low-power hardware** makes Auto choose **Lite**. Use it on older or battery-powered devices.

## Download

- **Prepare offline version** downloads the profile in effect (your choice, or Auto's).
- **Download full offline** downloads the **Full** profile regardless of your choice.

While downloading:

- the status line reads, for example, "Downloading the Balanced offline profile into this browser..." and then "Preparing offline version: A/B checked, C cached, D failed." (with real numbers);
- a message at the edge of the screen reads "Saving for offline — N%";
- you can keep using the site, and it is best to keep the tab open until it finishes.

When it finishes:

- the status reads, for example, "Balanced offline download finished: A/B assets ready." (with "N failed" if some files could not be fetched);
- a message reads "Full offline app ready";
- the readiness badge reads **Offline ready** and the cache audit runs.

If files failed, select **Repair cache** to try them again (see [Storage and cache](storage-and-cache.md)).

## Hindi offline

If the site is in Hindi when you prepare the offline version, the Hindi text is downloaded as well (about 11 MB). If you switch to Hindi later, prepare the offline version again to include it.

## Persistent storage

When you prepare the offline version, the site asks the browser to keep its storage **persistent**, so that the browser does not clear it when the device runs low on space. Some browsers grant this automatically, some ask you, and some decide from how often you use the site. The **Persistent storage** check shows the result: "Persistent storage is active for this browser." or "Storage is best-effort until the browser grants persistence."

## If the connection drops

If a download you started is interrupted, browsers that support background sync (such as Chrome and Edge) finish it when you are next online. Otherwise, select **Prepare offline version** again; files already stored are kept.

## Data use

The Full profile is the whole site and can be large (more than 100 MB). On a metered or slow connection, choose **Lite** or **Balanced**, or wait for Wi-Fi.

The site does not start a large download until you have asked for an offline copy at least once. After that, in browsers that support background sync, it refreshes your offline copy in the background when a new version of the site is released, so that you are not left with an old copy.
