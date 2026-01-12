/**
 * abego Steuerberatung - JavaScript
 * Dezente Animationen fuer professionelle Branche
 */

document.addEventListener('DOMContentLoaded', () => {
    initHeader();
    initMobileMenu();
    initScrollAnimations();
    initCounters();
    initStagger();
    initCalculatorAnimation();
});

/**
 * Header Scroll Effect
 */
function initHeader() {
    const header = document.querySelector('.header');
    if (!header) return;

    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
}

/**
 * Mobile Menu Toggle
 */
function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navList = document.querySelector('.nav-list');

    if (!menuToggle || !navList) return;

    menuToggle.addEventListener('click', () => {
        navList.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });

    // Close menu when clicking on a link
    const navLinks = navList.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navList.classList.remove('active');
            menuToggle.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav') && navList.classList.contains('active')) {
            navList.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });
}

/**
 * Scroll Animations with IntersectionObserver
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
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(el => observer.observe(el));
}

/**
 * Counter Animation
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
 */
function initStagger() {
    document.querySelectorAll('[data-stagger]').forEach(container => {
        const children = container.children;
        Array.from(children).forEach((child, i) => {
            child.style.transitionDelay = `${i * 0.1}s`;
        });
    });
}

/**
 * Calculator Unique Element Animation
 */
function initCalculatorAnimation() {
    const calculator = document.querySelector('.unique-element.calculator-element');
    if (!calculator) return;

    const calcNumber = calculator.querySelector('.calc-number');
    const targetNumber = 12847;
    let isAnimated = false;

    // Animate bars and number on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !isAnimated) {
                isAnimated = true;
                calculator.classList.add('animate');

                // Animate the display number
                animateDisplayNumber(calcNumber, targetNumber);
            }
        });
    }, { threshold: 0.3 });

    observer.observe(calculator);

    // Button click effects
    const buttons = calculator.querySelectorAll('.calc-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Visual feedback
            btn.style.transform = 'scale(0.95)';
            setTimeout(() => {
                btn.style.transform = '';
            }, 100);

            // Randomize display number
            if (calcNumber) {
                const randomNumber = Math.floor(Math.random() * 50000);
                animateDisplayNumber(calcNumber, randomNumber);
            }
        });
    });
}

function animateDisplayNumber(element, target) {
    if (!element) return;

    const duration = 1500;
    const start = performance.now();
    const startValue = parseInt(element.textContent) || 0;

    function update(currentTime) {
        const elapsed = currentTime - start;
        const progress = Math.min(elapsed / duration, 1);

        const eased = 1 - Math.pow(2, -10 * progress);
        const current = Math.floor(startValue + (target - startValue) * eased);

        element.textContent = current.toLocaleString('de-DE');

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = target.toLocaleString('de-DE');
        }
    }

    requestAnimationFrame(update);
}

/**
 * Smooth scroll for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});
