==============================================================================
DESIGN TOOL PLUGINS
==============================================================================
Which Auric Artisan plugins for design tools and launchers exist, what they
are planned to do, and why none can be installed yet.
Area: Design tool plugins   Updated: 2026-09-25

Auric Artisan is building small plugins that bring its colour and
accessibility checks into design tools and launchers: Figma, Penpot, Sketch,
Raycast and Alfred. None of them is published yet. There is no listing in the
Figma Community, the Penpot plugin catalogue, the Raycast Store or elsewhere,
and no download on auricartisan.com. This page will become full documentation
for each plugin when it can be installed.

In the meantime, the same checks are available today in the browser extension
[../browser-extension/README.txt], in the VS Code extensions (see the VS Code
extensions section of these docs), and in the tools on
https://auricartisan.com.

WHAT EXISTS
===========

  Plugin:          Auric Artisan for Figma
  Host:            Figma
  Planned purpose: Audit layers for WCAG and APCA contrast, generate palettes,
                   fix failing pairs, preview colour vision
  Status:          Not published

  Plugin:          Auric Artisan for Penpot
  Host:            Penpot
  Planned purpose: The same audit, palette, fix and vision workflow for Penpot
                   files
  Status:          Not published

  Plugin:          Auric Artisan for Sketch
  Host:            Sketch on macOS
  Planned purpose: Menu commands to audit a selection, auto-fix failing pairs,
                   generate a palette and preview colour vision
  Status:          Not published

  Plugin:          Auric Artisan for Raycast
  Host:            Raycast on macOS
  Planned purpose: A Check Contrast command for any two colours, with WCAG and
                   APCA results
  Status:          Not published

  Plugin:          Auric Artisan for Alfred
  Host:            Alfred on macOS
  Planned purpose: A contrast check typed as `aa contrast` followed by two
                   colours
  Status:          Not published

The site's article "Auric Artisan Plugins User Guide"
(https://auricartisan.com/library/documentation/articles/2026-05-26-plugins-user-guide)
describes how the plugins are intended to work. Because none of them can be
installed from a store or a download today, treat that article as a preview
rather than installation instructions.

PLANNED CAPABILITIES IN BRIEF
=============================

These descriptions come from the site's plugins guide and may change before
release.

  - Design plugins (Figma, Penpot, Sketch): check the contrast of text against
    its effective background in the selected frame or layers (or the current
    page when nothing is selected), report the WCAG ratio and APCA Lc of
    failing pairs, select or outline failing layers, nudge failing colours
    toward a target ratio, generate palettes from a seed colour, and preview
    protanopia, deuteranopia, tritanopia and achromatopsia.
  - Launcher plugins (Raycast, Alfred): check the contrast of two colours
    typed as HEX, `rgb()`, `hsl()` or CSS colour names, and copy the ratio,
    the APCA value, normalised HEX values or a summary.
  - Privacy: the plugins are designed to run locally in their host
    application, without an Auric Artisan account or API key for contrast
    checks.

WHEN THEY ARE RELEASED
======================

This folder will then hold, for each published plugin, the standard set of
pages: an overview, installation from its store, getting started, every
command and option, troubleshooting, an FAQ, a glossary, release notes and
privacy.

RELATED PAGES
=============

  - Browser extension [../browser-extension/README.txt]
  - Public API [../services/public-api/README.txt]
