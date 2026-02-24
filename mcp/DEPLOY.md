# MCP Server — Cloud Deployment Guide

This guide covers deploying the read-only MCP server so AI agents can
reach it over the network (SSE transport), not just locally via stdio.

---

## Option A — Railway (recommended, free tier available)

1. **Install Railway CLI** (once):
   ```bash
   npm install -g @railway/cli
   railway login
   ```

2. **Add required files** to the `mcp/` folder:

   **`mcp/requirements.txt`**
   ```
   mcp[cli]>=1.0
   uvicorn>=0.29
   starlette>=0.36
   ```

   **`mcp/Procfile`**
   ```
   web: python server.py --http
   ```

   **`mcp/railway.toml`** (optional, sets start command explicitly)
   ```toml
   [deploy]
   startCommand = "python server.py --http"
   healthcheckPath = "/health"
   ```

3. **Deploy:**
   ```bash
   cd mcp/
   railway init          # create new project
   railway up            # deploy
   railway domain        # get your public URL
   ```

4. Railway automatically sets `$PORT` — the server reads it.

5. Your MCP endpoint will be:
   ```
   https://your-app.up.railway.app/sse
   ```

---

## Option B — Render.com (free tier, auto-sleep after 15 min)

1. Push the repo to GitHub (already done).

2. Go to [render.com](https://render.com) → **New Web Service** →
   connect your GitHub repo.

3. Settings:
   - **Root directory:** `mcp`
   - **Runtime:** Python 3
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python server.py --http`
   - **Environment variable:** *(none needed, Render sets PORT automatically)*

4. Your endpoint:
   ```
   https://your-app.onrender.com/sse
   ```

---

## Option C — Fly.io

1. Install flyctl, then from `mcp/` folder:
   ```bash
   fly launch --name vassiliy-lakhonin-mcp --no-deploy
   fly deploy
   ```

2. `fly.toml` is auto-generated; add health check:
   ```toml
   [[services.http_checks]]
   path = "/health"
   ```

---

## Connecting to Claude Desktop (local stdio — existing behaviour)

```json
{
  "mcpServers": {
    "vassiliy-lakhonin": {
      "command": "python3",
      "args": ["/path/to/mcp/server.py"]
    }
  }
}
```

## Connecting to Claude Desktop (remote HTTP/SSE)

```json
{
  "mcpServers": {
    "vassiliy-lakhonin": {
      "url": "https://your-app.up.railway.app/sse"
    }
  }
}
```

---

## Health check

Once deployed, verify with:
```bash
curl https://your-app.up.railway.app/health
# → {"status": "ok", "server": "vassiliy-lakhonin-profile"}
```

---

## Updating the README

Add this section to your main `README.md` after deploying:

```markdown
## MCP server (remote)

Connect any MCP-compatible AI agent directly to Vassiliy's profile data:

SSE endpoint: `https://your-app.up.railway.app/sse`

Available tools: `get_profile`, `get_resume`, `get_availability`,
`get_capabilities`, `get_evidence`, `get_case_study`, `search_profile`, and more.
```
