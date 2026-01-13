# Rechtsanwalt Preset

Branche: Rechtsanwälte, Kanzleien, Notare

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Hero

```yaml
layout: centered
background: gradient (dunkel, seriös)
height: 100dvh
unique_element: false
```

| Element | Animation |
|---------|-----------|
| Headline | Statisch |
| Subline | fade-in (0.5s delay) |
| CTA | fade-in (0.8s delay) |

**VERBOTEN:** letter-reveal, Animierte SVGs, Parallax, Floating elements, Bunte Farben

---

## Text-Effekte

### Erlaubt (min. 3 verwenden)

| Effekt | Einsatz |
|--------|---------|
| `underline-scroll` | Rechtsgebiete |
| `blur-reveal` | Section-Überschriften |
| `stagger-list` | Rechtsgebiete-Cards |
| `counter` | Jahre Erfahrung |
| `fade` | Paragraphen, Team |

### Verboten

- letter-reveal, gradient-reveal, typewriter, split-lines

---

## Animationen

```yaml
level: dezent
duration: 0.6s - 0.8s
timing: ease-out
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Dunkelblau (#1a365d), Anthrazit (#2d3748) |
| Secondary | Grau (#718096) |
| Accent | Gold (#b8860b), Bordeaux (#8b0000) |
| Background | Weiß, helles Grau (#f8f9fa) |
| Text | Dunkelgrau (#2d3748) |

---

## Typography

- **Headings:** Elegante Serif
- **Body:** Clean Sans-Serif
- Empfohlen: Playfair Display + Source Sans Pro

---

## UX

```yaml
cta_style: subtle
trust_signals: SEHR WICHTIG
testimonials: dezent (Datenschutz!)
```

### Trust-Elemente (PFLICHT)

- Rechtsanwaltskammer-Zugehörigkeit
- Fachanwalt-Titel
- "Seit [Jahr] in [Stadt]"
- Mitgliedschaften (DAV)

### CTA-Texte

- "Erstberatung anfragen"
- "Kontakt aufnehmen"

**NICHT:** "Jetzt loslegen!", Dringlichkeit, Emojis
