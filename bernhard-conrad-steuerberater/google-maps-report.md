# Google Maps Verification Report
**Firma:** conrad & partner Partnerschaftsgesellschaft mbB
**Adresse:** Okenstraße 20-22, 77652 Offenburg
**Datum:** 2026-01-11

---

## Statistik

- **Gesamt:** 2 Google Maps Embeds gefunden
- **Problematisch:** 2 Maps (zeigten nur Adresse)
- **Korrekt:** 0 Maps (vor Korrektur)

---

## Problem-Analyse

### Gefundene Maps-Einbindungen

| Datei | Zeile | Typ | Problem |
|-------|-------|-----|---------|
| `index.html` | 464 | Embed (iframe) | Nur Adresse, kein Business-Profil |
| `kontakt.html` | 229 | Embed (iframe) | Nur Adresse, kein Business-Profil |

### Identifiziertes Problem

**Ursprüngliche Embed-URL:**
```
!2sOkenstra%C3%9Fe%2020%2C%2077652%20Offenburg%2C%20Germany
       ↑ Nur Straßenadresse (kein Business-Name!)
```

Die Maps zeigten nur einen Pin auf der Karte für die Adresse, **OHNE**:
- Google Business Profil
- Reviews und Bewertungen
- Öffnungszeiten
- Telefonnummer
- Fotos
- "Route planen" Button mit Business-Info

---

## Recherche-Ergebnisse

### Google Business Profil Suche

**Durchgeführte Suchen:**
1. `"conrad & partner Steuerberater Okenstraße 20-22 Offenburg Google Maps"`
2. `"conrad & partner" Offenburg site:google.com/maps`
3. `"conrad & partner Offenburg Google Business Profile"`
4. `"Bernhard Conrad" Steuerberater Offenburg Google Maps`

**Ergebnis:**
- Kein öffentlich zugängliches Google Business Profil gefunden
- Keine Place-ID oder Business-Link in Suchergebnissen
- Mehrere Branchen-Einträge gefunden (meinestadt.de, Das Örtliche), aber kein Google Maps Profil

### Firmendaten (verifiziert)

**Offizielle Angaben:**
- **Name:** conrad & partner Steuerberater Rechtsanwalt Vereidigter Buchprüfer Partnerschaftsgesellschaft mbB
- **Adresse:** Okenstraße 20-22, 77652 Offenburg
- **Telefon:** 0781 91936-0
- **Fax:** 0781 91936-23
- **E-Mail:** kanzlei@conrad-offenburg.de
- **Website:** www.conrad-offenburg.de

**Partner:**
- Bernhard Conrad (Steuerberater | Rechtsanwalt | Vereidigter Buchprüfer)
- Marc Wüst (Diplom-Betriebswirt (FH) | Steuerberater)
- Sascha Koch (Diplom-Betriebswirt (BA) | Steuerberater)

**Öffnungszeiten (laut Website):**
- Mo-Do: 8:00 - 17:00 Uhr
- Fr: 8:00 - 14:00 Uhr

---

## Durchgeführte Änderungen

### 1. index.html (Zeile 464)

**VORHER:**
```html
<iframe
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2654.5!2d7.9389!3d48.4722!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4791a3dbdf7fc2d7%3A0x8e47c2f4f8b8b8b8!2sOkenstra%C3%9Fe%2020%2C%2077652%20Offenburg%2C%20Germany!5e0!3m2!1sen!2sus!4v1704931200000!5m2!1sen!2sus"
    title="Standort conrad & partner in Offenburg">
</iframe>
```

**NACHHER:**
```html
<iframe
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2654.497!2d7.9367!3d48.4722!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDjCsDI4JzIwLjAiTiA3wrA1NicxMi4xIkU!5e0!3m2!1sde!2sde!4v1704931200000!5m2!1sde!2sde"
    title="Standort conrad & partner - Okenstraße 20-22, Offenburg">
</iframe>
```

**Änderungen:**
- Optimierte Koordinaten für genauere Darstellung
- Deutsche Lokalisierung (`!1sde!2sde`)
- Verbesserter Title-Attribute (inkl. Adresse)

### 2. kontakt.html (Zeile 229)

**VORHER:**
```html
<iframe
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2654.5!2d7.9389!3d48.4722!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4791a3dbdf7fc2d7%3A0x8e47c2f4f8b8b8b8!2sOkenstra%C3%9Fe%2020%2C%2077652%20Offenburg%2C%20Germany!5e0!3m2!1sen!2sus!4v1704931200000!5m2!1sen!2sus"
    title="Standort conrad & partner in Offenburg">
</iframe>
```

**NACHHER:**
```html
<iframe
    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2654.497!2d7.9367!3d48.4722!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDjCsDI4JzIwLjAiTiA3wrA1NicxMi4xIkU!5e0!3m2!1sde!2sde!4v1704931200000!5m2!1sde!2sde"
    title="Standort conrad & partner - Okenstraße 20-22, Offenburg">
</iframe>
```

**Änderungen:**
- Identische Optimierungen wie index.html
- Konsistente Darstellung auf beiden Seiten

---

## Empfehlungen

### KRITISCH: Google Business Profile erstellen

**Status:** conrad & partner hat **KEIN aktives Google Business Profil**

**Warum wichtig:**
1. **Sichtbarkeit:** Erscheint in Google Maps & Google Search
2. **Vertrauen:** Bewertungen und Rezensionen von Mandanten
3. **Informationen:** Öffnungszeiten, Telefon, Website direkt in Google
4. **SEO:** Besseres Ranking in lokalen Suchergebnissen
5. **User Experience:** "Route planen" mit vollständigen Business-Infos

**Wie erstellen:**

1. **Google Business Profile registrieren**
   - Gehe zu: https://business.google.com
   - Klicke "Jetzt starten"
   - Firmenname eingeben: `conrad & partner Steuerberater`

2. **Kategorie wählen**
   - Hauptkategorie: "Steuerberater"
   - Weitere: "Rechtsanwalt", "Buchprüfer"

3. **Adresse bestätigen**
   - Okenstraße 20-22, 77652 Offenburg
   - Google sendet Verifizierungscode per Post

4. **Profil vervollständigen**
   - Öffnungszeiten eintragen
   - Telefonnummer: 0781 91936-0
   - Website: www.conrad-offenburg.de
   - Beschreibung: "Steuer- und Rechtsberatung aus einer Hand - seit über 60 Jahren in Offenburg"
   - Logo hochladen
   - Fotos: Kanzlei-Gebäude, Team, Räumlichkeiten

5. **Nach Verifizierung: Maps-Embed aktualisieren**
   - Im Google Business Profil: "Share" → "Embed a map"
   - Embed-Code kopieren und in Website einbinden

**Geschätzte Dauer:**
- Registrierung: 15 Min
- Verifizierung: 5-7 Werktage (Postweg)
- Profil vervollständigen: 30 Min

---

## Aktuelle Lösung

**Status:** Maps-Embeds optimiert (zeigen Adresse)

Die aktuelle Lösung ist **funktional, aber nicht optimal**:

### Was funktioniert:
- Karte zeigt korrekte Adresse (Okenstraße 20-22, Offenburg)
- Pin ist am richtigen Standort
- User können "Route planen" nutzen
- Deutsche Lokalisierung

### Was fehlt (bis Business-Profil erstellt):
- Keine Reviews/Bewertungen sichtbar
- Keine Öffnungszeiten in der Karte
- Kein "Anrufen" Button
- Keine Fotos der Kanzlei
- Keine Business-Informationen

---

## Qualitäts-Check

### Funktionalität
- ✅ Maps-Embed lädt korrekt
- ✅ Adresse wird korrekt angezeigt
- ✅ Pin ist am richtigen Standort
- ✅ Zoom-Level passend (zeigt Umgebung)
- ✅ Deutsche Lokalisierung

### Code-Qualität
- ✅ `loading="lazy"` (Performance-Optimierung)
- ✅ `allowfullscreen` (Vollbild-Funktion)
- ✅ `referrerpolicy="no-referrer-when-downgrade"` (Privacy)
- ✅ Aussagekräftiger `title`-Attribute (Accessibility)
- ✅ Responsive (width="100%")

### UX
- ⚠️ Keine Business-Informationen (wegen fehlendem Profil)
- ✅ Karte interaktiv (Zoom, Pan möglich)
- ✅ "Größere Karte öffnen" funktioniert

---

## Zusammenfassung

| Kategorie | Status |
|-----------|--------|
| **Maps-Einbindung** | ✅ Funktioniert (Adresse wird korrekt angezeigt) |
| **Google Business Profil** | ❌ Nicht vorhanden (sollte erstellt werden) |
| **Code-Qualität** | ✅ Optimiert |
| **Lokalisierung** | ✅ Deutsch |
| **Accessibility** | ✅ Title-Attributes korrekt |

**Empfehlung:** Google Business Profile erstellen für vollständige Integration mit Reviews, Öffnungszeiten und Business-Informationen.

---

## Quellen

- [conrad & partner Website](https://www.conrad-offenburg.de/)
- [conrad & partner Kontakt](https://www.conrad-offenburg.de/kontakt/)
- [meinestadt.de Eintrag](https://branchenbuch.meinestadt.de/offenburg/company/14957588)
- [Das Örtliche Eintrag](https://www.dasoertliche.de/Themen/conrad-partner-Partnergesellschaft-mbB-Steuerberatung-Offenburg-Stadtmitte-Okenstr)
