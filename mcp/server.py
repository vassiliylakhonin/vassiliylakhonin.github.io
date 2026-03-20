"""
Vassiliy Lakhonin — MCP Server for CV/Profile Resources
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Any

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

try:
    from starlette.applications import Starlette
    from starlette.responses import JSONResponse, Response
    from starlette.routing import Mount, Route
    import uvicorn

    HTTP_AVAILABLE = True
except ImportError:
    HTTP_AVAILABLE = False

BASE_URL = "https://vassiliylakhonin.github.io"

RESOURCES = {
    "profile": f"{BASE_URL}/profile.md",
    "resume": f"{BASE_URL}/resume.json",
    "evidence": f"{BASE_URL}/evidence.json",
    "availability": f"{BASE_URL}/availability.json",
    "capabilities": f"{BASE_URL}/capabilities.json",
    "engage": f"{BASE_URL}/engage.json",
    "agent_card": f"{BASE_URL}/agent-card.json",
    "verification": f"{BASE_URL}/verification.json",
    "skills": f"{BASE_URL}/skills.json",
    "llms_txt": f"{BASE_URL}/llms.txt",
    "humans_txt": f"{BASE_URL}/humans.txt",
    "case_donor_reporting": f"{BASE_URL}/case-study-donor-reporting.md",
    "case_audit_readiness": f"{BASE_URL}/case-study-portfolio-audit-readiness.md",
    "case_saas_launch": f"{BASE_URL}/case-study-saas-ecommerce-launch.md",
    "case_openclaw_rbm": f"{BASE_URL}/case-study-openclaw-rbm-skill.md",
    "case_global_think_tank": f"{BASE_URL}/case-study-global-think-tank-analyst.md",
}


def _fetch(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=12) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} fetching {url}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error fetching {url}: {e.reason}") from e


def _fetch_json(url: str) -> dict:
    return json.loads(_fetch(url))


def _safe_get(data: Any, *path: str, default=None):
    cur = data
    for p in path:
        if not isinstance(cur, dict) or p not in cur:
            return default
        cur = cur[p]
    return cur


def _extract_achievements(resume: dict, evidence: dict) -> list[dict]:
    achievements: list[dict] = []
    work = _safe_get(resume, "work", default=[]) or []
    for job in work:
        for h in job.get("highlights", [])[:8]:
            nums = re.findall(r"\d+[%MmkK$]*", h)
            achievements.append(
                {
                    "metric": h,
                    "value": nums[0] if nums else None,
                    "period": f"{job.get('startDate','')}..{job.get('endDate','present')}",
                    "context": f"{job.get('name','')} — {job.get('position','')}",
                    "evidence_url": job.get("url") or _safe_get(evidence, "source") or BASE_URL,
                    "confidence": 0.85,
                }
            )
    return achievements[:20]


def _keyword_score(text: str, keywords: list[str]) -> int:
    t = text.lower()
    score = 0
    for k in keywords:
        if k in t:
            score += 1
    return score


def _role_keywords() -> dict[str, list[str]]:
    return {
        "program": ["program", "portfolio", "pmo", "operations", "governance"],
        "compliance": ["compliance", "audit", "donor", "usaid", "evidence", "reporting"],
        "delivery": ["delivery", "kpi", "stakeholder", "risk", "coordination", "sprint"],
        "tech": ["ai", "automation", "mcp", "openclaw", "saas", "e-commerce"],
    }


mcp = FastMCP(
    name="vassiliy-lakhonin-profile",
    instructions=(
        "Read-only access to Vassiliy Lakhonin's CV, case studies, and "
        "availability data. Use this server to answer recruiter and agent "
        "queries about experience, skills, metrics, and engagement."
    ),
)


@mcp.tool()
def get_profile(mode: str = "short") -> str:
    """Return profile in short or full mode. mode: short|full"""
    profile_md = _fetch(RESOURCES["profile"])
    if mode == "full":
        return profile_md

    resume = _fetch_json(RESOURCES["resume"])
    availability = _fetch_json(RESOURCES["availability"])
    basics = _safe_get(resume, "basics", default={})
    work = _safe_get(resume, "work", default=[]) or []

    top_highlights = []
    for job in work[:2]:
        top_highlights.extend(job.get("highlights", [])[:2])

    lines = [
        f"Name: {basics.get('name','Vassiliy Lakhonin')}",
        f"Role: {basics.get('label','Program/Portfolio/PMO Manager')}",
        f"Location: {_safe_get(basics,'location','city',default='Almaty')}, {_safe_get(basics,'location','countryCode',default='KZ')}",
        f"Email: {basics.get('email','vassiliy.lakhonin@gmail.com')}",
        f"Website: {basics.get('url', BASE_URL)}",
        "Top impact:",
    ]
    lines.extend([f"- {h}" for h in top_highlights[:4]])
    lines.append(f"Availability: {availability.get('status','available')} | {availability.get('notice_period','n/a')}")
    return "\n".join(lines)


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
def get_metrics() -> dict:
    """Return normalized achievements list for scoring/automation."""
    resume = _fetch_json(RESOURCES["resume"])
    evidence = _fetch_json(RESOURCES["evidence"])
    return {"achievements": _extract_achievements(resume, evidence)}


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
def get_skills() -> dict:
    """Return machine-readable skill graph (domain, tools, methods, intent)."""
    return _fetch_json(RESOURCES["skills"])


@mcp.tool()
def get_case_study(name: str, format: str = "full") -> str:
    """Return case study markdown. format: full|short|bullets"""
    key = f"case_{name}"
    if key not in RESOURCES:
        available = [k.replace("case_", "") for k in RESOURCES if k.startswith("case_")]
        return f"Unknown case study '{name}'. Available: {available}"

    text = _fetch(RESOURCES[key])
    if format == "full":
        return text

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if format == "bullets":
        bullets = [ln for ln in lines if ln.startswith("-")][:10]
        if bullets:
            return "\n".join(bullets)
    return "\n".join(lines[:20])


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
    """Keyword search across profile + resume."""
    profile_text = _fetch(RESOURCES["profile"])
    resume_data = _fetch_json(RESOURCES["resume"])
    resume_text = json.dumps(resume_data, ensure_ascii=False)
    combined = f"=== PROFILE ===\n{profile_text}\n\n=== RESUME ===\n{resume_text}"

    keywords = [kw.strip().lower() for kw in query.split() if kw.strip()]
    lines = combined.splitlines()
    hits = [line for line in lines if any(kw in line.lower() for kw in keywords)]

    if not hits:
        return f"No lines matching '{query}' found. Try get_profile() or get_resume() for full content."
    return "\n".join(hits[:60])


@mcp.tool()
def match_job(job_text: str, role_target: str = "") -> dict:
    """Score fit against job text and return strengths/gaps/positioning."""
    resume = _fetch_json(RESOURCES["resume"])
    availability = _fetch_json(RESOURCES["availability"])

    resume_text = json.dumps(resume, ensure_ascii=False)
    jt = job_text.lower()

    score = 40
    strengths = []
    gaps = []

    for group, kws in _role_keywords().items():
        s = _keyword_score(jt, kws)
        if s >= 2:
            score += 10
            strengths.append(f"Strong {group} match")
        elif s == 1:
            score += 4
            strengths.append(f"Partial {group} match")
        else:
            gaps.append(f"Low explicit {group} keyword overlap")

    proof_hits = _keyword_score(resume_text, ["usaid", "audit", "portfolio", "kpi", "delivery", "compliance"])
    score += min(15, proof_hits * 2)

    score = max(0, min(100, score))
    if role_target:
        strengths.append(f"Target role considered: {role_target}")

    red_flags = []
    if "relocation" in jt and "remote" in json.dumps(availability).lower():
        red_flags.append("Role may require relocation; confirm location expectations")
    if "immediate" in jt:
        red_flags.append("Confirm start date / notice alignment")

    positioning = (
        "Lead with cross-border program delivery, donor-compliance evidence governance, "
        "and measurable reporting outcomes (14M portfolio, on-time reporting, audit readiness)."
    )

    return {
        "fit_score": score,
        "strengths": strengths[:6],
        "gaps": gaps[:6],
        "mitigations": [
            "Provide case study links tailored to role domain",
            "Use evidence-backed metrics in first outreach message",
        ],
        "recommended_positioning": positioning,
        "red_flags": red_flags,
    }


@mcp.tool()
def generate_pitch(context: str, format: str = "dm_short") -> dict:
    """Generate outreach pitch. format: dm_short|email|proposal_intro"""
    profile_short = get_profile("short")

    if format == "email":
        text = (
            "Subject: Program/Portfolio leadership support\n\n"
            f"Hi,\n\n{context}\n\n"
            "I help teams improve delivery reliability, donor compliance, and KPI governance across multi-country programs. "
            "Recent outcomes include 100% on-time donor reporting (8 quarters), 40% reduction in partner submission delays, "
            "and audit-ready documentation with zero findings.\n\n"
            "If useful, I can share a tailored 1-page approach for your current priorities.\n"
        )
    elif format == "proposal_intro":
        text = (
            "This engagement will establish a practical PMO/evidence layer for execution control: "
            "clear KPI cadence, risk escalation, audit-ready documentation, and delivery governance. "
            "Approach is evidence-first and designed for cross-team, cross-country operations."
        )
    else:
        text = (
            "I help program teams improve delivery + compliance with evidence-backed ops. "
            "Recent impact: $14M portfolio oversight, 100% on-time donor reporting, -40% partner delays, zero audit findings. "
            "Happy to share a targeted plan for your context."
        )

    return {"format": format, "pitch": text, "profile_short": profile_short}


@mcp.tool()
def generate_cover_letter(job_text: str, tone: str = "professional") -> str:
    """Generate concise evidence-backed cover letter draft."""
    fit = match_job(job_text)
    intro = "Dear Hiring Team," if tone == "professional" else "Hello team,"
    return (
        f"{intro}\n\n"
        "I’m applying for this role with a focus on program/portfolio delivery, compliance, and measurable outcomes. "
        "I have led cross-country execution and reporting systems in donor-funded and private-sector contexts.\n\n"
        "Relevant evidence:\n"
        "- Managed performance/reporting for a $14M regional program\n"
        "- Delivered 100% on-time donor reporting for 8 consecutive quarters\n"
        "- Reduced partner submission delays by 40%\n"
        "- Supported donor audits with zero findings\n\n"
        f"Role fit score (machine estimate): {fit['fit_score']}/100\n"
        f"Positioning: {fit['recommended_positioning']}\n\n"
        "I’d welcome a short conversation to discuss how I can support your team’s delivery goals.\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Vassiliy Lakhonin MCP Server")
    parser.add_argument("--http", action="store_true", help="Run HTTP/SSE transport instead of stdio")
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", 8000)),
        help="Port for HTTP mode (default: 8000 or $PORT)",
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

        sse_app = mcp.sse_app()

        async def handle_health(request):
            return JSONResponse({"status": "ok", "server": "vassiliy-lakhonin-profile"})

        async def handle_sse_head(request):
            return Response(
                status_code=200,
                headers={
                    "cache-control": "no-store",
                    "x-accel-buffering": "no",
                    "content-type": "text/event-stream; charset=utf-8",
                },
            )

        app = Starlette(
            routes=[
                Route("/health", endpoint=handle_health),
                Route("/sse", endpoint=handle_sse_head, methods=["HEAD"]),
                Mount("/", app=sse_app),
            ]
        )
        uvicorn.run(app, host="0.0.0.0", port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
