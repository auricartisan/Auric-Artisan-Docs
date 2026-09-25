---
title: Shareable links — Troubleshooting
description: Fixes for common problems with page links and their saved state.
product: Website › Site features › Shareable links
updated: 2026-09-25
---

# Troubleshooting shareable links

## The link opened but my inputs were not restored

**Possible causes and fixes:**

- The field has no identity on the page, so it cannot be saved. Nothing can be done from your side.
- It was a password, file or search field, which are never saved.
- The state was too long (over about 3,600 characters), so only the scroll position and open panels were kept.
- The page uses its own `#` part, so no `#p=` was added. Use the tool's own sharing option if it has one.
- The page had not finished loading when the link was copied. Wait a moment after your last change before copying.

## Opening a link changed my theme, accent or text size

**Why:** the link carried the sender's appearance settings that differ from the defaults.

**What to do:** change them back in Settings, or use **Restore section defaults** in Appearance.

## A panel opened by itself when I loaded a page

**Why:** the address had a `#p=` part recorded while that panel was open.

**What to do:** close the panel. The address updates and it will not reopen.

## The address changes as I scroll

That is the page saving your position. It does not add steps to your Back button.

## I want a link without the extra part

Scroll to the top and undo your changes before copying, or delete everything from `#p=` onwards.

## `?color=` did not open the inspector

**Why:** the value is not a colour the site can read, or the `#` was not written as `%23`.

**What to do:** write the hex without `#` (`?color=d3af37`) or as `%23d3af37`.
