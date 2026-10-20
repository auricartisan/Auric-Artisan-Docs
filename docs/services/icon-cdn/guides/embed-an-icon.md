---
title: Icon CDN — Embed an icon
description: Every way to put an Icon CDN icon on a page — loader placeholders, inline SVG, a React component, a data-URI image, direct SVG files and the Material and Remix webfonts.
product: Services › Icon CDN
updated: 2026-09-25
---

# Embed an icon

The Icon Library at https://auricartisan.com/tool/icon/ gives every icon ready-made code. Open an icon, set its style, size and colour, then choose a copy button or copy a block from the code panel. This page explains each option.

## CDN tag (the loader)

**Copy CDN tag** gives a placeholder and the loader script:

```html
<i data-icon="phosphor:heart" data-style="fill"></i>
<script src="https://icons.auricartisan.com/icon-cdn.js"></script>
```

`data-style` appears only when you chose a style other than the set's default. Include the script once per page, and use as many placeholders as you like. The loader replaces each placeholder's contents with inline SVG when the page loads; see [Use the loader](use-the-loader.md).

Best for: plain HTML pages, prototypes, content managed in a CMS.

## Inline SVG

**Copy SVG** gives the icon's SVG markup, with your chosen colour and stroke applied. Paste it straight into your HTML. Nothing needs to load from the CDN afterwards.

```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
```

Give it a size with `width` and `height` attributes or CSS.

Best for: a handful of icons you want in your own markup, with no script.

## JSX / React

**Copy JSX** gives a React component. Attribute names are converted to React's camelCase, and your props are spread onto the `<svg>`:

```jsx
export const Activity = (props) => (
  <svg {...props} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
);
```

Use it as `<Activity width={24} height={24} />`.

## Image with a data URI

**Copy data-URI** gives an `<img>` whose source is the SVG itself, encoded into the address, with your chosen size and the icon's name as its `alt` text:

```html
<img src="data:image/svg+xml,…" width="48" height="48" alt="Activity">
```

An image cannot inherit the page's text colour, so choose the colour before you copy. Change the `alt` text to describe what the icon means in your page, or use `alt=""` if the icon is decorative.

## Direct SVG files

Every SVG icon is also served as a file you can link:

```html
<img src="https://icons.auricartisan.com/icon/feather/activity.svg" width="24" height="24" alt="Activity">
```

Paths follow each set's own folders:

| Set | Example path |
|---|---|
| Feather | `/icon/feather/activity.svg` |
| Lucide | `/icon/lucide/house.svg` |
| Tabler | `/icon/tabler/outline/home.svg`, `/icon/tabler/filled/home.svg` |
| Phosphor | `/icon/phosphor/regular/heart.svg`, `/icon/phosphor/fill/heart-fill.svg` |
| Heroicons | `/icon/heroicons/24/outline/home.svg` |
| Remix | `/icon/remix/Buildings/home-line.svg` |

As with a data URI, a linked file does not take the page's text colour.

**Download .svg** in the Icon Library saves the icon, in your chosen colour and stroke, as `<id>-<style>.svg`.

## Webfonts

### Material

Material icons are glyphs in a webfont. The Icon Library's code panel for a Material icon offers **HTML (CDN)**, which uses the loader:

```html
<i data-icon="material:home" data-style="outlined"></i>
<script src="https://icons.auricartisan.com/icon-cdn.js"></script>
```

and **Webfont @font-face**, which declares the font from the CDN and shows the icon's character code, so you can use the font directly. **Copy glyph** copies the character entity.

### Remix

Remix Icon's own webfont stylesheet is served at `https://icons.auricartisan.com/icon/remix/fonts/remixicon.css`. It uses Remix's `ri-*` classes, as documented by the Remix Icon project.

## Accessibility

- An icon next to visible text is usually decorative: hide it from assistive technology, for example with `aria-hidden="true"` on the placeholder.
- An icon on its own, such as an icon-only button, needs an accessible name, for example `aria-label` on the button.

## Related pages

- [Use the loader](use-the-loader.md)
- [Style, size and colour](style-size-and-colour.md)
- [Export and self-host](export-and-self-host.md)
