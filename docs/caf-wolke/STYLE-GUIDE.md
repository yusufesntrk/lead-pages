# Style Guide - Café Wolke

## Firmeninformationen

### Basisdaten
- **Firmenname:** Café Wolke
- **Inhaberin:** Esra Yagmur Türker
- **Branche:** Café / Konditorei / Frühstücksrestaurant
- **Gründung:** Nicht bekannt

### Kontaktdaten
- **Adresse:** Amalie-Hofer-Straße 2, 77656 Offenburg
- **Telefon:** +49 781 55776
- **E-Mail:** Nicht bekannt
- **Instagram:** [@cafe.wolke](https://www.instagram.com/cafe.wolke/) (2.194 Follower, 880 Posts)

### Öffnungszeiten
| Tag | Zeiten |
|-----|--------|
| Montag | Geschlossen |
| Dienstag - Freitag | 13:00 - 18:00 Uhr |
| Samstag - Sonntag & Feiertage | 09:00 - 18:00 Uhr |

### Bewertungen
- **Google:** 4.8 / 5.0 (227 Bewertungen)
- **Restaurant Guru:** 4.8 / 5.0 (228 Bewertungen)

---

## Farbpalette

Da keine Website existiert, wurde das Farbschema basierend auf dem beschriebenen Interieur (Holz + beige Töne, modern, warm) und dem Markennamen "Wolke" entwickelt.

### Primärfarben
| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| Warmes Beige | `#E8DDD4` | Hintergrund, Flächen |
| Sanftes Braun | `#8B7355` | Primäre Akzente, Buttons |
| Dunkles Holz | `#4A3728` | Überschriften, Text |

### Sekundärfarben
| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| Cremeweiß | `#FBF9F7` | Kartenfarbe, Hintergründe |
| Wolkengrau | `#B8C4CE` | Dezente Akzente, Icons |
| Warmes Gold | `#C9A962` | Hover-States, Highlights |

### Akzentfarben
| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| Türkisches Rot | `#B5533E` | CTA-Buttons, Wichtiges |
| Avocado-Grün | `#7D9A6F` | Frische-Akzente, Tags |
| Kaffeebraun | `#6F4E37` | Sekundäre Buttons |

### Text- und UI-Farben
| Farbe | Hex-Code | Verwendung |
|-------|----------|------------|
| Textfarbe Dunkel | `#2D2418` | Haupttext |
| Textfarbe Hell | `#FBF9F7` | Text auf dunklem Hintergrund |
| Textfarbe Muted | `#6B5D4D` | Sekundärer Text |
| Randfarbe | `#D4C8BC` | Trennlinien, Rahmen |

---

## Typografie

### Schriftarten
| Typ | Schriftart | Fallback |
|-----|------------|----------|
| Überschriften | **Playfair Display** | Georgia, serif |
| Fließtext | **Lato** | -apple-system, sans-serif |
| Akzente | **Dancing Script** | cursive |

### Schriftgrößen
| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 | 56px / 3.5rem | 40px / 2.5rem |
| H2 | 40px / 2.5rem | 32px / 2rem |
| H3 | 28px / 1.75rem | 24px / 1.5rem |
| Body | 18px / 1.125rem | 16px / 1rem |
| Small | 14px / 0.875rem | 14px / 0.875rem |

### Schriftstärken
- Light: 300
- Regular: 400
- Medium: 500
- Bold: 700

---

## Spacing-System

### Basis: 8px Grid
| Name | Wert | Verwendung |
|------|------|------------|
| xs | 4px | Micro-Abstände |
| sm | 8px | Icon-Abstände |
| md | 16px | Element-Padding |
| lg | 24px | Komponenten-Abstände |
| xl | 32px | Sektions-Padding |
| 2xl | 48px | Große Abstände |
| 3xl | 64px | Sektions-Margins |
| 4xl | 96px | Hero-Bereiche |

---

## Button-Styles

### Primär-Button
```css
background: #B5533E;
color: #FBF9F7;
padding: 16px 32px;
border-radius: 8px;
font-weight: 600;
transition: all 0.3s ease;
```

### Sekundär-Button
```css
background: transparent;
border: 2px solid #8B7355;
color: #8B7355;
padding: 14px 30px;
border-radius: 8px;
```

### Hover-States
```css
/* Primär */
background: #9A4433;
transform: translateY(-2px);
box-shadow: 0 4px 12px rgba(181, 83, 62, 0.3);

/* Sekundär */
background: #8B7355;
color: #FBF9F7;
```

---

## Komponenten-Styles

### Karten
```css
background: #FBF9F7;
border-radius: 16px;
box-shadow: 0 4px 24px rgba(45, 36, 24, 0.08);
padding: 24px;
```

### Bilder
```css
border-radius: 12px;
object-fit: cover;
```

### Navbar
```css
background: rgba(251, 249, 247, 0.95);
backdrop-filter: blur(10px);
box-shadow: 0 2px 20px rgba(45, 36, 24, 0.05);
```

---

## Inhalt & USPs

### Slogan-Vorschläge
- "Wo Genuss auf Gemütlichkeit trifft"
- "Hausgemacht. Mit Liebe. Für dich."
- "Dein Wohlfühlort in Offenburg"

### Alleinstellungsmerkmale (USPs)
1. **Beste Kuchen in Offenburg** - Laut Google-Bewertungen "den besten Kuchen in Offenburg"
2. **Türkische Spezialitäten** - Authentisches Menemen und türkische Frühstückstraditionen
3. **Individuelle Hochzeitstorten** - Auf Bestellung gefertigt
4. **Lokal gerösteter Kaffee** - Bohnen aus der Region
5. **Gemütliches Ambiente** - Holz + Beige, moderne Einrichtung mit warmer Atmosphäre

### Services
- Frühstück (am Wochenende & Feiertagen)
- Kuchen & Torten
- Kaffee-Spezialitäten
- Individuelle Hochzeitstorten
- Terrasse / Außenbereich
- Tischreservierung
- Kartenzahlung
- WLAN
- Parkplätze vorhanden
- Mitnahme / To-Go
- Lieferung

### Speisekarte-Highlights
| Kategorie | Beispiele |
|-----------|-----------|
| Frühstück | Menemen (türkische Rühreier), Avocado-Toast |
| Kuchen & Torten | Wolken Torte (Signature!), diverse Torten |
| Kaffee | Lokal geröstete Bohnen, diverse Spezialitäten |
| Türkische Spezialitäten | Authentische Gerichte |

### Preisklasse
€€ - Mittleres Preissegment (ca. 9-22€ pro Person)

---

## Zielgruppe

### Primär
- Familien am Wochenende
- Paare für entspannten Kaffee/Kuchen
- Brunch-Liebhaber

### Sekundär
- Hochzeitspaare (Tortenbestellung)
- Berufstätige in der Mittagspause (Di-Fr)
- Freundesgruppen

### Atmosphäre-Keywords
- Gemütlich
- Warm
- Modern
- Einladend
- Familienfreundlich
- Romantisch

---

## Bilder & Medien

### Logo
**Status:** Kein Logo gefunden
**Empfehlung:** Text-Logo mit "Café Wolke" in Playfair Display + Wolken-Icon

### Foto-Quellen
Da keine Website existiert, sollten Bilder von folgenden Quellen bezogen werden:
- **Instagram:** [@cafe.wolke](https://www.instagram.com/cafe.wolke/) - 880 Posts
- **Restaurant Guru:** 26 Fotos, 12 Videos verfügbar
- **Google Maps:** Nutzer-Fotos

### Bildstil
- Warme, natürliche Beleuchtung
- Food-Fotografie im "Cozy Café"-Stil
- Holz-Texturen sichtbar
- Dampfender Kaffee, appetitliche Kuchen
- Gemütliche Innenaufnahmen

---

## Team

### Inhaberin
- **Name:** Esra Yagmur Türker
- **Position:** Inhaberin
- **Foto:** Nicht verfügbar

---

## Wettbewerber

### In der Nähe
- Cafe Humpen (1,2 km entfernt)
- Café Barbier Offenburg (2,45 km entfernt)
- Z-Café Offenburg

### Differenzierung
- Türkische Einflüsse in der Speisekarte (einzigartig!)
- "Bester Kuchen in Offenburg"
- Individuelle Hochzeitstorten
- Moderne, warme Atmosphäre

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Cozy Editorial"** - Ein warmes, einladendes Design das an hochwertige Food-Magazine erinnert:

- **Hero:** Vollbild-Slider mit dampfendem Kaffee, appetitlichen Kuchen, gemütlichem Interieur
- **Über uns:** Split-Layout mit großem Bild links, Text rechts
- **Speisekarte:** Card-Grid mit Hover-Effekten (Bild-Zoom)
- **Galerie:** Masonry-Grid für Instagram-Vibes

### 2. Signature-Effekt

**Wolken-Motiv als durchgängiges Designelement:**

- Subtile Wolken-Shapes als Hintergrund-Dekoration (SVG)
- Weiche, geschwungene Formen statt harter Kanten
- "Floaty" Animations - sanftes Schweben von Elementen
- Soft Shadows die an Wolken erinnern

```css
/* Wolken-Shadow */
box-shadow: 0 10px 40px rgba(184, 196, 206, 0.3);

/* Wolken-Border */
border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
```

### 3. Animations-Level: MODERAT

Passend für ein gemütliches Café:

| Element | Animation |
|---------|-----------|
| Hero | Sanftes Ken-Burns-Effekt auf Bildern |
| Scroll | Fade-in von unten, dezent |
| Karten | Subtle hover-lift mit Schatten |
| Navigation | Smooth scroll, sticky mit Blur |
| Buttons | Sanfter Farbübergang |
| Bilder | Leichter Zoom bei Hover |

**KEINE:** Schnelle Animationen, aggressive Parallax, blinkende Elemente

### 4. Besondere Sektionen

#### a) "Unsere Spezialitäten" - Horizontaler Scroll
Kuchen-Karten mit großen Bildern, horizontal scrollbar auf Mobile

#### b) "Dein Wohlfühlmoment" - Fullscreen Galerie
Atmosphäre-Bilder des Cafés, Masonry-Grid mit Lightbox

#### c) "Von Gästen geliebt" - Testimonials
Google-Bewertungen als Zitat-Karten mit Sterne-Rating

#### d) "Türkische Tradition" - Story-Sektion
Split-Screen: Links Menemen-Bild, rechts Geschichte der türkischen Frühstückskultur

#### e) "Für deinen besonderen Tag" - Hochzeitstorten
Elegante Galerie mit CTA zur Anfrage

### 5. Micro-Interactions

- **Dampfender Kaffee:** CSS-Animation für aufsteigenden Dampf im Hero
- **Wolken-Cursor:** Subtiler Wolken-Trail bei Mouse-Bewegung (optional)
- **Loading:** Wolken-Animation beim Laden
- **Scroll-Indikator:** Schwebende Wolke

### 6. Mobile-First Features

- **Sticky CTA:** "Jetzt reservieren" Button immer sichtbar
- **Swipeable Galerie:** Kuchen-Bilder zum Durchswipen
- **Click-to-Call:** Telefonnummer direkt anrufbar
- **Maps-Integration:** Direkte Navigation zum Café

---

## Impressum (Entwurf)

```
Café Wolke
Inhaberin: Esra Yagmur Türker

Amalie-Hofer-Straße 2
77656 Offenburg
Deutschland

Telefon: +49 781 55776
E-Mail: [E-Mail-Adresse einfügen]

Umsatzsteuer-ID: [USt-IdNr. einfügen falls vorhanden]

Verantwortlich für den Inhalt nach § 55 Abs. 2 RStV:
Esra Yagmur Türker
Amalie-Hofer-Straße 2
77656 Offenburg
```

---

## Datenschutz

Ein vollständiger Datenschutztext sollte erstellt werden mit:
- Verantwortliche Stelle (Esra Yagmur Türker)
- Kontaktdaten
- Erhebung und Speicherung personenbezogener Daten
- Cookies und Tracking (falls verwendet)
- Social Media Einbindung (Instagram)
- Google Maps Einbindung
- Reservierungssystem (falls vorhanden)
- Rechte der betroffenen Personen

---

## Technische Empfehlungen

### Performance
- WebP-Bilder für Kuchen-Fotos
- Lazy Loading für Galerie
- Above-the-fold Optimierung

### SEO
- Lokale SEO (Offenburg, Ortenau, Schwarzwald)
- Strukturierte Daten (LocalBusiness, Restaurant)
- Google My Business Verlinkung

### Barrierefreiheit
- Kontrastreiche Farbkombinationen
- Alt-Texte für alle Food-Bilder
- Keyboard-Navigation

---

## Referenzen & Testimonials

### Bewertungsübersicht
| Plattform | Rating | Anzahl Bewertungen |
|-----------|--------|-------------------|
| Google | 4.7 / 5.0 | 264 Bewertungen |
| Restaurant Guru | 4.8 / 5.0 | 228 Bewertungen |

### Echte Kundenstimmen (Google Reviews)

**Hinweis:** Die folgenden Zitate stammen aus echten Google-Bewertungen. Da die Reviewer-Namen nicht öffentlich mit Fotos verknüpft sind, werden sie als anonyme Gästestimmen präsentiert.

#### Testimonial 1 - Ambiente
> "Sehr schönes Ambiente drinnen wie draußen. Wirkt frisch renoviert. Toller farblicher Kontrast. Holz und beige Töne. Wirkt ausgesprochen sauber und gepflegt."

**Bewertung:** ★★★★★
**Kategorie:** Ambiente & Atmosphäre

#### Testimonial 2 - Bester Kuchen
> "Sie haben den besten Kuchen in Offenburg. Einfach genial!"

**Bewertung:** ★★★★★
**Kategorie:** Kuchen & Torten

#### Testimonial 3 - Gesamteindruck
> "Sehr nettes Café. Das Essen ist Bombe! Wir werden wieder kommen!"

**Bewertung:** ★★★★★
**Kategorie:** Essen & Service

#### Testimonial 4 - Qualität & Empfehlung
> "Freundlicher Service und weil die Qualität richtig ist, gibt es kaum Platz an Sonn- und Feiertagen. Als Top-Adresse in Offenburg sehr empfehlenswert."

**Bewertung:** ★★★★★
**Kategorie:** Service & Beliebtheit

#### Testimonial 5 - Vollständiger Besuch
> "Es war alles hervorragend. Das Essen war wirklich lecker, reichlich an verschiedenen 'Sorten'."

**Bewertung:** ★★★★★
**Kategorie:** Speisenangebot

#### Testimonial 6 - Preis-Leistung
> "Super nettes Personal, sehr leckerer Kuchen und faire Preise."

**Bewertung:** ★★★★★
**Kategorie:** Preis-Leistung

#### Testimonial 7 - Wohlfühlfaktor
> "Wir waren sehr zufrieden mit unserem Besuch im Café Wolke und können es jedem empfehlen, der Lust auf eine Auszeit hat."

**Bewertung:** ★★★★★
**Kategorie:** Wohlfühlort

### Quellen
- [Restaurant Guru - Café Wolke Offenburg](https://restaurantguru.com/Cafe-Wolke-Offenburg)
- [speisekarte.de - Café Wolke](https://www.speisekarte.de/offenburg/restaurant/cafe_wolke)
- [restaurantnet.de - Café Wolke](https://www.restaurantnet.de/rest/cafe-wolke)
- Google Maps Bewertungen (via Aggregator-Seiten)

### Verwendung auf der Website

**Empfohlene Darstellung:**
- Zitat-Karten mit Sterne-Rating
- Ohne Personenfotos (da nicht verfügbar)
- Google-Logo zur Quellenangabe
- Link zu Google Reviews für mehr Bewertungen

**HTML-Struktur Vorschlag:**
```html
<div class="testimonial-card">
    <div class="stars">★★★★★</div>
    <blockquote>"Zitat hier..."</blockquote>
    <div class="source">
        <img src="assets/google-logo.svg" alt="Google">
        <span>Verifizierte Google-Bewertung</span>
    </div>
</div>
```

### Assets-Status

| Asset | Status | Pfad |
|-------|--------|------|
| Personenfotos | ❌ Nicht verfügbar | - |
| Firmenlogos | ❌ Keine B2B-Referenzen | - |
| Google Logo | Benötigt | `assets/google-logo.svg` |

**Hinweis:** Da keine individuellen Kundenfotos oder B2B-Referenzen verfügbar sind, sollte die Testimonials-Sektion auf anonyme Zitate mit Google-Branding setzen.
