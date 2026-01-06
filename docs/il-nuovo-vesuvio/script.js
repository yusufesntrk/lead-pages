/* ==========================================================================
   Il Nuovo Vesuvio - JavaScript
   Mobile Navigation, Smooth Scroll, Reveal Animations
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function() {

    /* --------------------------------------------------------------------------
       Mobile Navigation
       -------------------------------------------------------------------------- */
    const navMenu = document.getElementById('nav-menu');
    const navToggle = document.getElementById('nav-toggle');
    const navClose = document.getElementById('nav-close');
    const navLinks = document.querySelectorAll('.nav__link');

    // Open mobile menu
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.add('show');
            document.body.style.overflow = 'hidden';
        });
    }

    // Close mobile menu
    if (navClose) {
        navClose.addEventListener('click', () => {
            navMenu.classList.remove('show');
            document.body.style.overflow = '';
        });
    }

    // Close menu on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('show');
            document.body.style.overflow = '';
        });
    });

    // Close menu on outside click
    document.addEventListener('click', (e) => {
        if (navMenu.classList.contains('show') &&
            !navMenu.contains(e.target) &&
            !navToggle.contains(e.target)) {
            navMenu.classList.remove('show');
            document.body.style.overflow = '';
        }
    });

    /* --------------------------------------------------------------------------
       Header Scroll Effect
       -------------------------------------------------------------------------- */
    const header = document.getElementById('header');
    let lastScroll = 0;

    function handleHeaderScroll() {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    }

    window.addEventListener('scroll', handleHeaderScroll, { passive: true });
    handleHeaderScroll(); // Initial check

    /* --------------------------------------------------------------------------
       Smooth Scroll for Anchor Links
       -------------------------------------------------------------------------- */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                const headerHeight = header.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    /* --------------------------------------------------------------------------
       Scroll Reveal Animations
       -------------------------------------------------------------------------- */
    const revealElements = document.querySelectorAll('.reveal');

    const revealOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add staggered delay for elements in same section
                const delay = entry.target.dataset.delay || 0;

                setTimeout(() => {
                    entry.target.classList.add('active');
                }, delay);

                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach((el, index) => {
        // Add stagger effect for grid items
        const parent = el.parentElement;
        if (parent && parent.children.length > 1) {
            const siblings = Array.from(parent.querySelectorAll('.reveal'));
            const siblingIndex = siblings.indexOf(el);
            if (siblingIndex > 0) {
                el.dataset.delay = siblingIndex * 100;
            }
        }
        revealObserver.observe(el);
    });

    /* --------------------------------------------------------------------------
       Active Navigation Link
       -------------------------------------------------------------------------- */
    function setActiveNavLink() {
        const sections = document.querySelectorAll('section[id]');
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionHeight = section.offsetHeight;
            const sectionTop = section.offsetTop - 200;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.nav__link[href="#${sectionId}"]`);

            if (navLink) {
                if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                    navLink.classList.add('active');
                } else {
                    navLink.classList.remove('active');
                }
            }
        });
    }

    window.addEventListener('scroll', setActiveNavLink, { passive: true });

    /* --------------------------------------------------------------------------
       Parallax Effect (subtle)
       -------------------------------------------------------------------------- */
    const heroImage = document.querySelector('.hero__image');

    if (heroImage && window.innerWidth > 768) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * 0.3;
            heroImage.style.transform = `translateY(${rate}px)`;
        }, { passive: true });
    }

    /* --------------------------------------------------------------------------
       Image Lazy Loading Enhancement
       -------------------------------------------------------------------------- */
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: '50px 0px'
    });

    images.forEach(img => imageObserver.observe(img));

    /* --------------------------------------------------------------------------
       Testimonials Horizontal Scroll (Mobile)
       -------------------------------------------------------------------------- */
    const testimonialSlider = document.querySelector('.testimonials__slider');

    if (testimonialSlider && window.innerWidth <= 968) {
        let isDown = false;
        let startX;
        let scrollLeft;

        testimonialSlider.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - testimonialSlider.offsetLeft;
            scrollLeft = testimonialSlider.scrollLeft;
        });

        testimonialSlider.addEventListener('mouseleave', () => {
            isDown = false;
        });

        testimonialSlider.addEventListener('mouseup', () => {
            isDown = false;
        });

        testimonialSlider.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - testimonialSlider.offsetLeft;
            const walk = (x - startX) * 2;
            testimonialSlider.scrollLeft = scrollLeft - walk;
        });
    }

    /* --------------------------------------------------------------------------
       Button Ripple Effect
       -------------------------------------------------------------------------- */
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const rect = this.getBoundingClientRect();
            const ripple = document.createElement('span');

            ripple.className = 'ripple';
            ripple.style.left = `${e.clientX - rect.left}px`;
            ripple.style.top = `${e.clientY - rect.top}px`;

            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    /* --------------------------------------------------------------------------
       Form Validation (if forms exist)
       -------------------------------------------------------------------------- */
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = this.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    /* --------------------------------------------------------------------------
       Accessibility: Reduce Motion
       -------------------------------------------------------------------------- */
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    if (prefersReducedMotion.matches) {
        document.documentElement.style.setProperty('--transition-fast', '0ms');
        document.documentElement.style.setProperty('--transition-base', '0ms');
        document.documentElement.style.setProperty('--transition-slow', '0ms');

        // Instantly reveal all elements
        revealElements.forEach(el => el.classList.add('active'));
    }

    /* --------------------------------------------------------------------------
       Console Welcome Message
       -------------------------------------------------------------------------- */
    console.log('%c🍝 Il Nuovo Vesuvio', 'font-size: 20px; font-weight: bold; color: #8B2332;');
    console.log('%cAuthentische italienische Küche seit 1997', 'font-size: 14px; color: #C88E7C;');
    console.log('%cHildastraße 4, 77654 Offenburg', 'font-size: 12px; color: #6B6360;');

});

/* --------------------------------------------------------------------------
   CSS for Ripple Effect (injected via JS)
   -------------------------------------------------------------------------- */
const style = document.createElement('style');
style.textContent = `
    .btn {
        position: relative;
        overflow: hidden;
    }

    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }

    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
