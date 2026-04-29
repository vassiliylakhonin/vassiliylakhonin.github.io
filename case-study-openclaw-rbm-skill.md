# Case Study: Nonprofit Proposal Go/No-Go Engine

## TL;DR
- Built a **decision-grade nonprofit proposal engine** for OpenClaw and Codex.
- The core product is not a prettier proposal. It is a defensible submission decision: **Go / Conditional Go / No-Go**.
- The workflow combines donor-fit, RBM/Theory of Change, logframe, MEAL, safeguarding, budget logic, and evidence traceability.
- The skill is designed for teams that need to decide whether a proposal is worth submitting before they spend scarce time polishing weak logic.

## Evidence
- Public GitHub repository: https://github.com/vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub
- Public ClawHub listing: https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model
- OpenClaw skill: `SKILL.md`.
- Codex-ready variant: `codex/SKILL.md`.
- CI workflow and public repository hygiene: license, contribution guide, security policy, PR template.

## Metrics
- Verdict system: Go / Conditional Go / No-Go.
- Output modes: Concept, LOI, Full Proposal, Review, Donor-Fit, Express.
- Minimum input contract: donor/call, geography, target group, problem, scope, budget, timeline, partners, requested mode.
- Evidence labels: Fact, Assumption, Hypothesis, Unknown, Verdict.
- Core proposal components: RBM/ToC, logframe, MEAL mini-plan, risk/safeguarding matrix, donor-fit matrix, readiness checklist.

## Context/Constraint
- Nonprofit teams rarely fail because they cannot write enough text.
- They fail because the proposal logic is thin, donor fit is assumed, evidence gaps are hidden, or the budget/timeline does not survive review.
- Under deadline pressure, teams need a hard read before drafting turns into sunk cost.

## Problem
Most proposal-assistant workflows optimize for narrative production. That is useful, but dangerous when the underlying submission is weak.

A polished proposal can still be a bad submission if it has unsupported targets, unclear assumptions, weak donor alignment, safeguarding gaps, or a budget that does not match the intervention.

## Actions
- Reframed the skill from “proposal drafting assistant” to **submission decision engine**.
- Required every substantive run to support a verdict: **Go**, **Conditional Go**, or **No-Go**.
- Added a minimum input gate. If two or more critical fields are missing, the skill should not produce a polished proposal.
- Built six modes:
  - Concept
  - LOI
  - Full Proposal
  - Review
  - Donor-Fit
  - Express
- Standardized the evidence split:
  - Fact
  - Assumption
  - Hypothesis
  - Unknown
  - Verdict
- Added donor-fit checks instead of vague alignment claims.
- Added RBM/Theory of Change and logframe structure before prose.
- Added MEAL, safeguarding, feasibility, and budget-integrity stress tests.
- Added explicit anti-fabrication rules for donor criteria, citations, baselines, targets, partner commitments, and budget figures.
- Added a Codex-ready variant so the same discipline can be used outside OpenClaw.

## What it does now
- Turns rough nonprofit project inputs into a donor-aligned proposal package.
- Reviews existing drafts for structural weaknesses before submission.
- Shows donor-fit gaps instead of smoothing them over.
- Builds RBM/ToC and logframe-ready logic.
- Marks unsupported claims as evidence needs.
- Gives a clear submission gate with reasons and required fixes.

## Current outputs
- Submission framing block.
- Decision Summary with verdict and confidence.
- Facts / Assumptions / Hypotheses / Unknowns.
- Concept note, LOI, or proposal core sections depending on mode.
- Donor-fit matrix.
- RBM/ToC and logframe-ready structure.
- MEAL mini-plan.
- Risk, safeguarding, and feasibility checks.
- Budget logic summary.
- Evidence and verification plan.
- Submission readiness checklist.

## Who it is for
- NGO grant managers and proposal leads.
- MEAL/M&E specialists.
- Nonprofit consultants and bid teams.
- Program directors deciding whether to proceed.
- Small teams that need submission discipline without building a full proposal office.

## Why this version is better
It does not try to make weak proposals sound strong. It exposes the weaknesses early.

That is the point. A Go/No-Go engine is more useful than a drafting assistant when time, credibility, and donor fit matter.

## Tech stack
- OpenClaw skill architecture.
- Codex-compatible skill variant.
- GitHub repository with CI and contribution hygiene.
- ClawHub distribution.
- Instruction-first design with explicit evidence and readiness gates.

## Relevance
This project shows practical agent design for nonprofit operations: turn ambiguous inputs into a structured decision, preserve uncertainty, and prevent polished text from hiding submission risk.

## Project links
- GitHub repository: https://github.com/vassiliylakhonin/nonprofit-rbm-skill-for-claw-hub
- ClawHub listing: https://clawhub.ai/vassiliylakhonin/nonprofit-rbm-logic-model
