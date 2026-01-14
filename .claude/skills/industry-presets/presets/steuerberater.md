# Steuerberater Preset

Branche: Steuerberater, Wirtschaftsprüfer, Buchhalter

> **Implementierung:** Siehe `scroll-text-animations` Skill für CSS/JS Code

---

## Intro-Animation (Premium)

Logo-Maske Animation wie bei GKK Partners. Zeigt Video im Hintergrund durch Logo-Ausschnitt.

### Struktur

```
1. Intro-Mask (fixed) → Logo als Ausschnitt in grauer Fläche
2. Video-Section (fixed) → Video/Gradient im Hintergrund
3. Hero-Section → "GEMEINSAM ZUKUNFT GESTALTEN" Text über Video
4. Main-Content → Weißer Content schiebt sich drüber
```

### HTML-Struktur

```html
<!-- Video Background -->
<section id="video-section">
  <video autoplay loop muted playsinline>
    <source src="video.mp4" type="video/mp4">
  </video>
  <div class="video-fallback"></div>
</section>

<!-- Logo Mask Overlay -->
<div id="intro-mask">
  <svg viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
    <defs>
      <mask id="logoRevealMask">
        <rect width="100%" height="100%" fill="white"/>
        <g id="logo-cutout" transform="translate(660, 340) scale(1.2)">
          <!-- FIRMENLOGO PFADE HIER (black = transparent) -->
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

<!-- Hero Section -->
<section id="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">
      <span>GEMEINSAM</span>
      <span>ZUKUNFT</span>
      <span>GESTALTEN</span>
    </h1>
  </div>
  <div class="hero-badge"><!-- Nr.1 Badge SVG --></div>
  <div class="hero-scroll-arrow" id="heroScrollArrow"><!-- Arrow SVG --></div>
</section>

<!-- Main Content -->
<main id="main-content">
  <!-- Normaler Content hier -->
</main>
```

### CSS

```css
/* Video Background */
#video-section {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  z-index: 1;
  overflow: hidden;
}

#video-section video {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  min-width: 100%; min-height: 100%;
  object-fit: cover;
}

.video-fallback {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  width: 100vw; height: 100vh;
}

/* Intro Mask */
#intro-mask {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  z-index: 9998;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

#intro-mask svg { width: 100%; height: 100%; }
#intro-mask.fade-out { opacity: 0; }

#logo-cutout {
  transform-origin: center center;
  transform-box: fill-box;
}

/* Hero Section */
#hero-section {
  position: relative;
  height: 100vh;
  margin-top: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
  pointer-events: none;
}

.hero-title {
  font-size: clamp(40px, 8vw, 100px);
  font-weight: 300;
  color: white;
  text-shadow: 0 2px 20px rgba(0,0,0,0.3);
  line-height: 1.1;
  letter-spacing: 0.05em;
  text-align: center;
}

.hero-title span { display: block; }

.hero-badge {
  position: absolute;
  left: 40px; bottom: 100px;
  width: 100px; height: 100px;
  z-index: 10;
}

.hero-scroll-arrow {
  position: absolute;
  right: 40px; bottom: 100px;
  width: 40px; height: 60px;
  animation: arrowBounce 1.5s infinite;
  cursor: pointer;
  pointer-events: auto;
}

@keyframes arrowBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(10px); }
}

/* Main Content */
#main-content {
  position: relative;
  z-index: 10;
  background: white;
}

/* Scroll Indicator */
.scroll-down {
  position: fixed;
  bottom: 40px; left: 50%;
  transform: translateX(-50%);
  z-index: 10000;
  cursor: pointer;
  animation: bounce 2s infinite;
}

.scroll-down.hidden { opacity: 0; pointer-events: none; }

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
  40% { transform: translateX(-50%) translateY(-15px); }
}
```

### JavaScript (GSAP)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<script>
gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', () => {
  const introMask = document.getElementById('intro-mask');
  const scrollDown = document.getElementById('scrollDown');
  const logoCutout = document.getElementById('logo-cutout');
  const maskRect = document.getElementById('mask-rect');

  gsap.to(logoCutout, {
    scale: 20,
    scrollTrigger: {
      trigger: '#hero-section',
      start: 'top bottom',
      end: 'top top',
      scrub: 0.5,
      onUpdate: (self) => {
        const progress = self.progress;
        if (maskRect) maskRect.style.opacity = 1 - progress;
        scrollDown.classList.toggle('hidden', progress > 0.1);
        introMask.classList.toggle('fade-out', progress > 0.95);
      }
    }
  });

  scrollDown.addEventListener('click', () => {
    window.scrollTo({ top: window.innerHeight, behavior: 'smooth' });
  });

  document.getElementById('heroScrollArrow')?.addEventListener('click', () => {
    document.getElementById('main-content')?.scrollIntoView({ behavior: 'smooth' });
  });
});
</script>
```

### Beispiel-Referenz

Vollständige Implementation: `docs/gkkpartners/index.html`

---

## Hero (Standard)

```yaml
layout: centered
background: gradient (Primary → darker shade)
height: 100dvh
unique_element: false
```

| Element | Animation |
|---------|-----------|
| Headline | Statisch |
| Subline | fade-in (0.5s delay) |
| CTA | fade-in (0.8s delay) |

**VERBOTEN:** letter-reveal, Animierte SVGs, Parallax, Floating elements

---

## Text-Effekte

### Erlaubt (min. 3 verwenden)

| Effekt | Einsatz |
|--------|---------|
| `underline-scroll` | Headlines |
| `blur-reveal` | Section-Überschriften |
| `stagger-list` | Service-Cards |
| `counter` | Statistiken |
| `fade` | Paragraphen |

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
