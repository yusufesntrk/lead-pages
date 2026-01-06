# YUMMY Döner Offenburg - Style Guide

## Brand Overview
- **Name:** YUMMY Döner Offenburg
- **Kurzname:** YUMMY / Yummy
- **Branche:** Restaurant (Döner/Kebab/Türkische Küche)
- **Standort:** Ritterstraße 3, 77652 Offenburg
- **Telefon:** +49 781 25080527
- **Instagram:** @yummy_offenburg (3.922 Follower, 131 Posts)
- **Google Rating:** 4.6 ⭐ (639 Bewertungen)
- **Charakter:** Modern, einladend, appetitlich, familiär
- **Preisbereich:** €9-22 pro Person

## Farbpalette

### Primärfarben
- **Primary (Orange):** `#FF6B35` - Warm, appetitlich, einladend
- **Primary Dark:** `#E55A2B` - Für Hover-States
- **Primary Light:** `#FF8A5C` - Für Akzente

### Sekundärfarben
- **Secondary (Rot):** `#D62828` - Energie, Leidenschaft für gutes Essen
- **Secondary Dark:** `#B81E1E` - Für CTAs

### Akzentfarben
- **Accent Gold:** `#F4A261` - Wärme, Premium-Gefühl
- **Accent Yellow:** `#FFD166` - Frische, Fröhlichkeit

### Neutrale Farben
- **Text Primary:** `#1A1A1A` - Haupttext
- **Text Secondary:** `#4A4A4A` - Sekundärtext
- **Text Light:** `#717171` - Dezenter Text
- **Background:** `#FFFFFF` - Haupthintergrund
- **Background Warm:** `#FFF8F5` - Warmer Hintergrund für Sektionen
- **Background Dark:** `#1A1A1A` - Footer, dunkle Sektionen
- **Border:** `#E5E5E5` - Dezente Trennlinien

## Typografie

### Font Family
```css
--font-primary: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-display: 'Playfair Display', Georgia, serif;
```

### Font Sizes (Mobile-First)
```css
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
--text-5xl: 3rem;      /* 48px */
```

### Font Weights
```css
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

## Spacing System
```css
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
--space-24: 6rem;     /* 96px */
```

## Border Radius
```css
--radius-sm: 0.25rem;   /* 4px */
--radius-md: 0.5rem;    /* 8px */
--radius-lg: 0.75rem;   /* 12px */
--radius-xl: 1rem;      /* 16px */
--radius-2xl: 1.5rem;   /* 24px */
--radius-full: 9999px;  /* Pills */
```

## Shadows
```css
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
```

## Button Styles

### Primary Button
```css
.btn-primary {
  background: linear-gradient(135deg, #FF6B35, #E55A2B);
  color: white;
  padding: 0.875rem 2rem;
  border-radius: 9999px;
  font-weight: 600;
  transition: all 0.3s ease;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(255, 107, 53, 0.3);
}
```

### Secondary Button
```css
.btn-secondary {
  background: transparent;
  color: #FF6B35;
  border: 2px solid #FF6B35;
  padding: 0.875rem 2rem;
  border-radius: 9999px;
  font-weight: 600;
}
```

## Animationen
- **Level:** Moderat (Restaurant-Branche)
- **Scroll-Reveal:** Sanfte Fade-in Animationen
- **Image Hover:** Subtle zoom effect
- **Button Hover:** Lift + Shadow

## Logo
- Schwarzer Kreis mit weißem Kochmützen-Icon und Besteck
- Text: "YUMMY" in weißer Schrift
- Fallback: Text-Logo mit stilisiertem Design

## Responsive Breakpoints
```css
--breakpoint-sm: 640px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1280px;
```

## Sektion-Variation
- Hero: Vollbild-Bild mit Overlay
- Menü: Warmer Hintergrund (#FFF8F5) mit Cards
- Über uns: Weißer Hintergrund mit Bild
- Reviews: Dunkler Hintergrund (#1A1A1A)
- Kontakt: Warmer Hintergrund mit Karte

## Öffnungszeiten
- Montag: Ruhetag
- Dienstag - Samstag: 11:00 - 22:00 Uhr
- Sonntag: 11:30 - 22:00 Uhr

## Kontakt
- Adresse: Ritterstraße 3, 77652 Offenburg
- Telefon: +49 781 25080527
- Instagram: @yummy_offenburg
- Nur Barzahlung (keine Kartenzahlung!)

## Speisekarte

**Hinweis:** Keine digitale Speisekarte online verfügbar. Basierend auf Bewertungen und Instagram-Posts:

### Kategorien & Gerichte

#### Döner
- Döner Kebab (im Brot)
- Döner Teller (mit Reis/Pommes/Salat)
- Döner Box
- Döner Dürüm (im Wrap)

#### Kebab & Fleischgerichte
- Kebab Teller
- Adana Kebab
- Fleischteller

#### Pizza
- Verschiedene Pizzen

#### Weitere Gerichte
- Lahmacun
- Falafel
- Pommes
- Salate

#### Desserts
- Baklava (besonders empfohlen!)

#### Getränke
- Softdrinks
- Ayran

## Besonderheiten & Service

- ✅ Außensitzplätze / Terrasse
- ✅ Mitnahme / Take-away
- ✅ Rollstuhlgerecht
- ✅ Parkplätze in der Nähe
- ⚠️ **Nur Barzahlung** (keine Kartenzahlung!)
- ❌ Kein Lieferservice

## Bewertungen & Highlights

### Google Rating: 4.6 ⭐ (639 Bewertungen)

**Was Kunden sagen:**
- "By far the best kebab shop in all of Offenburg"
- "Frisches, geschmackvolles Essen"
- "Freundlicher Service"
- "Warme, einladende Atmosphäre"
- "Perfekt gewürztes Fleisch"
- "Leckere Saucen"

**Empfohlene Gerichte:**
1. Döner Kebab
2. Döner Teller
3. Pizza
4. Baklava

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Street Food Modern"** - Kombination aus:
- Großflächige Food-Fotografie im Hero
- Warme, einladende Farbpalette
- Klare, appetitanregende Produktdarstellung
- Mobile-First für schnelle Bestellentscheidungen

### 2. Signature-Effekt

**Warm Gradient Overlays:**
```css
background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(214, 40, 40, 0.05) 100%);
```

### 3. Animations-Level

**Moderat** (passend für Restaurant):
- Fade-in beim Scrollen für Sektionen
- Sanfte Hover-Transitions auf Cards
- Dezente Parallax für Hero-Bild

### 4. Besondere Sektionen

1. **Hero mit Signature-Dish**
   - Großes Döner-Bild, "Bester Döner in Offenburg" Claim
   - CTA: "Speisekarte ansehen" + "Anrufen & Bestellen"

2. **"Unsere Spezialitäten" Grid**
   - 3-4 Highlight-Gerichte mit Bildern
   - Döner, Lahmacun, Pizza, Baklava

3. **Bewertungs-Sektion**
   - Google Rating prominent
   - 2-3 ausgewählte Kundenzitate

4. **"So findest du uns"**
   - Interaktive Google Maps
   - Öffnungszeiten
   - Hinweis auf "Nur Barzahlung"

5. **Instagram-Feed Integration**
   - Letzte Posts zeigen
   - Link zum Profil

## Impressum-Daten

```
YUMMY Döner Offenburg
Ritterstraße 3
77652 Offenburg
Deutschland

Telefon: +49 781 25080527
```

## Referenzen

### Google Reviews Summary
- **Rating:** 4.7 ⭐ (771+ Bewertungen)
- **Restaurant Guru:** 3.9 ⭐ (773 Bewertungen)
- **Ranking:** Platz 63 unter den Restaurants in Offenburg

### Ausgewählte Testimonials

#### 1. Hasan Basri Mor
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
- **Zitat:** "A very stylish and modern kebab shop with nice dessert options."
- **Details:** Dine-in, €1-10 pro Person
- **Bewertete:** Essen, Service, Atmosphäre - jeweils 5/5
- **Quelle:** Google Reviews

#### 2. Loona Zimpfer
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
- **Bewertete:** Essen, Service, Atmosphäre - jeweils 5/5
- **Quelle:** Google Reviews

#### 3. Krystian Kasprzyk
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
- **Bewertete:** Essen, Service, Atmosphäre - jeweils 5/5
- **Quelle:** Google Reviews

### Weitere Kundenstimmen (Google Reviews)

**Begeisterte Stammkunden:**
> "YUMMY Döner hat Offenburg bisher gefehlt. Endlich ein Lokal mit sehr hochwertigen Zutaten, einem klasse Geschmack und richtig schönes Ambiente. Das kann sich sehen lassen, unbedingt probieren!"

**Qualitätsbewusste Kunden:**
> "Bester und qualitativster Dönerladen in Offenburg. Vor allem das Brot ist einmalig und die Zutaten sind sehr frisch und hochwertiger als bei anderen Dönerbuden. Die Saucen und das Fleisch sind was besonderes. Da zahle ich gerne ein paar Euro mehr."

**Fernreisende Fans:**
> "Ich komme aus Kiel, extra 850km nach Offenburg, um den besten Kebab zu essen. Ich war sehr beeindruckt und werde definitiv wiederkommen."

**Service-Bewertung:**
> "Das Personal ist legendär und super nett – 11/10!"

### Empfehlung für Website-Darstellung

Da es sich um ein Restaurant handelt und die Rezensenten Privatpersonen sind, empfehle ich für die Website:

1. **Google Reviews Widget** mit Rating und Anzahl der Bewertungen
2. **2-3 anonymisierte Zitate** (Vorname + Initiale, z.B. "Hasan B.")
3. **Link zu Google Maps** für weitere Bewertungen

**Hinweis:** Keine Profilbilder oder Firmenlogos verfügbar (Privatpersonen).

## Quellen

- [Instagram @yummy_offenburg](https://instagram.com/yummy_offenburg)
- [Restaurant Guru](https://restaurantguru.com/YUMMY-Doner-Offenburg-Offenburg)
- [Speisekarte.de](https://www.speisekarte.de/offenburg/restaurant/yummy_doener_offenburg)
- [Google Reviews](https://www.google.com/maps/place/YUMMY+D%C3%B6ner+Offenburg)
