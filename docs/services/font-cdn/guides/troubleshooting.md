---
title: Font CDN — Troubleshooting
description: Why a Font CDN family might not appear or look right, and what to do.
product: Services › Font CDN
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why | What to do |
|---|---|---|
| The text stays in the fallback font | The stylesheet URL is wrong, so it returns a "not found" page | Open the stylesheet URL: it should start with a comment naming the family. Copy it from **Use & Embed**. |
| The text stays in the fallback font, and the URL is right | The CSS names the family differently | Use the exact name in the stylesheet's `font-family`, in quotes, for example `'Roboto Slab'` |
| The fallback shows briefly, then the font | Normal: stylesheets use `font-display: swap` | Preload or use `AuricFonts.load()` and wait for it before showing text that must not change |
| Bold looks smeared or too heavy | The family has no bold file, so the browser synthesises one | Pick a weight the family has; the **Styles** tab lists them |
| A weight has no effect on a static family | Only the weights the family has can be shown | Choose another weight or a variable family |
| Italic looks slanted rather than true italic | The family has no italic style | Check the **Styles** tab, or choose a family with italics |
| `data-families` loads nothing | A family name is misspelt, or the names are not separated by a vertical bar | Use the exact family names; check the browser's network panel for a failed `/css/` request |
| `AuricFonts` is undefined | Your code ran before the script loaded | Put your code after the script tag, or wait for the page's `load` event |
| `get()` returns `null` | No family has that id or name | Check the spelling, or use `search()` |
| `list()` or `search()` is slow the first time | The catalogue index is downloaded on first use | Call it once and reuse the result |
| **Download kit** reads **Installed only** | The family is a system font the library does not serve | Choose another family, or license the font from its maker |
| The kit has `DOWNLOAD_NOTES.txt` | One or more files could not be fetched | Try again later; the note lists what is missing |
| A licence shows as **Unspecified** | The library found no licence text for the family | Check with the foundry before using it; the **License** tab says "No bundled license text was found for this family" |
| Characters show as boxes or in another font | The family does not cover that script | Check the **Charset** tab and add a fallback font that covers it |
| A strict Content-Security-Policy blocks the font | Your policy does not allow the CDN | Allow the CDN in `style-src` and `font-src` (and `script-src` for the loader), or self-host |

## Related pages

- [Embed a family](embed-a-family.md)
- [Self-host a family](self-host-a-family.md)
- [FAQ](faq.md)
