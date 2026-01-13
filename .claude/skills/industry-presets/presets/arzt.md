# Arzt/Praxis Preset

Branche: Ärzte, Zahnarztpraxen, Therapeuten, Physiotherapie

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Hero

```yaml
layout: centered
background: gradient (hell, beruhigend)
height: 100dvh
unique_element: false
```

| Element | Animation |
|---------|-----------|
| Headline | Statisch oder sanftes fade-in |
| Subline | fade-in (0.5s delay) |
| CTA | fade-in (0.8s delay) |

**VERBOTEN:** Schnelle Animationen, Blinkende Elemente, Laute Farben

---

## Text-Effekte

### Erlaubt (2-3 verwenden)

| Effekt | Einsatz |
|--------|---------|
| `fade` | Standard für alle |
| `blur-reveal` | Section-Überschriften |
| `stagger-list` | Leistungs-Cards |
| `counter` | Erfahrung, Patienten |

### Verboten

- letter-reveal, typewriter, split-lines, schnelle Animationen

---

## Animationen

```yaml
level: ruhig
duration: 0.8s - 1.2s
timing: ease-out
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Sanftes Blau (#4299e1), Türkis (#38b2ac) |
| Secondary | Helles Grau (#e2e8f0) |
| Accent | Grün (#48bb78), Mint (#9ae6b4) |
| Background | Weiß, helles Blau (#f0f9ff) |
| Text | Dunkelgrau (#2d3748) |

**NICHT:** Rot (außer Notfall), Orange, Grelle Farben

---

## Typography

- **Headings:** Freundliche Sans-Serif
- **Body:** Gut lesbare Sans-Serif
- Empfohlen: Nunito + Open Sans

---

## UX

```yaml
cta_style: einladend
trust_signals: WICHTIG
testimonials: dezent (mit Einwilligung)
```

### Trust-Elemente (PFLICHT)

- Ärztekammer/Kassenzulassung
- Qualifikationen
- Öffnungszeiten prominent
- Barrierefreier Zugang (wenn vorhanden)

### CTA-Texte

- "Termin vereinbaren"
- "Online buchen"

**NICHT:** Dringlichkeit, Aggressive Formulierungen
