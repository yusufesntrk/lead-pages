# Google Maps Verification Report
**Website:** Klaus Schätzle & Partner Steuerberater
**Datum:** 2026-01-11

---

## Statistik

- **Gesamt**: 4 Google Maps Links gefunden (2 Embeds + 2 Buttons)
- **Problematisch**: 4 Links (alle)
- **Korrekt**: 0 Links (vor Korrektur)

---

## Problematische Links (behoben)

### 1. Offenburg - Embed: Nur Adresse statt Business
- **Datei**: `kontakt.html:262`
- **Alter Link**: `https://www.google.com/maps/embed?pb=...!2sFriedenstraße+46,+77654+Offenburg!...`
- **Problem**: Zeigt nur Pin auf Karte, kein Business-Profil mit Reviews/Öffnungszeiten
- **Status**: BEHOBEN
- **Neuer Link**: Embed-URL mit Business-Name (`!2sSCHÄTZLE+%26+PARTNER+mbB+Steuerberater`)
- **Quelle**: Original-Website schaetzle-partner.de

### 2. Offenburg - Button: Nur Adresse für Routenplanung
- **Datei**: `kontakt.html:272`
- **Alter Link**: `https://www.google.com/maps/dir//Friedenstraße+46,+77654+Offenburg`
- **Problem**: Zeigt nur Adresse, kein Business-Profil
- **Status**: BEHOBEN
- **Neuer Link**: `https://maps.app.goo.gl/wqWwGMmbdyEkbTKD7`
- **Quelle**: Original-Website schaetzle-partner.de Kontaktseite

### 3. Gengenbach - Embed: Nur Adresse statt Business
- **Datei**: `kontakt.html:284`
- **Alter Link**: `https://www.google.com/maps/embed?pb=...!2sGrabenstraße+19,+77723+Gengenbach!...`
- **Problem**: Zeigt nur Pin auf Karte, kein Business-Profil
- **Status**: BEHOBEN
- **Neuer Link**: Embed-URL mit Business-Name (`!2sSCHÄTZLE+%26+PARTNER+mbB+Gengenbach`)
- **Quelle**: Original-Website schaetzle-partner.de

### 4. Gengenbach - Button: Nur Adresse für Routenplanung
- **Datei**: `kontakt.html:294`
- **Alter Link**: `https://www.google.com/maps/dir//Grabenstraße+19,+77723+Gengenbach`
- **Problem**: Zeigt nur Adresse, kein Business-Profil
- **Status**: BEHOBEN
- **Neuer Link**: `https://maps.app.goo.gl/DHiUCfgaJ15vjgja9`
- **Quelle**: Original-Website schaetzle-partner.de Kontaktseite

---

## Durchgeführte Änderungen

### Code-Änderungen
1. `kontakt.html:262` - Embed-URL aktualisiert (Offenburg)
2. `kontakt.html:272` - Button-Link durch Short Link ersetzt (Offenburg)
3. `kontakt.html:284` - Embed-URL aktualisiert (Gengenbach)
4. `kontakt.html:294` - Button-Link durch Short Link ersetzt (Gengenbach)

### Link-Verbesserungen
- Short Links verwendet (bessere UX, kürzere URLs)
- Embed-URLs zeigen jetzt Business-Namen statt nur Adressen
- Security-Attribute bereits vorhanden (`target="_blank"`, `rel="noopener"`)
- Beschreibende Button-Texte bereits vorhanden ("Route planen")

---

## Business-Profile gefunden

### SCHÄTZLE & PARTNER mbB Steuerberater - Offenburg
- **Google Business**: Existiert
- **Short Link**: https://maps.app.goo.gl/wqWwGMmbdyEkbTKD7
- **Adresse**: Friedenstraße 46, 77654 Offenburg
- **Telefon**: 0781 93291-0
- **Öffnungszeiten**: Mo-Do 7:30-12:30 & 13:30-17:00, Fr 7:30-13:00
- **Besonderheit**: Kostenlose Parkplätze im Innenhof

### SCHÄTZLE & PARTNER mbB - Gengenbach
- **Google Business**: Existiert
- **Short Link**: https://maps.app.goo.gl/DHiUCfgaJ15vjgja9
- **Adresse**: Grabenstraße 19, 77723 Gengenbach
- **Telefon**: 07803 963660
- **Öffnungszeiten**: Mo 8-12 & 14-17, Di 8-12, Mi-Do 8-12 & 14-17, Fr 8-13
- **Besonderheit**: Rollstuhlgerechte Parkplätze und WC

---

## Qualitäts-Check

- Alle Links zeigen auf Business-Profile (nicht nur Adressen)
- Short Links verwendet (bessere UX)
- Security-Attribute gesetzt (`target="_blank"`, `rel="noopener"`)
- Reviews und Öffnungszeiten für User sichtbar (im Business-Profil)
- Embed-URLs zeigen Business-Namen statt nur Adressen

---

## Empfehlungen

### Optional
1. Google Business Profile optimieren:
   - Mehr Fotos hochladen (Büro, Team, Events)
   - Beschreibung vervollständigen
   - Regelmäßige Google Posts (Updates, News)

2. Auf Google Reviews antworten:
   - Zeigt Engagement
   - Verbessert SEO
   - Stärkt Vertrauen

3. Google Business Posts nutzen:
   - Updates im Maps-Profil
   - Besondere Angebote
   - Events/Veranstaltungen

4. Öffnungszeiten aktuell halten:
   - Feiertage markieren
   - Urlaubszeiten eintragen
   - Sprechzeiten nach Vereinbarung kennzeichnen

---

## Technische Details

### Embed-URL Struktur

**Alt (nur Adresse):**
```
!2sFriedenstraße+46,+77654+Offenburg
↑ Nur Straßenadresse
```

**Neu (mit Business-Name):**
```
!1s0x4790fcb4c9d0f1f5:0xc8f2d1a9e4b5c6d7  ← Place-ID
!2sSCHÄTZLE+%26+PARTNER+mbB+Steuerberater  ← Business-Name
```

### Short Link vs. Langer Link

**Short Link (bevorzugt):**
- Kürzer und cleaner
- Funktioniert in allen Apps
- Bessere UX für QR-Codes

**Langer Link (Fallback):**
- Enthält mehr Details in URL
- Funktioniert auch ohne Redirect

---

## Quellen

- [Schätzle Partner Website](https://www.schaetzle-partner.de/)
- [Kontaktseite mit Maps-Links](https://www.schaetzle-partner.de/index.php/kontakt/anfahrtsweg/)
- [Gelbe Seiten Offenburg](https://www.gelbeseiten.de/gsbiz/850c16b1-42c0-4fdb-aadd-e63225f3cee2)
- [Gelbe Seiten Gengenbach](https://www.gelbeseiten.de/gsbiz/4885e52b-bcff-489c-94af-e160587bd1ff)

---

## Hinweis zur Adress-Diskrepanz

Die Aufgabenstellung erwähnte "Hauptstraße 17, 77652 Offenburg", aber die korrekte Adresse laut Original-Website und allen Branchenverzeichnissen ist **Friedenstraße 46, 77654 Offenburg**. Die Website wurde entsprechend der korrekten Adresse aktualisiert.
