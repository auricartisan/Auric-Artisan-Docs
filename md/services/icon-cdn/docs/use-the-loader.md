---
title: Icon CDN — Use the loader
description: Render Icon CDN icons with the icon-cdn.js placeholders and the AuricIcons JavaScript API, including icons added after the page loads.
product: Services › Icon CDN
updated: 2026-09-25
---

# Use the loader

`icon-cdn.js` is a small script with no dependencies. It fills `data-icon` placeholders with inline SVG, returns any icon's markup to your code, and searches the catalogue. It creates a global object, `AuricIcons` (also available as `AuricIconLoader`).

## Placeholders

```html
<script src="https://icons.auricartisan.com/icon-cdn.js"></script>

<i data-icon="lucide:house"></i>
<i data-icon="phosphor:heart" data-style="fill" data-size="32"
   data-color="#e11" data-stroke="1.5"></i>
```

| Attribute | What it does | Example |
|---|---|---|
| `data-icon` | The icon to show (required): `set:name`, `set-name` or `name` | `tabler:home` |
| `data-style` | One of the set's styles; otherwise the set's default | `fill`, `outline`, `24/solid` |
| `data-size` | Width and height. A number is treated as pixels; a value with a unit is used as written. | `24`, `1.5em` |
| `data-color` | The icon's colour; otherwise the text colour | `#e11`, `rebeccapurple` |
| `data-stroke` | Stroke width, for stroke-drawn icons | `1.5` |

When the page has finished loading (or at once, if it already has), the loader replaces the contents of every element with `data-icon` and marks it with a `data-icon-done` attribute. An element marked done is not processed again. If the icon cannot be found, the element is left as it was.

Any element works, not only `<i>`: `<span data-icon="…">` is fine.

## Icons added later

Placeholders added after the page loads, for example by your framework, are not filled automatically. Call `inject()` after adding them:

```js
await AuricIcons.inject();              // the whole document
await AuricIcons.inject(myContainer);   // only inside one element
```

It returns the number of placeholders it found.

## Get an icon's markup

```js
const svg = await AuricIcons.svg('tabler:home', { size: 24, color: 'red' });
element.innerHTML = svg;
```

| Option | Meaning |
|---|---|
| `style` | One of the set's styles |
| `size` | Width and height, as for `data-size` |
| `color` | The colour |
| `stroke` | The stroke width |

`svg()` returns a string: SVG markup for SVG sets, or a `<span>` in the Material webfont for Material icons. It returns an empty string when there is no such icon.

## Find icons

```js
const hits = await AuricIcons.search('arrow', { set: 'lucide', limit: 50 });
const rec  = await AuricIcons.get('feather:activity');
const sets = await AuricIcons.sets();
```

| Method | Returns |
|---|---|
| `search(query, { set, limit })` | Records whose name, id or search terms contain the query, optionally in one set and limited in number |
| `get(name)` or `resolve(name)` | The icon's record (its set, id, name and available styles), or `null` |
| `list()` | Every icon record |
| `sets()` | The metadata of the seven sets |

The first call to any of these downloads the catalogue index, which is large; reuse the results.

## How names are resolved

1. With a set prefix (`tabler:home` or `tabler-home`), the loader looks for that icon in that set.
2. If that set has no such icon, or there is no prefix, it takes the first set that has an icon with that name, in the order Lucide, Phosphor, Tabler, Remix, Heroicons, Feather, Material.
3. Finally it tries an exact id or name.

Because of step 2, a name that a set does not have can quietly come from another set. For example, Lucide's house icon is `house`, so `lucide:home` shows another set's `home` icon. Copy names from the Icon Library to be sure.

## Where it loads from

By default the loader loads its data from the address it was loaded from. To use a self-hosted copy, set one of these (the first found wins):

1. `data-base` on the script tag;
2. `window.AURIC_ICON_BASE` (or `window.AURIC_ICON_ASSET_BASE`), set before the script loads;
3. `<meta name="auric-icon-base" content="…">` in the page.

You can also set `AuricIcons.base` from JavaScript.

## Related pages

- [Style, size and colour](style-size-and-colour.md)
- [Reference](reference.md)
- [Privacy](../others/privacy.md)
