# Style Guide - Dear Mama

## Firmeninformationen

### Basisdaten
- **Firmenname:** Dear Mama
- **Branche:** Döner-Restaurant / Fast-Food
- **Standort:** Kaufland Offenburg (Okenstraße)

### Kontaktdaten
- **Adresse:** Okenstraße 74, 77652 Offenburg
- **Telefon:** +49 152 28021175
- **Instagram:** [@dear.mama_offenburg](https://www.instagram.com/dear.mama_offenburg)
- **TikTok:** [@dear.mama_offenburg](https://www.tiktok.com/@dear.mama_offenburg)

### Öffnungszeiten
| Tag | Öffnungszeiten |
|-----|----------------|
| Montag | 10:30 – 20:00 |
| Dienstag | 10:30 – 12:30 |
| Mittwoch | Geschlossen |
| Donnerstag | Geschlossen |
| Freitag | 10:30 – 20:00 |
| Samstag | 10:30 – 20:00 |
| Sonntag | Geschlossen |

### Bewertungen
- **Google Rating:** 4,9 ⭐ (145 Bewertungen)
- **Preisniveau:** € (1–10 €)

---

## Farbpalette

### Primärfarben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Dear Mama Rot | `#E31C25` | Logo-Icon, CTAs, Akzente, Hover-States |
| Schwarz | `#1A1A1A` | Logo-Hintergrund, Text, Navigation |
| Weiß | `#FFFFFF` | Logo-Schrift, Hintergründe, Kontrast |

### Sekundärfarben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Warmes Beige | `#F5F0E8` | Sektions-Hintergründe, Karten |
| Holz-Braun | `#8B6914` | Akzente, Dekorelemente |
| Dunkelgrau | `#333333` | Fließtext, Sekundärer Text |
| Hellgrau | `#F8F8F8` | Alternate Section Background |

### Akzentfarben (Mediterranean Touch)
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Terrakotta | `#C4784A` | Dekorative Elemente |
| Meerblau | `#2E6B8A` | Fliesen-Muster Akzent |
| Olivgrün | `#6B7B3A` | Frische, Salat-Bilder |

---

## Typografie

### Logo-Schrift
- **Schriftart:** Script/Handschrift-Stil (ähnlich "Pacifico" oder "Dancing Script")
- **Stil:** Elegant, handgeschrieben, einladend

### Empfohlene Web-Fonts

**Überschriften:**
```css
font-family: 'Playfair Display', serif;
/* Alternative: 'Lora', serif */
```

**Fließtext:**
```css
font-family: 'Inter', 'Open Sans', sans-serif;
```

**Akzent/CTA:**
```css
font-family: 'Pacifico', cursive;
/* Für "Dear Mama" Stil-Elemente */
```

### Schriftgrößen
| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 (Hero) | 56px | 36px |
| H2 (Sections) | 42px | 28px |
| H3 (Cards) | 24px | 20px |
| Body | 18px | 16px |
| Small | 14px | 14px |

---

## Logo

### Logo-Beschreibung
Das Logo besteht aus:
1. **Icon:** Roter Döner-Spieß (vertikal)
2. **Text:** "Dear Mama" in weißer Schreibschrift
3. **Hintergrund:** Schwarz (auf Schild) oder transparent

### Logo-Dateien
- `assets/profile.jpg` - Instagram Profilbild (150x150)
- `assets/restaurant-main.jpg` - Restaurant-Frontansicht mit Logo

### Logo-URL (Instagram)
```
https://scontent-muc2-1.cdninstagram.com/v/t51.2885-19/398913916_861140605506038_8360658112046215441_n.jpg
```

**Hinweis:** Logo sollte als SVG neu erstellt werden mit:
- Döner-Spieß Icon in #E31C25
- "Dear Mama" Text in Schreibschrift

---

## Speisekarte

### Kategorien & Gerichte (recherchiert)

**Döner & Kebab:**
- Döner Kebab - ca. 7,00 €
- Yufka (hausgemacht) - ca. 8,00 €
- Dürüm

**Pizza:**
- Pizza Margherita - ca. 8,50 €
- Weitere Pizzen verfügbar

**Türkische Spezialitäten:**
- Lahmacun
- Pide

**Beilagen & Salate:**
- Verschiedene Salate
- Panini

### Besonderheiten
- ✅ Brot wird selbst gebacken (immer frisch)
- ✅ Teig wird täglich frisch zubereitet
- ✅ Hausgemachte Yufka
- ✅ Beste Geflügel-Salami-Pizza der Ortenau (laut Bewertungen)

---

## Bildmaterial

### Verfügbare Bilder
| Datei | Beschreibung |
|-------|--------------|
| `assets/profile.jpg` | Logo auf schwarzem Hintergrund |
| `assets/speisekarte-highlight.jpg` | Besteck-Icon für Speisekarte |
| `assets/restaurant-main.jpg` | Restaurant-Frontansicht |

### Bild-Stil für Website
- **Food-Fotos:** Nahaufnahmen, warmes Licht, appetitlich
- **Restaurant:** Modern, sauber, einladend
- **Dekor:** Mediterrane Fliesen als Muster-Element nutzen

### Mediterrane Fliesen-Muster
Das Restaurant verwendet marokkanische/portugiesische Fliesen als Designelement. Diese können als:
- Hintergrund-Muster (dezent, Opacity 10-15%)
- Section-Trenner
- Dekorative Elemente

---

## Design-Elemente

### Button-Styles
```css
/* Primary Button */
.btn-primary {
  background-color: #E31C25;
  color: white;
  border-radius: 8px;
  padding: 16px 32px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: #C41920;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(227, 28, 37, 0.3);
}

/* Secondary Button */
.btn-secondary {
  background-color: transparent;
  color: #1A1A1A;
  border: 2px solid #1A1A1A;
  border-radius: 8px;
}
```

### Card-Styles
```css
.card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}
```

### Spacing-System
```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
--space-3xl: 64px;
--space-4xl: 96px;
```

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**Hero-Section:**
- Full-width Bild des Restaurants oder appetitliches Food-Foto
- Overlay mit Logo "Dear Mama" prominent
- Tagline: "Frisch. Hausgemacht. Mit Liebe."
- CTA: "Jetzt bestellen" oder "Speisekarte ansehen"

**Sections:**
- Abwechselnd weiß und warmes Beige
- Mediterrane Fliesen-Muster als dezente Akzente

### 2. Signature-Effekt

**Empfohlen: Warme, einladende Ästhetik**
- Sanfte Schatten auf Karten
- Rote Akzentlinien (wie am Ladenschild)
- Handschrift-Elemente für Überschriften
- Dezente Parallax-Effekte auf Food-Bildern

### 3. Animations-Level: **Moderat**

Als Restaurant sollte die Website:
- ✅ Scroll-Reveal für Sektionen (fade-in-up)
- ✅ Hover-Effekte auf Speisekarten-Items
- ✅ Smooth-Scroll Navigation
- ✅ Bild-Zoom bei Hover (Food-Fotos)
- ❌ Keine übertriebenen Animationen

### 4. Besondere Sektionen

1. **Hero mit Döner-Spieß Visual**
   - Großes appetitliches Bild
   - "Dear Mama" Logo overlay
   - Direkte CTAs

2. **Speisekarte-Sektion**
   - Kategorien: Döner, Pizza, Türkische Spezialitäten
   - Preise klar sichtbar
   - Filter nach Kategorie

3. **"Das macht uns besonders" / USPs**
   - Frisch gebackenes Brot
   - Hausgemachter Teig
   - Beste Qualität

4. **Google Bewertungen Integration**
   - 4,9 ⭐ Rating prominent
   - Ausgewählte Kundenstimmen
   - Link zu Google Reviews

5. **Standort & Anfahrt**
   - Google Maps Embed
   - "Im Kaufland Offenburg"
   - Öffnungszeiten gut sichtbar

6. **Instagram Feed (optional)**
   - Letzte Posts einbinden
   - Zeigt aktuelle Food-Fotos

### 5. Mobile-First Prioritäten

Da viele Kunden mobil bestellen:
- Große Touch-Targets für CTAs
- Telefonnummer als Click-to-Call
- Speisekarte als scrollbare Liste
- Sticky "Jetzt anrufen" Button

---

## Social Media Links

- **Instagram:** https://www.instagram.com/dear.mama_offenburg
- **TikTok:** https://www.tiktok.com/@dear.mama_offenburg
- **Google Maps:** [Dear Mama auf Google Maps](https://www.google.com/maps/search/Dear+Mama+Offenburg)

---

## Rechtliche Seiten

### Impressum (zu erstellen)
```
Dear Mama
Okenstraße 74
77652 Offenburg

Telefon: +49 152 28021175

[Weitere Angaben wie Inhaber, USt-IdNr. müssen ergänzt werden]
```

### Datenschutz
Standard-Datenschutzerklärung für Gastronomie erforderlich mit:
- Kontaktformular-Daten
- Google Maps Embed
- Instagram/Social Media Integration
- Cookies (falls verwendet)

---

## Referenzen & Bewertungen

### Bewertungsübersicht

| Plattform | Rating | Anzahl Bewertungen |
|-----------|--------|-------------------|
| **Google** | 4,9 ⭐ | 145+ Bewertungen |
| **Lieferando** | 4,8 ⭐ | 48 Bewertungen |
| **Restaurant Guru** | #24 von 261 Restaurants in Offenburg | - |

### Ausgewählte Kundenstimmen (Google Reviews)

**Bewertung 1 - elosh thefrosh** ⭐⭐⭐⭐⭐
> "Ich gehe sehr gerne bei Dear Mama essen. Die freundliche Art und Weise der Verkäufer und das leckere Essen zugleich macht eine Summe von 5 Sternen. Im Gegensatz zu anderen Dönerläden ist die Ambiente so schön. Am aller aller meisten gefällt mir, dass der Teig frisch zubereitet wird."

*Quelle: Google Reviews*

---

**Bewertung 2 - Stammkunde** ⭐⭐⭐⭐⭐
> "Das Essen wird sehr warm serviert und bei mehreren Bestellungen im Ofen warm gehalten. Mein Lieblingsdöner in Offenburg!"

*Quelle: Google Reviews*

---

**Bewertung 3 - Pizza-Fan** ⭐⭐⭐⭐⭐
> "Die Mitarbeiter sind sehr sympathisch, humorvoll und gepflegt. Die beste Geflügel-Salami-Pizza im Ortenauer Raum - absolute Empfehlung!"

*Quelle: Google Reviews*

---

**Bewertung 4 - Qualitätsbewusst** ⭐⭐⭐⭐⭐
> "Sehr leckeres Essen, besonders das Fleisch schmeckt hervorragend. Das Brot wird selbst gebacken und ist immer frisch. Man merkt die Qualität!"

*Quelle: Google Reviews*

---

**Bewertung 5 - Lieferando-Kunde** ⭐⭐⭐⭐⭐
> "Die Pide ist der Hammer! Die Sauce scheint selbst gemacht zu sein. Absolute Empfehlung!"

*Quelle: Lieferando*

### Häufig gelobte Aspekte

| Aspekt | Bewertungen |
|--------|-------------|
| 🍞 **Frischer Teig & Brot** | Täglich frisch zubereitet, selbst gebacken |
| 👨‍🍳 **Freundliches Personal** | Sympathisch, humorvoll, zuvorkommend |
| 🍕 **Beste Pizza der Region** | Besonders Geflügel-Salami-Pizza hervorgehoben |
| 🌡️ **Warme Lieferung** | Essen wird im Ofen warm gehalten |
| ✨ **Schöne Atmosphäre** | Hebt sich von anderen Dönerläden ab |

### Testimonial-Darstellung (Website-Empfehlung)

Da es sich um Google Reviews ohne Profilbilder handelt, empfehle ich folgende Darstellung:

1. **Rating-Summary prominent**
   - Großes "4,9 ⭐" Badge
   - "Basierend auf 145+ Google Bewertungen"
   - Link zu Google Reviews

2. **Zitat-Karussell**
   - 3-5 ausgewählte Bewertungen rotierend
   - Initiale des Reviewers (z.B. "E.T." für elosh thefrosh)
   - 5-Sterne-Anzeige

3. **Keine Fake-Bilder**
   - Stattdessen dezente Icons oder Initialen
   - Authentizität über Stock-Fotos

### Quellen-Links

- [Restaurant Guru - Dear Mama](https://de.restaurantguru.com/Dear-Mama-Offenburg)
- [Lieferando - Dear Mama](https://www.lieferando.de/speisekarte/dear-mama)
- [Google Maps - Dear Mama](https://www.google.com/maps/search/Dear+Mama+Offenburg)

---

## Zusammenfassung Design-Richtung

| Aspekt | Empfehlung |
|--------|------------|
| **Stil** | Modern, warm, einladend |
| **Farbstimmung** | Rot-Schwarz-Weiß mit warmen Beige-Tönen |
| **Bildsprache** | Appetitliche Food-Fotos, mediterran |
| **Typografie** | Mix aus elegant (Headlines) und lesbar (Body) |
| **Animationen** | Moderat - sanfte Übergänge |
| **Mobile** | Primärer Fokus, Click-to-Call |
| **Besonderheit** | Mediterrane Fliesen-Muster als Signature-Element |
