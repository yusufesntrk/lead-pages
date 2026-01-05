/**
 * Donna Selvatica - JavaScript
 * Mobile Navigation, Smooth Scroll, Reveal Animations
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav__toggle');
    const navMenu = document.querySelector('.nav__menu');
    const navLinks = document.querySelectorAll('.nav__link');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            const isOpen = navMenu.classList.contains('active');

            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            navToggle.setAttribute('aria-expanded', !isOpen);

            // Prevent body scroll when menu is open
            document.body.style.overflow = isOpen ? '' : 'hidden';
        });

        // Close menu when clicking on a link
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
    }

    // Smooth Scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');

            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                e.preventDefault();

                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Reveal on Scroll Animation
    const revealElements = document.querySelectorAll('.reveal');

    function revealOnScroll() {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        revealElements.forEach(function(element) {
            const elementTop = element.getBoundingClientRect().top;

            if (elementTop < windowHeight - revealPoint) {
                element.classList.add('visible');
            }
        });
    }

    // Initial check for elements already in view
    revealOnScroll();

    // Throttle scroll event for performance
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(function() {
            revealOnScroll();
        });
    });

    // Header background on scroll
    const header = document.querySelector('.header');

    function updateHeaderOnScroll() {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.08)';
        }
    }

    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(function() {
            updateHeaderOnScroll();
        });
    });

    // Lazy loading for images (fallback for older browsers)
    if ('loading' in HTMLImageElement.prototype) {
        // Browser supports native lazy loading
        const lazyImages = document.querySelectorAll('img[loading="lazy"]');
        lazyImages.forEach(function(img) {
            img.src = img.src;
        });
    } else {
        // Fallback for older browsers
        const lazyImages = document.querySelectorAll('img[loading="lazy"]');

        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.src;
                    observer.unobserve(img);
                }
            });
        });

        lazyImages.forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // Add animation delay to grid items
    function addStaggeredAnimation() {
        const grids = document.querySelectorAll('.speisen__grid, .ambiente__grid, .bewertungen__grid');

        grids.forEach(function(grid) {
            const items = grid.querySelectorAll('.reveal');
            items.forEach(function(item, index) {
                item.style.transitionDelay = (index * 0.1) + 's';
            });
        });
    }

    addStaggeredAnimation();
});
