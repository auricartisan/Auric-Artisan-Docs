---
title: Auric Artisan Icon Hub — Connect the icon CDN
description: How Icon Hub's Insert connects your HTML and web-framework files to the Auric icon CDN, what file it creates, and what your site needs.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Connect the icon CDN

In HTML and supported web-framework files, **Insert** places an icon placeholder that is drawn at runtime by the Auric icon CDN script, `https://icons.auricartisan.com/icon-cdn.js`. This works for all seven collections, including Material, whose glyphs load their matching font from the CDN.

A **CDN** (content delivery network) is a web service that serves files, here icon data and fonts, to your pages.

## What happens on your first Insert

1. Icon Hub checks the target file. It must be saved, local or in a VS Code remote workspace, and the workspace must be trusted.
2. It creates a small file called `icons.auricartisan.com.js` next to your source file and saves it. This **bridge** contains loader logic only: no fonts, no embedded font data and no icon catalog.
3. It connects the bridge to your file:

| File type | Connection added |
| --- | --- |
| HTML | `<script src="./icons.auricartisan.com.js" defer data-auric-icons="cdn"></script>` after `<head>` |
| JavaScript, TypeScript, React JSX and TSX | `import "./icons.auricartisan.com.js";` at the top, after any directives such as `"use client"` |
| Vue, Svelte | An import inside the component's `<script>` block (a block is added if there is none) |
| Astro | A browser-side `<script>` with the import at the end of the file (not a server-only frontmatter import) |

4. It inserts the icon placeholder at your cursors. The whole change is one edit labelled "Insert Auric icon and local CDN support".
5. The message ends "CDN bridge connected."

On later inserts, an existing matching bridge and connection are reused. If a different file already uses the bridge name, a second name with a short hash is used; existing files are never overwritten.

Only the bridge is saved automatically. Save your source file yourself.

## At runtime

The bridge loads the CDN script once, renders every icon placeholder on the page, and also renders icons added later or whose attributes change.

## Requirements and limits

- Pages need network access to show CDN icons.
- Your site's content security policy must allow the CDN for scripts, data requests and fonts, and the loader's generated font styles.
- Serve the bridge file with your application.
- JavaScript imports need module-aware tooling or a module script. Server-rendered frameworks need the bridge in a browser (client) entry.
- An HTML file that uses a `<base>` URL, or a Vue or Svelte component that uses an external script, is refused with an explanation; connect the bridge yourself or use Copy.
- If a selection overlaps the place where the loader connection goes, Insert asks you to place the cursor inside the page content.
- If the editor changes while Insert prepares, it asks you to try again.
- Browsing, searching, previewing, **Copy** and **Save** never create project files.

> **Note:** At the time of the 0.1.0 release, the published README noted that cross-origin access to the CDN's catalog files and fonts had not yet been enabled for other sites. Until it is, pages served from other origins may show blank icons even with a correct bridge. For fully self-contained artwork, use **Copy** as SVG or export SVG files. Material is font-backed and has no SVG form.

## Messages

| Message | Meaning |
| --- | --- |
| Save this file locally or in your remote workspace before inserting CDN icons. Copy is still available. | The file is untitled or on an unsupported file system. |
| Trust this workspace before generating CDN support files. SVG insertion and Copy are still available. | The workspace is in Restricted Mode. |
| CDN insertion requires an HTML or web-framework source file. Use Copy for other output formats. | The file type is not supported for CDN insertion. |
| The CDN support filenames are already used by different files. No files were overwritten. | Both bridge names are taken by other content. |
| Icon inserted, but its new CDN bridge could not be saved. Save the support file before previewing the page. | Save the bridge file manually. |

## Result

Your page references the Auric icon CDN through a small local bridge, and each inserted placeholder renders as the chosen icon when the page loads.
