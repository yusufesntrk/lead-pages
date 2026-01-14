# Steuerberater Preset

Branche: Steuerberater, Wirtschaftsprüfer, Buchhalter

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Animationen

```yaml
level: minimal
duration: 0.6s - 0.8s
timing: ease-out
```

### Erlaubte Animationen

| Animation | Wo | Beschreibung |
|-----------|-----|--------------|
| `fade-in` | Hero | Headline, Subline, CTA faden ein |
| `underline-scroll` | Überschriften | Linie erscheint beim Scrollen |
| `blur-reveal` | Section-Überschriften | Text wird scharf beim Scrollen |
| `stagger-list` | Service-Cards, Listen | Elemente erscheinen nacheinander |
| `counter` | Statistiken | Zahlen zählen hoch |

### Verboten

- Logo-Maske, Parallax, letter-reveal
- Floating elements, Animierte SVGs
- Alles andere nicht explizit erlaubte

---

## Navbar

```yaml
style: compact
background: white (transparent on dark hero optional)
height: auto (padding-based)
logo_height: 36px
```

### CSS

```css
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: var(--color-bg);
  z-index: 1000;
  /* KEINE feste height! */
}

.header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0; /* Kompakt durch Padding statt height */
}

.logo img {
  height: 36px;
  width: auto;
}

.nav {
  display: flex;
  align-items: center;
  gap: 2rem; /* Abstand Nav zu Button */
}

.nav__list {
  display: flex;
  align-items: center;
  gap: 1.5rem; /* Abstand zwischen Links */
}
```

### Wichtig

- **KEINE** feste `height` auf `.header`
- Padding `1rem 0` auf `.header__inner` für kompakten Look
- Logo max. `36px` Höhe
- Nav-Link Abstände: `1.5rem`
- Abstand Nav zu CTA-Button: `2rem`

---

## Hero

```yaml
layout: centered
background: gradient (Primary → darker shade)
height: 100dvh
```

| Element | Animation |
|---------|-----------|
| Headline | fade-in |
| Subline | fade-in (0.3s delay) |
| CTA | fade-in (0.5s delay) |

### CSS

```css
.hero-content {
  opacity: 0;
  animation: fadeIn 0.8s ease-out forwards;
}

.hero-content .subline {
  animation-delay: 0.3s;
}

.hero-content .cta {
  animation-delay: 0.5s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## Underline-Scroll für Überschriften

Überschriften bekommen beim Scrollen eine animierte Unterstreichung.

### HTML

```html
<h2 class="underline-scroll">Unsere Leistungen</h2>
```

### CSS

```css
.underline-scroll {
  position: relative;
  display: inline-block;
}

.underline-scroll::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 3px;
  background: var(--primary-color);
  transition: width 0.6s ease-out;
}

.underline-scroll.visible::after {
  width: 100%;
}
```

### JavaScript

```javascript
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.underline-scroll').forEach(el => {
    observer.observe(el);
  });
});
```

---

## Farben

| Rolle | Wert |
|-------|------|
| Primary | Dunkelblau (#1a365d) |
| Secondary | Grau (#718096) |
| Accent | Gold (#b8860b) oder Grün (#2f855a) |
| Background | Weiß, helles Grau (#f7fafc) |
| Text | Dunkelgrau (#2d3748) |

---

## Typography

- **Headings:** Serif oder elegante Sans-Serif
- **Body:** Clean Sans-Serif
- Empfohlen: Playfair Display + Source Sans Pro

---

## UX

```yaml
cta_style: subtle-prominent
trust_signals: SEHR WICHTIG
testimonials: prominent
```

### Trust-Elemente (PFLICHT)

- "Seit [Jahr] in [Stadt]"
- Steuerberaterkammer-Badge
- Google-Rating (wenn 4.5+)
- Qualifikationen

### CTA-Texte

- "Beratungstermin vereinbaren"
- "Kostenlose Erstberatung"

**NICHT:** "Jetzt loslegen!", Emojis
