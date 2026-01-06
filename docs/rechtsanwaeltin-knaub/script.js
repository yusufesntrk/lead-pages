/**
 * Kanzlei Knaub - JavaScript
 * Mobile Navigation, Smooth Scroll, Reveal Animations
 */

document.addEventListener('DOMContentLoaded', function() {
  // ============================================
  // MOBILE NAVIGATION
  // ============================================

  const nav = document.getElementById('nav');
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  // Toggle mobile menu
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function() {
      navToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
      document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });

    // Close menu on link click
    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
      });
    });

    // Close menu on click outside
    document.addEventListener('click', function(e) {
      if (navMenu.classList.contains('active') &&
          !navMenu.contains(e.target) &&
          !navToggle.contains(e.target)) {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  // ============================================
  // NAVIGATION SCROLL EFFECT
  // ============================================

  function handleNavScroll() {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavScroll);
  handleNavScroll(); // Check initial state

  // ============================================
  // SMOOTH SCROLL
  // ============================================

  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');

      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        e.preventDefault();

        const navHeight = nav.offsetHeight;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
        const offsetPosition = targetPosition - navHeight - 20;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // ============================================
  // REVEAL ANIMATIONS
  // ============================================

  const revealElements = document.querySelectorAll(
    '.section-header, ' +
    '.rechtsgebiet-card, ' +
    '.ueber-mich-content, ' +
    '.ueber-mich-visual, ' +
    '.timeline-item, ' +
    '.bewertung-card, ' +
    '.cta-content, ' +
    '.kontakt-info, ' +
    '.kontakt-map'
  );

  // Add reveal class to elements
  revealElements.forEach(function(el) {
    el.classList.add('reveal');
  });

  // Create intersection observer
  const revealObserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        // Optionally unobserve after revealing
        // revealObserver.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  });

  // Observe all reveal elements
  revealElements.forEach(function(el) {
    revealObserver.observe(el);
  });

  // ============================================
  // STAGGER ANIMATION FOR GRIDS
  // ============================================

  const staggerContainers = document.querySelectorAll('.rechtsgebiete-grid, .bewertungen-grid');

  staggerContainers.forEach(function(container) {
    container.classList.add('stagger-children');
  });

  // ============================================
  // HERO STATS COUNTER ANIMATION
  // ============================================

  const statNumbers = document.querySelectorAll('.stat-number');

  const countObserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        const el = entry.target;
        const text = el.textContent;

        // Only animate if it's a pure number
        if (/^\d+(\.\d+)?$/.test(text)) {
          const target = parseFloat(text);
          const isDecimal = text.includes('.');
          animateNumber(el, target, isDecimal);
        }

        countObserver.unobserve(el);
      }
    });
  }, {
    threshold: 0.5
  });

  statNumbers.forEach(function(el) {
    countObserver.observe(el);
  });

  function animateNumber(element, target, isDecimal) {
    const duration = 1500;
    const start = 0;
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Easing function (ease-out)
      const easeOut = 1 - Math.pow(1 - progress, 3);
      const current = start + (target - start) * easeOut;

      if (isDecimal) {
        element.textContent = current.toFixed(1);
      } else {
        element.textContent = Math.floor(current);
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        element.textContent = isDecimal ? target.toFixed(1) : target;
      }
    }

    requestAnimationFrame(update);
  }

  // ============================================
  // TIMELINE ANIMATION
  // ============================================

  const timelineItems = document.querySelectorAll('.timeline-item');

  const timelineObserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry, index) {
      if (entry.isIntersecting) {
        setTimeout(function() {
          entry.target.classList.add('revealed');
        }, index * 150);
      }
    });
  }, {
    threshold: 0.3
  });

  timelineItems.forEach(function(item) {
    item.classList.add('reveal');
    timelineObserver.observe(item);
  });

  // ============================================
  // ACTIVE NAVIGATION LINK
  // ============================================

  const sections = document.querySelectorAll('section[id]');

  function highlightNavLink() {
    const scrollPosition = window.scrollY + 150;

    sections.forEach(function(section) {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');
      const correspondingLink = document.querySelector('.nav-link[href="#' + sectionId + '"]');

      if (correspondingLink) {
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
          navLinks.forEach(function(link) {
            link.classList.remove('active');
          });
          correspondingLink.classList.add('active');
        }
      }
    });
  }

  window.addEventListener('scroll', highlightNavLink);

  // ============================================
  // PRELOADER (Optional)
  // ============================================

  window.addEventListener('load', function() {
    document.body.classList.add('loaded');
  });
});
