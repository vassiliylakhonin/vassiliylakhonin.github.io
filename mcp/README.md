# MCP Server (Profile Resources for AI Agents)

This folder contains the MCP server for Vassiliy Lakhonin's profile/CV resources.
It exposes read-only profile, resume, evidence, availability, and case-study data
to MCP-compatible AI agents.

## Transport modes

- Local stdio (Claude Desktop / local MCP clients)
- HTTP/SSE (for cloud deployment on Railway, Render, Fly.io, etc.)

## What it exposes (tools)

- `get_profile`
- `get_resume`
- `get_availability`
- `get_capabilities`
- `get_evidence`
- `get_engage`
- `get_agent_card`
- `get_verification`
- `get_case_study(name)`
- `list_resources`
- `search_profile(query)`

## Data sources (live site)

The server fetches read-only resources from:

- `https://vassiliylakhonin.github.io/profile.md`
- `https://vassiliylakhonin.github.io/resume.json`
- `https://vassiliylakhonin.github.io/evidence.json`
- `https://vassiliylakhonin.github.io/availability.json`
- `https://vassiliylakhonin.github.io/capabilities.json`
- `https://vassiliylakhonin.github.io/engage.json`
- `https://vassiliylakhonin.github.io/agent-card.json`
- `https://vassiliylakhonin.github.io/verification.json`
- Markdown case studies (`case-study-*.md`)

## Install dependencies

```bash
cd /Users/vassiliylakhonin/Documents/cv-site/mcp
python3 -m pip install -r requirements.txt
```

## Run locally (stdio)

```bash
cd /Users/vassiliylakhonin/Documents/cv-site/mcp
python3 server.py
```

## Run locally (HTTP/SSE)

```bash
cd /Users/vassiliylakhonin/Documents/cv-site/mcp
PORT=8000 python3 server.py --http
```

Endpoints in HTTP mode:

- SSE: `http://localhost:8000/sse`
- Messages: `http://localhost:8000/messages/`
- Health: `http://localhost:8000/health`

## Deploy

See `DEPLOY.md` for cloud deployment instructions (Railway, Render, Fly.io).
