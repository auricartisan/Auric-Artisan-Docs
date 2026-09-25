---
title: Font CDN — Use the loader
description: Load Font CDN families with the font-cdn.js script tag or its AuricFonts JavaScript API, and configure where it loads from.
product: Services › Font CDN
updated: 2026-09-25
---

# Use the loader

`font-cdn.js` is a small script with no dependencies. It adds family stylesheets to your page, waits until fonts are ready, registers single font faces, and lets you search the catalogue. It creates a global object, `AuricFonts` (also available as `AuricFontLoader`).

## Declarative: one script tag

```html
<script src="https://fonts.auricartisan.com/font-cdn.js"
        data-families="Alegreya|Roboto Slab|Open Sans:wght@400;700"></script>
```

| Attribute | What it does |
|---|---|
| `data-families` | The families to load, separated by a vertical bar; each can carry a weight list (see [Family specs](#family-specs)) |
| `data-fonts` | Another name for `data-families` |
| `data-display` | The `font-display` value for faces added with `AuricFonts.face()`. Default `swap`. |
| `data-base` | Load stylesheets and data from another address; see [Where it loads from](#where-it-loads-from) |

For each family, the loader adds a `<link rel="stylesheet">` for its CDN stylesheet to the page's `<head>`, once.

## Programmatic: AuricFonts

Include the script without `data-families`, then call the API:

```html
<script src="https://fonts.auricartisan.com/font-cdn.js"></script>
<script>
  AuricFonts.load('Alegreya').then(() => {
    document.body.style.fontFamily = "'Alegreya', serif";
  });
</script>
```

### Load families

```js
await AuricFonts.load('Alegreya');                 // one family
await AuricFonts.load(['Inter:400,700', 'Lora']);  // several at once
```

`load()` adds the family's stylesheet and resolves, with `{ id, family }` (an array of them for several), once the browser reports the requested weights are ready. Use it to avoid a flash of the fallback font before you measure or draw text.

### Register one face from any file

```js
AuricFonts.face({ family: 'Demo', url: 'https://example.com/Foo.ttf', weight: 400 });
```

| Option | Default | Meaning |
|---|---|---|
| `family` | — | The family name to register |
| `url` | — | The font file's URL |
| `local` | — | A locally installed font name to try first |
| `weight` | `400` | The weight |
| `style` | `normal` | `normal` or `italic` |
| `display` | `swap` (or `data-display`) | The `font-display` value |
| `stretch` | — | The `font-stretch` value |

It resolves with the family name, and does not reject if the file fails to load.

### Other methods

| Method | Returns | Use |
|---|---|---|
| `AuricFonts.cssUrl(spec)` or `AuricFonts.css(spec)` | The stylesheet URL for a family | Build your own link or `@import` |
| `AuricFonts.injectCss(cssText, id)` | The added `<style>` element | Add raw `@font-face` or `@import` CSS |
| `AuricFonts.whenReady(family, weights)` | A promise | Wait for a family you added another way |
| `AuricFonts.list()` | A promise of every family record | Build your own picker |
| `AuricFonts.search(query)` | A promise of matching family records | Match on name, designer or category |
| `AuricFonts.get(idOrName)` | A promise of the family's full metadata, or `null` | Read styles, axes, licence and more |
| `AuricFonts.slugify(name)` | The family id | Turn a name into its id |
| `AuricFonts.base` | The address it loads from | Read or change it |
| `AuricFonts.index` | The catalogue, once loaded | Inspect what `list()` fetched |

```js
const mono = await AuricFonts.search('mono');
const meta = await AuricFonts.get('alegreya');
```

`list()`, `search()` and `get()` download catalogue data from the CDN the first time you call them: the index is large, so call them only when you need them.

## Family specs

Anywhere the loader takes a family, you can write:

| Spec | Meaning |
|---|---|
| `Alegreya` | The whole family |
| `Open Sans:wght@400;700` | The family, waiting for weights 400 and 700 |
| `Roboto:400,700i` | Weights 400 and 700; the `i` marks italics |
| `{ family: 'Inter', weights: [400, 700] }` | The same as an object; `id` can be given instead of `family` |

The weights tell the loader what to wait for. The stylesheet it adds always declares the whole family.

## Where it loads from

By default the loader loads stylesheets and data from the address it was itself loaded from. To point it elsewhere, for example at a self-hosted copy, set one of these (the first found wins):

1. `data-base` on the script tag;
2. `window.AURIC_FONT_BASE` (or `window.AURIC_FONT_ASSET_BASE`), set before the script loads;
3. `<meta name="auric-font-base" content="…">` in the page.

You can also set `AuricFonts.base` from JavaScript before calling `load()`.

## Related pages

- [Embed a family](embed-a-family.md)
- [Reference](reference.md)
- [Privacy](../others/privacy.md)
