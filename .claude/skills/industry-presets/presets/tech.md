# Tech/Startup Preset

Branche: IT-Unternehmen, Startups, Software, Agenturen, SaaS

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Hero

```yaml
layout: asymmetric oder centered
background: gradient (modern, mutig)
height: 100dvh
unique_element: true (animierte SVGs, 3D)
```

| Element | Animation |
|---------|-----------|
| Headline | letter-reveal ODER gradient-reveal |
| Subline | fade-in (0.3s delay) |
| CTA | slide-up (0.5s delay) |
| Hero-Grafik | Animiertes SVG, Parallax |

**ERLAUBT:** letter-reveal, Animierte SVGs, Parallax, Gradient-Animationen, 3D-Effekte, Floating Elements

---

## Text-Effekte

### Erlaubt (ALLE!)

| Effekt | Einsatz |
|--------|---------|
| `letter-reveal` | Hero-Headline |
| `gradient-reveal` | Feature-Headlines |
| `underline-scroll` | Wichtige Begriffe |
| `blur-reveal` | Section-Überschriften |
| `stagger-list` | Feature-Cards, Team |
| `counter` | Metrics, Stats |
| `typewriter` | Code-Beispiele |
| `split-lines` | Große Statements |

---

## Animationen

```yaml
level: expressiv
duration: 0.4s - 0.8s
timing: cubic-bezier (snappy)
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Electric Blue (#3b82f6), Purple (#8b5cf6) |
| Secondary | Cyan (#06b6d4), Pink (#ec4899) |
| Accent | Neon-Akzente, Gradients |
| Background | Dunkel (#0f172a) ODER Hell (#ffffff) |
| Text | Kontrast zum Background |

**Gradients erlaubt:** `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

---

## Typography

- **Headings:** Modern, geometric Sans-Serif
- **Body:** Clean Sans-Serif
- **Code:** Monospace (JetBrains Mono)
- Empfohlen: Inter, Space Grotesk

---

## UX

```yaml
cta_style: prominent, auffällig
trust_signals: modern (Logos, Metrics)
testimonials: prominent mit Foto
```

### Trust-Elemente

- Kunden-Logos
- "Trusted by X+ companies"
- GitHub Stars
- Metrics (Users, Revenue)
- Awards

### CTA-Texte

- "Get Started"
- "Start Free Trial"
- "Book a Demo"
