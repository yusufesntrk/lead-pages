# Lead Pages - Projekt-Anweisungen

## Projekt-Ziel

Vollständige, **unique** Websites für Leads erstellen - KEINE Templates!
Jede Website behält das Corporate Design der Firma, aber mit modernem, professionellem Redesign.

## Tools & CLIs

- **GitHub CLI (`gh`)** - verfügbar und authentifiziert
- **Cloudflare CLI (`wrangler`)** - verfügbar

## Playwright

**IMMER `headless: true`** - keine sichtbaren Browser-Fenster.

```javascript
browser.launch({ headless: true })
```

### Screenshots - IMMER im Projektordner!

**NIEMALS Screenshots in globalen Ordnern speichern!**
- ❌ NIEMALS: `~/Downloads/`, `~/Desktop/`, `/tmp/`
- ✅ IMMER: Im jeweiligen Website-Ordner einen tmp-Ordner anlegen

**Workflow für Lead Pages:**
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

**Für Agents die Screenshots machen:**
- Screenshot-Pfad = aktueller Arbeitsordner + `.playwright-tmp/`
- Beispiel: Arbeite an `docs/kanzlei-knaub/` → Screenshots in `docs/kanzlei-knaub/.playwright-tmp/`
- Nach Analyse IMMER löschen (Bilder + Ordner)

---

## Website-Erstellung - Kernprinzipien

### 0. Deutsche Sprache - Umlaute verwenden!

**IMMER echte deutsche Umlaute und Sonderzeichen:**
- ä, ö, ü, ß (NICHT ae, oe, ue, ss)
- Beispiel: "Fachanwältinnen für Familienrecht" (NICHT "Fachanwaeltinnen fuer")

Dies gilt für:
- Alle HTML-Dateien
- Style Guide
- Alle generierten Texte

### 1. KEINE Templates - Unique Design

Jede Website ist individuell. Basierend auf:
- Extrahiertem Style Guide der Original-Website
- Branche des Unternehmens
- Vorhandenen Inhalten

### 2. Style Guide Extraktion (PFLICHT)

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

### 3. Logo-Konvertierung

Logos IMMER als SVG:
- PNG/GIF/JPG → SVG konvertieren (nutze `png-to-svg-converter` Skill)
- SVG bereits vorhanden → direkt verwenden

### 4. Content-Übernahme

Von Original-Website übernehmen:
- Alle Texte (Services, Über uns, etc.)
- Bilder (optimiert)
- Team-Infos
- Kontaktdaten

**ABER**: Besseres Storytelling, modernere Struktur, bessere UX.

### 5. Testimonials-Sektion

**Prioritäten:**
1. **Von Original-Website** (bevorzugt):
   - Testimonials übernehmen
   - Personen/Unternehmen recherchieren (LinkedIn)
   - Profilbilder und Firmenlogos hinzufügen
2. **Google Reviews** (Fallback):
   - Rating-Summary anzeigen
   - Link zu Google
3. **Keine Testimonials** → Sektion weglassen (keine Platzhalter!)

### 6. Rechtliche Seiten (VOLLSTÄNDIG!)

- Impressum, Datenschutz, AGB von Original extrahieren
- Falls nicht vorhanden: Mit echten Firmendaten erstellen
- **NIEMALS Platzhalter** (`{{FIRMA}}`, `[ADRESSE]`) im fertigen HTML!

### 8. Playwright Qualitätsprüfung (PFLICHT!)

Vor Deployment mit Playwright prüfen:

**Design:**
- Screenshots Desktop (1280x800) + Mobile (375x667)
- Farben entsprechen Style Guide
- Keine abgeschnittenen Elemente

**Sektions-Variation (KRITISCH!):**
```
⚠️ Sektionen hintereinander dürfen sich NIEMALS ähneln!
```
- Jede Sektion eigener visueller Charakter
- Abwechslung: Background, Layout, Spacing
- Keine zwei gleichen Card-Grids hintereinander

**Button & Link Check:**
- ALLE Links testen (keine 404)
- Navigation funktioniert
- Externe Links → neuer Tab

**CTA-Pflicht:**
- Homepage: min. 2 CTAs (Hero + Ende)
- Unterseiten: min. 1 CTA
- Handlungsauffordernd ("Jetzt kontaktieren")

**Logik-Check:**
- Texte machen Sinn
- Keine Widersprüche
- Branche-passende Sprache

---

### 9. Animationen nach Branche

| Branche | Animations-Level | Beispiele |
|---------|------------------|-----------|
| Rechtsanwalt, Steuerberater | Dezent | Fade-in, subtle hover |
| Restaurant, Café | Moderat | Scroll-reveal, image hover |
| Kreativagentur, Tech | Expressiv | Parallax, micro-interactions |
| Handwerk | Minimal | Nur hover-states |
| Arzt, Gesundheit | Ruhig | Sanfte transitions |

---

## Airtable

- **Base ID:** app4j0YLgGsYe1luA
- **Table:** Lead Pages (tblNQpZPxQleuajZc)

Felder:
- Firma, Branche, Website
- Straße, PLZ, Ort
- Telefon, Email
- Google Rating, Google Reviews
- Seite erstellt (Checkbox)
- Landingpage URL

---

## Generator-System (Agent SDK)

Der Lead Pages Generator nutzt das **Claude Agent SDK** mit 10 spezialisierten Agents:

### Agents und ihre Aufgaben

| # | Agent | Aufgabe |
|---|-------|---------|
| 1 | `style-guide` | Analysiert alte Website/Logo/Branche → Style Guide |
| 2 | `homepage` | Erstellt index.html, styles.css, script.js |
| 3 | `subpages` | Erstellt Kontakt, Über uns, Service-Seiten |
| 4 | `legal-pages` | Impressum, Datenschutz, AGB (keine Platzhalter!) |
| 5 | `link-qa` | Prüft und fixt alle Links/Buttons |
| 6 | `team-photos` | Sucht Team-Fotos (Website, LinkedIn, Google) |
| 7 | `logo` | PNG→SVG Konvertierung, Text-Logo Fallback |
| 8 | `references-page` | Erstellt Referenzen-Seite |
| 9 | `references-research` | Recherchiert echte Testimonials |
| 10 | `design-review` | QA mit Feedback Loop (max. 3 Iterationen) |

### Verwendung

```bash
# Interaktiv Lead auswählen
python -m generator.main

# Spezifischer Lead
python -m generator.main --lead recXXXXXX

# Test-Modus
python -m generator.main --test
```

### Workflow

```
1. Style Guide erstellen (Agent 1)
2. Logo verarbeiten (Agent 7)
3. Referenzen recherchieren (Agent 9)
4. Homepage erstellen (Agent 2)
5. Unterseiten erstellen (Agent 3)
6. Rechtliche Seiten erstellen (Agent 4)
7. Referenzen-Seite erstellen (Agent 8)
8. Team-Fotos suchen (Agent 6)
9. Link QA (Agent 5)
10. Design Review Loop (Agent 10) - max. 3 Iterationen
11. Airtable aktualisieren
12. Git commit & push
```

---

## Deployment & Finalisierung

### Output-Struktur

- Output: `docs/[firmenname]/`
- Cloudflare Pages: automatisch bei git push
- URL: `https://lead-pages.pages.dev/[firmenname]/`

### Automatische Finalisierung (im SDK)

Nach erfolgreicher Website-Generierung führt das SDK automatisch aus:

1. **Git Commit & Push** → `docs/[firmenname]/` wird committed und gepusht
2. **Airtable Update** → `Seite erstellt: true` + `Landingpage URL` gesetzt
3. **Live-URL Ausgabe** → `https://lead-pages.pages.dev/[firmenname]/`

**Hinweis:** Im Test-Modus (`--test`) werden Git und Airtable übersprungen.

### Manuelle Finalisierung (falls nötig)

Falls das SDK die Finalisierung nicht durchführt:

```bash
# Git
git add docs/[firmenname]/
git commit -m "Add landing page for [Firmenname]"
git push origin main

# Airtable (via MCP)
mcp__airtable__update_records(
    baseId="app4j0YLgGsYe1luA",
    tableId="tblNQpZPxQleuajZc",
    records=[{"id": "recXXX", "fields": {"Seite erstellt": True, "Landingpage URL": "https://..."}}]
)
```
