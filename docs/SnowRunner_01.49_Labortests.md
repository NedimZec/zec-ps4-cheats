# SnowRunner 01.49 · Windows- und PS4-Testprotokoll

**Ziel:** SnowRunner mit Title ID `CUSA17425`, Spielversion `01.49`, PS4 Pro, Firmware `14.00`, GoldHEN, offline. Dieser Branch enthält die Arbeitsdokumentation. Die sieben Schalter warten auf Messdaten und Hardware-Tests.

## Auf dem Windows-PC und der Konsole vorbereiten

1. Mit der [Installationsanleitung](Installation.md) den Spielstand auf USB sichern. Ein getrenntes Offline-Testprofil oder einen separaten Test-Spielstand verwenden. Spielversion, Firmware, GoldHEN-Build und Cheats-Manager-Version notieren. Weder ein Firmware-Update noch fremde SnowRunner-PKGs installieren.
2. Die PS4 und den Windows-PC ins gleiche private LAN bringen, wenn für eine bereits vorhandene, autorisierte Spielprozess-Debugging-Umgebung eine Verbindung nötig ist. Für den Einzelspielermodus den Internetzugang der Konsole trennen und ausschließlich lokal arbeiten. Keine Ports am Router freigeben.
3. Für Archiv und JSON Python 3.9 oder neuer aus einer bekannten Installation verwenden. Unter PowerShell im Projektordner zuerst `py -3 --version`, dann `py -3 -m unittest discover -s tests -v` und `py -3 tools/cheat_archive.py validate` ausführen.
4. Für die Spielprozessanalyse ist eine nachweislich kompatible, lokale Debugger-Verbindung erforderlich. Die offiziellen Hinweise für [PS4 Cheater Neo](https://github.com/avan06/PS4CheaterNeo/releases) und [PS4Debug-NG](https://github.com/Pharaoh2k/ps4debug-NG/releases/tag/1.3.3) stehen im [Abschlussbericht](Abschlussbericht.md). Die Kombination auf 14.00 ist für dieses Projekt noch ungeprüft. Vor der Verwendung eines offiziellen Downloads Quelle, genaue Version und gegebenenfalls veröffentlichte Signatur oder Prüfsumme prüfen. Falls die Verbindung zum eigenen SnowRunner-Spielprozess keine reine Leseprüfung erlaubt oder die Kombination einen Eingriff in Systemdateien erfordert, hier stoppen und den Fehler dokumentieren.

## Kandidaten ermitteln und verifizieren

Für die Portierung braucht es die exakte eigene 01.49-Spielbinary oder reproduzierbare Messungen aus dem laufenden eigenen Spielprozess. Den Prozess- und Modulnamen, die Build-Identität und nach Möglichkeit einen SHA-256 des eigenen Spielmoduls erfassen. Unter Windows ermittelt `Get-FileHash -Algorithm SHA256 -LiteralPath <Dateipfad>` die Prüfsumme einer bereits legal vorliegenden lokalen Datei. Für einen Bericht genügen Hash, Modulname, Spielversion und Befunde.

1. Pro Tabelle genau eine Aktion ausführen und den sichtbaren Wert vorher und nachher erfassen. In einem autorisierten Spielprozess-Debugger zunächst nur lesend nach wiederholbaren Wertänderungen suchen. Kandidaten mit einer Kontrollaktion prüfen, die den Wert unverändert lässt. Bei abgeleiteten Werten und Anzeige-Caches den tatsächlichen Spielzustand identifizieren.
2. Für einen reproduzierbaren Kandidaten die Stelle ermitteln, an der das Spiel den Wert aktualisiert. Alte Cheat-Namen und Wirkungen dienen zur Orientierung. Eine Portierung setzt voraus, dass der entsprechende Spielcode in 01.49 anhand Instruktionen, Aufrufern und Kontrollfluss eindeutig identifiziert ist. Direkt übernommene Offsets und globale Versionsverschiebungen sind dafür unzureichend.
3. Für einen isolierten Ein/Aus-Schalter Originalbytes des Ziel-Builds, Patchbytes, Modulbezug, bestätigten Offset und Begründung je Schreibstelle festhalten. Bei deaktiviertem Schalter müssen die tatsächlich veränderten Bytes vollständig wiederhergestellt werden. Nach einem Kaltstart die Zuordnung anhand des Moduls erneut prüfen. Bei gemeinsam genutzten Funktionen oder überschneidenden Schreibstellen die Abhängigkeit dokumentieren und die Schalter in beiden Reihenfolgen testen.
4. Kandidaten erst mit dem Ziel-Dateinamen `json/CUSA17425_01.49.json` im Entwicklungszweig ablegen, wenn echte Schreibstellen und Originalbytes vorliegen. Geld, XP und Rang können durch Autosave im separaten Testprofil erhalten bleiben. Die Schalterprüfung umfasst daher Laufzeitverhalten und die Frage, was nach Neuladen sichtbar bleibt.

## Testmatrix

| Cheat | Baseline und Aktion | Freigabekriterium |
| --- | --- | --- |
| Infinite Money | Geldstand notieren und Kauf, Verkauf sowie Belohnung getrennt auslösen. | Der dokumentierte Schutz gegen Ausgaben zeigt sich wiederholt. XP und Rang reagieren wie im Baseline-Test. Nach Ausschalten greifen die normalen Ausgaben. |
| Infinite Fuel | Mit einem Fahrzeug in vergleichbaren Bedingungen fahren. Tankstand vorher und nachher messen. | Aktiv sinkt der Tankstand bei normalem Verbrauchsvorgang nicht. Nach Deaktivierung sinkt er wieder. Fahrzeug- und Kartenwechsel testen. |
| No Vehicle Damage | Motor, Getriebe, Fahrwerk, Tank und Reifen jeweils über geeignete Spielereignisse prüfen. | Schäden bleiben in den zugesagten Kategorien aus und werden nach Deaktivierung wieder erfasst. Wirkungen auf schon bestehende Schäden dokumentieren. |
| Infinite Repair Points | Mit einem passenden Reparaturmodul mehrere Reparaturen nacheinander ausführen. | Reparaturen wirken und die Punkte werden aktiv nicht verbraucht. Nach Deaktivierung kehrt gewöhnlicher Verbrauch zurück. |
| Infinite Spare Tires | Mindestens zwei Reifenwechsel mit einem Fahrzeug mit Ersatzreifen durchführen. | Wechsel wirken und der Ersatzreifenzähler sinkt aktiv nicht. Nach Deaktivierung sinkt er wieder. |
| Max Experience (XP) | XP notieren und eine Belohnung auslösen. Geldwert separat beobachten. | Die verifizierte XP-Obergrenze ist erreichbar. Auslöser, Auswirkung auf Rang und Verhalten nach Deaktivierung sind dokumentiert. |
| Max Rank | Mit isoliertem Rang-Test den Wert vor und nach einer Fortschrittsaktion beobachten. | Höchster zulässiger Rang samt Freischaltungen. Falls Rang zwingend von XP abgeleitet wird, die Kopplung festhalten und keinen unabhängigen Rang-Schalter versprechen. |

Für jeden Kandidaten Ergebnis und Beleg erfassen. Dazu gehören Versionsdaten, Dateihash, Beobachtungsschritte, Anfangs- und Endwerte, Wirkung an/aus, Spielneustart, Save-Persistenz, 10 Minuten stabiler Betrieb und Kombinationstests bei gemeinsamen Pfaden. Anschließend das Import-ZIP zuerst mit ausgeschalteter Überschreiboption testen. Bei Absturz, abweichender Version oder fehlendem Nachweis bleibt der Kandidat im Entwicklungsbranch. Freigegebene Einträge aus der getesteten Datei auf `main` übernehmen, ZIP erneut prüfen und erst dann veröffentlichen.
