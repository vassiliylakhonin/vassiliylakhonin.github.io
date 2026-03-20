#!/usr/bin/env python3
import json
import re
import sys
import urllib.request
from pathlib import Path

BASE = "https://vassiliylakhonin.github.io"
FILES = {
    "robots": Path("robots.txt"),
    "llms": Path("llms.txt"),
    "sitemap": Path("sitemap.xml"),
    "agent_card": Path("agent-card.json"),
    "resume": Path("resume.json"),
    "capabilities": Path("capabilities.json"),
    "evidence": Path("evidence.json"),
    "availability": Path("availability.json"),
    "skills": Path("skills.json"),
}

AI_BOTS = ["OAI-SearchBot", "GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended"]


def exists(url: str, timeout: int = 10) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return 200 <= r.status < 400
    except Exception:
        return False


def main() -> int:
    score = 100
    critical = []
    warnings = []
    checks = []

    for name, p in FILES.items():
        ok = p.exists() and p.stat().st_size > 0
        checks.append((f"file:{name}", ok))
        if not ok:
            score -= 10
            critical.append(f"Missing required file: {p}")

    robots = FILES["robots"].read_text(encoding="utf-8") if FILES["robots"].exists() else ""
    for bot in AI_BOTS:
        has = bool(re.search(rf"(?im)^User-agent:\s*{re.escape(bot)}\s*$", robots))
        checks.append((f"robots:{bot}", has))
        if not has:
            score -= 4
            warnings.append(f"robots.txt missing explicit policy for {bot}")

    llms = FILES["llms"].read_text(encoding="utf-8") if FILES["llms"].exists() else ""
    mcp_link_ok = "vassiliy-lakhonin-mcp-production.up.railway.app/sse" in llms
    checks.append(("llms:mcp_sse_link", mcp_link_ok))
    if not mcp_link_ok:
        score -= 8
        warnings.append("llms.txt missing MCP SSE endpoint")

    sse_ok = exists("https://vassiliy-lakhonin-mcp-production.up.railway.app/sse")
    checks.append(("remote:mcp_sse", sse_ok))
    if not sse_ok:
        score -= 20
        critical.append("Remote MCP SSE endpoint unreachable")

    health_ok = exists("https://vassiliy-lakhonin-mcp-production.up.railway.app/health")
    checks.append(("remote:mcp_health", health_ok))
    if not health_ok:
        score -= 12
        critical.append("Remote MCP health endpoint unreachable")

    score = max(score, 0)

    report = [
        "# GEO Baseline Report",
        "",
        f"- Score: **{score}/100**",
        f"- Critical issues: **{len(critical)}**",
        f"- Warnings: **{len(warnings)}**",
        "",
        "## Checks",
    ]
    for name, ok in checks:
        report.append(f"- {'✅' if ok else '❌'} {name}")

    if critical:
        report += ["", "## Critical", *[f"- {x}" for x in critical]]
    if warnings:
        report += ["", "## Warnings", *[f"- {x}" for x in warnings]]

    report += [
        "",
        "## Top 5 fixes",
        "- Keep robots.txt explicit for key AI crawlers (OAI, GPTBot, ClaudeBot, PerplexityBot, Google-Extended)",
        "- Keep llms.txt synchronized with live MCP/JSON endpoints",
        "- Maintain JSON artifacts completeness (resume/capabilities/evidence/availability/skills)",
        "- Ensure MCP /sse and /health stay green after each deploy",
        "- Run this audit weekly via CI and track trend",
    ]

    Path("geo-report.md").write_text("\n".join(report), encoding="utf-8")
    Path("geo-report.json").write_text(
        json.dumps({"score": score, "critical": critical, "warnings": warnings}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("\n".join(report))
    return 1 if critical else 0


if __name__ == "__main__":
    sys.exit(main())
