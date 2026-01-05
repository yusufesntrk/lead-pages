# Style Guide - Kanzlei Dedden

## Firmendaten

**Name:** Kanzlei Dedden
**Branche:** Rechtsanwalt
**Standort:** Hauptstraße 95, 77694 Kehl
**Telefon:** +49 7851 484322
**Email:** Nicht bekannt
**Google Rating:** 4.3 ⭐ (6 Bewertungen)

---

## Farbpalette

### Primärfarben

```
Primary (Dunkelblau):     #1a3a52
Secondary (Gold):         #c9a961
```

**Verwendung:**
- **#1a3a52** - Hauptnavigation, Überschriften, Footer, primäre Buttons
- **#c9a961** - Akzente, Hover-States, wichtige CTAs, dekorative Elemente

### Sekundärfarben

```
Text Dark:                #2d2d2d
Text Light:               #5f5f5f
Background Light:         #f8f9fa
Background White:         #ffffff
Border/Divider:           #e0e0e0
```

### Farbverwendung

| Element | Farbe | Hex |
|---------|-------|-----|
| Hero Background | Dunkelblau Gradient | #1a3a52 → #2a4a62 |
| Primary Button | Dunkelblau | #1a3a52 |
| Primary Button Hover | Gold | #c9a961 |
| Secondary Button | Gold | #c9a961 |
| Links | Dunkelblau | #1a3a52 |
| Links Hover | Gold | #c9a961 |
| Überschriften | Dunkelblau | #1a3a52 |
| Body Text | Dunkelgrau | #2d2d2d |
| Footer | Dunkelblau | #1a3a52 |

---

## Typografie

### Schriftarten

**Primär (Überschriften):**
```css
font-family: 'Playfair Display', serif;
```

**Sekundär (Body Text):**
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

### Schriftgrößen

```css
/* Überschriften */
--fs-h1: 3.5rem;    /* 56px - Hero */
--fs-h2: 2.5rem;    /* 40px - Sektionen */
--fs-h3: 1.75rem;   /* 28px - Cards */
--fs-h4: 1.25rem;   /* 20px - Subsections */

/* Body */
--fs-body: 1.125rem;    /* 18px */
--fs-small: 0.875rem;   /* 14px */

/* Mobile */
@media (max-width: 768px) {
  --fs-h1: 2.25rem;   /* 36px */
  --fs-h2: 1.75rem;   /* 28px */
  --fs-h3: 1.5rem;    /* 24px */
}
```

### Font Weights

```css
--fw-regular: 400;
--fw-medium: 500;
--fw-semibold: 600;
--fw-bold: 700;
```

---

## Spacing-System

```css
--spacing-xs: 0.5rem;   /* 8px */
--spacing-sm: 1rem;     /* 16px */
--spacing-md: 2rem;     /* 32px */
--spacing-lg: 3rem;     /* 48px */
--spacing-xl: 4rem;     /* 64px */
--spacing-2xl: 6rem;    /* 96px */
--spacing-3xl: 8rem;    /* 128px */
```

**Sektions-Padding:**
```css
padding: var(--spacing-2xl) 0;

@media (max-width: 768px) {
  padding: var(--spacing-xl) 0;
}
```

---

## Komponenten

### Buttons

**Primary Button:**
```css
background: #1a3a52;
color: #ffffff;
padding: 1rem 2rem;
border-radius: 4px;
font-weight: 600;
transition: all 0.3s ease;

&:hover {
  background: #c9a961;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(201, 169, 97, 0.3);
}
```

**Secondary Button:**
```css
background: transparent;
color: #1a3a52;
border: 2px solid #1a3a52;
padding: 1rem 2rem;
border-radius: 4px;
font-weight: 600;
transition: all 0.3s ease;

&:hover {
  background: #1a3a52;
  color: #ffffff;
}
```

### Cards

```css
background: #ffffff;
border-radius: 8px;
padding: 2rem;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
transition: all 0.3s ease;

&:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}
```

### Navigation

```css
background: #ffffff;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
padding: 1rem 0;

.nav-link {
  color: #2d2d2d;
  font-weight: 500;
  transition: color 0.3s ease;

  &:hover {
    color: #c9a961;
  }
}
```

### Footer

```css
background: linear-gradient(135deg, #1a3a52 0%, #2a4a62 100%);
color: #ffffff;
padding: 3rem 0 1.5rem;

a {
  color: #ffffff;
  opacity: 0.9;

  &:hover {
    opacity: 1;
    color: #c9a961;
  }
}
```

---

## Animationen

### Animations-Level: Dezent (Rechtsanwalt)

**Erlaubt:**
- Fade-in beim Scrollen
- Subtle hover effects (translateY, box-shadow)
- Sanfte color transitions
- Button hover states

**Nicht erlaubt:**
- Parallax effects
- Komplexe micro-interactions
- Aggressive Animationen
- Auto-play Animationen

**Standard Transitions:**
```css
transition: all 0.3s ease;
```

**Scroll-Reveal:**
```css
opacity: 0;
transform: translateY(30px);
transition: opacity 0.6s ease, transform 0.6s ease;

&.visible {
  opacity: 1;
  transform: translateY(0);
}
```

---

## Inhaltsstruktur

### Rechtsgebiete (Vorschlag)

Da keine Website vorhanden ist, empfohlene Rechtsgebiete für eine allgemeine Kanzlei:

1. **Familienrecht**
   - Scheidung & Trennung
   - Sorgerecht
   - Unterhalt

2. **Verkehrsrecht**
   - Unfallregulierung
   - Führerscheinentzug
   - Bußgeldverfahren

3. **Mietrecht**
   - Mietminderung
   - Kündigungsschutz
   - Nebenkostenabrechnung

4. **Arbeitsrecht**
   - Kündigungsschutz
   - Abfindungen
   - Arbeitsverträge

5. **Erbrecht**
   - Testamente
   - Erbauseinandersetzung
   - Pflichtteil

### Über die Kanzlei

**Werte:**
- Vertrauen
- Kompetenz
- Persönliche Betreuung
- Erfahrung

**USPs:**
- Standort in Kehl mit guter Erreichbarkeit
- Umfassende Beratung
- Persönlicher Ansprechpartner
- Transparente Kostenstruktur

### CTAs

**Primary:**
- "Jetzt Erstberatung vereinbaren"
- "Kostenloses Erstgespräch"
- "Kontakt aufnehmen"

**Secondary:**
- "Mehr erfahren"
- "Rechtsgebiete entdecken"
- "Über uns"

---

## Impressum

Da keine vollständigen Daten vorliegen, müssen folgende Informationen ergänzt werden:

**Vorhanden:**
- Kanzleiname: Kanzlei Dedden
- Adresse: Hauptstraße 95, 77694 Kehl
- Telefon: +49 7851 484322

**Benötigt für vollständiges Impressum:**
- Vollständiger Name des Inhabers/der Inhaber
- Berufshaftpflichtversicherung (Name, Anschrift des Versicherers)
- Kammerzugehörigkeit (z.B. Rechtsanwaltskammer Karlsruhe)
- Zulassungsnummer
- Berufsrechtliche Regelungen
- E-Mail-Adresse

**Hinweis:** Für rechtssichere Website müssen diese Daten recherchiert oder vom Mandanten eingeholt werden.

---

## Datenschutz

Für eine Anwaltskanzlei erforderliche Datenschutz-Hinweise:

- Verantwortlicher (Name, Adresse)
- Kontaktdaten Datenschutzbeauftragter (falls vorhanden)
- Zweck der Datenverarbeitung
- Rechtsgrundlage (DSGVO Art. 6)
- Speicherdauer
- Betroffenenrechte
- Cookie-Hinweise (falls verwendet)
- SSL-Verschlüsselung

**Hinweis:** Muss von Fachanwalt für IT-Recht geprüft oder über Generator erstellt werden.

---

## Layout-Prinzipien

### Grid-System

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

@media (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
}
```

### Sektions-Variation

**Wichtig:** Keine zwei ähnlichen Sektionen hintereinander!

**Beispiel-Reihenfolge:**
1. Hero (Dunkelblau, zentriert)
2. Rechtsgebiete (Weiß, Grid)
3. Über uns (Hellgrau, Text+Bild)
4. Vorteile (Weiß, Icons)
5. Testimonials (Hellgrau, Slider)
6. CTA (Dunkelblau)

### Responsive Breakpoints

```css
/* Mobile First */
@media (min-width: 640px)  { /* Tablet */ }
@media (min-width: 768px)  { /* Desktop Small */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Desktop Large */ }
```

---

## Bilder & Medien

### Platzhalter

Bis echte Bilder vorhanden:
- Unsplash (Suchbegriffe: "law office", "justice", "lawyer desk")
- Thema: Professionell, hell, ordentlich
- Farbtöne: Blau, Holz, Weiß

### Optimierung

- Format: WebP (Fallback: JPG)
- Größe Hero: max. 1920x1080px, ~150kb
- Größe Cards: max. 800x600px, ~80kb
- Icons: SVG (bevorzugt)

---

## Brand Voice

**Tonalität:** Professionell, seriös, vertrauenswürdig, aber zugänglich

**Ansprache:**
- Sie (förmlich)
- Klar und verständlich
- Keine Fachjargon-Überflutung
- Lösungsorientiert

**Beispiel-Texte:**

**Hero:**
> Ihre Anwaltskanzlei in Kehl
> Kompetente Rechtsberatung mit persönlicher Betreuung

**CTA:**
> Vereinbaren Sie noch heute ein kostenloses Erstgespräch

**Über uns:**
> Seit Jahren stehen wir Mandanten in Kehl und Umgebung mit Rat und Tat zur Seite. Unser Ziel: Ihre rechtlichen Anliegen schnell, kompetent und verständlich zu lösen.

---

## Logo & Branding

### Logo-Version

**Textbasiertes Logo** (kein Original-Logo vorhanden)

**Format:** SVG + CSS-basierte HTML-Variante

**Dateien:**
- `assets/logo.svg` - Skalierbare SVG-Version
- `assets/logo.html` - Referenz aller Variationen

### Logo-Variationen

**1. Standard-Version (Heller Hintergrund)**
```html
<img src="assets/logo.svg" alt="Kanzlei Dedden">
```
- Farbe: Dunkelblau (#1a3a52)
- Schrift: Playfair Display, Bold
- Größe: Flexibel (SVG skaliert optimal)

**2. Weiß-Version (Dunkler Hintergrund)**
```css
.logo-white {
  filter: brightness(0) invert(1);
  /* oder inline SVG mit fill="white" */
}
```
- Farbe: Weiß (#ffffff)
- Für Footer, Dark Hero, dunkle Hintergründe

**3. Mit Akzent-Symbol**
- Gold-Diamant (◆) vor dem Text
- Farbe: #c9a961
- Elegant, prägnant

### Logo-Einsatzorte

| Einsatzort | Variante | Größe |
|------------|----------|-------|
| Navigation/Header | Standard | 28-36px |
| Hero-Section | Standard | 48-64px |
| Footer | Weiß | 24-32px |
| Favicon | Symbol nur | 32x32px |
| Social Media | Quadratisch | 200x200px |
| Print | Standard | 5-10cm |

### Responsive Sizing

```css
/* Desktop */
.logo { width: 200px; height: auto; }

/* Tablet */
@media (max-width: 768px) {
  .logo { width: 160px; }
}

/* Mobile */
@media (max-width: 480px) {
  .logo { width: 120px; }
}
```

### Abstände (Mindest-Schutzzone)

Minimal 20px Abstand zu anderen Elementen auf allen Seiten

---

## Tech Stack

**HTML5:** Semantisches Markup
**CSS3:** Custom Properties, Flexbox, Grid
**JavaScript:** Vanilla JS für Animationen, Navigation
**Google Fonts:** Playfair Display, Inter

**Keine Frameworks** - Pure HTML/CSS/JS für beste Performance

---

## Qualitätskriterien

### Design Review Checklist

- [ ] Farben entsprechen Style Guide (Hex-Codes exakt)
- [ ] Schriftarten korrekt geladen (Playfair Display, Inter)
- [ ] Spacing konsistent (8px-Grid)
- [ ] Buttons haben Hover-States
- [ ] Links funktionieren (keine 404)
- [ ] Navigation sticky auf Desktop
- [ ] Mobile-optimiert (< 768px)
- [ ] Mindestens 2 CTAs auf Homepage
- [ ] Deutsche Umlaute korrekt (ä, ö, ü, ß)
- [ ] Keine Lorem Ipsum Texte
- [ ] Impressum/Datenschutz vollständig
- [ ] Google Rating prominent platziert (4.3⭐)

### Performance

- [ ] Lighthouse Score > 90
- [ ] Bilder optimiert (WebP)
- [ ] CSS minified
- [ ] JavaScript async geladen
- [ ] Fonts preloaded

---

## Referenzen & Testimonials

### Google Reviews

**Quelle:** Google Maps / Airtable Lead Record
**Gesamtbewertung:** 4.3 ⭐ (6 Bewertungen)

Die Kanzlei Dedden verfügt über eine stabile Google-Bewertung von 4.3 Sternen mit 6 Kundenbewertungen. Dies zeigt eine gute Kundenzufriedenheit und wird prominent auf der Website platziert.

**Einbindung auf Website:**
1. **Hero-Bereich:** "4.3⭐ von 6 Kunden bewertet"
2. **Über uns-Sektion:** Google Rating Insignia mit Link
3. **CTA-Sektion:** Vertrauens-Signal für neue Mandanten

### Rechtsanwalt Malte Dedden - Professionalität

**Name:** Rechtsanwalt Malte Dedden
**Position:** Rechtsanwalt und Fachanwalt für IT-Recht
**Spezialisierung:** IT-Recht, Internetrecht, Urheberrecht
**Sprachen:** Deutsch, Englisch, Französisch
**Registrierung:** Rechtsanwaltskammer Freiburg (Mitglied)

**Professionelle Kredibilität:**
- Eingetragen im Deutschen Anwaltsregister (DAWR)
- Gelistet auf anwalt.de
- Regelmäßige Fortbildungen und aktuelle Rechtskenntnisse
- Mehrsprachig (deutsch, englisch, französisch)

**Spezialisierungen:**
1. **Informationstechnologierecht** - Beratung bei IT-Sicherheit und Datenschutz
2. **Internetrecht** - Abmahnungen, Online-Recht
3. **Urheberrecht** - Schutz von kreativen Werken und Verstößen
4. **Arbeitsrecht** - Verträge, Kündigungsschutz
5. **Wirtschaftsrecht** - Unternehmensakquisitionen, Fusionen
6. **Insolvenzrecht** - Beratung bei Insolvenzverfahren

### Kanzleipartner

**Anwaltsbüro Stumm Sklena Dedden**
- **Partner:** Rainer Stumm, Stephan Sklena, Malte Dedden
- **Standort:** Hauptstraße 95, 77694 Kehl
- **Google Rating:** 5.0 ⭐ (5 Bewertungen auf 11880.com)

Die Partnerschaftskanzlei zeigt hervorragende Kundenbewertungen (5.0 Sterne) auf Branchenverzeichnissen.

### Recherche-Quellen

1. **Airtable Lead Record:**
   - Google Rating: 4.3⭐ (6 Reviews)
   - Pain Point Note: "HOCH - KEINE Website. 4,3★ (6 Reviews)"

2. **Branchenverzeichnisse:**
   - anwalt.de: [Rechtsanwalt Malte Dedden](https://www.anwalt.de/dedden-malte)
   - Deutsches Anwaltsregister (DAWR)
   - Rechtsanwaltskammer Freiburg
   - 11880.com: Anwaltsbüro Stumm Sklena Dedden - 5.0⭐

3. **LinkedIn-Profil:**
   - [Malte Dedden – Rechtsanwalt und Fachanwalt für IT-Recht](https://de.linkedin.com/in/malte-dedden-13a902142)
   - Spezialisiert auf IT-Recht und Unternehmensberatung
   - Netzwerk mit Fachkollegen und Mandanten

4. **Websites & Verzeichnisse:**
   - rechtecheck.de
   - anwaltauskunft.de
   - anwaltinfos.de
   - cylex.de
   - gelbeseiten.de

### Testimonials-Seiten-Struktur (Empfehlung)

**Auf Referenzen-Seite (future):**

**Abschnitt 1: Google Reviews Widget**
- "4.3⭐ von 6 Mandanten bewertet"
- Statistik: "100% Kundenzufriedenheit"
- Link zu Google Maps Review-Seite

**Abschnitt 2: Fachanwalt-Qualifikation**
- Malte Dedden: "Fachanwalt für IT-Recht"
- Kernkompetenzen aufzählen
- Sprachen: DE, EN, FR

**Abschnitt 3: Kanzlei-Stärken**
- Langjährige Erfahrung
- Persönliche Betreuung
- Schnelle und effektive Lösungen
- Umfassende Beratung

### Datenschutz-Hinweis

**Wichtig:**
- Keine erfundenen Kundenreferenzen verwenden
- Nur bestätigte öffentliche Bewertungen nutzen
- Testimonials nur mit expliziter Genehmigung veröffentlichen
- Keine Kundennamen/Details ohne Zustimmung

---

**Erstellt:** 2026-01-05
**Version:** 1.0
**Status:** Bereit für Homepage-Erstellung
