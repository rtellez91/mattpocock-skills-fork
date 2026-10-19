---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Check the ticket's kind, actual blocking relationships, and accepted contracts before building. For experience-bearing work, call the Skill tool with "ux-discovery" in assessment mode against the current references. A readiness label or closed design issue alone is insufficient. Build only deliverables whose decisions and dependencies permit execution; report the specific blocked part and continue independent authorized work. A design/decision ticket is not an implementation assignment, and this skill must not silently choose its visual direction or product behavior.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

For UI, reuse the accepted product components, tokens, and assets. Verify relevant interactions, sizes, states, and accessibility behavior in the browser against the selected references and acceptance criteria. If the Product Design plugin built the prototype, preserve its design evidence; its prototype QA does not replace verification of the production implementation. Report unavailable checks and scope any readiness claim to the evidence actually obtained.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the current branch.
