// ===== SCROLL-DRIVEN CAR (fixed → absolute) =====
(function () {
  const track    = document.querySelector('.hero-track');
  const hero     = document.getElementById('hero');
  const assembly = document.getElementById('carAssembly');
  if (!track || !hero || !assembly) return;

  let lastMode = ''; // 'fixed' or 'done'

  function setFixed() {
    if (lastMode === 'fixed') return;
    lastMode = 'fixed';
    hero.style.position = 'fixed';
    hero.style.top      = '0';
    hero.style.bottom   = 'auto';
    hero.style.left     = '0';
    hero.style.right    = '0';
  }

  function setDone() {
    if (lastMode === 'done') return;
    lastMode = 'done';
    // Pin hero to bottom of track so it scrolls off naturally
    hero.style.position = 'absolute';
    hero.style.top      = 'auto';
    hero.style.bottom   = '0';
    hero.style.left     = '0';
    hero.style.right    = '0';
  }

  function update() {
    const scrollY   = window.scrollY;
    const trackH    = track.offsetHeight;  // 200dvh in px
    const viewH     = window.innerHeight;
    const viewW     = window.innerWidth;
    const maxScroll = trackH - viewH;      // 100dvh scroll space

    if (scrollY >= maxScroll) {
      setDone();
      return;
    }

    setFixed();
    const progress = Math.max(0, scrollY / maxScroll);

    // car: starts half-visible on left, exits fully right
    const carW = viewW <= 640 ? 260 : 400;
    const x = -(carW / 2) + progress * (viewW + carW / 2 + 50);
    assembly.style.left = x + 'px';

    // wheel spin speed
    const speed = 0.8 - progress * 0.5;
    assembly.querySelectorAll('.wheel').forEach(w => {
      w.style.animationDuration = speed + 's';
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
})();

// ===== NAVBAR SCROLL =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// ===== MOBILE MENU =====
const mobileToggle = document.getElementById('mobileToggle');
const navMenu = document.getElementById('navMenu');

mobileToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
  const isOpen = navMenu.classList.contains('active');
  mobileToggle.setAttribute('aria-label', isOpen ? 'Menü schließen' : 'Menü öffnen');
  document.body.style.overflow = isOpen ? 'hidden' : '';
});

// Close menu on link click
navMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('active');
    document.body.style.overflow = '';
  });
});

// ===== SCROLL REVEAL =====
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll(
  '.way-card, .feature-item, .location-card, .class-card, .why-card, .milestone-step, .testimonial-card, .contact-detail'
).forEach((el, i) => {
  el.classList.add('reveal');
  el.style.transitionDelay = `${(i % 4) * 80}ms`;
  revealObserver.observe(el);
});

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    if (href === '#') return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

// ===== CONTACT FORM =====
const form = document.querySelector('.contact-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type=submit]');
    btn.textContent = '✓ Anfrage gesendet!';
    btn.style.background = '#16a34a';
    btn.disabled = true;
    setTimeout(() => {
      btn.innerHTML = 'Jetzt anfragen <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>';
      btn.style.background = '';
      btn.disabled = false;
      form.reset();
    }, 3000);
  });
}

// ===== COUNTER ANIMATION =====
const counters = document.querySelectorAll('.stat-number');
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = el.textContent.replace(/[^0-9]/g, '');
      if (!target) return;
      const suffix = el.textContent.replace(/[0-9]/g, '');
      const duration = 1500;
      const steps = 40;
      const increment = parseInt(target) / steps;
      let current = 0;
      const timer = setInterval(() => {
        current += increment;
        if (current >= parseInt(target)) {
          el.textContent = target + suffix;
          clearInterval(timer);
        } else {
          el.textContent = Math.round(current) + suffix;
        }
      }, duration / steps);
      counterObserver.unobserve(el);
    }
  });
}, { threshold: 0.5 });

counters.forEach(c => counterObserver.observe(c));

// ===== DATA-ANIM OBSERVER =====
const animObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('anim-visible');
      animObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('[data-anim]').forEach((el, i) => {
  el.style.transitionDelay = `${(i % 5) * 60}ms`;
  animObserver.observe(el);
});
