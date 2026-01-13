# Handwerk Preset

Branche: Handwerker, Elektriker, Sanitär, Maler, Schreiner, Dachdecker, KFZ

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Hero

```yaml
layout: centered oder asymmetric
background: gradient oder dezentes Arbeitsfoto
height: 100dvh
unique_element: false
```

| Element | Animation |
|---------|-----------|
| Headline | Statisch oder fade-in |
| Subline | fade-in (0.4s delay) |
| CTA | fade-in (0.6s delay) |

**VERBOTEN:** Komplexe Animationen, Parallax, Animierte SVGs

---

## Text-Effekte

### Erlaubt (2-3 verwenden)

| Effekt | Einsatz |
|--------|---------|
| `fade` | Standard |
| `stagger-list` | Leistungs-Cards |
| `counter` | Erfahrung, Projekte |
| `underline-scroll` | Sparsam |

### Verboten

- letter-reveal, gradient-reveal, typewriter, split-lines, blur-reveal

---

## Animationen

```yaml
level: minimal
duration: 0.5s - 0.6s
timing: ease-out
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Branchenfarbe (siehe unten) |
| Secondary | Grau (#6b7280), Anthrazit (#374151) |
| Accent | Orange (#f59e0b), Gelb (#eab308) |
| Background | Weiß, helles Grau (#f9fafb) |
| Text | Dunkelgrau (#1f2937) |

**Branchenfarben:** Elektriker=Blau/Gelb, Sanitär=Blau, Maler=Orange, Schreiner=Braun, Dachdecker=Rot

---

## Typography

- **Headings:** Kräftige Sans-Serif
- **Body:** Klare Sans-Serif
- Empfohlen: Montserrat + Open Sans

**NICHT:** Script-Fonts, dünne Schriften

---

## UX

```yaml
cta_style: direkt, klar
trust_signals: SEHR WICHTIG
testimonials: wichtig
```

### Trust-Elemente (PFLICHT)

- Meisterbrief/Innungsmitglied
- Jahre Erfahrung
- Google-Bewertungen
- Notdienst (wenn vorhanden)
- **Telefonnummer PROMINENT!**

### CTA-Texte

- "Angebot anfordern"
- "Jetzt anrufen: XXX"
- "Rückruf anfordern"
