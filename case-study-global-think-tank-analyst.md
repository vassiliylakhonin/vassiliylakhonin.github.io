# Case Study: Agenda-Intelligence.md

## TL;DR
- Built **Agenda-Intelligence.md** as a portable markdown protocol for AI agents that analyze public agenda.
- Repositioned the project away from a tool-specific install flow and toward a plain `.md` layer any agent can copy, reference, or retrieve.
- Added regional lens packs for **Central Asia + Caspian** and **Middle East** to make the protocol useful beyond generic news analysis.
- Optimized the repo for people building research, news, policy, compliance, and risk agents.

## Evidence
- Public GitHub repository: https://github.com/vassiliylakhonin/agenda-intelligence-md
- Agent-readable orientation file: `llms.txt`.
- Base protocol files: `analysis-protocol.md`, `agenda-triage.md`, `evidence-discipline.md`, `output-patterns.md`.
- Regional lens packs: `regional/central-asia-caspian.md`, `regional/middle-east.md`.

## Metrics
- Core protocol files: 4.
- Regional lens packs: 2.
- Example briefs: 4.
- CI validation: repository structure and required protocol files checked on every push.
- Distribution model: plain markdown, usable outside any single agent runtime.

## Context/Constraint
- AI agents are getting better at collecting information, but many still write weak news analysis.
- The common failure mode is simple: they recap events, add confident-sounding commentary, and stop before the answer becomes useful.
- The project needed to work as a small reusable layer, not as a long prompt that bloats every agent context.

## Problem
Most AI-generated public-agenda analysis is readable but decision-light. It rarely says what changed, who gained leverage, what remains unknown, or what would falsify the view.

That is fine for a summary. It is weak for research, compliance, policy monitoring, investment context, or operating decisions.

## Actions
- Reframed the project as a **markdown protocol for agenda analysis**, not a news-summary skill.
- Defined the core separation agents should preserve:
  - Fact
  - Assessment
  - Assumption
  - Unknown
  - Scenario
  - Indicator to watch
- Added triage categories: noise, weak signal, signal, structural shift, trigger event, compliance-relevant development.
- Added evidence rules so agents do not imply live verification when none happened.
- Added output patterns for compact briefs, decision memos, red-team checks, and watchlists.
- Added regional lens packs for Central Asia + Caspian and Middle East, focused on regional failure modes that generic agents often miss.
- Removed tool-specific install language from the public README so the repo reads as a universal protocol first.

## What it does now
- Helps agents avoid shallow news summaries.
- Forces a clear answer to “what changed?”
- Separates facts from judgments and assumptions.
- Makes uncertainty visible without turning the answer into vague caveats.
- Produces watch-next indicators instead of soft endings.
- Gives regional checklists for higher-context analysis.

## Current outputs
- Bottom line.
- Signal classification.
- What changed.
- Why it matters.
- Who is affected.
- Main uncertainty.
- Scenarios.
- Watch-next indicators.

## Regional lens packs

### Central Asia + Caspian
Focused on sanctions routing, corridor politics, Caspian chokepoints, banking/payment exposure, state leverage, energy, minerals, and regional political economy.

### Middle East
Focused on escalation risk, energy flows, maritime chokepoints, sovereign capital, sanctions exposure, normalization, and regional power competition.

## Who it is for
- People building research or news agents.
- Policy and geopolitical analysts.
- Compliance and sanctions-monitoring workflows.
- Investors and founders tracking operating-context shifts.
- NGOs and advisory teams monitoring regional risk.
- Anyone tired of agents producing fluent but low-value news commentary.

## Why this version is better
It is small enough to reuse and strict enough to change the output. The protocol does not ask an agent to sound smarter. It asks the agent to classify signal, expose uncertainty, and name what to watch next.

That is the part most generic news analysis misses.

## Tech stack
- Plain markdown.
- GitHub repository with CI validation.
- Agent-readable `llms.txt`.
- Optional OpenClaw-compatible wrapper, but the protocol itself is runtime-agnostic.

## Relevance
This project demonstrates how I think about useful agent infrastructure: small files, explicit reasoning contracts, low context cost, and outputs that improve decisions rather than just sounding polished.

![Agenda-Intelligence.md workflow concept for agent agenda analysis](/case-study-global-think-tank-analyst.jpg)

## Project links
- GitHub repository: https://github.com/vassiliylakhonin/agenda-intelligence-md
