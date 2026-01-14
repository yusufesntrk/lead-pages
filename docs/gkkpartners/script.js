/**
 * GKK Partners - Main JavaScript
 * Handles all animations, interactions and UI behaviors
 */

document.addEventListener('DOMContentLoaded', () => {
  // Initialize all modules
  initHeader();
  initNavigation();
  initScrollAnimations();
  initTabGallery();
  initServiceCards();
  initScrollToTop();
  initSmoothScroll();
  initVideoPlayer();
});

/**
 * Header Module
 * Handles sticky header, logo switch on scroll
 */
function initHeader() {
  const header = document.getElementById('siteHeader');
  const scrollThreshold = 100;
  let lastScrollY = 0;
  let ticking = false;

  function updateHeader() {
    const scrollY = window.scrollY;

    // Add/remove scrolled class
    if (scrollY > scrollThreshold) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    // Hide/show header on scroll direction (optional)
    if (scrollY > lastScrollY && scrollY > 200) {
      // Scrolling down
      // header.style.transform = 'translateY(-100%)';
    } else {
      // Scrolling up
      // header.style.transform = 'translateY(0)';
    }

    lastScrollY = scrollY;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(updateHeader);
      ticking = true;
    }
  });

  // Initial check
  updateHeader();
}

/**
 * Navigation Module
 * Handles hamburger menu toggle and mobile navigation
 */
function initNavigation() {
  const menuToggle = document.getElementById('menuToggle');
  const mainNav = document.getElementById('mainNav');
  const body = document.body;

  if (!menuToggle || !mainNav) return;

  menuToggle.addEventListener('click', () => {
    menuToggle.classList.toggle('active');
    mainNav.classList.toggle('active');
    body.classList.toggle('menu-open');
  });

  // Close menu on link click
  const navLinks = mainNav.querySelectorAll('a');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      menuToggle.classList.remove('active');
      mainNav.classList.remove('active');
      body.classList.remove('menu-open');
    });
  });

  // Close menu on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mainNav.classList.contains('active')) {
      menuToggle.classList.remove('active');
      mainNav.classList.remove('active');
      body.classList.remove('menu-open');
    }
  });

  // Submenu toggles for mobile
  const submenuToggles = mainNav.querySelectorAll('.nav-menu > li > a');
  submenuToggles.forEach(toggle => {
    const submenu = toggle.nextElementSibling;
    if (submenu && submenu.classList.contains('nav-submenu')) {
      // On mobile, prevent default and toggle submenu
      toggle.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          submenu.classList.toggle('open');
          toggle.classList.toggle('open');
        }
      });
    }
  });
}

/**
 * Scroll Animations Module
 * Uses Intersection Observer for scroll-triggered animations
 */
function initScrollAnimations() {
  // Elements to animate
  const animatedSections = document.querySelectorAll(
    '.image-gradient-section, .tab-gallery, .logo-mask-section'
  );

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -100px 0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        // Unobserve after animation
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  animatedSections.forEach(section => {
    observer.observe(section);
  });
}

/**
 * Tab Gallery Module
 * Handles hover interactions on target group tabs
 */
function initTabGallery() {
  const tabLinks = document.querySelectorAll('.tab-link');
  const tabImages = document.querySelectorAll('.tab-image');

  if (tabLinks.length === 0 || tabImages.length === 0) return;

  // Show default image initially
  const defaultImage = document.querySelector('.tab-image[data-tab="0"]');
  if (defaultImage) {
    defaultImage.classList.add('active');
  }

  tabLinks.forEach(link => {
    link.addEventListener('mouseenter', () => {
      const tabId = link.dataset.tab;

      // Hide all images
      tabImages.forEach(img => {
        img.classList.remove('active');
      });

      // Show corresponding image
      const targetImage = document.querySelector(`.tab-image[data-tab="${tabId}"]`);
      if (targetImage) {
        targetImage.classList.add('active');
      }
    });

    link.addEventListener('mouseleave', () => {
      // Optionally show default image when not hovering
      // Uncomment below to revert to default on mouse leave
      /*
      tabImages.forEach(img => {
        img.classList.remove('active');
      });
      if (defaultImage) {
        defaultImage.classList.add('active');
      }
      */
    });
  });

  // Reset to default when leaving the entire gallery
  const tabGallery = document.querySelector('.tab-gallery');
  if (tabGallery) {
    tabGallery.addEventListener('mouseleave', () => {
      tabImages.forEach(img => {
        img.classList.remove('active');
      });
      if (defaultImage) {
        defaultImage.classList.add('active');
      }
    });
  }
}

/**
 * Service Cards Module
 * Handles card animations on scroll and hover effects
 */
function initServiceCards() {
  const cards = document.querySelectorAll('.service-card');

  if (cards.length === 0) return;

  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Stagger animation delay
        setTimeout(() => {
          entry.target.classList.add('animate-in');
        }, index * 100);
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  cards.forEach(card => {
    observer.observe(card);
  });

  // Additional hover effects handled in CSS
}

/**
 * Scroll to Top Module
 * Shows/hides button based on scroll position
 */
function initScrollToTop() {
  const scrollBtn = document.getElementById('scrollToTop');

  if (!scrollBtn) return;

  const showThreshold = 500;
  let ticking = false;

  function updateButton() {
    if (window.scrollY > showThreshold) {
      scrollBtn.classList.add('visible');
    } else {
      scrollBtn.classList.remove('visible');
    }
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(updateButton);
      ticking = true;
    }
  });

  scrollBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  // Initial check
  updateButton();
}

/**
 * Smooth Scroll Module
 * Handles smooth scrolling for anchor links
 */
function initSmoothScroll() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');

  anchorLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');

      // Skip if it's just "#"
      if (href === '#') return;

      const target = document.querySelector(href);

      if (target) {
        e.preventDefault();

        const headerOffset = 100;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.scrollY - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });

        // Update URL without jumping
        history.pushState(null, '', href);
      }
    });
  });
}

/**
 * Video Player Module
 * Handles hero video playback
 */
function initVideoPlayer() {
  const video = document.querySelector('.hero-video');

  if (!video) return;

  // Ensure video plays on mobile
  video.play().catch(() => {
    // Autoplay was prevented, show poster instead
    console.log('Video autoplay prevented');
  });

  // Pause video when not in viewport (performance)
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        video.play().catch(() => {});
      } else {
        video.pause();
      }
    });
  }, { threshold: 0.1 });

  observer.observe(video);
}

/**
 * Parallax Effect (Optional)
 * Add subtle parallax to hero section
 */
function initParallax() {
  const hero = document.querySelector('.hero-section');

  if (!hero) return;

  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        const heroHeight = hero.offsetHeight;

        if (scrollY < heroHeight) {
          const parallaxValue = scrollY * 0.5;
          hero.style.transform = `translateY(${parallaxValue}px)`;
        }

        ticking = false;
      });
      ticking = true;
    }
  });
}

/**
 * Lazy Loading Images
 * Load images as they enter viewport
 */
function initLazyLoading() {
  const lazyImages = document.querySelectorAll('img[data-src]');

  if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
  } else {
    // Fallback for older browsers
    lazyImages.forEach(img => {
      img.src = img.dataset.src;
    });
  }
}

/**
 * Preloader (Optional)
 * Show loading animation until page is ready
 */
function initPreloader() {
  const preloader = document.getElementById('preloader');

  if (!preloader) return;

  window.addEventListener('load', () => {
    preloader.classList.add('loaded');
    setTimeout(() => {
      preloader.remove();
    }, 500);
  });
}

/**
 * Counter Animation
 * Animate numbers when they come into view
 */
function animateCounter(element, target, duration = 2000) {
  let start = 0;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    // Easing function (ease-out)
    const easeOut = 1 - Math.pow(1 - progress, 3);

    const current = Math.floor(easeOut * target);
    element.textContent = current.toLocaleString('de-DE');

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      element.textContent = target.toLocaleString('de-DE');
    }
  }

  requestAnimationFrame(update);
}

/**
 * Form Validation (for contact forms)
 */
function initFormValidation() {
  const forms = document.querySelectorAll('form[data-validate]');

  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      let isValid = true;
      const requiredFields = form.querySelectorAll('[required]');

      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          isValid = false;
          field.classList.add('error');
        } else {
          field.classList.remove('error');
        }

        // Email validation
        if (field.type === 'email' && field.value) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(field.value)) {
            isValid = false;
            field.classList.add('error');
          }
        }
      });

      if (!isValid) {
        e.preventDefault();
      }
    });
  });
}

/**
 * Utility: Debounce function
 */
function debounce(func, wait = 100) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

/**
 * Utility: Throttle function
 */
function throttle(func, limit = 100) {
  let inThrottle;
  return function executedFunction(...args) {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// Export for potential use in other scripts
window.GKKPartners = {
  initHeader,
  initNavigation,
  initScrollAnimations,
  initTabGallery,
  initServiceCards,
  initScrollToTop,
  initSmoothScroll,
  animateCounter
};
