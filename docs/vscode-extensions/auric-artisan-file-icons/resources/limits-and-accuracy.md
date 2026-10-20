---
title: Auric Artisan File Icons — Limits and accuracy
description: What the File Icons themes, smart detection and code output can and cannot do.
product: VS Code extensions › Auric Artisan File Icons
updated: 2026-09-25
---

# Limits and accuracy

## Themes

- Only one file icon theme can be active in VS Code.
- Appearance and association changes need a window reload.
- Parent patterns match the direct parent only, not a recursive path.
- The asset totals include open-folder states, framework artwork and alternatives; they are not counts of unique file types.

## Smart detection

- Detection is a heuristic based on names, dependencies and the start of small files. It can miss projects or match unexpectedly; use **Explain Smart Icon Match** to see why.
- By default it considers up to 250 direct entries per folder and text files up to 64 KiB, cached for 15 seconds. The workspace scan checks up to 80 first-level folders.
- Decorations supplement the icon; they do not replace the artwork dynamically.
- VS Code limits badges to two characters.
- Availability in remote and virtual workspaces depends on the file system provider.

## Code output

- Output uses shipped artwork; Explorer appearance settings are not applied to it.
- Insertion adds no surrounding quotes and does not save the file.
- Check the insertion context and add meaningful alternative text where needed.

## Licence

Free to install and use under the Auric Artisan Free Use Licence. It is not an open-source or unrestricted asset licence: redistribution, resale, republishing and extraction of bundled artwork are restricted. Inserting code does not change those terms.
