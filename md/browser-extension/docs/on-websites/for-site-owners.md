---
title: Browser extension — For site owners
description: How a website can keep its form controls native and keep the browser's right-click menu for visitors who use the Auric Artisan extension.
product: Browser extension › On websites
updated: 2026-09-25
---

# For site owners

Visitors who use Auric Artisan can turn on its website pickers and its right-click menu. Both are designed to leave designed sites alone, but you can also opt out explicitly with a few attributes. None of these affect visitors who do not have the extension.

## Keep form controls native

| Where | What to add | Works |
|---|---|---|
| On the control itself | `data-aa-picker-skip` | Always |
| On an ancestor of the control | `data-aa-picker-skip` | While the visitor keeps **Leave designed controls alone** on (the default) |
| On the control or an ancestor | `data-native-control`, `data-aa-native` or `data-no-enhance` | While **Leave designed controls alone** is on |
| On a colour input | `data-cp-skip` | Always. Colour inputs follow their own rule; the attributes above do not apply to them. |

Example:

```html
<select data-aa-picker-skip>
  <option>Keep the browser's list</option>
</select>
<input type="color" data-cp-skip>
```

Controls you have restyled (for example with `appearance: none`) or hidden behind your own widget are already left alone while **Leave designed controls alone** is on. Hidden, disabled and read-only colour inputs are never replaced.

## Keep the browser's right-click menu

For the whole page, add either attribute to the `<html>` element:

```html
<html data-aa-no-ext-menu>
```

```html
<html data-native-context-menu>
```

or add a meta tag:

```html
<meta name="auric-extension-menu" content="off">
```

For one area, mark the element or an ancestor:

```html
<div data-aa-own-menu>…</div>
```

A page that shows its own right-click menu by cancelling the browser's (calling `preventDefault()` on the `contextmenu` event) is left alone automatically, while the visitor keeps **Step aside for a site's own menu** on (the default).

## What the extension never does on your site

- It does not read or write your site's cookies, local storage or other storage.
- It does not send anything from your pages anywhere.
- Its pickers write values into your real controls through the normal `input` and `change` events, and the native controls stay in the page for form submission.

## Related pages

- [Website pickers](website-pickers.md)
- [Right-click menu](right-click-menu.md)
- [Privacy](../../others/privacy.md)
