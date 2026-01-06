# Style Guide: Nazar Kebap - Gasthaus

## Firmeninformationen

### Basisdaten
- **Firmenname:** Nazar Kebap - Gasthaus
- **Branche:** Restaurant (Türkisch, Italienisch, Deutsch)
- **Adresse:** Saarlandstraße 2, 77652 Offenburg
- **Telefon:** +49 781 96643005
- **E-Mail:** Nicht bekannt
- **Öffnungszeiten:** Täglich 09:00 - 00:00 Uhr

### Online-Präsenz
- **Facebook:** [facebook.com/nazarkebaphaus](https://www.facebook.com/nazarkebaphaus/)
- **Instagram:** [@nazar_offenburg](https://www.instagram.com/nazar_offenburg/)
- **Google Rating:** 4.0 (360 Bewertungen)
- **Restaurant Guru:** 4.3 (346 Bewertungen)

### Standort-Besonderheit
Direkt gegenüber vom Bahnhof Offenburg - ideal für Pendler und Reisende.

---

## Farbpalette

### Primärfarben (aus Restaurant-Branding)
Das Restaurant verwendet eine markante **Blau-Rot-Kombination** in der Außenbeleuchtung und Beschilderung.

| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| **Neon-Blau** | `#00B4FF` | Außenbeleuchtung, Akzente, Highlight-Elemente |
| **Nazar-Rot** | `#E31E24` | Logo-Schriftzug "NAZAR", CTA-Buttons |
| **Warm-Weiß** | `#FFF8F0` | Hintergrund, Lesbarkeit |
| **Nacht-Schwarz** | `#0A0A0A` | Kontrast, Dark Sections |

### Sekundärfarben (Türkische Küche / Warm)
| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| **Döner-Gold** | `#D4A84B` | Akzente, Speisekarten-Highlights |
| **Gewürz-Orange** | `#E87A35` | Hover-States, Warm-Akzente |
| **Fladenbrot-Beige** | `#F5E6D3` | Hintergründe, Cards |
| **Kebab-Braun** | `#6B4423` | Texte auf hellem Hintergrund |

### Hintergrundfarben
| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| **Helles Beige** | `#FAF7F2` | Haupthintergrund |
| **Warmes Grau** | `#F0EBE3` | Section-Alternierung |
| **Dunkles Blau** | `#0D1B2A` | Hero-Section, Footer |

---

## Typografie

### Empfohlene Schriftarten

**Headlines (Display):**
```css
font-family: 'Playfair Display', 'Georgia', serif;
```
- Elegant, einladend für Restaurant-Atmosphäre
- Verwendung: H1, H2, Speisekarten-Kategorien

**Body Text:**
```css
font-family: 'Inter', 'Helvetica Neue', sans-serif;
```
- Modern, gut lesbar
- Verwendung: Fließtext, Beschreibungen

**Akzente/Preise:**
```css
font-family: 'DM Sans', sans-serif;
```
- Clean, für Preise und CTAs

### Schriftgrößen
| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 (Hero) | 56px | 36px |
| H2 (Section) | 42px | 28px |
| H3 (Card Title) | 24px | 20px |
| Body | 18px | 16px |
| Small | 14px | 14px |

---

## Spacing-System

```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
--space-4xl: 6rem;     /* 96px */
```

---

## Button-Styles

### Primary Button (Rot)
```css
.btn-primary {
  background: linear-gradient(135deg, #E31E24 0%, #C41A1F 100%);
  color: #FFFFFF;
  padding: 16px 32px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(227, 30, 36, 0.3);
  transition: all 0.3s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(227, 30, 36, 0.4);
}
```

### Secondary Button (Blau)
```css
.btn-secondary {
  background: transparent;
  border: 2px solid #00B4FF;
  color: #00B4FF;
  padding: 14px 30px;
  border-radius: 8px;
}
.btn-secondary:hover {
  background: #00B4FF;
  color: #FFFFFF;
}
```

---

## Speisekarte / Angebot

### Hauptkategorien
1. **Döner & Kebap** - Spezialität des Hauses
2. **Pizza** - Italienische Klassiker
3. **Grillgerichte** - Türkische Grillspezialitäten
4. **Yufka / Dürüm** - Wraps
5. **Beilagen & Salate**
6. **Getränke** (inkl. Bier)

### Beliebte Gerichte (aus Bewertungen)
- **Yufka** - "Für 7,50€ bekommt man einen fetten großen Yufka der sehr lecker schmeckt"
- **Döner Kebap** - Hausgemacht, reichlich Fleisch
- **Pizza Margherita** - Italienischer Klassiker
- **Grillspieße** - Saftig gegrillt

### Preisklasse
€ - €€ (1-10€ pro Person) - Günstig und reichhaltig

---

## Über das Restaurant

### Beschreibung
Nazar Kebap - Gasthaus ist ein familienfreundliches Restaurant in Offenburg, das türkische, italienische und deutsche Küche vereint. Das Ecklokal direkt gegenüber vom Bahnhof besticht durch seine einladende Atmosphäre und die markante blaue Neonbeleuchtung, die es zum Blickfang macht.

### Alleinstellungsmerkmale (USPs)
1. **Zentrale Lage** - Direkt am Bahnhof, perfekt für Reisende
2. **Lange Öffnungszeiten** - Täglich 9-24 Uhr
3. **Vielfältige Küche** - Türkisch, Italienisch, Deutsch
4. **Großzügige Portionen** - Viel Essen für kleines Geld
5. **Schneller Service** - Ideal für die Mittagspause

### Atmosphäre
- Gemütliches Gasthaus-Ambiente
- Multikulturelle, einladende Atmosphäre
- Schnelles, freundliches Personal

---

## Kundenbewertungen (Highlights)

> "Best damn kebab I have EVER eaten. Enough donor meat, plenty of veg, loads of hot dripping sauce, and nice bread to hold it all in. Good service and friendly to boot."

> "Für 7,50 Euro bekommt man einen fetten großen Yufka der sehr lecker schmeckt."

> "Very friendly kebab shop doing pizzas and chips and all the usual fare - just across from the station."

---

## Verfügbare Assets

### Bilder (in assets/ Ordner)
| Datei | Beschreibung |
|-------|--------------|
| `cover.jpg` | Restaurant bei Nacht mit blauer Neonbeleuchtung (Hero-Bild) |
| `logo-fb.jpg` | Facebook Profilbild (Gebäude-Außenansicht) |
| `food.jpg` | Knusprige Beilagen/Nuggets |

### Logo
**Status:** Kein offizielles Logo-File verfügbar
**Empfehlung:** Text-Logo erstellen basierend auf dem "NAZAR" Schriftzug:
- Schriftart: Bold Sans-Serif (z.B. Montserrat Black)
- Farbe: Rot (#E31E24) auf dunklem Hintergrund
- Alternativ: Blau (#00B4FF) als Akzent

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept
**"Neon Nights meets Gasthaus Gemütlichkeit"**
- Hero mit dem Nachtfoto des Restaurants (blaue Beleuchtung)
- Kontrastreiche Sektionen: Dunkle Hero → Helle Speisekarte → Dunkler CTA
- Großzügige Food-Fotografie als visuelle Trenner

### 2. Signature-Effekt
**Neon-Glow Akzente:**
```css
.neon-glow {
  text-shadow: 0 0 10px rgba(0, 180, 255, 0.5),
               0 0 20px rgba(0, 180, 255, 0.3),
               0 0 30px rgba(0, 180, 255, 0.2);
}
.neon-border {
  box-shadow: 0 0 15px rgba(0, 180, 255, 0.4),
              inset 0 0 15px rgba(0, 180, 255, 0.1);
}
```
- Dezenter Neon-Effekt für Überschriften und Karten
- Passt zur blauen Außenbeleuchtung des Restaurants

### 3. Animations-Level: **Moderat**
- Sanfte Fade-In Animationen beim Scrollen
- Hover-Effekte auf Speisekarten-Karten
- Dezente Parallax-Effekte im Hero
- KEINE übertriebenen Animationen - Restaurant-Atmosphäre soll einladend bleiben

### 4. Besondere Sektionen

**A) Hero mit Nachtfoto:**
- Vollbild-Foto des Restaurants bei Nacht
- Overlay mit Gradient (transparent → dunkel)
- Große Headline: "Willkommen bei Nazar"
- CTA: "Speisekarte ansehen" + "Jetzt bestellen"

**B) Speisekarten-Grid:**
- Bento-Grid Layout mit Kategorien
- Jede Kategorie als Karte mit Icon
- Hover zeigt 2-3 beliebte Gerichte

**C) Google Reviews Integration:**
- 4.0 Sterne prominent anzeigen
- 2-3 ausgewählte Bewertungen als Slider
- Link zu Google Maps

**D) Anfahrt-Sektion:**
- Split-Screen: Google Maps + Infos
- USP hervorheben: "Direkt am Bahnhof"
- Öffnungszeiten prominent

**E) CTA-Banner:**
- Dunkler Hintergrund mit Neon-Akzent
- "Hunger? Komm vorbei oder ruf an!"
- Telefon-Button + Adresse

### 5. Mobile-First Prioritäten
1. Telefon-Button sticky im Header
2. Speisekarte als erstes scrollbar
3. Google Maps direkt erreichbar
4. Öffnungszeiten prominent

---

## Impressum-Daten

```
Nazar Kebap - Gasthaus
Saarlandstraße 2
77652 Offenburg
Deutschland

Telefon: +49 781 96643005

[E-Mail und weitere rechtliche Angaben müssen vom Inhaber ergänzt werden]
```

---

## Datenschutz-Hinweise

Da keine Website existiert, müssen Datenschutzbestimmungen neu erstellt werden.
Mindestens erforderlich:
- Verantwortliche Stelle (Adresse)
- Kontaktdaten
- Hosting-Informationen
- Cookie-Hinweise (falls verwendet)
- Google Maps Einbindung (Datenschutz-Hinweis erforderlich)

---

## Zusammenfassung für Entwicklung

| Aspekt | Empfehlung |
|--------|------------|
| **Stil** | Modern-warm mit Neon-Akzenten |
| **Primärfarbe** | Blau #00B4FF + Rot #E31E24 |
| **Schriften** | Playfair Display + Inter |
| **Hero** | Nachtfoto mit blauer Beleuchtung |
| **USP** | Bahnhofsnähe, lange Öffnungszeiten |
| **CTA-Fokus** | Telefon + Speisekarte |
| **Animationen** | Moderat, einladend |
