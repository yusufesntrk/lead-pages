# Restaurant Preset

Branche: Restaurants, Cafés, Bars, Catering, Bäckereien

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Hero

```yaml
layout: asymmetric oder fullscreen-image
background: Hochwertiges Food-Bild oder Video
height: 100dvh
unique_element: true (Parallax möglich)
```

| Element | Animation |
|---------|-----------|
| Headline | fade-in oder slide-up |
| Subline | fade-in (0.3s delay) |
| CTA | fade-in (0.6s delay) |
| Food-Bild | Parallax (optional) |

**ERLAUBT:** Parallax, Subtle Image-Zoom, Overlay-Animationen

---

## Text-Effekte

### Erlaubt (min. 4 verwenden)

| Effekt | Einsatz |
|--------|---------|
| `underline-scroll` | Menü-Kategorien |
| `blur-reveal` | Section-Headlines |
| `stagger-list` | Menü-Items, Galerie |
| `counter` | Jahre seit Eröffnung |
| `fade` | Beschreibungen |
| `gradient-reveal` | Optional bei kreativen Konzepten |

### Verboten

- typewriter

---

## Animationen

```yaml
level: moderat
duration: 0.5s - 0.8s
timing: ease-out
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Bordeaux (#8b0000), Terracotta (#e07b53) |
| Secondary | Creme (#faf5e4), Olive (#6b8e23) |
| Accent | Gold (#d4a574), Orange (#ed8936) |
| Background | Warm-weiß (#fffbf0) oder Dunkel |
| Text | Dunkelbraun (#3d2914) |

**Branchenspezifisch:** Italienisch=Rot/Grün, Asiatisch=Rot/Gold, Café=Braun/Creme

---

## Typography

- **Headings:** Charaktervoll (Script, Display)
- **Body:** Sans-Serif oder Serif
- Empfohlen: Playfair Display + Lato

---

## UX

```yaml
cta_style: einladend, warm
trust_signals: wichtig
testimonials: prominent (Google!)
```

### Trust-Elemente (PFLICHT)

- Google-Rating prominent
- Echte Food-Fotos
- Öffnungszeiten sichtbar
- Reservierungs-Option

### CTA-Texte

- "Tisch reservieren"
- "Speisekarte ansehen"
