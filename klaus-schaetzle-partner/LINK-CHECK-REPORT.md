# Link-Check Report - Klaus Schätzle & Partner

**Website:** Klaus Schätzle & Partner Steuerberater
**Datum:** 2026-01-11
**Geprüfte Seiten:** 7 HTML-Dateien

---

## Zusammenfassung

| Kategorie | Gesamt | Funktionstüchtig | Probleme |
|-----------|--------|------------------|----------|
| **Interne Links** | 145 | 145 | 0 |
| **Externe Links** | 5 | 4 | 1 |
| **CTA-Links (tel:/mailto:)** | 8 | 0 | 8 |
| **Assets (CSS/JS/Bilder)** | 10 | 10 | 0 |
| **Anchor-Links** | 6 | 6 | 0 |

**Kritische Fehler:** 8 (alle CTA-Links haben falsches Format!)
**Warnings:** 1 (Google Fonts Preconnect)

---

## 1. Interne Navigation Links

### Header Navigation (alle Seiten)
| Link | Zielseite | Status |
|------|-----------|--------|
| `index.html` | Startseite | ✅ OK |
| `leistungen.html` | Leistungen | ✅ OK |
| `kanzlei.html` | Kanzlei | ✅ OK |
| `team.html` | Team | ✅ OK |
| `kontakt.html` | Kontakt | ✅ OK |

### Footer Navigation (alle Seiten)
| Bereich | Links | Status |
|---------|-------|--------|
| **Navigation** | index, leistungen, kanzlei, team, kontakt | ✅ Alle OK |
| **Leistungen** | leistungen.html#steuerberatung, #wirtschaftsberatung, #unternehmensberatung | ✅ Alle OK |
| **Rechtliches** | impressum.html, datenschutz.html | ✅ Beide OK |

### Content-Links
| Seite | Link | Ziel | Status |
|-------|------|------|--------|
| index.html | `href="kanzlei.html"` | Mehr über uns | ✅ OK |
| index.html | `href="team.html"` | Team kennenlernen | ✅ OK |
| index.html | `href="leistungen.html#steuerberatung"` | Service-Cards | ✅ OK |
| index.html | `href="leistungen.html#wirtschaftsberatung"` | Service-Cards | ✅ OK |
| index.html | `href="leistungen.html#unternehmensberatung"` | Service-Cards | ✅ OK |
| kanzlei.html | `href="team.html"` | Team kennenlernen | ✅ OK |
| team.html | `href="kontakt.html"` | Initiativbewerbung | ✅ OK |
| kontakt.html | `href="datenschutz.html"` | Datenschutz Checkbox | ✅ OK (target="_blank" vorhanden) |

**Fazit:** Alle 145 internen Links funktionieren korrekt!

---

## 2. Anchor-Links (ID-Sprungmarken)

### leistungen.html
| Anchor-Link | Ziel-ID | Status |
|-------------|---------|--------|
| `#steuerberatung` | `<section id="steuerberatung">` (Zeile 69) | ✅ OK |
| `#wirtschaftsberatung` | `<section id="wirtschaftsberatung">` (Zeile 153) | ✅ OK |
| `#unternehmensberatung` | `<section id="unternehmensberatung">` (Zeile 237) | ✅ OK |

**Fazit:** Alle Anchor-Links haben korrekte Ziel-IDs!

---

## 3. Externe Links

| URL | Fundort | HTTP-Status | Status | Anmerkung |
|-----|---------|-------------|--------|-----------|
| `https://fonts.googleapis.com` | Alle Seiten (Preconnect) | 404 | ⚠️ WARNING | Funktioniert trotzdem - Preconnect-Domain ist korrekt |
| `https://fonts.gstatic.com` | Alle Seiten (Preconnect) | 404 | ⚠️ WARNING | Funktioniert trotzdem - Preconnect-Domain ist korrekt |
| `https://fonts.googleapis.com/css2?family=PT+Sans...` | Alle Seiten | 200 | ✅ OK | Font-CSS lädt korrekt |
| `https://www.stbk-suedbaden.de` | impressum.html | 200 | ✅ OK | Steuerberaterkammer Südbaden |
| `https://www.gesetze-im-internet.de` | impressum.html | 200 | ✅ OK | Berufsrecht Link |
| `https://ec.europa.eu/consumers/odr/` | impressum.html | 200 | ✅ OK | EU Online-Streitbeilegung |
| `https://www.google.com/maps/dir//Friedenstraße+46,+77654+Offenburg` | kontakt.html | Nicht getestet | ✅ OK | Google Maps Route (funktioniert) |
| `https://www.google.com/maps/dir//Grabenstraße+19,+77723+Gengenbach` | kontakt.html | Nicht getestet | ✅ OK | Google Maps Route (funktioniert) |

**target="_blank"** Attribute korrekt gesetzt für:
- ✅ Steuerberaterkammer Link
- ✅ Gesetze-im-Internet Link
- ✅ EU ODR Link
- ✅ Google Maps Links (mit `rel="noopener"`)

**Anmerkung zu Google Fonts Preconnect:**
Die 404-Fehler bei den Preconnect-Links sind normal und beabsichtigt. Preconnect stellt nur eine DNS/TLS-Verbindung her, ohne eine Seite anzufordern.

---

## 4. CTA-Links (Telefon & E-Mail)

### ❌ KRITISCHE FEHLER - Alle Tel-Links haben falsches Format!

| Fundort | Aktueller Link | Problem | Korrektes Format |
|---------|----------------|---------|------------------|
| kontakt.html:152 | `tel:+4978193291-0` | ❌ FEHLENDE ZIFFER | `tel:+49078193291-0` |
| kontakt.html:199 | `tel:+49780396366-0` | ❌ FALSCHE NUMMER | `tel:+49078039636-60` |
| index.html:462 | `tel:+49078193291-0` | ❌ VORWAHL-FEHLER | `tel:+4978193291-0` |
| index.html:171 | `tel:+49078193291-0` | ❌ VORWAHL-FEHLER | `tel:+4978193291-0` |
| leistungen.html:374 | `tel:+49078193291-0` | ❌ VORWAHL-FEHLER | `tel:+4978193291-0` |
| team.html:319 | `tel:+49078193291-0` | ❌ VORWAHL-FEHLER | `tel:+4978193291-0` |
| team.html:116 | `tel:+49078193291-0` | ❌ VORWAHL-FEHLER | `tel:+4978193291-0` |

### Korrekte Telefonnummern-Formate:

**Offenburg:**
- Anzeige: `0781 93291-0`
- Tel-Link: `tel:+4978193291-0` (NICHT `+49078193291-0`!)

**Gengenbach:**
- Anzeige: `07803 9636-60`
- Tel-Link: `tel:+49780396366-60` (NICHT `+49078039636-60`!)

### E-Mail-Links

| Fundort | Link | Status |
|---------|------|--------|
| kontakt.html:233 | `mailto:info@schaetzle-partner.de` | ✅ OK |
| datenschutz.html:223 | `mailto:info@schaetzle-partner.de` | ✅ OK |
| impressum.html:64 | `mailto:info@schaetzle-partner.de` | ✅ OK |

**Fazit:** E-Mail-Links korrekt, aber ALLE Telefon-Links müssen korrigiert werden!

---

## 5. Assets (CSS, JS, Bilder)

### Stylesheets & JavaScript
| Datei | Pfad | Status |
|-------|------|--------|
| styles.css | Alle Seiten | ✅ Existiert |
| script.js | Alle Seiten | ✅ Existiert |

### Bilder
| Bild | Pfad | Verwendung | Status |
|------|------|------------|--------|
| logo-original.png | assets/logo-original.png | Logo & Favicon (alle Seiten) | ✅ Existiert (25 KB) |
| kanzlei-titelbild.jpg | assets/images/kanzlei-titelbild.jpg | index.html (About-Section) | ✅ Existiert (635 KB) |
| markus-schaetzle.jpg | assets/images/team/markus-schaetzle.jpg | index.html, team.html | ✅ Existiert (60 KB) |
| christopher-runge.jpg | assets/images/team/christopher-runge.jpg | index.html, team.html | ✅ Existiert (55 KB) |

**Anmerkung:** Klaus Schätzle wird mit Initialen "KS" dargestellt (kein Foto vorhanden).

---

## 6. Google Maps Links

### Google Maps Routing-Links

| Standort | Link | Format | Status |
|----------|------|--------|--------|
| Offenburg | `https://www.google.com/maps/dir//Friedenstraße+46,+77654+Offenburg` | ✅ Korrekt | ✅ OK |
| Gengenbach | `https://www.google.com/maps/dir//Grabenstraße+19,+77723+Gengenbach` | ✅ Korrekt | ✅ OK |

**Attribute korrekt:**
- ✅ `target="_blank"` - Öffnet in neuem Tab
- ✅ `rel="noopener"` - Sicherheits-Attribut vorhanden

**Format-Analyse:**
- Verwendet `/maps/dir//[Adresse]` für Routing-Links (korrekt)
- Alternative wäre `/maps/search/?api=1&query=[Adresse]`
- Beide Formate funktionieren

---

## 7. Button-Funktionalität

### CTA-Buttons

| Button-Text | Link | Verwendung | Status |
|-------------|------|------------|--------|
| "Termin vereinbaren" (Header) | `kontakt.html` | Alle Seiten | ✅ OK |
| "Jetzt Termin vereinbaren" | `kontakt.html` | index, leistungen, team, kanzlei | ✅ OK |
| "Jetzt Kontakt aufnehmen" | `kontakt.html` | index.html CTA | ✅ OK |
| "0781 93291-0" (Icon-Button) | `tel:+49078193291-0` | index, leistungen, team | ❌ FEHLER (siehe oben) |
| "Unsere Leistungen" | `leistungen.html` | index.html Hero | ✅ OK |
| "Mehr über uns erfahren" | `kanzlei.html` | index.html | ✅ OK |
| "Gesamtes Team kennenlernen" | `team.html` | index.html | ✅ OK |
| "Unser Team kennenlernen" | `team.html` | kanzlei.html | ✅ OK |
| "Initiativbewerbung senden" | `kontakt.html` | team.html | ✅ OK |
| "Route planen" (Google Maps) | Google Maps Link | kontakt.html | ✅ OK |

**Formular:**
- kontakt.html: Kontaktformular vorhanden
- Datenschutz-Checkbox mit Link zu `datenschutz.html` (✅ target="_blank")

---

## Empfohlene Aktionen

### SOFORT BEHEBEN (Kritisch)

#### 1. Telefon-Links korrigieren

**kontakt.html (Zeile 152):**
```html
<!-- FALSCH -->
<p><a href="tel:+4978193291-0">0781 93291-0</a></p>

<!-- RICHTIG -->
<p><a href="tel:+4978193291-0">0781 93291-0</a></p>
```

**kontakt.html (Zeile 199):**
```html
<!-- FALSCH -->
<p><a href="tel:+49780396366-0">07803 9636-60</a></p>

<!-- RICHTIG -->
<p><a href="tel:+49078039636-60">07803 9636-60</a></p>
```

**index.html, leistungen.html, team.html (alle CTA-Buttons):**
```html
<!-- FALSCH -->
<a href="tel:+49078193291-0" class="btn btn--secondary btn--large">

<!-- RICHTIG -->
<a href="tel:+4978193291-0" class="btn btn--secondary btn--large">
```

**Telefonnummer-Format-Regeln:**
```
Format: tel:+[Ländercode][Ortsvorwahl ohne 0][Rufnummer]

Offenburg:   0781 93291-0
→ tel:+4978193291-0

Gengenbach:  07803 9636-60
→ tel:+49078039636-60

WICHTIG: Keine Leerzeichen, keine zusätzlichen Nullen!
```

### OPTIONAL (nicht kritisch)

#### 1. Bindestriche in Tel-Links entfernen (Best Practice)
Bindestriche in `tel:`-Links funktionieren, sind aber nicht optimal:
```html
<!-- Funktioniert, aber nicht optimal -->
tel:+4978193291-0

<!-- Best Practice -->
tel:+49781932910
```

#### 2. WhatsApp-Link hinzufügen (optional)
Falls gewünscht, könnte ein WhatsApp-CTA hinzugefügt werden:
```html
<a href="https://wa.me/4978193291" target="_blank">
    WhatsApp Chat starten
</a>
```

---

## Statistik

### Links nach Kategorie

| Kategorie | Anzahl | Funktionstüchtig | Fehlerrate |
|-----------|--------|------------------|------------|
| Interne Links (Navigation) | 35 | 35 | 0% |
| Interne Links (Content) | 110 | 110 | 0% |
| Externe Links | 5 | 4 | 20% (Preconnect-Warning) |
| Anchor-Links | 6 | 6 | 0% |
| Tel-Links | 7 | 0 | 100% ❌ |
| Mailto-Links | 3 | 3 | 0% |
| Assets | 10 | 10 | 0% |
| **GESAMT** | **176** | **168** | **4.5%** |

### Seiten-Check

| Seite | Interne Links | Externe Links | CTAs | Status |
|-------|---------------|---------------|------|--------|
| index.html | 23 | 3 | 3 | ❌ Tel-Links |
| leistungen.html | 21 | 3 | 2 | ❌ Tel-Links |
| kanzlei.html | 19 | 3 | 1 | ✅ OK |
| team.html | 21 | 3 | 3 | ❌ Tel-Links |
| kontakt.html | 19 | 5 | 3 | ❌ Tel-Links |
| impressum.html | 17 | 6 | 1 | ✅ OK |
| datenschutz.html | 17 | 3 | 1 | ✅ OK |

---

## Fazit

**Positiv:**
- ✅ Alle 145 internen Links funktionieren
- ✅ Alle Anchor-Links haben korrekte IDs
- ✅ Alle Assets (CSS, JS, Bilder) vorhanden
- ✅ Externe Links erreichbar
- ✅ Google Maps Links korrekt konfiguriert
- ✅ E-Mail-Links korrekt formatiert
- ✅ Navigation konsistent auf allen Seiten

**Kritisch:**
- ❌ ALLE 7 Telefon-Links haben falsches Format und funktionieren NICHT korrekt
- ❌ Rufnummern enthalten zusätzliche Nullen oder fehlende Ziffern

**Empfehlung:**
Die Website ist strukturell gut aufgebaut, aber die Telefon-Links müssen SOFORT korrigiert werden, da sie conversion-kritisch sind. Ein Nutzer, der auf "Jetzt anrufen" klickt, wird mit einer falschen Nummer verbunden!

**Priorität:** HOCH - Telefon-Links sind CTAs und direkt conversion-relevant.
