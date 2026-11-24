# Installation auf der PS4 Pro

Für SnowRunner CUSA17425 01.49 steht derzeit keine freigegebene Datei zum Installieren bereit. Die folgenden Schritte gelten für ein künftig geprüftes Paket.

## Konsole vorbereiten

1. In den Spielinformationen und im Cheats Manager Title ID `CUSA17425` und Spielversion `01.49` abgleichen. Firmware und GoldHEN-Version für das Testprotokoll notieren.
2. SnowRunner schließen. Unter **Einstellungen → Verwaltung der von der Anwendung gespeicherten Daten → Gespeicherte Daten im Systemspeicher → Auf USB-Speichergerät kopieren** die SnowRunner-Spielstände sichern. Die Kopie prüfen. Für Spieltests einen separaten Test-Spielstand oder ein eigenes lokales Testprofil verwenden.
3. Version des Cheats Managers notieren. Falls bereits Cheats vorhanden sind, über **Backup Cheats to .Zip (USB)** eine Kopie erstellen. **Overwrite Files on Update** für den ersten Test deaktivieren. Der geprüfte Manager v1.2.2 setzt diese Option ab Werk auf an. Es kommt jeweils auf den gleichen Dateipfad an. GoldHEN dokumentiert außerdem nur ein Cheat-Format pro Title ID und Spielversion.

[Sony zur PS4-Speicherverwaltung](https://www.playstation.com/en-ie/support/hardware/ps4-manage-storage-space/) · [GoldHEN-Menü und Pfade](https://github.com/GoldHEN/GoldHEN/blob/master/CHEATMENU.md) · [PS4 Cheats Manager v1.2.2](https://github.com/bucanero/PS4CheatsManager/tree/v1.2.2/source)

## USB-Import

1. Unter Windows aus einem Checkout von `main` mit mindestens einer freigegebenen Cheat-Datei das Archiv bauen und prüfen.

   ```powershell
   py -3 tools/cheat_archive.py pack dist/cheats-zec.zip
   py -3 tools/cheat_archive.py check-zip dist/cheats-zec.zip
   ```

2. `cheats-zec.zip` ins Stammverzeichnis des USB-Sticks kopieren. Der geprüfte Manager erkennt den Dateinamen anhand des Präfixes `cheats`.
3. Im **PS4 Cheats Manager** unter **Update Cheats, Patches, Plugins** den USB-Eintrag wählen und **Update Cheats from USB (cheats-zec.zip)** starten. Bei einer bestehenden Datei gleichen Namens zunächst deren Inhalt und Sicherung prüfen. Nur für ein bewusstes Update des gesicherten Cheat-Files die Überschreiboption einschalten.
4. Manager und Spiel bei Bedarf neu öffnen. SnowRunner offline starten, das GoldHEN-Cheat-Menü mit langem Druck auf **SHARE** öffnen und Schalter mit **X** bedienen. Die erste Runde mit genau einem aktiven Schalter und dem separaten Test-Spielstand durchführen.

Einzeldatei-Alternative im eigenen lokalen Netz. Eine freigegebene JSON kann per lokalem FTP nach `/user/data/GoldHEN/cheats/json/` übertragen werden. Vorher im Zielordner nach einem gleichnamigen Eintrag und in `shn/` und `mc4/` nach derselben Title ID und Version sehen. Nur die Cheat-Datei übertragen. Das GitHub-Quellarchiv ist der Download für den Projektcode.

## Spätere Aktualisierung über GitHub

Für PS4 Cheats Manager v1.2.2 kann bei einer künftigen Freigabe ein geprüftes Paket manuell als Release-Asset `main.zip` hochgeladen werden. Es enthält `json/`, `shn/` oder `mc4/` direkt im Stamm und nur freigegebene Dateien. Unter **Settings → Change Update Download URLs** ist die Cheats-Basis `https://github.com/NedimZec/zec-ps4-cheats/releases/latest/download/` vorgesehen. Der Manager hängt `main.zip` an. Danach unter **Internet → Update Cheats from GitHub** auslösen. Die GitHub-Weiterleitung wird vom HTTP-Code des Managers verfolgt. Diese Release-Adresse ist für ein künftiges Paket vorgesehen und wurde auf einer PS4 noch nicht getestet. Die **Online Database** für einzelne Upstream-Einträge ist eine getrennte Funktion. [PS4 Cheats Manager v1.2.2](https://github.com/bucanero/PS4CheatsManager/tree/v1.2.2/source)
