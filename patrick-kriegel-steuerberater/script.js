/**
 * Patrick Kriegel Steuerberater - Website Scripts
 * Dezente Animationen passend für eine seriöse Steuerberatung
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // ============================================
    // Header Scroll Effect
    // ============================================
    const header = document.getElementById('header');
    let lastScroll = 0;

    function handleScroll() {
        const currentScroll = window.pageYOffset;

        // Add shadow when scrolled
        if (currentScroll > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    }

    window.addEventListener('scroll', handleScroll, { passive: true });

    // ============================================
    // Mobile Navigation
    // ============================================
    const navToggle = document.getElementById('navToggle');
    const nav = document.getElementById('nav');

    if (navToggle && nav) {
        navToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            nav.classList.toggle('active');
            document.body.classList.toggle('nav-open');
        });

        // Close nav when clicking on a link
        const navLinks = nav.querySelectorAll('.nav__link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.classList.remove('nav-open');
            });
        });

        // Close nav when clicking outside
        document.addEventListener('click', function(e) {
            if (nav.classList.contains('active') &&
                !nav.contains(e.target) &&
                !navToggle.contains(e.target)) {
                navToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.classList.remove('nav-open');
            }
        });
    }

    // ============================================
    // Fade In Animations (Dezent)
    // ============================================
    const fadeElements = document.querySelectorAll('.fade-in');

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    const fadeObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                // Small delay for staggered effect
                const delay = entry.target.dataset.delay || 0;
                setTimeout(function() {
                    entry.target.classList.add('visible');
                }, delay);
                fadeObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    fadeElements.forEach(function(el, index) {
        // Add staggered delay for grid items
        if (el.closest('.services-grid') ||
            el.closest('.values-grid') ||
            el.closest('.testimonials-grid')) {
            el.dataset.delay = (index % 3) * 100;
        }
        fadeObserver.observe(el);
    });

    // ============================================
    // Smooth Scroll for Anchor Links
    // ============================================
    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerHeight = header.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============================================
    // Active Navigation State
    // ============================================
    const sections = document.querySelectorAll('section[id]');
    const navItems = document.querySelectorAll('.nav__link');

    function setActiveNav() {
        const scrollPosition = window.pageYOffset + 150;

        sections.forEach(function(section) {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navItems.forEach(function(item) {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === '#' + sectionId) {
                        item.classList.add('active');
                    }
                });
            }
        });
    }

    window.addEventListener('scroll', setActiveNav, { passive: true });

    // ============================================
    // Phone Number Click Tracking (Optional)
    // ============================================
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

    phoneLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Could add analytics tracking here
            console.log('Phone link clicked:', this.href);
        });
    });

    // ============================================
    // Email Link Protection
    // ============================================
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');

    emailLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Could add analytics tracking here
            console.log('Email link clicked:', this.href);
        });
    });

    // ============================================
    // Scroll to Top on Hero CTA
    // ============================================
    const heroScroll = document.querySelector('.hero__scroll');

    if (heroScroll) {
        heroScroll.addEventListener('click', function() {
            const nextSection = document.querySelector('.trust') || document.querySelector('.section');
            if (nextSection) {
                const headerHeight = header.offsetHeight;
                const targetPosition = nextSection.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    }

    // ============================================
    // Preload Critical Assets
    // ============================================
    function preloadImage(src) {
        const img = new Image();
        img.src = src;
    }

    // Preload logo
    preloadImage('assets/logo.svg');

    // ============================================
    // Reduce Motion for Accessibility
    // ============================================
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    if (prefersReducedMotion.matches) {
        // Disable animations for users who prefer reduced motion
        fadeElements.forEach(function(el) {
            el.classList.add('visible');
        });
    }

    // ============================================
    // Console Welcome Message
    // ============================================
    console.log('%cPatrick Kriegel Steuerberater', 'color: #1a5f3c; font-size: 24px; font-weight: bold;');
    console.log('%cWir Steuern! - Aktiv. Individuell. Smart.', 'color: #4a4a4a; font-size: 14px;');
    console.log('%cWebsite erstellt mit moderner Technologie', 'color: #6b6b6b; font-size: 12px;');
});
