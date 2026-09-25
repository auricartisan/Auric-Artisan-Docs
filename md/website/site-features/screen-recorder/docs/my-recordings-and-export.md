---
title: Screen recorder — My recordings and export
description: Play, rename, trim, export and delete your recordings.
product: Website › Site features › Screen recorder
updated: 2026-09-25
---

# My recordings and export

**My recordings** lists every recording kept in this browser. It opens after each recording, or from **My recordings** in the recorder dialog.

## The list

The panel header has a grip to move it, the title **My recordings**, **New recording** (opens the setup dialog) and **Close**. `Esc` closes it.

Each recording shows:

- a thumbnail; select it to play the recording;
- its title, which you can edit in place (an empty title becomes "Untitled recording");
- details: length, file size, pixel size, and "with audio" when it has sound;
- actions: **Download video**, **GIF**, **Frames**, **Still**, **Trim** and **Delete**.

The foot of the panel shows the total, for example "4 recordings · 38.2 MB used · 1.1 GB free".

With no recordings, the panel reads "No recordings yet." with a **Record something** button.

## Play a recording

Select the thumbnail. A player opens with the recording's title and standard video controls. `Esc` or **Close** closes it.

## Download the video

Select **Download video**. The file downloads as MP4 or WebM, whichever format this browser recorded.

## Export an animated GIF

1. Select **GIF** (Export as an animated GIF).
2. A progress bar shows "Encoding GIF…".
3. The GIF downloads, and the message gives its size, for example "GIF exported — 2.4 MB."

GIFs are made at 10 frames per second, at most 640 pixels wide, with up to 300 frames, and they loop. Longer recordings are sampled evenly across their length.

## Export frames

Select **Frames** (Export every frame as PNG (ZIP)). A progress bar shows "Exporting frames…", then a ZIP file downloads containing PNG images named `frame-0001.png`, `frame-0002.png` and so on. Frames are taken five times per second, at most 1,280 pixels wide, up to 120 frames.

## Save a still

Select **Still** (Save the current frame as a PNG). A progress bar shows "Grabbing frame…", then a PNG downloads. The still is taken one second into the recording (or halfway through a recording shorter than two seconds), at most 1,280 pixels wide.

## Trim a recording

1. Select **Trim**. The player opens with the trim controls showing (or select **Trim…** in the player).
2. Enter **Start** and **End** in seconds (to one decimal place). **End** starts as the full length.
3. Select **Export trimmed clip**.
4. The trimmed clip downloads as a new file with "-trimmed" added to its title: "Trimmed clip exported."

Trimming re-encodes in real time, so a 30-second clip takes about 30 seconds. The original recording is not changed. If **End** is not after **Start**, the message reads "End must be after start."

## Delete a recording

Select **Delete** (the bin), then select it again within four seconds ("Click again to delete permanently"). The recording is removed from this browser. This cannot be undone.

## File names

Downloads are named from the recording's title and the time it was made, for example `Recording-Sep-24-1042-AM-2026-09-24-05-12-33.mp4`. The date in the title follows your browser's language settings; the time stamp at the end is in UTC. Characters other than letters, numbers, spaces and hyphens are removed, spaces become hyphens, and the title part is limited to 48 characters.

## If an export fails

The message explains why, for example "That recording could not be read.", "No frames could be read from that recording." or "The ZIP library could not be loaded." (frames export needs to load a small helper from the site the first time).
