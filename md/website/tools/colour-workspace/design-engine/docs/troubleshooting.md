---
title: Design System Generator — Troubleshooting
description: Symptoms you may meet in the Design System Generator, why they happen, and what to do.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Troubleshooting the Design System Generator

## Generation and inputs

### My open modal, typed text or folded cards reset when I changed an input

- **Why:** every change regenerates the whole system and rebuilds every tab.
- **What to do:** settle the brief first, then explore the tabs and the playground.

### My seed colour looks duller than the colour I entered

- **Why:** the seed's chroma is kept within a workable range, and ramp steps outside sRGB have their chroma reduced until they fit.
- **What to do:** this is expected. For more colour, try a more saturated style (Bold, Playful, Futuristic) or a **Vivid** ramp peak.

### My brand colour is not the primary button colour

- **Why:** the primary fill is the ramp step that is visible on the background (3:1) and takes a readable label at your target. Your exact seed may not meet that.
- **What to do:** keep the generated fill for accessibility, or lower the **Contrast target** if your requirements allow.

### Changing Industry does nothing to the colours

- **Why:** when a seed is set, the seed decides hue and chroma; the industry then only affects fonts and icons.
- **What to do:** select **Auto** beside the seed to go back to the industry's hue.

### Generation failed — see console

- **Why:** an unexpected error while generating.
- **What to do:** reload the page. If a shared link caused it, check its parameter values against [Share, save and connect](share-save-and-connect.md).

## Audit

### Some pairings say CHECK or the pill says N failing

- **Why:** a role colour does not meet its requirement.
- **What to do:** open the full audit and read **What would fix it**. Try the next contrast target, a less saturated style, or a different seed.

### The score went down when I relaxed the contrast target

- **Why:** lighter text tiers can collide (losing hierarchy points) and headroom shrinks.
- **What to do:** keep the stricter target and raise the score through a more saturated style or seed instead.

### The dark theme is not reflected in the score

- **Why:** the score uses the light roles. The dark roles are audited separately.
- **What to do:** open the full audit and choose **Dark**.

## Fonts and icons

### The type specimens look like system fonts

- **Why:** the fonts load from the Auric font CDN, with Google Fonts as a fallback. If both are blocked (by an extension, a firewall or no connection), the page uses system fonts. The names, sizes and weights shown are still correct.
- **What to do:** allow fonts.auricartisan.com and fonts.googleapis.com, or check your connection, then reload.

### The icons look generic, not like the recommended family

- **Why:** the real icons come from the Auric icon CDN. If it cannot be reached, the tool shows built-in line icons of the same stroke weight.
- **What to do:** allow icons.auricartisan.com and reload.

## Share, save and export

### A shared link opens with different ramp shape or token names

- **Why:** shared links, saved systems and your last visit do not apply the ramp shape or token naming.
- **What to do:** set **Ramp shape** and **Token naming** again after opening the link, or share the exported file.

### Save shows "Workspace library isn't available on this page"

- **Why:** the Library did not load on the page.
- **What to do:** reload. If it persists, use **Share** or an export to keep your system.

### A generator link in Connect shows a missing page

- **Why:** the Palette, Harmony, Gradient, Shade and Accessibility Generator pages are not available on the site at the time of writing.
- **What to do:** use the collections in the library area instead: [Colour libraries](../../../../library/colour-libraries/README.md).

### Download all gives a .txt file, not a zip

- **Why:** the bundle is one text file with every format separated by comment lines.
- **What to do:** download the formats you need one at a time, or split the bundle by hand.

### My Tailwind v3 or Figma export has no background or text roles

- **Why:** those formats do not carry role tokens.
- **What to do:** use CSS, Tailwind v4, JSON or a native export for roles. See the coverage table in [Export tokens](export-tokens.md).

### Native exports are missing spacing and radius after I set a token prefix

- **Why:** with a prefix or a non-kebab case, the native exporters may not recognise dimension tokens.
- **What to do:** export native formats with no prefix and kebab case, then rename in your project.

### Copy does nothing

- **Why:** the browser blocked clipboard access.
- **What to do:** select **Download** instead, or select the code in the export block and copy it by hand.

### The "Automate this" API note has gone from every tool

- **Why:** dismissing it with **×** hides it on all tool pages in this browser.
- **What to do:** clear the site's data for auricartisan.com in your browser to see it again.

## Related

- [FAQ](faq.md)
- [Limits and accuracy](../others/limits-and-accuracy.md)
- [Help centre](../../../../../help/README.md)
