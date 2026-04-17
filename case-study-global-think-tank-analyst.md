# Case Study: Global Think Tank Analyst

## TL;DR
- Repositioned the skill as a **policy-risk memo architect**, not a generic “geopolitics explainer.”
- Optimized for decision support: clear options, trade-offs, indicators, and bounded confidence.
- Added strict evidence discipline to separate facts, assumptions, judgment, scenarios, and unknowns.
- Built mode-based outputs so teams can request quick briefs, standard memos, scenario briefs, or red-team stress tests.

## Evidence
- Public ClawHub listing: https://clawhub.ai/vassiliylakhonin/global-think-tank-analyst
- Public skill contract (purpose, intake, workflow, guardrails, output template).
- Explicit limits policy: no fabricated sources, no fake certainty, no legal/intelligence-style claims.

## Metrics
- Output modes: Quick Brief, Standard Memo, Scenario Brief, Red-Team Challenge.
- Core workflow depth: 9-step analytical sequence (decision framing -> options -> bounded judgment).
- Confidence protocol: Low / Moderate / High, tied to evidence quality and ambiguity.
- Decision quality bias: options and trade-offs required, not optional.

## Context/Constraint
- Policy requests usually arrive broad and under-specified.
- Teams need actionable judgment under uncertainty, not long summaries.
- Analysis had to stay transparent about evidence limits and avoid confidence theater.

## Problem
Most AI analysis outputs sound polished but are weak for real decisions. They blend fact and inference, understate unknowns, and overuse frameworks without improving choices.

## Actions
- Reframed the skill mission from “think tank style writing” to **decision-space clarification**.
- Added intake discipline: question, audience, geography, time horizon, actors, domain, depth, evidence mode.
- Enforced evidence separation and explicit “EVIDENCE ACCESS LIMITED” handling when source access is constrained.
- Standardized analytical sequence:
  1) define decision problem,
  2) context,
  3) actors/incentives,
  4) evidence limits,
  5) competing interpretations,
  6) risks/trade-offs,
  7) scenarios,
  8) options,
  9) bounded conclusion.
- Added recommendation rules to prevent vague advice and force trigger-based action guidance.
- Restricted framework sprawl: tools like PESTLE/SWOT only when they add decision value.

## What it does now
- Produces decision-ready geopolitical and policy memos.
- Makes uncertainty explicit without collapsing into non-answers.
- Compares plausible interpretations when ambiguity is real.
- Returns practical options with downside and implementation friction.
- Outputs concrete indicators to watch and trigger conditions.

## Current outputs
- Executive takeaway.
- Decision context.
- Known facts and evidence limits.
- Actor and incentive map.
- Main assessment.
- Risks and trade-offs.
- Options.
- Indicators to watch.
- Confidence and key unknowns.

## Who it is for
- Policy and geopolitical analysts.
- Strategy and risk teams.
- Corporate intelligence and foresight functions.
- Think-tank and advisory teams producing decision memos.

## Why this version is better
It is optimized for choices, not prose. The output is tighter, more auditable, and more useful under ambiguity because it forces explicit limits and concrete options.

## Tech stack
- OpenClaw runtime.
- ClawHub skill distribution.
- Instruction-first architecture with mode routing and evidence guardrails.

## Relevance
Demonstrates product-grade prompt architecture for high-stakes analysis: clear decision framing, explicit uncertainty, and operator-friendly outputs.

![OpenClaw-oriented workflow concept for structured geopolitical and policy analysis](/case-study-global-think-tank-analyst.jpg)

## Project links
- ClawHub skill listing: https://clawhub.ai/vassiliylakhonin/global-think-tank-analyst
