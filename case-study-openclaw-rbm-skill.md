# Case Study: Nonprofit Proposal Decision Engine

## TL;DR
- Reframed the skill from “proposal drafting assistant” to a **submission decision engine**.
- Core output is not just text, but a hard verdict: **Go / Conditional Go / No-Go**.
- Enforced evidence discipline: facts, assumptions, hypotheses, unknowns are always separated.
- Built for NGO proposal teams that need donor-fit, risk visibility, and traceable decisions under deadline pressure.

## Evidence
- Public ClawHub listing: https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model
- Public skill contract and instructions (mode system, output structure, evidence guardrails).
- Explicit safety boundaries: no fabricated citations, no legal/financial sign-off, no guaranteed funding claims.

## Metrics
- Decision outputs: Go / Conditional Go / No-Go (mandatory in every substantive run).
- Mode coverage: concept, loi, full, review, donor-fit, express.
- Minimum input gate: 8 critical fields before full drafting.
- Evidence confidence labels: HIGH / MEDIUM / LOW / UNVERIFIED.

## Context/Constraint
- Nonprofit teams often produce strong narrative but weak submission discipline.
- Donor proposals fail due to hidden unknowns, weak evidence, or unrealistic budget/timeline logic.
- Needed a reusable workflow that prioritizes decision quality and traceability over prose volume.

## Problem
Most grant workflows over-optimize for polished narrative and under-optimize for decision integrity.
That creates avoidable submission risk: unclear assumptions, weak donor-fit mapping, and missing verification steps.

## Actions
- Defined a strict operating contract: optimize for submission quality, not verbosity.
- Added explicit input gate (donor/call, geography, target group, problem, scope, budget, timeline, partners, output mode).
- Implemented mode routing for different job types:
  - `concept`, `loi`, `full`, `review`, `donor-fit`, `express`.
- Standardized output into fixed sections:
  1) Decision Summary,
  2) Facts/Assumptions/Hypotheses/Unknowns,
  3) Core Proposal Artifacts,
  4) Donor-Fit Matrix,
  5) Evidence and Traceability,
  6) Submission Readiness Checklist.
- Added hard evidence rules and confidence labels to prevent fabricated certainty.
- Added safety guardrails: escalate compliance/safeguarding/budget realism risks early.

## What it does now
- Produces donor-oriented proposal artifacts plus a clear submission decision.
- Surfaces risk and uncertainty early instead of hiding them behind confident prose.
- Creates donor-fit gap analysis with concrete fix actions.
- Forces an evidence plan when source support is missing.

## Current outputs
- Decision Summary (Go / Conditional Go / No-Go + confidence + reasons).
- RBM/ToC logic and logframe-ready structure.
- MEAL mini-plan and budget logic summary.
- Risk and safeguarding matrix.
- Donor-fit matrix with gap-to-action mapping.
- Submission readiness checklist and verification plan.

## Who it is for
- NGO grant managers and proposal leads.
- MEAL/M&E specialists.
- Nonprofit consultants and bid teams.
- Program directors who need a defensible decision before submission.

## Why this version is better
- It treats proposal writing as a decision system, not a text-generation task.
- It improves submission discipline under time pressure.
- It is transparent about uncertainty, which improves trust and review quality.

## Tech stack
- OpenClaw (execution runtime and orchestration).
- ClawHub (skill distribution).
- Instruction-first architecture with explicit contracts and guardrails.

## Relevance
Demonstrates product + operations thinking applied to nonprofit workflows: tighter input gates, better risk signaling, and measurable improvement in submission readiness quality.

## Project links
- ClawHub skill listing: https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model
- OpenClaw skill repository: https://github.com/vassiliylakhonin/Nonprofit-RBM-Skill-For-Claw-Hub
