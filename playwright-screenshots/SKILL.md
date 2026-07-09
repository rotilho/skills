---
name: "playwright-screenshots"
version: "1.0.0"
description: "Use when a task needs browser screenshots, visual verification, page smoke tests, or headless browser capture after browsermcp is unavailable or unnecessary. Prefer Playwright for localhost, static files, generated pages, and unauthenticated pages; note when a live user browser session is required instead."
license: "MIT"
compatibility: "codex"
metadata:
  audience: "agent"
  workflow: "browser-verification"
---

# Playwright Screenshots

## When to use

Use this skill when the user asks to:
- take or verify a screenshot of a webpage or local app
- check a UI visually without relying on browsermcp
- run a headless browser smoke test
- confirm that Playwright can open a page, render it, and save an image

Do not use this skill when the task requires the user's already-open browser state, Chrome extensions, active tabs, or existing logged-in cookies. In that case, say that a browser bridge or exported auth state is required.

## Core promise

Prove screenshot capability with a real browser launch and a generated image, not just a successful package install.

## Workflow

1. Check basic tooling:

```bash
node --version
npm --version
npx --yes playwright --version
```

2. If Playwright runs but the browser is missing, install the needed browser:

```bash
npx --yes playwright install chromium
```

3. Take a smoke-test screenshot before relying on the workflow:

```bash
npx --yes playwright screenshot "data:text/html,%3Ch1%3EPlaywright%20screenshot%20works%3C%2Fh1%3E" /tmp/playwright-smoke.png
file /tmp/playwright-smoke.png
```

4. Inspect the image with the available local image viewer when possible.

5. For project pages, prefer a local URL from the running dev server:

```bash
npx --yes playwright screenshot http://127.0.0.1:8080 /tmp/page.png
```

6. If the page needs waiting, viewport size, or full-page capture, use CLI options:

```bash
npx --yes playwright screenshot --wait-for-timeout=1000 --viewport-size=390,844 --full-page http://127.0.0.1:8080 /tmp/mobile-full-page.png
```

## Constraints

- `npx` may need network access to fetch Playwright.
- `npx playwright install chromium` downloads browser binaries into the Playwright cache.
- Playwright controls a separate browser context; it does not automatically share the user's Chrome session.
- For authenticated apps, use app test credentials, a persistent browser profile, or exported Playwright storage state.
- Keep screenshots in `/tmp` unless the user asks for repo artifacts.

## Verification checklist

Before saying Playwright works, confirm:
- `npx --yes playwright --version` succeeds
- a browser binary is installed or launched successfully
- a screenshot command exits 0
- the output file is a valid non-empty PNG
- the image was inspected when visual correctness matters
