import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", REPO / "scripts/install_codex.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.target = self.root / ".agents"
        self.names = json.loads((REPO / "fork.json").read_text())["adaptedSkills"] + ["ux-discovery"]
        for name in self.names:
            self.write(self.repo / "skills/engineering" / name / "SKILL.md", f"new {name}")
            if name != "ux-discovery":
                self.write(self.target / "skills" / name / "SKILL.md", f"old {name}")
                self.write(self.target / "skills" / name / "obsolete.md", "remove this old file")
        self.write(self.target / "skills/unrelated/SKILL.md", "leave unchanged")
        self.write_json(self.repo / "fork.json", json.loads((REPO / "fork.json").read_text()))
        self.write_json(self.repo / ".claude-plugin/plugin.json", {
            "skills": [f"./skills/engineering/{name}" for name in self.names]})
        self.lock = {"version": 3, "preferences": {"keep": True}, "skills": {
            name: {"source": "mattpocock/skills", "installedAt": "preserve"} for name in self.names[:-1]}}
        self.lock["skills"]["unrelated"] = {"source": "someone/else", "extra": 42}
        self.write_json(self.target / ".skill-lock.json", self.lock)

    def write(self, path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def write_json(self, path, value):
        self.write(path, json.dumps(value))

    def run_install(self, apply=True):
        with contextlib.redirect_stdout(io.StringIO()):
            return installer.install(self.repo, self.target, apply)

    def snapshot(self):
        return {str(p.relative_to(self.target)): p.read_bytes()
                for p in self.target.rglob("*") if p.is_file()}

    def test_preview_has_no_writes(self):
        before = self.snapshot()
        self.assertEqual(len(self.run_install(False)["entries"]), 9)
        self.assertEqual(self.snapshot(), before)
        self.target = self.root / "not-created"
        self.run_install(False)
        self.assertFalse(self.target.exists())

    def test_replace_only_selected_without_backups_and_preserve_other_metadata(self):
        self.run_install()
        for name in self.names:
            self.assertEqual((self.target / "skills" / name / "SKILL.md").read_text(), f"new {name}")
            self.assertFalse((self.target / "skills" / name / "obsolete.md").exists())
        self.assertEqual((self.target / "skills/unrelated/SKILL.md").read_text(), "leave unchanged")
        lock = json.loads((self.target / ".skill-lock.json").read_text())
        self.assertEqual(lock, {**self.lock, "skills": {"unrelated": self.lock["skills"]["unrelated"]}})
        self.assertEqual({p.name for p in self.target.iterdir()},
                         {"skills", ".skill-lock.json", installer.STATE_FILE})
        self.assertFalse(any(b"old " in data for data in self.snapshot().values()))

    def test_repeat_and_update(self):
        self.run_install()
        before = self.snapshot()
        self.run_install()
        self.assertEqual(self.snapshot(), before)
        self.write(self.repo / "skills/engineering/prototype/SKILL.md", "updated prototype")
        self.run_install()
        self.assertEqual((self.target / "skills/prototype/SKILL.md").read_text(), "updated prototype")

    def test_local_edits_block_entire_update(self):
        self.run_install()
        self.write(self.target / "skills/prototype/SKILL.md", "user changes")
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "local edits"):
            self.run_install()
        self.assertEqual(self.snapshot(), before)

    def test_foreign_owner_and_unknown_collision_block_before_changes(self):
        for record in ({"source": "someone/else"}, None):
            with self.subTest(record=record):
                lock = json.loads(json.dumps(self.lock))
                if record is None:
                    del lock["skills"]["prototype"]
                else:
                    lock["skills"]["prototype"] = record
                self.write_json(self.target / ".skill-lock.json", lock)
                before = self.snapshot()
                with self.assertRaises(ValueError):
                    self.run_install()
                self.assertEqual(self.snapshot(), before)

    def test_unsupported_lock_is_preserved(self):
        self.write_json(self.target / ".skill-lock.json", {"version": 99, "skills": {}})
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "Unsupported"):
            self.run_install()
        self.assertEqual(self.snapshot(), before)

    def test_unsafe_name_and_relative_target_are_rejected(self):
        fork = json.loads((self.repo / "fork.json").read_text())
        fork["addedSkills"] = ["../outside"]
        self.write_json(self.repo / "fork.json", fork)
        with self.assertRaisesRegex(ValueError, "Unsafe skill name"):
            self.run_install()
        with self.assertRaisesRegex(ValueError, "absolute"):
            installer.plan_install(self.repo, Path("relative"))

    def test_stage_failure_preserves_originals(self):
        before = self.snapshot()
        with patch.object(installer.shutil, "copytree", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(RuntimeError, "Completed replacements: \\[\\]"):
                self.run_install()
        self.assertEqual(self.snapshot(), before)

    def test_metadata_failure_can_retry_same_checkout(self):
        with patch.object(installer, "atomic_json", side_effect=OSError("metadata locked")):
            with self.assertRaisesRegex(RuntimeError, "metadata locked"):
                self.run_install()
        self.run_install()
        self.assertTrue((self.target / installer.STATE_FILE).exists())
        self.assertEqual(set(json.loads((self.target / ".skill-lock.json").read_text())["skills"]), {"unrelated"})

    def test_reparse_paths_are_rejected(self):
        class Reparse:
            st_file_attributes = 0x400
        with patch.object(Path, "lstat", return_value=Reparse()), patch.object(Path, "is_symlink", return_value=False):
            with self.assertRaisesRegex(ValueError, "reparse"):
                installer.reject_links(self.target)


if __name__ == "__main__":
    unittest.main()
