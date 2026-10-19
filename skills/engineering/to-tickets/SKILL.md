---
name: to-tickets
description: Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one file per ticket locally, or native blocking links on a real tracker).
disable-model-invocation: true
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets**: tracer-bullet implementation slices and, when needed, bounded design work, each declaring the tickets or decisions that **block** it.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Assess design timing and draft the work

For experience-bearing work, call the Skill tool with "ux-discovery" in assessment mode. Reuse the accepted evidence and current product patterns. The agent decides whether design must precede decomposition or can be bounded work with dependencies, and explains why. If an open design decision could change delivery boundaries, return that concrete question and a provisional breakdown instead of publishing a fictional implementation-ready plan. Continue independent, well-defined scope.

When boundaries are stable, distinguish **Design** from **Implementation** tickets. A design ticket states the question or experience to resolve, fixed constraints, resources to reuse, expected evidence, human decisions required, and handoff criteria from the assessment. Keep coherent journeys together instead of creating one design ticket per technical layer or screen. New UI exploration and prototyping use the Product Design bridge through `ux-discovery`; this decomposition step does not start generation.

Give a design ticket its own acceptance criteria for a decided, usable handoff, not a screenshot count. Assign dependencies only to implementation deliverables that require its answer. Verify that accepted existing designs still cover the current scope before adding or removing a design blocker.

Break implementation work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each implementation slice covers every layer required for its complete deliverable (such as schema, API, UI, and tests). Do not add unrelated layers; a technical layer alone is not proof of a complete deliverable.
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

Give each ticket its **blocking edges**: the other tickets that must complete before it can start. An implementation ticket can start only when dependencies are satisfied and its relevant decisions are settled. An empty dependency list is not proof of design readiness.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket; green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work
- **Kind and readiness**: design or implementation, supporting references, and any unresolved decision

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Publish the tickets to the configured tracker

Before publication, compare the complete ticket set against the source spec, plan, or conversation and its canonical decisions. Preserve every agreed technical decision in scope, including constraints, exact values and units, conditions, exceptions, and explicit prohibitions, in each ticket that depends on it or through a precise, accessible reference to the shared contract. Correct any omission, weakening, contradiction, or decision left without a responsible ticket during decomposition. If a source is missing or conflicting, identify the specific gap instead of inventing an answer or claiming complete coverage.

Publish the approved tickets. **How** depends on the tracker `/setup-matt-pocock-skills` configured; the tickets are the same either way, only the shape of the blocking edges changes:

- **Local files** → write one file per ticket under `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01` in dependency order (blockers first). Each file's "Blocked by" lists the numbers/titles it depends on. Use the per-ticket file template below: one ticket per file, never a single combined file.
- **A real issue tracker (GitHub, Linear, …)** → publish one issue per ticket in dependency order (blockers first) so each ticket's blocking edges can reference real identifiers. Use the platform's native blocking relationship where it has one; otherwise set each ticket's "Blocked by" to the blocking issues. If the source was an existing issue, make each ticket its sub-issue (tracker doc's operation). Use the configured readiness roles. Reserve `ready-for-agent` for sufficiently specified autonomous implementation work; design tickets requiring human choices and implementation tickets with pending design are not agent-grabbable by construction. Keep ordinary implementation dependencies explicit even when the contract is fully specified. Verify published bodies and relationships.

Work the implementation **frontier**: implementation tickets whose blockers are all done and whose current design evidence satisfies the assessment. Design/decision work follows its own human exchange; an implementation executor must not silently answer it.

Do NOT close or modify any parent issue.

<local-ticket-template>

# <NN>: <Ticket title>

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective, not a layer-by-layer implementation list.

**Why it matters:** the problem or outcome in language the whole team can review.

**Kind:** Implementation or Design. For Design, describe the question and evidence to deliver instead of a production build.

**Design readiness:** disposition, supporting references, and remaining decisions from the assessment; omit only when not applicable and explained.

**Blocked by:** the numbers/titles of the tickets that gate this one, or "None (can start immediately)".

**Status:** the configured readiness role justified by this ticket's actual remaining work.

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

Put relevant technical contracts and source requirements after the team-readable outcome and criteria. Link canonical decisions rather than copying them.

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue, otherwise omit this section).

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective, not layer-by-layer implementation.

Explain why it matters. Identify **Kind: Implementation or Design**; for Design, describe the decision/evidence to deliver. Put technical contracts after the observable acceptance criteria.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None (can start immediately)". Omit this section when blockers were set as native edges.

</issue-template>

Include a **Design readiness and references** section with the assessment disposition, exact supporting references, and remaining decisions. Keep named decision blockers visible even when native issue edges are used. Explain non-applicability where appropriate. Follow it with **Technical notes** for relevant source requirements, contracts, and implementation constraints.

In either form, avoid specific file paths or code snippets: they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.
