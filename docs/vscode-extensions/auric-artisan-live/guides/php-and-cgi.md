---
title: Auric Artisan Live — run PHP sites
description: Run .php pages in Auric Live through php-cgi or the PHP built-in server, and run other CGI scripts.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Run PHP sites

A plain static server sends a `.php` file to the browser as a download. Auric Live can run it instead, in one of two ways.

| Way | How it works | Best for |
| --- | --- | --- |
| **PHP through CGI** | Auric Live runs each `.php` request through `php-cgi` and serves the result itself | Classic PHP sites made of `.php` pages, with live reload and the dashboard |
| **PHP built-in server, Laravel or Symfony** | Auric Live starts PHP's own server (or `php artisan serve`, or `symfony server:start`) and forwards to it | Front-controller applications and frameworks |

*CGI* (Common Gateway Interface) is a standard way for a web server to run a program for each request and send back what it prints. With `php-cgi`, `$_GET`, `$_POST`, headers, cookies, sessions and `header()` calls all work.

Both ways need PHP installed on your computer, and both need a trusted workspace.

## Run PHP through CGI

1. Install PHP so that `php-cgi` is on your `PATH`, or note its full path.
2. Open the folder and run **Auric Live: Go Live**. The first time, Auric Live notices the PHP files and offers **Enable PHP**. Choose it.

   Or choose **PHP through CGI** in **Auric Live: Select Run Target…**, or set `auricLive.cgi.enabled` to `true`.
3. Open a `.php` page. It runs, and its output is served.

When you choose **Enable PHP**, the index list becomes `index.php`, then `index.html`, so a folder opens its `index.php`.

### CGI settings

| Setting | Default | What it does |
| --- | --- | --- |
| `auricLive.cgi.enabled` | `false` | Run matching files through a handler instead of serving them |
| `auricLive.cgi.handlers` | `{ ".php": "php-cgi" }` | The command for each file extension, for example `{ ".php": "php-cgi", ".cgi": "perl" }` |
| `auricLive.cgi.indexes` | `["index.php"]` | Extra index file names tried for a folder when CGI is on |

The handler must be on your `PATH` or given as a full path, such as `C:\php\php-cgi.exe`. In the project file you can also set `cgi.timeoutMs` (default 30000) for how long a script may run before the request fails.

The **Routes and Mocks** view lists each handler, for example `*.php` › `php-cgi`. If a script fails, the page shows an error overlay (`auricLive.liveReload.overlay`) and the output channel has the details.

## Run the PHP built-in server or a framework

In **Auric Live: Select Run Target…**, choose:

- **Laravel** when `artisan` is present: runs `php artisan serve --port=8000`.
- **Symfony** when `symfony.lock` is present: runs `symfony server:start --port=8000 --no-tls`.
- **PHP built-in server** when the folder has `composer.json`, `index.php` or `.php` files: runs `php -S 127.0.0.1:8000 -t <docroot>`, where the document root is `public` if `public/index.php` exists.

Auric Live starts the process, waits for it, and forwards requests to it. See [Run a backend or framework dev server](run-targets-and-backends.md) for supervision, port adoption and restarts.

## In an untrusted workspace

CGI settings (`auricLive.cgi.enabled`, `auricLive.cgi.handlers`, `auricLive.cgi.indexes`) are ignored until you trust the folder, even when a project file sets them. Choosing a PHP run target shows **Trust this workspace before running CGI, commands, or proxy profiles.**

When PHP is running, opening a `.php` page shows the rendered page, not its source, and the **Requests** view shows `cgi` as the handler.
