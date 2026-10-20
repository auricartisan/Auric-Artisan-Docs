---
title: Auric Artisan Icon Hub — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Artisan Icon Hub.
product: VS Code extensions › Auric Artisan Icon Hub
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| The catalog gained no new icons after **Refresh**. | Refresh updates compatible metadata only. | Install an extension update for new artwork. |
| The badge says **Offline · using local catalog**. | The metadata check could not reach or validate the website. | Local browsing still works. Check your connection or try **Refresh** later; automatic retries wait for the interval. |
| Material names such as `4k_plus` appear as text on my page. | The Material font is not loaded, often from an older insertion that used a local font. | Reinsert the icon with the current version so it uses a CDN placeholder, save the source, and reload the page with network access. Old spans are not rewritten automatically. |
| CDN icons appear blank on my site. | The page has no network access, your content security policy blocks the CDN, the bridge file is not served, or the CDN does not yet allow cross-origin access to its catalog and fonts. | Check network access, CSP and that the bridge is deployed. For self-contained artwork, use **Copy** as SVG or **Export ZIP**. |
| Insert says the workspace must be trusted. | Creating the CDN bridge needs a trusted workspace. | Trust the workspace, or use **Copy**. |
| Insert says to save the file first. | CDN insertion needs a saved local or remote file. | Save the file, then insert again. |
| Insert refuses because of a `<base>` URL or an external component script. | The bridge path could be wrong in those files. | Connect the bridge yourself, or use **Copy**. |
| Insert cannot use the editor. | No writable editor, or the editor is read-only. | Focus a writable text file, then return to the Hub. **Copy** is always available. |
| A Material icon cannot be inserted into my file. | Material insertion needs HTML or a web-framework file. | Use **Copy** with HTML, JSX, React component, CSS or CDN format. |
| Stroke has no effect. | The icon is filled, not stroke-based. | This is expected; choose an outline style. |
| **Export ZIP** includes a text list instead of Material SVGs. | Material icons are font-backed. | This is expected; they are listed in `MATERIAL_ICONS.txt`. |
| I also have Icon Studio. Which should I use? | They are separate products with separate settings and views. | Icon Hub: seven open-source sets, colour tools, sprite and ZIP export, CDN insertion. Icon Studio: Auric artwork, emoji and open-source sets, fully offline. |

If the problem continues, note your VS Code version, the Hub version (0.1.0), the icon ID and the steps to reproduce, remove private code from screenshots, and contact support at https://auricartisan.com/company/contact/.
