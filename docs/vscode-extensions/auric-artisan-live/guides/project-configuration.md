---
title: Auric Artisan Live — project configuration
description: Keep an Auric Live setup with your repository in auric.live.json, control exclusions with .auricignore-live, and understand how settings, project files and session changes combine.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Project configuration

## Where settings come from

Auric Live combines four layers. A later layer wins:

1. **Built-in defaults.**
2. **VS Code settings** — user, workspace and folder settings with the `auricLive.` prefix.
3. **The project file** — `auric.live.json` in the workspace folder.
4. **Session overrides** — changes you make with commands, the Auric Live menu or the control panel. They last until you close or reload the VS Code window.

So a repository can carry its own proxy, mock and CGI setup, and you can still try something for a moment without editing a file.

## The project file: auric.live.json

### Create it

1. Run **Auric Live: Create Project Config File**, or select **Create a config file** in the **Servers** view when nothing is running.
2. Auric Live writes a starter `auric.live.json` in the workspace folder and opens it.

The starter file:

```json
{
  // Auric Artisan Live — project configuration.
  // Every key is optional and overrides the matching auricLive.* setting.
  "port": 5500,
  "spa": { "enabled": false, "fallback": "/index.html" },
  "cleanUrls": false,

  // Send /api to a backend you already run, so the front end talks to the
  // real thing without a CORS shim.
  "proxy": [
    {
      "path": "/api",
      "target": "http://localhost:3000",
      "changeOrigin": true,
      "ws": true
    }
  ],

  // Or answer /api yourself while that backend does not exist yet.
  "mock": {
    "enabled": false,
    "routes": [
      {
        "method": "GET",
        "path": "/api/health",
        "status": 200,
        "body": { "ok": true, "service": "auric-live" }
      },
      {
        "method": "POST",
        "path": "/api/session",
        "status": 201,
        "delayMs": 250,
        "body": { "id": "{{uuid}}", "user": "{{body.user}}", "issued": "{{now}}" }
      }
    ],
    "rest": {
      "enabled": false,
      "base": "/api",
      "database": "db.json"
    }
  },

  "headers": [
    { "match": ["**/*.html"], "headers": { "X-Frame-Options": "SAMEORIGIN" } }
  ],

  "liveReload": { "enabled": true, "reloadOnSave": "save", "cssHotSwap": true, "overlay": true },

  // Alt+Shift+D opens the in-page developer dashboard. Diagnostics are saved
  // locally under .auric-live/ without headers, bodies, queries or values.
  "dashboard": { "enabled": true, "customCursor": true },
  "records": { "enabled": true, "maxRequests": 200 }
}
```

### Rules for the file

- Every key is optional. Keys are the setting names **without** the `auricLive.` prefix, nested as objects: the setting `auricLive.liveReload.cssHotSwap` is `"liveReload": { "cssHotSwap": … }`.
- Comments (`//` and `/* … */`) and trailing commas are allowed.
- A `$schema` key is ignored.
- The file is looked for in the workspace folder first, then in `.auric/`.
- Change the file name with the `auricLive.configFile` setting.
- If the file is not valid JSON, Auric Live shows **Auric Live: auric.live.json is not valid JSON** with the error, and ignores the file until it is fixed.

### Open and reload

- **Auric Live: Open Project Config File** opens it. If there is none, it offers **Create it**.
- Changes apply as soon as you save, while `auricLive.autoRestart.onConfigChange` is on (the default). **Auric Live: Reload Configuration** re-reads everything by hand.
- Several commands offer **Save to config file** after a session change: adding a proxy route or a mock route, and the **Write config** choice when a framework is detected.

### A fuller example

```json
{
  "host": "127.0.0.1",
  "port": 5500,
  "open": "none",
  "liveReload": {
    "enabled": true,
    "reloadOnSave": "save",
    "cssHotSwap": true,
    "preserveScroll": true
  },
  "dashboard": {
    "enabled": true,
    "independent": false
  },
  "proxy": [
    { "path": "/api", "target": "http://localhost:3000" }
  ],
  "inspector": {
    "sensitiveFields": ["customerPin"],
    "harIncludeBodies": false
  },
  "console": {
    "enabled": true,
    "levels": ["error", "warn", "info"]
  },
  "throttle": {
    "profile": "custom",
    "latencyMs": 150,
    "downloadKbps": 1600,
    "uploadKbps": 750
  },
  "maxRequestBodyBytes": 16777216,
  "requestBodyTimeoutMs": 30000
}
```

### Additional project-file keys

These keys have no VS Code setting of their own but are accepted in `auric.live.json`:

| Key | Default | Meaning |
| --- | --- | --- |
| `mount` | `/` | Serve the site under a sub-path, such as `/app` |
| `trailingSlash` | `preserve` | `preserve`, `add` or `remove` a trailing slash, by redirect |
| `liveReload.fullReload` | `[]` | Globs whose changes always cause a full reload instead of a hot swap |
| `watch.extraPaths` | `[]` | Additional absolute paths to watch |
| `cors.methods` | `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS` | Methods allowed on cross-origin requests |
| `cors.headers` | `*` | Request headers allowed on cross-origin requests |
| `cors.exposeHeaders` | `[]` | Response headers exposed to cross-origin scripts |
| `cors.maxAge` | `600` | Seconds a browser may cache a preflight answer |
| `auth.realm` | `Auric Live` | Name shown in the browser's login prompt |
| `cgi.timeoutMs` | `30000` | How long a CGI script may run |
| `mock.rest.pageSize` | `10` when unset | Page size when `_page` is given without `_limit` |
| `maxPortAttempts` | `40` | How many ports `increment` tries before giving up |

## Workspace trust and the project file

In an untrusted workspace, a project file cannot switch on anything that runs code or opens the server to other devices. These keys are ignored until you trust the folder: `cgi.enabled`, `cgi.handlers`, `cgi.indexes`, `proxy`, `host`, `auth.username`, `auth.password`, `https.certPath`, `https.keyPath` and `mock.rest.persist`. Run commands, proxying, CGI, file-backed mocks, custom certificate files and listening on your network all need trust. Static serving, live reload and request inspection keep working on this machine.

## Exclusions: .auricignore-live

`.auricignore-live` lists paths Auric Live must leave completely alone. A matched path is never served, listed, watched, hot-swapped, reloaded or recorded.

1. Run **Auric Live: Open .auricignore-live**. If the file does not exist, a commented starter is created in the served folder.
2. Add one pattern per line, relative to the served folder.
3. Save. The patterns apply straight away.

```text
# Auric Artisan Live project exclusions
# One glob per line, relative to the served root. Later !rules re-include a path.
private/**
generated/**
!generated/preview/**
```

The syntax is a small, predictable part of the `.gitignore` syntax:

- blank lines and lines starting with `#` are ignored;
- `*`, `**` and `?` are wildcards;
- a pattern ending in `/` matches a folder and everything inside it;
- a pattern starting with `/` is anchored to the served root;
- a later line starting with `!` re-includes something an earlier line excluded.

Choosing **Ignore *folder*/** after a reload storm adds a line here for you.

## Session records: .auric-live/

Auric Live keeps a small local record of each development session under `.auric-live/` in the workspace folder: sanitised request summaries and the page's performance summary. It never stores query strings, headers, bodies, cookies, IP addresses, user agents or storage values, and the folder is never served.

| Setting | Default | Range | Meaning |
| --- | --- | --- | --- |
| `auricLive.records.enabled` | `true` | — | Keep session records |
| `auricLive.records.maxRequests` | 200 | 20–5000 | Request summaries per session |
| `auricLive.records.maxSessionBytes` | 5242880 (about 5 MiB) | 65536–104857600 | Size of one session record; oldest summaries go first |
| `auricLive.records.maxSessions` | 12 | 1–100 | Recent sessions kept under `.auric-live/sessions/` |
| `auricLive.records.flushIntervalMs` | 1000 | 250–60000 | Minimum time between writes |
| `auricLive.records.telemetryIntervalMs` | 5000 | 1000–60000 | How often a served page sends its performance summary to the record |

**Auric Live: Open Recorded Live Session** opens `.auric-live/latest.json`. If nothing has been recorded yet, it says to start the server and open a served page first. Browser console messages are never added to session records.

You may want to add `.auric-live/` to your `.gitignore`.

## Multi-root workspaces

Each workspace folder has its own server, settings, project file and ignore file. Settings with resource scope (almost all Auric Live settings) can differ per folder. Unrelated configuration changes keep API routes, session settings and in-memory REST data.

When your configuration is in place, the **Servers** view shows a **Config file** row for the running server, and the settings apply every time you go live.
