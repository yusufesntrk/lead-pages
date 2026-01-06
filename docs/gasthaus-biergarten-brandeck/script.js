/**
 * Gasthaus Biergarten Brandeck - JavaScript
 * Mobile Navigation, Smooth Scroll, Reveal Animations
 */

document.addEventListener('DOMContentLoaded', function() {
    // ========================================
    // Mobile Navigation
    // ========================================
    const menuToggle = document.getElementById('menu-toggle');
    const nav = document.getElementById('nav');
    const navLinks = document.querySelectorAll('.header__nav-link');

    if (menuToggle && nav) {
        menuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            nav.classList.toggle('active');
            document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu when clicking a link
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                menuToggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // ========================================
    // Header Scroll Effect
    // ========================================
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

    // ========================================
    // Smooth Scroll for Anchor Links
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerHeight = header.offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ========================================
    // Reveal Animations on Scroll
    // ========================================
    const revealElements = document.querySelectorAll('.reveal');

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

    // Initial check
    revealOnScroll();

    // Listen for scroll
    window.addEventListener('scroll', revealOnScroll, { passive: true });

    // ========================================
    // Open Status Checker
    // ========================================
    function updateOpenStatus() {
        const statusElement = document.getElementById('open-status');
        if (!statusElement) return;

        const now = new Date();
        const day = now.getDay(); // 0 = Sunday
        const hours = now.getHours();
        const minutes = now.getMinutes();
        const currentTime = hours * 60 + minutes;

        // Opening hours configuration
        const schedule = {
            0: { open: 11 * 60 + 30, close: 21 * 60 + 30 }, // Sunday
            1: { open: 10 * 60 + 30, close: 23 * 60 },      // Monday
            2: null,                                          // Tuesday - closed
            3: { open: 10 * 60 + 30, close: 23 * 60 },      // Wednesday
            4: { open: 10 * 60 + 30, close: 23 * 60 },      // Thursday
            5: { open: 10 * 60 + 30, close: 23 * 60 },      // Friday
            6: { open: 10 * 60 + 30, close: 23 * 60 }       // Saturday
        };

        const todaySchedule = schedule[day];
        const badge = statusElement.closest('.hero__badge');
        const dot = badge ? badge.querySelector('.hero__badge-dot') : null;

        if (!todaySchedule) {
            // Closed day (Tuesday)
            statusElement.textContent = 'Heute Ruhetag';
            if (dot) dot.style.backgroundColor = '#E53935';
        } else if (currentTime >= todaySchedule.open && currentTime < todaySchedule.close) {
            // Open
            const closeHour = Math.floor(todaySchedule.close / 60);
            const closeMinute = todaySchedule.close % 60;
            const closeTime = closeMinute > 0
                ? `${closeHour}:${closeMinute.toString().padStart(2, '0')}`
                : `${closeHour}:00`;
            statusElement.textContent = `Heute geöffnet bis ${closeTime}`;
            if (dot) dot.style.backgroundColor = '#4CAF50';
        } else {
            // Closed but will open/was open today
            if (currentTime < todaySchedule.open) {
                const openHour = Math.floor(todaySchedule.open / 60);
                const openMinute = todaySchedule.open % 60;
                const openTime = openMinute > 0
                    ? `${openHour}:${openMinute.toString().padStart(2, '0')}`
                    : `${openHour}:00`;
                statusElement.textContent = `Öffnet heute um ${openTime}`;
            } else {
                statusElement.textContent = 'Heute geschlossen';
            }
            if (dot) dot.style.backgroundColor = '#E53935';
        }
    }

    updateOpenStatus();
    // Update every minute
    setInterval(updateOpenStatus, 60000);

    // ========================================
    // Gallery Image Lightbox (Simple)
    // ========================================
    const galleryItems = document.querySelectorAll('.gallery__item');

    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            if (!img) return;

            // Create lightbox
            const lightbox = document.createElement('div');
            lightbox.className = 'lightbox';
            lightbox.innerHTML = `
                <div class="lightbox__overlay"></div>
                <div class="lightbox__content">
                    <img src="${img.src}" alt="${img.alt}">
                    <button class="lightbox__close">&times;</button>
                </div>
            `;

            // Add styles dynamically
            const style = document.createElement('style');
            style.textContent = `
                .lightbox {
                    position: fixed;
                    inset: 0;
                    z-index: 9999;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    animation: fadeIn 0.3s ease;
                }
                .lightbox__overlay {
                    position: absolute;
                    inset: 0;
                    background: rgba(0, 0, 0, 0.9);
                }
                .lightbox__content {
                    position: relative;
                    max-width: 90vw;
                    max-height: 90vh;
                }
                .lightbox__content img {
                    max-width: 100%;
                    max-height: 90vh;
                    border-radius: 8px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
                }
                .lightbox__close {
                    position: absolute;
                    top: -40px;
                    right: 0;
                    background: none;
                    border: none;
                    color: white;
                    font-size: 2rem;
                    cursor: pointer;
                    transition: transform 0.2s;
                }
                .lightbox__close:hover {
                    transform: scale(1.2);
                }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
            `;
            document.head.appendChild(style);
            document.body.appendChild(lightbox);
            document.body.style.overflow = 'hidden';

            // Close handlers
            const closeLightbox = () => {
                lightbox.remove();
                style.remove();
                document.body.style.overflow = '';
            };

            lightbox.querySelector('.lightbox__overlay').addEventListener('click', closeLightbox);
            lightbox.querySelector('.lightbox__close').addEventListener('click', closeLightbox);
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') closeLightbox();
            }, { once: true });
        });
    });

    // ========================================
    // Parallax Effect for Hero (subtle)
    // ========================================
    const heroImg = document.querySelector('.hero__bg-img');

    if (heroImg && window.innerWidth > 768) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * 0.3;
            heroImg.style.transform = `translateY(${rate}px)`;
        }, { passive: true });
    }

    // ========================================
    // Button Ripple Effect
    // ========================================
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const ripple = document.createElement('span');
            ripple.className = 'btn-ripple';
            ripple.style.cssText = `
                position: absolute;
                width: 0;
                height: 0;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: translate(-50%, -50%);
                animation: ripple 0.6s ease-out;
                left: ${x}px;
                top: ${y}px;
                pointer-events: none;
            `;

            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);

            // Add keyframe animation if not exists
            if (!document.querySelector('#ripple-style')) {
                const style = document.createElement('style');
                style.id = 'ripple-style';
                style.textContent = `
                    @keyframes ripple {
                        to {
                            width: 300px;
                            height: 300px;
                            opacity: 0;
                        }
                    }
                `;
                document.head.appendChild(style);
            }

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // ========================================
    // Lazy Loading Enhancement
    // ========================================
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px 0px',
            threshold: 0.01
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
});
