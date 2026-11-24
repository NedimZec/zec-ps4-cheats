# ZEC PS4 Cheat Database · Abschlussbericht V1.0

**Stand 24. November 2026.** Zielsystem ist eine PS4 Pro mit Firmware 14.00 und GoldHEN. Getestet werden soll SnowRunner `CUSA17425`, Version `01.49`, im Offline-Einzelspielermodus.

## GitHub und Bereitstellung

Das Projekt liegt im öffentlichen Repository [NedimZec/zec-ps4-cheats](https://github.com/NedimZec/zec-ps4-cheats). Hauptbranch ist `main`. Die Analyse und lokale Testmatrix liegen im Branch `dev/snowrunner-01.49`. Die Arbeit verwendete kostenlose Werkzeuge und enthält keine GitHub-Actions-Workflows.

| Zweck | Adresse oder Status |
| --- | --- |
| Quellarchiv | [main.zip von GitHub](https://github.com/NedimZec/zec-ps4-cheats/archive/refs/heads/main.zip) |
| GoldHEN-Download | Noch kein Importpaket verfügbar. Für eine spätere Freigabe kann ein separat gepacktes `main.zip` als manuelles GitHub-Release-Asset dienen. |
| Offline-Import | Nach Freigabe per separat gepacktem `cheats-zec.zip` vom USB-Stick oder per einzeln übertragener JSON. |

Der GitHub-Download ist ein Quellarchiv mit dem Präfix `zec-ps4-cheats-main/`. Die beiden geprüften Extraktoren entfernen den ersten Ordner nur, wenn der Pfad mit `GoldHEN`, `patches` oder `cheats` beginnt. Die Pfade im ZEC-Quellarchiv werden deshalb übersprungen. Der aktuelle PS4 Cheats Manager bietet einen einstellbaren Download-Basispfad und hängt `main.zip` selbst an. Die archivierte GoldHEN-App verwendet einen fest eingebauten Standardpfad. Die Funktion für eine eigene Download-URL setzt daher einen passenden Manager und ein separat gepacktes Archiv voraus. [Quellcode v1.2.2](https://github.com/bucanero/PS4CheatsManager/tree/v1.2.2/source) · [Archivierte GoldHEN-App](https://github.com/GoldHEN/GoldHEN_Cheat_Manager)

## Recherche und Status der sieben Cheats

Die offizielle Datenbank wurde bei Commit `1d46700b3f84f80cb7f809cfec313eea0cc5a019` geprüft. Zu CUSA17425 gibt es JSON für 01.02 und 01.37 sowie SHN/MC4 für 01.37 und 01.40. CUSA17438 ist eine andere Title ID. PSXPatches führt 01.49 als Spielupdate zu CUSA17425. Ein Foreneintrag mit 1.49 im Titel dokumentiert die Nutzung einer 01.45-JSON mit einem modifizierten 01.45-Spielpatch und meldet einen Test auf Firmware 5.05. Der Eintrag nennt Reddevil82 und jwhy als Codeautoren. Die Dateinamen, die Build- und Firmwareangaben belegen keine Kompatibilität mit dem hier angefragten Setup. [Offizielle GoldHEN-Datenbank](https://github.com/GoldHEN/GoldHEN_Cheat_Repository/tree/1d46700b3f84f80cb7f809cfec313eea0cc5a019) · [PSXPatches](https://psxpatches.com/details/CUSA17425) · [Forum zum 01.45-Paket](https://www.gnoooo.com/thread-28914-1-1.html)

| Gewünschter Cheat | Ältere Referenz | Status für 01.49 |
| --- | --- | --- |
| Infinite Money | 01.40 nennt Max Money für die Kampagne mit gemeinsamem Mastercode für Geld und XP. | Offen. Dauerhaft unbegrenztes Geld und Schaltbarkeit getrennt von XP sind unbelegt. |
| Infinite Fuel | In 01.02, 01.37 und 01.40 aufgeführt. | Offen. Verbrauch und Rückkehr zum normalen Verbrauch auf 01.49 prüfen. |
| No Vehicle Damage | 01.37 und 01.40 nennen No Damage. Der 01.45-Forenfund nennt speziell Motorschutz. | Offen. Motor, Getriebe, Fahrwerk, Tank und Reifen getrennt prüfen. |
| Infinite Repair Points | 01.37 und 01.40 nennen Max Repair Points. Der 01.45-Forenfund nennt Infinite Repair Points. | Offen. Einen Maximalwert und ausbleibenden Verbrauch getrennt prüfen. |
| Infinite Spare Tires | Der 01.45-Forenfund nennt Infinite Spare Tires. | Offen. Verbrauch bei Reifenwechsel und Verhalten nach Fahrzeugwechsel prüfen. |
| Max Experience (XP) | 01.40 nennt Max XP für die Kampagne mit gemeinsamem Mastercode. Der 01.45-Forenfund nennt maxEXP. | Offen. XP-Grenze, Auslöser und Wechselwirkung mit Geld und Rang prüfen. |
| Max Rank | In den untersuchten älteren Dateien ist kein eigener Rang-Schalter aufgeführt. | Offen. Zuerst feststellen, ob Rang aus XP berechnet oder separat gespeichert wird. |

Die 01.02-JSON nennt TylerMods, die 01.37-JSON und die lesbaren 01.40-Metadaten Reddevil82. Das GoldHEN-Repository enthält den GPLv3-Lizenztext. In diesem Projekt wurden keine fremden Cheat-Dateien oder Patches übernommen. Für 01.49 lagen weder verifizierte Originalbytes und Modul-Offsets noch ein Hardware-Test vor. Die Zieldatei `json/CUSA17425_01.49.json` wird erst nach entsprechenden Funden und Tests erstellt. Historische Dateien enthalten 01.37- und 01.40-spezifische Angaben. Die gemeinsame Money/XP-Voraussetzung aus 01.40 ist ein konkreter Prüfpunkt für die gewünschte Unabhängigkeit. [Lizenz im GoldHEN-Repository](https://github.com/GoldHEN/GoldHEN_Cheat_Repository/blob/main/LICENSE)

## Windows-Werkzeuge und Firmware 14.00

| Werkzeug | Ergebnis |
| --- | --- |
| PS4 Cheater Neo 1.0.7.0 | Das Windows-Werkzeug verwendet eine PS4-Debugger-Anbindung. Die geprüften offiziellen Release-Angaben belegen die konkrete Kombination mit PS4Debug-NG auf Firmware 14.00 nicht. Die Verbindung wurde nicht praktisch getestet. |
| PS4Debug-NG 1.3.3 | Die Release-Notes nennen Unterstützung für Firmware 14.00. Das ist eine Herstellerangabe und kein Test auf der Zielkonsole. |
| Python 3 | Der Paketierer und Validator benötigen keine Zusatzpakete. Getestet in Linux. Dieselben Befehle sind für PowerShell dokumentiert. |

[PS4 Cheater Neo](https://github.com/avan06/PS4CheaterNeo) · [PS4Debug-NG 1.3.3](https://github.com/Pharaoh2k/ps4debug-NG/releases/tag/1.3.3)

## Tatsächlich ausgeführte Tests

| Test | Ergebnis |
| --- | --- |
| Offizielle Dateien zu CUSA17425 aufgelistet | Treffer für 01.02, 01.37 und 01.40. Kein Eintrag für 01.49 im geprüften Commit. |
| JSON-Struktur der offiziellen Dateien 01.02 und 01.37 geprüft | Beide entsprechen dem für dieses Projekt geprüften JSON-Aufbau. |
| `python3 -m unittest discover -s tests -v` | 9 von 9 Tests bestanden. Geprüft wurden Rundlauf, leere Datenbank, Dateiname/Version, Formatkollision, Hex-Bytes, JSON-Syntax, doppelte JSON-Schlüssel, GitHub-Präfix und unerwartete ZIP-Pfade. |
| `python3 tools/cheat_archive.py validate` | Verzeichnisstruktur gültig, 0 Cheat-Dateien. |
| Echter öffentlicher GitHub-Download | Download ohne Anmeldung erfolgreich. Der ZIP-Inhalt liegt unter `zec-ps4-cheats-main/`. |
| Originalfunktion `extract_zip_gh` aus PS4 Cheats Manager v1.2.2 mit dessen ZIP-Bibliothek unter Linux ausgeführt | Eine synthetische JSON direkt unter `json/` wurde importiert. Derselbe Inhalt unter `zec-ps4-cheats-main/json/` wurde übersprungen. Mit Überschreiben aus blieb die vorhandene Datei erhalten. Mit Überschreiben an wurde sie aktualisiert. |

Im Linux-Test wurden die PS4-Oberfläche und Konsolendienste durch lokale Funktionen ersetzt. Offen sind der reale Manager-Import auf der PS4 Pro, das Laden im GoldHEN-Menü, die Debugger-Verbindung, die Spielwirkung und die Stabilität aller sieben Schalter. Es wurden keine Dateien auf einer PS4 verändert und keine Spieldateien oder fremden Programme installiert.

## Nächster lokaler Test

Die [PS4-Installationsanleitung](Installation.md) beschreibt die Sicherung sowie USB- und Einzeldatei-Import. Das [Windows- und PS4-Protokoll im Entwicklungsbranch](https://github.com/NedimZec/zec-ps4-cheats/blob/dev/snowrunner-01.49/docs/SnowRunner_01.49_Labortests.md) enthält die einzelnen Spielaktionen und Freigabekriterien.
