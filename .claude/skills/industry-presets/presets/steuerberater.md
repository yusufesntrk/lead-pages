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
| `logo-mask-intro` | Page Load | Logo als Maske, zoomt auf beim Scrollen |

### Verboten

- Parallax, letter-reveal
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

## Logo Mask Intro Animation

Premium Intro-Effekt: Seite startet mit Logo als "Fenster", beim Scrollen zoomt das Logo auf und gibt den Blick auf den Hero frei.

### Wann verwenden

- Hochwertige Kanzlei-Websites
- Wenn ein starkes Logo vorhanden ist
- Als Premium-Feature für Unterscheidung

### Struktur

```
┌─────────────────────────────┐
│  Grauer Overlay (#e5e5e5)   │
│  ┌─────────────────────┐    │
│  │    LOGO (Loch)      │    │  ← Viewport 1: Intro
│  │  (Video/Gradient    │    │
│  │   durchscheint)     │    │
│  └─────────────────────┘    │
└─────────────────────────────┘
           ↓ Scroll
┌─────────────────────────────┐
│      HERO SECTION           │  ← Viewport 2: Hero
│   "Gemeinsam Zukunft..."    │
└─────────────────────────────┘
           ↓ Scroll
┌─────────────────────────────┐
│      MAIN CONTENT           │  ← Viewport 3+: Content
│   (weißer Hintergrund)      │
└─────────────────────────────┘
```

### HTML

```html
<!-- GSAP (im <head>) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Video/Gradient Hintergrund (fixed, z-index: 1) -->
<section id="video-section">
  <video autoplay loop muted playsinline>
    <source src="intro-video.mp4" type="video/mp4">
  </video>
  <div class="video-fallback"></div> <!-- Gradient Fallback -->
</section>

<!-- Logo Mask Overlay (fixed, z-index: 9998) -->
<div id="intro-mask">
  <svg viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
    <defs>
      <mask id="logoRevealMask">
        <rect width="100%" height="100%" fill="white"/>
        <g id="logo-cutout" transform="translate(760, 390) scale(1)">
          <!-- LOGO SVG PATHS HIER (fill="black") -->
          <!-- Schwarz = Loch/Transparent -->
        </g>
      </mask>
    </defs>
    <rect id="mask-rect" width="100%" height="100%" fill="#e5e5e5" mask="url(#logoRevealMask)"/>
  </svg>
</div>

<!-- Scroll Indicator -->
<div class="scroll-down" id="scrollDown">
  <svg viewBox="0 0 50 50" fill="none" stroke="white" stroke-width="2">
    <circle cx="25" cy="25" r="23" opacity="0.3"/>
    <path d="M25 15 L25 35 M17 27 L25 35 L33 27" stroke-linecap="round"/>
  </svg>
</div>

<!-- Hero Section (margin-top: 100vh) -->
<section id="hero-section">
  <div class="hero-content">
    <h1>HEADLINE</h1>
  </div>
</section>

<!-- Main Content (position: relative, z-index: 10, background: white) -->
<main id="main-content">
  <!-- Normale Sektionen -->
</main>
```

### CSS

```css
/* Video Background */
#video-section {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1;
  overflow: hidden;
}

#video-section video {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%;
  min-height: 100%;
  object-fit: cover;
}

.video-fallback {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
}

/* Logo Mask Overlay */
#intro-mask {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 9998;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

#intro-mask svg {
  width: 100%;
  height: 100%;
}

#intro-mask.fade-out {
  opacity: 0;
}

#logo-cutout {
  transform-origin: center center;
  transform-box: fill-box;
}

/* Scroll Indicator */
.scroll-down {
  position: fixed;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10000;
  cursor: pointer;
  animation: bounce 2s infinite;
}

.scroll-down svg {
  width: 50px;
  height: 50px;
  filter: drop-shadow(0 2px 8px rgba(0,0,0,0.3));
}

.scroll-down.hidden {
  opacity: 0;
  pointer-events: none;
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
  40% { transform: translateX(-50%) translateY(-15px); }
  60% { transform: translateX(-50%) translateY(-7px); }
}

/* Hero Section */
#hero-section {
  position: relative;
  height: 100vh;
  margin-top: 100vh; /* WICHTIG: Schiebt Hero unter Intro */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
}

/* Main Content */
#main-content {
  position: relative;
  z-index: 10;
  background: white;
}
```

### JavaScript

```javascript
gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', () => {
  const introMask = document.getElementById('intro-mask');
  const scrollDown = document.getElementById('scrollDown');
  const logoCutout = document.getElementById('logo-cutout');
  const maskRect = document.getElementById('mask-rect');

  // Logo zoom Animation beim Scrollen
  gsap.to(logoCutout, {
    scale: 20,
    scrollTrigger: {
      trigger: '#hero-section',
      start: 'top bottom',
      end: 'top top',
      scrub: 0.5,
      onUpdate: (self) => {
        const progress = self.progress;

        // Grauer Overlay ausblenden
        if (maskRect) {
          maskRect.style.opacity = 1 - progress;
        }

        // Scroll-Indicator verstecken
        if (progress > 0.1) {
          scrollDown.classList.add('hidden');
        } else {
          scrollDown.classList.remove('hidden');
        }

        // Intro-Mask komplett ausblenden wenn fertig
        if (progress > 0.95) {
          introMask.classList.add('fade-out');
        } else {
          introMask.classList.remove('fade-out');
        }
      }
    }
  });

  // Click auf Scroll-Indicator
  scrollDown.addEventListener('click', () => {
    window.scrollTo({
      top: window.innerHeight,
      behavior: 'smooth'
    });
  });
});
```

### Logo SVG vorbereiten

Das Logo muss als SVG-Pfade in die Maske eingefügt werden:

1. Logo SVG öffnen
2. Alle `<path>` Elemente kopieren
3. `fill="black"` setzen (schwarz = transparent/Loch)
4. In `#logo-cutout` einfügen
5. `transform="translate(X, Y) scale(S)"` anpassen für Zentrierung

```svg
<!-- Beispiel: Logo zentrieren in 1920x1080 -->
<g id="logo-cutout" transform="translate(760, 390) scale(1.2)">
  <path fill="black" d="M..."/> <!-- Logo Pfad 1 -->
  <path fill="black" d="M..."/> <!-- Logo Pfad 2 -->
</g>
```

### Ohne Video (nur Gradient)

Falls kein Video vorhanden, einfach `<video>` weglassen - der `.video-fallback` Gradient wird angezeigt.

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
