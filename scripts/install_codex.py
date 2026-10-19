"""Install only this fork's adaptations. Preview by default; no original backups."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile

REPO = Path(__file__).resolve().parents[1]
STATE_FILE = ".mattpocock-skills-fork.json"


def reject_links(path):
    """Check lexical ancestors before resolving, including Windows junctions."""
    for part in (path, *path.parents):
        if part.is_symlink() or (part.exists() and
                getattr(part.lstat(), "st_file_attributes", 0) & 0x400):
            raise ValueError(f"Linked/reparse path is unsupported: {part}")


def fingerprint(directory):
    reject_links(directory)
    if not directory.is_dir():
        raise ValueError(f"Expected a skill directory: {directory}")
    digest = hashlib.sha256()
    for path in sorted(directory.rglob("*")):
        reject_links(path)
        if path.is_dir():
            continue
        if not stat.S_ISREG(path.stat().st_mode):
            raise ValueError(f"Unsupported file: {path}")
        digest.update(path.relative_to(directory).as_posix().encode())
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def read_json(path, default):
    reject_links(path)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def atomic_json(path, value):
    handle, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def plan_install(repo, target):
    if not target.is_absolute():
        raise ValueError("--target-root must be absolute")
    if ".." in target.parts or target == Path(target.anchor):
        raise ValueError("Unsafe target root")
    reject_links(target)
    fork = read_json(repo / "fork.json", {})
    names = fork["adaptedSkills"] + fork["addedSkills"]
    if len(set(names)) != len(names) or not names:
        raise ValueError("Duplicate or empty skill selection")
    for name in names:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"Unsafe skill name: {name!r}")
    manifest = read_json(repo / ".claude-plugin/plugin.json", {})
    lock_path = target / ".skill-lock.json"
    lock = read_json(lock_path, {"version": 3, "skills": {}})
    if lock.get("version") != 3 or not isinstance(lock.get("skills"), dict):
        raise ValueError("Unsupported .skill-lock.json format; expected version 3")
    state = read_json(target / STATE_FILE, {"version": 1, "repository": fork["repository"], "skills": {}})
    if (state.get("version") != 1 or state.get("repository") != fork["repository"]
            or not isinstance(state.get("skills"), dict)):
        raise ValueError("Unsupported fork installation record")
    reject_links(target / "skills")
    entries = []
    for name in names:
        source = repo / "skills/engineering" / name
        if f"./skills/engineering/{name}" not in manifest["skills"]:
            raise ValueError(f"Selected skill missing from manifest: {name}")
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing source skill: {name}")
        desired = fingerprint(source)
        destination = target / "skills" / name
        reject_links(destination)
        record = lock["skills"].get(name)
        if record is not None and (not isinstance(record, dict) or record.get("source") != "mattpocock/skills"):
            raise ValueError(f"{name}: owned by another installer source; resolve that collision first")
        current = fingerprint(destination) if destination.exists() else None
        if current is not None and current != desired:
            if name in state["skills"]:
                if current != state["skills"][name]:
                    raise ValueError(f"{name}: installed fork has local edits; reconcile them in the checkout first")
            elif record is None:
                raise ValueError(f"{name}: untracked existing skill; ownership must be resolved first")
        entries.append({"name": name, "source": source, "destination": destination,
                        "hash": desired, "current": current,
                        "action": "unchanged" if current == desired else "replace" if current else "add"})
    return {"fork": fork, "entries": entries, "lock": lock, "lock_exists": lock_path.exists(),
            "lock_bytes": lock_path.read_bytes() if lock_path.exists() else None,
            "state_bytes": (target / STATE_FILE).read_bytes() if (target / STATE_FILE).exists() else None}


def install(repo, target, apply=False):
    plan = plan_install(repo, target)
    print(f"{'Apply' if apply else 'Preview'}: {target}")
    for entry in plan["entries"]:
        suffix = "; remove upstream update record" if entry["name"] in plan["lock"]["skills"] else ""
        print(f"  {entry['action']}: {entry['name']}{suffix}")
    print("Only the listed skills change. No backups of original skills are created.")
    if not apply:
        return plan
    target.mkdir(parents=True, exist_ok=True)
    (target / "skills").mkdir(exist_ok=True)
    completed = []
    try:
        # Stage and verify all new copies before deleting any original directory.
        with tempfile.TemporaryDirectory(prefix=".fork-stage-", dir=target) as stage:
            for entry in plan["entries"]:
                if entry["action"] != "unchanged":
                    staged = Path(stage) / entry["name"]
                    shutil.copytree(entry["source"], staged)
                    if fingerprint(staged) != entry["hash"]:
                        raise ValueError(f"Source changed during staging: {entry['name']}")
            # Recheck the whole target before the first replacement.
            fresh = plan_install(repo, target)
            if ([(e["current"], e["hash"]) for e in fresh["entries"]] !=
                    [(e["current"], e["hash"]) for e in plan["entries"]]
                    or fresh["lock_bytes"] != plan["lock_bytes"]
                    or fresh["state_bytes"] != plan["state_bytes"]):
                raise ValueError("Target or source changed during staging; rerun preview")
            for entry in plan["entries"]:
                if entry["action"] == "unchanged":
                    continue
                destination = entry["destination"]
                reject_links(destination)
                if destination.exists():
                    shutil.rmtree(destination)
                (Path(stage) / entry["name"]).rename(destination)
                completed.append(entry["name"])
        atomic_json(target / STATE_FILE, {
            "version": 1, "repository": plan["fork"]["repository"],
            "branch": plan["fork"]["branch"],
            "skills": {e["name"]: e["hash"] for e in plan["entries"]},
        })
        removed = False
        for entry in plan["entries"]:
            if entry["name"] in plan["lock"]["skills"]:
                del plan["lock"]["skills"][entry["name"]]
                removed = True
        if removed:
            atomic_json(target / ".skill-lock.json", plan["lock"])
    except Exception as error:
        raise RuntimeError(f"Installation interrupted. Completed replacements: {completed}. "
                           "No originals were backed up. Fix the reported error and rerun preview/apply "
                           f"from this same checkout. Cause: {error}") from error
    print("Installed. Update these skills from this fork; other upstream records are preserved.")
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-root", type=Path, default=Path.home() / ".agents")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        install(REPO, args.target_root, args.apply)
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
