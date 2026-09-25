---
title: Library Kit — Settings, sync and reports
description: Every option on the Library Kit's Settings tab: preferences, reporting, sync destinations, report generation and storage.
product: Website › Kits › Library Kit
updated: 2026-09-25
---

# Settings, sync and reports

Open the **Settings** tab (or select **Settings** in the footer, or type `>` and choose **Library settings**). It has five sections, chosen from a row of tabs: **Preferences**, **Reporting**, **Sync & auto-update**, **Generate reports** and **Storage**. Changes save as soon as you make them.

## Preferences

| Setting | What it does | Values | Default |
|---|---|---|---|
| **Autosave drafts as you work** | Lets tools keep drafts of unsaved work in the library | On or off | On |
| **Show archived items in default views** | Includes archived items in library views outside the Archive tab. In the Library Kit itself, archived items stay on the Archive tab | On or off | Off |
| **Auto-update: keep all integrations in sync as items change** | Allows sync destinations to be updated when items change | On or off | On |
| **Autosave interval** | How often drafts are saved | 4, 8, 15 or 30 seconds | 8 seconds |
| **Keep drafts for** | How long unsaved drafts are kept before they expire | 3, 7, 14, 30 or 90 days | 14 days |

## Reporting

"Controls how much each tool reports back into the library when it saves an asset."

| Setting | What it does | Default |
|---|---|---|
| **Capture full output payload from every tool** | Saves the tool's complete output with each item | On |
| **Capture the tool's settings/state alongside the asset** | Saves the tool's settings, so restoring brings them back and **Saved option values** can list them | On |
| **Capture export configuration (formats, channels, intent)** | Saves the export choices you made in the tool | On |

**Report defaults**

| Setting | Values | Default |
|---|---|---|
| **Default report kind** | full, summary, assets, tool, activity | full |
| **Default report format** | JSON, NDJSON, CSV, XML, HTML, MD, TXT | JSON |
| **Include full asset payloads in reports** | On or off | On |
| **Include unsaved drafts** | On or off | Off |

Turning capture options off makes new saves smaller; items already saved are not changed.

## Sync & auto-update

"Send everything in your library to one or more external systems. Supports any HTTP endpoint that accepts JSON/NDJSON/CSV/reports."

Sync sends your library from your browser directly to web addresses you choose. Auric Artisan's servers are not involved. Sync is off until you turn it on.

### Sync options

| Setting | What it does | Default |
|---|---|---|
| **Sync enabled** | Master switch for sync | Off |
| **Auto-push on every change** | Pushes shortly after items change, and on the poll interval | On |
| **Include full payloads** | Sends each item's full data, not only its summary | On |
| **Include drafts** | Sends unsaved drafts too | Off |
| **Redact previews** | Removes preview images and swatches from what is sent | Off |
| **Auto-poll interval** | How often automatic pushes run | 30 s, 1 min, 5 min, 15 min, 60 min (default 1 min) |

Buttons:

- **Push all destinations now** — sends to every active destination and reports "N/M destinations succeeded."
- **Add destination** — adds a new destination named **Destination 1**, **Destination 2** and so on.
- **Clear history** — empties the activity list.

### Set up a destination

1. Turn on **Sync enabled**.
2. Select **Add destination**.
3. Fill in the destination card:

| Field | What it means | Values |
|---|---|---|
| Name | A label for you | Text |
| **Active** | Whether this destination is used | On or off |
| **On change** | Push to it when items change | On or off |
| **On interval** | Push to it on the poll interval | On or off |
| **Transport** | How to send | **webhook** or **http** (send to the URL), **console** (write to your browser's developer console, for testing), **local** (keep a temporary log in the page, for testing) |
| **Method** | The HTTP method | **POST**, **PUT**, **PATCH** |
| **URL** | Where to send, such as `https://example.com/webhook` | A web address |
| **Body format** | What to send | **JSON**, **NDJSON**, **CSV**, **REPORT** |
| **Report kind**, **Report format** | Used when the body format is REPORT | As for reports |
| **Auth bearer token** | Sent as an `Authorization: Bearer` header, if filled in | Optional |

4. Select **Test now** to send once. The card's status line shows the result (for example **idle**, or the last success time and any error). A failed test also opens **Push failed** with the reason.
5. Select **Remove** to delete a destination (confirm **Remove**).

Requests are sent from your browser, so the receiving server must accept requests from https://auricartisan.com (cross-origin requests). Your cookies are not sent. Each request carries the header `X-Auric-Library-Version: 1`.

**Recent sync activity** lists up to 20 recent pushes with time, destination, reason, and bytes and HTTP status, or the error.

You can also push from the command palette (**Sync now**) or the panel's right-click menu. If sync is off you see "Sync is switched off — turn it on in Library settings."; with no destinations, "No sync destinations configured yet."

## Generate reports

"Download a detailed report of everything in your library in the format of your choice."

1. Choose a **Kind**:

   | Kind | Contents |
   |---|---|
   | **full** | Library statistics, every item's details and data, collections and settings |
   | **summary** | Statistics only |
   | **assets** | Every item's details |
   | **tool** | The items saved from one tool, with their data. A **Tool** list appears so you can pick the tool; each shows its item count |
   | **activity** | Items added and updated per day |

2. Choose a **Format**: **JSON**, **NDJSON**, **CSV**, **XML**, **HTML**, **MD** or **TXT**.
3. Select **Download report**.

The quick buttons **JSON**, **NDJSON**, **CSV**, **XML**, **HTML**, **MD** and **TXT** download the default report kind in that format at once. Report files are named `auric-library-` followed by the kind and the date and time.

## Storage

- The line "Using" shows how much space the library takes and across how many entries.
- **Export library** downloads the full backup (`auric-library-backup.json`).
- **Import library** loads a backup, asking whether to **Merge** or **Replace**; see [Share, export and import](share-export-and-import.md).
- **Purge expired drafts** removes drafts older than **Keep drafts for** and confirms **Drafts purged**.
- **Reset library** deletes every saved item and collection after the warning "This deletes every saved item and collection. This cannot be undone." Select **Reset everything** to confirm.

**Maintenance**

**Repair empty Ishihara plates** rebuilds missing images for Ishihara plates that were saved with their generation settings but without an image. It asks to confirm how many plates it will re-render, shows progress, and reports how many it repaired. Plates saved without settings cannot be repaired this way.

The last line lists the available sync transports: `webhook`, `http`, `console`, `local`.

## Related

- [Privacy](../others/privacy.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Troubleshooting](troubleshooting.md)
