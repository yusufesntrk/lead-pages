# Steuerberater Preset

Branche: Steuerberater, Wirtschaftsprüfer, Buchhalter

## Hero Section

```yaml
layout: centered
background: gradient (Primary → darker shade)
height: 100dvh
unique_element: false
```

### Hero-Animationen

| Element | Animation |
|---------|-----------|
| Headline | Statisch (kein Effekt) |
| Subline | fade-in (0.5s delay) |
| CTA Button | fade-in (0.8s delay) |
| Trust-Badge | Statisch |

**VERBOTEN im Hero:**
- ❌ letter-reveal
- ❌ Animierte SVGs
- ❌ Parallax
- ❌ Floating elements

---

## Body-Sektionen

### Erlaubte Text-Effekte (PFLICHT: mindestens 3 verwenden!)

| Effekt | Wo einsetzen |
|--------|--------------|
| `underline-scroll` | Wichtige Begriffe in Headlines |
| `blur-reveal` | Section-Überschriften |
| `stagger-list` | Leistungslisten, Service-Cards |
| `counter` | Jahre Erfahrung, Mandanten-Anzahl |
| `fade` | Paragraphen, Testimonials |

### Verbotene Text-Effekte

- ❌ letter-reveal (zu verspielt)
- ❌ gradient-reveal (zu bunt)
- ❌ typewriter (zu technisch)
- ❌ split-lines (zu dynamisch)

---

## Animationen

```yaml
level: dezent
sections: fade-in, slide-up
duration: 0.6s - 0.8s
timing: ease-out
```

### Sections-Animationen

| Sektion | Animation |
|---------|-----------|
| Leistungen-Cards | stagger (0.1s delay pro Card) |
| Testimonials | fade-in |
| Über-uns | slide-up |
| Kontakt-Form | fade-in |
| Footer | keine |

---

## Farben

```yaml
mood: professional, vertrauenswürdig
saturation: low-medium
```

| Rolle | Empfehlung |
|-------|------------|
| Primary | Dunkelblau (#1a365d, #1e3a5f) |
| Secondary | Grau (#4a5568, #718096) |
| Accent | Dezentes Gold (#b8860b) oder Grün (#2f855a) |
| Background | Weiß, sehr helles Grau (#f7fafc) |
| Text | Dunkelgrau (#2d3748) |

---

## Typography

```yaml
headings: Serif oder elegante Sans-Serif
body: Clean Sans-Serif
```

Empfohlene Kombinationen:
- Playfair Display + Source Sans Pro
- Merriweather + Open Sans
- Lora + Roboto

---

## UX Patterns

```yaml
cta_style: subtle-prominent (nicht aggressiv)
trust_signals: SEHR WICHTIG
testimonials: prominent
```

### Trust-Elemente (PFLICHT)

- ✅ "Seit [Jahr] in Offenburg"
- ✅ Steuerberaterkammer-Logo/Badge
- ✅ Google-Rating (wenn 4.5+)
- ✅ "Persönliche Betreuung"
- ✅ Qualifikationen (Dipl.-Kfm., etc.)

### CTA-Texte

- "Jetzt Beratungstermin vereinbaren"
- "Kostenlose Erstberatung"
- "Kontakt aufnehmen"

**NICHT:**
- ❌ "Jetzt loslegen!"
- ❌ "Let's go!"
- ❌ Emojis in CTAs

---

## Beispiel-Implementierung

### Hero mit Underline

```html
<section class="hero">
    <div class="hero-content">
        <span class="hero-badge">Seit 1995 in Offenburg</span>
        <h1>Kompetente Steuerberatung<br>
            <span class="underline-scroll" data-scroll>für Ihren Erfolg</span>
        </h1>
        <p class="hero-sub" data-scroll>
            Persönlich. Zuverlässig. Zukunftsorientiert.
        </p>
        <a href="kontakt.html" class="btn-primary" data-scroll>
            Beratungstermin vereinbaren
        </a>
    </div>
</section>
```

### Statistik mit Counter

```html
<section class="stats">
    <div class="stat" data-scroll>
        <span class="counter" data-target="25" data-scroll>0</span>
        <span class="stat-suffix">+</span>
        <span class="stat-label">Jahre Erfahrung</span>
    </div>
    <div class="stat" data-scroll style="transition-delay: 0.2s">
        <span class="counter" data-target="500" data-scroll>0</span>
        <span class="stat-suffix">+</span>
        <span class="stat-label">Zufriedene Mandanten</span>
    </div>
</section>
```

### Leistungen mit Stagger

```html
<section class="services">
    <h2 class="blur-reveal" data-scroll>Unsere Leistungen</h2>
    <div class="services-grid" data-scroll data-stagger>
        <div class="service-card">
            <h3>Steuererklärung</h3>
            <p>Für Privatpersonen und Unternehmen</p>
        </div>
        <div class="service-card">
            <h3>Finanzbuchhaltung</h3>
            <p>Laufende Buchführung und Auswertungen</p>
        </div>
        <!-- weitere cards -->
    </div>
</section>
```
