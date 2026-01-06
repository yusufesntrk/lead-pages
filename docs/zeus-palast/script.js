/**
 * Zeus Palast - JavaScript
 * Griechisches Restaurant in Offenburg
 */

(function() {
    'use strict';

    // ================================
    // DOM Elements
    // ================================
    const header = document.getElementById('header');
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav__link');
    const todayHours = document.getElementById('today-hours');
    const revealElements = document.querySelectorAll('.reveal');

    // ================================
    // Mobile Navigation
    // ================================
    function toggleMobileMenu() {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    }

    function closeMobileMenu() {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (navToggle) {
        navToggle.addEventListener('click', toggleMobileMenu);
    }

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            closeMobileMenu();
        });
    });

    // Close menu on click outside
    document.addEventListener('click', (e) => {
        if (navMenu && navMenu.classList.contains('active')) {
            if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
                closeMobileMenu();
            }
        }
    });

    // Close menu on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navMenu && navMenu.classList.contains('active')) {
            closeMobileMenu();
        }
    });

    // ================================
    // Sticky Header
    // ================================
    function handleScroll() {
        if (header) {
            if (window.scrollY > 100) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Initial check

    // ================================
    // Today's Opening Hours
    // ================================
    function updateTodayHours() {
        if (!todayHours) return;

        const now = new Date();
        const day = now.getDay(); // 0 = Sunday, 1 = Monday, etc.

        const hours = {
            0: '11:30 - 14:00 & 17:30 - 22:30', // Sunday
            1: '11:30 - 14:00 & 17:30 - 22:30', // Monday
            2: 'Ruhetag', // Tuesday
            3: '11:30 - 14:00 & 17:30 - 22:30', // Wednesday
            4: '11:30 - 14:00 & 17:30 - 22:30', // Thursday
            5: '11:30 - 14:00 & 17:30 - 22:30', // Friday
            6: '11:30 - 14:00 & 17:30 - 22:30'  // Saturday
        };

        todayHours.textContent = hours[day];

        // Update label if closed
        const label = todayHours.previousElementSibling;
        if (label && day === 2) {
            label.textContent = 'Heute';
            todayHours.style.color = '#E94F1D';
        }
    }

    updateTodayHours();

    // ================================
    // Smooth Scroll
    // ================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ================================
    // Reveal on Scroll
    // ================================
    function revealOnScroll() {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;

            if (elementTop < windowHeight - revealPoint) {
                element.classList.add('active');
            }
        });
    }

    // Use Intersection Observer for better performance
    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(element => {
            revealObserver.observe(element);
        });
    } else {
        // Fallback for older browsers
        window.addEventListener('scroll', revealOnScroll, { passive: true });
        revealOnScroll(); // Initial check
    }

    // ================================
    // Lazy Loading Images
    // ================================
    if ('loading' in HTMLImageElement.prototype) {
        // Browser supports native lazy loading
        document.querySelectorAll('img[loading="lazy"]').forEach(img => {
            img.src = img.dataset.src || img.src;
        });
    } else {
        // Fallback with Intersection Observer
        const lazyImages = document.querySelectorAll('img[loading="lazy"]');

        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src || img.src;
                        imageObserver.unobserve(img);
                    }
                });
            });

            lazyImages.forEach(img => imageObserver.observe(img));
        }
    }

    // ================================
    // Preload critical resources
    // ================================
    function preloadCriticalResources() {
        const criticalImages = [
            'assets/logo.svg',
            'assets/biergarten.jpg'
        ];

        criticalImages.forEach(src => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'image';
            link.href = src;
            document.head.appendChild(link);
        });
    }

    // Only preload on faster connections
    if ('connection' in navigator) {
        const connection = navigator.connection;
        if (connection && !connection.saveData && connection.effectiveType !== '2g') {
            preloadCriticalResources();
        }
    }

    // ================================
    // Handle reduced motion preference
    // ================================
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    function handleReducedMotion() {
        if (prefersReducedMotion.matches) {
            // Disable animations for users who prefer reduced motion
            document.documentElement.style.setProperty('--transition-fast', '0s');
            document.documentElement.style.setProperty('--transition-base', '0s');
            document.documentElement.style.setProperty('--transition-slow', '0s');

            // Immediately show all reveal elements
            revealElements.forEach(element => {
                element.classList.add('active');
                element.style.transition = 'none';
            });
        }
    }

    handleReducedMotion();
    prefersReducedMotion.addEventListener('change', handleReducedMotion);

    // ================================
    // Active navigation link highlighting
    // ================================
    function updateActiveNavLink() {
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';

        navLinks.forEach(link => {
            link.classList.remove('active');
            const linkHref = link.getAttribute('href');

            if (linkHref === currentPage ||
                (currentPage === '' && linkHref === 'index.html') ||
                (currentPage === 'index.html' && linkHref === 'index.html')) {
                link.classList.add('active');
            }
        });
    }

    updateActiveNavLink();

    // ================================
    // Phone number click tracking (optional)
    // ================================
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
        link.addEventListener('click', function() {
            // You can add analytics tracking here
            console.log('Phone number clicked:', this.href);
        });
    });

    // ================================
    // Lightbox for Menu Gallery
    // ================================
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxClose = document.querySelector('.lightbox__close');
    const lightboxPrev = document.querySelector('.lightbox__nav--prev');
    const lightboxNext = document.querySelector('.lightbox__nav--next');
    const menuPages = document.querySelectorAll('.menu-page');

    let currentImageIndex = 0;
    const menuImages = [];

    // Collect all menu images
    menuPages.forEach((page, index) => {
        const img = page.querySelector('img');
        if (img) {
            menuImages.push({
                src: img.src,
                alt: img.alt
            });

            page.addEventListener('click', () => {
                openLightbox(index);
            });
        }
    });

    function openLightbox(index) {
        if (!lightbox || menuImages.length === 0) return;

        currentImageIndex = index;
        updateLightboxImage();
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        if (!lightbox) return;

        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }

    function updateLightboxImage() {
        if (!lightboxImage || menuImages.length === 0) return;

        const image = menuImages[currentImageIndex];
        lightboxImage.src = image.src;
        lightboxImage.alt = image.alt;
    }

    function showPreviousImage() {
        currentImageIndex = (currentImageIndex - 1 + menuImages.length) % menuImages.length;
        updateLightboxImage();
    }

    function showNextImage() {
        currentImageIndex = (currentImageIndex + 1) % menuImages.length;
        updateLightboxImage();
    }

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
    }

    if (lightboxPrev) {
        lightboxPrev.addEventListener('click', showPreviousImage);
    }

    if (lightboxNext) {
        lightboxNext.addEventListener('click', showNextImage);
    }

    // Close lightbox on background click
    if (lightbox) {
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });
    }

    // Keyboard navigation for lightbox
    document.addEventListener('keydown', (e) => {
        if (!lightbox || !lightbox.classList.contains('active')) return;

        switch (e.key) {
            case 'Escape':
                closeLightbox();
                break;
            case 'ArrowLeft':
                showPreviousImage();
                break;
            case 'ArrowRight':
                showNextImage();
                break;
        }
    });

    // ================================
    // Console greeting
    // ================================
    console.log(
        '%c Zeus Palast %c Griechische Spezialitäten in Offenburg',
        'background: #C8943D; color: white; padding: 5px 10px; border-radius: 3px 0 0 3px; font-weight: bold;',
        'background: #6B4423; color: white; padding: 5px 10px; border-radius: 0 3px 3px 0;'
    );

})();
