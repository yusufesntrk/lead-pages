/**
 * SCHÄTZLE & PARTNER mbB - Website JavaScript
 * Dezente Animationen für seriöse Steuerberatung
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all modules
    initHeader();
    initMobileMenu();
    initScrollAnimations();
    initSmoothScroll();
});

/**
 * Header Scroll Effect
 * Adds shadow and reduces height on scroll
 */
function initHeader() {
    const header = document.getElementById('header');
    if (!header) return;

    let lastScroll = 0;
    const scrollThreshold = 50;

    function handleScroll() {
        const currentScroll = window.pageYOffset;

        if (currentScroll > scrollThreshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    }

    // Throttle scroll events for performance
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                handleScroll();
                ticking = false;
            });
            ticking = true;
        }
    });

    // Initial check
    handleScroll();
}

/**
 * Mobile Menu Toggle
 * Opens/closes mobile navigation
 */
function initMobileMenu() {
    const menuToggle = document.getElementById('menuToggle');
    const nav = document.getElementById('nav');
    const body = document.body;

    if (!menuToggle || !nav) return;

    menuToggle.addEventListener('click', function() {
        this.classList.toggle('active');
        nav.classList.toggle('open');
        body.classList.toggle('menu-open');
    });

    // Close menu when clicking on a link
    const navLinks = nav.querySelectorAll('.nav__link');
    navLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            menuToggle.classList.remove('active');
            nav.classList.remove('open');
            body.classList.remove('menu-open');
        });
    });

    // Close menu on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && nav.classList.contains('open')) {
            menuToggle.classList.remove('active');
            nav.classList.remove('open');
            body.classList.remove('menu-open');
        }
    });
}

/**
 * Scroll Animations
 * Fade-in elements when they enter viewport
 * Dezent und professionell
 */
function initScrollAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');

    if (!fadeElements.length) return;

    // Check if IntersectionObserver is supported
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    // Add slight delay for staggered effect
                    const delay = entry.target.dataset.delay || 0;
                    setTimeout(function() {
                        entry.target.classList.add('visible');
                    }, delay);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Add staggered delays for grid items
        fadeElements.forEach(function(el, index) {
            // Check if element is in a grid
            const parent = el.parentElement;
            if (parent && (
                parent.classList.contains('trust__grid') ||
                parent.classList.contains('services__grid') ||
                parent.classList.contains('team__grid') ||
                parent.classList.contains('why-us__grid') ||
                parent.classList.contains('locations__grid')
            )) {
                const siblings = Array.from(parent.querySelectorAll('.fade-in'));
                const siblingIndex = siblings.indexOf(el);
                el.dataset.delay = siblingIndex * 100;
            }

            // Make elements visible immediately if already in viewport on page load
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                el.classList.add('visible');
            } else {
                observer.observe(el);
            }
        });
    } else {
        // Fallback: show all elements immediately
        fadeElements.forEach(function(el) {
            el.classList.add('visible');
        });
    }
}

/**
 * Smooth Scroll
 * Smooth scrolling for anchor links
 */
function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Skip if it's just "#"
            if (href === '#') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();

                const headerHeight = document.getElementById('header').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Active Navigation State
 * Highlights current page in navigation
 */
(function() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav__link');

    navLinks.forEach(function(link) {
        const href = link.getAttribute('href');
        if (href === currentPage) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
})();

/**
 * Prevent body scroll when mobile menu is open
 */
(function() {
    const style = document.createElement('style');
    style.textContent = `
        body.menu-open {
            overflow: hidden;
        }
    `;
    document.head.appendChild(style);
})();

/**
 * Trust Numbers Animation
 * Animate numbers counting up when visible
 */
function initTrustNumbers() {
    const trustNumbers = document.querySelectorAll('.trust__number');

    if (!trustNumbers.length || !('IntersectionObserver' in window)) return;

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                animateNumber(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    trustNumbers.forEach(function(el) {
        observer.observe(el);
    });
}

function animateNumber(element) {
    const text = element.textContent;
    const hasPlus = text.includes('+');
    const hasPercent = text.includes('%');
    const number = parseInt(text.replace(/[^0-9]/g, ''));

    if (isNaN(number)) return;

    let current = 0;
    const duration = 1500;
    const step = number / (duration / 16);

    function update() {
        current += step;
        if (current < number) {
            element.textContent = Math.floor(current) + (hasPlus ? '+' : '') + (hasPercent ? '%' : '');
            requestAnimationFrame(update);
        } else {
            element.textContent = text; // Reset to original
        }
    }

    element.textContent = '0' + (hasPlus ? '+' : '') + (hasPercent ? '%' : '');
    requestAnimationFrame(update);
}

// Initialize trust numbers animation
document.addEventListener('DOMContentLoaded', initTrustNumbers);
