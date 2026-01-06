/**
 * Diyar's Laufsteg - JavaScript
 * Türkisches Restaurant & Café
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all components
    initMobileNav();
    initStickyHeader();
    initScrollReveal();
    initSmoothScroll();
    updateOpeningStatus();
});

/**
 * Mobile Navigation
 */
function initMobileNav() {
    const toggle = document.querySelector('.nav__toggle');
    const menu = document.querySelector('.nav__menu');
    const links = document.querySelectorAll('.nav__link');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        const isOpen = toggle.classList.contains('active');
        toggle.classList.toggle('active');
        menu.classList.toggle('active');
        toggle.setAttribute('aria-expanded', !isOpen);

        // Prevent body scroll when menu is open
        document.body.style.overflow = isOpen ? '' : 'hidden';
    });

    // Close menu when clicking a link
    links.forEach(link => {
        link.addEventListener('click', () => {
            toggle.classList.remove('active');
            menu.classList.remove('active');
            toggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!menu.contains(e.target) && !toggle.contains(e.target) && menu.classList.contains('active')) {
            toggle.classList.remove('active');
            menu.classList.remove('active');
            toggle.setAttribute('aria-expanded', 'false');
            document.body.style.overflow = '';
        }
    });
}

/**
 * Sticky Header with scroll effect
 */
function initStickyHeader() {
    const header = document.querySelector('.header');
    if (!header) return;

    let lastScroll = 0;
    const scrollThreshold = 50;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add scrolled class for visual changes
        if (currentScroll > scrollThreshold) {
            header.classList.add('header--scrolled');
        } else {
            header.classList.remove('header--scrolled');
        }

        lastScroll = currentScroll;
    }, { passive: true });
}

/**
 * Scroll Reveal Animation
 */
function initScrollReveal() {
    const reveals = document.querySelectorAll('.reveal');

    if (!reveals.length) return;

    const revealOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    const revealOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    reveals.forEach(reveal => {
        revealOnScroll.observe(reveal);
    });
}

/**
 * Smooth Scroll for anchor links
 */
function initSmoothScroll() {
    const anchors = document.querySelectorAll('a[href^="#"]');

    anchors.forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const href = anchor.getAttribute('href');

            // Skip if it's just "#"
            if (href === '#') return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Update Opening Status based on current time
 */
function updateOpeningStatus() {
    const statusElement = document.querySelector('.hero__info-item span');
    if (!statusElement || !statusElement.textContent.includes('geöffnet')) return;

    const now = new Date();
    const day = now.getDay(); // 0 = Sunday, 1 = Monday, etc.
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const currentTime = hours * 60 + minutes;

    // Opening hours
    // Mon-Thu: 08:00 - 23:00 (480 - 1380)
    // Fri-Sat: 08:00 - 01:00 (480 - 1500, where 1500 = 25*60 for next day 01:00)
    // Sun: 08:00 - 23:00 (480 - 1380)

    let openTime = 8 * 60; // 08:00
    let closeTime;
    let isOpen = false;

    if (day === 5 || day === 6) { // Friday or Saturday
        closeTime = 25 * 60; // 01:00 next day
        isOpen = currentTime >= openTime || currentTime < 60; // After 08:00 or before 01:00
    } else {
        closeTime = 23 * 60; // 23:00
        isOpen = currentTime >= openTime && currentTime < closeTime;
    }

    // Format close time for display
    const closeHour = day === 5 || day === 6 ? '01:00' : '23:00';

    // Get day name in German
    const dayNames = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
    const dayName = dayNames[day];

    if (isOpen) {
        statusElement.innerHTML = `Heute geöffnet bis ${closeHour} Uhr`;
        statusElement.closest('.hero__info-item').style.color = '#059669';
    } else {
        statusElement.innerHTML = `Heute: ${dayName} 08:00 - ${closeHour} Uhr`;
    }
}

/**
 * Helper: Debounce function for performance
 */
function debounce(func, wait = 100) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Helper: Check if element is in viewport
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
