/**
 * RECHTSANWALT RAINER STUMM - JavaScript
 * Mobile Navigation, Smooth Scroll, Reveal Animations
 */

document.addEventListener('DOMContentLoaded', function() {
    // ===================================
    // MOBILE NAVIGATION
    // ===================================
    const navToggle = document.getElementById('nav-toggle');
    const nav = document.getElementById('nav');
    const header = document.getElementById('header');

    if (navToggle && nav) {
        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            nav.classList.toggle('active');
            document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu when clicking a link
        const navLinks = nav.querySelectorAll('.nav__link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (nav.classList.contains('active') &&
                !nav.contains(e.target) &&
                !navToggle.contains(e.target)) {
                navToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // ===================================
    // HEADER SCROLL EFFECT
    // ===================================
    if (header) {
        let lastScroll = 0;

        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 50) {
                header.classList.add('header--scrolled');
            } else {
                header.classList.remove('header--scrolled');
            }

            lastScroll = currentScroll;
        });
    }

    // ===================================
    // SMOOTH SCROLL
    // ===================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href === '#') return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();

                const headerHeight = header ? header.offsetHeight : 80;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ===================================
    // SCROLL REVEAL ANIMATIONS
    // ===================================
    const revealElements = document.querySelectorAll('.reveal');

    if (revealElements.length > 0) {
        const revealOnScroll = function() {
            const windowHeight = window.innerHeight;
            const revealPoint = 100;

            revealElements.forEach(function(element) {
                const elementTop = element.getBoundingClientRect().top;

                if (elementTop < windowHeight - revealPoint) {
                    element.classList.add('active');
                }
            });
        };

        // Initial check
        revealOnScroll();

        // Check on scroll
        window.addEventListener('scroll', revealOnScroll);
    }

    // ===================================
    // HERO SCROLL INDICATOR
    // ===================================
    const heroScroll = document.querySelector('.hero__scroll');

    if (heroScroll) {
        heroScroll.addEventListener('click', function() {
            const nextSection = document.querySelector('.hero').nextElementSibling;

            if (nextSection) {
                const headerHeight = header ? header.offsetHeight : 80;
                const targetPosition = nextSection.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    }

    // ===================================
    // ACTIVE NAVIGATION STATE
    // ===================================
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav__link');

    navLinks.forEach(function(link) {
        const linkPath = link.getAttribute('href');

        if (linkPath === currentPath ||
            (currentPath === '' && linkPath === 'index.html') ||
            (currentPath === 'index.html' && linkPath === 'index.html')) {
            link.classList.add('nav__link--active');
        }
    });

    // ===================================
    // FORM HANDLING (for contact page)
    // ===================================
    const contactForm = document.querySelector('.contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(contactForm);
            const data = Object.fromEntries(formData);

            // Here you would typically send the data to a server
            // For now, we'll just show a success message
            console.log('Form submitted:', data);

            // Show success message (you can customize this)
            alert('Vielen Dank für Ihre Nachricht. Wir werden uns schnellstmöglich bei Ihnen melden.');

            // Reset form
            contactForm.reset();
        });
    }

    // ===================================
    // PHONE NUMBER CLICK TRACKING
    // ===================================
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

    phoneLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Track phone clicks for analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'phone_call', {
                    'event_category': 'Contact',
                    'event_label': this.getAttribute('href')
                });
            }
        });
    });

    // ===================================
    // EMAIL LINK CLICK TRACKING
    // ===================================
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');

    emailLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Track email clicks for analytics
            if (typeof gtag !== 'undefined') {
                gtag('event', 'email_click', {
                    'event_category': 'Contact',
                    'event_label': this.getAttribute('href')
                });
            }
        });
    });

    // ===================================
    // LAZY LOADING IMAGES
    // ===================================
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img[loading="lazy"]');
        images.forEach(function(img) {
            img.src = img.dataset.src || img.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lozad.js/1.16.0/lozad.min.js';
        script.onload = function() {
            const observer = lozad();
            observer.observe();
        };
        document.body.appendChild(script);
    }

    // ===================================
    // ACCESSIBILITY: Skip to Main Content
    // ===================================
    const skipLink = document.querySelector('.skip-link');

    if (skipLink) {
        skipLink.addEventListener('click', function(e) {
            e.preventDefault();
            const main = document.querySelector('main');
            if (main) {
                main.setAttribute('tabindex', '-1');
                main.focus();
            }
        });
    }

    // ===================================
    // KEYBOARD NAVIGATION SUPPORT
    // ===================================
    document.addEventListener('keydown', function(e) {
        // Close mobile menu with Escape key
        if (e.key === 'Escape' && nav && nav.classList.contains('active')) {
            navToggle.classList.remove('active');
            nav.classList.remove('active');
            document.body.style.overflow = '';
            navToggle.focus();
        }
    });
});
