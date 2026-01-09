# Unique Element Examples

Konkrete SVG-Code-Beispiele für verschiedene Branchen.

## 1. Arzt/Praxis - Pulsierendes Herz mit EKG

```svg
<svg class="heart-pulse" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="heartGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#e74c3c"/>
            <stop offset="100%" style="stop-color:#c0392b"/>
        </linearGradient>
        <filter id="heartGlow">
            <feGaussianBlur stdDeviation="4" result="blur"/>
            <feMerge>
                <feMergeNode in="blur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>

    <!-- EKG Linie -->
    <g class="ekg-line">
        <path class="ekg-path" d="M0 150 L100 150 L120 150 L140 80 L160 220 L180 150 L200 150 L400 150"
              stroke="#e74c3c" stroke-width="3" fill="none" stroke-linecap="round"/>
    </g>

    <!-- Herz -->
    <g class="heart" filter="url(#heartGlow)">
        <path d="M200 230
                 C200 230 120 170 120 120
                 C120 80 160 60 200 100
                 C240 60 280 80 280 120
                 C280 170 200 230 200 230Z"
              fill="url(#heartGradient)"/>
    </g>
</svg>
```

**CSS Animation:**
```css
.heart {
    animation: heartbeat 1.2s ease-in-out infinite;
    transform-origin: center;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    15% { transform: scale(1.15); }
    30% { transform: scale(1); }
    45% { transform: scale(1.1); }
    60% { transform: scale(1); }
}

.ekg-path {
    stroke-dasharray: 800;
    stroke-dashoffset: 800;
    animation: ekg-draw 2s linear infinite;
}

@keyframes ekg-draw {
    to { stroke-dashoffset: 0; }
}
```

---

## 2. Steuerberater - Wachsende Balkendiagramme

```svg
<svg class="chart-growth" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="barGradient" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" style="stop-color:#1a365d"/>
            <stop offset="100%" style="stop-color:#2c5282"/>
        </linearGradient>
    </defs>

    <!-- Achsen -->
    <line x1="50" y1="250" x2="350" y2="250" stroke="#1a365d" stroke-width="2"/>
    <line x1="50" y1="50" x2="50" y2="250" stroke="#1a365d" stroke-width="2"/>

    <!-- Balken -->
    <g class="bars">
        <rect class="bar bar-1" x="80" y="250" width="40" height="0" fill="url(#barGradient)" rx="4"/>
        <rect class="bar bar-2" x="140" y="250" width="40" height="0" fill="url(#barGradient)" rx="4"/>
        <rect class="bar bar-3" x="200" y="250" width="40" height="0" fill="url(#barGradient)" rx="4"/>
        <rect class="bar bar-4" x="260" y="250" width="40" height="0" fill="url(#barGradient)" rx="4"/>
    </g>

    <!-- Trend-Pfeil -->
    <path class="trend-arrow" d="M70 200 Q200 100 330 80"
          stroke="#b8860b" stroke-width="3" fill="none" stroke-dasharray="5,5"/>
    <polygon class="arrow-head" points="340,75 330,90 345,85" fill="#b8860b"/>
</svg>
```

**CSS Animation:**
```css
.bar {
    transition: height 1s ease-out, y 1s ease-out;
}

.chart-growth.animate .bar-1 { height: 80px; y: 170; }
.chart-growth.animate .bar-2 { height: 120px; y: 130; }
.chart-growth.animate .bar-3 { height: 100px; y: 150; }
.chart-growth.animate .bar-4 { height: 160px; y: 90; }

.bar-1 { transition-delay: 0s; }
.bar-2 { transition-delay: 0.2s; }
.bar-3 { transition-delay: 0.4s; }
.bar-4 { transition-delay: 0.6s; }

.trend-arrow {
    stroke-dashoffset: 300;
    animation: draw-trend 2s ease-out 1s forwards;
}

@keyframes draw-trend {
    to { stroke-dashoffset: 0; }
}
```

---

## 3. Restaurant - Dampfende Kaffeetasse

```svg
<svg class="coffee-cup" viewBox="0 0 300 350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="cupGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B4513"/>
            <stop offset="100%" style="stop-color:#5D3A1A"/>
        </linearGradient>
        <filter id="blur">
            <feGaussianBlur stdDeviation="2"/>
        </filter>
    </defs>

    <!-- Untertasse -->
    <ellipse cx="150" cy="300" rx="100" ry="20" fill="#D2691E"/>
    <ellipse cx="150" cy="295" rx="90" ry="15" fill="#8B4513"/>

    <!-- Tasse -->
    <path d="M70 150 L80 280 Q150 300 220 280 L230 150 Z" fill="url(#cupGradient)"/>

    <!-- Henkel -->
    <path d="M230 170 Q280 170 280 220 Q280 270 230 260"
          stroke="#8B4513" stroke-width="15" fill="none" stroke-linecap="round"/>

    <!-- Kaffee-Oberfläche -->
    <ellipse cx="150" cy="160" rx="75" ry="20" fill="#3E2723"/>

    <!-- Dampf -->
    <g class="steam" filter="url(#blur)">
        <path class="steam-1" d="M120 120 Q115 80 125 50" stroke="white" stroke-width="8" fill="none" opacity="0.6"/>
        <path class="steam-2" d="M150 110 Q145 70 155 40" stroke="white" stroke-width="8" fill="none" opacity="0.5"/>
        <path class="steam-3" d="M180 120 Q175 80 185 50" stroke="white" stroke-width="8" fill="none" opacity="0.6"/>
    </g>
</svg>
```

**CSS Animation:**
```css
.steam-1, .steam-2, .steam-3 {
    animation: rise 3s ease-in-out infinite;
}

.steam-1 { animation-delay: 0s; }
.steam-2 { animation-delay: 0.5s; }
.steam-3 { animation-delay: 1s; }

@keyframes rise {
    0% {
        transform: translateY(0) scaleY(1);
        opacity: 0.6;
    }
    50% {
        transform: translateY(-20px) scaleY(1.2);
        opacity: 0.3;
    }
    100% {
        transform: translateY(-40px) scaleY(1.5);
        opacity: 0;
    }
}
```

---

## 4. Handwerker - Rotierender Schraubenschlüssel

```svg
<svg class="wrench" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="metalGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#C0C0C0"/>
            <stop offset="50%" style="stop-color:#A0A0A0"/>
            <stop offset="100%" style="stop-color:#808080"/>
        </linearGradient>
        <filter id="metalShadow">
            <feDropShadow dx="3" dy="3" stdDeviation="2" flood-color="#333" flood-opacity="0.5"/>
        </filter>
    </defs>

    <g class="wrench-group" filter="url(#metalShadow)">
        <!-- Griff -->
        <rect x="130" y="100" width="40" height="150" rx="5" fill="url(#metalGradient)"/>

        <!-- Kopf oben -->
        <path d="M100 100 L200 100 L200 60 Q200 40 180 40 L170 40 L170 70 L130 70 L130 40 L120 40 Q100 40 100 60 Z"
              fill="url(#metalGradient)"/>

        <!-- Kopf unten (offen) -->
        <path d="M100 250 L200 250 L200 290 Q200 310 180 310 L180 270 L120 270 L120 310 Q100 310 100 290 Z"
              fill="url(#metalGradient)"/>

        <!-- Schraube -->
        <g class="screw">
            <circle cx="150" cy="290" r="15" fill="#555"/>
            <line x1="140" y1="290" x2="160" y2="290" stroke="#333" stroke-width="3"/>
            <line x1="150" y1="280" x2="150" y2="300" stroke="#333" stroke-width="3"/>
        </g>
    </g>
</svg>
```

**CSS Animation:**
```css
.wrench-group {
    transform-origin: center;
    animation: tighten 2s ease-in-out infinite;
}

@keyframes tighten {
    0%, 100% { transform: rotate(0deg); }
    25% { transform: rotate(15deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(-15deg); }
}

.screw {
    animation: screw-turn 2s linear infinite;
    transform-origin: 150px 290px;
}

@keyframes screw-turn {
    to { transform: rotate(360deg); }
}
```

---

## 5. IT/Tech - Matrix Code Rain

```svg
<svg class="code-matrix" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="codeGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#00ff00;stop-opacity:1"/>
            <stop offset="100%" style="stop-color:#00ff00;stop-opacity:0"/>
        </linearGradient>
    </defs>

    <rect width="400" height="300" fill="#0a0a0a"/>

    <g class="matrix-rain" fill="url(#codeGradient)" font-family="monospace" font-size="14">
        <text class="col-1" x="20" y="0">01101</text>
        <text class="col-2" x="60" y="50">10010</text>
        <text class="col-3" x="100" y="20">11001</text>
        <text class="col-4" x="140" y="80">00110</text>
        <text class="col-5" x="180" y="10">10101</text>
        <text class="col-6" x="220" y="60">01010</text>
        <text class="col-7" x="260" y="30">11110</text>
        <text class="col-8" x="300" y="70">00011</text>
        <text class="col-9" x="340" y="40">10100</text>
    </g>

    <!-- Zentrales Element: Chip -->
    <g class="chip" transform="translate(150, 100)">
        <rect x="0" y="0" width="100" height="100" rx="5" fill="#1a1a2e" stroke="#00ff00" stroke-width="2"/>
        <text x="50" y="55" text-anchor="middle" fill="#00ff00" font-family="monospace" font-size="12">CPU</text>
        <!-- Pins -->
        <line x1="-10" y1="25" x2="0" y2="25" stroke="#00ff00" stroke-width="2"/>
        <line x1="-10" y1="50" x2="0" y2="50" stroke="#00ff00" stroke-width="2"/>
        <line x1="-10" y1="75" x2="0" y2="75" stroke="#00ff00" stroke-width="2"/>
        <line x1="100" y1="25" x2="110" y2="25" stroke="#00ff00" stroke-width="2"/>
        <line x1="100" y1="50" x2="110" y2="50" stroke="#00ff00" stroke-width="2"/>
        <line x1="100" y1="75" x2="110" y2="75" stroke="#00ff00" stroke-width="2"/>
    </g>
</svg>
```

**CSS Animation:**
```css
.matrix-rain text {
    animation: rain 3s linear infinite;
}

.col-1 { animation-delay: 0s; }
.col-2 { animation-delay: 0.3s; }
.col-3 { animation-delay: 0.6s; }
.col-4 { animation-delay: 0.9s; }
.col-5 { animation-delay: 1.2s; }
.col-6 { animation-delay: 0.2s; }
.col-7 { animation-delay: 0.5s; }
.col-8 { animation-delay: 0.8s; }
.col-9 { animation-delay: 1.1s; }

@keyframes rain {
    0% { transform: translateY(-50px); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(350px); opacity: 0; }
}

.chip {
    animation: chip-glow 2s ease-in-out infinite;
}

@keyframes chip-glow {
    0%, 100% { filter: drop-shadow(0 0 5px #00ff00); }
    50% { filter: drop-shadow(0 0 20px #00ff00); }
}
```

---

## 6. Zahnarzt - Strahlender Zahn

```svg
<svg class="shiny-tooth" viewBox="0 0 300 350" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="toothGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#ffffff"/>
            <stop offset="50%" style="stop-color:#f5f5f5"/>
            <stop offset="100%" style="stop-color:#e8e8e8"/>
        </linearGradient>
        <filter id="toothGlow">
            <feGaussianBlur stdDeviation="8" result="glow"/>
            <feMerge>
                <feMergeNode in="glow"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>

    <!-- Zahn -->
    <g class="tooth" filter="url(#toothGlow)">
        <path d="M100 50
                 Q90 50 85 70
                 L80 150 Q80 180 100 200 L110 280 Q115 300 130 300 Q145 300 150 280
                 L150 280 Q155 300 170 300 Q185 300 190 280 L200 200 Q220 180 220 150
                 L215 70 Q210 50 200 50
                 Q175 60 150 60 Q125 60 100 50 Z"
              fill="url(#toothGradient)" stroke="#ddd" stroke-width="2"/>
    </g>

    <!-- Glitzer-Sterne -->
    <g class="sparkles">
        <path class="sparkle sparkle-1" d="M80 80 L85 90 L80 100 L75 90 Z" fill="#FFD700"/>
        <path class="sparkle sparkle-2" d="M220 100 L225 110 L220 120 L215 110 Z" fill="#FFD700"/>
        <path class="sparkle sparkle-3" d="M150 30 L155 40 L150 50 L145 40 Z" fill="#FFD700"/>
        <circle class="sparkle sparkle-4" cx="100" cy="120" r="3" fill="#FFD700"/>
        <circle class="sparkle sparkle-5" cx="200" cy="80" r="2" fill="#FFD700"/>
    </g>
</svg>
```

**CSS Animation:**
```css
.tooth {
    animation: tooth-shine 3s ease-in-out infinite;
}

@keyframes tooth-shine {
    0%, 100% { filter: url(#toothGlow) brightness(1); }
    50% { filter: url(#toothGlow) brightness(1.1); }
}

.sparkle {
    animation: twinkle 1.5s ease-in-out infinite;
    transform-origin: center;
}

.sparkle-1 { animation-delay: 0s; }
.sparkle-2 { animation-delay: 0.3s; }
.sparkle-3 { animation-delay: 0.6s; }
.sparkle-4 { animation-delay: 0.9s; }
.sparkle-5 { animation-delay: 1.2s; }

@keyframes twinkle {
    0%, 100% {
        transform: scale(0);
        opacity: 0;
    }
    50% {
        transform: scale(1.2);
        opacity: 1;
    }
}
```

---

## Verwendung

Bei Website-Erstellung:
1. Branche identifizieren
2. Passendes Element aus Beispielen wählen
3. Farben an Corporate Design anpassen
4. In Website integrieren (nach Hero-Sektion)
5. JavaScript für Interaktivität hinzufügen
