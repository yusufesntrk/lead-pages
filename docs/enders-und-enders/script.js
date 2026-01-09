/**
 * Enders und Enders Rechtsanwälte - JavaScript
 * Dezente Animationen für Rechtsanwaltskanzlei
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all modules
    initHeader();
    initMobileMenu();
    initScrollAnimations();
    initSmoothScroll();
    initJusticeScale();
});

/**
 * Header scroll effect
 */
function initHeader() {
    const header = document.querySelector('.header');
    if (!header) return;

    let lastScroll = 0;
    const scrollThreshold = 50;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        // Add/remove scrolled class
        if (currentScroll > scrollThreshold) {
            header.classList.add('header--scrolled');
        } else {
            header.classList.remove('header--scrolled');
        }

        lastScroll = currentScroll;
    }, { passive: true });
}

/**
 * Mobile menu toggle
 */
function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMobile = document.querySelector('.nav-mobile');
    const navLinks = document.querySelectorAll('.nav-mobile__link');

    if (!menuToggle || !navMobile) return;

    menuToggle.addEventListener('click', function() {
        menuToggle.classList.toggle('menu-toggle--active');
        navMobile.classList.toggle('nav-mobile--active');
        document.body.style.overflow = navMobile.classList.contains('nav-mobile--active') ? 'hidden' : '';
    });

    // Close menu when clicking a link
    navLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            menuToggle.classList.remove('menu-toggle--active');
            navMobile.classList.remove('nav-mobile--active');
            document.body.style.overflow = '';
        });
    });

    // Close menu on escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navMobile.classList.contains('nav-mobile--active')) {
            menuToggle.classList.remove('menu-toggle--active');
            navMobile.classList.remove('nav-mobile--active');
            document.body.style.overflow = '';
        }
    });
}

/**
 * Scroll-triggered fade-in animations
 */
function initScrollAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');

    if (fadeElements.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    fadeElements.forEach(function(element) {
        observer.observe(element);
    });
}

/**
 * Smooth scroll for anchor links
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

                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Animate numbers (for statistics)
 */
function animateNumber(element, start, end, duration) {
    let startTimestamp = null;

    const step = function(timestamp) {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        element.textContent = value;

        if (progress < 1) {
            window.requestAnimationFrame(step);
        } else {
            element.textContent = end;
        }
    };

    window.requestAnimationFrame(step);
}

/**
 * Initialize stat counters when visible
 */
function initStatCounters() {
    const stats = document.querySelectorAll('.stat__number[data-count]');

    if (stats.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                const target = entry.target;
                const endValue = parseInt(target.getAttribute('data-count'), 10);
                animateNumber(target, 0, endValue, 2000);
                observer.unobserve(target);
            }
        });
    }, observerOptions);

    stats.forEach(function(stat) {
        observer.observe(stat);
    });
}

// Initialize stat counters after DOM is loaded
document.addEventListener('DOMContentLoaded', initStatCounters);

/**
 * Interactive Justice Scale Animation
 * - Reacts to scroll position (tilts based on scroll)
 * - Reacts to hover on bowls
 * - Click to temporarily tilt
 */
function initJusticeScale() {
    const scale = document.querySelector('.justice-scale');
    const scaleSection = document.querySelector('.justice-scale-section');

    if (!scale || !scaleSection) return;

    const bowlLeft = scale.querySelector('.bowl-left');
    const bowlRight = scale.querySelector('.bowl-right');

    let isAnimating = false;
    let scrollTiltEnabled = true;

    // Scroll-based tilting
    function handleScroll() {
        if (!scrollTiltEnabled || isAnimating) return;

        const rect = scaleSection.getBoundingClientRect();
        const sectionHeight = rect.height;
        const sectionTop = rect.top;
        const windowHeight = window.innerHeight;

        // Calculate how far through the section we've scrolled
        // -1 = top of section at bottom of viewport
        // 0 = center of section in center of viewport
        // 1 = bottom of section at top of viewport
        const scrollProgress = (windowHeight / 2 - sectionTop - sectionHeight / 2) / (sectionHeight / 2);

        // Clamp between -1 and 1
        const clampedProgress = Math.max(-1, Math.min(1, scrollProgress));

        // Apply tilt classes based on scroll position
        scale.classList.remove('tilted-left', 'tilted-right', 'balanced');

        if (clampedProgress < -0.3) {
            scale.classList.add('tilted-left');
        } else if (clampedProgress > 0.3) {
            scale.classList.add('tilted-right');
        } else {
            scale.classList.add('balanced');
        }
    }

    // Debounced scroll handler
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            window.cancelAnimationFrame(scrollTimeout);
        }
        scrollTimeout = window.requestAnimationFrame(handleScroll);
    }, { passive: true });

    // Initial state
    handleScroll();

    // Click on left bowl - tilt left temporarily
    if (bowlLeft) {
        bowlLeft.addEventListener('click', function() {
            if (isAnimating) return;

            isAnimating = true;
            scrollTiltEnabled = false;

            scale.classList.remove('tilted-right', 'balanced');
            scale.classList.add('tilted-left');

            // Animate back to balanced, then re-enable scroll
            setTimeout(function() {
                scale.classList.remove('tilted-left');
                scale.classList.add('balanced');

                setTimeout(function() {
                    isAnimating = false;
                    scrollTiltEnabled = true;
                    handleScroll(); // Restore scroll-based position
                }, 800);
            }, 1500);
        });
    }

    // Click on right bowl - tilt right temporarily
    if (bowlRight) {
        bowlRight.addEventListener('click', function() {
            if (isAnimating) return;

            isAnimating = true;
            scrollTiltEnabled = false;

            scale.classList.remove('tilted-left', 'balanced');
            scale.classList.add('tilted-right');

            // Animate back to balanced, then re-enable scroll
            setTimeout(function() {
                scale.classList.remove('tilted-right');
                scale.classList.add('balanced');

                setTimeout(function() {
                    isAnimating = false;
                    scrollTiltEnabled = true;
                    handleScroll(); // Restore scroll-based position
                }, 800);
            }, 1500);
        });
    }

    // Add subtle hover effect - bowls gently rise on hover
    function addBowlHoverEffect(bowl, side) {
        if (!bowl) return;

        bowl.addEventListener('mouseenter', function() {
            if (isAnimating) return;
            bowl.style.transform = 'translateY(-5px) scale(1.02)';
        });

        bowl.addEventListener('mouseleave', function() {
            if (isAnimating) return;
            bowl.style.transform = '';
        });
    }

    addBowlHoverEffect(bowlLeft, 'left');
    addBowlHoverEffect(bowlRight, 'right');

    // Accessibility: keyboard interaction
    scale.setAttribute('tabindex', '0');
    scale.setAttribute('role', 'img');
    scale.setAttribute('aria-label', 'Interaktive Waage der Gerechtigkeit. Drücken Sie Enter um die Animation zu sehen.');

    scale.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            if (isAnimating) return;

            isAnimating = true;
            scrollTiltEnabled = false;

            // Swing animation sequence
            scale.classList.remove('balanced');
            scale.classList.add('tilted-left');

            setTimeout(function() {
                scale.classList.remove('tilted-left');
                scale.classList.add('tilted-right');

                setTimeout(function() {
                    scale.classList.remove('tilted-right');
                    scale.classList.add('balanced');

                    setTimeout(function() {
                        isAnimating = false;
                        scrollTiltEnabled = true;
                        handleScroll();
                    }, 800);
                }, 800);
            }, 800);
        }
    });
}
