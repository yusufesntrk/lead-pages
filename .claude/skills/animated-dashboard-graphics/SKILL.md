---
name: animated-dashboard-graphics
description: Generiert animierte Dashboard-Grafiken mit Alpine.js und CSS. Erstellt KPI-Cards mit Counter-Animation, Progress-Bars, SVG-Line-Drawing, Funnel-Visualisierungen und AI-Worker-Grafiken. Use when creating animated dashboards, KPI visualizations, progress indicators, funnel graphics, or interactive data displays.
allowed-tools: Write, Edit, Read, Glob
user-invocable: true
---

# Animated Dashboard Graphics Generator

Erstellt hochwertige, animierte Dashboard-Grafiken mit Alpine.js und CSS-Animationen.

## Schnellstart

Generiere eine animierte Dashboard-Grafik mit:
- IntersectionObserver für scroll-basierte Aktivierung
- Gestaffelte CSS-Animationen mit `--delay` Custom Properties
- Counter-Animationen (Alpine.js `x-effect`)
- SVG Line-Drawing Animationen
- Wiederholende Animation alle 6 Sekunden

## Verfügbare Grafik-Typen

### 1. KPI Dashboard (Agency Cockpit)

Zeigt KPIs mit animierten Countern, Progress-Bars und Auslastungs-Kreis.

**Features:**
- 3 KPI-Cards mit Counter-Animation
- Projekt-Fortschrittsbalken (4 Projekte)
- Auslastungs-Kreis (SVG Circle Progress)
- Kunden-Status Liste

### 2. AI Jarvis Worker Graphic

Zeigt ein AI-Brain mit verbundenen Worker-Cards.

**Features:**
- Zentrales AI-Brain mit Glow-Effekt
- Animierte SVG-Verbindungslinien
- Bewegende Dots entlang der Pfade
- Worker-Cards (Copy, Foto, CEO)
- Task-Status Cards

### 3. Tool Consolidation Funnel

Zeigt mehrere Tools die zu einem System konvergieren.

**Features:**
- Tool-Icons fallen von oben ein
- Animierte Funnel-Linien
- Konvergenz-Punkt mit Glow
- Ziel-Badge (Nexus)
- Benefits-Row mit Checkmarks

---

## Technische Anforderungen

### Dependencies

```html
<script src="https://cdn.tailwindcss.com"></script>
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
```

### Alpine.js Pattern für Scroll-Trigger

```html
<div x-data="{ visible: false }"
     x-init="
       const observer = new IntersectionObserver((entries) => {
         if (entries[0].isIntersecting) {
           observer.disconnect();
           setTimeout(() => visible = true, 200);
           setInterval(() => {
             visible = false;
             setTimeout(() => visible = true, 800);
           }, 6000);
         }
       }, { threshold: 0.1 });
       observer.observe($el);
     ">
  <!-- Animierte Inhalte hier -->
</div>
```

### Counter-Animation Pattern

```html
<div x-data="{ count: 0, counting: false }"
     x-effect="if(visible && !counting) {
       counting = true;
       count = 0;
       let interval = setInterval(() => {
         if(count < TARGET) count++;
         else clearInterval(interval);
       }, 50);
     } else if(!visible) {
       counting = false;
       count = 0;
     }">
  <span x-text="count">0</span>
</div>
```

---

## CSS Animation Classes

### Fade-In (von unten)

```css
.graphic-fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.graphic-fade-in.is-visible {
  opacity: 1;
  transform: translateY(0);
  transition-delay: var(--delay, 0ms);
}
```

### Fade-In von Links

```css
.graphic-fade-in-left {
  opacity: 0;
  transform: translateX(-12px);
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.graphic-fade-in-left.is-visible {
  opacity: 1;
  transform: translateX(0);
  transition-delay: var(--delay, 0ms);
}
```

### Fade-In von Oben (für Funnel)

```css
.funnel-fade-in-down {
  opacity: 0;
  transform: translateY(-24px);
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.funnel-fade-in-down.is-visible {
  opacity: 1;
  transform: translateY(0);
  transition-delay: var(--delay, 0ms);
}
```

### Fade-In mit Scale

```css
.fade-in-scale {
  opacity: 0;
  transform: translateY(16px) scale(0.9);
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-in-scale.is-visible {
  opacity: 1;
  transform: translateY(0) scale(1);
  transition-delay: var(--delay, 0ms);
}
```

### Progress Bar Animation

```css
.progress-bar-animate {
  width: 0%;
  transition: width 1s cubic-bezier(0.16, 1, 0.3, 1);
}

.progress-bar-animate.is-visible {
  width: var(--progress, 0%);
  transition-delay: var(--delay, 0ms);
}
```

### Circle Progress (SVG)

```css
.circle-progress-animate {
  stroke-dashoffset: 251.2; /* Umfang: 2 * PI * r (r=40) */
  transition: stroke-dashoffset 1s cubic-bezier(0.16, 1, 0.3, 1);
}

.circle-progress-animate.is-visible {
  stroke-dashoffset: var(--progress-offset, 251.2);
  transition-delay: var(--delay, 0ms);
}
```

### SVG Line Drawing

```css
.line-draw {
  stroke-dashoffset: var(--dashoffset, 200);
  transition: stroke-dashoffset 1s cubic-bezier(0.16, 1, 0.3, 1);
}

.line-draw.is-visible {
  stroke-dashoffset: 0;
  transition-delay: var(--delay, 0ms);
}
```

### Glow Effect

```css
.glow-effect {
  opacity: 0;
  transition: opacity 0.5s ease-out;
}

.glow-effect.is-visible {
  opacity: 1;
  transition-delay: 300ms;
}
```

---

## SVG Patterns

### Dotted Background Pattern

```html
<div class="absolute inset-0 opacity-30">
  <svg width="100%" height="100%">
    <defs>
      <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">
        <circle cx="1" cy="1" r="1" fill="#94a3b8"></circle>
      </pattern>
    </defs>
    <rect width="100%" height="100%" fill="url(#dots)"></rect>
  </svg>
</div>
```

### Animated Dot on Path

```html
<circle r="3" fill="#3B82F6">
  <animateMotion dur="2s" repeatCount="indefinite" path="M150 0 L150 60"></animateMotion>
</circle>
```

### Circle Progress mit Gradient

```html
<svg class="w-20 h-20 -rotate-90" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="none" stroke="#e2e8f0" stroke-width="8"></circle>
  <circle cx="50" cy="50" r="40" fill="none"
          stroke="url(#gradient)" stroke-width="8"
          stroke-linecap="round" stroke-dasharray="251.2"
          class="circle-progress-animate"
          :class="visible ? 'is-visible' : ''"
          style="--progress-offset: 32.656;"></circle>
  <defs>
    <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3B82F6"></stop>
      <stop offset="100%" stop-color="#8B5CF6"></stop>
    </linearGradient>
  </defs>
</svg>
```

---

## Delay-Strategie

Gestaffelte Delays für natürlichen Flow:

| Element-Typ | Delay-Range |
|-------------|-------------|
| Header/Title | 0-100ms |
| KPI Cards | 0-200ms (je +100ms) |
| Content Cards | 300-500ms |
| Progress Bars | 500-800ms (je +100ms) |
| Details/Status | 700-900ms |
| Final Elements | 1000-1400ms |

---

## Container-Struktur

```html
<div class="relative bg-gradient-to-br from-slate-50 to-slate-100 rounded-2xl p-4 md:p-6 overflow-hidden border border-slate-200">
  <!-- Dotted Background Pattern -->
  <div class="absolute inset-0 opacity-30">...</div>

  <!-- Content -->
  <div class="relative z-10">
    <!-- Animierte Elemente -->
  </div>
</div>
```

---

## Responsive Breakpoints

| Breakpoint | Anpassungen |
|------------|-------------|
| Mobile (default) | Kleinere Fonts, kompaktere Spacing |
| `md:` (768px+) | Größere Fonts, mehr Padding |

Beispiel:
```html
<div class="text-lg md:text-2xl">
<div class="p-2 md:p-3">
<div class="w-16 h-16 md:w-20 md:h-20">
```

---

## Farbpalette

| Verwendung | Tailwind Class |
|------------|----------------|
| Primary | `blue-500`, `blue-600` |
| Success | `emerald-500` |
| Warning | `amber-500` |
| Info | `violet-500` |
| Text | `slate-900`, `slate-700`, `slate-500` |
| Background | `slate-50`, `slate-100`, `white` |
| Border | `slate-100`, `slate-200` |

---

## Beispiel-Referenz

Vollständige Implementierung siehe:
`docs/animation-test/index.html`
