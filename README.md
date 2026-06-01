# Toolbox

A collection of handy utility tools, self-hosted at [fazz.uk](https://fazz.uk).

## Tools

**Images**
- **Image to Text** — OCR via Tesseract.js, runs locally in the browser

**Lists**
- **De-dupe List** — remove duplicate lines, preserve order, case-sensitive toggle
- **Compare Lists** — see what's in both, only in A, or only in B

**Text & Encoding**
- **Case Converter** — camelCase, snake_case, kebab-case, PascalCase, UPPER, Title Case, and more
- **Base64 Encode/Decode** — two-way, handles Unicode
- **URL Encode/Decode** — `encodeURIComponent` / `decodeURIComponent`

**Data**
- **JSON Formatter** — pretty-print, minify, syntax highlighting, validation
- **JWT Decoder** — decode header and payload, expiry check (signature not verified)
- **CSV ↔ JSON** — convert either direction, handles quoted fields, comma/semicolon/tab delimiters

**Dev Tools**
- **Epoch Converter** — Unix timestamp ↔ date, auto-detects seconds vs milliseconds
- **Number Base Converter** — decimal, binary, octal, hex
- **Cron Explainer** — plain English breakdown of cron expressions
- **UUID Generator** — bulk v4 UUIDs, multiple format options
- **Regex Tester** — live match highlighting, match table with capture groups

## Running locally

```bash
docker compose up --build
```

App runs at `http://localhost:5002`.

## Tech

Flask + Gunicorn, Bootstrap 5, all tool logic in client-side JavaScript.
