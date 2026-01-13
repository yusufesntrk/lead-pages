/* ═══════════════════════════════════════════════════════════════════════════
   SCROLL-DRIVEN ANIMATIONS
   Animationen reagieren direkt auf Scroll-Position
   ═══════════════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
});

function initScrollAnimations() {
    // Alle Sektionen sammeln
    const sections = document.querySelectorAll('[data-scroll-section]');

    // Scroll-Handler mit requestAnimationFrame für Performance
    let ticking = false;

    function onScroll() {
        if (!ticking) {
            requestAnimationFrame(() => {
                sections.forEach(section => {
                    const rect = section.getBoundingClientRect();
                    const windowHeight = window.innerHeight;

                    // Progress:
                    // 0 = Section-Top erreicht Viewport-Bottom (Section kommt rein)
                    // 1 = Section-Mitte ist bei Viewport-Mitte (Section ist zentriert)
                    const sectionTop = rect.top;
                    const sectionHeight = rect.height;
                    const sectionCenter = sectionTop + sectionHeight / 2;
                    const viewportCenter = windowHeight / 2;

                    // Start: sectionTop = windowHeight (Section kommt von unten)
                    // Ende: sectionCenter = viewportCenter (Section ist mittig)
                    const startPoint = windowHeight; // Section-Top am Viewport-Bottom
                    const endPoint = viewportCenter - sectionHeight / 2; // Section-Top wenn zentriert

                    const progress = Math.max(0, Math.min(1, (startPoint - sectionTop) / (startPoint - endPoint)));

                    // Animationen basierend auf Section-Klasse
                    if (section.classList.contains('v1')) animateV1(section, progress);
                    if (section.classList.contains('v2')) animateV2(section, progress);
                    if (section.classList.contains('v3')) animateV3(section, progress);
                    if (section.classList.contains('v4')) animateV4(section, progress);
                    if (section.classList.contains('v5')) animateV5(section, progress);
                    if (section.classList.contains('v6')) animateV6(section, progress);
                    if (section.classList.contains('v7')) animateV7(section, progress);
                    if (section.classList.contains('v8')) animateV8(section, progress);
                });
                ticking = false;
            });
            ticking = true;
        }
    }

    window.addEventListener('scroll', onScroll);
    onScroll(); // Initial call
}

/* ═══════════════════════════════════════════════════════════════════════════
   V1: PATH PROGRESS - Linie zeichnet sich beim Scrollen
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV1(section, progress) {
    const path = section.querySelector('.path-progress');
    const steps = section.querySelectorAll('.path-step');

    if (path) {
        // Pfad zeichnet sich sofort (400 ist die stroke-dasharray Länge)
        path.style.strokeDashoffset = 400 - (400 * progress);
    }

    // Steps aktivieren basierend auf Progress
    steps.forEach((step, i) => {
        const threshold = i * 0.15; // Früher starten
        if (progress > threshold) {
            step.classList.add('active');
        } else {
            step.classList.remove('active');
        }
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V2: HORIZONTAL SLIDE - Cards schieben sich basierend auf Scroll rein
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV2(section, progress) {
    const steps = section.querySelectorAll('.h-step');

    steps.forEach((step, i) => {
        const isFromLeft = step.classList.contains('from-left');

        // Stagger-Effekt pro Card - früher starten
        const staggeredProgress = Math.max(0, Math.min(1, (progress - i * 0.08) / 0.4));

        // Slide-In Distanz (startet außerhalb des Viewports)
        const distance = 100 * (1 - staggeredProgress); // in vw
        const translateX = isFromLeft ? -distance : distance;

        step.style.transform = `translateX(${translateX}vw)`;
        step.style.opacity = staggeredProgress;
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V3: SCALE & FADE - Elemente wachsen beim Scrollen
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV3(section, progress) {
    const steps = section.querySelectorAll('.scale-step');
    const connectors = section.querySelectorAll('.scale-connector');

    steps.forEach((step, i) => {
        const delay = parseFloat(step.dataset.delay) || 0;
        // Früher starten - sofort bei Eintritt
        const stepProgress = Math.max(0, Math.min(1, (progress - delay) / 0.3));

        // Scale von 0 bis 1
        const scale = stepProgress;
        step.style.transform = `scale(${scale})`;
        step.style.opacity = stepProgress;
    });

    connectors.forEach((conn, i) => {
        const connProgress = Math.max(0, Math.min(1, (progress - 0.1 - i * 0.12) / 0.2));
        conn.style.transform = `scaleX(${connProgress})`;
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V4: PARALLAX LAYERS - Elemente bewegen sich unterschiedlich schnell
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV4(section, progress) {
    const layers = section.querySelectorAll('.parallax-layer');
    const steps = section.querySelectorAll('.parallax-step');

    // Layers bewegen sich mit unterschiedlicher Geschwindigkeit
    layers.forEach(layer => {
        const speed = parseFloat(layer.dataset.speed) || 0.5;
        const offset = (progress - 0.5) * 200 * speed;
        layer.style.transform = `translateY(${offset}px)`;
    });

    // Cards bewegen sich auch
    steps.forEach(step => {
        const speed = parseFloat(step.dataset.speed) || 0.5;
        const offset = (progress - 0.5) * 150 * speed;
        step.style.transform = `translateY(${offset}px)`;
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V5: ROTATE ON SCROLL - Icons drehen sich basierend auf Scroll
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV5(section, progress) {
    const steps = section.querySelectorAll('.rotate-step');

    steps.forEach((step, i) => {
        const maxRotation = parseInt(step.dataset.rotation) || 360;
        const icon = step.querySelector('.rotate-icon');

        // Rotation basierend auf Scroll-Progress
        const rotation = progress * maxRotation;

        if (icon) {
            icon.style.transform = `rotate(${rotation}deg)`;
        }
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V6: STICKY PROGRESS - Fortschrittsbalken folgt Scroll
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV6(section, progress) {
    const fill = section.querySelector('.progress-fill');
    const dots = section.querySelectorAll('.progress-dot');
    const steps = section.querySelectorAll('.sticky-step');

    if (fill) {
        // Progress Bar füllt sich sofort (0-100%)
        const fillProgress = Math.max(0, Math.min(100, progress * 100));
        fill.style.width = `${fillProgress}%`;
    }

    // Dots aktivieren - früher
    dots.forEach((dot, i) => {
        const threshold = i * 0.2;
        const nextThreshold = threshold + 0.2;

        dot.classList.remove('active', 'completed');

        if (progress > nextThreshold) {
            dot.classList.add('completed');
        } else if (progress > threshold) {
            dot.classList.add('active');
        }
    });

    // Content Steps aktivieren - früher
    steps.forEach((step, i) => {
        const threshold = i * 0.2;

        if (progress > threshold && progress < threshold + 0.3) {
            step.classList.add('active');
        } else {
            step.classList.remove('active');
        }
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V7: 3D FLIP ON SCROLL - Cards kippen basierend auf Scroll
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV7(section, progress) {
    const steps = section.querySelectorAll('.flip-step');

    steps.forEach((step, i) => {
        const card = step.querySelector('.flip-card');
        const flipType = step.dataset.flip || 'rotateY';

        // Flip startet sofort gestaffelt
        const staggeredProgress = Math.max(0, Math.min(1, (progress - i * 0.1) / 0.4));

        // Flip von 0 bis 180 Grad
        const rotation = staggeredProgress * 180;

        if (card) {
            card.style.transform = `${flipType}(${rotation}deg)`;
        }
    });
}

/* ═══════════════════════════════════════════════════════════════════════════
   V8: SCROLL COUNTER - Zahlen zählen basierend auf Scroll
   ═══════════════════════════════════════════════════════════════════════════ */

function animateV8(section, progress) {
    const steps = section.querySelectorAll('.counter-step');

    steps.forEach((step, i) => {
        const num = step.querySelector('.counter-num');
        const circle = step.querySelector('.counter-progress');

        if (num && circle) {
            const target = parseInt(num.dataset.target) || 100;

            // Staggered progress - startet sofort
            const staggeredProgress = Math.max(0, Math.min(1, (progress - i * 0.08) / 0.5));

            // Zahl animieren
            const currentValue = Math.round(staggeredProgress * target);
            num.textContent = currentValue;

            // Kreis füllen (283 ist der Umfang bei r=45)
            const circumference = 283;
            const offset = circumference - (staggeredProgress * target / 100 * circumference);
            circle.style.strokeDashoffset = offset;
        }
    });
}
