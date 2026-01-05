/* =========================================
   KAISERPALAST CHINA RESTAURANT
   JavaScript - Navigation, Smooth Scroll, Animations
   ========================================= */

// Add JS class to HTML element for CSS progressive enhancement
document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', function() {
  // -----------------------------------------
  // MOBILE NAVIGATION
  // -----------------------------------------
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('.mobile-nav');
  const mobileNavLinks = document.querySelectorAll('.mobile-nav__link');
  const body = document.body;

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', function() {
      this.classList.toggle('menu-toggle--active');
      mobileNav.classList.toggle('mobile-nav--open');
      body.style.overflow = mobileNav.classList.contains('mobile-nav--open') ? 'hidden' : '';
    });

    // Close mobile nav when clicking a link
    mobileNavLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        menuToggle.classList.remove('menu-toggle--active');
        mobileNav.classList.remove('mobile-nav--open');
        body.style.overflow = '';
      });
    });
  }

  // -----------------------------------------
  // HEADER SCROLL EFFECT
  // -----------------------------------------
  const header = document.querySelector('.header');
  let lastScroll = 0;

  function handleHeaderScroll() {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
      header.classList.add('header--scrolled');
    } else {
      header.classList.remove('header--scrolled');
    }

    lastScroll = currentScroll;
  }

  window.addEventListener('scroll', handleHeaderScroll, { passive: true });

  // -----------------------------------------
  // SMOOTH SCROLL
  // -----------------------------------------
  const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');

  smoothScrollLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');

      if (href === '#') return;

      const target = document.querySelector(href);

      if (target) {
        e.preventDefault();

        const headerHeight = header.offsetHeight;
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // -----------------------------------------
  // REVEAL ON SCROLL ANIMATIONS
  // -----------------------------------------
  const revealElements = document.querySelectorAll('.reveal');

  function revealOnScroll() {
    const windowHeight = window.innerHeight;
    const revealPoint = 100;

    revealElements.forEach(function(element) {
      const elementTop = element.getBoundingClientRect().top;

      if (elementTop < windowHeight - revealPoint) {
        element.classList.add('reveal--visible');
      }
    });
  }

  // Initial check
  revealOnScroll();

  // Check on scroll
  window.addEventListener('scroll', revealOnScroll, { passive: true });

  // -----------------------------------------
  // GALLERY LIGHTBOX (Simple)
  // -----------------------------------------
  const galleryItems = document.querySelectorAll('.gallery__item');

  galleryItems.forEach(function(item) {
    item.style.cursor = 'pointer';

    item.addEventListener('click', function() {
      const img = this.querySelector('.gallery__image');
      if (img) {
        // Open image in new tab (simple approach)
        window.open(img.src, '_blank');
      }
    });
  });

  // -----------------------------------------
  // INTERSECTION OBSERVER FOR STATS
  // -----------------------------------------
  const trustItems = document.querySelectorAll('.trust__number');

  if (trustItems.length > 0 && 'IntersectionObserver' in window) {
    const statsObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-count');
          statsObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.5
    });

    trustItems.forEach(function(item) {
      statsObserver.observe(item);
    });
  }

  // -----------------------------------------
  // CURRENT YEAR IN FOOTER
  // -----------------------------------------
  const yearElement = document.querySelector('.footer__year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // -----------------------------------------
  // PHONE LINK CLICK TRACKING
  // -----------------------------------------
  const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

  phoneLinks.forEach(function(link) {
    link.addEventListener('click', function() {
      // Analytics tracking could be added here
      console.log('Phone link clicked');
    });
  });

  // -----------------------------------------
  // LAZY LOADING IMAGES (Progressive Enhancement)
  // -----------------------------------------
  if ('loading' in HTMLImageElement.prototype) {
    // Browser supports native lazy loading
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');
    lazyImages.forEach(function(img) {
      img.src = img.dataset.src || img.src;
    });
  } else {
    // Fallback for browsers without native support
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');

    if ('IntersectionObserver' in window) {
      const imageObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src || img.src;
            imageObserver.unobserve(img);
          }
        });
      });

      lazyImages.forEach(function(img) {
        imageObserver.observe(img);
      });
    }
  }
});
