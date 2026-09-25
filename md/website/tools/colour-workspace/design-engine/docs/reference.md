---
title: Design System Generator — Reference
description: Every control, option, default, view and output of the Design System Generator in one place.
product: Website › Tools › Colour workspace
updated: 2026-09-25
---

# Design System Generator reference

## Page

| Item | Value |
| --- | --- |
| Address | https://auricartisan.com/tool/design-engine/ |
| Tabs | Overview, Colour, Type, Icons, Scales, Components, Tokens |
| Views | Compare, Workspace, Audit, Help |
| Tokens | 177 (light + dark), 163 (light only) |
| Export targets | 12 |
| Contrast measures | WCAG 2.1 ratio, APCA Lc |
| API equivalent | POST /v1/tokens/generate, 4 API credits per call |

## Masthead

| Control | What it does |
| --- | --- |
| **Surprise** | Random industry, style and target; seed reset to auto; harmony auto or random. Keeps other overrides. |
| **Share** | Copies a link with the current inputs and updates the address bar. |
| **Save** | Saves the system to your Library. |
| **Help** | Opens the **How this works** view. |
| **Workspace** | Opens saved systems and the Connect cards. |
| **Read the API reference →** | Opens the API documentation. |
| API note **×** | Hides the "Automate this" note; remembered in your browser. |
| **Expand** / **Collapse** | Hides or shows both side rails; remembered in your browser. |

## The brief

| Control | What it does | Values | Default |
| --- | --- | --- | --- |
| **Industry** | Brand hue, chroma, mood and font/icon tags | Auto, Fintech, Healthcare, SaaS / B2B, E-commerce, Education, Creative / Agency, Gaming, Luxury, Food & Drink, Travel, Real Estate, Non-profit, Crypto / Web3, Wellness | Auto |
| **Style** | Saturation, corners, shadows, weights, ratio, motion | Modern, Minimal, Classic, Bold, Playful, Elegant, Corporate, Brutalist, Organic, Futuristic | Modern |
| **Contrast target** | Body-text requirement | AA Large (3:1), AA (4.5:1), AAA (7:1) | AAA |
| **Density** | Body size and spacing | Compact (15 px, 4 px × 0.9), Comfort (16 px, 4 px), Spacious (17 px, 5 px × 1.15) | Comfort |
| **Seed** colour well and HEX box | Brand colour | Any HEX; **Auto** | Auto (from the industry) |
| Seed hue buttons | Set a seed at a fixed hue | 0° to 330° in 30° steps | — |
| **Harmony** | Secondary and accent hue positions | Auto, Complementary, Analogous, Triadic, Split-complementary, Tetradic, Monochrome | Auto |
| **Colour mode** | Which role sets are built into the tokens | Light, Dark, Both | Both |
| **Corner style** | Radius family | Auto, Sharp, Soft, Rounded, Pill | Auto |
| **Type ratio** | Modular scale ratio | Auto, 1.125, 1.2, 1.25, 1.333, 1.414, 1.5, 1.618 | Auto |
| **Ramp shape** span | Lightness travel of brand ramps | Tight, Even, Wide | Even |
| **Ramp shape** peak | Chroma curve of brand ramps | Flat, Natural, Vivid | Natural |
| **Token naming** prefix | Prefix for every token | Free text | Empty |
| **Token naming** case | Name style | kebab, camel, snake, Pascal | kebab |
| **Compare every style →** | Opens Compare | — | — |

## Generated system

| Part | Contents |
| --- | --- |
| Ramps | Primary, secondary, accent: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950. Neutral: 0, 50, 100 … 950, 1000. |
| Semantic | Success, warning, danger, info: solid, bg, border, text, and a label colour. |
| Roles | bg, bg-subtle, bg-muted, surface, elevated, border, border-strong, text, text-muted, text-subtle, primary, primary-hover, primary-active, primary-subtle, on-primary, ring (light, and dark unless mode is Light). |
| Gradients | brand, brand-soft, sunrise, mesh, subtle. |
| Type | Heading, body and mono families; 13 sizes (2xs to 7xl); 12 roles; leading (none, tight, snug, normal, relaxed, loose); tracking (tighter, tight, normal, wide, wider, widest). |
| Icons | One of Feather, Lucide, Heroicons, Phosphor, Tabler, Remix Icon, Material Symbols, with stroke width. |
| Spacing | 19 steps: 0, px, 0.5, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40. |
| Radius | none, sm, md, lg, xl, 2xl, 3xl, pill. |
| Shadows | xs, sm, md, lg, xl, 2xl, inner, primary. |
| Motion | Durations fast, base, slow; easings standard, spring. |
| Z-index | base 0, dropdown 1000, sticky 1100, banner 1200, overlay 1300, modal 1400, popover 1500, toast 1600, tooltip 1700. |
| Breakpoints | sm 640, md 768, lg 1024, xl 1280, 2xl 1536 (px). |

Motion by style personality:

| Personality | fast / base / slow (ms) | Used by |
| --- | --- | --- |
| Subtle | 120 / 200 / 320 | Minimal, Corporate |
| Smooth | 150 / 250 / 400 | Modern, Classic, Elegant, Organic |
| Snappy | 110 / 180 / 280 | Bold, Brutalist, Futuristic |
| Bouncy | 160 / 280 / 460 | Playful |

## Tabs

| Tab | Cards |
| --- | --- |
| **Overview** | System summary, At a glance, Generation recipe, Jump to |
| **Colour** | Color ramps, Semantic colors, Surfaces & roles, Gradients (folded) |
| **Type** | Font pairing, Type scale, Roles, Available weights (folded) |
| **Icons** | Recommended icon family, Preview set, On brand color (folded), Size ramp (folded) |
| **Scales** | Spacing scale, Border radius scale, Elevation / shadow scale, Shadow values (folded), Durations, Easing curves |
| **Components** | Component playground |
| **Tokens** | Find token, Design tokens, Export tokens |

## Component playground controls

| Control | Values | Default |
| --- | --- | --- |
| **Theme** | Light, Dark (as allowed by colour mode) | Light |
| **Density** | Compact, Cozy, Spacious | Cozy |
| **Corners** | Auto, Sharp, Soft, Round, Pill | Auto |
| **Elevation** | None, Flat, Auto, Deep | Auto |
| **Buttons** | Auto, Square, Pill | Auto |
| **Viewport** | Fluid, Desktop, Tablet, Mobile | Fluid |
| **↺ Reset** | Resets density, corners, elevation, buttons, viewport | — |
| Category chips | ✦ All, Navigation, Buttons, Forms, Feedback, Data, Overlays, Commerce, Marketing, Industry | ✦ All |
| Scene chips (Industry) | The 14 industries | Your industry, or SaaS |

## Audit

| Item | Value |
| --- | --- |
| Pairings | 12 per theme (8 roles + 4 semantic solids) |
| Requirements | Target (body, text on surface, text on muted), 4.5 (muted text, on-primary), 3 (subtle text, primary vs bg, semantic solids), 1.4 (strong border) |
| Score | Accessibility 55, Vibrancy 18, Headroom 15, Hierarchy 12; range 40–100 |
| Rail score colours | Green 85+, amber 70+, red below |
| Overview ring colours | Green 85+, amber 65+, red below |
| Full audit | Theme audited (Light, Dark), requirements, What would fix it, Every foreground on every surface, Color-vision preview |
| Matrix colours | Gold: meets target; green: 4.5+; amber: 3+; red: below 3 |
| APCA rating labels | Lc 90 fine print, Lc 75 body text, Lc 60 fluent text, Lc 45 large/bold, Lc 30 headlines, Lc 15 non-text, insufficient |

## Compare

| Control | Values | Default |
| --- | --- | --- |
| **Vary** | Style, Industry | Style |
| **Order by** | Score, Chroma, Listed | Score |
| **Use** | Adopts that style or industry | — |

## Export formats

| Pill | File | Language |
| --- | --- | --- |
| CSS | tokens.css | css |
| CSS (modern) | tokens.modern.css | css |
| SCSS | _tokens.scss | scss |
| Tailwind v3 | tailwind.config.js | javascript |
| Tailwind v4 | theme.css | css |
| Figma / W3C | design-tokens.json | json |
| JSON | design-system.json | json |
| TypeScript | tokens.ts | typescript |
| Android XML | colors.xml | xml |
| SwiftUI | DesignTokens.swift | swift |
| Flutter | app_tokens.dart | dart |
| Compose | Tokens.kt | kotlin |

Buttons: **Copy**, **Download**, **Download all (.zip-less bundle)** (`design-system-bundle.txt`). Coverage per format: see [Export tokens](export-tokens.md).

## Share link parameters

`industry`, `style`, `a11y`, `mode`, `density`, `harmony`, `ratio`, `corner` and `seedHex` are applied when a link is opened. `rampSpan`, `rampPeak`, `tokenPrefix` and `tokenCase` are written into shared links but not applied. See [Share, save and connect](share-save-and-connect.md).

## Messages

| Message | When |
| --- | --- |
| **Copied …** | A value was copied. |
| **Shareable link copied ✓** | After **Share**. |
| **Saved to workspace ⭐** | After **Save**. |
| **Workspace library isn't available on this page** | Save could not reach the Library. |
| **Restored from workspace ✓** | After **Restore**. |
| **Couldn't read that saved system** | A saved item had no inputs. |
| **Removed from workspace** | After **Delete**. |
| **Export copied ✓**, **Downloaded …**, **Downloaded full bundle ✓** | After export actions. |
| **Using …** | After **Use** in Compare. |
| **Generation failed — see console** | Generation hit an error. |

## Related

- [Getting started](getting-started.md)
- [Glossary](../others/glossary.md)
