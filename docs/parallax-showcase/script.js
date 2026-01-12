/**
 * PARALLAX SHOWCASE - JavaScript
 * Handles scroll animations, mouse tracking, and interactive effects
 */

document.addEventListener('DOMContentLoaded', () => {
    initMouseGlow();
    initParticles();
    initScrollAnimations();
    initParallaxLayers();
    initNavigation();
    initBuildAnimation();
    initExplosion();
    initStickySteps();
    initFloatingCards();
    initTextReveal();
    initMagneticButtons();
    initCounterAnimation();
    initImageReveal();
    initMarquee();
});

/**
 * Mouse Glow Effect
 * Creates a glowing orb that follows the mouse cursor
 */
function initMouseGlow() {
    const glow = document.getElementById('mouseGlow');
    if (!glow) return;

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let currentX = mouseX;
    let currentY = mouseY;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animateGlow() {
        // Smooth interpolation
        currentX += (mouseX - currentX) * 0.1;
        currentY += (mouseY - currentY) * 0.1;

        glow.style.left = `${currentX}px`;
        glow.style.top = `${currentY}px`;

        requestAnimationFrame(animateGlow);
    }

    animateGlow();
}

/**
 * Floating Particles
 * Generates and animates particles in the background
 */
function initParticles() {
    const container = document.getElementById('particles');
    if (!container) return;

    const colors = ['#667eea', '#764ba2', '#f093fb', '#FFD700', '#FF6B6B'];
    const particleCount = 40;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';

        const size = Math.random() * 8 + 4;
        const color = colors[Math.floor(Math.random() * colors.length)];

        particle.style.cssText = `
            width: ${size}px;
            height: ${size}px;
            background: ${color};
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            animation-delay: ${Math.random() * 5}s;
            animation-duration: ${5 + Math.random() * 5}s;
            filter: blur(${Math.random() * 2}px);
            opacity: ${0.3 + Math.random() * 0.5};
        `;

        container.appendChild(particle);
    }
}

/**
 * Scroll Animations with Intersection Observer
 * Reveals elements when they enter the viewport
 */
function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe reveal elements
    document.querySelectorAll('.reveal-text, .floating-card, .sticky-step').forEach((el) => {
        observer.observe(el);
    });
}

/**
 * Parallax Layer Movement
 * Different layers move at different speeds based on scroll
 */
function initParallaxLayers() {
    const layers = {
        deep: document.querySelectorAll('.layer-deep'),
        back: document.querySelectorAll('.layer-back'),
        mid: document.querySelectorAll('.layer-mid'),
        front: document.querySelectorAll('.layer-front')
    };

    const speeds = {
        deep: 0.1,
        back: 0.3,
        mid: 0.5,
        front: 0.8
    };

    let ticking = false;

    function updateParallax() {
        const scrollY = window.scrollY;

        Object.keys(layers).forEach((key) => {
            layers[key].forEach((layer) => {
                const offset = scrollY * speeds[key];
                layer.style.transform = `translateY(${offset}px)`;
            });
        });

        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateParallax);
            ticking = true;
        }
    });
}

/**
 * Navigation Dots
 * Updates active state based on current section
 */
function initNavigation() {
    const sections = document.querySelectorAll('.parallax-section');
    const navDots = document.querySelectorAll('.nav-dot');

    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.id;

                navDots.forEach((dot) => {
                    dot.classList.remove('active');
                    if (dot.dataset.section === sectionId) {
                        dot.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach((section) => {
        observer.observe(section);
    });

    // Smooth scroll on dot click
    navDots.forEach((dot) => {
        dot.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = dot.getAttribute('href').slice(1);
            const target = document.getElementById(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

/**
 * Build Animation
 * Progressive reveal of stacked elements as user scrolls
 */
function initBuildAnimation() {
    const buildSection = document.getElementById('build');
    const buildItems = document.querySelectorAll('.build-item');
    const progressFill = document.getElementById('buildProgress');

    if (!buildSection || !buildItems.length) return;

    function updateBuild() {
        const rect = buildSection.getBoundingClientRect();
        const sectionHeight = buildSection.offsetHeight;
        const viewportHeight = window.innerHeight;

        // Calculate scroll progress within section
        const scrolledIntoSection = -rect.top;
        const scrollableDistance = sectionHeight - viewportHeight;
        const progress = Math.max(0, Math.min(1, scrolledIntoSection / scrollableDistance));

        // Update progress bar
        if (progressFill) {
            progressFill.style.width = `${progress * 100}%`;
        }

        // Show/hide build items based on progress
        buildItems.forEach((item) => {
            const trigger = parseFloat(item.dataset.trigger) || 0;
            if (progress >= trigger) {
                item.classList.add('visible');
            } else {
                item.classList.remove('visible');
            }
        });
    }

    window.addEventListener('scroll', () => {
        requestAnimationFrame(updateBuild);
    });

    updateBuild();
}

/**
 * Explosion Effect
 * Particles explode outward when scrolling into view
 */
function initExplosion() {
    const explosionSection = document.getElementById('explosion');
    const particlesContainer = document.getElementById('explosionParticles');

    if (!explosionSection || !particlesContainer) return;

    // Create explosion particles
    const particleCount = 30;
    const particles = [];

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'explosion-particle';

        const size = 10 + Math.random() * 20;
        const angle = (i / particleCount) * Math.PI * 2;
        const distance = 100 + Math.random() * 200;
        const hue = Math.random() * 60 + 350; // Red-orange range

        particle.style.cssText = `
            width: ${size}px;
            height: ${size}px;
            background: hsl(${hue % 360}, 80%, 60%);
            box-shadow: 0 0 ${size}px hsl(${hue % 360}, 80%, 60%);
        `;

        particle.dataset.angle = angle;
        particle.dataset.distance = distance;

        particles.push(particle);
        particlesContainer.appendChild(particle);
    }

    let hasExploded = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting && !hasExploded) {
                hasExploded = true;
                triggerExplosion(particles);
            }
        });
    }, { threshold: 0.5 });

    observer.observe(explosionSection);
}

function triggerExplosion(particles) {
    particles.forEach((particle, index) => {
        setTimeout(() => {
            const angle = parseFloat(particle.dataset.angle);
            const distance = parseFloat(particle.dataset.distance);

            const x = Math.cos(angle) * distance;
            const y = Math.sin(angle) * distance;

            particle.classList.add('exploded');
            particle.style.transform = `translate(${x}px, ${y}px) rotate(${angle * 180}deg)`;

            // Fade out after explosion
            setTimeout(() => {
                particle.style.opacity = '0';
            }, 500);
        }, index * 30);
    });
}

/**
 * Sticky Steps Animation
 * Reveal steps as user scrolls through sticky section
 */
function initStickySteps() {
    const steps = document.querySelectorAll('.sticky-step');
    const stickyElement = document.querySelector('.sticky-element');

    if (!steps.length || !stickyElement) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');

                // Rotate sticky element based on step
                const stepNum = parseInt(entry.target.dataset.step) || 1;
                const rotation = (stepNum - 1) * 15;
                const scale = 1 + (stepNum - 1) * 0.05;

                stickyElement.querySelector('svg').style.transform =
                    `rotate(${rotation}deg) scale(${scale})`;
            }
        });
    }, {
        rootMargin: '-30% 0px -30% 0px',
        threshold: 0.5
    });

    steps.forEach((step) => observer.observe(step));
}

/**
 * Floating Cards with Depth Effect
 * Cards move at different rates based on their data-depth attribute
 */
function initFloatingCards() {
    const cards = document.querySelectorAll('.floating-card');

    cards.forEach((card) => {
        const depth = parseFloat(card.dataset.depth) || 0.5;

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            const rotateX = (y / rect.height) * -10 * depth;
            const rotateY = (x / rect.width) * 10 * depth;

            card.style.transform = `
                perspective(1000px)
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                translateZ(20px)
            `;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });
}

/**
 * Perspective Section - 3D Effect on Scroll
 */
(function initPerspectiveSection() {
    const perspectiveSection = document.getElementById('perspective');
    const perspectiveLayers = document.querySelectorAll('.perspective-layer');

    if (!perspectiveSection) return;

    window.addEventListener('scroll', () => {
        const rect = perspectiveSection.getBoundingClientRect();
        const viewportHeight = window.innerHeight;

        if (rect.top < viewportHeight && rect.bottom > 0) {
            const progress = 1 - (rect.top / viewportHeight);

            perspectiveLayers.forEach((layer) => {
                const depth = parseFloat(layer.dataset.depth) || 1;
                const translateZ = progress * 100 * depth;
                const rotateX = progress * 5 * depth;

                layer.style.transform = `
                    translateZ(${translateZ}px)
                    rotateX(${rotateX}deg)
                `;
            });
        }
    });
})();

/**
 * Horizontal Scroll Speed Variation
 * Pauses animation on hover
 */
(function initHorizontalScroll() {
    const scrollTrack = document.querySelector('.scroll-track');

    if (!scrollTrack) return;

    // Duplicate items for seamless loop
    const items = scrollTrack.innerHTML;
    scrollTrack.innerHTML = items + items;

    // Pause on hover
    scrollTrack.addEventListener('mouseenter', () => {
        scrollTrack.style.animationPlayState = 'paused';
    });

    scrollTrack.addEventListener('mouseleave', () => {
        scrollTrack.style.animationPlayState = 'running';
    });
})();

/**
 * Performance: Reduce animations when not visible
 */
(function initPerformanceOptimization() {
    const animatedElements = document.querySelectorAll('[class*="animation"], .particle');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
            } else {
                entry.target.style.animationPlayState = 'paused';
            }
        });
    });

    animatedElements.forEach((el) => observer.observe(el));
})();

/**
 * Smooth scroll for all anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/**
 * Text Reveal Animation
 * Letters animate in one by one when section enters viewport
 */
function initTextReveal() {
    const textSection = document.getElementById('textreveal');
    const letters = document.querySelectorAll('.reveal-letter');

    if (!textSection || !letters.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                letters.forEach((letter, index) => {
                    setTimeout(() => {
                        letter.classList.add('visible');
                    }, index * 50);
                });
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });

    observer.observe(textSection);
}

/**
 * Magnetic Buttons
 * Buttons follow cursor on hover with elastic effect
 */
function initMagneticButtons() {
    const buttons = document.querySelectorAll('.magnetic-btn');

    buttons.forEach((btn) => {
        const strength = parseFloat(btn.dataset.strength) || 30;
        const span = btn.querySelector('span');

        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            const moveX = (x / rect.width) * strength;
            const moveY = (y / rect.height) * strength;

            btn.style.transform = `translate(${moveX}px, ${moveY}px)`;

            if (span) {
                span.style.transform = `translate(${moveX * 0.3}px, ${moveY * 0.3}px)`;
            }
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
            if (span) {
                span.style.transform = '';
            }
        });
    });
}

/**
 * Counter Animation
 * Numbers count up when section enters viewport
 */
function initCounterAnimation() {
    const counterSection = document.getElementById('counter');
    const counters = document.querySelectorAll('.counter-number');
    const fills = document.querySelectorAll('.counter-fill');

    if (!counterSection) return;

    let hasAnimated = false;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting && !hasAnimated) {
                hasAnimated = true;

                counters.forEach((counter) => {
                    const target = parseInt(counter.dataset.target) || 0;
                    const duration = 2000;
                    const startTime = performance.now();

                    function updateCounter(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);

                        // Easing function
                        const easeOut = 1 - Math.pow(1 - progress, 3);
                        const current = Math.floor(easeOut * target);

                        counter.textContent = current.toLocaleString();

                        if (progress < 1) {
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target.toLocaleString();
                        }
                    }

                    requestAnimationFrame(updateCounter);
                });

                // Animate progress bars
                fills.forEach((fill) => {
                    const width = fill.dataset.width || 100;
                    setTimeout(() => {
                        fill.style.width = `${width}%`;
                    }, 200);
                });
            }
        });
    }, { threshold: 0.3 });

    observer.observe(counterSection);
}

/**
 * Image Reveal
 * Images reveal with sliding overlay when scrolling
 */
function initImageReveal() {
    const images = document.querySelectorAll('.reveal-image');

    if (!images.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '0px 0px -100px 0px'
    });

    images.forEach((img) => observer.observe(img));
}

/**
 * Infinite Marquee
 * Duplicate content for seamless looping
 */
function initMarquee() {
    const marqueeContents = document.querySelectorAll('.marquee-content');

    marqueeContents.forEach((content) => {
        // Duplicate content for seamless loop
        const clone = content.cloneNode(true);
        content.parentElement.appendChild(clone);
    });

    // Pause on hover
    document.querySelectorAll('.marquee-track').forEach((track) => {
        track.addEventListener('mouseenter', () => {
            track.querySelectorAll('.marquee-content').forEach((content) => {
                content.style.animationPlayState = 'paused';
            });
        });

        track.addEventListener('mouseleave', () => {
            track.querySelectorAll('.marquee-content').forEach((content) => {
                content.style.animationPlayState = 'running';
            });
        });
    });
}

/**
 * Tilt Effect for Flip Cards
 * Add subtle tilt on mouse move
 */
(function initFlipCardsTilt() {
    const cards = document.querySelectorAll('.flip-card');

    cards.forEach((card) => {
        card.addEventListener('mousemove', (e) => {
            if (card.matches(':hover')) {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;

                const inner = card.querySelector('.flip-card-inner');
                if (inner) {
                    const rotateX = (y / rect.height) * 10;
                    const rotateY = 180 + (x / rect.width) * 10;
                    inner.style.transform = `rotateY(${rotateY}deg) rotateX(${-rotateX}deg)`;
                }
            }
        });

        card.addEventListener('mouseleave', () => {
            const inner = card.querySelector('.flip-card-inner');
            if (inner) {
                inner.style.transform = '';
            }
        });
    });
})();

/**
 * Debug: Log scroll position (uncomment for development)
 */
// window.addEventListener('scroll', () => {
//     console.log('Scroll Y:', window.scrollY);
// });
