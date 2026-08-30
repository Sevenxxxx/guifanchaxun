import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "tools" / "guifan-chaxun-scripts" / "scripts" / "spec.py"
MODULE_SPEC = importlib.util.spec_from_file_location("guifan_spec", SPEC_PATH)
spec = importlib.util.module_from_spec(MODULE_SPEC)
# These safety tests only cover filesystem/index metadata helpers.  Stub the
# optional runtime dependency so they can run before PDF dependencies are set up.
sys.modules.setdefault("fitz", types.ModuleType("fitz"))
MODULE_SPEC.loader.exec_module(spec)


class IndexSafetyTests(unittest.TestCase):
    def test_same_stem_in_nested_directories_gets_distinct_stable_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sources = [root / "a" / "same.txt", root / "b" / "a" / "same.txt"]
            for source in sources:
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_text("内容", encoding="utf-8")
            cfg = {"library_dir": str(root)}
            plan = spec.plan_book_ids(sources, cfg, {"books": []})
            self.assertEqual(len(plan), 2)
            self.assertEqual(len(set(plan.values())), 2)
            self.assertEqual(plan, spec.plan_book_ids(list(reversed(sources)), cfg, {"books": []}))

    def test_status_reports_changed_source_using_precise_signature(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            library, data = root / "library", root / "data"
            library.mkdir()
            data.mkdir()
            source = library / "book.txt"
            source.write_text("first", encoding="utf-8")
            sig = spec.source_signature(source)
            shelf = {"schema_version": 1, "books": [{
                "id": "book", "file": "book.txt", "title": "book", "std_no": "",
                "source_mtime_ns": sig["mtime_ns"] - 1, "source_size": sig["size"],
            }]}
            (data / "bookshelf.json").write_text(json.dumps(shelf), encoding="utf-8")
            cfg = {"library_dir": str(library), "data_dir": str(data)}
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                spec.cmd_status(SimpleNamespace(), cfg)
            self.assertIn("[更新] book.txt", output.getvalue())

    def test_superseded_target_must_exist_and_not_be_self(self):
        with tempfile.TemporaryDirectory() as tmp:
            data = Path(tmp)
            shelf = {"books": [{"id": "old", "file": "old.txt", "title": "old", "std_no": ""}]}
            (data / "bookshelf.json").write_text(json.dumps(shelf), encoding="utf-8")
            cfg = {"data_dir": str(data)}
            with self.assertRaises(SystemExit):
                spec.cmd_remove(SimpleNamespace(book="old", mark_superseded="missing"), cfg)
            with self.assertRaises(SystemExit):
                spec.cmd_remove(SimpleNamespace(book="old", mark_superseded="old"), cfg)

    def test_atomic_write_replaces_complete_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "value.txt"
            spec.atomic_write_text(path, "first")
            spec.atomic_write_text(path, "second")
            self.assertEqual(path.read_text(encoding="utf-8"), "second")
            self.assertEqual(list(path.parent.glob("*.tmp")), [])


if __name__ == "__main__":
    unittest.main()
