---
title: Auric Artisan Live — FAQ
description: Short answers to common questions about Auric Artisan Live.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# FAQ

## Is Auric Live a production web server?

No. It is a development server for your own machine. Do not use it to host a public site.

## Does it need Node.js or other software?

Serving static files needs nothing extra. Running a backend needs that backend's runtime (PHP, Python, Node.js and so on) and the project's dependencies, installed by you. The extension itself has no runtime npm dependencies.

## What is the default address?

`http://localhost:5500`, or the next free port. Change it with `auricLive.port`.

## Can other people on my network see my site?

In a trusted workspace the default host `0.0.0.0` lets devices on your local network reach the server, subject to your firewall. Set `auricLive.host` to `127.0.0.1` to keep it on your machine, or turn on `auricLive.auth.enabled` to require a password.

## Why does the page not reload for files my build tool writes?

The default trigger reacts only to saves in VS Code, so generated and synchronised files cannot keep refreshing the page. Set `auricLive.liveReload.reloadOnSave` to `change` for build tools.

## Can I use it with Vite, Next.js, Angular or another framework?

Yes. Choose the framework's dev server as the run target. Auric Live starts it, forwards to it and keeps the framework's own hot reload in charge, while still adding its dashboard.

## Can I run PHP?

Yes, through `php-cgi` or the PHP built-in server, with PHP installed. See [Run PHP sites](php-and-cgi.md).

## Can I serve several projects at once?

Yes. Each folder of a multi-root workspace gets its own server and port. Use **Select Active Server** to choose which one the panel shows.

## Does it work in an untrusted folder?

Partly. Static serving, live reload and request inspection work on this machine only. Running commands, PHP, proxying, file-backed mocks, custom certificates and network access need trust.

## Does it work over Remote SSH, in containers or in virtual workspaces?

It needs a real file system and a port. Virtual workspaces are not supported. In remote setups it runs next to the files; forward the port to reach it from your computer.

## Does HTTPS remove the browser warning?

Only if the browser trusts the certificate. The generated certificate is self-signed, so each browser or device warns until you trust it. A certificate your devices already trust removes the warning.

## Is my request data sent anywhere?

No. Requests are recorded locally, credentials are masked, and HAR exports leave out bodies by default. There is no telemetry.

## Can I use it in Hindi?

Yes. Choose **हिन्दी** in the control panel header, or set `auricLive.interfaceLanguage` to `hi`. The browser dashboard and your website are not translated.

## How is it different from other live servers?

Besides live reload, it runs and waits for backends, proxies and mocks APIs, serves a REST API from a JSON file, inspects and replays requests, simulates slow networks for every client, and adds an in-page dashboard.
