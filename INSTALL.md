# Local installation for this fork

This fork keeps the original skill names. Use one active source per name. Its stable maintained branch is `main`; the original project remains available through the `upstream` remote and Git history. Product Design is a separate plugin dependency for visual work, not bundled or installed by this package.

The supported local route is Python 3.10+ and Git, without extra Python packages. Clone the maintained branch, preview the exact target changes, then apply them:

```powershell
git clone --branch main https://github.com/rtellez91/mattpocock-skills-fork.git
Set-Location mattpocock-skills-fork
python scripts/install_codex.py
python scripts/install_codex.py --apply
```

The default target is the current user's `.agents` directory. Use `--target-root <absolute-path-to-.agents>` to choose another scope. Preview is read-only. Apply replaces only the eight adapted skills and adds `ux-discovery`, as listed in `fork.json`. It creates no backups of the originals. Unmodified upstream skills and unrelated skills remain untouched.

This is an overlay on an existing Matt Pocock skills installation, not a standalone installation of every upstream skill. Keep the original dependencies used by your workflows installed (for example `grilling`, `domain-modeling`, `tdd`, and `code-review`). The installer supports original copies tracked by skills.sh in a version 3 `.skill-lock.json`. It removes only the nine selected names from that updater's records. Other records and metadata remain. A separate `.mattpocock-skills-fork.json` records ownership and content hashes for subsequent fork updates.

Installed files are deployment copies; edit and review the versioned repository, then reinstall. The installer refuses foreign or unknown ownership, changed managed copies, linked paths, and unsupported lock formats instead of silently overwriting them. All new copies are staged and verified before replacement. Do not run another installer concurrently. A filesystem failure during replacement can leave a partial installation: the error reports completed replacements, and you must inspect that state before retrying from the same checkout. This procedure is not a transactional rollback system.

If Matt's managed plugin is also enabled, disable that overlapping plugin before using these local copies. The installer does not change plugin settings or Codex configuration. Check project-local skills too: Codex does not merge duplicate names. Keep the Product Design plugin enabled for visual workflows. Do not run the upstream `scripts/link-skills.sh` for this installation.

Codex normally detects changed skills automatically; restart it if they do not appear. Start a fresh chat and verify `ux-discovery` is available and the adapted entry points describe Product Design and design readiness.

## Updating

Review the fork's changes, then fast-forward your local checkout and reapply:

```powershell
git pull --ff-only origin main
python scripts/install_codex.py
python scripts/install_codex.py --apply
```

Use this route for the fork's skills. `npx skills update` no longer owns the entries migrated by the installer. Reinstalling them explicitly from `mattpocock/skills` would opt back into the upstream copies. A future switch to a managed plugin or a different installer is a separate migration, not an additional installation on top.

There is no backup or restore command. The original versions remain available in upstream Git history if you later choose to reinstall them.

## Maintaining this fork

Develop changes on task branches and open pull requests into this fork's `main`. Merge only after review and relevant validation; update installations from `main` after the merge. The inherited release workflow targets pushes to `main` and uses Changesets to propose version updates or tag versions when GitHub Actions is enabled.

## Maintainer updates from upstream

If the checkout has no `upstream` remote, add it once with `git remote add upstream https://github.com/mattpocock/skills.git`. Fetch `upstream`, inspect changes since `fork.json`'s recorded base, and merge normally into the maintained branch when ready. Preserve history. Resolve semantic changes in the interview, invocation, publication, and readiness contracts; do not just accept text merges. Recheck Product Design's installed contract separately. Run the repository checks and behavioral scenarios before publishing an update; then advance the recorded upstream base. Updates are deliberate, not automatic.

Sources: [Codex local skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills), [original Matt Pocock skills](https://github.com/mattpocock/skills).
