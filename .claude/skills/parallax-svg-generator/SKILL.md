---
name: parallax-svg-generator
description: Generiert detaillierte SVG-Grafiken für Parallax-Items mit radialen Gradienten, SVG-Filtern (feDropShadow, feGaussianBlur), Lichtreflexen und SVG-Animationen. Nutze diesen Skill wenn der User SVG-Code für Parallax-Effekte, Food-Items, realistische Grafiken oder animierte SVG-Elemente benötigt.
allowed-tools: Read, Write, Edit
---

# Parallax SVG Generator

Generiert hochwertige SVG-Grafiken für detaillierte Parallax-Items mit realistischen Effekten - wie Food-Items (Tomaten, Gurken, Salat, etc.).

## Instructions

### 1. Kontext erfassen

Frage ZUERST (falls unklar):
- **Element-Typ**: Welches Item? (z.B. Tomate, Gurke, Salat, Tropfen, etc.)
- **Farbpalette**: Welche Hauptfarbe(n)? (z.B. "Rot für Tomate", "Grün für Salat")
- **Größe**: ViewBox-Größe? (Standard: 120x120)
- **Position**: Links oder rechts? (für unique IDs)

### 2. SVG-Struktur generieren

Nutze diese Basis-Struktur für JEDES Item:

```html
<svg viewBox="0 0 120 120" class="ingredient-svg [name]-svg">
    <defs>
        <!-- Radial Gradient für Hauptelement (4-6 Stops) -->
        <radialGradient id="[name]-[side]" cx="35%" cy="35%" r="65%">
            <stop offset="0%" stop-color="[COLOR_LIGHT]" />
            <stop offset="30%" stop-color="[COLOR_MID_LIGHT]" />
            <stop offset="70%" stop-color="[COLOR_MID_DARK]" />
            <stop offset="100%" stop-color="[COLOR_DARK]" />
        </radialGradient>

        <!-- Filter: Glow-Effekt -->
        <filter id="[name]Glow-[side]" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="2" result="blur" />
            <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>

        <!-- Filter: Drop Shadow -->
        <filter id="[name]Shadow-[side]" x="-50%" y="-50%" width="200%" height="200%">
            <feDropShadow dx="2" dy="4" stdDeviation="3"
                          flood-color="[SHADOW_COLOR]" flood-opacity="0.5" />
        </filter>
    </defs>

    <!-- Hauptelement mit Filter -->
    <g filter="url(#[name]Shadow-[side])">
        <ellipse cx="60" cy="60" rx="45" ry="42" fill="url(#[name]-[side])">
            <!-- Pulsierende Animation -->
            <animate attributeName="ry" values="42; 44; 42" dur="3s" repeatCount="indefinite" />
        </ellipse>

        <!-- Lichtreflexe (2-3 Ellipsen) -->
        <ellipse cx="48" cy="48" rx="16" ry="10" fill="#ffffff" opacity="0.35"
                 transform="rotate(-20 48 48)">
            <animate attributeName="opacity" values="0.35; 0.5; 0.35"
                     dur="2.5s" repeatCount="indefinite" />
        </ellipse>
        <ellipse cx="52" cy="52" rx="8" ry="5" fill="#ffffff" opacity="0.5"
                 transform="rotate(-20 52 52)" />

        <!-- Kleine Lichtpunkte -->
        <circle cx="42" cy="55" r="3" fill="#ffffff" opacity="0.25" />
        <circle cx="70" cy="50" r="2" fill="#ffffff" opacity="0.2" />
    </g>
</svg>
```

### 3. Radiale SVG-Gradienten (PFLICHT)

**IMMER mindestens 4 stop-Elemente verwenden** für realistische Tiefe:

**Beispiel: Tomaten-Rot**
```html
<radialGradient id="tomato-left" cx="35%" cy="35%" r="65%">
    <stop offset="0%" stop-color="#fca5a5" />   <!-- Hell (Lichtpunkt) -->
    <stop offset="30%" stop-color="#f87171" />  <!-- Heller Mittelpunkt -->
    <stop offset="70%" stop-color="#ef4444" />  <!-- Mittlerer Ton -->
    <stop offset="100%" stop-color="#b91c1c" /> <!-- Dunkelster (Schatten) -->
</radialGradient>
```

**Wichtig:**
- **cx/cy:** Lichtquelle (meist 30-40%)
- **r:** Radius (meist 60-70%)
- **offset:** Farbverteilung (0%, 30%, 70%, 100%)

**Farbpaletten-Guide:**
- **Rot/Orange**: #fca5a5 → #f87171 → #ef4444 → #dc2626 → #b91c1c
- **Grün (Salat)**: #86efac → #66BB6A → #4ade80 → #4CAF50 → #22c55e
- **Grün (Gurke)**: #d1fae5 → #a7f3d0 → #6ee7b7 → #34d399 → #10b981
- **Gelb (Sauce)**: #fef9c3 → #fef08a → #fde047 → #facc15 → #eab308
- **Braun (Fleisch)**: #d4a574 → #bc8a5f → #a67c52 → #8b6f47 → #6d4c41
- **Lila (Zwiebel)**: #f5f3ff → #ede9fe → #ddd6fe → #c4b5fd → #a78bfa
- **Orange (Paprika)**: #fed7aa → #fdba74 → #fb923c → #f97316 → #ea580c

### 4. Lichtreflexe mit SVG-Ellipsen (PFLICHT)

**IMMER 2-3 Lichtreflex-Ellipsen hinzufügen:**

```html
<!-- Hauptreflex (groß, animiert) -->
<ellipse cx="48" cy="48" rx="16" ry="10" fill="#ffffff" opacity="0.35"
         transform="rotate(-20 48 48)">
    <animate attributeName="opacity" values="0.35; 0.5; 0.35"
             dur="2.5s" repeatCount="indefinite" />
</ellipse>

<!-- Sekundärer Reflex (klein, statisch) -->
<ellipse cx="52" cy="52" rx="8" ry="5" fill="#ffffff" opacity="0.5"
         transform="rotate(-20 52 52)" />

<!-- Kleine Lichtpunkte (optional) -->
<circle cx="42" cy="55" r="3" fill="#ffffff" opacity="0.25" />
<circle cx="70" cy="50" r="2" fill="#ffffff" opacity="0.2" />
```

**Positionierung:**
- Hauptreflex: 35-45% von links, 35-45% von oben
- Rotation: -15° bis -25° für natürlichen Look
- Opacity: 0.3-0.5 für subtilen Effekt

### 5. SVG-Filter für Schatten (PFLICHT)

**IMMER feDropShadow-Filter verwenden:**

```html
<defs>
    <filter id="[name]Shadow-[side]" x="-50%" y="-50%" width="200%" height="200%">
        <feDropShadow dx="2" dy="4" stdDeviation="3"
                      flood-color="#7f1d1d" flood-opacity="0.5" />
    </filter>
</defs>

<g filter="url(#[name]Shadow-[side])">
    <!-- Element hier -->
</g>
```

**Parameter:**
- **dx/dy:** Schatten-Offset (meist dx="2" dy="4")
- **stdDeviation:** Unschärfe (2-4 für weichen Schatten)
- **flood-color:** Dunklere Version der Hauptfarbe
- **flood-opacity:** 0.4-0.6 je nach Tiefe

**Optional: Glow-Effekt**

```html
<filter id="[name]Glow-[side]" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="2" result="blur" />
    <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
    </feMerge>
</filter>
```

### 6. SVG-Animationen hinzufügen (PFLICHT)

**Pulsieren (Standard für organische Elemente):**

```html
<ellipse cx="60" cy="60" rx="45" ry="42" fill="url(#tomato-left)">
    <animate attributeName="ry" values="42; 44; 42" dur="3s" repeatCount="indefinite" />
</ellipse>
```

**Glow-Animation (für Lichtreflexe):**

```html
<ellipse cx="48" cy="48" rx="16" ry="10" fill="#ffffff" opacity="0.35">
    <animate attributeName="opacity" values="0.35; 0.5; 0.35"
             dur="2.5s" repeatCount="indefinite" />
</ellipse>
```

**Rotation (für schwebende Elemente):**

```html
<g transform="rotate(0 60 60)">
    <animateTransform
        attributeName="transform"
        type="rotate"
        values="0 60 60; 5 60 60; 0 60 60"
        dur="4s"
        repeatCount="indefinite" />
    <!-- Element hier -->
</g>
```

**Float-Animation (für Tropfen):**

```html
<ellipse cx="60" cy="60" rx="20" ry="30" fill="url(#water-drop)">
    <animate attributeName="cy" values="60; 55; 60" dur="2.5s" repeatCount="indefinite" />
</ellipse>
```

### 7. Unique IDs für Symmetrie (WICHTIG!)

**Für Links/Rechts IMMER unterschiedliche IDs verwenden:**

```html
<!-- Links -->
<svg viewBox="0 0 120 120">
    <defs>
        <radialGradient id="tomato-left" cx="35%" cy="35%" r="65%">
            <!-- Gradient-Stops -->
        </radialGradient>
        <filter id="tomatoShadow-left">
            <!-- Filter-Definition -->
        </filter>
    </defs>
    <ellipse fill="url(#tomato-left)" filter="url(#tomatoShadow-left)" />
</svg>

<!-- Rechts -->
<svg viewBox="0 0 120 120">
    <defs>
        <radialGradient id="tomato-right" cx="35%" cy="35%" r="65%">
            <!-- Identische Gradient-Stops -->
        </radialGradient>
        <filter id="tomatoShadow-right">
            <!-- Identische Filter-Definition -->
        </filter>
    </defs>
    <ellipse fill="url(#tomato-right)" filter="url(#tomatoShadow-right)" />
</svg>
```

**Warum?** IDs müssen im gesamten HTML unique sein. `-left` und `-right` Suffix vermeidet Konflikte.

## Output-Format

Generiere IMMER vollständigen SVG-Code mit diesem Format:

```html
<!-- Layer [NUMBER]: [ELEMENT NAME] ([SPEED]x) -->
<div class="parallax-item parallax-item-left" data-speed="[SPEED]" data-layer="[NUMBER]">
    <svg viewBox="0 0 120 120" class="ingredient-svg [name]-svg">
        <defs>
            <!-- Radial Gradient -->
            <radialGradient id="[name]-left" cx="35%" cy="35%" r="65%">
                <stop offset="0%" stop-color="[COLOR_1]" />
                <stop offset="30%" stop-color="[COLOR_2]" />
                <stop offset="70%" stop-color="[COLOR_3]" />
                <stop offset="100%" stop-color="[COLOR_4]" />
            </radialGradient>

            <!-- Shadow Filter -->
            <filter id="[name]Shadow-left" x="-50%" y="-50%" width="200%" height="200%">
                <feDropShadow dx="2" dy="4" stdDeviation="3"
                              flood-color="[SHADOW_COLOR]" flood-opacity="0.5" />
            </filter>
        </defs>

        <!-- Hauptelement mit Animation -->
        <g filter="url(#[name]Shadow-left)">
            <ellipse cx="60" cy="60" rx="[RX]" ry="[RY]" fill="url(#[name]-left)">
                <animate attributeName="ry" values="[RY]; [RY+2]; [RY]"
                         dur="3s" repeatCount="indefinite" />
            </ellipse>

            <!-- Lichtreflexe -->
            <ellipse cx="48" cy="48" rx="16" ry="10" fill="#ffffff" opacity="0.35"
                     transform="rotate(-20 48 48)">
                <animate attributeName="opacity" values="0.35; 0.5; 0.35"
                         dur="2.5s" repeatCount="indefinite" />
            </ellipse>
            <ellipse cx="52" cy="52" rx="8" ry="5" fill="#ffffff" opacity="0.5"
                     transform="rotate(-20 52 52)" />

            <!-- Kleine Lichtpunkte -->
            <circle cx="42" cy="55" r="3" fill="#ffffff" opacity="0.25" />
            <circle cx="70" cy="50" r="2" fill="#ffffff" opacity="0.2" />
        </g>
    </svg>
</div>

<div class="parallax-item parallax-item-right" data-speed="[SPEED]" data-layer="[NUMBER]">
    <svg viewBox="0 0 120 120" class="ingredient-svg [name]-svg">
        <defs>
            <radialGradient id="[name]-right" cx="35%" cy="35%" r="65%">
                <!-- Identische Stops wie links -->
            </radialGradient>
            <filter id="[name]Shadow-right">
                <!-- Identische Filter wie links -->
            </filter>
        </defs>
        <g filter="url(#[name]Shadow-right)">
            <!-- Identischer Inhalt wie links -->
        </g>
    </svg>
</div>
```

## Beispiele

### Beispiel 1: Tomate

**User-Request:** "Erstelle CSS für eine Tomate als Parallax-Item"

**Output:**
```css
/* ===================================
   TOMATE - Layer 2
   =================================== */

.tomato-slice {
  width: 100px;
  height: 100px;
  background: radial-gradient(circle at 35% 30%,
              #fca5a5 0%,
              #f87171 20%,
              #ef4444 50%,
              #dc2626 80%,
              #b91c1c 100%);
  border-radius: 50%;
  box-shadow: inset -12px -12px 20px rgba(0, 0, 0, 0.2),
              inset 8px 8px 15px rgba(255, 255, 255, 0.1),
              0 8px 25px rgba(239, 68, 68, 0.5),
              0 4px 12px rgba(185, 28, 28, 0.4);
  position: relative;
  filter: drop-shadow(0 4px 8px rgba(127, 29, 29, 0.3));
}

.tomato-slice::before {
  content: '';
  position: absolute;
  width: 32px;
  height: 18px;
  background: radial-gradient(ellipse, rgba(255, 255, 255, 0.45), transparent);
  border-radius: 50%;
  top: 22%;
  left: 28%;
  transform: rotate(-25deg);
  animation: tomatoGlow 2.5s ease-in-out infinite;
}

.tomato-slice::after {
  content: '';
  position: absolute;
  width: 45px;
  height: 45px;
  background: radial-gradient(circle,
              rgba(254, 242, 242, 0.3) 0%,
              rgba(254, 202, 202, 0.2) 40%,
              rgba(252, 165, 165, 0.1) 70%,
              transparent 100%);
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.parallax-item-left .tomato-slice {
  transform: rotate(-10deg);
}

.parallax-item-right .tomato-slice {
  transform: rotate(10deg);
}

@keyframes tomatoGlow {
  0%, 100% { opacity: 0.45; }
  50% { opacity: 0.65; }
}
```

### Beispiel 2: Wassertropfen

**User-Request:** "Erstelle CSS für einen Wassertropfen"

**Output:**
```css
/* ===================================
   WASSERTROPFEN
   =================================== */

.water-drop {
  width: 50px;
  height: 70px;
  background: linear-gradient(135deg,
              rgba(255, 255, 255, 0.95) 0%,
              rgba(254, 254, 254, 0.85) 30%,
              rgba(240, 249, 255, 0.7) 60%,
              rgba(191, 219, 254, 0.6) 100%);
  border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
  box-shadow: inset -4px -6px 12px rgba(0, 0, 0, 0.08),
              inset 4px 4px 10px rgba(255, 255, 255, 0.6),
              0 6px 20px rgba(59, 130, 246, 0.35),
              0 3px 10px rgba(37, 99, 235, 0.25);
  position: relative;
  filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.25));
  animation: dropFloat 2.5s ease-in-out infinite;
}

.water-drop::before {
  content: '';
  position: absolute;
  width: 18px;
  height: 12px;
  background: radial-gradient(ellipse, rgba(255, 255, 255, 0.8), transparent);
  border-radius: 50%;
  top: 20%;
  left: 35%;
  transform: rotate(-15deg);
}

.water-drop::after {
  content: '';
  position: absolute;
  width: 10px;
  height: 10px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.6), transparent);
  border-radius: 50%;
  bottom: 25%;
  right: 30%;
}

@keyframes dropFloat {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-10px) scale(1.05); }
}
```

## Best Practices - BEFOLGE DIESE IMMER

1. **MINDESTENS 5 Gradient-Stops**
   - Mehr Stops = mehr Realismus

2. **IMMER alle 3 Schatten-Typen kombinieren**
   - Inset Dark (innere Tiefe)
   - Inset Light (innerer Glanz)
   - Outset (äußerer Schatten, 2 Layer)
   - Drop-Shadow (zusätzliche Tiefe)

3. **IMMER ::before für Lichtreflex**
   - Position: 20-35% von oben/links
   - Ellipse mit weißem Gradient
   - Opacity: 0.4-0.5

4. **Animation hinzufügen**
   - Float für organische Elemente
   - Glow für Lichtreflexe
   - Sway für Tropfen/flüssige Elemente

5. **Symmetrie für Parallax**
   - Links: transform: rotate(-[angle]deg)
   - Rechts: transform: rotate([angle]deg) scaleX(-1)

6. **Position: relative IMMER setzen**
   - Für ::before/::after Positionierung

7. **Filter statt nur box-shadow**
   - drop-shadow für komplexe Shapes
   - Besser für nicht-rechteckige Formen

## Troubleshooting

**Problem: Gradient sieht flach aus**
→ Lösung: Mehr Stops hinzufügen (min. 5), radial-gradient verwenden

**Problem: Schatten zu schwach**
→ Lösung: Opacity erhöhen (0.4-0.6), blur-radius vergrößern

**Problem: Lichtreflex nicht sichtbar**
→ Lösung: Opacity erhöhen auf 0.5-0.7, Position anpassen (25-35% von oben/links)

**Problem: Animation ruckelt**
→ Lösung: transform statt top/left, will-change: transform hinzufügen

**Problem: Zu viele ::before/::after**
→ Lösung: Nur 1 ::before (Lichtreflex) + 1 ::after (Detail) pro Element
