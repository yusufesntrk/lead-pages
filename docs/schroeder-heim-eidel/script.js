/**
 * Schroeder-Heim & Eidel - Main JavaScript
 * Mobile Navigation, Smooth Scroll & Dezente Animationen
 */

(function() {
    'use strict';

    // ==========================================================================
    // Mobile Navigation Toggle
    // ==========================================================================

    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navMenu.classList.toggle('active');

            // Toggle aria-expanded for accessibility
            const isExpanded = this.classList.contains('active');
            this.setAttribute('aria-expanded', isExpanded);
        });

        // Close menu when clicking on a nav link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ==========================================================================
    // Smooth Scroll for Anchor Links
    // ==========================================================================

    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');

            // Skip if it's just "#"
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                e.preventDefault();

                // Account for fixed header
                const header = document.querySelector('.header');
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ==========================================================================
    // Dezente Scroll Reveal Animationen
    // ==========================================================================

    // Elemente, die animiert werden sollen
    const revealElements = document.querySelectorAll(
        '.trust-item, .service-card, .feature-box, .team-card, .rating-card, .about-text'
    );

    if (revealElements.length > 0 && 'IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    // Dezente Fade-in Animation
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateY(20px)';
                    entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';

                    setTimeout(function() {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 100);

                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        });

        revealElements.forEach(function(element) {
            revealObserver.observe(element);
        });
    }

    // ==========================================================================
    // Header Scroll Effect (dezent)
    // ==========================================================================

    const header = document.querySelector('.header');
    let lastScrollY = window.scrollY;

    if (header) {
        window.addEventListener('scroll', function() {
            const currentScrollY = window.scrollY;

            // Dezente Shadow-Verstärkung beim Scrollen
            if (currentScrollY > 10) {
                header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
            } else {
                header.style.boxShadow = '0 1px 3px rgba(0, 0, 0, 0.08)';
            }

            lastScrollY = currentScrollY;
        }, { passive: true });
    }

    // ==========================================================================
    // Telefonnummer und E-Mail Tracking (optional)
    // ==========================================================================

    // Optional: Analytics-Events für Telefon-Klicks
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
    phoneLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Hier könnte ein Analytics-Event gefeuert werden
            console.log('Telefon-Link geklickt');
        });
    });

    // Optional: Analytics-Events für E-Mail-Klicks
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');
    emailLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Hier könnte ein Analytics-Event gefeuert werden
            console.log('E-Mail-Link geklickt');
        });
    });

})();
