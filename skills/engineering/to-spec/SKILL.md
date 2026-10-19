---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user; just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. Sketch out the seams at which you're going to test the feature. Existing seams should be preferred to new ones. Use the highest seam possible. If new seams are needed, propose them at the highest point you can. The fewer seams across the codebase, the better - the ideal number is one.

Check with the user that these seams match their expectations.

3. For experience-bearing work, call the Skill tool with "ux-discovery" in assessment mode. Synthesize existing evidence only: do not start research or design. Record design readiness per deliverable and name unresolved decisions and their impact. An internal change with no experience impact can state that briefly.

4. Write the spec using the applicable sections below, then publish within the requested scope. A draft request stays a draft. Use configured tracker roles based on actual readiness; a parent spec is not automatically an executable `ready-for-agent` ticket. In particular, pending design decisions must not be hidden by that label. Lead with material the whole team can review; place implementation detail after observable requirements.

Preserve every agreed technical decision in scope, including constraints, exact values and units, conditions, exceptions, and explicit prohibitions. Before publication, compare the completed spec against the source conversation and canonical decisions; correct any omission, weakening, or contradiction introduced by synthesis. A precise, accessible reference to a canonical contract can preserve a decision without duplicating it. If a source is missing or conflicting, identify the specific gap instead of inventing an answer or claiming complete coverage.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A concise set of distinct actor goals and important boundary behaviors. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

Cover the established scope without repeating every requirement as another story. Omit user stories for internal work with no meaningful actor; describe its purpose and observable guarantees instead.

## Experience and Functional Requirements

Describe the agreed outcome, scope, main journey, consequential alternatives, rules, and observable results in the domain's language. Include hosted transitions and ownership where relevant. Use stable requirement identifiers when multiple deliveries need traceability. Omit dimensions irrelevant to the work rather than inventing content.

## Design Evidence and Readiness

Summarize the assessment from `ux-discovery`: deliverable, disposition, exact existing/selected references, and unresolved design decisions with their effect. Reference the canonical decision instead of duplicating it. Distinguish hypotheses, stakeholder selection, inspected behavior, and user research. State whether design must precede decomposition or can be bounded dependent work, with the reason. A completed requirements discussion may leave explicit design work pending.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

Lead with observable acceptance scenarios that the whole team can understand. For UI, identify the relevant browser, responsive, interaction, and accessibility checks still required in implementation. A prototype check or selected image does not prove production behavior.

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>
