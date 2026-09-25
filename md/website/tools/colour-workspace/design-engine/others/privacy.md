---
title: Design System Generator — Privacy
description: What the Design System Generator keeps in your browser, what it saves, and which services it contacts.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Privacy

## Stays in your browser

- The whole system is generated in the page. Your inputs are not sent to a server to generate it.
- Copies go to your clipboard only when you select a copy control.
- Downloads are created in the browser.

## Remembered in your browser

Stored in your browser's local storage on this device:

- your last set of inputs, used to restore the system on your next visit;
- whether the side rails are expanded;
- whether you dismissed the API note.

## Uses the network

| What | Where | Why |
| --- | --- | --- |
| Fonts for the type previews | fonts.auricartisan.com (Auric font CDN) and fonts.googleapis.com (fallback) | To draw the specimens in the recommended families. The requests name the font families. |
| Icons for the previews | icons.auricartisan.com (Auric icon CDN) | To show the recommended icon family. |
| Saving | Your Auric Artisan Library | When you select **Save** or the save button. |
| Share links | Your clipboard and address bar | The link contains your inputs; anyone you send it to can see them. |

Opening another tool from **Connect** passes your seed colour and palette to that tool in the address, and keeps a copy for that tool in your browser's session storage.

For the CDNs as services, see the [Font CDN](../../../../../services/font-cdn/README.md) and [Icon CDN](../../../../../services/icon-cdn/README.md). Site-wide analytics and advertising follow your cookie choices; see the [Help centre](../../../../../help/README.md).

## Related

- [Limits and accuracy](limits-and-accuracy.md)
- [Share, save and connect](../docs/share-save-and-connect.md)
