/**
 * Große-Wächter & Watter Rechtsanwälte
 * Kanzlei für Arbeitsrecht - Kehl
 * Website JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize all components
  initMobileNav();
  initStickyHeader();
  initScrollAnimations();
  initSmoothScroll();
});

/**
 * Mobile Navigation Toggle
 */
function initMobileNav() {
  const toggle = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.nav');

  if (!toggle || !nav) return;

  toggle.addEventListener('click', function() {
    nav.classList.toggle('active');

    // Animate hamburger to X
    const spans = toggle.querySelectorAll('span');
    if (nav.classList.contains('active')) {
      spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
    } else {
      spans[0].style.transform = 'none';
      spans[1].style.opacity = '1';
      spans[2].style.transform = 'none';
    }
  });

  // Close nav when clicking outside
  document.addEventListener('click', function(e) {
    if (!toggle.contains(e.target) && !nav.contains(e.target)) {
      nav.classList.remove('active');
      const spans = toggle.querySelectorAll('span');
      spans[0].style.transform = 'none';
      spans[1].style.opacity = '1';
      spans[2].style.transform = 'none';
    }
  });

  // Close nav when clicking a link
  nav.querySelectorAll('a').forEach(function(link) {
    link.addEventListener('click', function() {
      nav.classList.remove('active');
      const spans = toggle.querySelectorAll('span');
      spans[0].style.transform = 'none';
      spans[1].style.opacity = '1';
      spans[2].style.transform = 'none';
    });
  });
}

/**
 * Sticky Header with Shadow on Scroll
 */
function initStickyHeader() {
  const header = document.querySelector('.header');
  if (!header) return;

  let lastScroll = 0;

  window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
  });
}

/**
 * Scroll Animations - Fade In Elements
 */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.fade-in');

  if (!elements.length) return;

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  elements.forEach(function(element) {
    observer.observe(element);
  });
}

/**
 * Smooth Scroll for Anchor Links
 */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;

      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();

      const headerHeight = document.querySelector('.header').offsetHeight;
      const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    });
  });
}

/**
 * Utility: Debounce function for performance
 */
function debounce(func, wait) {
  let timeout;
  return function executedFunction() {
    const context = this;
    const args = arguments;
    const later = function() {
      timeout = null;
      func.apply(context, args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}
