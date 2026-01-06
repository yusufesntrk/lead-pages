# Style Guide - Billard Cafe Bistro

## Firmeninformationen

| Feld | Wert |
|------|------|
| **Firmenname** | Billard Cafe Bistro |
| **Branche** | Billard-Bar / Café / Bistro |
| **Adresse** | Unionrampe 6, 77652 Offenburg |
| **Telefon** | +49 781 95579047 |
| **Email** | Nicht bekannt |
| **Google Rating** | 4.3 ⭐ (130 Bewertungen) |

---

## Öffnungszeiten

| Tag | Zeiten |
|-----|--------|
| Montag | Geschlossen |
| Dienstag | Geschlossen |
| Mittwoch | 17:00 - 02:00 Uhr |
| Donnerstag | 17:00 - 02:00 Uhr |
| Freitag | 17:00 - 05:00 Uhr |
| Samstag | 17:00 - 05:00 Uhr |
| Sonntag | 17:00 - 02:00 Uhr |

---

## Farbpalette

### Primärfarben (Billard-Theme)
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Billard-Grün** | `#1B5E20` | Primärfarbe, Billardtisch-Assoziation |
| **Dunkelgrün** | `#0D3B12` | Header, Footer, dunkle Sektionen |
| **Smaragd** | `#2E7D32` | Hover-States, Akzente |

### Akzentfarben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Gold/Messing** | `#D4AF37` | CTAs, Highlights, edle Akzente |
| **Amber** | `#FFA000` | Sekundäre Buttons, Badges |
| **Warmweiß** | `#FFFBF0` | Hintergründe mit warmem Touch |

### Neutrale Farben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Holzbraun** | `#4E3629` | Texte, Queue-Assoziation |
| **Creme** | `#F5F1E8` | Helle Hintergründe |
| **Anthrazit** | `#1A1A2E` | Dunkle Hintergründe, Footer |
| **Dunkelblau** | `#101C36` | Alternative dunkle Sektion |

---

## Typografie

### Überschriften
```css
font-family: 'Playfair Display', Georgia, serif;
```
- H1: 48px / 3rem, font-weight: 700
- H2: 36px / 2.25rem, font-weight: 600
- H3: 28px / 1.75rem, font-weight: 600
- H4: 22px / 1.375rem, font-weight: 500

### Fließtext
```css
font-family: 'Poppins', 'Open Sans', sans-serif;
```
- Body: 16px / 1rem, font-weight: 400
- Small: 14px / 0.875rem
- Line-height: 1.6

### Akzent-Font (für Menü/Preise)
```css
font-family: 'Roboto Slab', serif;
```

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

### Primary Button
```css
background: linear-gradient(135deg, #D4AF37 0%, #C5A028 100%);
color: #1A1A2E;
padding: 14px 32px;
border-radius: 8px;
font-weight: 600;
text-transform: uppercase;
letter-spacing: 1px;
box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
transition: all 0.3s ease;
```

### Secondary Button
```css
background: transparent;
border: 2px solid #D4AF37;
color: #D4AF37;
padding: 12px 28px;
border-radius: 8px;
```

### Dark Button (auf hellen Hintergründen)
```css
background: #1B5E20;
color: #FFFFFF;
padding: 14px 32px;
border-radius: 8px;
```

---

## Angebot & Services

### Getränke
- ✅ Alkohol
- ✅ Bier
- ✅ Cocktails
- ✅ Kaffee
- ✅ Spirituosen
- ✅ Wein

### Speisen
- ✅ Kleine Gerichte / Snacks
- ✅ Late-Night Food
- ✅ Vor-Ort-Verzehr

### Aktivitäten
- ✅ Billard (Hauptattraktion)
- ✅ Darts
- ✅ Karaoke

### Ausstattung
- ✅ Bar vor Ort
- ✅ Toiletten
- ✅ WLAN
- ✅ Sitzplätze
- ✅ Reservierungen möglich
- ⚠️ Raucherbereich vorhanden

### Zahlungsmethoden
- ✅ Bargeld
- ✅ Kreditkarten
- ✅ NFC Mobile Payment
- ✅ Schecks

### Atmosphäre
- Casual / Entspannt
- Gemütlich
- Gruppenfreundlich

---

## Preise

| Angebot | Preis |
|---------|-------|
| Billard (pro Stunde) | ~6 € |
| Durchschnittliche Ausgabe pro Person | 9 - 24 € |

---

## Assets

### Logo
- **Status:** Kein offizielles Logo gefunden
- **Empfehlung:** Text-Logo mit Billardkugel-Icon erstellen
- **Stil:** Modern, minimalistisch mit Billard-Element (8er-Kugel oder Queue)

### Hauptbild (heruntergeladen)
**Datei:** `assets/interior-main.jpg`

**Bildbeschreibung:**
- Stehtische mit schwarzen Barhockern
- Spielautomaten im Hintergrund
- Grüne Neon-Beleuchtung (charakteristisch!)
- Deutsche Flagge an der Wand
- Heller Korkboden
- Bar-Bereich mit Getränkeregalen
- Wanduhr und "Mustang Jeans" Schild (Vintage-Deko)
- Gemütliche, entspannte Atmosphäre

---

## Team-Sektion

**Status:** Keine Team-Informationen gefunden.

Das Billard Cafe Bistro scheint ein inhabergeführtes kleines Lokal zu sein. In Bewertungen werden "freundliches Personal" und "guter Service" erwähnt, aber keine spezifischen Namen.

**Empfehlung:** Team-Sektion weglassen oder generische "Unser Team" Sektion mit allgemeinem Text erstellen.

---

## Speisekarte

**Status:** Keine detaillierte Speisekarte verfügbar.

Das Café bietet hauptsächlich Getränke und kleine Snacks an. Der Fokus liegt auf dem Billard-Spielerlebnis, nicht auf Gastronomie.

**Empfehlung:** Statt detaillierter Speisekarte eine "Angebot"-Sektion mit Kategorien:
- Warme Getränke
- Softdrinks
- Bier & Spirituosen
- Cocktails
- Snacks & kleine Gerichte

---

## Referenzen

### Google Reviews Summary
- **Gesamtbewertung:** ⭐ 4.3/5 (132 Bewertungen)
- **Quelle:** [Google Maps](https://www.google.com/maps/place/Billard+Cafe+Bistro/)

### Ausgewählte Bewertungen

#### 1. Robert Searley
- **Bewertung:** Service: 5/5, Atmosphäre: 5/5
- **Datum:** ca. September 2025
- **Zitat:** *"Great place to play billiards, two tables in very good condition and very reasonably priced. Paid €6 for an hour."*
- **Besonderheit:** Mitarbeiter Patrik half freundlich beim Wiederfinden einer vergessenen Tasche
- **Quelle:** [RestaurantGuru](https://restaurantguru.com/Cafe-Billard-Offenburg)

#### 2. Anonymer Gast (KennstDuEinen)
- **Bewertung:** 5/5 Sterne
- **Titel:** *"Treffpunkt für jung und alt"*
- **Zitat:** *"Hier treffen sich überwiegend die Jüngsten aus dem Ort. Es gibt aber auch Stammgäste mittleren Alters. Eine gute Möglichkeit Billard oder Dart zu spielen oder sich einfach nur an die Theke zu setzen. Man findet schnell Anschluss."*
- **Quelle:** [KennstDuEinen](https://www.kennstdueinen.de/cafe-niedernhausen-billard-cafe-bistro-d12162.html)

#### 3. Christian Thiel
- **Bewertung:** Service: 5/5
- **Datum:** ca. März 2025
- **Servicetyp:** Vor-Ort-Besuch
- **Quelle:** [RestaurantGuru](https://restaurantguru.com/Cafe-Billard-Offenburg)

#### 4. Schwarz Sascha
- **Bewertung:** Service: 3/5, Atmosphäre: 2/5
- **Datum:** ca. Dezember 2025
- **Anmerkung:** *"Parkplatz schwer zu finden"*
- **Preiskategorie:** €10–20 pro Person
- **Quelle:** [RestaurantGuru](https://restaurantguru.com/Cafe-Billard-Offenburg)

### Häufig gelobte Aspekte
- ✅ Sehr freundliches Personal
- ✅ Billardtische in hervorragendem Zustand
- ✅ Faire Preise (ca. 6€/Stunde Billard)
- ✅ Ruhige, entspannte Atmosphäre
- ✅ Einziger Ort in der Gegend, der spät nachts geöffnet hat
- ✅ Gute Getränkeauswahl

### Kritikpunkte (aus Bewertungen)
- ⚠️ Parkplatz schwer zu finden
- ⚠️ Nur Barzahlung möglich
- ⚠️ Raucherbereich vorhanden (kann störend sein)

### Assets
**Hinweis:** Keine herunterladbaren Personenfotos oder Firmenlogos verfügbar, da alle Bewertungen von Privatpersonen stammen (keine Firmenkunden).

**Empfehlung für Website:**
- Google Reviews Widget mit 4.3-Sterne-Rating einbinden
- 2-3 der besten Zitate als Testimonial-Slider
- Link zu allen Google-Bewertungen

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Lounge Atmosphere"** - Dunkles, elegantes Design mit goldenen Akzenten
- Hero: Vollbild-Foto des Innenraums mit Overlay
- Split-Sections für verschiedene Bereiche (Bar, Billard, Darts)
- Card-Grid für Services/Angebote

### 2. Signature-Effekt

**Neon-Glow & Ambient Lighting**
- Subtile Neon-Glows um wichtige Elemente (wie in einer echten Bar-Atmosphäre)
- Grüne Neon-Akzente (wie im echten Lokal sichtbar!)
- Dunkle Hintergründe mit warmen Lichtakzenten

```css
/* Grüner Neon-Glow (passend zum echten Lokal) */
.neon-green {
  box-shadow: 0 0 10px rgba(0, 255, 100, 0.5),
              0 0 20px rgba(0, 255, 100, 0.3),
              0 0 30px rgba(0, 255, 100, 0.1);
}

/* Goldener Glow für CTAs */
.neon-gold {
  box-shadow: 0 0 10px rgba(212, 175, 55, 0.5),
              0 0 20px rgba(212, 175, 55, 0.3),
              0 0 30px rgba(212, 175, 55, 0.1);
}
```

### 3. Animations-Level: **Moderat**

| Element | Animation |
|---------|-----------|
| Hero | Subtle parallax, fade-in Titel |
| Cards | Hover-lift mit Glow |
| Buttons | Pulse-Effekt bei CTAs |
| Sektionen | Scroll-reveal von unten |
| Bilder | Sanfter Zoom bei Hover |

**Keine:** Aggressive Animationen, blinkende Elemente

### 4. Besondere Sektionen

1. **Hero mit Atmosphäre-Foto**
   - Vollbild mit dunklem Overlay
   - "Dein Abend. Dein Spiel." als Tagline
   - CTA: "Reservieren" + "Angebot entdecken"

2. **"Das Erlebnis" - Split Section**
   - Links: Billard & Darts beschrieben
   - Rechts: Großes Bild

3. **Öffnungszeiten als stilisierte Karte**
   - Neon-Uhr Icon
   - "Wann wir für dich da sind"

4. **Getränke-Showcase**
   - Horizontaler Scroll mit Kategorien
   - Cocktails, Bier, Spirituosen als Cards

5. **Atmosphäre-Galerie**
   - Masonry Grid mit Innenaufnahmen
   - Hover: Leichte Vergrößerung

6. **Late Night CTA**
   - "Bis 5 Uhr morgens am Wochenende"
   - Einladend für Nachtaktive

7. **Google Reviews Integration**
   - 4.3 Sterne prominent
   - 2-3 Zitate aus echten Reviews
   - Link zu allen Bewertungen

8. **Kontakt & Anfahrt**
   - Google Maps Embed
   - Kontaktdaten
   - "Nur Barzahlung" Hinweis (wichtig!)

---

## SEO Keywords

- Billard Offenburg
- Billard Cafe Offenburg
- Billardhalle Offenburg
- Darts spielen Offenburg
- Spätnachts Bar Offenburg
- Karaoke Offenburg
- Cocktails Offenburg
- Late Night Offenburg

---

## Wichtige Hinweise für Entwicklung

1. **Nur Barzahlung erwähnen** - Wichtig für Gäste zu wissen
2. **Late-Night Focus** - USP: Bis 5 Uhr am Wochenende
3. **Raucherbereich** - Hinweis auf separate Raucherbereiche
4. **Reservierungen** - Aktiv bewerben
5. **Keine Lieferung/Takeaway** - Nicht erwähnen
6. **WLAN verfügbar** - Als Benefit nennen

---

## Rechtliche Seiten

### Impressum (zu erstellen)
```
Billard Cafe Bistro
Unionrampe 6
77652 Offenburg

Telefon: +49 781 95579047

[Inhaberangaben müssen noch ergänzt werden]
```

### Datenschutz
Standard-Datenschutzerklärung für Gastronomie erstellen.

---

## Zusammenfassung Design-Richtung

**Mood:** Entspannte Nacht-Lounge, elegantes Billard-Ambiente
**Primär:** Dunkelgrün (Billardtisch) + Gold (Eleganz)
**Sekundär:** Dunkles Anthrazit/Blau für Tiefe
**Akzente:** Warme Neon-Glows, goldene Highlights
**Typografie:** Elegant (Playfair) + Modern (Poppins)
**Bilder:** Warme, atmosphärische Innenaufnahmen
**Animation:** Subtil, loungy, nicht aufdringlich
