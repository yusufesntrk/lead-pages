# Lead Pages Generator - Unique Websites

Du erstellst **vollständige, einzigartige Websites** für Unternehmen.
KEINE Templates - jede Website ist individuell basierend auf dem Corporate Design der Firma.

## Airtable
- Base ID: app4j0YLgGsYe1luA
- Table: Lead Pages (tblNQpZPxQleuajZc)

---

## WORKFLOW

### Phase 1: Lead auswählen

```
Airtable: filterByFormula = NOT({Seite erstellt})
```

Benötigte Felder:
- Firma (Pflicht)
- Website (Pflicht)
- Branche
- Google Rating + Reviews (für Testimonials)
- Kontaktdaten

---

### Phase 2: Style Guide extrahieren

**PFLICHT für jede Website!**

Von der Original-Website analysieren und extrahieren:

```markdown
## Style Guide: [Firmenname]

### Farben
- Primary: #XXXXXX (Hauptfarbe aus Logo/Header)
- Secondary: #XXXXXX (Akzentfarbe)
- Text: #XXXXXX
- Background: #XXXXXX
- Accent: #XXXXXX

### Typografie
- Headings: [Font-Familie] oder moderne Alternative
- Body: [Font-Familie] oder moderne Alternative
- Gewichtungen: [Welche werden verwendet]

### Spacing
- Section Padding: [z.B. 80px/120px]
- Element Gaps: [z.B. 24px/32px]

### Buttons
- Style: [Rounded/Square/Pill]
- Hover-Effekt: [Beschreibung]

### Besonderheiten
- [Spezielle Design-Elemente der Marke]
```

Speichern als: `docs/[firmenname]/style-guide.md`

---

### Phase 3: Assets extrahieren

**3.1 Logo**
- Logo von Website extrahieren
- Format prüfen:
  - SVG → direkt verwenden
  - PNG/GIF/JPG → mit `png-to-svg-converter` Skill konvertieren
- Speichern als: `docs/[firmenname]/assets/logo.svg`

**3.2 Favicon**
- Favicon extrahieren oder aus Logo generieren
- Speichern als: `docs/[firmenname]/assets/favicon.ico`

**3.3 Bilder**
- Relevante Bilder von Original-Website
- Team-Fotos, Hero-Images, Service-Bilder
- Optimieren und speichern in: `docs/[firmenname]/assets/images/`

---

### Phase 4: Content extrahieren & verbessern

**4.1 Texte übernehmen**
Von der Original-Website:
- Über uns / Geschichte
- Services / Leistungen
- Team-Beschreibungen
- USPs / Vorteile

**4.2 Storytelling verbessern**
Die Texte NICHT 1:1 kopieren, sondern:
- Bessere Struktur (Headline → Subheadline → Body)
- Emotionalere Ansprache
- Klarere Value Proposition
- Scanbare Formatierung (Bullet Points, kurze Absätze)

**4.3 Rechtliche Seiten (VOLLSTÄNDIG!)**

Von der Original-Website extrahieren (falls vorhanden):
- Impressum → `impressum.html`
- Datenschutz → `datenschutz.html`
- AGB → `agb.html` (falls relevant)
- Widerrufsbelehrung → (falls E-Commerce)

**WICHTIG:**
- Texte VOLLSTÄNDIG übernehmen, nicht kürzen
- Firmenspezifische Daten (Name, Adresse, etc.) verifizieren
- Links zu Aufsichtsbehörden, Streitschlichtung etc. prüfen

**Falls NICHT vorhanden auf Original-Website:**
- Impressum: Mit echten Firmendaten aus Airtable erstellen (Pflichtangaben nach §5 TMG)
- Datenschutz: Basis-DSGVO-Text mit Firmendaten anpassen
- NIEMALS Platzhalter wie "[FIRMA]" oder "{{ADRESSE}}" im fertigen HTML!

```
Jede rechtliche Seite muss:
✓ Vollständig ausgefüllt sein
✓ Echte Firmendaten enthalten
✓ Korrekt formatiert sein
✓ Alle Pflichtangaben haben
```

**4.4 Social Media**
```
WebSearch: "[Firmenname] LinkedIn"
WebSearch: "[Firmenname] Xing"
WebSearch: "[Firmenname] Instagram"
```
NUR echte, verifizierte URLs verwenden!

---

### Phase 5: Testimonials-Sektion erstellen

**PFLICHT für jede Website!**

**Priorität 1: Testimonials von Original-Website**
Falls auf der Original-Website Testimonials vorhanden sind:
- Alle Testimonials übernehmen (Text, Name, Firma)
- Personen/Unternehmen recherchieren:
  ```
  WebSearch: "[Person Name] [Firma] LinkedIn"
  ```
- Profilbilder der Personen finden und einbinden
- Firmenlogos der Referenzkunden hinzufügen

```html
<section class="testimonials">
  <h2>Das sagen unsere Kunden</h2>

  <div class="testimonials-grid">
    <div class="testimonial-card">
      <img src="assets/images/testimonials/person-1.jpg" alt="Max Mustermann" class="testimonial-avatar">
      <blockquote>"Testimonial-Text von der Original-Website..."</blockquote>
      <div class="testimonial-author">
        <strong>Max Mustermann</strong>
        <span>Geschäftsführer, Musterfirma GmbH</span>
        <img src="assets/images/testimonials/logo-musterfirma.svg" alt="Musterfirma" class="client-logo">
      </div>
    </div>
  </div>
</section>
```

**Priorität 2: Google Reviews (Fallback)**
Falls keine Testimonials auf Website, aber Google Rating in Airtable:
- Rating-Summary anzeigen
- Link zu Google Reviews

```html
<section class="testimonials">
  <h2>Kundenbewertungen</h2>
  <div class="google-rating">
    <span class="stars">★★★★★</span>
    <span class="score">4.8 / 5</span>
    <span class="count">156 Bewertungen auf Google</span>
    <a href="[GOOGLE_MAPS_LINK]" class="btn">Alle Bewertungen ansehen</a>
  </div>
</section>
```

**Priorität 3: Keine Testimonials**
Falls weder Website-Testimonials noch Google Rating:
- Sektion weglassen (nicht mit Platzhaltern füllen!)

---

### Phase 6: Animations-Level bestimmen

Basierend auf Branche:

| Branche | Level | Animationen |
|---------|-------|-------------|
| **Rechtsanwalt, Notar, Steuerberater** | Dezent | `fade-in` auf Sections, subtile `hover` auf Buttons |
| **Arzt, Gesundheit, Pflege** | Ruhig | Sanfte `transitions`, keine abrupten Bewegungen |
| **Handwerk, Bau** | Minimal | Nur `hover`-States, keine Scroll-Animationen |
| **Restaurant, Café, Hotel** | Moderat | `scroll-reveal`, Image-Hover-Effekte, sanftes Parallax |
| **Kreativagentur, Marketing** | Expressiv | Parallax, Micro-Interactions, Text-Animationen |
| **Tech, Software, Startup** | Modern | Smooth Scrolling, Cursor-Effekte, SVG-Animationen |
| **Einzelhandel, Mode** | Elegant | Fade-Transitions, Produkt-Hover-Zoom |

**CSS-Beispiele:**

```css
/* Dezent (Anwalt, Steuerberater) */
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Moderat (Restaurant) */
.scroll-reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Expressiv (Kreativagentur) */
.parallax-section {
  background-attachment: fixed;
  background-position: center;
  background-size: cover;
}
```

---

### Phase 7: Website erstellen

**KEINE Templates!** Jede Seite individuell basierend auf:
1. Style Guide
2. Content
3. Branche & Animations-Level

**Struktur:**
```
docs/[firmenname]/
├── index.html          # Homepage
├── about.html          # Über uns (falls Content vorhanden)
├── services.html       # Leistungen (falls relevant)
├── contact.html        # Kontakt
├── impressum.html      # Impressum
├── datenschutz.html    # Datenschutz
├── style-guide.md      # Extrahierter Style Guide
└── assets/
    ├── logo.svg
    ├── favicon.ico
    ├── styles.css      # Unique CSS basierend auf Style Guide
    └── images/
```

**CSS muss enthalten:**
- Farben aus Style Guide
- Custom Properties für einfache Anpassung
- Responsive Design (Mobile-First)
- Branchen-spezifische Animationen
- Testimonials-Styling

---

### Phase 8: Playwright Qualitätsprüfung (PFLICHT!)

**Automatisierte Prüfung mit Playwright - headless: true**

**8.1 Screenshots erstellen**
```bash
# Desktop + Mobile Screenshots jeder Seite
npx playwright screenshot http://localhost:[PORT]/[firmenname]/ desktop-home.png --viewport-size=1280,800
npx playwright screenshot http://localhost:[PORT]/[firmenname]/ mobile-home.png --viewport-size=375,667
# Für jede Unterseite wiederholen
```

**8.2 Design-Review (visuell)**
Screenshots analysieren auf:
- [ ] Farben entsprechen Style Guide
- [ ] Typography konsistent
- [ ] Spacing gleichmäßig
- [ ] Keine abgeschnittenen Elemente
- [ ] Responsive Layout korrekt

**8.3 Sektions-Variation Check (KRITISCH!)**
```
⚠️ Sektionen hintereinander dürfen sich NIEMALS ähneln!
```
Prüfen:
- [ ] Jede Sektion hat eigenen visuellen Charakter
- [ ] Abwechslung: Hintergrundfarbe, Layout, Spacing
- [ ] Keine zwei aufeinanderfolgenden Sektionen mit gleichem Background
- [ ] Grid/Layout variiert (nicht 3x gleiche Card-Rows)

Beispiel für gute Variation:
```
Hero (Bild + Text)
  ↓
Services (3-Spalten Grid, heller Hintergrund)
  ↓
Über uns (2-Spalten, Bild links, dunkler Hintergrund)
  ↓
Testimonials (Horizontal Scroll, Akzentfarbe)
  ↓
CTA (Zentriert, Primary Color Background)
```

**8.4 Logik-Check (Inhalt)**
Jede Sektion prüfen:
- [ ] Text macht Sinn im Kontext
- [ ] Keine Widersprüche zwischen Sektionen
- [ ] Informationsfluss logisch (Problem → Lösung → CTA)
- [ ] Keine doppelten Inhalte
- [ ] Branche-passende Sprache

**8.5 Button & Link Check (ALLE!)**
```javascript
// Playwright: Alle Links sammeln und testen
const links = await page.$$eval('a[href]', els => els.map(e => ({
  text: e.textContent,
  href: e.href
})));

// Jeden Link prüfen:
// - Führt zu korrekter Unterseite?
// - Kein 404?
// - Externe Links öffnen in neuem Tab?
```

Prüfen:
- [ ] Alle internen Links funktionieren
- [ ] Navigation Links zeigen auf richtige Seiten
- [ ] CTA-Buttons haben korrekte Ziele
- [ ] Keine toten Links (404)
- [ ] Footer-Links funktionieren
- [ ] Social Links öffnen extern

**8.6 CTA-Check (PFLICHT!)**
```
⚠️ Jede Seite MUSS mindestens einen CTA haben!
```
- [ ] Homepage: Mindestens 2 CTAs (Hero + Ende)
- [ ] Unterseiten: Mindestens 1 CTA
- [ ] CTA-Text ist handlungsauffordernd ("Jetzt kontaktieren", "Termin vereinbaren")
- [ ] CTA führt zu Kontaktseite oder Formular
- [ ] CTA ist visuell hervorgehoben (Primary Button Style)

**8.7 Accessibility Quick-Check**
- [ ] Alle Bilder haben alt-Text
- [ ] Kontrast ausreichend (Text auf Hintergrund)
- [ ] Buttons haben erkennbare Hover-States
- [ ] Focus-States vorhanden

**8.8 Finale Checkliste**
```
╔══════════════════════════════════════════════════════════╗
║  QUALITÄTSPRÜFUNG                                        ║
╠══════════════════════════════════════════════════════════╣
║  □ Style Guide angewendet                                ║
║  □ Logo als SVG                                          ║
║  □ Sektionen variieren (nicht ähnlich!)                  ║
║  □ Alle Buttons/Links funktionieren                      ║
║  □ CTAs vorhanden (min. 2 auf Homepage)                  ║
║  □ Testimonials (echt, mit Recherche)                    ║
║  □ Rechtliche Seiten vollständig                         ║
║  □ Keine Platzhalter im HTML                             ║
║  □ Mobile responsive                                     ║
║  □ Logik & Inhalt sinnvoll                               ║
╚══════════════════════════════════════════════════════════╝
```

**Bei Fehlern:** Zurück zu Phase 7, korrigieren, erneut prüfen.

---

### Phase 9: Deployment

```bash
git add docs/[firmenname]/
git commit -m "Neue Website: [Firmenname] - [Branche]"
git push
```

---

### Phase 10: Airtable aktualisieren

```
update_records:
- "Seite erstellt": true
- "Landingpage URL": https://lead-pages.pages.dev/[firmenname]/
```

---

## NIEMALS

- ❌ Template-basierte Websites
- ❌ Generische Farben statt Corporate Design
- ❌ Logos in PNG/GIF/JPG (immer SVG!)
- ❌ Falsche Animations-Intensität für Branche
- ❌ Copy-Paste Texte ohne Storytelling-Verbesserung
- ❌ Generische Social Links
- ❌ Platzhalter im fertigen HTML (`{{FIRMA}}`, `[NAME]`, etc.)
- ❌ Unvollständige rechtliche Seiten
- ❌ Testimonials erfinden (nur echte verwenden!)

## IMMER

- ✅ Style Guide zuerst extrahieren
- ✅ Corporate Design beibehalten
- ✅ Logo zu SVG konvertieren
- ✅ Testimonials von Website übernehmen + Personen recherchieren
- ✅ Branchen-passende Animationen
- ✅ Besseres Storytelling als Original
- ✅ Unique CSS pro Website
- ✅ Rechtliche Seiten vollständig (Impressum, Datenschutz, AGB)
- ✅ Alles muss fertig aussehen - keine Variablen!
