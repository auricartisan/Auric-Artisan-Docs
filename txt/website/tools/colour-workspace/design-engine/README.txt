==============================================================================
DESIGN SYSTEM GENERATOR
==============================================================================
What the Design System Generator (Design Engine) is, who it is for, where to
find it, and how to generate, check and export your first design system.
Area: Website › Tools › Colour workspace   Updated: 2026-09-25

The Design System Generator, also called the Design Engine, turns three
choices into a complete design system. You pick an industry, a style and a
contrast target, and the tool composes colour ramps in OKLCH, light and dark
colour roles that meet your contrast target, semantic colours, a font pairing
with a modular type scale, an icon family, and spacing, radius, shadow,
motion, z-index and breakpoint scales. That is 177 design tokens in the
default light-and-dark mode.

There is no Generate button. Every change regenerates the whole system at
once, and a contrast audit on the right of the screen re-runs with it, showing
a score out of 100, the twelve pairings it checks and whether each passes.
When you are happy, you export the tokens to any of twelve targets, from CSS
and Tailwind to Figma, SwiftUI and Jetpack Compose, or share a link that
rebuilds the exact same system.

Everything is calculated in your browser, and the same inputs always give the
same system. The tool does not know your brand, your competitors or your
product: the page itself says the result is generated, not designed. Treat it
as a well-built, well-checked starting point.

WHO IT IS FOR
=============

  - Product designers who want a coherent token set and the evidence that it
    passes contrast.
  - Front-end developers who want ready-to-use tokens in their stack's format
    and naming convention.
  - Accessibility leads who want to see every colour pairing's WCAG ratio and
    APCA value in one place.
  - Founders and small teams starting a product without a design system.

WHERE TO FIND IT
================

  - Page: https://auricartisan.com/tool/design-engine/
  - No sign-in is needed to generate, share or export. Saving systems uses
    your Auric Artisan Library.
  - The same job is available through the public API: the page shows the
    endpoint and its cost in API credits. See the Public API
    [../../../../services/public-api/README.txt].

QUICK START
===========

  1. Open https://auricartisan.com/tool/design-engine/. A system is generated
     straight away.
  2. In The brief on the left, choose an Industry, for example Healthcare.
  3. Choose a Style, for example Modern.
  4. Under Contrast target, choose AA or AAA.
  5. Watch The audit on the right: the score, and whether all twelve pairings
     pass.
  6. Open the Colour, Type and Components tabs to look at the result.
  7. Open Tokens, pick an export format such as CSS, and select Copy or
     Download.
  8. Select Share at the top to copy a link that rebuilds this system.

WHAT YOU CAN DO
===============

  - Generate a design system from 15 industry settings (Auto plus 14
    industries), 10 styles and 3 contrast targets.
  - Override the brand seed colour, harmony, colour mode, density, corner
    style, type ratio and ramp shape.
  - Rename every token with a prefix and a naming case (kebab, camel, snake or
    Pascal) before export.
  - Read colour ramps, semantic colours, surface roles, gradients, the type
    scale and roles, the icon family and every scale.
  - Try the tokens on a live, clickable component gallery in light and dark.
  - Audit twelve contrast pairings for both themes with WCAG 2.1 ratios and
    APCA values, with suggested fixes.
  - Compare the same brief across all ten styles or all industries.
  - Export to CSS, modern CSS, SCSS, Tailwind v3 and v4, Figma / W3C tokens,
    JSON, TypeScript, Android XML, SwiftUI, Flutter and Compose.
  - Save systems to your Library, restore them, and send the palette to other
    colour tools.

IN THIS FOLDER
==============

  - docs/ [docs/README.txt] — how to use the tool.
    - Getting started [docs/getting-started.txt]
    - Set the brief [docs/set-the-brief.txt]
    - Read the system [docs/read-the-system.txt]
    - Use the component playground [docs/component-playground.txt]
    - Check contrast with the audit [docs/contrast-audit.txt]
    - Compare styles and industries [docs/compare.txt]
    - Export tokens [docs/export-tokens.txt]
    - Share, save and connect [docs/share-save-and-connect.txt]
    - Reference [docs/reference.txt]
    - Troubleshooting [docs/troubleshooting.txt]
    - FAQ [docs/faq.txt]
  - others/ [others/README.txt] — supporting material.
    - Glossary [others/glossary.txt]
    - Limits and accuracy [others/limits-and-accuracy.txt]
    - Related [others/related.txt]
    - Privacy [others/privacy.txt]
