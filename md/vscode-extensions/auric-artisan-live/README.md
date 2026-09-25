---
title: Auric Artisan Live — live server and preview for VS Code
description: What Auric Artisan Live does, who it is for, how to install it and where to find every guide.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Auric Artisan Live

Auric Artisan Live (full name **Auric Artisan Live — Live Server & Preview**) is a local development server inside VS Code. Run **Go Live** and it serves your project folder over a real HTTP server on your own machine, opens it in your browser or in a preview beside your code, and updates connected pages when you save. It works for plain HTML, CSS and JavaScript, and it can also run or connect to a backend: PHP, Python, Ruby, Go, Java, Node.js and more.

Around the server it gives you the tools you normally need a second terminal or a browser extension for: HTTPS with a generated certificate, an API proxy so your page and your backend share one origin, mock endpoints and a JSON-file REST database for APIs that do not exist yet, a request inspector with curl and fetch copies and HAR export, slow-network simulation, a phone QR code for testing on a real device, and an in-page developer dashboard (`Alt` + `Shift` + `D`) showing page health, network, storage and server state.

Everything runs locally. The extension has no runtime npm dependencies and no telemetry. It is a development server, not production hosting.

## Who it is for

- Front-end developers who want live reload and a quick preview while editing HTML, CSS and JavaScript.
- Full-stack developers who run a framework dev server or a backend and want one address for the page and its API.
- PHP developers who want `.php` pages to run instead of download.
- Anyone testing a site on a phone, over HTTPS, or on a slow connection.
- Developers debugging requests: which rule answered, how long it took, what was sent.

## Where to find it

- Marketplace ID: `auric-artisan.auric-artisan-live`
- Marketplace page: https://marketplace.visualstudio.com/items?itemName=auric-artisan.auric-artisan-live
- Install from a terminal:

  ```text
  code --install-extension auric-artisan.auric-artisan-live
  ```

- Requires VS Code 1.95 or newer and a folder on disk. Version 0.2.1 at the time of writing.
- Interface in English and Hindi. See [Use an extension in Hindi](../install-and-setup/docs/display-language-hindi.md).

## Quick start

1. Install the extension and open your website folder in VS Code (**File** › **Open Folder…**).
2. Run **Auric Live: Go Live** from the Command Palette, press `Ctrl` + `Alt` + `L` (`Cmd` + `Alt` + `L` on macOS), or select **Go Live** in the status bar.
3. Your default browser opens at `http://localhost:5500` (or the next free port). A notification offers **Open**, **Preview** and **Phone QR**.
4. Edit an HTML, CSS or image file and save it. Connected pages update: stylesheets and images swap in place, HTML reloads.
5. Press `Ctrl` + `Alt` + `K` to open a preview beside your editor, and pick a device size.
6. Open the **Auric Live** icon in the Activity Bar to see the **Servers**, **Requests** and **Routes and Mocks** views.
7. Press `Ctrl` + `Alt` + `Shift` + `I` to open the control panel for requests, run targets, routing and session settings.
8. Stop with **Auric Live: Stop Server**, or stop every server with `Ctrl` + `Alt` + `Shift` + `L`.

## What you can do

- Serve a folder, a subfolder or a build output (`dist`, `public`) with live reload on save.
- Swap changed CSS and images without a full reload, and restore scroll position after one.
- Preview beside your code at responsive, phone, tablet, laptop and desktop sizes, with rotation.
- Open the site on your phone with a locally generated QR code.
- Serve over HTTPS with a generated or imported certificate.
- Run a detected backend or framework dev server (PHP, Python, Ruby, Go, Java, Node.js, Deno, Bun, .NET, Rust, Elixir, Hugo, Jekyll and more), or your own command, and forward to it.
- Connect to a backend that is already running, and wait for it while it starts.
- Proxy API paths to a backend, including WebSockets.
- Answer mock endpoints and a full REST API from a JSON file.
- Run PHP through `php-cgi`.
- Inspect, filter, sort, replay and export requests as HAR; copy any request as curl or fetch.
- Simulate slow 3G, 3G, 4G, cable or custom networks for every client, including a phone.
- Open an in-page developer dashboard with health, network, server, storage, environment, request and console tabs.
- Keep the setup with the repository in `auric.live.json` and `.auricignore-live`.

## In this folder

- [docs/](docs/README.md) — task guides and the full reference.
  - [Getting started](docs/getting-started.md)
  - [Serve a folder with live reload](docs/serve-and-live-reload.md)
  - [Preview, devices and phone testing](docs/preview-and-devices.md)
  - [Run a backend or framework dev server](docs/run-targets-and-backends.md)
  - [Run PHP sites](docs/php-and-cgi.md)
  - [Proxy an API, mock endpoints and a REST database](docs/api-proxy-and-mocks.md)
  - [Inspect requests](docs/inspect-requests.md)
  - [Use the in-page browser dashboard](docs/browser-dashboard.md)
  - [Serve over HTTPS](docs/https-and-certificates.md)
  - [Simulate a slow network](docs/network-simulation.md)
  - [Project configuration](docs/project-configuration.md)
  - [Reference: commands, keys and settings](docs/reference.md)
  - [Troubleshooting](docs/troubleshooting.md)
  - [FAQ](docs/faq.md)
- [others/](others/README.md) — supporting material.
  - [Glossary](others/glossary.md)
  - [Shortcuts](others/shortcuts.md)
  - [Limits and safeguards](others/limits-and-accuracy.md)
  - [Privacy](others/privacy.md)
  - [Related](others/related.md)
  - [Release notes](others/release-notes.md)
