"""Check packaging invariants; this does not test agent behavior."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def validate():
    fork = json.loads((ROOT / "fork.json").read_text(encoding="utf-8"))
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    lock = json.loads((ROOT / "package-lock.json").read_text(encoding="utf-8"))
    assert package["name"] == plugin["name"] == fork["name"] == lock["name"] == lock["packages"][""]["name"]
    assert package["version"] == plugin["version"] == lock["version"] == lock["packages"][""]["version"]
    promoted = {f"./{p.parent.relative_to(ROOT).as_posix()}"
                for bucket in ("engineering", "productivity")
                for p in (ROOT / "skills" / bucket).glob("*/SKILL.md")}
    assert promoted == set(plugin["skills"]), "Promoted skill/manifest mismatch"
    assert len(promoted) == len(plugin["skills"]), "Duplicate manifest entry"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for path in promoted:
        directory = ROOT / path
        name = directory.name
        bucket = directory.parent.name
        assert f"skills/{bucket}/{name}/SKILL.md" in readme, f"Missing root catalog link: {name}"
        assert f"{name}/SKILL.md" in (directory.parent / "README.md").read_text(encoding="utf-8")
        assert (ROOT / "docs" / bucket / f"{name}.md").is_file(), f"Missing docs: {name}"
    selected = fork["adaptedSkills"] + fork["addedSkills"]
    assert len(selected) == len(set(selected)) == 9
    for name in selected:
        directory = ROOT / "skills/engineering" / name
        skill = (directory / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---", skill, re.S)
        assert frontmatter, f"Missing frontmatter: {name}"
        assert f"name: {name}\n" in frontmatter[1] + "\n"
        assert re.search(r"^description: .+", frontmatter[1], re.M)
        policy = (directory / "agents/openai.yaml").read_text(encoding="utf-8")
        if name not in ("ux-discovery", "prototype"):
            assert "disable-model-invocation: true" in frontmatter[1]
            assert "allow_implicit_invocation: false" in policy
        else:
            assert "disable-model-invocation: true" not in frontmatter[1]
            assert "allow_implicit_invocation: false" not in policy
        doc = (ROOT / "docs/engineering" / f"{name}.md").read_text(encoding="utf-8")
        for heading in ("What it does", "When to reach for it", "Common questions", "It's working if"):
            assert f"## {heading}" in doc, f"Missing {heading}: {name}"
        for source in list(directory.rglob("*.md")) + [ROOT / "docs/engineering" / f"{name}.md"]:
            text = source.read_text(encoding="utf-8")
            assert "\u2014" not in text, f"Em dash: {source}"
            # Code examples can contain placeholder Markdown, not navigable links.
            prose = re.sub(r"```.*?```|`[^`\n]+`", "", text, flags=re.S)
            for link in re.findall(r"\]\(([^)]+)\)", prose):
                if "://" in link or link.startswith("#"):
                    continue
                assert (source.parent / link.split("#")[0]).exists(), f"Broken local link: {source}: {link}"
    print(f"Packaging valid: {len(promoted)} promoted skills; {len(selected)} scoped installation entries.")


if __name__ == "__main__":
    validate()
