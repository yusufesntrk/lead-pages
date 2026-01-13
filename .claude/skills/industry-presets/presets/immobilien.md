# Immobilien Preset

Branche: Immobilienmakler, Hausverwaltung, Bauträger, Architekten

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Hero

```yaml
layout: fullscreen-image oder asymmetric
background: Hochwertiges Immobilien-Bild
height: 100dvh
unique_element: optional (dezente Parallax)
```

| Element | Animation |
|---------|-----------|
| Headline | fade-in oder slide-up |
| Subline | fade-in (0.4s delay) |
| CTA | fade-in (0.6s delay) |

**ERLAUBT:** Dezente Parallax auf Hintergrundbild, Overlay-Animationen

---

## Text-Effekte

### Erlaubt (3-4 verwenden)

| Effekt | Einsatz |
|--------|---------|
| `underline-scroll` | Überschriften |
| `blur-reveal` | Section-Headlines |
| `stagger-list` | Property-Cards, Services |
| `counter` | Verkaufte Objekte, Jahre |
| `fade` | Beschreibungen |

### Verboten

- letter-reveal, typewriter

---

## Animationen

```yaml
level: moderat
duration: 0.6s - 0.8s
timing: ease-out
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Dunkelblau (#1e3a5f), Anthrazit (#2d3748) |
| Secondary | Grau (#718096), Taupe (#a39171) |
| Accent | Gold (#c9a227), Kupfer (#b87333) |
| Background | Weiß, helles Beige (#faf8f5) |
| Text | Dunkelgrau (#2d3748) |

**Luxury:** Schwarz, Gold (#d4af37), Weiß

---

## Typography

- **Headings:** Elegante Serif oder moderne Sans-Serif
- **Body:** Clean Sans-Serif
- Empfohlen: Playfair Display + Source Sans Pro

---

## UX

```yaml
cta_style: prominent aber elegant
trust_signals: SEHR WICHTIG
testimonials: prominent
```

### Trust-Elemente (PFLICHT)

- IVD-Mitgliedschaft
- Anzahl verkaufter Objekte
- "Seit [Jahr] in [Region]"
- Google-Bewertungen
- Regionale Kompetenz

### CTA-Texte

- "Kostenlose Bewertung anfordern"
- "Objekte entdecken"
- "Beratungstermin vereinbaren"
