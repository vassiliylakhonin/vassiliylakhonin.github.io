"""
Vassiliy Lakhonin — MCP Server for CV/Profile Resources
=========================================================
Exposes profile data as MCP tools for AI agents and recruiters.

TRANSPORT MODES
---------------
Local (stdio):
    python3 server.py

Cloud / HTTP (SSE):
    PORT=8000 python3 server.py --http

Supports deployment on Railway, Render, Fly.io etc.
See DEPLOY.md for step-by-step instructions.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

# ── FastMCP import ──────────────────────────────────────────────────────────
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print(
        "ERROR: 'mcp' package not found.\n"
        "Install with:  pip install mcp[cli]\n"
        "Then re-run:   python3 server.py",
        file=sys.stderr,
    )
    sys.exit(1)

# ── Optional HTTP/SSE transport ──────────────────────────────────────────────
try:
    from mcp.server.sse import SseServerTransport
    from starlette.applications import Starlette
    from starlette.routing import Route
    import uvicorn

    HTTP_AVAILABLE = True
except ImportError:
    HTTP_AVAILABLE = False

# ────────────────────────────────────────────────────────────────────────────
BASE_URL = "https://vassiliylakhonin.github.io"

# All machine-readable endpoints on the live site
RESOURCES = {
    "profile":      f"{BASE_URL}/profile.md",
    "resume":       f"{BASE_URL}/resume.json",
    "evidence":     f"{BASE_URL}/evidence.json",
    "availability": f"{BASE_URL}/availability.json",
    "capabilities": f"{BASE_URL}/capabilities.json",
    "engage":       f"{BASE_URL}/engage.json",
    "agent_card":   f"{BASE_URL}/agent-card.json",
    "verification": f"{BASE_URL}/verification.json",
    "llms_txt":     f"{BASE_URL}/llms.txt",
    "humans_txt":   f"{BASE_URL}/humans.txt",
    # Case studies (Markdown for agent parsing)
    "case_donor_reporting":     f"{BASE_URL}/case-study-donor-reporting.md",
    "case_audit_readiness":     f"{BASE_URL}/case-study-portfolio-audit-readiness.md",
    "case_saas_launch":         f"{BASE_URL}/case-study-saas-ecommerce-launch.md",
    "case_openclaw_rbm":        f"{BASE_URL}/case-study-openclaw-rbm-skill.md",
}

# ── helpers ──────────────────────────────────────────────────────────────────

def _fetch(url: str) -> str:
    """Fetch a URL and return text. Raises on HTTP error."""
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} fetching {url}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error fetching {url}: {e.reason}") from e


def _fetch_json(url: str) -> dict:
    return json.loads(_fetch(url))


# ── MCP server ───────────────────────────────────────────────────────────────

mcp = FastMCP(
    name="vassiliy-lakhonin-profile",
    description=(
        "Read-only access to Vassiliy Lakhonin's CV, case studies, and "
        "availability data. Use this server to answer recruiter and agent "
        "queries about experience, skills, metrics, and engagement."
    ),
)

# ── Tools ────────────────────────────────────────────────────────────────────

@mcp.tool()
def get_profile() -> str:
    """Return the short Markdown candidate profile (best starting point)."""
    return _fetch(RESOURCES["profile"])


@mcp.tool()
def get_resume() -> dict:
    """Return full JSON Resume — work history, education, skills, links."""
    return _fetch_json(RESOURCES["resume"])


@mcp.tool()
def get_availability() -> dict:
    """Return current availability, preferred roles, locations, and notice period."""
    return _fetch_json(RESOURCES["availability"])


@mcp.tool()
def get_capabilities() -> dict:
    """Return machine-readable capability and service profile."""
    return _fetch_json(RESOURCES["capabilities"])


@mcp.tool()
def get_evidence() -> dict:
    """Return claim-to-evidence map: each key metric backed by source/proof."""
    return _fetch_json(RESOURCES["evidence"])


@mcp.tool()
def get_engage() -> dict:
    """Return structured outreach intake schema for initiating engagement."""
    return _fetch_json(RESOURCES["engage"])


@mcp.tool()
def get_agent_card() -> dict:
    """Return A2A-style agent card for capability discovery in agent workflows."""
    return _fetch_json(RESOURCES["agent_card"])


@mcp.tool()
def get_verification() -> dict:
    """Return cross-source identity and credential verification map."""
    return _fetch_json(RESOURCES["verification"])


@mcp.tool()
def get_case_study(name: str) -> str:
    """
    Return a full case study in Markdown.

    name options:
      - "donor_reporting"   — Donor reporting quality & delivery reliability
      - "audit_readiness"   — Cross-country portfolio & audit readiness
      - "saas_launch"       — SaaS / E-commerce platform launch delivery
      - "openclaw_rbm"      — OpenClaw RBM logic model skill pilot
    """
    key = f"case_{name}"
    if key not in RESOURCES:
        available = [k.replace("case_", "") for k in RESOURCES if k.startswith("case_")]
        return f"Unknown case study '{name}'. Available: {available}"
    return _fetch(RESOURCES[key])


@mcp.tool()
def list_resources() -> dict:
    """List all available resources and their URLs."""
    return {
        "resources": RESOURCES,
        "base_url": BASE_URL,
        "note": "All resources are read-only and served from the live GitHub Pages site.",
    }


@mcp.tool()
def search_profile(query: str) -> str:
    """
    Fetch profile + resume and return sections relevant to query keywords.
    Useful for quick Q&A like 'does he have audit experience?' without
    loading all resources.
    """
    profile_text = _fetch(RESOURCES["profile"])
    resume_data  = _fetch_json(RESOURCES["resume"])

    # Flatten resume to text for lightweight keyword search
    resume_text = json.dumps(resume_data, ensure_ascii=False)
    combined    = f"=== PROFILE ===\n{profile_text}\n\n=== RESUME ===\n{resume_text}"

    keywords = [kw.strip().lower() for kw in query.split()]
    lines    = combined.splitlines()
    hits     = [
        line for line in lines
        if any(kw in line.lower() for kw in keywords)
    ]

    if not hits:
        return f"No lines matching '{query}' found. Try get_profile() or get_resume() for full content."

    return "\n".join(hits[:60])  # cap at 60 lines


# ── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Vassiliy Lakhonin MCP Server")
    parser.add_argument(
        "--http",
        action="store_true",
        help="Run HTTP/SSE transport instead of stdio (for cloud deployment)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", 8000)),
        help="Port for HTTP mode (default: 8000 or $PORT env var)",
    )
    args = parser.parse_args()

    if args.http:
        if not HTTP_AVAILABLE:
            print(
                "ERROR: HTTP transport requires extra packages.\n"
                "Install with:  pip install mcp[cli] uvicorn starlette",
                file=sys.stderr,
            )
            sys.exit(1)

        print(f"Starting MCP HTTP/SSE server on port {args.port}...")
        sse = SseServerTransport("/messages/")

        async def handle_sse(request):
            async with sse.connect_sse(
                request.scope, request.receive, request._send
            ) as streams:
                await mcp._mcp_server.run(
                    streams[0], streams[1],
                    mcp._mcp_server.create_initialization_options(),
                )

        async def handle_messages(request):
            await sse.handle_post_message(request.scope, request.receive, request._send)

        app = Starlette(
            routes=[
                Route("/sse",       endpoint=handle_sse),
                Route("/messages/", endpoint=handle_messages, methods=["POST"]),
                Route("/health",    endpoint=lambda r: __import__("starlette.responses", fromlist=["JSONResponse"]).JSONResponse({"status": "ok", "server": "vassiliy-lakhonin-profile"})),
            ]
        )
        uvicorn.run(app, host="0.0.0.0", port=args.port)
    else:
        # Default: stdio (local use with Claude Desktop, etc.)
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
