---
title: Icon CDN — Style, size and colour
description: Choose an icon's style, give it a size, colour it and change its stroke width, with the loader, CSS or the Icon Library.
product: Services › Icon CDN
updated: 2026-09-25
---

# Style, size and colour

## Style

Many icons come in several styles: Phosphor's `thin`, `light`, `regular`, `bold`, `fill` and `duotone`; Tabler's `outline` and `filled`; Remix's `line` and `fill`; Heroicons' `24/outline`, `24/solid`, `20/solid` and `16/solid`; Material's `outlined`, `round`, `sharp`, `regular` and `twotone`. See [Collections](collections.md).

- With the loader, set `data-style="fill"` or pass `{ style: 'fill' }` to `svg()`.
- If you ask for a style the icon does not have, the loader uses the set's default style, or else the icon's first style.
- In the Icon Library, the **Style** buttons in an icon's panel switch between its styles, and the copied code follows.

## Size

Served icons have no width or height of their own, only a `viewBox`, so always size them.

With the loader:

```html
<i data-icon="lucide:house" data-size="24"></i>     <!-- 24 px -->
<i data-icon="lucide:house" data-size="1.25em"></i> <!-- scales with text -->
```

With CSS, for every icon at once:

```css
[data-icon] svg { width: 1em; height: 1em; vertical-align: -0.125em; }
```

Sizing in `em` makes icons follow the surrounding font size. Material icons are font glyphs and follow `data-size` or the font size.

Icons are drawn on a grid: 24 units for most sets, 256 for Phosphor, and 20 or 16 for some Heroicons styles.

In the Icon Library, the **Size** slider runs from 16 to 160 px and sets the size of the copied `<img>` code.

## Colour

Icons are drawn with `currentColor`: by default they take the text colour of the element they are in.

- To match your text, do nothing, or set `color` on the parent in CSS.
- To set a colour with the loader, use `data-color="#e11"` or `{ color: '#e11' }`.
- With CSS: `.danger [data-icon] { color: #b00020; }`.

A linked SVG file or a data-URI image cannot inherit the page's colour. Choose the colour in the Icon Library before you copy, or recolour the file yourself. In the Icon Library, **Colour** sets a colour and the **currentColor** button goes back to inheriting.

## Stroke width

Stroke-drawn icons (Lucide, Tabler, Feather, and Heroicons' outline style) can be made thinner or bolder:

- with the loader, `data-stroke="1.5"` or `{ stroke: 1.5 }`;
- with CSS, `[data-icon] svg { stroke-width: 1.5; }`.

In the Icon Library, the **Stroke** slider runs from 0.5 to 3 in steps of 0.25, or **auto** for the set's own width. Fill-drawn sets, such as Phosphor and Remix, ignore stroke width; choose a lighter or heavier style instead.

## Related pages

- [Collections](collections.md)
- [Use the loader](use-the-loader.md)
