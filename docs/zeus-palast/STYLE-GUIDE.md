# Style Guide - Zeus Palast

## Firmeninfos

| Feld | Wert |
|------|------|
| **Name** | Zeus Palast |
| **Slogan** | Griechische Spezialitäten |
| **Branche** | Restaurant (Griechisch) |
| **Inhaber** | Paraskevi Mangoufi |
| **Adresse** | Lange Straße 43, 77652 Offenburg |
| **Telefon** | +49 781 96723768 |
| **E-Mail** | info@zeuspalast.de |
| **Website** | www.zeuspalast.de |
| **Google Rating** | 4.5 (740 Bewertungen) |

---

## Farbpalette

### Primärfarben (vom Logo abgeleitet)

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Gold/Bernstein** | `#C8943D` | Primärfarbe, Buttons, Akzente |
| **Dunkelbraun** | `#6B4423` | Text auf hellem Hintergrund, Logo-Schrift |
| **Hellgold** | `#D4A84B` | Hover-States, Highlights |
| **Cremeweiß** | `#FDF8F0` | Hintergründe |

### Sekundärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Orange-Rot** | `#E94F1D` | Akzentfarbe (aus Website), CTAs |
| **Dunkelgrau** | `#333333` | Fließtext |
| **Warmweiß** | `#FFFBF5` | Sektions-Hintergründe |
| **Terrakotta** | `#B85C38` | Sekundäre Akzente |

### Griechisches Farbschema (ergänzend)

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Ägäis-Blau** | `#1E5B8C` | Optionale Akzente, Icons |
| **Olivgrün** | `#6B7B3C` | Natur-Elemente, frische Akzente |
| **Mediterranes Weiß** | `#FFFFFF` | Saubere Flächen |

---

## Typografie

### Empfohlene Schriften

| Typ | Schrift | Fallback | Verwendung |
|-----|---------|----------|------------|
| **Headlines** | Playfair Display | Georgia, serif | H1, H2, Hero-Text |
| **Subheadlines** | Cormorant Garamond | Times New Roman, serif | H3, H4, Zitate |
| **Body** | Lato | -apple-system, sans-serif | Fließtext, Navigation |
| **Akzent** | Cinzel | serif | Logo-ähnliche Elemente |

### Schriftgrößen

| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 | 3.5rem (56px) | 2.5rem (40px) |
| H2 | 2.5rem (40px) | 2rem (32px) |
| H3 | 1.75rem (28px) | 1.5rem (24px) |
| Body | 1.125rem (18px) | 1rem (16px) |
| Small | 0.875rem (14px) | 0.875rem (14px) |

---

## Spacing-System

```
--space-xs: 0.25rem (4px)
--space-sm: 0.5rem (8px)
--space-md: 1rem (16px)
--space-lg: 1.5rem (24px)
--space-xl: 2rem (32px)
--space-2xl: 3rem (48px)
--space-3xl: 4rem (64px)
--space-4xl: 6rem (96px)
```

---

## Button-Styles

### Primary Button
```css
background: linear-gradient(135deg, #C8943D 0%, #D4A84B 100%);
color: #FFFFFF;
padding: 1rem 2rem;
border-radius: 4px;
font-weight: 600;
text-transform: uppercase;
letter-spacing: 1px;
box-shadow: 0 4px 15px rgba(200, 148, 61, 0.3);
```

### Secondary Button
```css
background: transparent;
color: #C8943D;
border: 2px solid #C8943D;
padding: 1rem 2rem;
border-radius: 4px;
```

### CTA Button (Reservierung)
```css
background: #E94F1D;
color: #FFFFFF;
padding: 1.25rem 2.5rem;
border-radius: 4px;
font-weight: 700;
```

---

## Logo

### Dateien
- **Original**: `assets/logo.jpg`
- **URL**: https://www.zeuspalast.de/wp-content/uploads/cropped-Zeuspalast-Logo.jpg

### Logo-Beschreibung
Das Logo zeigt eine Zeus-Büste (griechischer Gott) mit lockigem Haar und Bart in einer warmen Gold/Bernstein-Farbpalette. Der Schriftzug "ZEUS PALAST" ist in einer eleganten Serif-Schrift mit "GRIECHISCHE SPEZIALITÄTEN RESTAURANT" als Untertitel.

### Logo-Verwendung
- Auf dunklem Hintergrund: Original-Logo
- Auf hellem Hintergrund: Logo mit erhöhtem Kontrast
- Favicon: Nur Zeus-Kopf

---

## Bilder

### Verfügbare Assets

| Datei | Beschreibung |
|-------|--------------|
| `assets/logo.jpg` | Vollständiges Logo mit Zeus-Büste |
| `assets/biergarten.jpg` | Außenbereich/Biergarten |
| `assets/mittagsbuffet.jpg` | Mittagsbuffet-Ankündigung |
| `assets/speisekarte-1.jpg` bis `speisekarte-18.jpg` | Alle Seiten der Speisekarte |

### Bild-URLs (Original-Website)
- Logo: https://www.zeuspalast.de/wp-content/uploads/cropped-Zeuspalast-Logo.jpg
- Biergarten: https://www.zeuspalast.de/wp-content/uploads/biergarten.jpeg
- Mittagsbuffet: https://www.zeuspalast.de/wp-content/uploads/mittagsbuffet.jpg

### Galerie-Bilder (Restaurant & Gerichte)
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/Zeuspalast.JPG
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/Restaurant1.jpg
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/Restaurant2.jpg
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/Restaurant3.jpg
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/Restaurant4.jpg
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/image1.jpg
- https://www.zeuspalast.de/wp-content/uploads/photo-gallery/image7.jpg

---

## Öffnungszeiten

| Tag | Zeit |
|-----|------|
| Montag | 11:30 - 14:00 Uhr, 17:30 - 22:30 Uhr |
| **Dienstag** | **Ruhetag** |
| Mittwoch - Sonntag | 11:30 - 14:00 Uhr, 17:30 - 22:30 Uhr |

**Mittagsbuffet**: Montags, mittwochs und donnerstags (außer Feiertagen) von 11:30 - 14:00 Uhr

---

## Inhalte

### Über das Restaurant

Das Restaurant Zeus Palast wurde 2010 neu eröffnet und wird von der Familie Mangoufis geführt. Die Gäste schätzen die familiäre Atmosphäre und die freundliche Bedienung.

Das Restaurant bietet seinen Gästen ca. 140 Plätze. Weitere Plätze finden Sie bei gutem Wetter im Biergarten.

Sämtliche Gerichte sind auch außer Haus erhältlich. Dieser Service wird gerne für private Feiern angeboten, inklusive Buffet-Zusammenstellung zur Abholung.

Für Feiern steht ein Raum für bis zu 90 Personen zur Verfügung.

### Besondere Angebote

1. **Mittagsbuffet** - Mo, Mi, Do (außer Feiertage) 11:30-14:00 Uhr
2. **Biergarten** - Bei schönem Wetter im Innenhof
3. **Außer-Haus-Service** - Alle Gerichte zum Mitnehmen
4. **Veranstaltungen** - Räumlichkeiten für bis zu 90 Personen
5. **Weihnachtsfeiern** - Spezielle Arrangements für Firmen/Gruppen

### Navigation (Seiten)

- Startseite
- Aktuelles
- Restaurant
- Anfahrt
- Kontakt
- Datenschutz
- Impressum

---

## Speisekarte

Die Speisekarte ist als Bild-Serie verfügbar:
- `assets/speisekarte-1.jpg` bis `assets/speisekarte-18.jpg`

**Empfehlung für neue Website:**
- Speisekarte als Bild-Galerie oder PDF zum Download anbieten
- Alternativ: Kategorien extrahieren und als HTML darstellen

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Mediterranean Elegance"** - Kombination aus klassisch-griechischer Ästhetik und moderner Gastro-Website:

- **Hero**: Vollbild-Slider mit Restaurant-Atmosphäre, überlagert mit goldenem Zeus-Logo
- **Sektionen**: Abwechselnd helle (Cremeweiß) und dunkle (Dunkelbraun) Hintergründe
- **Grid-Layouts**: Asymmetrische Bildanordnungen für Gerichte
- **Sticky-Navigation**: Gold-akzentuiert mit transparentem Scroll-Effekt

### 2. Signature-Effekt

**"Golden Glow"** - Subtiler goldener Schimmer-Effekt:
- Gold-Gradient-Overlays auf Bildern beim Hover
- Goldene Linien als Sektions-Trenner (griechisches Mäander-Muster)
- Sanfte Gold-Schatten auf Cards und Buttons
- Griechische Säulen-Elemente als dezente Deko

### 3. Animations-Level: **Moderat**

Passend für Restaurant-Branche:
- Sanftes Fade-in für Sektionen beim Scrollen
- Hover-Effekte auf Speisekarten-Bilder (leichter Zoom)
- Smooth-Scroll Navigation
- Parallax-Effekt auf Hero-Bild
- Card-Hover mit Schatten-Verstärkung
- Animierte Öffnungszeiten-Anzeige

### 4. Besondere Sektionen

1. **Hero mit Reservierungs-CTA**
   - Großes Atmosphären-Bild vom Restaurant
   - Prominent: "Jetzt Tisch reservieren" Button
   - Öffnungszeiten-Badge

2. **Speisekarten-Galerie**
   - Lightbox-Ansicht der Speisekarten-Seiten
   - Alternative: Kategorien als elegante Cards

3. **"Unsere Spezialitäten" Showcase**
   - 3-4 Signature-Gerichte mit großen Bildern
   - Kurze Beschreibung und Preis

4. **Mittagsbuffet-Highlight**
   - Eigene Sektion mit Timer/Uhrzeit-Anzeige
   - "Heute verfügbar" Badge wenn zutreffend

5. **Biergarten-Sektion**
   - Atmosphärische Outdoor-Bilder
   - Wetter-Icon oder saisonale Verfügbarkeit

6. **Google Reviews Integration**
   - 4.5 Sterne prominent anzeigen
   - "740 zufriedene Gäste" als Social Proof
   - Link zu Google Maps/Reviews

7. **Anfahrt mit interaktiver Karte**
   - Google Maps Embed
   - Parkplatz-Hinweise
   - ÖPNV-Verbindungen

8. **Footer mit griechischem Flair**
   - Mäander-Bordüre
   - Kontaktdaten + Social Links
   - Mini-Speisekarten-Preview

### 5. Visuelle Akzente

- **Griechische Ornamente**: Dezente Mäander-Muster als Bordüren
- **Olivenzweig-Illustrationen**: Als Trennelemente
- **Terrakotta-Texturen**: Für spezielle Sektionen
- **Amphoren/Säulen**: Als dezente Hintergrund-Elemente

---

## Impressum (Volltext)

**Restaurant Zeus Palast**
Paraskevi Mangoufi
Lange Straße 43
77652 Offenburg

**Telefon**: +49(0)781 / 9672 3768
**E-Mail**: info@zeuspalast.de
**Internet**: www.zeuspalast.de

**Inhaber**: Paraskevi Mangoufi

**Zuständige Aufsichtsbehörde**: Gewerbeamt Stadt Offenburg

**Umsatzsteuer-Identifikationsnummer** gemäß § 27 a Umsatzsteuergesetz: DE 24458/7167

**Inhaltlich Verantwortlicher** gemäß § 55 Abs. 2 RStV: Paraskevi Mangoufi

**Haftungshinweis**: Trotz sorgfältiger inhaltlicher Kontrolle übernehmen wir keine Haftung für die Inhalte externer Links. Für den Inhalt der verlinkten Seiten sind ausschließlich deren Betreiber verantwortlich.

---

## Datenschutz (Volltext)

### 1. Datenschutz auf einen Blick

**Allgemeine Hinweise**
Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können.

**Datenerfassung auf dieser Website**

*Wer ist verantwortlich für die Datenerfassung auf dieser Website?*
Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Dessen Kontaktdaten können Sie dem Abschnitt „Hinweis zur Verantwortlichen Stelle" in dieser Datenschutzerklärung entnehmen.

*Wie erfassen wir Ihre Daten?*
Ihre Daten werden zum einen dadurch erhoben, dass Sie uns diese mitteilen. Hierbei kann es sich z. B. um Daten handeln, die Sie in ein Kontaktformular eingeben.

Andere Daten werden automatisch oder nach Ihrer Einwilligung beim Besuch der Website durch unsere IT-Systeme erfasst. Das sind vor allem technische Daten (z. B. Internetbrowser, Betriebssystem oder Uhrzeit des Seitenaufrufs).

*Wofür nutzen wir Ihre Daten?*
Ein Teil der Daten wird erhoben, um eine fehlerfreie Bereitstellung der Website zu gewährleisten. Andere Daten können zur Analyse Ihres Nutzerverhaltens verwendet werden.

*Welche Rechte haben Sie bezüglich Ihrer Daten?*
Sie haben jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten. Sie haben außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen.

### 2. Allgemeine Hinweise und Pflichtinformationen

**Datenschutz**
Die Betreiber dieser Seiten nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend den gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung.

**Hinweis zur verantwortlichen Stelle**
Die verantwortliche Stelle für die Datenverarbeitung auf dieser Website ist:

Paraskevi Mangoufi
Lange Straße 43
77652 Offenburg

Telefon: +49(0)781 / 9672 3768
E-Mail: info@zeuspalast.de

**Speicherdauer**
Soweit innerhalb dieser Datenschutzerklärung keine speziellere Speicherdauer genannt wurde, verbleiben Ihre personenbezogenen Daten bei uns, bis der Zweck für die Datenverarbeitung entfällt.

**SSL- bzw. TLS-Verschlüsselung**
Diese Seite nutzt aus Sicherheitsgründen und zum Schutz der Übertragung vertraulicher Inhalte eine SSL- bzw. TLS-Verschlüsselung.

---

## Team

**Inhaber/Familie**: Familie Mangoufis (geführt von Paraskevi Mangoufi)

*Hinweis: Keine individuellen Team-Fotos auf der Website verfügbar. Bei Bedarf Team-Fotos vom Kunden anfordern oder generische "Unser Team"-Sektion ohne individuelle Fotos erstellen.*

---

## Referenzen

### Bewertungsübersicht

| Plattform | Bewertung | Anzahl Reviews |
|-----------|-----------|----------------|
| **Google** | ⭐ 4.5/5 | 774 Bewertungen |
| **TripAdvisor** | ⭐ 4.2/5 | 74 Bewertungen |
| **Foodpearl** | ⭐ 4/5 | 190 Bewertungen |

### Ausgewählte Kundenstimmen

#### 1. Michaela Schaefer ⭐⭐⭐⭐⭐
> "Vielen Dank für das leckere Essen zu Silvester. Sehr schön angerichtet auch bei to go."

*Quelle: Google Reviews (März 2021)*

---

#### 2. Steffen Sauer ⭐⭐⭐⭐⭐
> "Tolles Ambiente, leckeres Essen, freundliches Personal, Preis/Leistung in Ordnung."

*Quelle: Google Reviews (Oktober 2020)*

---

#### 3. Uwe Hauser ⭐⭐⭐⭐⭐
> "Aufmerksames und freundliches Personal, eine schöne Atmosphäre und sehr leckeres Essen bei einem für Offenburg sehr guten Preis-Leistungsverhältnis. Eine gute Entscheidung und von uns eine Empfehlung für Freunde der griechischen Küche. Wir kommen bestimmt wieder."

*Quelle: Google Reviews (Oktober 2020)*

---

#### 4. Daniel Wagner ⭐⭐⭐⭐⭐
> "Sehr gutes Essen, große Portionen und sehr freundliches Personal. Eines der besten Restaurants in Offenburg!"

*Quelle: Google Reviews (Juli 2020)*

---

#### 5. Stammgast (TripAdvisor)
> "Ein sehr empfehlenswerter Grieche in Offenburg! Klare Empfehlung. Herzlicher Service, leckeres Essen, das frisch zubereitet wird."

*Quelle: TripAdvisor*

---

#### 6. Lokaler Gast
> "Sehr guter Grieche, gerne wieder! 1/4 l Wein, Wasser, Griechischer Mocca, Tzaziki, Pita und Gyros Metaxa - Alles wunderbar. Service freundlich und nett. Beim Bezahlen ein gratis Ouzo. Angenehmes Ambiente im Innenhof Gastgarten."

*Quelle: TripAdvisor*

---

#### 7. Familiengast
> "Eine Bekannte sagte sogar, dass es ihr besser gefalle wie in Griechenland selbst! Dieses Restaurant ist einfach in Allem Spitze."

*Quelle: Google Reviews*

---

### Häufig gelobte Aspekte

| Kategorie | Feedback |
|-----------|----------|
| **Essen** | Typisch griechisch, große Portionen, selbstgemachtes Tzatziki |
| **Service** | Freundlich, aufmerksam, schnell |
| **Ambiente** | Schöne Atmosphäre, gemütlicher Biergarten |
| **Preis-Leistung** | Fair, Mittagsbuffet ab €8,90 |
| **Veranstaltungen** | Ideal für größere Gruppen |

### Hinweis für Website-Umsetzung

Da keine Profilbilder der Reviewer verfügbar sind (Privacy-Schutz auf Review-Plattformen), empfehlen wir:

1. **Google Reviews Widget** - Rating-Summary mit Sternebewertung prominent anzeigen
2. **Zitat-Karussell** - Ausgewählte Testimonials als Slider ohne Fotos
3. **Initialen-Avatare** - Stilisierte Buchstaben-Avatare (z.B. "MS" für Michaela Schaefer)
4. **Google-Link** - "Mehr Bewertungen auf Google" Button

---

## Zusammenfassung für Entwicklung

| Aspekt | Empfehlung |
|--------|------------|
| **Stil** | Elegant, warm, mediterran |
| **Hauptfarbe** | Gold/Bernstein (#C8943D) |
| **Akzent** | Orange-Rot (#E94F1D) |
| **Schriften** | Playfair Display + Lato |
| **Animationen** | Moderat (fade-in, hover, parallax) |
| **Besonderheit** | Griechische Ornamente, goldene Akzente |
| **Wichtigste CTAs** | Reservierung, Speisekarte, Mittagsbuffet |
