---
title: Auric Artisan Live — reference
description: Every Auric Artisan Live command, keyboard shortcut, menu entry, view and setting, with types, defaults and ranges.
product: VS Code extensions › Auric Artisan Live
updated: 2026-09-25
---

# Reference: commands, keys and settings

This page lists everything Auric Artisan Live 0.2.1 contributes to VS Code: 54 commands, 7 keyboard shortcuts, 3 sidebar views and 103 settings. Command titles appear in the Command Palette with the **Auric Live:** prefix.

## Commands

| Command | ID | Keys | What it does |
| --- | --- | --- | --- |
| **Auric Live: Select Active Server** | `auricLive.selectServer` | — | Choose which workspace folder's server the panel and commands act on |
| **Auric Live: Toggle Browser Console Capture** | `auricLive.toggleConsole` | — | Turn browser console capture on or off for this session |
| **Auric Live: Use HTTPS Certificate and Key** | `auricLive.configureCertificate` | — | Import and validate a PEM certificate and matching private key, then turn HTTPS on |
| **Auric Live: Diagnose Project and Runtime** | `auricLive.diagnose` | — | Open a local report on configuration, run targets and prerequisites, with credentials redacted |
| **Auric Live: Go Live** | `auricLive.goLive` | `Ctrl` + `Alt` + `L` (macOS `Cmd` + `Alt` + `L`) | Start serving the workspace folder, or reopen a server that is already running |
| **Auric Live: Stop Server** | `auricLive.stop` | — | Stop the active server |
| **Auric Live: Stop All Servers** | `auricLive.stopAll` | `Ctrl` + `Alt` + `Shift` + `L` (macOS `Cmd` + `Alt` + `Shift` + `L`) | Stop every Auric Live server |
| **Auric Live: Restart Server** | `auricLive.restart` | — | Restart the active server |
| **Auric Live: Serve This Folder** | `auricLive.startHere` | — | Serve the folder you right-clicked (Explorer only); not in the Command Palette |
| **Auric Live: Open with Auric Live** | `auricLive.openWithLive` | — | Start the server if needed and open this file's address |
| **Auric Live: Open in Default Browser** | `auricLive.openInBrowser` | — | Open the server's address in your default browser |
| **Auric Live: Open Preview Beside** | `auricLive.openPreview` | `Ctrl` + `Alt` + `K` (macOS `Cmd` + `Alt` + `K`) | Open the preview beside the editor |
| **Auric Live: Copy Local URL** | `auricLive.copyUrl` | — | Copy the localhost address |
| **Auric Live: Copy Network URL** | `auricLive.copyNetworkUrl` | — | Copy an address other devices on your network can use |
| **Auric Live: Show Phone QR Code** | `auricLive.showQrCode` | — | Show a locally generated QR code for opening the site on a phone |
| **Auric Live: Open Control Panel** | `auricLive.openControlPanel` | `Ctrl` + `Alt` + `Shift` + `I` (macOS `Cmd` + `Alt` + `Shift` + `I`) | Open the Auric Live control panel |
| **Auric Live: Open Request Inspector** | `auricLive.openInspector` | — | Open the control panel at its Requests section |
| **Auric Live: Clear Request Log** | `auricLive.clearRequests` | — | Empty the request inspector |
| **Auric Live: Export Requests as HAR** | `auricLive.exportHar` | — | Save captured requests as a HAR file |
| **Auric Live: Copy Request as curl** | `auricLive.copyAsCurl` | — | Copy a captured request as a curl command (Requests view); not in the Command Palette |
| **Auric Live: Copy Request as fetch** | `auricLive.copyAsFetch` | — | Copy a captured request as a fetch() call (Requests view); not in the Command Palette |
| **Auric Live: Replay Request** | `auricLive.replayRequest` | — | Send a captured request again (Requests view); not in the Command Palette |
| **Auric Live: Show Request Detail** | `auricLive.showRequestDetail` | — | Show a captured request's details (Requests view); not in the Command Palette |
| **Auric Live: Create Project Config File** | `auricLive.createConfigFile` | — | Write a starter auric.live.json and open it |
| **Auric Live: Open Project Config File** | `auricLive.openConfigFile` | — | Open auric.live.json, or offer to create it |
| **Auric Live: Open .auricignore-live** | `auricLive.openIgnoreFile` | — | Open .auricignore-live, creating a starter if needed |
| **Auric Live: Open Recorded Live Session** | `auricLive.openRuntimeRecords` | — | Open the latest session record, .auric-live/latest.json |
| **Auric Live: Reload Configuration** | `auricLive.reloadConfig` | — | Re-read settings and the project file |
| **Auric Live: Change Port…** | `auricLive.changePort` | — | Set the port for this session (0 chooses a free one) |
| **Auric Live: Change Served Folder…** | `auricLive.setRoot` | — | Pick the folder to serve for this session |
| **Auric Live: Toggle Live Reload** | `auricLive.toggleLiveReload` | — | Turn live reload on or off for this session |
| **Auric Live: Toggle Mock API** | `auricLive.toggleMocks` | — | Turn mock answering on or off for this session |
| **Auric Live: Toggle HTTPS** | `auricLive.toggleHttps` | — | Turn HTTPS on (with a generated certificate) or off for this session |
| **Auric Live: Simulate Network Profile…** | `auricLive.setThrottle` | — | Choose a network profile for this session |
| **Auric Live: Reveal Development Certificate** | `auricLive.revealCertificate` | — | Show the generated certificate file in your file manager |
| **Auric Live: Open Settings** | `auricLive.openSettings` | — | Open the Settings editor filtered to Auric Live |
| **Auric Live: Show Log** | `auricLive.showLog` | — | Show the Auric Artisan Live output channel |
| **Auric Live: Reload Connected Pages** | `auricLive.reloadBrowsers` | `Ctrl` + `Alt` + `U` (macOS `Cmd` + `Alt` + `U`) | Reload every connected page now |
| **Auric Live: Resume Live Reload** | `auricLive.resumeLiveReload` | — | Resume live reload after reload-storm protection paused it |
| **Auric Live: Start Framework Dev Server…** | `auricLive.startDevServer` | — | Detect the framework dev server, start it and forward to it; trusted workspaces only |
| **Auric Live: Stop Framework Dev Server** | `auricLive.stopDevServer` | — | Stop the dev server and remove the forwarding it added; trusted workspaces only |
| **Auric Live: Restart Framework Dev Server** | `auricLive.restartDevServer` | — | Restart the dev server or run target; trusted workspaces only |
| **Auric Live: Show Dev Server Output** | `auricLive.showDevServerLog` | — | Show the run target's output |
| **Auric Live: Find a Running Backend** | `auricLive.detectBackendPort` | — | Scan common ports for a running backend and offer to forward to it |
| **Auric Live: Select Run Target…** | `auricLive.selectRunTarget` | `Ctrl` + `Alt` + `J` (macOS `Cmd` + `Alt` + `J`) | Choose what serves the site: static files, a detected runtime or your own command |
| **Auric Live: Add Custom Run Command…** | `auricLive.addRunProfile` | — | Save a command (with any leading environment variables) as a run target |
| **Auric Live: Edit Saved Run Commands** | `auricLive.editRunProfiles` | — | Open the auricLive.runProfiles setting |
| **Auric Live: Show Detected Run Targets** | `auricLive.showRunTargets` | — | List every run target for the folder, with the reason for each, in the log |
| **Auric Live: Add API Proxy Route…** | `auricLive.addProxyRoute` | — | Forward a path prefix to a backend for this session |
| **Auric Live: Add Mock API Route…** | `auricLive.addMockRoute` | — | Answer a method and path with a JSON body for this session |
| **Auric Live: Open Mock Database** | `auricLive.openMockDatabase` | — | Open the REST database file, or create a sample |
| **Auric Live: Refresh** | `auricLive.refresh` | — | Refresh the Servers view (view menu only); not in the Command Palette |
| **Auric Live: Open Live Menu** | `auricLive.openMenu` | `Ctrl` + `Alt` + `Shift` + `K` (macOS `Cmd` + `Alt` + `Shift` + `K`) | Open the Auric Live quick menu |
| **Auric Live: Focus Auric Live** | `auricLive.focus` | — | Show the Auric Live sidebar |

Commands marked "not in the Command Palette" run from the context menus of the **Servers** and **Requests** views, the Explorer or a view's title bar. Most other commands appear in the Command Palette only when a folder is open; **Open with Auric Live** appears when an editor is open.

## Keyboard shortcuts

All seven shortcuts work whenever a folder is open. On macOS, `Cmd` replaces `Ctrl`.

| Keys (Windows and Linux) | Keys (macOS) | Command |
| --- | --- | --- |
| `Ctrl` + `Alt` + `L` | `Cmd` + `Alt` + `L` | **Go Live** |
| `Ctrl` + `Alt` + `Shift` + `L` | `Cmd` + `Alt` + `Shift` + `L` | **Stop All Servers** |
| `Ctrl` + `Alt` + `K` | `Cmd` + `Alt` + `K` | **Open Preview Beside** |
| `Ctrl` + `Alt` + `Shift` + `K` | `Cmd` + `Alt` + `Shift` + `K` | **Open Live Menu** |
| `Ctrl` + `Alt` + `J` | `Cmd` + `Alt` + `J` | **Select Run Target…** |
| `Ctrl` + `Alt` + `U` | `Cmd` + `Alt` + `U` | **Reload Connected Pages** |
| `Ctrl` + `Alt` + `Shift` + `I` | `Cmd` + `Alt` + `Shift` + `I` | **Open Control Panel** |

Inside other surfaces:

| Where | Keys | What they do |
| --- | --- | --- |
| A served page | `Alt` + `Shift` + `D` (set by `auricLive.dashboard.shortcut`) | Open the in-page dashboard |
| Control panel, Requests section | `Ctrl` + `F` (`Cmd` + `F` on macOS) | Focus the request search |
| Control panel | `Escape` | Close request details or an open menu |
| Dashboard tabs | Arrow keys, `Home`, `End` | Move between tabs |
| Dashboard content | Arrow keys, `Page Up`, `Page Down`, `Home`, `End`, `Space`, `Shift` + `Space` | Scroll |

## Where commands appear

- Status bar: **Go Live** when stopped; the port (opens the Live menu) when running
- **Servers** view title: **Go Live**, **Select Run Target…**, **Stop All Servers**, **Open Control Panel**; **…** menu: **Refresh**, **Open Settings**, **Show Log**
- A running server in **Servers**: Inline: **Open in Default Browser**, **Stop Server**. Right-click: **Restart Server**, **Open Preview Beside**, **Copy Local URL**, **Copy Network URL**, **Show Phone QR Code**
- A stopped server in **Servers**: Inline: **Go Live**
- **Requests** view title: **Clear Request Log**, **Export Requests as HAR**
- A request in **Requests**: Inline: **Show Request Detail**. Right-click: **Replay Request**, **Copy Request as curl**, **Copy Request as fetch**
- **Routes and Mocks** view title: **Add API Proxy Route…**, **Add Mock API Route…**, **Find a Running Backend**; **…** menu: **Open Mock Database**, **Open Project Config File**, **Restart Framework Dev Server**, **Show Dev Server Output**
- Explorer, on a folder: **Serve This Folder**, and the **Auric Live** submenu
- Explorer, on `.html`, `.htm`, `.php`, `.xhtml` or `.md`: **Open with Auric Live**
- Editor and editor tab, for `.html`, `.htm`, `.php` or `.xhtml`: **Open with Auric Live**
- Editor title **Run** menu › **Auric Live**: **Go Live**, **Select Run Target…**, **Add Custom Run Command…**, **Open Preview Beside**, **Open in Default Browser**, **Show Phone QR Code**, **Restart Framework Dev Server**, **Stop Server**, **Open Live Menu**

### The Auric Live menu

**Open Live Menu** lists, when a server is running: **Open in browser**, **Open preview beside**, **Show phone QR code**, **Reload connected pages**, **Open control panel**, **Restart server** and **Stop server**. When stopped: **Go Live** and **Open control panel**. Then always: **Add an API proxy route**, **Add a mock API route**, **Open the mock database**, **Change the run target…**, **Add a custom command…**, the run target's **Restart the run target**, **Show its output** and **Stop it** (or **Start the framework dev server** when none is running), **Find a backend that is already running**, **Simulate a network profile**, **Select active server**, **Toggle browser console capture**, **Diagnose configuration and runtimes**, **Import an HTTPS certificate**, **Toggle HTTPS**, **Toggle live reload**, **Change the port**, **Change the served folder**, **Open the project config file**, **Open .auricignore-live**, **Open recorded session**, **Export requests as HAR**, **Open settings** and **Show log**. Each shows its current value where it has one.

## Views

| View | Where | Contents |
| --- | --- | --- |
| **Servers** | Auric Live sidebar | One entry per workspace folder; expand for root, run target, dev server, upstreams, addresses, live reload, requests, certificate and config file |
| **Requests** | Auric Live sidebar | Recent requests with status, handler and time |
| **Routes and Mocks** | Auric Live sidebar | Proxy rules, mock routes, REST collections and CGI handlers |
| Control panel | Editor tab | Overview, Requests, Runtime, Routing, Settings |
| **Auric Live Preview** | Editor tab beside the code | The served site at a chosen device size |

Output channels: **Auric Artisan Live** (server log) and **Auric Live: Run Target** (run target output).

## Settings

All 103 settings, grouped by area. A project file sets the same values with the names shown here minus the `auricLive.` prefix. "Values or range" lists the allowed values, or the minimum and maximum for numbers.

### Server and address

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.root` | string | empty |  | Folder to serve, relative to the workspace folder. Empty serves the workspace folder; use `dist` or `public` for a build output. |
| `auricLive.port` | number | `5500` | 0–65535 | Port to listen on. Set 0 to let the operating system pick a free one, which is useful when several projects run at once. |
| `auricLive.portStrategy` | string | `increment` | `increment`, `fail`, `random` | What to do when the chosen port is already in use. |
| `auricLive.host` | string | `0.0.0.0` |  | Address to bind. `0.0.0.0` also answers devices on your network (phone testing); `127.0.0.1` keeps it on this machine. |
| `auricLive.open` | string | `default` | `default`, `preview`, `none` | What to open once the server starts. |
| `auricLive.openPath` | string | empty |  | Path appended to the URL that is opened, for a site whose entry point is not the root — /docs/index.html, for example. |
| `auricLive.startOnOpen` | boolean | `false` |  | Start the server automatically when a folder is opened. |
| `auricLive.showStatusBar` | boolean | `true` |  | Show the Go Live control in the status bar. |
| `auricLive.suggestFrameworkSetup` | boolean | `true` |  | Once per folder, offer the matching setup when the project is a framework with its own dev server, or a PHP site. |
| `auricLive.configFile` | string | `auric.live.json` |  | Name of the project file, looked for in the workspace folder, then `.auric/`. It overrides these settings. |
| `auricLive.interfaceLanguage` | string | `auto` | `auto`, `en`, `hi` | Language of the Auric Live panel and supported messages. `auto` follows VS Code. Changing it does not restart servers. |

### HTTPS

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.https.enabled` | boolean | `false` |  | Serve over HTTPS, which service workers, clipboard, camera, microphone and geolocation need on a phone. |
| `auricLive.https.certPath` | string | empty |  | Certificate file. Empty generates and reuses a self-signed one for `localhost` and your network addresses. |
| `auricLive.https.keyPath` | string | empty |  | Private key matching `auricLive.https.certPath`. |

### Static files and responses

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.index` | array | `["index.html","index.htm"]` |  | File names tried, in order, when a directory is requested. |
| `auricLive.directoryListing` | boolean | `true` |  | Render a browsable index for a directory that has no index file. |
| `auricLive.cleanUrls` | boolean | `false` |  | Serve /about from about.html, so links can drop the extension the way most static hosts do. |
| `auricLive.dotfiles` | string | `ignore` | `ignore`, `allow`, `deny` | How paths with a dot-file or dot-folder are treated. The default hides them, keeping `.env` and `.git` unserved. |
| `auricLive.notFoundPage` | string | empty |  | Page served for a missing file, relative to the served root. Leave empty for the built-in 404. |
| `auricLive.spa.enabled` | boolean | `false` |  | Answer unknown paths with the fallback document, so a client-side router keeps working on a deep link and a hard refresh. |
| `auricLive.spa.fallback` | string | `/index.html` |  | Document served for unknown paths when the single-page fallback is on. |
| `auricLive.spa.ignore` | array | `["/api/**","**/*.*"]` |  | Paths the fallback must not answer. The default keeps `/api` and anything with a file extension returning honest 404s. |
| `auricLive.compression` | string | `auto` | `auto`, `gzip`, `brotli`, `off` | Compression for text responses over one kilobyte. Turn it off when measuring uncompressed transfer sizes. |
| `auricLive.cache` | string | `no-store` | `no-store`, `no-cache`, `short`, `immutable-assets` | Caching policy sent with served files. |
| `auricLive.etag` | boolean | `true` |  | Send a validator so an unchanged file can answer 304 instead of being sent again. |
| `auricLive.mimeTypes` | object | `{}` |  | Extra content types, keyed by extension — `{ ".data": "application/json" }`. Overrides the built-in table. |
| `auricLive.headers` | array | `[]` |  | Extra response headers, applied to the paths each rule matches. |

### Cross-origin and access

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.cors.enabled` | boolean | `true` |  | Answer cross-origin requests, so a page served from another port can call this one during development. |
| `auricLive.cors.origin` | string | `*` |  | Origin allowed by the CORS headers. Use a specific origin when credentials are involved. |
| `auricLive.cors.credentials` | boolean | `false` |  | Allow cookies and authorization headers on cross-origin requests. |
| `auricLive.crossOriginIsolation` | boolean | `false` |  | Send COOP and COEP headers, needed for `SharedArrayBuffer`, WebAssembly threads and precise timers. |
| `auricLive.auth.enabled` | boolean | `false` |  | Require a username and password before anything is served. Useful when bound to a shared network. |
| `auricLive.auth.username` | string | empty |  | Username for basic authentication. |
| `auricLive.auth.password` | string | empty |  | Password for basic authentication. Stored in plain settings; a development convenience, not a secret store. |

### Request limits

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.maxRequestBodyBytes` | number | `8388608` | 0–1073741824 | Maximum buffered request size in bytes. Larger bodies receive HTTP 413. Zero rejects all non-empty bodies. |
| `auricLive.requestBodyTimeoutMs` | number | `30000` | 0–3600000 | Deadline for receiving a request body; 0 disables it. Simulated transfer time is excluded. |

### Network simulation

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.throttle.profile` | string | `off` | `off`, `slow-3g`, `3g`, `4g`, `cable`, `custom` | Simulate a slower network for every client, including a phone on your LAN where browser devtools are not available. |
| `auricLive.throttle.latencyMs` | number | `0` | 0–60000 | Delay added before each response when the custom profile is selected. |
| `auricLive.throttle.downloadKbps` | number | `0` | 0–no maximum | Download ceiling in kilobits per second when the custom profile is selected. 0 means unlimited. |
| `auricLive.throttle.uploadKbps` | number | `0` | 0–1000000 | Upload bandwidth in kilobits per second; 0 uses unlimited bandwidth. |

### Live reload and watching

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.liveReload.enabled` | boolean | `true` |  | Inject the reload client into served HTML and update open pages when the configured save/change trigger fires. |
| `auricLive.liveReload.reloadOnSave` | string | `save` | `save`, `change`, `off` | What may refresh the page: `save` (explicit VS Code saves), `change` (any file change) or `off` (manual only). |
| `auricLive.liveReload.injectTo` | string | `body` | `body`, `head` | Where the reload client is inserted: end of `body` (out of the critical path) or `head` (earlier). |
| `auricLive.liveReload.cssHotSwap` | boolean | `true` |  | Swap a changed stylesheet in place, keeping scroll position, open dialogs and filled forms. |
| `auricLive.liveReload.imageHotSwap` | boolean | `true` |  | Refresh a changed image in place instead of reloading the page. |
| `auricLive.liveReload.preserveScroll` | boolean | `true` |  | Restore scroll position and open disclosure elements after a full reload. |
| `auricLive.liveReload.overlay` | boolean | `true` |  | Show an overlay in the page when a proxied request or a CGI handler fails, instead of leaving the failure in the log. |
| `auricLive.liveReload.ignore` | array | see "Default reload exclusions" |  | Paths that never trigger a reload. Dot-paths such as `.next/`, `.vite/` and `.git/` are always excluded as well. |
| `auricLive.liveReload.stormLimit` | number | `3` | 2–200 | Reloads allowed within the storm window before Auric Live stops reloading and reports the files responsible. |
| `auricLive.liveReload.stormWindowMs` | number | `10000` | 1000–120000 | The window the reload limit is measured over. |
| `auricLive.liveReload.debounceMs` | number | `350` | 0–5000 | Quiet period after the last file change before pages are told, so a multi-file build causes one update. |
| `auricLive.watch.enabled` | boolean | `true` |  | Watch the served folder for changes. Turning this off leaves live reload to the Reload Connected Pages command. |
| `auricLive.watch.pollIntervalMs` | number | `0` | 0–60000 | Poll for changes at this interval instead of file system events (for network shares and VMs). `0` uses events. |

### Browser dashboard and console

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.dashboard.enabled` | boolean | `true` |  | Inject the in-page developer dashboard with live health, performance, cache, network, storage and server diagnostics. |
| `auricLive.dashboard.independent` | boolean | `false` |  | Inject the dashboard even when Auric live reload is off. Framework run targets turn this on. |
| `auricLive.dashboard.shortcut` | string | `Alt+Shift+D` |  | Keys inside a served page that open the dashboard, joined with `+`, for example `Alt+Shift+D`. |
| `auricLive.dashboard.customCursor` | boolean | `true` |  | Show the Auric pointer on served pages. Touch, coarse-pointer and forced-colour setups keep the native cursor. |
| `auricLive.dashboard.sampleIntervalMs` | number | `1000` | 500–10000 | How often an open dashboard asks for server state, in milliseconds. |
| `auricLive.console.enabled` | boolean | `false` |  | Capture browser console messages into the dashboard and the extension log, redacted and rate-limited. |
| `auricLive.console.levels` | array | `["error","warn","info","log","debug"]` |  | Console levels to capture. |
| `auricLive.console.maxEntries` | number | `200` | 20–2000 | Maximum console entries retained in each page. |
| `auricLive.console.maxMessageLength` | number | `2000` | 100–10000 | Maximum characters captured from one console call. |
| `auricLive.console.rateLimit` | number | `20` | 1–100 | Maximum console messages sent per second from each page. |

### Session records

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.records.enabled` | boolean | `true` |  | Keep a bounded local session record under `.auric-live/`. It never stores queries, headers, bodies or cookies. |
| `auricLive.records.maxRequests` | number | `200` | 20–5000 | Maximum sanitized request summaries retained in one recorded session. |
| `auricLive.records.maxSessionBytes` | number | `5242880` | 65536–104857600 | Maximum approximate size in bytes of one `.auric-live` session snapshot. Older request summaries are removed first. |
| `auricLive.records.maxSessions` | number | `12` | 1–100 | Number of recent recorded sessions retained under `.auric-live/sessions/`. |
| `auricLive.records.flushIntervalMs` | number | `1000` | 250–60000 | Minimum interval between atomic diagnostic snapshot writes. |
| `auricLive.records.telemetryIntervalMs` | number | `5000` | 1000–60000 | How often a served page sends its bounded performance summary to the local session record. |

### Proxy and backend readiness

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.proxy` | array | `[]` |  | Paths forwarded to another server, so the page and its API share one origin. Each rule has a `path` and a `target`. |
| `auricLive.upstream.wait` | boolean | `true` |  | Hold a request while a proxied backend is still starting, instead of answering 502 at once. |
| `auricLive.upstream.waitTimeoutMs` | number | `25000` | 0–600000 | How long a request waits for the backend before the waiting page is shown; that page reloads until it answers. |
| `auricLive.upstream.pollIntervalMs` | number | `400` | 50–10000 | How often a backend that is not answering is checked. Once it is up, checks drop to one every few seconds. |
| `auricLive.upstream.reloadOnRecover` | boolean | `true` |  | Reload every connected page when a backend comes back. |
| `auricLive.upstream.autoDetectPort` | boolean | `true` |  | Adopt the port a supervised dev server prints when it differs from the configured one. |
| `auricLive.upstream.candidatePorts` | array | `[]` |  | Ports searched by Find a Running Backend. Leave empty to use the built-in list of ports these tools normally choose. |

### Run targets and dev servers

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.runProfiles` | array | `[]` |  | Named ways to run the project, shown in the run-target list. Environment assignments before a command are read. |
| `auricLive.devServer.autoStart` | boolean | `false` |  | Start the detected framework dev server automatically when Go Live runs on a project that has one, instead of offering it. |
| `auricLive.devServer.autoRestart` | boolean | `true` |  | Restart a supervised dev server when it exits unexpectedly, with a growing delay between attempts. |
| `auricLive.devServer.maxRestarts` | number | `5` | 0–50 | How many times a dev server may be restarted before Auric Live stops and reports it. |
| `auricLive.devServer.command` | string | empty |  | Command used to start the dev server. Leave empty to use the one detected from the project, such as npm run dev. |
| `auricLive.devServer.useTerminal` | boolean | `false` |  | Run the dev server in a VS Code terminal. Allows typed input, but loses port adoption and restart supervision. |
| `auricLive.autoRestart.onConfigChange` | boolean | `true` |  | Apply setting and project-file changes to a running server. Only port, host, root, mount or TLS changes rebind it. |
| `auricLive.autoRestart.reloadBrowsers` | boolean | `true` |  | Reload connected pages after a configuration change is applied. |

### Mock API and REST database

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.mock.enabled` | boolean | `false` |  | Answer the declared mock routes. They are matched before the proxy, so one endpoint can be overridden. |
| `auricLive.mock.routes` | array | `[]` |  | Endpoints answered by the server itself. Bodies can use placeholders such as `{{params.id}}` and `{{uuid}}`. |
| `auricLive.mock.delayMs` | number | `0` | 0–60000 | Latency applied to every mock and REST response, on top of any per-route delay. |
| `auricLive.mock.rest.enabled` | boolean | `false` |  | Serve a full REST backend from a JSON file, with filtering, sorting, pagination and relationships. |
| `auricLive.mock.rest.base` | string | `/api` |  | Prefix the REST collections are mounted under. Other paths fall through to the proxy, then to static files. |
| `auricLive.mock.rest.database` | string | `db.json` |  | JSON file holding the collections, relative to the served root, shaped like `{ "users": [ … ] }`. |
| `auricLive.mock.rest.persist` | boolean | `false` |  | Write changes back to the database file. Off by default so a restart returns to a known fixture. |

### PHP and CGI

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.cgi.enabled` | boolean | `false` |  | Run matching files through a CGI handler instead of serving them as downloads. With `php-cgi`, PHP sites run. |
| `auricLive.cgi.handlers` | object | `{".php":"php-cgi"}` |  | Handler command per extension, such as `{ ".php": "php-cgi" }`. It must be on your PATH or a full path. |
| `auricLive.cgi.indexes` | array | `["index.php"]` |  | Additional index file names tried for a directory when CGI is enabled. |

### Request inspector

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.inspector.enabled` | boolean | `true` |  | Record requests so the Requests view shows which rule answered each one. |
| `auricLive.inspector.maxEntries` | number | `500` | 20–10000 | How many requests are kept before the oldest are dropped. |
| `auricLive.inspector.captureBodies` | boolean | `true` |  | Keep request and response bodies for inspection and HAR export. Credential headers are always masked. |
| `auricLive.inspector.maxBodyBytes` | number | `262144` | 0–8388608 | Maximum bytes captured per request or response body. |
| `auricLive.inspector.redactSensitive` | boolean | `true` |  | Redact common credential fields in captured query strings and JSON/form bodies. Credential headers are always redacted. |
| `auricLive.inspector.sensitiveFields` | array | `[]` |  | Additional field and header names to redact, case insensitive. |
| `auricLive.inspector.harIncludeBodies` | boolean | `false` |  | Include captured bodies in HAR exports. Disabled by default because arbitrary application data can be sensitive. |

### Logging

| Setting | Type | Default | Values or range | What it does |
| --- | --- | --- | --- | --- |
| `auricLive.logLevel` | string | `info` | `off`, `error`, `warn`, `info`, `debug` | How much detail reaches the Auric Artisan Live output channel. Credential-like values are masked. |
| `auricLive.requestLogging` | boolean | `true` |  | Write one line per request to the output channel, at debug level for successes and higher for failures. |

### Default reload exclusions

The default value of `auricLive.liveReload.ignore`:

```json
[
  "**/node_modules/**", "**/dist/**", "**/out/**", "**/build/**", "**/coverage/**",
  "**/target/**", "**/vendor/**", "**/bin/**", "**/obj/**", "**/__pycache__/**",
  "**/venv/**", "**/tmp/**", "**/temp/**", "**/*.log", "**/*.tmp", "**/*.temp",
  "**/*.swp", "**/*.swx", "**/*~", "**/*.pyc", "**/*.class", "**/*.o", "**/*.obj",
  "**/*.pdb", "**/*.crdownload", "**/*.partial", "**/*-journal", "**/*.sqlite*",
  "**/~$*", "**/.~lock.*", "**/Thumbs.db", "**/desktop.ini", "**/.DS_Store"
]
```

### Enumerated values explained

| Setting | Value | Meaning |
| --- | --- | --- |
| `auricLive.portStrategy` | `increment` | Walk upward from the chosen port until one is free |
| `auricLive.portStrategy` | `fail` | Report the conflict instead of moving |
| `auricLive.portStrategy` | `random` | Choose a free port between 20000 and 40000 |
| `auricLive.open` | `default` | Open the default browser when the server starts |
| `auricLive.open` | `preview` | Open the preview beside the editor |
| `auricLive.open` | `none` | Open nothing |
| `auricLive.dotfiles` | `ignore`, `allow`, `deny` | Hide, serve or refuse paths with a dot-file or dot-folder |
| `auricLive.cache` | `no-store` | Never cache, so a stale file never survives a reload |
| `auricLive.cache` | `no-cache` | Keep a copy but check it on every request |
| `auricLive.cache` | `short` | A short freshness window, for measuring repeat visits |
| `auricLive.cache` | `immutable-assets` | Fonts and images immutable for a year; everything else uncached |
| `auricLive.throttle.profile` | `off`, `slow-3g`, `3g`, `4g`, `cable`, `custom` | See [Simulate a slow network](network-simulation.md) |
| `auricLive.liveReload.reloadOnSave` | `save` | Reload once per explicit VS Code save |
| `auricLive.liveReload.reloadOnSave` | `change` | Watch the whole served folder |
| `auricLive.liveReload.reloadOnSave` | `off` | Never reload automatically |
| `auricLive.liveReload.injectTo` | `body`, `head` | Where the reload script is inserted |
| `auricLive.logLevel` | `off`, `error`, `warn`, `info`, `debug` | Detail written to the output channel |
| `auricLive.interfaceLanguage` | `auto`, `en`, `hi` | Follow VS Code, English, or Hindi |

### Settings restricted in untrusted workspaces

`auricLive.cgi.enabled`, `auricLive.cgi.handlers`, `auricLive.cgi.indexes`, `auricLive.proxy`, `auricLive.host`, `auricLive.auth.username`, `auricLive.auth.password`, `auricLive.https.certPath`, `auricLive.https.keyPath` and `auricLive.mock.rest.persist` are ignored until you trust the workspace, whether they come from settings or the project file.

### Setting scope

Most settings have **resource** scope, so each folder of a multi-root workspace can differ. `auricLive.showStatusBar`, `auricLive.etag`, `auricLive.inspector.enabled`, `auricLive.inspector.maxEntries`, `auricLive.inspector.captureBodies`, `auricLive.logLevel`, `auricLive.requestLogging` and `auricLive.interfaceLanguage` have **window** scope: they can be set for the user or the workspace, but not per folder.

## Files Auric Live reads and writes

| File | Written by | Purpose |
| --- | --- | --- |
| `auric.live.json` (or the name in `auricLive.configFile`), in the workspace folder or `.auric/` | You, **Create Project Config File** or **Save to config file** | Project configuration |
| `.auricignore-live`, in the served folder | You, **Open .auricignore-live** or **Ignore *folder*/** | Paths never served, watched or recorded |
| `.auric-live/latest.json` and `.auric-live/sessions/` | Auric Live | Local session records |
| `db.json` (or `auricLive.mock.rest.database`) | You, or **Open Mock Database** › **Create** | REST database; written back only with `mock.rest.persist` |
| A `.har` file | **Export Requests as HAR** | Request export |
| Generated certificate | Auric Live, in its own extension storage | Self-signed HTTPS certificate |
| Workspace settings | **Add Custom Run Command…** | Saves `auricLive.runProfiles` |
