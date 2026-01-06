# Style Guide - Gasthaus Biergarten Brandeck

## Firmeninformationen

| Feld | Wert |
|------|------|
| **Firmenname** | Gasthaus Biergarten Brandeck |
| **Branche** | Restaurant / Biergarten |
| **Adresse** | Zeller Straße 44, 77654 Offenburg |
| **Telefon** | 0781/30352 |
| **E-Mail** | katarina.henninger@googlemail.com |
| **Inhaber/Verantwortlich** | Katarina Henninger |
| **Steuernummer** | 14229/79017 |
| **Google Rating** | 4.4 ⭐ (1305 Bewertungen) |

---

## Farbpalette

### Primärfarben (aus Original-Website extrahiert)

| Farbe | Hex-Code | RGB | Verwendung |
|-------|----------|-----|------------|
| **Goldgelb (Primary)** | `#FFC107` | rgb(255, 193, 7) | Buttons, Akzente, Headlines, Divider |
| **Weiß** | `#FFFFFF` | rgb(255, 255, 255) | Button-Text, Hintergründe |
| **Schwarz** | `#000000` | rgb(0, 0, 0) | Body-Text |
| **Weiß (90% Opacity)** | `rgba(255, 255, 255, 0.9)` | - | Sekundärer Text auf dunklem Hintergrund |

### Empfohlene erweiterte Palette

| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| **Dunkelbraun** | `#3E2723` | Headlines, Footer-Hintergrund |
| **Warmbeige** | `#F5F0EB` | Helle Sektionen |
| **Holzbraun** | `#5D4037` | Akzentelemente |
| **Cremeweiß** | `#FFFDE7` | Karten-Hintergründe |
| **Naturgrün** | `#558B2F` | Biergarten-Akzente (optional) |

---

## Typografie

### Schriftarten (Original)

| Kategorie | Schriftart | Fallback |
|-----------|------------|----------|
| **Headlines/Titel** | Baskervville | Georgia, serif |
| **Body/Fließtext** | Roboto | Arial, sans-serif |

### Empfohlene Schriftgrößen

| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 (Hero) | 56px / 3.5rem | 36px / 2.25rem |
| H2 (Sections) | 42px / 2.625rem | 28px / 1.75rem |
| H3 (Cards) | 24px / 1.5rem | 20px / 1.25rem |
| Body | 18px / 1.125rem | 16px / 1rem |
| Small | 14px / 0.875rem | 14px / 0.875rem |

### Schriftgewichte

- **Headlines:** 400 (Baskervville ist elegant in Regular)
- **Body:** 400, 500
- **Buttons:** 500

---

## Spacing-System

| Name | Wert | Verwendung |
|------|------|------------|
| xs | 4px / 0.25rem | Micro-Gaps |
| sm | 8px / 0.5rem | Enge Abstände |
| md | 16px / 1rem | Standard |
| lg | 24px / 1.5rem | Komponenten-Gaps |
| xl | 32px / 2rem | Sektions-Padding |
| 2xl | 48px / 3rem | Große Abstände |
| 3xl | 64px / 4rem | Hero-Padding |
| 4xl | 96px / 6rem | Sektions-Trennung |

---

## Button-Styles

### Primary Button
```css
.btn-primary {
  background-color: #FFC107;
  color: #FFFFFF;
  padding: 12px 24px;
  border-radius: 4px;
  font-weight: 500;
  font-family: 'Roboto', sans-serif;
  text-transform: none;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: #FFB300;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 193, 7, 0.3);
}
```

### Secondary Button (Outline)
```css
.btn-secondary {
  background-color: transparent;
  color: #FFC107;
  border: 2px solid #FFC107;
  padding: 12px 24px;
  border-radius: 4px;
}
```

---

## Komponenten

### Divider/Trennlinien
```css
.divider {
  height: 3px;
  width: 60px;
  background-color: #FFC107;
  margin: 16px auto;
}
```

### Cards
- Hintergrund: Weiß oder Cremeweiß
- Border-Radius: 8px
- Box-Shadow: 0 4px 20px rgba(0, 0, 0, 0.08)
- Hover: Transform translateY(-4px) + erhöhter Schatten

---

## Content - Über uns

### Hauptbeschreibung

**Restaurant mit wundervollem Biergarten**

Unsere deutsche Küche bietet eine Vielzahl an köstlicher, liebevoll zubereiteter Leckerbissen!

Genießen Sie unsere große Auswahl an knackigen Salaten und regionalen, frischen Gerichten.

Vom Klassiker, wie Wiener Schnitzel & Rumpsteak über Wild- und Fischgerichten bis hin zu einer Vielfalt an vegetarischen Gerichten, ganz sicher ist etwas dabei, was Ihren Gaumen erfreuen wird.

Lassen Sie sich zwischendurch oder als Nachspeise von unseren hausgemachten Waffeln & unseren himmlischen Desserts verführen.

Damit keine Langweile bei unseren kleinsten Gästen aufkommt und Sie genüsslich schlemmen können, haben wir eine Kinderecke mit vielen Beschäftigungsmöglichkeiten eingerichtet.

**Wir freuen uns sehr darauf Sie bei uns zu einem Mittagessen, einem Abendessen oder zu einer Veranstaltung begrüßen zu dürfen!**

### USPs / Highlights

- 🍽️ Deutsche Küche mit regionalen Produkten
- 🌳 Wunderschöner Biergarten
- 🥗 Große Auswahl an frischen Salaten
- 🥩 Klassiker: Wiener Schnitzel, Rumpsteak
- 🐟 Wild- und Fischgerichte
- 🥬 Vegetarische Vielfalt
- 🧇 Hausgemachte Waffeln & himmlische Desserts
- 👶 Kinderecke vorhanden
- 🐕 Hundefreundlich (Vierbeiner willkommen!)
- 📦 Speisen zum Mitnehmen
- 🎉 Räumlichkeiten für Feiern & Veranstaltungen

---

## Öffnungszeiten

| Tag | Öffnungszeiten | Küche |
|-----|----------------|-------|
| **Montag** | 10:30 - 23:00 | 10:30 - 14:30, 17:30 - 21:30 |
| **Dienstag** | Geschlossen | - |
| **Mittwoch** | 10:30 - 23:00 | 11:30 - 14:30, 17:00 - 21:30 |
| **Donnerstag** | 10:30 - 23:00 | 11:30 - 14:30, 17:00 - 21:30 |
| **Freitag** | 10:30 - 23:00 | 11:30 - 14:30, 17:00 - 21:30 |
| **Samstag** | 10:30 - 23:00 | 11:30 - 21:30 |
| **Sonntag** | 11:30 - 21:30 | 11:30 - 21:00 |

---

## Speisekarte

### Downloads
- **Hauptspeisekarte (PDF):** `assets/speisekarte.pdf`
- **Mittagstisch (Bild):** `assets/mittagstisch.jpg`

### Mittagstisch (Beispiel - KW 01/2026)

**Montag:**
1. Tomaten-Zucchinigemüse mit Schafskäse, Reis und Salat - 9,90 €
2. Rinderpaprikagulasch mit Nudeln und Salat - 10,90 €

**Dienstag:** Feiertag (geschlossen)

**Mittwoch:**
1. Fettuccini in Olivenöl mit Knoblauch, Paprika - 9,90 €
2. Braten in Portweinsoße mit Rotkraut und Kartoffelpüree, Salat - 10,90 €

**Donnerstag:**
1. Schupfnudeln mit Gemüse, Champignons und Salat - 9,90 €
2. Schnitzel mit Nudeln und Salat - 10,90 €

**Freitag:**
1. Bunter Gemüseteller mit Ei und Salzkartoffeln, Salat - 9,90 €
2. Hausgemachte Fischklößchen mit Gemüse, Salzkartoffeln und Salat - 10,90 €

---

## Bilder & Assets

### Hero-Bild
- **URL:** `https://cdn.website.dish.co/media/b7/e1/208656/brandeck-biergarten-2.jpg`
- **Beschreibung:** Biergarten mit Tischen unter Bäumen

### Galerie-Bilder (Download-URLs)

| # | URL | Beschreibung |
|---|-----|--------------|
| 1 | `https://cdn.website.dish.co/media/6b/32/4180749/Gasthaus-Biergarten-Brandeck-Hauptloge-hangt-drauen-PNG.jpg` | Hauptlogo/Schild |
| 2 | `https://cdn.website.dish.co/media/66/f3/1552433/Gasthaus-Biergarten-Brandeck-IMG-20190601-WA0001.jpg` | Biergarten |
| 3 | `https://cdn.website.dish.co/media/6e/09/1552408/Gasthaus-Biergarten-Brandeck-IMG-20190601-WA0002.jpg` | Biergarten |
| 4 | `https://cdn.website.dish.co/media/8c/27/1552418/Gasthaus-Biergarten-Brandeck-IMG-20190601-WA0000.jpg` | Biergarten |
| 5 | `https://cdn.website.dish.co/media/6a/49/1552428/Gasthaus-Biergarten-Brandeck-IMG-20190601-WA0011.jpg` | Ambiente |
| 6 | `https://cdn.website.dish.co/media/d8/2f/1552438/Gasthaus-Biergarten-Brandeck-IMG-20180623-WA0013.jpg` | Gericht |
| 7 | `https://cdn.website.dish.co/media/91/8f/1552443/Gasthaus-Biergarten-Brandeck-IMG-20180627-WA0010.jpg` | Gericht |
| 8 | `https://cdn.website.dish.co/media/14/43/1552644/Gasthaus-Biergarten-Brandeck-20180629-201008.jpg` | Ambiente |
| 9 | `https://cdn.website.dish.co/media/0b/ce/1552499/Gasthaus-Biergarten-Brandeck-20190104-160444.jpg` | Innenraum |
| 10 | `https://cdn.website.dish.co/media/62/e8/1552448/Gasthaus-Biergarten-Brandeck-IMG-20181220-WA0018.jpg` | Gericht |
| 11 | `https://cdn.website.dish.co/media/7d/6d/1552494/Gasthaus-Biergarten-Brandeck-20190104-160711.jpg` | Innenraum |
| 12 | `https://cdn.website.dish.co/media/93/3a/1552520/Gasthaus-Biergarten-Brandeck-20190104-160418.jpg` | Ambiente |
| 13 | `https://cdn.website.dish.co/media/3b/e1/1552480/Gasthaus-Biergarten-Brandeck-20190920-232622.jpg` | Gericht |
| 14 | `https://cdn.website.dish.co/media/a9/c8/1552602/Gasthaus-Biergarten-Brandeck-20181124-145637.jpg` | Gericht |
| 15 | `https://cdn.website.dish.co/media/2d/58/1552547/Gasthaus-Biergarten-Brandeck-20181220-212702.jpg` | Dessert/Waffeln |
| 16 | `https://cdn.website.dish.co/media/08/28/1552630/Gasthaus-Biergarten-Brandeck-20180203-154445.jpg` | Ambiente |
| 17 | `https://cdn.website.dish.co/media/bb/ca/1552613/Gasthaus-Biergarten-Brandeck-20180304-154036.jpg` | Ambiente |

### Logo
- **Kein separates Logo-File gefunden** - Das Hauptbild zeigt ein hängendes Holzschild mit dem Namen
- **Empfehlung:** Text-Logo erstellen mit "Brandeck" in Baskervville + goldgelbem Akzent

---

## Team

**Keine Team-Seite auf der Website vorhanden.**

- **Bekannte Person:** Katarina Henninger (Inhaberin/Verantwortliche)
- **Inhaber (seit 2020):** Familie Henninger

---

## Referenzen

### Bewertungsübersicht

| Plattform | Rating | Anzahl Bewertungen |
|-----------|--------|-------------------|
| **Google** | ⭐ 4.4/5 | 1.280+ |
| **TripAdvisor** | ⭐ 4.0/5 | 69 |
| **Facebook** | ⭐ 4.0/5 | 252 |
| **golocal** | ⭐ 5.0/5 | 8 |
| **Foursquare** | 7.8/10 | 14 |

### Auszeichnung

**Im Jahr 2005 wurde der Biergarten der "Brandeck" zum schönsten Biergarten der gesamten Ortenau gewählt.**

### Ausgewählte Kundenstimmen

#### 1. Albert Fahney
- **Quelle:** golocal
- **Datum:** August 2021
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "Offenburgs schönster Biergarten und liberalstes Gasthaus."

#### 2. Markus Trautmann
- **Quelle:** golocal
- **Datum:** Dezember 2019
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "Sehr gutes Essen, fantastischer Biergarten."

#### 3. Anna Uhl
- **Quelle:** golocal
- **Datum:** Oktober 2018
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "Sehr gutes Essen und freundliches Personal."

#### 4. Der Hannes
- **Quelle:** golocal
- **Datum:** Mai 2019
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "Wunderschöner Biergarten mit feinem Essen, angenehmen Preisen und freundlichem Personal."

#### 5. Gaumenfreundinnen
- **Quelle:** speisekarte.de
- **Datum:** März 2017
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "Lockere Atmosphäre. Sehr schmackhaftes Essen. Höfliche Bedienung."

#### 6. TripAdvisor-Rezensent
- **Quelle:** TripAdvisor
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "Meiner Meinung nach hat das Brandeck einen der schönsten, wenn nicht der schönste Biergarten in Offenburg. Das Essen gut bürgerlich ist meist handwerklich gut gekocht und es scheinen stets frische Produkte zu sein."

#### 7. Internationaler Gast
- **Quelle:** TripAdvisor (englisch)
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
> "This was a great choice! The service was excellent, and they have a good selection of beer and food. The schnitzel is huge (you only need 1). The prices are very reasonable as well."

### Was Gäste besonders loben

- 🌳 **Schönster Biergarten in Offenburg** (mehrfach genannt)
- 🥩 **Riesige Schnitzel** - legendär unter Stammgästen
- 🍺 **Gute Bierauswahl** - regionale Spezialitäten
- 💰 **Faire Preise** - gutes Preis-Leistungs-Verhältnis
- 👨‍🍳 **Frische, handwerklich gute Küche**
- 😊 **Freundliches Personal**

### Hinweis zur Umsetzung

**Empfehlung für Website:**
Da keine Personenfotos der Rezensenten verfügbar sind, wird empfohlen:
1. **Google Reviews Widget** mit 4.4⭐ Rating und Anzahl der Bewertungen
2. **Zitat-Karussell** mit den besten Kundenstimmen (ohne Fotos, mit Initialen)
3. **Auszeichnungs-Badge** "Schönster Biergarten der Ortenau 2005"

**Assets:** Keine Testimonial-Fotos vorhanden (anonyme Bewertungen).

---

## Rechtliche Texte

### Impressum-Daten
- **Telefon:** 0781/30352
- **E-Mail:** katarina.henninger@googlemail.com
- **Steuernummer:** 14229/79017
- **Verantwortliche Person:** Katarina Henninger

### Datenschutzerklärung
Vollständiger Text liegt vor (DSGVO-konform) - siehe Original-Website oder separates Dokument.

Enthält:
- Allgemeine Datenverarbeitung
- Cookie-Richtlinie (Adobe Analytics, Google Analytics)
- Facebook Pixel Information
- Betroffenenrechte nach DSGVO

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Biergarten-Erlebnis"** - Ein Layout das die Gemütlichkeit und das Outdoor-Feeling eines traditionellen deutschen Biergartens einfängt:

- **Hero:** Vollbild-Foto des Biergartens mit leichtem Parallax-Effekt, darüber der Name in eleganter Serifenschrift
- **Content-Sektionen:** Abwechselnd helle (Cremeweiß) und bildreiche Bereiche
- **Speisekarten-Sektion:** Gestaltung wie eine echte Speisekarte auf Holz-Textur-Hintergrund

### 2. Signature-Effekt

**Warme Holz- & Natur-Ästhetik:**
- Subtile Holzmaserung-Texturen als Hintergrund-Akzente
- Sanfte Schatten die Tiefe erzeugen (keine harten Kanten)
- Goldgelbe (#FFC107) Akzent-Linien als Trennelemente
- Abgerundete Foto-Ecken mit leichtem Sepia-Touch bei Hover

### 3. Animations-Level: **Moderat**

Passend für ein einladendes Restaurant:
- **Scroll-Reveal:** Sektionen soft einblenden (fade-up, 0.6s)
- **Image-Hover:** Leichtes Zoom (1.05) + Warmton-Overlay
- **Button-Hover:** Sanfte Farbverschiebung + subtle Lift
- **Parallax:** Nur im Hero, dezent (0.3 Faktor)
- **KEINE:** Schnelle Animationen, blinkende Elemente, komplexe Transitions

### 4. Besondere Sektionen

| Sektion | Beschreibung |
|---------|--------------|
| **Hero mit Öffnungsstatus** | Live-Anzeige "Heute geöffnet bis 22:00" wie im Original |
| **Speisekarten-Karussell** | Swipeable Kategorie-Karten (Vorspeisen, Hauptgerichte, Desserts) |
| **Biergarten-Galerie** | Masonry-Grid mit Hover-Effekt, zeigt die Atmosphäre |
| **Tisch reservieren** | Prominenter CTA mit Kalender-Icon |
| **Google Reviews Widget** | 4.4 ⭐ Rating mit echten Bewertungs-Snippets |
| **Anfahrt + Parken** | Karte mit Parkplatz-Info (Biergarten hat eigenen Parkplatz) |
| **Veranstaltungen** | Hinweis auf Räumlichkeiten für Feiern mit Bild |

### 5. Visuelle Hierarchie

```
1. HERO (100vh)
   └── Biergarten-Foto + Name + "Heute geöffnet"

2. WILLKOMMEN (Cremeweiß)
   └── Kurze Einleitung + 3 USP-Icons

3. SPEISEKARTE (Holz-Textur Hintergrund)
   └── Kategorie-Karten + PDF-Download

4. GALERIE (Dunkel)
   └── Masonry-Grid der besten Fotos

5. ÜBER UNS (Cremeweiß)
   └── Geschichte + Kinderecke + Hundefreundlich

6. RESERVIERUNG (Gold-Akzent)
   └── CTA + Telefon + Formular-Link

7. ÖFFNUNGSZEITEN (Weiß)
   └── Tages-Übersicht + Küchen-Zeiten

8. ANFAHRT (Karte)
   └── Google Maps + Adresse + Parken

9. FOOTER (Dunkelbraun)
   └── Kontakt + Social + Legal
```

### 6. Spezielle UI-Elemente für Restaurants

- **"Heute geöffnet" Badge:** Grüner Punkt + Text, prominent im Header
- **Mittagstisch-Banner:** Wenn wochentags → Sticky-Banner mit Tagesgerichten
- **Zum Mitnehmen Icon:** Telefon-Icon mit "Jetzt bestellen" für Take-away
- **Kinderecke-Badge:** 👶 Symbol bei "Familienfreundlich"
- **Hundefreundlich-Badge:** 🐕 Symbol prominent platzieren

---

## Technische Empfehlungen

### Fonts einbinden
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baskervville:ital@0;1&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
```

### CSS Custom Properties
```css
:root {
  /* Colors */
  --color-primary: #FFC107;
  --color-primary-dark: #FFB300;
  --color-white: #FFFFFF;
  --color-black: #000000;
  --color-dark-brown: #3E2723;
  --color-warm-beige: #F5F0EB;
  --color-wood-brown: #5D4037;
  --color-cream: #FFFDE7;

  /* Typography */
  --font-heading: 'Baskervville', Georgia, serif;
  --font-body: 'Roboto', Arial, sans-serif;

  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;
  --space-4xl: 6rem;

  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;

  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 20px rgba(0, 0, 0, 0.12);
  --shadow-lg: 0 8px 40px rgba(0, 0, 0, 0.16);
}
```

---

*Style Guide erstellt: Januar 2026*
*Quelle: http://biergarten-brandeck.eatbu.com/*
