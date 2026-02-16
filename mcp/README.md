# MCP Server (Read-only)

This folder contains a minimal Model Context Protocol (MCP) server that exposes
machine-readable profile resources from this repository.

## What it exposes

- `site://resume.json`
- `site://evidence.json`
- `site://availability.json`
- `site://capabilities.json`
- `site://engage.json`
- `site://agent-card.json`

## Supported methods

- `initialize`
- `ping`
- `resources/list`
- `resources/read`
- `tools/list` (returns empty)
- `prompts/list` (returns empty)

## Run locally

```bash
cd "/Users/vassiliylakhonin/Documents/New project/cv-site"
python3 mcp/server.py
```

The server uses stdio transport and returns data in JSON-RPC 2.0 envelopes.
