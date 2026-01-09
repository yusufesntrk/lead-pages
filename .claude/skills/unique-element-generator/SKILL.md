---
name: unique-element-generator
description: Generiert einzigartige, interaktive SVG-Elemente für Websites basierend auf Branche. Erstellt animierte 3D-Grafiken mit Scroll-, Hover- und Klick-Interaktionen. Verwende diesen Skill wenn der User nach einzigartigen Features, interaktiven Elementen, Branchensymbolen, animierten SVGs oder Unterscheidungsmerkmalen für Websites fragt.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Unique Element Generator

Erstellt **einzigartige, interaktive Elemente** die eine Website von der Konkurrenz abheben. Jedes Element ist branchenspezifisch, animiert und interaktiv.

## Wann verwenden

- User fragt nach "einzigartigen Features"
- User will Website "von anderen abheben"
- User möchte "interaktive Elemente"
- User fragt nach "Branchensymbol" oder "animiertes Element"
- Bei Website-Erstellung als Differenzierungsmerkmal

## Branchen-Elemente Katalog

| Branche | Element | Interaktion |
|---------|---------|-------------|
| **Rechtsanwalt** | 3D Waage der Gerechtigkeit | Scroll-Kippen, Klick auf Schalen |
| **Arzt/Praxis** | Animiertes Stethoskop / Herzschlag | Pulsierender Herzschlag, Hover-Glow |
| **Steuerberater** | Interaktiver Taschenrechner / Diagramm | Zahlen-Animation, Balken wachsen |
| **Architekt** | 3D Bauplan / Haus-Aufbau | Scroll-basierter Aufbau, Hover-Details |
| **Restaurant** | Dampfende Tasse / Teller | Dampf-Animation, Parallax-Effekt |
| **Handwerker** | Animiertes Werkzeug | Rotation, Hammer-Schlag-Animation |
| **Fotograf** | Kamera mit Blitz | Blitz-Effekt bei Klick, Zoom-Animation |
| **Friseur** | Animierte Schere | Schnipp-Animation, Haar-Partikel |
| **Zahnarzt** | Strahlender Zahn | Glitzer-Animation, Weiß-Pulse |
| **Immobilien** | Haus mit öffnender Tür | Tür öffnet bei Hover, Schlüssel-Animation |
| **Fitness** | Pulsierende Hantel | Bounce-Animation, Kraft-Meter |
| **IT/Tech** | Code-Matrix / Chip | Matrix-Rain, Daten-Flow |

## Technische Umsetzung

### 1. SVG-Struktur

```svg
<svg class="unique-element" viewBox="0 0 400 350">
    <defs>
        <!-- Gradienten für 3D-Effekt -->
        <linearGradient id="primaryGradient">...</linearGradient>
        <radialGradient id="glowGradient">...</radialGradient>

        <!-- Filter für Schatten und Glow -->
        <filter id="shadow">
            <feDropShadow dx="2" dy="4" stdDeviation="3"/>
        </filter>
        <filter id="glow">
            <feGaussianBlur stdDeviation="3"/>
        </filter>
    </defs>

    <!-- Animierte Gruppen -->
    <g class="element-base">...</g>
    <g class="element-interactive">...</g>
    <g class="element-particles">...</g>
</svg>
```

### 2. CSS-Animationen

```css
/* Basis-Setup */
.unique-element {
    width: 100%;
    max-width: 400px;
    filter: drop-shadow(0 20px 40px rgba(0,0,0,0.15));
    transition: all 0.5s ease;
}

/* Scroll-basierte Zustände */
.unique-element.state-1 .interactive-part { transform: ...; }
.unique-element.state-2 .interactive-part { transform: ...; }

/* Hover-Effekte */
.unique-element .hoverable:hover {
    transform: scale(1.05);
    filter: brightness(1.1);
}

/* Partikel-Animation */
@keyframes float {
    0%, 100% { transform: translateY(0); opacity: 0.4; }
    50% { transform: translateY(-15px); opacity: 0.8; }
}

/* Pulse/Glow Animation */
@keyframes pulse-glow {
    0%, 100% { filter: brightness(1); }
    50% { filter: brightness(1.2); }
}
```

### 3. JavaScript-Interaktion

```javascript
function initUniqueElement() {
    const element = document.querySelector('.unique-element');
    const section = element.closest('section');

    // Scroll-basierte Animation
    window.addEventListener('scroll', () => {
        const rect = section.getBoundingClientRect();
        const progress = calculateScrollProgress(rect);
        applyScrollState(element, progress);
    }, { passive: true });

    // Klick-Interaktion
    element.querySelectorAll('.clickable').forEach(el => {
        el.addEventListener('click', () => triggerAnimation(element));
    });

    // Keyboard Accessibility
    element.setAttribute('tabindex', '0');
    element.addEventListener('keydown', handleKeyboard);
}
```

## Sektion-Template

```html
<section class="unique-element-section">
    <div class="container">
        <div class="unique-element-wrapper">
            <div class="unique-element-content">
                <span class="unique-element-label fade-in">[Kontext-Label]</span>
                <h2 class="unique-element-title fade-in">[Aussagekräftiger Titel]</h2>
                <p class="unique-element-text fade-in">[Beschreibung mit Bezug zur Branche]</p>
            </div>
            <div class="unique-element-animation">
                <!-- SVG hier -->
                <p class="element-hint">
                    <svg><!-- Info-Icon --></svg>
                    [Interaktions-Hinweis]
                </p>
            </div>
        </div>
    </div>
</section>
```

## Design-Prinzipien

### Farben
- Primärfarbe der Website als Hauptfarbe
- Akzentfarbe für Highlights und Glow
- Schatten in dunklerer Primärfarbe

### Animation-Level nach Branche

| Branche | Level | Beschreibung |
|---------|-------|--------------|
| Rechtsanwalt, Steuerberater, Bank | Dezent | Langsame Transitions, subtile Effekte |
| Arzt, Zahnarzt, Apotheke | Ruhig | Sanfte Pulse, beruhigende Bewegungen |
| Restaurant, Café, Hotel | Moderat | Appetitliche Animationen, Wärme |
| Kreativagentur, Tech, Startup | Expressiv | Dynamisch, auffällig, innovativ |
| Handwerk, Bau | Solide | Kraftvolle, aber kontrollierte Bewegungen |

### Accessibility
- `tabindex="0"` für Keyboard-Navigation
- `role="img"` mit `aria-label`
- Keyboard-Trigger (Enter/Space)
- Reduzierte Bewegung respektieren: `prefers-reduced-motion`

## Beispiel: Rechtsanwalt-Waage

Siehe implementiertes Beispiel in:
- HTML: `docs/enders-und-enders/index.html` (Zeile 86-245)
- CSS: `docs/enders-und-enders/styles.css` (Zeile 1290-1585)
- JS: `docs/enders-und-enders/script.js` (Zeile 187-349)

## Workflow

1. **Branche identifizieren** → Element aus Katalog wählen
2. **Farben extrahieren** → Corporate Design der Website
3. **Animation-Level festlegen** → Basierend auf Branche
4. **SVG erstellen** → Mit Gradienten, Filtern, Gruppen
5. **CSS hinzufügen** → Animationen, Transitions, States
6. **JS implementieren** → Scroll, Hover, Klick, Keyboard
7. **Testen** → Desktop + Mobile, Accessibility
