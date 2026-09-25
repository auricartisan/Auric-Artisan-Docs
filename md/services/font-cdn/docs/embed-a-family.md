---
title: Font CDN — Embed a family
description: Every way to embed a Font CDN family — link tag, CSS @import, @font-face rules and usage CSS — plus weights, italics, variable axes and several families at once.
product: Services › Font CDN
updated: 2026-09-25
---

# Embed a family

The Font Library's **Use & Embed** tab gives each family six ready snippets: **Link**, **Import**, **Script**, **JS**, **@font-face** and **Usage**. Choose one, then **Copy**. The tab also shows the family's weights as chips under **Selected weights**, and a note naming the licence. This page explains each snippet.

## Link (recommended)

Add the stylesheet to your page's `<head>`:

```html
<!-- Self-hosted stylesheet (Google-Fonts style) -->
<link rel="stylesheet" href="https://fonts.auricartisan.com/css/alegreya.css">
```

Put it before your own stylesheets so your CSS can use the family straight away.

## Import

From inside a CSS file:

```css
/* In your CSS file */
@import url('https://fonts.auricartisan.com/css/alegreya.css');
```

An `@import` must come before other rules in the file. A link tag is usually faster, because the browser finds it sooner.

## Script and JS

The loader script adds the stylesheet for you:

```html
<!-- Auto-load with the CDN script -->
<script src="https://fonts.auricartisan.com/font-cdn.js"
        data-families="Alegreya"></script>
```

```js
// Programmatic load
AuricFonts.load('Alegreya').then(() => {
  document.body.style.fontFamily = "'Alegreya', serif";
});
```

See [Use the loader](use-the-loader.md).

## @font-face

The **@font-face** snippet gives the rules themselves, pointing at the font files on the CDN, for up to four of the family's styles. Use it when you want to control the rules, for example to rename the family or include only some styles:

```css
@font-face {
  font-family: 'Alegreya';
  font-style: normal;
  font-weight: 400 900;
  font-display: swap;
  src: url('https://fonts.auricartisan.com/font/A-F/ALEGREYA/Alegreya%5Bwght%5D.ttf') format('truetype-variations');
}
```

Variable styles are written with a weight range, and with a `font-stretch` range when the font has a width axis.

## Usage

The **Usage** snippet applies the family with a fallback for its category:

```css
/* Apply the family */
.headline {
  font-family: 'Alegreya', serif;
  font-weight: 400 900; /* variable range */
}
```

For a static family the snippet uses `font-weight: 400;`. The fallbacks used by category are:

| Category | Fallback in the Usage snippet |
|---|---|
| Sans-serif | `sans-serif` |
| Serif | `serif` |
| Monospace | `monospace` |
| Display | `system-ui` |
| Handwriting | `cursive` |

The Font Library's **Develop** tab offers a fuller font stack with safe fallbacks; see [Reference](reference.md).

## Weights and italics

- A family's stylesheet declares **every** style the CDN has for it. You do not choose weights in the URL.
- Set the weight you want in your CSS with `font-weight`. If the family lacks that weight, the browser uses the nearest one it has, or synthesises bold.
- Use `font-style: italic` for italics, if the family has them. The **Styles** tab of the Font Library lists each weight and style.

## Variable fonts

A variable font holds a continuous range of a design axis in one file. On the CDN, 550 families are variable. Their stylesheets declare the range, such as `font-weight: 400 900`, so any weight in between works:

```css
h1 { font-family: 'Alegreya', serif; font-weight: 650; }
```

Other axes, such as width (`wdth`), slant (`slnt`) or optical size (`opsz`), can be set with standard CSS such as `font-stretch` or `font-variation-settings`, where the family has them. The Font Library's **Specimen** tab has sliders for each axis a family provides.

## Several families at once

Link each stylesheet:

```html
<link rel="stylesheet" href="https://fonts.auricartisan.com/css/inter.css">
<link rel="stylesheet" href="https://fonts.auricartisan.com/css/lora.css">
```

Or use one script tag with the family names separated by `|`:

```html
<script src="https://fonts.auricartisan.com/font-cdn.js"
        data-families="Inter|Lora"></script>
```

In the Font Library, add families to your selection, then choose **Embed** in the **Your kit** tray to get **Combined embed code** for all of them: the link tags, the equivalent script tag, and a `:root` block of `--font-<id>` variables.

## Related pages

- [Use the loader](use-the-loader.md)
- [Self-host a family](self-host-a-family.md)
- [Licences](../others/licences.md)
