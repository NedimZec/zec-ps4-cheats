"""Synthetic fixtures exercise validation only and are never published as cheats."""

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from tools.cheat_archive import build_archive, check_archive, collect_files


class CheatArchiveTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for folder in ("json", "shn", "mc4"):
            (self.root / folder).mkdir()
        self.archive = self.root / "cheats-zec.zip"
        self.entry = "json/CUSA00000_01.00.json"
        self.fixture = {
            "name": "Synthetic test",
            "id": "CUSA00000",
            "version": "01.00",
            "process": "test.bin",
            "credits": ["Test fixture"],
            "mods": [{
                "name": "Test toggle", "type": "checkbox",
                "memory": [{"offset": "0", "on": "00", "off": "01"}],
            }],
        }

    def write_fixture(self):
        (self.root / self.entry).write_text(json.dumps(self.fixture), encoding="utf-8")

    def test_round_trip_at_zip_root(self):
        self.write_fixture()
        self.assertEqual(build_archive(self.root, self.archive), 1)
        self.assertEqual(check_archive(self.archive), 1)
        with ZipFile(self.archive) as archive:
            self.assertEqual(archive.namelist(), [self.entry])
        with self.assertRaises(FileExistsError):
            build_archive(self.root, self.archive)

    def test_empty_database_does_not_create_import_archive(self):
        (self.root / "json" / ".gitkeep").touch()
        self.assertEqual(collect_files(self.root), [])
        with self.assertRaisesRegex(ValueError, "Keine Cheat-Datei"):
            build_archive(self.root, self.archive)
        self.assertFalse(self.archive.exists())

    def test_title_and_version_must_match_filename(self):
        self.fixture["version"] = "01.02"
        self.write_fixture()
        with self.assertRaisesRegex(ValueError, "id/version"):
            collect_files(self.root)

    def test_different_formats_for_same_version_are_rejected(self):
        self.write_fixture()
        (self.root / "shn" / "CUSA00000_01.00.shn").write_bytes(b"synthetic")
        with self.assertRaisesRegex(ValueError, "Doppelter Eintrag"):
            collect_files(self.root)

    def test_incomplete_hex_byte_is_rejected(self):
        self.fixture["mods"][0]["memory"][0]["off"] = "A"
        self.write_fixture()
        with self.assertRaisesRegex(ValueError, "ganze Bytes"):
            collect_files(self.root)

    def test_invalid_json_syntax_is_rejected(self):
        (self.root / self.entry).write_text("{", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Expecting"):
            collect_files(self.root)

    def test_duplicate_json_keys_are_rejected(self):
        (self.root / self.entry).write_text('{"id": "a", "id": "b"}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Doppelter JSON-Schlüssel"):
            collect_files(self.root)

    def test_github_wrapper_is_rejected(self):
        with ZipFile(self.archive, "w") as archive:
            archive.writestr(f"zec-ps4-cheats-main/{self.entry}", json.dumps(self.fixture))
        with self.assertRaisesRegex(ValueError, "direkt unter"):
            check_archive(self.archive)

    def test_traversal_in_archive_is_rejected(self):
        with ZipFile(self.archive, "w") as archive:
            archive.writestr(f"../{self.entry}", json.dumps(self.fixture))
        with self.assertRaisesRegex(ValueError, "direkt unter"):
            check_archive(self.archive)
