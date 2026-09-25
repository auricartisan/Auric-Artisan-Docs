---
title: Library Kit — Privacy
description: Where the Library Kit keeps your saved work, and the only ways it can leave your device.
product: Website › Kits › Library Kit
updated: 2026-09-25
---

# Library Kit privacy

## Where your library is kept

Every saved item, collection, draft and library setting is stored in your browser's storage for auricartisan.com, on this device. It is not uploaded to Auric Artisan and not linked to your account. Anyone who uses the same browser profile can see it.

The Library Kit's own view preferences (tab, grouping, density, collapsed groups, panel position, size, theme and **Keep open**) are stored the same way.

## The only ways your items leave the device

| Action | What leaves, and where it goes |
|---|---|
| **Share a link…** | A copy of the item, packed into the link. It goes wherever you send the link. Anyone with the link can open the copy |
| **Export**, **Export JSON**, downloads, reports | Files saved to your device by your browser |
| Sync | Your library (with or without full data, drafts and previews, as you choose) sent from your browser to the URLs you configure, with your bearer token if you set one |

Nothing is sent to Auric Artisan's servers by the Library Kit.

## Sensitive settings

Sync destinations, including any **Auth bearer token**, are stored in your browser as part of the library settings. They are included in a full library backup (`auric-library-backup.json`) and in **full** reports. Treat those files as private if you use tokens, or remove destinations before exporting.

## Removing your data

- Delete items individually, empty the archive, or use **Settings** > **Storage** > **Reset library** to delete everything.
- Clearing this site's data in your browser also deletes the library.
- Deleted data cannot be recovered unless you exported it.

## Related

- [Privacy for all kits](../../others/privacy.md)
- The site's privacy policy: https://auricartisan.com/legal/privacy/
