---
title: Auric Artisan Icon Hub — Limits and accuracy
description: What Auric Artisan Icon Hub can and cannot do.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Limits and accuracy

## Catalog

- 12,895 icons and 32,802 indexed variants in seven collections, bundled with the extension.
- Metadata updates never add artwork or sets; new artwork arrives with extension updates.
- The combined Remix sprite is excluded because it is not a standalone icon.
- Material is font-backed and never exported as SVG.

## Output

- Stroke controls only affect stroke-based artwork.
- The eyedropper in the colour picker depends on the host.
- Contrast checks in the colour picker are guidance for choosing a colour against one background.
- Exports are capped at 200 icons each.

## CDN insertion

- CDN pages need network access and a content security policy that allows the CDN.
- The bridge is created only for saved files in trusted workspaces; untitled files, untrusted workspaces and unsupported file types are refused.
- JavaScript imports need module-aware tooling; server-rendered frameworks need the bridge in a client entry.
- At release, the published README noted that cross-origin access to the CDN's catalog files and fonts had not yet been enabled, so pages on other origins could show blank icons until it is.
- Previously generated local font stylesheets are not deleted automatically, and old local-font spans are not rewritten.

## Search

Search matches every word you type against the name, ID, category, search terms and set. It does not use synonyms beyond those search terms.

## Licences

Each collection keeps its upstream licence. The extension itself is under the Auric Artisan Free Use Licence.
