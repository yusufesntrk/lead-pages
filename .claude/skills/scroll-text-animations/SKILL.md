---
name: scroll-text-animations
description: Scroll-triggered text animations for real website sections. Use when adding text reveal effects, underline animations, word-by-word reveals, counters, or staggered list animations to websites.
---

# Scroll-Triggered Text Animations

Praktische Text-Animationen für echte Website-Sektionen. Alle Effekte werden durch `IntersectionObserver` beim Scrollen ausgelöst.

## Übersicht der Effekte

| Effekt | Klasse | Beschreibung |
|--------|--------|--------------|
| Underline | `.underline-scroll` | Unterstreichung wächst von links |
| Highlight | `.highlight-scroll` | Marker-Hervorhebung von links |
| Word-by-Word | `.word-reveal` | Wörter erscheinen nacheinander |
| Letter-by-Letter | `.letter-reveal` | Buchstaben einzeln einblenden |
| Gradient Reveal | `.gradient-reveal` | Farbverlauf füllt Text |
| Split Lines | `.split-lines` | Zeilen von links/rechts |
| Blur → Sharp | `.blur-reveal` | Unscharf zu scharf |
| Scale Up | `.scale-reveal` | Klein zu groß |
| Counter | `.counter` | Zahlen hochzählen |
| Clip Reveal | `.clip-reveal` | Von links aufdecken |
| Staggered List | `.stagger-list` | Listeneinträge nacheinander |
| Typewriter | `.typewriter-scroll` | Schreibmaschinen-Effekt |

---

## HTML-Struktur

### 1. Underline Animation

```html
<h2>Wir entwickeln<br>
    <span class="underline-scroll" data-scroll>RuleBreaker Systeme</span>
</h2>
```

### 2. Highlight/Marker

```html
<h2>Wir sind <span class="highlight-scroll" data-scroll>Digitalarchitekten</span>.</h2>
```

### 3. Word-by-Word Reveal

```html
<h2 class="word-reveal" data-scroll data-words>
    Technologie sollte Menschen verbinden, nicht trennen.
</h2>
```

### 4. Letter-by-Letter

```html
<span class="letter-reveal" data-scroll data-letters>INNOVATION</span>
```

### 5. Counter Animation

```html
<div class="stat">
    <span class="counter" data-target="150" data-scroll>0</span>
    <span class="stat-suffix">+</span>
    <span class="stat-label">Projekte</span>
</div>
```

### 6. Staggered List

```html
<ul class="stagger-list" data-scroll data-stagger>
    <li><strong>Webentwicklung</strong> — Moderne, schnelle Websites</li>
    <li><strong>App Development</strong> — Native & Cross-Platform</li>
    <li><strong>Cloud Solutions</strong> — Skalierbare Infrastruktur</li>
</ul>
```

### 7. Cards mit Stagger

```html
<div class="team-grid" data-scroll data-stagger>
    <div class="team-card">
        <div class="team-avatar">MK</div>
        <h4>Max Krause</h4>
        <p>CEO & Founder</p>
    </div>
    <!-- weitere cards -->
</div>
```

---

## CSS

```css
/* ========================================
   BASE STYLES
   ======================================== */

[data-scroll] {
    opacity: 0;
    transition: opacity 0.6s ease, transform 0.6s ease;
}

[data-scroll].visible {
    opacity: 1;
}

/* ========================================
   UNDERLINE ANIMATION
   ======================================== */

.underline-scroll {
    position: relative;
    display: inline;
}

.underline-scroll::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transition: width 0.8s cubic-bezier(0.65, 0, 0.35, 1);
}

.underline-scroll.visible::after {
    width: 100%;
}

/* ========================================
   HIGHLIGHT/MARKER
   ======================================== */

.highlight-scroll {
    position: relative;
    display: inline;
}

.highlight-scroll::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: -4px;
    right: -4px;
    height: 40%;
    background: rgba(102, 126, 234, 0.3);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.6s cubic-bezier(0.65, 0, 0.35, 1);
    z-index: -1;
}

.highlight-scroll.visible::before {
    transform: scaleX(1);
}

/* ========================================
   WORD-BY-WORD REVEAL
   ======================================== */

.word-reveal .word {
    display: inline-block;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.5s ease, transform 0.5s ease;
}

.word-reveal.visible .word {
    opacity: 1;
    transform: translateY(0);
}

/* Stagger delay wird per JS gesetzt */

/* ========================================
   LETTER-BY-LETTER
   ======================================== */

.letter-reveal .letter {
    display: inline-block;
    opacity: 0;
    transform: translateY(30px) rotateX(-90deg);
    transition: opacity 0.4s ease, transform 0.4s ease;
}

.letter-reveal.visible .letter {
    opacity: 1;
    transform: translateY(0) rotateX(0);
}

/* ========================================
   GRADIENT REVEAL
   ======================================== */

.gradient-reveal {
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    background-size: 200% 100%;
    background-position: 100% 0;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    transition: background-position 1.5s ease;
}

.gradient-reveal.visible {
    background-position: 0 0;
}

/* ========================================
   SPLIT LINES
   ======================================== */

.split-lines .line {
    display: block;
    opacity: 0;
    transition: opacity 0.6s ease, transform 0.6s ease;
}

.split-lines .line:nth-child(odd) {
    transform: translateX(-50px);
}

.split-lines .line:nth-child(even) {
    transform: translateX(50px);
}

.split-lines.visible .line {
    opacity: 1;
    transform: translateX(0);
}

/* ========================================
   BLUR REVEAL
   ======================================== */

.blur-reveal {
    filter: blur(10px);
    opacity: 0.3;
    transition: filter 0.8s ease, opacity 0.8s ease;
}

.blur-reveal.visible {
    filter: blur(0);
    opacity: 1;
}

/* ========================================
   SCALE REVEAL
   ======================================== */

.scale-reveal {
    transform: scale(0.5);
    opacity: 0;
    transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.6s ease;
}

.scale-reveal.visible {
    transform: scale(1);
    opacity: 1;
}

/* ========================================
   CLIP REVEAL
   ======================================== */

.clip-reveal {
    clip-path: inset(0 100% 0 0);
    transition: clip-path 1s cubic-bezier(0.65, 0, 0.35, 1);
}

.clip-reveal.visible {
    clip-path: inset(0 0 0 0);
}

/* ========================================
   COUNTER
   ======================================== */

.counter {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ========================================
   STAGGERED LIST
   ======================================== */

.stagger-list li,
[data-stagger] > * {
    opacity: 0;
    transform: translateX(-30px);
    transition: opacity 0.5s ease, transform 0.5s ease;
}

.stagger-list.visible li,
[data-stagger].visible > * {
    opacity: 1;
    transform: translateX(0);
}

/* ========================================
   TYPEWRITER
   ======================================== */

.typewriter-scroll {
    overflow: hidden;
    white-space: nowrap;
    width: 0;
    transition: none;
}

.typewriter-scroll.visible {
    animation: typewrite 2s steps(30) forwards;
}

@keyframes typewrite {
    to { width: 100%; }
}

.typewriter-cursor {
    display: inline-block;
    animation: blink 0.8s infinite;
}

@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}
```

---

## JavaScript

```javascript
document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initWordReveal();
    initLetterReveal();
    initCounters();
    initStagger();
});

/**
 * Base Scroll Animation mit IntersectionObserver
 */
function initScrollAnimations() {
    const elements = document.querySelectorAll('[data-scroll]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(el => observer.observe(el));
}

/**
 * Word-by-Word Reveal
 * Wraps each word in a span with staggered delay
 */
function initWordReveal() {
    document.querySelectorAll('[data-words]').forEach(el => {
        const text = el.textContent.trim();
        const words = text.split(/\s+/);

        el.innerHTML = words.map((word, i) =>
            `<span class="word" style="transition-delay: ${i * 0.1}s">${word}</span>`
        ).join(' ');
    });
}

/**
 * Letter-by-Letter Reveal
 * Wraps each letter in a span with staggered delay
 */
function initLetterReveal() {
    document.querySelectorAll('[data-letters]').forEach(el => {
        const text = el.textContent.trim();

        el.innerHTML = text.split('').map((char, i) =>
            `<span class="letter" style="transition-delay: ${i * 0.05}s">${char}</span>`
        ).join('');
    });
}

/**
 * Counter Animation
 * Counts up from 0 to data-target value
 */
function initCounters() {
    const counters = document.querySelectorAll('.counter[data-target]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.dataset.target);
                animateCounter(counter, target);
                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
}

function animateCounter(element, target) {
    const duration = 2000;
    const start = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - start;
        const progress = Math.min(elapsed / duration, 1);

        // Easing: easeOutExpo
        const eased = 1 - Math.pow(2, -10 * progress);
        const current = Math.floor(eased * target);

        element.textContent = current;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = target;
        }
    }

    requestAnimationFrame(update);
}

/**
 * Staggered Children Animation
 * Adds delay to each child element
 */
function initStagger() {
    document.querySelectorAll('[data-stagger]').forEach(container => {
        const children = container.children;
        Array.from(children).forEach((child, i) => {
            child.style.transitionDelay = `${i * 0.1}s`;
        });
    });
}
```

---

## Anwendungsbeispiele

### Hero-Sektion mit Underline

```html
<section class="hero">
    <div class="hero-content">
        <h1>Wir entwickeln<br>
            <span class="underline-scroll" data-scroll>RuleBreaker Systeme</span>
        </h1>
        <p class="hero-sub" data-scroll style="transition-delay: 0.3s">
            Digitale Lösungen, die Grenzen sprengen.
        </p>
    </div>
</section>
```

### Statistik-Sektion mit Counter

```html
<section class="stats">
    <div class="stats-grid">
        <div class="stat" data-scroll>
            <span class="counter" data-target="150" data-scroll>0</span>
            <span class="stat-suffix">+</span>
            <span class="stat-label">Projekte</span>
        </div>
        <div class="stat" data-scroll style="transition-delay: 0.2s">
            <span class="counter" data-target="98" data-scroll>0</span>
            <span class="stat-suffix">%</span>
            <span class="stat-label">Kundenzufriedenheit</span>
        </div>
        <div class="stat" data-scroll style="transition-delay: 0.4s">
            <span class="counter" data-target="24" data-scroll>0</span>
            <span class="stat-suffix">/7</span>
            <span class="stat-label">Support</span>
        </div>
    </div>
</section>
```

### Leistungen mit Staggered List

```html
<section class="services">
    <h2 class="highlight-scroll" data-scroll>Unsere Leistungen</h2>
    <ul class="stagger-list" data-scroll data-stagger>
        <li><strong>Webentwicklung</strong> — Moderne, schnelle Websites</li>
        <li><strong>App Development</strong> — Native & Cross-Platform</li>
        <li><strong>Cloud Solutions</strong> — Skalierbare Infrastruktur</li>
        <li><strong>UI/UX Design</strong> — Nutzerzentrierte Gestaltung</li>
    </ul>
</section>
```

---

## Branchenspezifische Anwendung

| Branche | Empfohlene Effekte |
|---------|-------------------|
| **Rechtsanwalt/Steuerberater** | Underline, Blur-Reveal, Stagger (dezent) |
| **Tech/Startup** | Letter-by-Letter, Gradient-Reveal, Counter |
| **Kreativagentur** | Word-by-Word, Split-Lines, Scale-Reveal |
| **Restaurant/Café** | Highlight, Clip-Reveal, Typewriter |
| **Handwerk** | Underline, Stagger-List (minimal) |
| **Arzt/Gesundheit** | Blur-Reveal, Fade (sehr sanft) |

---

## Performance-Tipps

1. **IntersectionObserver** statt scroll-Event (besser für Performance)
2. **will-change** sparsam einsetzen
3. **transform/opacity** bevorzugen (GPU-beschleunigt)
4. **Unobserve** nach Animation für Counter/Einmal-Effekte
5. **Threshold anpassen** je nach Viewport-Größe

```javascript
// Mobile: Früher triggern
const threshold = window.innerWidth < 768 ? 0.1 : 0.2;
```

---

## Live-Demo

Siehe: `docs/parallax-showcase/text-sections.html`
