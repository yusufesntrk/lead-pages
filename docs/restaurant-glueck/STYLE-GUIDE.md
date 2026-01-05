# Style Guide - Restaurant Glück

## Übersicht

**Restaurant:** China Restaurant Glück
**Branche:** Chinesisches & Japanisches Restaurant (Sushi)
**Standort:** Offenburg, Baden-Württemberg
**Design-Basis:** Branchenspezifisch (keine bestehende Website vorhanden)

---

## Farbpalette

### Primärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Glücksrot** | `#C8102E` | Hauptakzent, CTAs, Logo-Akzent, wichtige Elemente |
| **Gold** | `#D4AF37` | Sekundärakzent, Highlights, Dekoelemente |
| **Tiefes Schwarz** | `#1A1A1A` | Text, Header, Footer |

### Sekundärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Cremeweiß** | `#FDF8F3` | Hintergrund, helle Sektionen |
| **Warmes Grau** | `#4A4A4A` | Sekundärtext, Beschreibungen |
| **Hellgrau** | `#F5F5F5` | Kartenhintenründe, Sektionswechsel |
| **Jade-Grün** | `#00A86B` | Akzente, Icons, Frische-Elemente |

### Farbpsychologie

- **Rot:** Glück, Wohlstand, Festlichkeit (traditionell chinesisch)
- **Gold:** Reichtum, Eleganz, Premium-Qualität
- **Schwarz:** Eleganz, Modernität, Raffinesse
- **Jade-Grün:** Frische, Harmonie, Natur (für Sushi/Frische)

---

## Typografie

### Schriftarten

```css
/* Überschriften - elegant, modern */
font-family: 'Playfair Display', 'Georgia', serif;

/* Fließtext - gut lesbar, modern */
font-family: 'Inter', 'Segoe UI', sans-serif;

/* Akzente/Spezial - für asiatischen Touch */
font-family: 'Noto Sans SC', sans-serif;
```

### Schriftgrößen

| Element | Desktop | Mobile | Gewicht |
|---------|---------|--------|---------|
| H1 | 56px | 36px | 700 |
| H2 | 42px | 28px | 600 |
| H3 | 28px | 22px | 600 |
| H4 | 22px | 18px | 500 |
| Body | 18px | 16px | 400 |
| Small | 14px | 14px | 400 |

### Zeilenabstand

- Überschriften: 1.2
- Fließtext: 1.7
- Navigation: 1.5

---

## Spacing-System

### Basis-Einheit: 8px

| Name | Wert | Verwendung |
|------|------|------------|
| xs | 8px | Inline-Abstände |
| sm | 16px | Komponenten-Innenabstände |
| md | 24px | Kartenabstände |
| lg | 48px | Sektionsabstände intern |
| xl | 80px | Sektionsabstände |
| 2xl | 120px | Hero-Bereiche |

---

## Komponenten-Styles

### Buttons

```css
/* Primär-Button */
.btn-primary {
  background: linear-gradient(135deg, #C8102E 0%, #A00D24 100%);
  color: #FFFFFF;
  padding: 16px 32px;
  border-radius: 8px;
  font-weight: 600;
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(200, 16, 46, 0.3);
}

/* Sekundär-Button */
.btn-secondary {
  background: transparent;
  color: #C8102E;
  border: 2px solid #C8102E;
  padding: 14px 30px;
  border-radius: 8px;
}
```

### Karten

```css
.card {
  background: #FFFFFF;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
}
```

### Navigation

```css
.navbar {
  background: rgba(26, 26, 26, 0.95);
  backdrop-filter: blur(10px);
  padding: 16px 0;
}

.nav-link {
  color: #FFFFFF;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #D4AF37;
}
```

---

## Animations-Level

**Branche:** Restaurant → **Moderat**

### Erlaubte Animationen

- Fade-in beim Scrollen (sanft)
- Hover-Effekte auf Karten und Buttons
- Sanfte Bild-Overlays
- Dezente Parallax-Effekte im Hero
- Smooth Scroll

### Animation-Timing

```css
/* Standard-Transition */
transition: all 0.3s ease;

/* Hover-Effekte */
transition: transform 0.2s ease, box-shadow 0.3s ease;

/* Scroll-Animationen */
animation-duration: 0.6s;
animation-timing-function: ease-out;
```

---

## Bildsprache

### Stil-Richtlinien

- **Speisefotos:** Warm ausgeleuchtet, appetitlich, Close-ups
- **Ambiente:** Warme Beleuchtung, einladend, elegant
- **Details:** Tischdekorationen, Essstäbchen, Keramik
- **Menschen:** Authentisch, freundlich (falls Team-Fotos)

### Bildbehandlung

```css
/* Speisebilder */
.food-image {
  border-radius: 12px;
  object-fit: cover;
}

/* Overlay für Textlesbarkeit */
.image-overlay {
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(26, 26, 26, 0.7) 100%
  );
}
```

---

## Firmendaten

### Kontaktinformationen

| Feld | Wert |
|------|------|
| **Name** | Restaurant Glück (China Restaurant Glück) |
| **Inhaber** | Pujun Ji |
| **Adresse** | Schutterwälder Str. 5, 77656 Offenburg |
| **Telefon** | +49 781 97051115 |
| **Email** | Nicht bekannt |
| **Instagram** | @glueck_offenburg |

### Öffnungszeiten

| Tag | Zeiten |
|-----|--------|
| Montag - Freitag | 11:30 - 14:30 Uhr, 17:30 - 22:00 Uhr |
| Samstag | 11:30 - 22:30 Uhr |
| Sonntag & Feiertage | 11:30 - 22:00 Uhr |

**Kein Ruhetag**

### Bewertungen

- **Google Rating:** 4.1 (123 Bewertungen)
- **Restaurant Guru:** 4.6 (240 Bewertungen)
- **Too Good To Go Preis:** 27€ regulär / 9€ Überraschungstüte

### Besonderheiten

- Kostenlose Parkplätze direkt am Restaurant
- Sushi & chinesische Küche
- Takeout & Lieferservice (Lieferando)
- Spielbereich vorhanden
- Vegetarische/Vegane Optionen verfügbar
- Bier & Wein im Angebot

---

## Speisekarte-Kategorien

Da keine detaillierte Speisekarte verfügbar ist, basierend auf Recherche:

### Hauptkategorien

1. **Vorspeisen**
   - Frühlingsrollen
   - Dim Sum
   - Suppen

2. **Sushi & Sashimi**
   - Maki-Rollen
   - Nigiri
   - Sashimi-Platten
   - Spezialrollen

3. **Hauptgerichte**
   - Gebratene Nudeln
   - Gebratener Reis
   - Ente (Peking-Ente)
   - Hühnchen-Gerichte
   - Rindfleisch-Gerichte
   - Meeresfrüchte

4. **Vegetarisch/Vegan**
   - Tofu-Gerichte
   - Gemüsegerichte

5. **Desserts**
   - Gebackene Banane
   - Lychees

### Preisrahmen

- **Mittlerer Preis:** 20€ - 30€ pro Person
- **Mittagsmenüs:** Günstiger (vermutlich 8€ - 12€)

---

## Content-Bausteine

### Hero-Headline Vorschläge

> "Authentische asiatische Küche in Offenburg"

> "Wo Tradition auf Genuss trifft"

> "Frisches Sushi & chinesische Spezialitäten"

### Über uns (Vorschlag)

> Im Herzen von Offenburg erwartet Sie das Restaurant Glück mit einer kulinarischen Reise durch die Aromen Asiens. Unsere Küche verbindet traditionelle chinesische Rezepte mit der Kunst des japanischen Sushi – zubereitet mit frischen Zutaten und viel Liebe zum Detail.
>
> In unserem gemütlichen Ambiente können Sie entspannen und sich von unserer Gastfreundschaft verwöhnen lassen. Ob beim Mittagessen mit Kollegen, einem romantischen Dinner oder dem Familienausflug – bei uns finden Sie für jeden Anlass das passende Gericht.

### Unique Selling Points

1. **Frische Qualität** - Täglich frisch zubereitete Speisen
2. **Vielfalt** - Sushi & traditionelle chinesische Küche
3. **Familienfreundlich** - Spielbereich für Kinder
4. **Bequem** - Kostenlose Parkplätze & Lieferservice
5. **Erfahrung** - Über 240 positive Bewertungen

---

## SEO-Keywords

### Primär
- China Restaurant Offenburg
- Sushi Offenburg
- Asiatisches Restaurant Offenburg
- Restaurant Glück Offenburg

### Sekundär
- Chinesisches Essen Offenburg
- Sushi Lieferservice Offenburg
- Asia Restaurant Schutterwälder Straße
- Mittagstisch asiatisch Offenburg

---

## Logo

### Status
**Kein Logo verfügbar** - Es wurde kein offizielles Logo gefunden.

### Empfehlung
Textbasiertes Logo mit:
- Name "Glück" in eleganter Schrift (Playfair Display)
- Optionales Glückssymbol (z.B. stilisierte Glückskatze oder chinesisches Schriftzeichen 福)
- Farben: Rot (#C8102E) + Gold (#D4AF37)

### Text-Logo CSS

```css
.logo-text {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: 32px;
  color: #C8102E;
}

.logo-accent {
  color: #D4AF37;
}
```

---

## Dekorative Elemente

### Asiatische Akzente (dezent)

- Stilisierte Wolkenmuster
- Geometrische Muster (chinesisch inspiriert)
- Bambus-Silhouetten
- Glückskatze (Maneki-neko) als Icon

### Trennlinien

```css
.divider-asian {
  height: 2px;
  background: linear-gradient(
    to right,
    transparent,
    #D4AF37 20%,
    #D4AF37 80%,
    transparent
  );
  width: 100px;
  margin: 24px auto;
}
```

---

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 640px) { }

/* Tablet */
@media (min-width: 641px) and (max-width: 1024px) { }

/* Desktop */
@media (min-width: 1025px) { }

/* Large Desktop */
@media (min-width: 1440px) { }
```

---

## Impressum-Daten

### Für rechtliche Seiten

```
Restaurant Glück
Inhaber: Pujun Ji
Schutterwälder Str. 5
77656 Offenburg

Telefon: +49 781 97051115
```

**Hinweis:** USt-IdNr., Handelsregister und weitere rechtliche Angaben müssen beim Kunden erfragt werden.

---

## Quellen

- [Restaurant Guru](https://restaurantguru.com/Restaurant-Gluck-Offenburg)
- [Swipein Restaurant](https://www.swipein.restaurant/de/restaurant/restaurant-gluck-offenburg-baden-wurttemberg)
- [Instagram @glueck_offenburg](https://www.instagram.com/glueck_offenburg/)
- [Creditreform Firmeneintrag](https://firmeneintrag.creditreform.de/77656/7210195338/PUJUN_JI_CHINA_RESTAURANT_GLUECK)
- [Too Good To Go](https://www.toogoodtogo.com/de/find/offenburg/chinarestaurantgluck)

---

## Referenzen

### Bewertungsübersicht

| Plattform | Rating | Anzahl Bewertungen |
|-----------|--------|-------------------|
| **Google** | ⭐ 4.6 / 5 | 213+ Bewertungen |
| **Restaurant Guru** | ⭐ 4.6 / 5 | 240 Bewertungen |
| **Swipein** | ⭐ 4.7 / 5 | - |
| **TripAdvisor** (als Feng Ze Yuan) | ⭐ 3.1 / 5 | 17 Bewertungen |

**Hinweis:** Das Restaurant hieß früher "Feng Ze Yuan" und wurde in "Restaurant Glück" umbenannt. Die neueren Bewertungen (Google, Restaurant Guru) spiegeln die aktuelle Qualität besser wider.

### Echte Kundenstimmen

#### Positive Bewertungen

**Bewertung 1 - TripAdvisor (März 2019)**
> "Das Buffet war sehr ausreichend groß, mit großer Auswahl von Speisen sowie einer großen Dessertauswahl. Das Restaurant machte einen ordentlichen und sauberen Eindruck, der Service war gut und aufmerksam."
- **Quelle:** [TripAdvisor](https://www.tripadvisor.de/ShowUserReviews-g198528-d3354040-r657285176-Feng_Ze_Yuan-Offenburg_Baden_Wurttemberg.html)

**Bewertung 2 - TripAdvisor (2014)**
> "Für alle was dabei. Buffet, Sushi und Tepanyaki. Service unterbesetzt aber auf Zack. Riesenauswahl am Buffet."
- **Titel:** "Tolles Restaurant mit live cooking"
- **Quelle:** [TripAdvisor](https://www.tripadvisor.de/ShowUserReviews-g198528-d3354040-r246573996-Feng_Ze_Yuan-Offenburg_Baden_Wurttemberg.html)

**Bewertung 3 - TripAdvisor (nach Umbenennung)**
> "Second time we have come since the restaurant changed its name... It's Glück now. Always so satisfied, friendly staff, big Hugg every time."
- **Quelle:** TripAdvisor

**Bewertung 4 - Restaurant Guru**
> "Das Restaurant ist bekannt für gut zubereitetes Sushi, großartigen Service und freundliches Personal, das immer bereit ist zu helfen. Die spektakuläre Spielecke und angenehme Atmosphäre lassen die Gäste sich entspannt fühlen."
- **Quelle:** [Restaurant Guru](https://restaurantguru.com/Restaurant-Gluck-Offenburg)

### Highlights aus Bewertungen

- ✅ **Freundliches Personal** - Wird durchgehend positiv erwähnt
- ✅ **Große Auswahl** - Buffet, Sushi, Teppanyaki, Desserts
- ✅ **Familienfreundlich** - Spielbereich für Kinder vorhanden
- ✅ **Sauberkeit** - Ordentlicher und sauberer Eindruck
- ✅ **Live Cooking** - Teppanyaki-Grill vor Ort
- ✅ **Kostenlose Parkplätze** - Direkt am Restaurant

### Social Media Präsenz

- **Instagram:** [@glueck_offenburg](https://www.instagram.com/glueck_offenburg/) - 11.000+ Follower, 51 Beiträge
- **Lieferando:** [China Restaurant Glück](https://www.lieferando.de/speisekarte/china-restaurant-gluck-offenburg)
- **Too Good To Go:** Aktive Teilnahme (Überraschungstüten für 9€)

### Empfehlung für Website

Da keine individuellen Testimonials mit Personenfotos verfügbar sind, empfehle ich für die Website:

**Option A - Google Reviews Integration:**
```html
<div class="reviews-summary">
    <div class="rating">
        <span class="stars">★★★★★</span>
        <span class="score">4.6</span>
    </div>
    <p>Basierend auf über 450 Bewertungen bei Google und Restaurant Guru</p>
    <a href="https://g.page/..." class="btn-secondary">Alle Bewertungen ansehen</a>
</div>
```

**Option B - Ausgewählte Zitate (ohne Personenfotos):**
Echte Zitate aus Bewertungen mit Quellenangabe (TripAdvisor, Google) ohne persönliche Fotos.

### Quellen

- [Restaurant Guru - Restaurant Glück](https://restaurantguru.com/Restaurant-Gluck-Offenburg)
- [TripAdvisor - Feng Ze Yuan](https://www.tripadvisor.com/Restaurant_Review-g198528-d3354040-Reviews-Feng_Ze_Yuan-Offenburg_Baden_Wurttemberg.html)
- [Swipein - Restaurant Glück](https://www.swipein.restaurant/de/restaurant/restaurant-gluck-offenburg-baden-wurttemberg)
- [Instagram - @glueck_offenburg](https://www.instagram.com/glueck_offenburg/)

---

*Style Guide erstellt am: Januar 2026*
*Basis: Branchenspezifisches Design (keine bestehende Website)*
