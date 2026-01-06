/* =====================================================
   MUTTER & JÄCKL RECHTSANWÄLTE - JAVASCRIPT
   Mobile Navigation, Smooth Scroll, Reveal Animations
   ===================================================== */

document.addEventListener('DOMContentLoaded', function() {

    // =====================================================
    // Mobile Navigation Toggle
    // =====================================================
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const header = document.getElementById('header');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // =====================================================
    // Header Scroll Effect
    // =====================================================
    if (header) {
        let lastScrollY = window.scrollY;

        window.addEventListener('scroll', function() {
            const currentScrollY = window.scrollY;

            // Add/remove scrolled class
            if (currentScrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }

            lastScrollY = currentScrollY;
        }, { passive: true });
    }

    // =====================================================
    // Smooth Scroll for Anchor Links
    // =====================================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href !== '#' && href.length > 1) {
                const target = document.querySelector(href);

                if (target) {
                    e.preventDefault();

                    const headerHeight = header ? header.offsetHeight : 80;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
                    const offsetPosition = targetPosition - headerHeight - 20;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // =====================================================
    // Scroll Reveal Animation
    // =====================================================
    const revealElements = document.querySelectorAll('.reveal');

    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    // Optionally unobserve after revealing
                    // revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -80px 0px'
        });

        revealElements.forEach(function(element, index) {
            // Add staggered delay for elements
            element.style.transitionDelay = (index % 4) * 0.1 + 's';
            revealObserver.observe(element);
        });
    }

    // =====================================================
    // Active Navigation Link Highlighting
    // =====================================================
    const navLinks = document.querySelectorAll('.nav__link');
    const sections = document.querySelectorAll('section[id]');

    if (navLinks.length > 0 && sections.length > 0) {
        const highlightNavLink = function() {
            const scrollY = window.pageYOffset;
            const headerHeight = header ? header.offsetHeight : 80;

            sections.forEach(function(section) {
                const sectionTop = section.offsetTop - headerHeight - 100;
                const sectionBottom = sectionTop + section.offsetHeight;
                const sectionId = section.getAttribute('id');

                if (scrollY >= sectionTop && scrollY < sectionBottom) {
                    navLinks.forEach(function(link) {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === '#' + sectionId) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        };

        window.addEventListener('scroll', highlightNavLink, { passive: true });
    }

    // =====================================================
    // Lazy Loading for Images (native fallback)
    // =====================================================
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');

    if ('loading' in HTMLImageElement.prototype) {
        // Browser supports native lazy loading
        lazyImages.forEach(function(img) {
            if (img.dataset.src) {
                img.src = img.dataset.src;
            }
        });
    } else {
        // Fallback for older browsers
        const lazyImageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                    }
                    lazyImageObserver.unobserve(img);
                }
            });
        });

        lazyImages.forEach(function(img) {
            lazyImageObserver.observe(img);
        });
    }

    // =====================================================
    // Phone Number Click Tracking (optional analytics)
    // =====================================================
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

    phoneLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Track phone clicks if analytics is available
            if (typeof gtag === 'function') {
                gtag('event', 'click', {
                    'event_category': 'Contact',
                    'event_label': 'Phone Call',
                    'value': 1
                });
            }
        });
    });

    // =====================================================
    // Email Link Click Tracking (optional analytics)
    // =====================================================
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');

    emailLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // Track email clicks if analytics is available
            if (typeof gtag === 'function') {
                gtag('event', 'click', {
                    'event_category': 'Contact',
                    'event_label': 'Email',
                    'value': 1
                });
            }
        });
    });

    // =====================================================
    // Keyboard Accessibility for Mobile Menu
    // =====================================================
    if (navToggle) {
        navToggle.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                navToggle.click();
            }
        });
    }

    // Escape key to close mobile menu
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navMenu && navMenu.classList.contains('active')) {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
            navToggle.focus();
        }
    });

    // =====================================================
    // Preload Critical Images
    // =====================================================
    const criticalImages = [
        'assets/logo.svg',
        'assets/logo-white.svg'
    ];

    criticalImages.forEach(function(src) {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.as = 'image';
        link.href = src;
        document.head.appendChild(link);
    });

    // =====================================================
    // Console Welcome Message
    // =====================================================
    console.log('%c⚖️ Mutter & Jäckl Rechtsanwälte', 'font-size: 20px; font-weight: bold; color: #1E3A5F;');
    console.log('%cWebsite entwickelt für Rechtsanwaltskanzlei Mutter und Jäckl', 'font-size: 12px; color: #666;');
});
