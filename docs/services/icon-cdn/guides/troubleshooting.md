---
title: Icon CDN — Troubleshooting
description: Why an Icon CDN icon might not appear, appear huge, show the wrong icon or ignore its colour, and what to do.
product: Services › Icon CDN
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why | What to do |
|---|---|---|
| Icons are huge, or fill their container | Served SVGs have no width or height | Set `data-size`, or add CSS such as `[data-icon] svg { width: 1em; height: 1em; }` |
| A placeholder stays empty | The name matches no icon | Copy the name from the Icon Library; check the spelling and the set |
| The wrong set's icon appears | The set you named has no icon by that name, so another set's is used | Use the set's own name, for example `lucide:house` rather than `lucide:home` |
| Icons added after page load stay empty | The loader fills placeholders once, when the page loads | Call `AuricIcons.inject()` after adding them |
| An icon does not update when I change `data-icon` | Filled placeholders are marked `data-icon-done` | Remove that attribute (and the contents), then call `inject()` again |
| The colour does not change | An `<img>` or linked SVG file cannot inherit text colour | Use the loader, inline SVG or a sprite; or pick the colour before copying |
| `data-stroke` has no effect | The set is drawn with fills | Choose a lighter or heavier style instead, for example Phosphor `light` or `bold` |
| A style is ignored | The icon does not have that style | Check the icon's **Style** buttons; the loader falls back to the default |
| A Material icon looks like a letter or box | The Material font has not loaded yet, or the name is wrong | Wait for the font; check the name in the Icon Library |
| The first icons are slow to appear | The loader downloads the catalogue index and the markup for each set and style on first use | Use fewer sets and styles, or export a sprite |
| `AuricIcons` is undefined | Your code ran before the script loaded | Put your code after the script tag, or wait for the page's `load` event |
| A strict Content-Security-Policy blocks it | Your policy does not allow the CDN | Allow `https://icons.auricartisan.com` for `script-src` and `connect-src` (and `font-src` for Material), or self-host |

## Related pages

- [Use the loader](use-the-loader.md)
- [Style, size and colour](style-size-and-colour.md)
- [FAQ](faq.md)
