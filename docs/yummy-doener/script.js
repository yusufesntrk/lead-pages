/* ========================================
   YUMMY Döner Offenburg - JavaScript
   Scroll Reveal, Testimonials, Mobile Nav,
   Menu Filter, Counter, Cookie Banner
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initTestimonialSlider();
    initScrollReveal();
    initMobileNav();
    initCookieBanner();
    initMenuFilter();
    initCounter();
});

/* ========================================
   NAVBAR - Scroll Effect
   ======================================== */
function initNavbar() {
    const header = document.getElementById('header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }, { passive: true });
}

/* ========================================
   TESTIMONIAL SLIDER
   ======================================== */
function initTestimonialSlider() {
    const cards = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.t-dot');
    if (cards.length === 0) return;

    let current = 0;
    let interval;

    function goTo(index) {
        cards[current].classList.remove('active');
        dots[current]?.classList.remove('active');
        current = index;
        cards[current].classList.add('active');
        dots[current]?.classList.add('active');
    }

    function next() {
        goTo((current + 1) % cards.length);
    }

    function startAutoplay() {
        interval = setInterval(next, 6000);
    }

    function stopAutoplay() {
        clearInterval(interval);
    }

    dots.forEach((dot, i) => {
        dot.addEventListener('click', () => {
            stopAutoplay();
            goTo(i);
            startAutoplay();
        });
    });

    startAutoplay();
}

/* ========================================
   SCROLL REVEAL - Intersection Observer
   ======================================== */
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');
    if (revealElements.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            el.classList.add('visible');
        } else {
            observer.observe(el);
        }
    });
}

/* ========================================
   MOBILE NAV
   ======================================== */
function initMobileNav() {
    const toggle = document.querySelector('.nav-toggle');
    const menu = document.querySelector('.nav-menu');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', () => {
        const isOpen = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', !isOpen);
        menu.classList.toggle('open');
        document.body.style.overflow = isOpen ? '' : 'hidden';
    });

    menu.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            toggle.setAttribute('aria-expanded', 'false');
            menu.classList.remove('open');
            document.body.style.overflow = '';
        });
    });

    document.addEventListener('click', (e) => {
        if (!menu.contains(e.target) && !toggle.contains(e.target) && menu.classList.contains('open')) {
            toggle.setAttribute('aria-expanded', 'false');
            menu.classList.remove('open');
            document.body.style.overflow = '';
        }
    });
}

/* ========================================
   COOKIE BANNER
   ======================================== */
function initCookieBanner() {
    const banner = document.getElementById('cookieBanner');
    const acceptBtn = document.getElementById('cookieAccept');
    const rejectBtn = document.getElementById('cookieReject');
    if (!banner) return;

    if (!localStorage.getItem('cookieConsent')) {
        setTimeout(() => {
            banner.classList.add('visible');
        }, 1500);
    }

    acceptBtn?.addEventListener('click', () => {
        localStorage.setItem('cookieConsent', 'accepted');
        banner.classList.remove('visible');
    });

    rejectBtn?.addEventListener('click', () => {
        localStorage.setItem('cookieConsent', 'rejected');
        banner.classList.remove('visible');
    });
}

/* ========================================
   MENU FILTER
   ======================================== */
function initMenuFilter() {
    const tabs = document.querySelectorAll('.menu-tab');
    const items = document.querySelectorAll('.menu-item');
    if (tabs.length === 0 || items.length === 0) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const category = tab.dataset.category;

            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            items.forEach(item => {
                if (category === 'all' || item.dataset.category === category) {
                    item.classList.remove('hidden');
                } else {
                    item.classList.add('hidden');
                }
            });
        });
    });
}

/* ========================================
   COUNTER ANIMATION
   ======================================== */
function initCounter() {
    const counters = document.querySelectorAll('.stat-number[data-target]');
    if (counters.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.dataset.target);
                animateCounter(el, target);
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
}

function animateCounter(el, target) {
    const duration = 2000;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(eased * target);
        el.textContent = current.toLocaleString('de-DE');

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}
