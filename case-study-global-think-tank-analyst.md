# Case Study: Global Think Tank Analyst

## TL;DR
- Packaged a think-tank style analysis skill for geopolitical/policy tasks.
- Enforces explicit assumptions, confidence labels, and alternative hypotheses.
- Produces decision-useful outputs (briefs, scenarios, risk memos, JSON).
- Designed for clarity under uncertainty, not generic summarization.

## Evidence
- Public ClawHub listing available (link below).
- Structured output format and mode taxonomy documented in the case narrative.

## Metrics
- Framework coverage: PESTLE, stakeholder/power mapping, scenario/horizon, red-team.
- Output modes: executive summary, policy brief, risk memo, scenario set, JSON export.
- Reusability: instruction-only packaging for easy install/update.

## Context/Constraint
- Policy questions often arrive under-specified and politically ambiguous.
- Analysts need traceable reasoning structure, not prose-only answers.
- Uncertainty must remain visible for responsible decision support.


## Context
I packaged the Global Think Tank Analyst skill as a ClawHub-ready workflow for structured geopolitical, strategic, and policy analysis. The goal is to turn ambiguous international questions into clear, think-tank style output that is easier to review, compare, and act on.

## Problem
Policy and strategy questions often arrive with too little structure. Teams need analysis that separates facts from judgment, states assumptions, considers alternatives, and keeps uncertainty visible instead of hiding it inside prose.

## Actions
- Structured the skill around think-tank style analysis rather than generic summarization.
- Built an intake pattern for topic, region, horizon, actors, audience, and depth.
- Added framework selection so the model can choose only what the task needs.
- Incorporated PESTLE, stakeholder analysis, power mapping, scenario planning, horizon scanning, and red-team challenge modes.
- Added explicit confidence labels and alternative hypotheses.
- Designed the workflow to produce executive summaries, policy briefs, risk memos, scenarios, and JSON exports.
- Kept the skill instruction-only so it stays reusable and easy to install from ClawHub.

## What it does
- Produces structured geopolitical, strategic, and policy analysis.
- Separates sourced facts from expert judgment.
- States key assumptions and confidence levels.
- Generates scenario sets and indicators to watch.
- Supports red-team challenge mode for stress-testing claims.
- Outputs a clean, decision-useful format for policy and strategy teams.

## Current outputs
- Executive summary.
- Situation overview.
- Strategic drivers.
- PESTLE scan.
- Stakeholder analysis and power map.
- Risk matrix.
- Scenario set and horizon scan.
- Alternative hypotheses.
- Policy or strategy options.
- Recommendations and indicators to watch.
- JSON export block.

## Who it is for
- Policy analysts.
- Geopolitical researchers.
- Strategy teams.
- Risk and foresight professionals.
- Corporate intelligence teams.
- Think-tank style writers and brief producers.

## Why I built it
Most AI tools can summarize a topic, but they do not consistently produce analyst-grade structure. This skill is meant to make complex international analysis more readable, testable, and useful for decision-making.

## Tech stack
- ClawHub skill registry for installation and reuse.
- Template-driven intake and framework selection.
- Confidence labels to separate facts from judgment.
- Structured modes for brief, report, risk, scenarios, horizon, red-team, and JSON.
- Instruction-only design, with no external API dependency.

## Relevance
Demonstrates practical AI application in policy, strategy, and risk analysis workflows: structured framing, explicit uncertainty, and decision-useful outputs.

![OpenClaw-oriented workflow concept for structured geopolitical and policy analysis](/case-study-global-think-tank-analyst.jpg)

## Project links
- ClawHub skill listing: https://clawhub.ai/vassiliylakhonin/global-think-tank-analyst
