# Style Guide: Rebstüble

> Weinstube & Restaurant in Offenburg - Regionale Küche mit Weinkultur

---

## Firmendaten

| Feld | Wert |
|------|------|
| **Name** | Rebstüble |
| **Typ** | Restaurant / Weinstube |
| **Küche** | Regionale Küche (Baden) |
| **Adresse** | Durbacher Str. 32, 77654 Offenburg |
| **Telefon** | +49 781 93995533 |
| **Email** | Nicht bekannt |
| **Google Rating** | 4.5 ⭐ (200 Bewertungen) |

### Öffnungszeiten

| Tag | Zeiten |
|-----|--------|
| Montag | 16:30 - 23:00 |
| Dienstag | Ruhetag |
| Mittwoch | 16:30 - 23:00 |
| Donnerstag | 16:30 - 23:00 |
| Freitag | 16:30 - 23:00 |
| Samstag | 16:30 - 23:00 |
| Sonntag | 16:30 - 23:00 |

---

## Farbpalette

> Design-Konzept: Warme Weinstube-Atmosphäre mit badischer Tradition

### Primärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Weinrot** | `#722F37` | Primary - Headlines, CTA-Buttons, Akzente |
| **Dunkelrot** | `#5A252C` | Primary Dark - Hover-States, Footer |
| **Creme-Weiß** | `#FDF8F3` | Background - Haupthintergrund |

### Sekundärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Gold/Bernstein** | `#C9A227` | Akzente, Icons, Sterne, Highlights |
| **Dunkelbraun** | `#3D2314` | Text - Überschriften, wichtiger Text |
| **Warmgrau** | `#6B5B4F` | Body-Text, Beschreibungen |

### Neutrale Farben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Off-White** | `#FAF7F2` | Karten-Hintergrund |
| **Sandbeige** | `#E8DFD4` | Borders, Trennlinien |
| **Holzton** | `#8B7355` | Subtile Akzente |

### Gradient

```css
/* Hero-Overlay */
background: linear-gradient(135deg, rgba(114, 47, 55, 0.9) 0%, rgba(61, 35, 20, 0.85) 100%);

/* Warme Atmosphäre */
background: linear-gradient(to bottom, #FDF8F3 0%, #FAF7F2 100%);
```

---

## Typografie

### Schriftarten

| Typ | Font | Fallback | Verwendung |
|-----|------|----------|------------|
| **Display** | Playfair Display | Georgia, serif | Logo, H1, Hero |
| **Headings** | Cormorant Garamond | Georgia, serif | H2, H3, Sektions-Titel |
| **Body** | Source Sans 3 | system-ui, sans-serif | Fließtext, Navigation |

### Font-Einbindung

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&family=Source+Sans+3:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### Schriftgrößen

| Element | Desktop | Mobile | Gewicht |
|---------|---------|--------|---------|
| H1 (Hero) | 4rem (64px) | 2.5rem (40px) | 600 |
| H2 (Sektion) | 2.5rem (40px) | 2rem (32px) | 600 |
| H3 (Untertitel) | 1.75rem (28px) | 1.5rem (24px) | 500 |
| H4 | 1.25rem (20px) | 1.125rem (18px) | 500 |
| Body | 1rem (16px) | 1rem (16px) | 400 |
| Small | 0.875rem (14px) | 0.875rem (14px) | 400 |
| Caption | 0.75rem (12px) | 0.75rem (12px) | 400 |

---

## Spacing-System

```css
:root {
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */
  --space-4xl: 6rem;     /* 96px */

  --section-padding: 5rem;  /* 80px */
  --container-max: 1200px;
  --container-padding: 1.5rem;
}
```

---

## Komponenten

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: #722F37;
  color: #FDF8F3;
  padding: 0.875rem 2rem;
  border-radius: 4px;
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
  border: none;
}

.btn-primary:hover {
  background: #5A252C;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(114, 47, 55, 0.3);
}

/* Secondary Button (Outline) */
.btn-secondary {
  background: transparent;
  color: #722F37;
  border: 2px solid #722F37;
  padding: 0.75rem 1.75rem;
  border-radius: 4px;
}

.btn-secondary:hover {
  background: #722F37;
  color: #FDF8F3;
}

/* Gold Accent Button */
.btn-gold {
  background: #C9A227;
  color: #3D2314;
}
```

### Cards

```css
.card {
  background: #FAF7F2;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 2px 8px rgba(61, 35, 20, 0.08);
  border: 1px solid #E8DFD4;
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(61, 35, 20, 0.12);
}
```

### Navigation

```css
.nav {
  background: rgba(253, 248, 243, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #E8DFD4;
}

.nav-link {
  color: #3D2314;
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 500;
  font-size: 0.9375rem;
  letter-spacing: 0.3px;
}

.nav-link:hover {
  color: #722F37;
}
```

---

## Bilder & Assets

### Logo

**Status:** Kein Logo verfügbar - Text-Logo erstellen

**Empfehlung für Text-Logo:**
```
Schrift: Playfair Display, 600
Farbe: #722F37 (Weinrot)
Zusatz: Kleine Weinrebe als Icon-Element
```

### Bildsprache

Da keine Bilder verfügbar sind, Stock-Empfehlungen:

| Typ | Beschreibung | Quellen |
|-----|--------------|---------|
| **Hero** | Gemütliche Weinstube-Atmosphäre, gedimmtes Licht, Weingläser | Unsplash: wine cellar, wine bar |
| **Ambiente** | Holztische, rustikale Einrichtung, Kerzen | Unsplash: cozy restaurant |
| **Essen** | Regionale badische Küche, Flammkuchen, Vesper | Unsplash: german cuisine, tarte flambée |
| **Wein** | Weinflaschen, Weinberg (Durbach), Weingläser | Unsplash: wine, vineyard |

### Speisekarte

**Status:** Nicht online verfügbar - Platzhalter-Kategorien basierend auf typischer Weinstube:

- Vorspeisen & Salate
- Flammkuchen-Variationen
- Vesper & Kleinigkeiten
- Hauptgerichte
- Desserts
- Weine (Durbacher Weine)

---

## Website-Struktur

### Seiten

1. **Startseite** (index.html)
   - Hero mit Atmosphäre-Bild
   - Über uns / Willkommen
   - Highlights der Speisekarte
   - Öffnungszeiten
   - Kontakt-CTA

2. **Speisekarte** (speisekarte.html)
   - Kategorien mit Gerichten
   - Wein-Empfehlungen
   - Hinweis: Aktuelle Karte vor Ort

3. **Über uns** (ueber-uns.html)
   - Geschichte / Philosophie
   - Das Team (falls bekannt)
   - Weinstube-Tradition

4. **Kontakt** (kontakt.html)
   - Kontaktformular
   - Google Maps
   - Öffnungszeiten
   - Reservierungshinweis

5. **Impressum** (impressum.html)
6. **Datenschutz** (datenschutz.html)

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Warme Weinstube-Ästhetik"**
- Großzügige weiße Räume mit weinroten Akzenten
- Asymmetrische Hero-Section mit überlappendem Text
- Horizontale Divider mit dezenten Weinreben-Ornamenten

### 2. Signature-Effekt

**Elegante Rahmen & Ornamente**
- Dezente Weinreben-Muster als SVG-Ornamente
- Goldene Akzent-Linien bei Sektionstrennern
- Leicht strukturierter Papier-Hintergrund (subtle texture)

```css
/* Ornament-Divider */
.divider-ornament {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.divider-ornament::before,
.divider-ornament::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #C9A227, transparent);
}
```

### 3. Animations-Level: Moderat

Passend für ein gemütliches Restaurant:

| Element | Animation |
|---------|-----------|
| **Scroll-Reveal** | Sanftes Fade-up (0.6s ease) |
| **Hover auf Cards** | Leichter Lift + Schatten |
| **Bilder** | Zoom-in on hover (scale 1.05) |
| **Navigation** | Smooth color transitions |
| **CTA-Buttons** | Subtle lift + glow |

```css
/* Scroll Animation */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.6s ease-out;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### 4. Besondere Sektionen

1. **"Unser Wein" Hero-Modul**
   - Split-Screen: Bild links, Text rechts
   - Durbacher Weine hervorheben
   - Dezente Parallax-Bewegung

2. **Öffnungszeiten als stilvolle Karte**
   - Rustikaler Rahmen-Stil
   - Handschrift-Font für "Herzlich willkommen"
   - Weinrot auf Creme

3. **Google Reviews Integration**
   - 4.5 Sterne prominent zeigen
   - 2-3 ausgewählte Bewertungen
   - Link zu Google Maps

4. **Atmosphäre-Galerie**
   - Wenn Bilder verfügbar: Masonry-Grid
   - Lightbox für Vollansicht
   - Hover-Effekt mit Overlay

---

## Besondere Hinweise

### Name-Bedeutung
"Rebstüble" = "Reben-Stübchen" - kleines, gemütliches Weinlokal
→ Design soll diese Gemütlichkeit widerspiegeln

### Lage
Durbacher Straße → Nähe zum Weinanbaugebiet Durbach
→ Verbindung zur badischen Weinkultur betonen

### USP-Potenzial
- Regionale Küche
- Badische Weine
- Gemütliche Atmosphäre
- Gutes Google-Rating (4.5)

---

## CSS-Variablen Zusammenfassung

```css
:root {
  /* Farben */
  --color-primary: #722F37;
  --color-primary-dark: #5A252C;
  --color-secondary: #C9A227;
  --color-text: #3D2314;
  --color-text-muted: #6B5B4F;
  --color-bg: #FDF8F3;
  --color-bg-alt: #FAF7F2;
  --color-border: #E8DFD4;

  /* Typografie */
  --font-display: 'Playfair Display', Georgia, serif;
  --font-heading: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Source Sans 3', system-ui, sans-serif;

  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;
  --space-4xl: 6rem;

  /* Layout */
  --container-max: 1200px;
  --section-padding: 5rem;
  --border-radius: 8px;

  /* Schatten */
  --shadow-sm: 0 2px 8px rgba(61, 35, 20, 0.08);
  --shadow-md: 0 4px 16px rgba(61, 35, 20, 0.12);
  --shadow-lg: 0 8px 24px rgba(61, 35, 20, 0.16);

  /* Transitions */
  --transition-fast: 0.2s ease;
  --transition-normal: 0.3s ease;
  --transition-slow: 0.6s ease;
}
```

---

## Referenzen / Testimonials

> Quelle: Google Reviews via [foodpearl.com](https://rebstuble.foodpearl.com/)

### Gesamtbewertung

| Plattform | Rating | Anzahl |
|-----------|--------|--------|
| **Google** | ⭐⭐⭐⭐⭐ 4.6 | ~230 Bewertungen |
| **Tripadvisor** | ⭐⭐⭐⭐⭐ 5.0 | 9 Bewertungen |

### Ausgewählte Testimonials

#### 1. Christian Junker ⭐⭐⭐⭐⭐
> "Toller Wirt, authentisches Lokal mit prima badischer Küche am Fuße des Schwarzwalds."

---

#### 2. H-P Herb ⭐⭐⭐⭐⭐
> "Schnitzel sind hier echt Top... Ingo's Empfehlung (Cordon bleu) war hervorragend!"

---

#### 3. Martin Schauer ⭐⭐⭐⭐⭐
> "Service freundlich, schnell und kundenorientierte Haltung... Fazit: Top!"

---

#### 4. Wolfgang Baumgartner ⭐⭐⭐⭐⭐
> "Preis-Leistung super, Essen schmeckt sehr gut, gut bürgerlich."

---

#### 5. Larissa Hahn ⭐⭐⭐⭐⭐
> "Dieses Lokal ist sehr sehr gut, das Schnitzel ist sehr zu empfehlen."

---

#### 6. Patrick Pöschl ⭐⭐⭐⭐
> "Gut bürgerliche Küche mit ordentlichen Portionen. Sehr freundlicher Service."

---

### Highlights aus Bewertungen

| Kategorie | Feedback |
|-----------|----------|
| **Essen** | "Mega Portionen, sehr lecker" • "Schnitzel ist ein Traum" • "Koch versteht sein Handwerk" |
| **Service** | "Sehr netter Service" • "Freundliches Personal" • "Kundenorientiert" |
| **Preis** | "Preis-Leistung sehr gut" • "Für den kleinen Geldbeutel okay" |
| **Ambiente** | "Sehr gemütlich" • "Authentisches Lokal" • "Sehr sauber" |

### Hinweise zur Verwendung

- **Keine Personenfotos verfügbar** - Bewertungen sind anonym/pseudonym
- **Empfehlung:** Google Rating prominent zeigen (4.6 ⭐)
- **Alternative:** Testimonials als Zitate mit Initialen darstellen
- **Link zu Google Reviews** für Authentizität einbinden

---

## Team

**Status:** Nicht bekannt - keine Team-Informationen verfügbar

---

## Impressum-Daten (für rechtliche Seiten)

```
Rebstüble
Durbacher Str. 32
77654 Offenburg

Telefon: +49 781 93995533

(Weitere rechtliche Angaben wie Inhaber, USt-IdNr. etc.
müssen vom Betreiber ergänzt werden)
```

---

*Style Guide erstellt am: Januar 2025*
*Basierend auf: Branchenanalyse (Restaurant/Weinstube), keine bestehende Website*
