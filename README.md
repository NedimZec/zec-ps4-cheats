# ZEC PS4 Cheat Database

Datenbank für GoldHEN auf der PS4. Alle Spieltests und Cheats sind für den Offline-Einzelspielermodus vorgesehen.

Der Stand V1.0 enthält die Repository-Struktur sowie einen Validator und ZIP-Paketierer. Für SnowRunner auf der PS4 Pro, Firmware 14.00, Title ID `CUSA17425`, Spielversion `01.49`, sind derzeit **0 von 7 Cheats freigegeben**.

## Projektdateien

| Pfad | Inhalt |
| --- | --- |
| `json/` | GoldHEN-JSON-Cheats |
| `shn/` | SHN-Cheats |
| `mc4/` | MC4-Cheats |
| `tools/` | Validator und ZIP-Paketierer |
| `docs/` | Abschlussbericht und PS4-Anleitung |
| `tests/` | Automatisierte Tests mit synthetischen Daten |

[Abschlussbericht V1.0](docs/Abschlussbericht.md) · [Installation und Updates](docs/Installation.md) · [Änderungen](CHANGELOG.md)

## Prüfung unter Windows

Mit Python 3.9 oder neuer im Repository-Ordner ausführen. Das Werkzeug verwendet die Python-Standardbibliothek.

```powershell
py -3 -m unittest discover -s tests -v
py -3 tools/cheat_archive.py validate
```

Sobald freigegebene Cheat-Dateien in `main` vorliegen, lässt sich daraus ein Importpaket erstellen.

```powershell
py -3 tools/cheat_archive.py pack dist/cheats-zec.zip
py -3 tools/cheat_archive.py check-zip dist/cheats-zec.zip
```

Der Paketierer verweigert ein leeres ZIP. Für JSON prüft er die ZEC-Konvention auf Basis publizierter GoldHEN-Beispiele. Für SHN und MC4 prüft er Dateiname, Formatordner und ob die Datei Inhalt hat. Die Funktionsprüfung erfolgt auf der Zielkonsole.

[GitHub-Quellarchiv](https://github.com/NedimZec/zec-ps4-cheats/archive/refs/heads/main.zip) · [Offizielles GoldHEN Cheat Repository](https://github.com/GoldHEN/GoldHEN_Cheat_Repository)
