/**
 * Schröder-Heim & Eidel - Website Scripts
 * Mobile Navigation, Smooth Scroll, Reveal Animations
 */

(function() {
    'use strict';

    // DOM Elements
    const header = document.querySelector('.header');
    const navToggle = document.getElementById('nav-toggle');
    const nav = document.getElementById('nav');

    // -------------------------------------------------------------------------
    // Mobile Navigation
    // -------------------------------------------------------------------------
    function initMobileNav() {
        if (!navToggle || !nav) return;

        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            nav.classList.toggle('active');
            document.body.classList.toggle('nav-open');
        });

        // Close menu when clicking on a link
        const navLinks = nav.querySelectorAll('.nav-link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.classList.remove('nav-open');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!nav.contains(e.target) && !navToggle.contains(e.target)) {
                navToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.classList.remove('nav-open');
            }
        });
    }

    // -------------------------------------------------------------------------
    // Header Scroll Effect
    // -------------------------------------------------------------------------
    function initHeaderScroll() {
        if (!header) return;

        let lastScroll = 0;

        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;

            // Add scrolled class when scrolled past 50px
            if (currentScroll > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }

            lastScroll = currentScroll;
        }, { passive: true });
    }

    // -------------------------------------------------------------------------
    // Smooth Scroll for Anchor Links
    // -------------------------------------------------------------------------
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;

                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    const headerHeight = header ? header.offsetHeight : 0;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    // -------------------------------------------------------------------------
    // Reveal Animations on Scroll
    // -------------------------------------------------------------------------
    function initRevealAnimations() {
        // Elements to reveal
        const revealElements = document.querySelectorAll(
            '.service-card, .feature-card, .team-card, .stat-card, .trust-item, .section-header'
        );

        if (revealElements.length === 0) return;

        // Add reveal class
        revealElements.forEach(function(el) {
            el.classList.add('reveal');
        });

        // Intersection Observer for reveal
        const revealObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(function(el) {
            revealObserver.observe(el);
        });
    }

    // -------------------------------------------------------------------------
    // Staggered Animation for Grid Items
    // -------------------------------------------------------------------------
    function initStaggeredAnimations() {
        const grids = document.querySelectorAll('.services-grid, .team-grid, .trust-grid, .hero-stats');

        grids.forEach(function(grid) {
            const items = grid.children;
            Array.from(items).forEach(function(item, index) {
                item.style.transitionDelay = (index * 0.1) + 's';
            });
        });
    }

    // -------------------------------------------------------------------------
    // Phone Number Click Tracking (for analytics)
    // -------------------------------------------------------------------------
    function initPhoneTracking() {
        const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

        phoneLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                // Analytics tracking could be added here
                console.log('Phone click tracked');
            });
        });
    }

    // -------------------------------------------------------------------------
    // Active Navigation State
    // -------------------------------------------------------------------------
    function initActiveNav() {
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const navLinks = document.querySelectorAll('.nav-link');

        navLinks.forEach(function(link) {
            const href = link.getAttribute('href');
            if (href === currentPage || (currentPage === '' && href === 'index.html')) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    // -------------------------------------------------------------------------
    // Initialize All
    // -------------------------------------------------------------------------
    function init() {
        initMobileNav();
        initHeaderScroll();
        initSmoothScroll();
        initRevealAnimations();
        initStaggeredAnimations();
        initPhoneTracking();
        initActiveNav();
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
