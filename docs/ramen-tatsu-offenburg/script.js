/**
 * Ramen Tatsu Offenburg - Main JavaScript
 * Mobile Navigation, Smooth Scroll, Reveal Animations
 */

(function() {
    'use strict';

    // ==========================================================================
    // Mobile Navigation
    // ==========================================================================
    const navToggle = document.querySelector('.nav__toggle');
    const navMenu = document.querySelector('.nav__menu');
    const navLinks = document.querySelectorAll('.nav__link');
    const body = document.body;

    function toggleMenu() {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    }

    function closeMenu() {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        body.style.overflow = '';
    }

    if (navToggle) {
        navToggle.addEventListener('click', toggleMenu);
    }

    // Close menu when clicking on a link
    navLinks.forEach(function(link) {
        link.addEventListener('click', closeMenu);
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(e) {
        if (navMenu.classList.contains('active') &&
            !navMenu.contains(e.target) &&
            !navToggle.contains(e.target)) {
            closeMenu();
        }
    });

    // Close menu on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
            closeMenu();
        }
    });

    // ==========================================================================
    // Header Scroll Effect
    // ==========================================================================
    const header = document.querySelector('.header');
    let lastScrollY = 0;
    let ticking = false;

    function updateHeader() {
        const scrollY = window.scrollY;

        if (scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScrollY = scrollY;
        ticking = false;
    }

    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(updateHeader);
            ticking = true;
        }
    });

    // ==========================================================================
    // Smooth Scroll for Anchor Links
    // ==========================================================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');

            if (targetId === '#') return;

            const target = document.querySelector(targetId);

            if (target) {
                e.preventDefault();

                const headerHeight = header.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.scrollY - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });

                closeMenu();
            }
        });
    });

    // ==========================================================================
    // Reveal on Scroll Animation
    // ==========================================================================
    const revealElements = document.querySelectorAll('.reveal');

    function revealOnScroll() {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        revealElements.forEach(function(element) {
            const elementTop = element.getBoundingClientRect().top;

            if (elementTop < windowHeight - revealPoint) {
                element.classList.add('active');
            }
        });
    }

    // Initial check for elements in view
    revealOnScroll();

    // Throttled scroll handler
    let revealTicking = false;

    window.addEventListener('scroll', function() {
        if (!revealTicking) {
            window.requestAnimationFrame(function() {
                revealOnScroll();
                revealTicking = false;
            });
            revealTicking = true;
        }
    });

    // ==========================================================================
    // Horizontal Scroll Enhancement for Experience Section
    // ==========================================================================
    const experienceScroll = document.querySelector('.experience__scroll');

    if (experienceScroll) {
        // Add grab cursor styling
        experienceScroll.style.cursor = 'grab';

        let isDown = false;
        let startX;
        let scrollLeft;

        experienceScroll.addEventListener('mousedown', function(e) {
            isDown = true;
            experienceScroll.style.cursor = 'grabbing';
            startX = e.pageX - experienceScroll.offsetLeft;
            scrollLeft = experienceScroll.scrollLeft;
        });

        experienceScroll.addEventListener('mouseleave', function() {
            isDown = false;
            experienceScroll.style.cursor = 'grab';
        });

        experienceScroll.addEventListener('mouseup', function() {
            isDown = false;
            experienceScroll.style.cursor = 'grab';
        });

        experienceScroll.addEventListener('mousemove', function(e) {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - experienceScroll.offsetLeft;
            const walk = (x - startX) * 2;
            experienceScroll.scrollLeft = scrollLeft - walk;
        });
    }

    // ==========================================================================
    // Lazy Load Images (Intersection Observer)
    // ==========================================================================
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;

                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }

                    if (img.dataset.srcset) {
                        img.srcset = img.dataset.srcset;
                        img.removeAttribute('data-srcset');
                    }

                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px 0px',
            threshold: 0.01
        });

        document.querySelectorAll('img[data-src]').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // ==========================================================================
    // Form Validation (if contact form exists)
    // ==========================================================================
    const forms = document.querySelectorAll('form');

    forms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(function(field) {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });

            // Email validation
            const emailField = form.querySelector('input[type="email"]');
            if (emailField && emailField.value) {
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailPattern.test(emailField.value)) {
                    isValid = false;
                    emailField.classList.add('error');
                }
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    // ==========================================================================
    // Active Navigation State
    // ==========================================================================
    function setActiveNavLink() {
        const currentPath = window.location.pathname.split('/').pop() || 'index.html';

        navLinks.forEach(function(link) {
            const href = link.getAttribute('href');

            if (href === currentPath || (href === 'index.html' && currentPath === '')) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }

    setActiveNavLink();

    // ==========================================================================
    // Performance: Reduce animations for users who prefer reduced motion
    // ==========================================================================
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        document.documentElement.style.setProperty('--transition-slow', '0s');

        revealElements.forEach(function(el) {
            el.classList.add('active');
        });
    }

    // ==========================================================================
    // Console Easter Egg
    // ==========================================================================
    console.log('%c🍜 Ramen Tatsu Offenburg', 'font-size: 20px; font-weight: bold; color: #C41E3A;');
    console.log('%cAuthentische japanische Ramen im Herzen von Offenburg.', 'color: #4A4A4A;');

})();
