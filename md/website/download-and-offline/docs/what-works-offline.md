---
title: Download and offline — What works offline
description: What keeps working without a connection, what needs one, and what the offline page shows.
product: Website › Download and offline
updated: 2026-09-25
---

# What works offline

## Works offline, once stored

After you prepare the offline version, these work without a connection, as far as your profile includes them:

- the pages and colour tools stored on the device;
- the colour libraries and their data (Balanced and Full);
- your library of saved palettes, gradients and exports, which lives on your device;
- site features such as the Settings panel, theme, the right-click menu, split view between stored pages, the recorder, eye rest and the screen saver;
- searching the site with Spotlight (the search index is part of the Balanced and Full profiles);
- Hindi, if it was included (see [Prepare the offline version](prepare-offline.md#hindi-offline)).

When you go offline, a message reads **Offline mode** and stays until the connection returns; then **Back online** appears.

## Needs a connection

Anything that has to reach a server:

- signing in, your account, billing and anything synced to your account;
- the Analyzer's audits of live websites;
- the **Web** tab in Spotlight and web results on the search page;
- sending feedback (it is kept and sent when you are back online);
- installing or updating the app;
- pages and files you have not stored.

## How pages are served

- **Pages** are fetched fresh from the network when you are online, and stored as you visit them. Offline, the stored copy is used.
- **Styles, scripts, images and library data** are served from storage when available and refreshed in the background.

So a page you have visited recently is usually available offline even without preparing the offline version, but only preparing it guarantees a complete set.

## The offline page

If you open a page that is not stored while offline, the site shows **You are offline** instead of an error:

- a **No connection** badge (it changes to **Back online** when the connection returns);
- "That page wasn't saved before the connection dropped.";
- **You wanted** with the address you asked for;
- **Try again**, which reloads the page;
- **Saved on this device**, with a count such as "38 pages" and a list of every page stored on this device that opens right now, shortest addresses first.

If nothing is stored yet, it reads "Nothing saved on this device yet".
