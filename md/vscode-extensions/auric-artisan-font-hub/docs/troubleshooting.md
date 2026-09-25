---
title: Auric Artisan Font Hub — troubleshooting
description: Symptoms, causes and fixes for common Auric Artisan Font Hub problems.
product: VS Code extensions › Auric Artisan Font Hub
updated: 2026-09-25
---

# Troubleshooting

For anything not listed, run **Auric Font Hub: Show Logs** and see [Get support](../../install-and-setup/docs/get-support.md). Include your extension version, the file language and the error message with anything private removed.

## Fonts are not visible on your website

- **Why:** the stylesheet is not loaded, the font file is blocked (often by CORS or a Content Security Policy), or the class is not applied.
- **Fix:** run **Check Font CDN and Browser CORS**, then check the browser's Network tab for both the stylesheet and the font file. A successful stylesheet response alone is not enough. See [Check CDN and browser delivery](cdn-and-browser-delivery.md).

## An embed is present but the text has not changed

- **Why:** the setup only defines the `.auric-font-<id>` class.
- **Fix:** add the class to your markup, or use the family's `font-family` value in your own selector.

## Nothing changed after inserting

- **Why:** the setup was already in the file (**… is already configured in this document.**), or the file type needs manual placement and the embed was copied to the clipboard instead.
- **Fix:** read the notification, then paste the embed where it belongs if it was copied.

## "No HTML head found."

- **Why:** the HTML file has no `<head>` element, for example a partial or a component template.
- **Fix:** paste the copied embed into your page's head or your framework's layout.

## "The document changed. Preview the font insertion again before applying."

- **Why:** the file was edited after the preview opened, so the preview is out of date.
- **Fix:** run **Preview** again and apply the new preview.

## "Smart insertion supports documents up to 2 MiB."

- **Why:** the file is larger than automatic insertion handles.
- **Fix:** copy an embed and place it by hand.

## "This is a local system font."

- **Why:** system fonts are not on the CDN, so there is nothing to link to.
- **Fix:** copy its family name and rely on it being installed, or choose a library font.

## Previews are missing or say "Preview unavailable"

- **Why:** you are offline, `auricFontLib.network.enabled` is off, the font is not cached yet, or the file could not be fetched.
- **Fix:** connect, turn the network setting on, or wait and retry. Details, styles and licences still work from the bundled catalogue.

## The catalogue refresh was rejected

- **Why:** the network failed, or the refreshed data did not pass validation.
- **Fix:** nothing is lost: **Auric Font Hub kept cached data** and the bundled snapshot stays available. New families may need an extension update.

## "Self-hosting kit blocked."

- **Why:** a family's licence does not allow redistribution, permission could not be established, a required licence notice could not be loaded, or the family is a system font.
- **Fix:** remove the families named in the message and try again.

## "Choose at most *N* families for one kit." or the 250 MB limit

- **Why:** the kit is limited by `auricFontLib.download.maxFamilies` (6 by default, up to 12) and to 250 MB in total.
- **Fix:** split the selection into several kits, or raise the setting.

## "Select at least two font families to compare."

- **Fix:** select two to four families with the select button on each card, then **Compare**.

## Duplicate commands or views

- **Why:** the older Font Library extension is still enabled.
- **Fix:** disable or uninstall it. See [Moving from Font Library](moving-from-font-library.md).

## "Enable network access in Font Hub settings to run CDN checks."

- **Fix:** set `auricFontLib.network.enabled` to `true`.

## A preview became stale

- **Why:** you edited the source file after opening the diff.
- **Fix:** reopen **Preview** after editing.
