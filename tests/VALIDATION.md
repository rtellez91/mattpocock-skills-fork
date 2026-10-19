# Validation of the initial UX adaptation

Validated on 2026-10-19 against the upstream commit recorded in `fork.json`. The installer suite and packaging checks were rerun after restoring upstream documentation and removing distribution changes.

| Check | Result |
| --- | --- |
| `python -m unittest discover -s tests -p test_install_codex.py` | 10 tests passed in isolated temporary directories |
| `python scripts/validate_fork.py` | Passed: 28 promoted skills and nine scoped installation entries, packaging/version/catalog/docs/local-link and invocation checks |
| `node scripts/sync-plugin-version.mjs --check` | Passed, inherited version `1.3.1` |
| `git diff --check` | Passed |
| Read-only installer preview against the existing local installation | Seven replacements; additions of `implement-spec` and `ux-discovery`; no files installed |
| Claude Code 2.1.303, `plugin validate .claude-plugin/marketplace.json --strict` | Passed |
| Claude Code 2.1.303, `plugin validate .` | Passed with the root `CLAUDE.md` warning described below |
| Claude Code 2.1.303, required `plugin validate . --strict` | Failed because strict mode treats that warning as an error |
| Skill creator `quick_validate.py` | Passed for `ux-discovery` and `prototype`; rejected the seven user-invoked skills' existing `disable-model-invocation` field, which its allowlist does not recognize |

The root `CLAUDE.md` is inherited repository contributor guidance. Claude warns that a root instruction file is not loaded as installed plugin context. The adapted runtime instructions live in the skill directories, and the supported installation route is the scoped Codex overlay. The contributor file was retained intentionally. Original package, marketplace, author, version, release configuration, and lockfile metadata are preserved; only the new skill registration and test commands are added to the package/plugin files. README installation examples from upstream are retained and clearly identified as upstream reference, with the fork's scoped route linked separately.

The seven user-invoked skills preserve their upstream `disable-model-invocation: true` and Codex `allow_implicit_invocation: false` settings. They were not weakened to satisfy the generic validator. The fork packaging check verifies both settings. These limitations are not claims that all strict validation passed.

An independent agent applied the actual instructions to three scenarios: incomplete hosted sign-in evidence; reuse of a canonical component without new mockups; and a spec with one design-blocked ticket plus independent server work. It found the intended readiness gates and identified ambiguous all-layer slicing language, which was clarified to cover the layers required by each implementation deliverable.

That exercise was a read-only scenario walkthrough, not a live Product Design generation, browser prototype run, or empirical user study. The bridge was reviewed against installed Product Design 0.1.56. A live end-to-end exercise remains a follow-up when real product work needs it; it was not simulated by generating unrelated designs. No claim of runtime accessibility or production readiness follows from these checks.
