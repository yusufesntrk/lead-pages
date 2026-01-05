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

Screenshots temporär in `.playwright-tmp/` speichern und nach Analyse löschen.

---

## Website-Erstellung - Kernprinzipien

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

## Deployment

- Output: `docs/[firmenname]/`
- Cloudflare Pages: automatisch bei git push
- URL: `https://lead-pages.pages.dev/[firmenname]/`
