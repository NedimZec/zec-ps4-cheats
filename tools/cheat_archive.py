"""Validate ZEC cheat files and build an archive for PS4 Cheats Manager."""

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile

FORMATS = ("json", "shn", "mc4")
FILENAME = re.compile(r"(CUSA[0-9]{5})_([0-9]{2}\.[0-9]{2})\.(json|shn|mc4)")
HEX = re.compile(r"[0-9A-Fa-f]+")
ROOT = Path(__file__).resolve().parents[1]


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Doppelter JSON-Schlüssel: {key}")
        result[key] = value
    return result


def validate_json(data, title, version):
    document = json.loads(data.decode("utf-8"), object_pairs_hook=unique_keys)
    if not isinstance(document, dict):
        raise ValueError("JSON-Wurzel muss ein Objekt sein.")
    if (document.get("id"), document.get("version")) != (title, version):
        raise ValueError("id/version stimmen nicht mit dem Dateinamen überein.")
    for key in ("name", "process"):
        value = document.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key} muss Text enthalten.")
    credits = document.get("credits")
    if not isinstance(credits, list) or not credits or any(
        not isinstance(author, str) or not author.strip() for author in credits
    ):
        raise ValueError("credits muss mindestens einen Autor enthalten.")
    mods = document.get("mods")
    if not isinstance(mods, list) or not mods:
        raise ValueError("mods muss mindestens einen Cheat enthalten.")
    names = set()
    for mod in mods:
        if not isinstance(mod, dict) or not isinstance(mod.get("name"), str):
            raise ValueError("Jeder Cheat braucht einen Namen.")
        name = mod["name"].strip()
        if not name or name.casefold() in names or mod.get("type") != "checkbox":
            raise ValueError(f"Erwartet eindeutigen Namen und type=checkbox: {name!r}")
        names.add(name.casefold())
        memory = mod.get("memory")
        if not isinstance(memory, list) or not memory:
            raise ValueError(f"{name}: memory fehlt oder ist leer.")
        for record in memory:
            if not isinstance(record, dict):
                raise ValueError(f"{name}: Speichereintrag muss ein Objekt sein.")
            for key in ("offset", "on", "off"):
                value = record.get(key)
                if not isinstance(value, str) or not HEX.fullmatch(value):
                    raise ValueError(f"{name}: {key} muss ein Hex-String sein.")
                if key != "offset" and len(value) % 2:
                    raise ValueError(f"{name}: {key} muss ganze Bytes enthalten.")


def validate_entry(name, data, seen):
    path = PurePosixPath(name)
    match = FILENAME.fullmatch(path.name)
    if not match:
        raise ValueError(f"Ungültiger Cheat-Dateiname: {name}")
    title, version, extension = match.groups()
    if name != f"{extension}/{path.name}" or not data:
        raise ValueError(f"Erwartet eine nichtleere Datei direkt unter {extension}/: {name}")
    key = (title, version)
    if key in seen:
        raise ValueError(f"Doppelter Eintrag für {title} {version}.")
    seen.add(key)
    if extension == "json":
        try:
            validate_json(data, title, version)
        except ValueError as error:
            raise ValueError(f"{name}: {error}") from error


def collect_files(source):
    entries = []
    seen = set()
    for folder in FORMATS:
        directory = source / folder
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError(f"Verzeichnis fehlt oder ist ein Symlink: {directory}")
        for path in sorted(directory.iterdir()):
            if path.name == ".gitkeep" and path.is_file() and not path.is_symlink() and not path.stat().st_size:
                continue
            if not path.is_file() or path.is_symlink():
                raise ValueError(f"Erwartet eine reguläre Cheat-Datei: {path}")
            name = f"{folder}/{path.name}"
            data = path.read_bytes()
            validate_entry(name, data, seen)
            entries.append((name, data))
    return entries


def build_archive(source, output):
    entries = collect_files(source)
    if not entries:
        raise ValueError("Keine Cheat-Datei vorhanden. Es wird kein Import-ZIP erstellt.")
    if output.suffix != ".zip":
        raise ValueError("Der Ausgabepfad muss mit .zip enden.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "x", compression=ZIP_DEFLATED) as archive:
        for name, data in entries:
            archive.writestr(name, data)
    return len(entries)


def check_archive(path):
    seen = set()
    with ZipFile(path) as archive:
        for entry in archive.infolist():
            if entry.is_dir():
                if entry.filename not in {f"{folder}/" for folder in FORMATS}:
                    raise ValueError(f"Unerwarteter ZIP-Ordner: {entry.filename}")
                continue
            validate_entry(entry.filename, archive.read(entry), seen)
    if not seen:
        raise ValueError("ZIP enthält keine Cheat-Dateien.")
    return len(seen)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("--source", type=Path, default=ROOT)
    pack = commands.add_parser("pack")
    pack.add_argument("output", type=Path)
    pack.add_argument("--source", type=Path, default=ROOT)
    check = commands.add_parser("check-zip")
    check.add_argument("archive", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            print(f"Struktur geprüft. Cheat-Dateien: {len(collect_files(args.source))}")
        elif args.command == "pack":
            count = build_archive(args.source, args.output)
            print(f"ZIP erstellt. Cheat-Dateien: {count}")
        else:
            print(f"ZIP geprüft. Cheat-Dateien: {check_archive(args.archive)}")
    except (OSError, ValueError, BadZipFile, RuntimeError) as error:
        print(f"Fehler: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
