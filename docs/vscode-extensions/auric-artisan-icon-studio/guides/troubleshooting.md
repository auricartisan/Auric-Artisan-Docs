---
title: Auric Artisan Icon Studio — Troubleshooting
description: Symptoms, causes and fixes for common problems with Auric Artisan Icon Studio.
product: VS Code extensions › Auric Artisan Icon Studio
updated: 2026-09-25
---

# Troubleshooting

| Symptom | Why it happens | What to do |
| --- | --- | --- |
| No search results. | A collection or category filter is narrowing the search, or you are in Likes or Recent. | Select **Reset filters**, switch to **Library**, and try a simpler word or synonym. |
| A style or skin tone option is missing. | Styles differ by collection; the Style control only appears when one collection with several styles is chosen. Only some emoji support skin tones. | Choose a single collection to see its styles. |
| **For you** chip is missing. | Recommendations are turned off. | Turn on `auricIconStudio.recommendations.enabled`. |
| **For you** is empty. | There is no editor context and no likes or usage yet. | Open a file, and like or use a few icons. |
| Insert copied the icon instead. | No editor was available to insert into. | Open and focus a writable text editor, then insert again. |
| "VS Code could not apply the edit." | The editor is read-only or rejected the change. | Use **Copy**, or open a writable file. |
| A Material icon shows as a word in my app. | Material output needs the Material font; the Studio's preview font is not installed in your project. | Load the matching Material Icons font and styles in your application. |
| I cannot save a Material icon or emoji as SVG. | They are font glyphs and characters, not SVG files. | Use **Copy** or **As…** for a text format. |
| The output needs editing. | Smart insert picks a format; it does not integrate the icon into your code for you. | Use **As…** for a different format and check the insertion point. |
| The Modern, Drawn or Playful library view disappeared. | Icon Studio is hosting those collections. | Turn off `auricIconStudio.hostFamilyLibraries` to show their views again. |
| `Ctrl` + `Alt` + `I` does not run Icon Studio. | The editor is not focused, another extension uses the same keys, or Icon Studio's shortcuts stepped aside because you kept the separate collection views. | Focus the editor, check **Keyboard Shortcuts** for conflicts, and review `hostFamilyLibraries`. |
| Hovering an Auric icon ID shows no Icon Studio preview. | The owning collection extension is installed and shows its own preview, or previews are off. | This is expected; or turn on `auricIconStudio.hoverPreview`. |
| Emoji look different from other screenshots. | Emoji are drawn by your operating system's emoji font. | This is expected; newer emoji may not appear with older fonts. |
| An error says the icon catalog failed to load. | The installed extension files are damaged or incomplete. | Reinstall the extension from the Marketplace. |

## Reset personalisation

Run **Auric Icon Studio: Clear Likes, Recents and Learned Recommendations** and confirm with **Clear**.

## Still stuck

Note your VS Code version, the Icon Studio version, the collection and icon ID, and the steps that reproduce the problem. Remove private code and paths from screenshots, then contact support at https://auricartisan.com/company/contact/.
