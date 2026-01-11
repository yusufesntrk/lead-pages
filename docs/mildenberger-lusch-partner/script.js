/**
 * Mildenberger Lusch + Partner
 * Main JavaScript File
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollAnimations();
    initCounters();
    initStagger();
    initChartAnimation();
    initHeaderScroll();
});

/**
 * Mobile Navigation
 */
function initNavigation() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-menu');

    if (toggle && menu) {
        toggle.addEventListener('click', () => {
            toggle.classList.toggle('active');
            menu.classList.toggle('active');
        });

        // Close menu when clicking a link
        menu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                toggle.classList.remove('active');
                menu.classList.remove('active');
            });
        });
    }
}

/**
 * Header scroll effect
 */
function initHeaderScroll() {
    const header = document.querySelector('.header');

    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        };

        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
    }
}

/**
 * Scroll animations with IntersectionObserver
 */
function initScrollAnimations() {
    const elements = document.querySelectorAll('[data-scroll], .blur-reveal, .underline-scroll, .highlight-scroll');

    // CRITICAL FIX: Make elements visible if already in viewport on page load
    // Use generous margin for elements just below fold (especially hero CTA)
    elements.forEach(el => {
        const rect = el.getBoundingClientRect();
        const margin = 100; // Allow 100px below viewport
        const inViewport = rect.top < (window.innerHeight + margin) && rect.bottom > -margin;

        if (inViewport) {
            el.classList.add('visible');
        }
    });

    // Continue observing for elements that scroll into view later
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(el => observer.observe(el));
}

/**
 * Counter animation
 */
function initCounters() {
    const counters = document.querySelectorAll('.counter[data-target]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.dataset.target);
                animateCounter(counter, target);
                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
}

function animateCounter(element, target) {
    const duration = 2000;
    const start = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - start;
        const progress = Math.min(elapsed / duration, 1);

        // Easing: easeOutExpo
        const eased = 1 - Math.pow(2, -10 * progress);
        const current = Math.floor(eased * target);

        element.textContent = current;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = target;
        }
    }

    requestAnimationFrame(update);
}

/**
 * Staggered children animation
 */
function initStagger() {
    document.querySelectorAll('[data-stagger]').forEach(container => {
        const children = container.children;
        Array.from(children).forEach((child, i) => {
            child.style.transitionDelay = `${i * 0.1}s`;
        });
    });
}

/**
 * Chart growth animation
 */
function initChartAnimation() {
    const chart = document.querySelector('.chart-growth');

    if (chart) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    chart.classList.add('animate');
                    observer.unobserve(chart);
                }
            });
        }, { threshold: 0.3 });

        observer.observe(chart);
    }
}

/**
 * Smooth scroll for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        }
    });
});
