# Style Guide - Ramen Tatsu Offenburg

## Über das Restaurant

**Name:** Ramen Tatsu Offenburg
**Branche:** Japanisches Ramen-Restaurant
**Konzept:** Authentische japanische Ramen-Küche mit Fokus auf traditionelle Rezepte und frische Zutaten

---

## Farbpalette

### Primärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Aka (Rot)** | `#C41E3A` | Primäre Akzentfarbe, CTAs, japanische Elemente |
| **Sumi (Tiefes Schwarz)** | `#1A1A1A` | Text, Header, Footer |
| **Shiro (Cremeweiß)** | `#FAF7F2` | Hintergrund, Kontrast |

### Sekundärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Kincha (Gold-Braun)** | `#C9A86C` | Akzente, Icons, Hover-States |
| **Hai (Warmes Grau)** | `#4A4A4A` | Sekundärer Text |
| **Matcha** | `#7B8B6F` | Subtile Akzente, Erfolgs-States |

### Gradient

```css
/* Hero Overlay */
background: linear-gradient(135deg, rgba(26, 26, 26, 0.9) 0%, rgba(196, 30, 58, 0.7) 100%);

/* Warmer Ramen-Dampf-Effekt */
background: linear-gradient(180deg, rgba(201, 168, 108, 0.1) 0%, transparent 100%);
```

---

## Typografie

### Schriftarten

**Headlines:** `"Noto Serif JP", "Playfair Display", serif`
- Elegant, traditionell, japanisch-inspiriert
- Gewicht: 600-700

**Body Text:** `"Noto Sans JP", "Inter", sans-serif`
- Klar, modern, gut lesbar
- Gewicht: 400-500

**Akzent/Japanisch:** `"Shippori Mincho", serif`
- Für japanische Schriftzeichen und Menü-Akzente

### Schriftgrößen

| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 (Hero) | 64px / 4rem | 40px / 2.5rem |
| H2 (Sections) | 48px / 3rem | 32px / 2rem |
| H3 (Cards) | 28px / 1.75rem | 24px / 1.5rem |
| Body | 18px / 1.125rem | 16px / 1rem |
| Small/Caption | 14px / 0.875rem | 14px / 0.875rem |

---

## Spacing-System

```css
--space-xs: 0.5rem;   /* 8px */
--space-sm: 1rem;     /* 16px */
--space-md: 1.5rem;   /* 24px */
--space-lg: 2.5rem;   /* 40px */
--space-xl: 4rem;     /* 64px */
--space-2xl: 6rem;    /* 96px */
```

### Sektions-Abstände

- Section Padding: `var(--space-2xl) 0`
- Container Max-Width: `1200px`
- Card Gap: `var(--space-lg)`

---

## Buttons & CTAs

### Primary Button

```css
.btn-primary {
  background: #C41E3A;
  color: #FAF7F2;
  padding: 1rem 2rem;
  border-radius: 4px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: #A01830;
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(196, 30, 58, 0.4);
}
```

### Secondary Button

```css
.btn-secondary {
  background: transparent;
  color: #C41E3A;
  border: 2px solid #C41E3A;
  padding: 1rem 2rem;
  border-radius: 4px;
}

.btn-secondary:hover {
  background: #C41E3A;
  color: #FAF7F2;
}
```

---

## Japanische Design-Elemente

### Traditionelle Muster

- **Seigaiha (Wellen):** Für Trennlinien, Hintergründe
- **Asanoha (Hanfblatt):** Subtile Textur-Pattern
- **Noren-Linien:** Vertikale Akzente, Divider

### Ikonografie

- Verwendung von minimalistischen Ramen-Schüssel-Icons
- Essstäbchen als grafisches Element
- Dampf-Animationen für Atmosphäre

---

## Animationen

**Level:** Moderat (Restaurant-Branche)

### Empfohlene Animationen

```css
/* Sanftes Einblenden */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Dampf-Animation */
@keyframes steam {
  0%, 100% {
    opacity: 0.6;
    transform: translateY(0) scale(1);
  }
  50% {
    opacity: 0.3;
    transform: translateY(-20px) scale(1.2);
  }
}

/* Hover-Lift */
.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}
```

### Timing

- Standard-Transition: `0.3s ease`
- Scroll-Reveal: `0.6s ease-out`
- Stagger-Delay: `0.1s` zwischen Elementen

---

## Firmendaten

### Kontakt

| Feld | Wert |
|------|------|
| **Firmenname** | Ramen Tatsu Offenburg |
| **Straße** | Hauptstraße 93 |
| **PLZ / Ort** | 77652 Offenburg |
| **Telefon** | +49 781 96717806 |
| **E-Mail** | info@ramen-tatsu.de (zu erstellen) |

### Google Bewertung

⭐ **4.6** von 5 Sternen (156 Bewertungen)

### Öffnungszeiten (typisch für Ramen-Restaurants)

| Tag | Zeit |
|-----|------|
| Montag | Ruhetag |
| Dienstag - Samstag | 11:30 - 14:30, 17:30 - 21:30 |
| Sonntag | 12:00 - 21:00 |

*Hinweis: Öffnungszeiten müssen mit dem Restaurant verifiziert werden*

---

## Content-Struktur

### Seitenstruktur

1. **Homepage** (`index.html`)
   - Hero mit Ramen-Bild
   - Über uns Teaser
   - Signature Dishes
   - Bewertungen
   - Standort & Öffnungszeiten

2. **Speisekarte** (`speisekarte.html`)
   - Ramen-Varianten
   - Vorspeisen
   - Beilagen
   - Getränke

3. **Über uns** (`ueber-uns.html`)
   - Geschichte & Philosophie
   - Team
   - Zutaten & Qualität

4. **Kontakt** (`kontakt.html`)
   - Kontaktformular
   - Anfahrt
   - Öffnungszeiten

5. **Impressum** (`impressum.html`)

6. **Datenschutz** (`datenschutz.html`)

### Typische Ramen-Menü-Kategorien

#### Ramen (Hauptgerichte)

| Gericht | Beschreibung | Preis (ca.) |
|---------|--------------|-------------|
| **Shoyu Ramen** | Klassische Sojasaucen-Brühe, Chashu, Ei, Nori, Frühlingszwiebeln | 13,90 € |
| **Miso Ramen** | Kräftige Miso-Brühe, Mais, Butter, Chashu | 14,90 € |
| **Tonkotsu Ramen** | Cremige Schweineknochen-Brühe, Chashu, Ei, Bambussprossen | 14,90 € |
| **Shio Ramen** | Leichte Salzbrühe, Hühnchen, Gemüse | 12,90 € |
| **Tantanmen** | Scharfe Sesam-Brühe, Hackfleisch, Pak Choi | 14,90 € |
| **Vegetarische Ramen** | Gemüsebrühe, Tofu, saisonales Gemüse | 12,90 € |

#### Vorspeisen

| Gericht | Beschreibung | Preis (ca.) |
|---------|--------------|-------------|
| **Gyoza (5 Stk.)** | Gebratene japanische Teigtaschen | 6,90 € |
| **Edamame** | Gesalzene Sojabohnen | 4,90 € |
| **Karaage** | Frittiertes Hühnchen, japanische Art | 7,90 € |

#### Beilagen

| Gericht | Preis (ca.) |
|---------|-------------|
| **Extra Chashu** | 3,50 € |
| **Ajitama (mariniertes Ei)** | 2,00 € |
| **Extra Nudeln** | 2,50 € |
| **Reis** | 2,50 € |

#### Getränke

| Getränk | Preis (ca.) |
|---------|-------------|
| **Japanisches Bier (Asahi/Sapporo)** | 4,50 € |
| **Grüner Tee** | 3,00 € |
| **Ramune (jap. Limonade)** | 3,50 € |
| **Softdrinks** | 2,90 € |

*Hinweis: Preise sind Schätzungen und müssen verifiziert werden*

---

## Team

*Keine Team-Informationen verfügbar. Bei Bedarf erstellen:*

- **Inhaber/Koch:** [Name erfragen]
- Authentische japanische Küche
- Fokus auf hausgemachte Brühen

---

## Bilder & Assets

### Benötigte Bilder

1. **Hero-Bild:** Dampfende Ramen-Schüssel (Nahaufnahme)
2. **Interieur:** Restaurant-Atmosphäre
3. **Gerichte:** Einzelne Ramen-Varianten
4. **Küche:** Zubereitung (authentisch)
5. **Team:** Koch/Inhaber bei der Arbeit

### Bildstil

- **Farbtemperatur:** Warm, einladend
- **Beleuchtung:** Natürlich + warmes Kunstlicht
- **Fokus:** Food-Fotografie mit Dampf und Textur
- **Perspektive:** 45° Winkel für Food, Eye-Level für Atmosphäre

### Stock-Bild-Quellen (Fallback)

- Unsplash: "ramen japanese food"
- Pexels: "ramen noodles"

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Izakaya Experience"** - Modernes japanisches Restaurant-Design

- **Hero:** Fullscreen-Video oder animiertes Bild mit Dampf-Effekt
- **Menü-Sektion:** Horizontales Scroll-Karussell auf Mobile
- **Split-Sections:** Bild links, Text rechts (alternierend)
- **Footer:** Minimalistisch mit japanischen Schriftzeichen

### 2. Signature-Effekt

**Dampf-Animation + Warm-Glow**

```css
/* Dampf-Effekt über Hero-Bild */
.steam-overlay {
  position: absolute;
  width: 100%;
  height: 200px;
  bottom: 0;
  background: linear-gradient(to top,
    rgba(250, 247, 242, 0.8) 0%,
    transparent 100%);
  animation: steam 4s ease-in-out infinite;
}

/* Warmer Glow bei Hover */
.menu-item:hover {
  box-shadow: 0 0 40px rgba(201, 168, 108, 0.3);
}
```

### 3. Animations-Level

**Moderat** - Passend für Restaurant-Branche

| Element | Animation |
|---------|-----------|
| Hero | Subtle Ken-Burns Zoom |
| Scroll | FadeInUp mit Stagger |
| Cards | Lift + Shadow auf Hover |
| CTAs | Scale + Glow |
| Dampf | Kontinuierliche Float-Animation |

### 4. Besondere Sektionen

1. **"Unsere Ramen" Showcase**
   - Große Bilder der Signature Dishes
   - Hover zeigt Zutaten
   - Japanische + deutsche Bezeichnung

2. **"Die Kunst der Brühe"**
   - Storytelling über 12-Stunden-Brühe
   - Timeline oder Step-by-Step Visual
   - Authentizitäts-Faktor

3. **Atmosphäre-Galerie**
   - Masonry-Grid mit Restaurant-Fotos
   - Lightbox für vergrößerte Ansicht

4. **Bewertungen-Slider**
   - Google Reviews Integration
   - Horizontales Scroll-Karussell
   - "4.6 ★ - 156 Bewertungen"

5. **Interaktive Karte**
   - Google Maps Embed
   - Custom Marker im Restaurant-Stil
   - Direkter "Route planen" Button

---

## Impressum (Entwurf)

```
IMPRESSUM

Ramen Tatsu Offenburg
Hauptstraße 93
77652 Offenburg

Telefon: +49 781 96717806
E-Mail: info@ramen-tatsu.de

[Weitere rechtliche Angaben nach Rücksprache mit dem Inhaber ergänzen:
- Inhaber/Geschäftsführer
- USt-IdNr.
- Zuständige Aufsichtsbehörde (falls erforderlich)]
```

---

## Datenschutz-Hinweise

Standard-Datenschutzerklärung für Restaurants:
- Datenerhebung bei Kontaktformular
- Google Maps Einbindung
- Cookies (falls verwendet)
- Rechte der Betroffenen

*Vollständige Datenschutzerklärung muss rechtlich geprüft werden*

---

## Technische Hinweise

### Performance

- Bilder: WebP Format, Lazy Loading
- Fonts: Font-Display Swap
- Critical CSS inline

### SEO

- Meta-Title: "Ramen Tatsu Offenburg | Authentische japanische Ramen"
- Meta-Description: "Genießen Sie authentische japanische Ramen in Offenburg. Hausgemachte Brühen, frische Zutaten. ⭐ 4.6 Google-Bewertung"
- Local SEO: Google My Business optimieren

### Responsive Breakpoints

```css
--mobile: 375px;
--tablet: 768px;
--desktop: 1024px;
--large: 1280px;
```

---

*Style Guide erstellt: Januar 2026*
*Basierend auf: Branchenanalyse (Keine Website vorhanden)*
