---
name: parallax-design-ideas
description: Collection of advanced parallax effects and scroll-based animations for interactive web experiences. Use when designing immersive scroll experiences, food/restaurant websites, or interactive product showcases.
---

# Parallax Design Ideas

Creative concepts for building immersive scroll experiences with layered parallax effects.

## 7-Layer Parallax System

### Layer Structure (Back to Front)

1. **Deep Background** – Gradient that reacts to mouse movement
2. **Kitchen Glow** – Dynamic fire glow that follows the mouse cursor
3. **Smoke Particles** – Rising smoke particles with realistic physics
4. **Döner Spieß** – Rotating spit in the background
5. **Spice Particles** – 30 floating spice particles (Yellow, Orange, Red, Green)
6. **Main Döner Build** – The interactive döner assembly
7. **Flying Ingredients** – Foreground ingredients in motion

## "Build Your Döner" Scroll Experience

Interactive scroll-based assembly animation where the döner is built layer by layer as the user scrolls:

### Scroll Timeline

| Scroll % | Animation | Details |
|----------|-----------|---------|
| **0-15%** | Bread opens | Pita bread unfolds with bounce effect |
| **15-30%** | Meat flies in | From right side with rotation animation |
| **30-45%** | Lettuce slides in | From left with water droplet particles! |
| **45-60%** | Tomatoes zoom | Scale-in effect from center |
| **60-75%** | Onion rings fall | Drop from top with gravity simulation |
| **75-100%** | Sauce drips | Animated drip effect onto the döner |

## Implementation Concepts

### Mouse-Reactive Background
```javascript
// Gradient follows mouse position
background: radial-gradient(
  circle at var(--mouse-x) var(--mouse-y),
  rgba(255, 150, 0, 0.3),
  rgba(139, 69, 19, 0.8)
)
```

### Particle Systems

**Spice Particles:**
- 30 floating elements
- Colors: `#FFD700`, `#FFA500`, `#FF4500`, `#32CD32`
- Random size, speed, and drift patterns
- Blur effect for depth

**Smoke Particles:**
- Vertical rise with horizontal drift
- Opacity fade-out as they rise
- Scale increase with altitude

### Scroll-Triggered Animations

Use `IntersectionObserver` or scroll position to trigger:
- Transform: `translateX`, `translateY`, `rotate`, `scale`
- Opacity transitions
- Staggered timing for layered ingredients
- Physics-based easing (bounce, elastic)

## Use Cases

- Food & Restaurant websites
- Product assembly showcases
- Interactive storytelling
- E-commerce product reveals
- Landing pages with high engagement goals

## Technical Stack Suggestions

- **Parallax:** React Spring Parallax (recommended), Framer Motion, GSAP ScrollTrigger, or custom CSS `transform: translateZ()`
- **Particles:** Three.js, Particles.js, or CSS-only with generated elements
- **Scroll Animations:** Locomotive Scroll, GSAP, or native Intersection Observer

---

# React Spring Parallax Implementation

Complete implementation guide using `@react-spring/parallax` library.

## Installation

```bash
npm install @react-spring/parallax react-spring
```

## Core Concepts

### 1. Parallax Container

```jsx
import { Parallax } from '@react-spring/parallax';

<Parallax pages={4} ref={ref}>
  {/* ParallaxLayer components */}
</Parallax>
```

- `pages`: Total scrollable height (4 = 4x viewport height)
- `ref`: For programmatic scrolling

### 2. ParallaxLayer Props

| Prop | Type | Description | Example |
|------|------|-------------|---------|
| `offset` | number | Which "page" the layer starts (0-based) | `offset={0}` = first page, `offset={2}` = third page |
| `speed` | number | Parallax scroll speed multiplier | `0.05` = very slow, `1` = normal, `2` = fast |
| `factor` | number | Height multiplier (1 = viewport height) | `factor={2}` = 2x viewport height |
| `sticky` | object | Keep layer visible between pages | `sticky={{ start: 0.9, end: 2.5 }}` |

### 3. Complete Working Example

Based on Fireship.io's Skydiving Cat demo:

```jsx
import { useRef } from 'react';
import { Parallax, ParallaxLayer } from '@react-spring/parallax';

function App() {
  const ref = useRef();

  return (
    <Parallax pages={4} ref={ref}>

      {/* Background Layer 1 - Moon (slow, covers first 2 pages) */}
      <ParallaxLayer
        offset={0}
        speed={1}
        factor={2}
        style={{
          backgroundImage: `url('/moon.png')`,
          backgroundSize: 'cover',
        }}
      />

      {/* Background Layer 2 - Ground (covers last 2 pages) */}
      <ParallaxLayer
        offset={2}
        speed={1}
        factor={4}
        style={{
          backgroundImage: `url('/land.png')`,
          backgroundSize: 'cover',
        }}
      />

      {/* Sticky Element - Cat stays visible from page 0.9 to 2.5 */}
      <ParallaxLayer
        sticky={{ start: 0.9, end: 2.5 }}
        style={{ textAlign: 'center' }}
      >
        <img src="/cat.gif" alt="Skydiving cat" />
      </ParallaxLayer>

      {/* Slow-moving text layer */}
      <ParallaxLayer
        offset={0.2}
        speed={0.05}
        onClick={() => ref.current.scrollTo(3)}
      >
        <h2>Welcome to my website</h2>
      </ParallaxLayer>

      {/* Fast-moving text at bottom */}
      <ParallaxLayer
        offset={3}
        speed={2}
        onClick={() => ref.current.scrollTo(0)}
      >
        <h2>Hi Mom!</h2>
      </ParallaxLayer>

    </Parallax>
  );
}
```

## Speed Values Guide

| Speed | Effect | Use Case |
|-------|--------|----------|
| `0.05 - 0.3` | Very slow crawl | Deep backgrounds, distant mountains |
| `0.5` | Slower than scroll | Mid-ground elements |
| `1` | Normal scroll speed | Static content |
| `1.5 - 2` | Faster than scroll | Foreground elements, clouds |
| `2+` | Very fast | Flying particles, dramatic effects |


## Best Practices

1. **Layer Order**: Background layers first, foreground last
2. **Factor sizing**: Use `factor` to extend layers across multiple pages
3. **Sticky elements**: Great for characters, logos that stay visible during scroll
4. **Speed variety**: Mix slow (0.1-0.5) and fast (1.5-2.5) speeds for depth
5. **Optimize images**: Use compressed PNGs/WebP for background images
6. **Mobile**: Consider reducing `pages` or disabling parallax on mobile

## Source

Implementation based on [Fireship.io's Skydiving Cat Parallax Demo](https://github.com/fireship-io/skydiving-cat-parallax)
