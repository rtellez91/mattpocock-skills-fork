# Experience readiness

Assess the specific deliverable against current evidence. Completing an interview or a spec is distinct from being ready to implement every experience it describes. A future design question can be explicitly deferred, but cannot be silently treated as answered or used to dispatch dependent implementation.

## Criteria

| Criterion | Sufficient evidence for this deliverable |
| --- | --- |
| Outcome and scope | Actor, goal, entry, completion, exclusions, and ownership are clear |
| Behavior | The main flow and consequential alternatives, interruptions, errors, recovery, permissions, and hosted transitions are decided where applicable |
| Information and actions | Information hierarchy, representative content, actions, and their consequences are specified sufficiently to avoid inventing product behavior |
| Visual target | A selected visual reference or an accepted existing pattern covers the surface, relevant sizes, and states; exceptions are explicit |
| Product compatibility | Reusable components, variants, tokens, assets, and patterns are identified against current sources; proposed additions or departures have a decision |
| Accessibility intent | Applicable focus, keyboard, labels, reading order, contrast, and state communication requirements are defined; actual runtime checks remain implementation obligations |
| Reviewable handoff | Exact references are accessible, decisions have one canonical home, and acceptance criteria can verify the delivered outcome |
| Blocking uncertainty | No remaining unknown forces the implementer to choose product behavior, interaction structure, or visual direction on behalf of the human |

Apply only relevant criteria. Existing components can supply documented states without a new mock for each state. New screenshots are not required for unchanged patterns. Reference the evidence and explain omissions; do not turn optional dimensions into blanket blockers.

## Disposition

Use one of these plain-language conclusions, not new tracker labels:

- **Ready:** applicable criteria are covered by current evidence and accepted decisions.
- **Covered by existing design:** cite the current contract and explain why it covers this scope. This is ready for design purposes without additional exploration.
- **Pending:** name the unresolved decision or missing evidence, its owner or next action, and the specific deliverables it gates.
- **Not applicable:** explain why the change has no experience-design impact. Technical requirements and execution authorization still apply.

Record the disposition in the existing canonical spec or ticket, alongside the evidence assessed and remaining limitations. A closed design issue alone does not establish readiness if the linked evidence is missing, obsolete, or incomplete for the current scope. Verify the handoff, not just the issue state.

Ready means sufficiently decided to implement, not proven market value, demonstrated usability, runtime accessibility compliance, or release readiness. Distinguish stakeholder selection, expert review, prototype verification, and participant research. Where uncertain user behavior would materially change the proposed solution, identify the needed research or explicit product decision before declaring the dependent scope ready. Routine implementation details do not require a design gate.

## Dependencies and execution

A ticket can be fully specified yet wait on an implementation dependency. Separate that execution dependency from design readiness. A ticket whose design is pending is not an autonomous implementation candidate. Map this to the configured tracker roles; do not create labels or change their semantics automatically.

When design changes an agreed requirement, present the effect and obtain the product decision before revising the canonical requirement. Under the existing authorization, update affected references and dependent tickets together. If publication is not authorized, return the exact proposed changes without mutating the tracker.

Independent work may proceed when its complete deliverable can be decided, built, and verified without the pending design. A technical-layer name is not evidence of independence.

## Minimal record

Use a short paragraph or table containing: deliverable, disposition, supporting evidence, blocking question if any, and next action. Do not create a parallel registry or duplicate editable requirements.
