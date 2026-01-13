/**
 * Dietmar Felchner Steuerberater - Website JavaScript
 * Dezente Animationen passend für Steuerberater-Branche
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollAnimations();
    initStagger();
    initSmoothScroll();
});

/**
 * Navigation - Scroll-Effekt und Mobile Menu
 */
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    // Scroll-Effekt
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // Mobile Menu Toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Schliesse Menu bei Klick auf Link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }
}

/**
 * Scroll-Animationen mit IntersectionObserver
 * Dezent und professionell
 */
function initScrollAnimations() {
    const elements = document.querySelectorAll('[data-scroll]');

    if (elements.length === 0) return;

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
 * Staggered Animation fuer Kinder-Elemente
 */
function initStagger() {
    const containers = document.querySelectorAll('[data-stagger]');

    containers.forEach(container => {
        const children = container.children;
        Array.from(children).forEach((child, i) => {
            child.style.transitionDelay = `${i * 0.1}s`;
        });
    });
}

/**
 * Smooth Scroll fuer Anker-Links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href === '#') return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();

                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navbarHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Formular-Handling (fuer Kontaktseite)
 */
function initContactForm() {
    const form = document.querySelector('.contact-form');

    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Einfache Validierung
        const requiredFields = form.querySelectorAll('[required]');
        let isValid = true;

        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                field.classList.add('error');
            } else {
                field.classList.remove('error');
            }
        });

        if (isValid) {
            // Hier koennte eine echte Formularverarbeitung stattfinden
            const button = form.querySelector('button[type="submit"]');
            const originalText = button.textContent;

            button.textContent = 'Nachricht gesendet!';
            button.disabled = true;

            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
                form.reset();
            }, 3000);
        }
    });
}

// Initialisiere Kontaktformular wenn vorhanden
document.addEventListener('DOMContentLoaded', initContactForm);
