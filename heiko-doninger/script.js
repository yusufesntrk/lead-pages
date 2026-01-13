/* ========================================
   HEIKO DONINGER - STEUERBERATER
   JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollAnimations();
    initStagger();
    initHeaderScroll();
    initCalculator();
});

/* ========================================
   NAVIGATION
   ======================================== */
function initNavigation() {
    const navToggle = document.querySelector('.nav-toggle');
    const navList = document.querySelector('.nav-list');

    if (!navToggle || !navList) return;

    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navList.classList.toggle('active');
        navToggle.setAttribute('aria-expanded', navList.classList.contains('active'));
    });

    // Close menu on link click
    const navLinks = navList.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navList.classList.remove('active');
            navToggle.setAttribute('aria-expanded', 'false');
        });
    });

    // Close menu on outside click
    document.addEventListener('click', (e) => {
        if (!navToggle.contains(e.target) && !navList.contains(e.target)) {
            navToggle.classList.remove('active');
            navList.classList.remove('active');
            navToggle.setAttribute('aria-expanded', 'false');
        }
    });
}

/* ========================================
   SCROLL ANIMATIONS
   ======================================== */
function initScrollAnimations() {
    const elements = document.querySelectorAll('[data-scroll]');

    if (!elements.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(el => observer.observe(el));
}

/* ========================================
   STAGGER ANIMATION
   ======================================== */
function initStagger() {
    const containers = document.querySelectorAll('[data-stagger]');

    containers.forEach(container => {
        const children = container.children;
        Array.from(children).forEach((child, i) => {
            child.style.transitionDelay = `${i * 0.1}s`;
        });
    });
}

/* ========================================
   HEADER SCROLL
   ======================================== */
function initHeaderScroll() {
    const header = document.querySelector('.header');
    if (!header) return;

    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    }, { passive: true });
}

/* ========================================
   CALCULATOR INTERACTION
   ======================================== */
function initCalculator() {
    const calculator = document.querySelector('.calculator-svg');
    if (!calculator) return;

    const screenNumber = calculator.querySelector('.screen-number');
    const buttons = calculator.querySelectorAll('.button-group');

    let currentValue = '0,00';
    let isNewNumber = true;

    // Sample values for animation
    const sampleValues = [
        '1.250,00',
        '4.800,50',
        '12.375,00',
        '850,25',
        '3.999,99',
        '7.450,00',
        '15.200,00',
        '2.875,50'
    ];

    // Animate on hover with random value
    calculator.addEventListener('mouseenter', () => {
        if (screenNumber) {
            const randomValue = sampleValues[Math.floor(Math.random() * sampleValues.length)];
            animateValue(screenNumber, currentValue, randomValue);
            currentValue = randomValue;
        }
    });

    // Button click animation
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.stopPropagation();

            // Visual feedback
            const rect = button.querySelector('rect');
            if (rect) {
                rect.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    rect.style.transform = 'scale(1)';
                }, 100);
            }

            // Update display for number buttons
            const value = button.dataset.value;
            if (value && screenNumber) {
                if (button.classList.contains('number')) {
                    if (isNewNumber) {
                        currentValue = value + ',00';
                        isNewNumber = false;
                    } else {
                        currentValue = currentValue.replace(',00', '') + value + ',00';
                    }
                } else if (value === 'C') {
                    currentValue = '0,00';
                    isNewNumber = true;
                } else {
                    // Operator pressed - simulate calculation
                    const randomResult = sampleValues[Math.floor(Math.random() * sampleValues.length)];
                    animateValue(screenNumber, currentValue, randomResult);
                    currentValue = randomResult;
                    isNewNumber = true;
                    return;
                }

                screenNumber.textContent = currentValue;
            }
        });

        // Keyboard accessibility
        button.setAttribute('tabindex', '0');
        button.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                button.click();
            }
        });
    });
}

/* ========================================
   HELPER: ANIMATE VALUE
   ======================================== */
function animateValue(element, from, to) {
    const duration = 500;
    const steps = 20;
    const stepDuration = duration / steps;

    let step = 0;

    const interval = setInterval(() => {
        step++;

        if (step < steps) {
            // Random intermediate value
            const randomDigits = Math.floor(Math.random() * 99999);
            element.textContent = randomDigits.toLocaleString('de-DE', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });
        } else {
            element.textContent = to;
            clearInterval(interval);
        }
    }, stepDuration);
}

/* ========================================
   SMOOTH SCROLL
   ======================================== */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        const target = document.querySelector(href);

        if (target) {
            const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});
