# Website Builder - Projekt-Anweisungen

## Projekt-Ziel

Vollständige, **unique** Websites für Unternehmen erstellen - KEINE Templates!
Jede Website behält das Corporate Design der Firma, aber mit modernem, professionellem Redesign.

---

## Airtable

- **Base ID:** `app4j0YLgGsYe1luA`
- **Table:** Lead Pages (`tblNQpZPxQleuajZc`)

**Felder:**
| Feld | Beschreibung |
|------|--------------|
| Firma | Firmenname |
| Branche | IT, Healthcare, Finance, etc. |
| Website | Firmenwebsite URL |
| Straße | Straßenadresse |
| PLZ | Postleitzahl |
| Ort | Stadt |
| Telefon | Telefonnummer |
| Email | E-Mail-Adresse |
| Google Rating | Bewertung (1-5 Sterne) |
| Google Reviews | Anzahl der Bewertungen |
| Seite erstellt | Checkbox ✓ wenn fertig |
| Landingpage URL | Generierte URL |

**MCP-Zugriff:**
```javascript
// Records lesen
mcp__airtable__list_records({
  baseId: "app4j0YLgGsYe1luA",
  tableId: "tblNQpZPxQleuajZc"
})

// Record aktualisieren
mcp__airtable__update_records({
  baseId: "app4j0YLgGsYe1luA",
  tableId: "tblNQpZPxQleuajZc",
  records: [{ id: "recXXX", fields: { "Seite erstellt": true, "Landingpage URL": "https://..." }}]
})
```

### Lead-Priorisierung

**Reihenfolge bei Website-Erstellung:**
1. Firmen am nächsten zu **Offenburg** zuerst
2. Sortierung nach Priorität absteigend

Bei Batch-Erstellung immer mit dem nächstgelegenen Standort zu Offenburg starten.

---

## Tools & CLIs

- **GitHub CLI (`gh`)** - verfügbar und authentifiziert
- **Cloudflare CLI (`wrangler`)** - verfügbar
- **Airtable MCP** - konfiguriert in `.mcp.json`
- **Playwright MCP** - konfiguriert in `.mcp.json`

---

## Playwright

**IMMER `headless: true`** - keine sichtbaren Browser-Fenster.

```javascript
browser.launch({ headless: true })
```

### Screenshots - IMMER im Projektordner!

**NIEMALS Screenshots in globalen Ordnern speichern!**
- ❌ NIEMALS: `~/Downloads/`, `~/Desktop/`, `/tmp/`
- ✅ IMMER: Im jeweiligen Website-Ordner einen tmp-Ordner anlegen

**Workflow:**
```bash
# 1. Temp-Ordner im Website-Ordner erstellen
mkdir -p docs/[firmenname]/.playwright-tmp

# 2. Screenshots dort speichern
playwright_screenshot({
  name: "review-desktop",
  savePng: true,
  downloadsDir: "docs/[firmenname]/.playwright-tmp"
})

# 3. Nach Analyse SOFORT löschen!
rm docs/[firmenname]/.playwright-tmp/*.png
rmdir docs/[firmenname]/.playwright-tmp
```

---

## Website-Erstellung - Kernprinzipien

### 1. Deutsche Sprache - Umlaute verwenden!

**IMMER echte deutsche Umlaute und Sonderzeichen:**
- ä, ö, ü, ß (NICHT ae, oe, ue, ss)
- Beispiel: "Fachanwältinnen für Familienrecht" (NICHT "Fachanwaeltinnen fuer")

### 2. KEINE Templates - Unique Design

Jede Website ist individuell. Basierend auf:
- Extrahiertem Style Guide der Original-Website
- Branche des Unternehmens
- Vorhandenen Inhalten

### 3. Style Guide Extraktion (PFLICHT)

Von der Original-Website extrahieren:
```
- Primary Color (Hauptfarbe)
- Secondary Color (Akzentfarbe)
- Text Color
- Background Color
- Font Family (oder ähnliche moderne Alternative)
- Spacing-System
- Button-Styles
- Logo-Farben
```

### 4. Logo-Konvertierung

Logos IMMER als SVG:
- PNG/GIF/JPG → SVG konvertieren
- SVG bereits vorhanden → direkt verwenden

### 5. Content-Übernahme

Von Original-Website übernehmen:
- Alle Texte (Services, Über uns, etc.)
- Bilder (optimiert)
- Team-Infos
- Kontaktdaten

**ABER**: Besseres Storytelling, modernere Struktur, bessere UX.

### 6. Testimonials-Sektion

**Prioritäten:**
1. **Von Original-Website** (bevorzugt)
2. **Google Reviews** (Fallback)
3. **Keine Testimonials** → Sektion weglassen (keine Platzhalter!)

### 7. Rechtliche Seiten (VOLLSTÄNDIG!)

- Impressum, Datenschutz, AGB von Original extrahieren
- Falls nicht vorhanden: Mit echten Firmendaten erstellen
- **NIEMALS Platzhalter** (`{{FIRMA}}`, `[ADRESSE]`) im fertigen HTML!

### 8. Sektions-Variation (KRITISCH!)

```
⚠️ Sektionen hintereinander dürfen sich NIEMALS ähneln!
```
- Jede Sektion eigener visueller Charakter
- Abwechslung: Background, Layout, Spacing
- Keine zwei gleichen Card-Grids hintereinander

### 9. CTA-Pflicht

- Homepage: min. 2 CTAs (Hero + Ende)
- Unterseiten: min. 1 CTA
- Handlungsauffordernd ("Jetzt kontaktieren")

### 10. Animationen nach Branche

| Branche | Animations-Level | Beispiele |
|---------|------------------|-----------|
| Rechtsanwalt, Steuerberater | Dezent | Fade-in, subtle hover |
| Restaurant, Café | Moderat | Scroll-reveal, image hover |
| Kreativagentur, Tech | Expressiv | Parallax, micro-interactions |
| Handwerk | Minimal | Nur hover-states |
| Arzt, Gesundheit | Ruhig | Sanfte transitions |

---

## Verfügbare Agents

| Agent | Beschreibung |
|-------|--------------|
| **website-builder** | Erstellt komplette Websites basierend auf Corporate Design |
| **subpages-builder** | Erstellt alle relevanten Unterseiten |
| **links-checker** | Prüft alle Buttons und Links auf Korrektheit |
| **responsive-checker** | Prüft Mobile- und Desktop-Ansicht |
| **testimonials-verifier** | Findet und extrahiert echte Testimonials |
| **placeholder-replacer** | Findet SVG-Platzhalter und ersetzt sie durch echte Bilder |
| **image-quality-checker** | Prüft Bildauflösung, Dateigröße und Retina-Support |
| **image-authenticity-checker** | Prüft ob Team/Testimonials echte Fotos sind (keine Stock) |
| **google-maps-verifier** | Prüft Google Maps URLs |
| **broken-images-fixer** | Findet und behebt nicht angezeigte Bilder |
| **team-photos-extractor** | Extrahiert Team-Fotos von Original-Websites und bindet sie ein |

**Agent-Aufruf:**
```
"Use the website-builder to create a website for [Firma]"
"Use the links-checker to verify all links"
"Use the responsive-checker to test mobile view"
```

---

## Output-Struktur

```
docs/
├── [firmenname]/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   ├── about.html
│   ├── contact.html
│   ├── services.html
│   ├── impressum.html
│   ├── datenschutz.html
│   └── assets/
│       ├── logo.svg
│       ├── images/
│       └── fonts/
```

---

## Deployment

- **Output:** `docs/[firmenname]/` (in diesem Repo)
- **Lead-Pages Repo:** `~/lead-pages/` (separates Repo für Cloudflare Pages)
- **Cloudflare Pages:** automatisch bei git push zu lead-pages
- **URL:** `https://lead-pages.pages.dev/[firmenname]/`

### Finalisierung

```bash
# 1. Ordner ins lead-pages Repo kopieren
cp -r docs/[firmenname] ~/lead-pages/

# 2. Im lead-pages Repo committen und pushen
cd ~/lead-pages
git add [firmenname]/
git commit -m "Add landing page for [Firmenname]"
git push origin main

# 3. Zurück zum website-builder
cd ~/website-builder
```

```javascript
// 4. Airtable Update (via MCP)
mcp__airtable__update_records({
  baseId: "app4j0YLgGsYe1luA",
  tableId: "tblNQpZPxQleuajZc",
  records: [{ id: "recXXX", fields: { "Seite erstellt": true, "Landingpage URL": "https://lead-pages.pages.dev/[firmenname]/" }}]
})
```

---

## Qualitätsprüfung (PFLICHT!)

Vor Deployment mit Playwright prüfen:

**Design:**
- Screenshots Desktop (1280x800) + Mobile (375x667)
- Farben entsprechen Style Guide
- Keine abgeschnittenen Elemente

**Button & Link Check:**
- ALLE Links testen (keine 404)
- Navigation funktioniert
- Externe Links → neuer Tab

**Logik-Check:**
- Texte machen Sinn
- Keine Widersprüche
- Branche-passende Sprache

**Agent-Prüfungen:**
- `links-checker` für Link-Validierung
- `responsive-checker` für Mobile/Desktop-Test
- `image-verifier` für Bild-Prüfung
