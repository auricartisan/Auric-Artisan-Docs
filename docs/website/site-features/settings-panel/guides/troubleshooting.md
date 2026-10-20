---
title: Settings panel — Troubleshooting
description: Fixes for common problems with the Settings panel and the settings it controls.
product: Website › Site features › Settings panel
updated: 2026-09-25
---

# Troubleshooting the Settings panel

## My settings are gone

**Why:** settings are kept in this browser's local storage. They are lost when you clear site data or cookies for auricartisan.com, when you use a private or incognito window (which forgets everything when it closes), or when you open the site in a different browser or on another device.

**What to do:** set them again, or import a settings file you exported earlier (**Import** in the panel footer). Export a file now so you have a copy next time.

## `Ctrl` + `,` does nothing

**Why:** the panel loads a moment after the page. A shortcut pressed while the page is still loading can be missed. Some browser extensions also claim `Ctrl` + `,`.

**What to do:** wait until the page has finished loading and try again, or open the panel from the page utilities bar at the bottom-left (**Settings**).

## The Alt shortcuts do nothing

**Why:** `Alt` + `R`, `Alt` + `T`, `Alt` + `M`, `Alt` + `+`, `Alt` + `-` and `Alt` + `0` are ignored while your cursor is in a text field, so they cannot interfere with typing. They are also ignored when `Ctrl` or `Cmd` is held.

**What to do:** click an empty part of the page first, then press the shortcut.

## A change in one tab did not reach another tab

**Why:** other open tabs pick up a change when the browser tells them about it. This works in normal windows but not between a normal window and a private window, which keep separate storage.

**What to do:** reload the other tab.

## My theme, accent or text size changed after I opened a link

**Why:** a page link copied from the site can carry the sender's appearance settings when they differ from the defaults (see [Shareable links](../../shareable-links/README.md)). Opening it applies those settings in your browser.

**What to do:** set them back in Appearance, or select **Restore section defaults**.

## The Ads controls are greyed out

**Why:** ad preferences are a paid perk. For signed-out and free-plan visitors the controls are disabled, and selecting one shows an upgrade message.

**What to do:** nothing is broken. Upgrading unlocks the controls; every tool stays free either way.

## I cannot find the Ads section

**Why:** the section appears only while the site is showing ads.

## The Eyedropper button is missing

**Why:** it appears only in browsers that offer a screen colour picker to web pages, which at present means desktop Chromium-based browsers such as Chrome and Edge.

**What to do:** use the **Custom color** chip instead, or pick a colour with a colour tool on the site and paste its hex into your browser's picker.

## The + button next to my custom colour is disabled

**Why:** either the colour is already in **Saved colors** (the button reads **Already saved**), or the palette already holds 18 colours.

**What to do:** remove a saved colour with the X on its swatch, then try again.

## The Settings panel does not stay open when I move to another page

**Why:** the panel closes when you leave a page, even with the **Focus mode** button on.

**What to do:** press `Ctrl` + `,` on the new page. Your settings themselves carry over.

## Import says "That file isn't valid settings"

**Why:** the file is not valid JSON, for example because it was edited by hand and a comma or bracket is missing, or because it is a different kind of file.

**What to do:** export a fresh file from a browser that has the settings you want, or fix the JSON. See [Reference](reference.md#the-settings-file) for the format.

## After Reset all my saved colours are still there

**Why:** this is intended. Saved colours are a palette you built, so neither **Reset all** nor **Restore section defaults** removes them.

**What to do:** remove them one by one with the X on each swatch.

## A bar I switched on shows on every page, not just the homepage

**Why:** the Welcome, Announcement and Quick links bars start in a "homepage only" state. Switching one off and on again shows it everywhere.

**What to do:** select **Restore section defaults** in Highlights to go back to homepage only.
