# Style Guide: Diyar's Laufsteg

> Türkisches Restaurant & Café in Offenburg
> *Erstellt am: 06.01.2026*

---

## Farbpalette

### Primärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Türkis-Blau** | `#0891B2` | Primäre Akzentfarbe, CTAs, Links |
| **Warmes Gold** | `#D97706` | Sekundäre Akzentfarbe, Highlights, Icons |
| **Dunkles Anthrazit** | `#1F2937` | Überschriften, Logo-Hintergrund |

### Sekundärfarben

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Cremeweiß** | `#FFFBEB` | Hintergründe, Karten |
| **Warmes Beige** | `#FEF3C7` | Sektion-Hintergründe |
| **Terrakotta** | `#C2410C` | Akzente, Hover-States |
| **Dunkelbraun** | `#78350F` | Texte auf hellem Grund |

### Graustufen

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Text Dunkel** | `#374151` | Fließtext |
| **Text Medium** | `#6B7280` | Sekundärer Text |
| **Border** | `#E5E7EB` | Trennlinien, Borders |
| **Background Light** | `#F9FAFB` | Helle Sektionen |

---

## Typografie

### Schriftarten

```css
/* Überschriften - Elegant mit orientalischem Touch */
font-family: 'Playfair Display', Georgia, serif;

/* Fließtext - Modern und gut lesbar */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;

/* Akzente/Preise - Für Speisekarte */
font-family: 'DM Sans', sans-serif;
```

### Schriftgrößen

| Element | Desktop | Mobile | Gewicht |
|---------|---------|--------|---------|
| H1 (Hero) | 56px | 36px | 700 |
| H2 (Sektionen) | 40px | 28px | 600 |
| H3 (Karten) | 24px | 20px | 600 |
| Body | 18px | 16px | 400 |
| Small | 14px | 14px | 400 |
| Button | 16px | 16px | 600 |

### Zeilenhöhen

- Überschriften: 1.2
- Fließtext: 1.7
- UI-Elemente: 1.4

---

## Spacing-System

```css
--space-xs: 4px;
--space-sm: 8px;
--space-md: 16px;
--space-lg: 24px;
--space-xl: 32px;
--space-2xl: 48px;
--space-3xl: 64px;
--space-4xl: 96px;

/* Sektions-Padding */
--section-padding-y: 80px; /* Desktop */
--section-padding-y-mobile: 48px;
```

---

## Komponenten

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: linear-gradient(135deg, #0891B2 0%, #0E7490 100%);
  color: white;
  padding: 14px 28px;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 4px 14px rgba(8, 145, 178, 0.3);
  transition: transform 0.2s, box-shadow 0.2s;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(8, 145, 178, 0.4);
}

/* Secondary Button */
.btn-secondary {
  background: transparent;
  color: #1F2937;
  border: 2px solid #D97706;
  padding: 12px 26px;
  border-radius: 8px;
}

.btn-secondary:hover {
  background: #D97706;
  color: white;
}
```

### Karten

```css
.card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid #E5E7EB;
}

.card:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}
```

### Speisekarten-Item

```css
.menu-item {
  display: flex;
  justify-content: space-between;
  padding: 16px 0;
  border-bottom: 1px dashed #E5E7EB;
}

.menu-item-name {
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  color: #1F2937;
}

.menu-item-price {
  font-family: 'DM Sans', sans-serif;
  font-weight: 600;
  color: #D97706;
}
```

---

## Firmendaten

### Kontaktinformationen

| Feld | Wert |
|------|------|
| **Firmenname** | Diyar's Laufsteg |
| **Straße** | Hauptstraße 84 |
| **PLZ/Ort** | 77652 Offenburg |
| **Telefon** | +49 781 20366641 |
| **E-Mail** | *Nicht bekannt* |

### Öffnungszeiten

| Tag | Zeiten |
|-----|--------|
| Montag | 08:00 - 23:00 Uhr |
| Dienstag | 08:00 - 23:00 Uhr |
| Mittwoch | 08:00 - 23:00 Uhr |
| Donnerstag | 08:00 - 23:00 Uhr |
| Freitag | 08:00 - 01:00 Uhr |
| Samstag | 08:00 - 01:00 Uhr |
| Sonntag | 08:00 - 23:00 Uhr |

**Besonderheit:** Frühstück bis 16:00 Uhr

### Bewertungen

- **Google Rating:** 4.6 ⭐ (288 Bewertungen)
- **Preisniveau:** €10-20 pro Person

### Küche & Kategorien

- Türkische Küche
- Orientalische Spezialitäten
- Frühstück & Brunch
- Halal
- Café

---

## Speisekarten-Kategorien (recherchiert)

### Frühstück
- Türkisches Frühstück für 2 Personen *(empfohlen)*
- Rührei-Variationen
- Gekochte Eier

### Hauptgerichte
- Cheeseburger *(beliebt)*
- Kebab-Variationen
- Falafel
- Fleischgerichte

### Beilagen
- Pommes Frites
- Süßkartoffelpommes
- Frische Salate

### Desserts
- Crêpes
- Orientalische Süßspeisen

### Getränke

**Heiß:**
- Türkischer Tee
- Kaffee-Spezialitäten

**Kalt:**
- Frisch gepresste Säfte (Orangensaft)
- Softdrinks

**Alkoholisch:**
- Bier
- Cocktails (Mojito)
- Aperol Spritz

---

## Logo

### Beschreibung
- **Form:** Rundes, schwarzes Logo
- **Text:** "Diyar's Laufsteg" in eleganter Schrift
- **Stil:** Minimalistisch, modern mit orientalischem Touch

### Logo-Platzierung
- Header: Links, max. Höhe 48px
- Footer: Zentriert, max. Höhe 64px
- Favicon: Initialen "DL" oder vereinfachtes Icon

### Fallback (Text-Logo)
```css
.text-logo {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-size: 28px;
  color: #1F2937;
  letter-spacing: -0.5px;
}

.text-logo span {
  color: #D97706;
}
```

**Format:** Diyar's <span>Laufsteg</span>

---

## Bilder & Medien

### Bildstil
- Warme, einladende Atmosphäre
- Fokus auf Speisen (Food Photography)
- Authentische orientalische Ästhetik
- Menschen beim Genießen

### Bildquellen (zu beschaffen)
1. Hero-Bild: Frühstückstisch mit türkischen Spezialitäten
2. Restaurant-Innenraum
3. Terrasse/Außenbereich
4. Signatur-Gerichte (Frühstück für 2, Kebab)

### Bildbehandlung
```css
.image-overlay {
  background: linear-gradient(
    180deg,
    rgba(31, 41, 55, 0) 0%,
    rgba(31, 41, 55, 0.7) 100%
  );
}
```

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Warme Einladung"** - Ein Layout das Gastfreundschaft ausstrahlt:

- **Hero:** Vollbild-Bild mit Frühstückstisch, darüber halbtransparente Textur
- **Services/Angebot:** Horizontaler Scroll mit Food-Karten (Mobile) / Grid (Desktop)
- **Über uns:** Split-Screen mit Bild links, Geschichte rechts
- **Speisekarte:** Tab-basierte Navigation nach Kategorien
- **Testimonials:** Karussell mit Google Reviews

### 2. Signature-Effekt

**Orientalische Muster-Akzente:**
- Dezente geometrische Muster als Hintergrund-Texturen
- Goldene Linien-Ornamente bei Sektions-Übergängen
- Warme Farbverläufe (Gold → Terrakotta)

```css
.oriental-pattern {
  background-image: url('pattern-subtle.svg');
  background-size: 200px;
  opacity: 0.05;
}

.gold-divider {
  height: 2px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    #D97706 50%,
    transparent 100%
  );
  max-width: 200px;
  margin: 24px auto;
}
```

### 3. Animations-Level: **Moderat**

Als Restaurant mit Café-Atmosphäre:
- Sanfte Fade-ins beim Scrollen (300ms)
- Hover-Effekte auf Speisekarten-Items
- Smooth Scroll für Navigation
- Subtile Parallax im Hero (optional)

```css
/* Scroll Reveal */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Menu Item Hover */
.menu-item:hover {
  background: #FFFBEB;
  padding-left: 8px;
  transition: all 0.3s ease;
}
```

### 4. Besondere Sektionen

1. **"Unsere Spezialitäten" Showcase**
   - 3-4 Signature-Gerichte mit großen Bildern
   - Hover zeigt Beschreibung
   - Preise prominent

2. **Frühstücks-Highlight-Banner**
   - "Frühstück bis 16 Uhr" als USP
   - Bild des türkischen Frühstücks für 2
   - Direkter CTA zur Reservierung

3. **Google Reviews Integration**
   - Live-Rating Badge
   - 2-3 ausgewählte Bewertungen
   - Link zu allen Reviews

4. **Interaktive Karte**
   - Google Maps Embed
   - Anfahrtsbeschreibung
   - Parkplatz-Info

5. **Atmosphäre-Galerie**
   - Masonry-Grid mit Restaurant-Fotos
   - Innenraum, Terrasse, Speisen
   - Lightbox für Vollansicht

---

## Referenzen & Testimonials

### Google Reviews Zusammenfassung

| Metrik | Wert |
|--------|------|
| **Google Rating** | 4.6 ⭐ |
| **Anzahl Bewertungen** | 288+ |
| **Restaurant Guru** | 4.6 ⭐ (254 Bewertungen) |
| **Preisniveau** | €10-20 pro Person |

### Ausgewählte Testimonials

#### Testimonial 1 - Stammgast
> "Ich kann gar nicht zählen, wie oft ich schon im Laufsteg war - und das hat seinen Grund. Zuerst muss ich den guten Service loben. Man merkt, dass der Kellner seinen Job gerne macht und auch Extrawünsche sind kein Problem. Im Sommer kann man toll draußen auf dem Marktplatz sitzen und sich wie im Kurzurlaub fühlen. Zudem gibt es super leckere Salate mit einem tollen Dressing sowie eine von Woche zu Woche wechselnde Mittagskarte mit feinen Gerichten und bezahlbaren Preisen. Auch beim Frühstück gibt es eine tolle Auswahl - am Wochenende sollte man reservieren, da der Andrang meistens sehr groß ist. Ich empfehle das Laufsteg wärmstens!"
- **Quelle:** TripAdvisor
- **Kategorie:** Stammgast, Service, Frühstück

#### Testimonial 2 - Türkisches Frühstück
> "Das orientalische Frühstück für 2 Personen ist sehr schön angerichtet und geschmacklich gibt es nichts zu beanstanden. Das Preis-Leistungs-Verhältnis stimmt absolut und der Service war auch freundlich."
- **Quelle:** Google Reviews
- **Kategorie:** Frühstück, Preis-Leistung
- **Bewertung:** 5 Sterne

#### Testimonial 3 - Team & Atmosphäre
> "Der Chef und das gesamte Team sind super freundlich und zuvorkommend, das Preis-Leistungs-Verhältnis stimmt und sowohl Essen als auch Getränke sind sehr gut."
- **Quelle:** Restaurant Guru
- **Kategorie:** Team, Gesamterlebnis

#### Testimonial 4 - Burger-Empfehlung
> "Der Burger war sehr lecker und kann auch ohne Brot bestellt werden. Die Preise sind angemessen."
- **Quelle:** Google Reviews
- **Kategorie:** Hauptgerichte, Burger

### Wiederkehrende Stärken (aus Bewertungen)

| Aspekt | Häufigkeit | Zusammenfassung |
|--------|------------|-----------------|
| **Freundlicher Service** | Sehr häufig | Personal wird durchweg als freundlich und hilfsbereit beschrieben |
| **Gutes Preis-Leistungs-Verhältnis** | Sehr häufig | Demokratische Preise, €10-20 pro Person |
| **Lage am Marktplatz** | Häufig | Zentrale Lage, Parkhaus direkt vor der Tür, Terrasse im Sommer |
| **Frühstück bis 16 Uhr** | Häufig | Besonderes Highlight, türkisches Frühstück für 2 besonders beliebt |
| **Atmosphäre** | Häufig | Gemütlich, einladend, "wie im Kurzurlaub" |

### Empfehlung für Website

Da keine individuellen Personenfotos verfügbar sind, empfehle ich:

1. **Google Reviews Widget** - Dynamische Einbindung der aktuellen Bewertungen
2. **Rating Badge** - 4.6 ⭐ prominent im Hero oder Header
3. **Zitat-Karussell** - 3-4 der obigen Testimonials rotierend
4. **"Unsere Gäste sagen..."** Sektion mit:
   - Große Anführungszeichen als Design-Element
   - Goldene Akzente (#D97706)
   - Link zu Google Reviews

### Hinweis zu Assets

⚠️ **Keine Personenfotos verfügbar** - Die Testimonials stammen von anonymen Google/TripAdvisor Reviews ohne Profilbilder.

**Alternative Darstellung:**
- Abstrakte Avatar-Icons mit Initialen
- Dekorative Ornamente statt Fotos
- Fokus auf Text und Sternebewertung

---

## Social Media

### Gefundene Profile
- **Facebook:** facebook.com/diyarslaufsteg *(existiert, aber nicht verifiziert)*
- **Instagram:** @diyars_laufsteg (1.355 Follower, 18 Posts)

### Empfohlene Verlinkungen
- Google Maps Profil
- Google Reviews
- Instagram @diyars_laufsteg

---

## SEO-Keywords

- Türkisches Restaurant Offenburg
- Frühstück Offenburg
- Orientalisches Essen Offenburg
- Halal Restaurant Offenburg
- Türkisches Frühstück
- Kebab Offenburg
- Café Offenburg Hauptstraße

---

## Technische Hinweise

### Performance
- Lazy Loading für Bilder
- WebP-Format mit JPEG-Fallback
- Critical CSS inline
- Schriften mit font-display: swap

### Accessibility
- Kontrastverhältnis min. 4.5:1
- Focus-States für alle interaktiven Elemente
- Alt-Texte für alle Bilder
- Skip-to-content Link

### Mobile First
- Touch-Targets min. 44px
- Hamburger-Menü unter 768px
- Sticky Header mit Telefon-Button
- Click-to-call für Telefonnummer
