---
name: industry-presets
description: Branchenspezifische Design-Presets für Website-Erstellung. Definiert Hero-Stil, Animationen, Farben und UX-Patterns je Branche. Verwende diesen Skill um konsistente, branchengerechte Websites zu erstellen.
allowed-tools: Read, Glob, Grep
---

# Industry Presets

Branchenspezifische Design-Vorgaben für konsistente, professionelle Websites.

## Wann verwenden

- Vor Website-Erstellung → Preset der Branche laden
- Bei Unsicherheit über Design-Entscheidungen
- Um branchengerechte Animationen/Effekte zu wählen

## Verfügbare Presets

| Branche | Preset-Datei | Animations-Level |
|---------|--------------|------------------|
| **Steuerberater** | `presets/steuerberater.md` | Dezent |
| **Rechtsanwalt** | `presets/rechtsanwalt.md` | Dezent |
| **Arzt/Praxis** | `presets/arzt.md` | Ruhig |
| **Restaurant** | `presets/restaurant.md` | Moderat |
| **Handwerk** | `presets/handwerk.md` | Minimal |
| **Tech/Startup** | `presets/tech.md` | Expressiv |
| **Immobilien** | `presets/immobilien.md` | Moderat |

## Preset-Struktur

Jedes Preset definiert:

```yaml
hero:
  layout: centered | asymmetric | parallax
  background: gradient | image | video
  unique_element: true | false

animations:
  level: dezent | ruhig | moderat | expressiv
  hero: keine | fade | slide-up
  sections: fade-in | slide-up | none

text_effects:
  allowed: [liste der erlaubten effekte]
  forbidden: [liste der verbotenen effekte]

colors:
  mood: professional | warm | modern | creative
  saturation: low | medium | high

ux:
  cta_style: subtle | prominent
  trust_signals: wichtig | optional
  testimonials: prominent | dezent | keine
```

## Verwendung im Website-Builder

```
1. Branche identifizieren
2. Read(".claude/skills/industry-presets/presets/[branche].md")
3. Preset-Vorgaben befolgen
4. KEINE Abweichungen ohne explizite User-Anfrage
```

## Preset hinzufügen

Neue Presets in `presets/[branche].md` anlegen mit vollständiger Struktur.
