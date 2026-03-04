// ===== NAVBAR SCROLL =====
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
}, { passive: true });

// ===== MOBILE MENU =====
const toggle = document.getElementById('mobileToggle');
const menu = document.getElementById('navMenu');
toggle.addEventListener('click', () => {
  const open = menu.classList.toggle('active');
  document.body.style.overflow = open ? 'hidden' : '';
});
menu.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    menu.classList.remove('active');
    document.body.style.overflow = '';
  });
});

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      e.preventDefault();
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 80, behavior: 'smooth' });
    }
  });
});

// ===== COUNTER ANIMATION (odometer style) =====
const counters = document.querySelectorAll('.hstat-num[data-target]');
let countersAnimated = false;

function animateCounters() {
  if (countersAnimated) return;
  countersAnimated = true;
  counters.forEach(el => {
    const target = parseInt(el.dataset.target);
    const duration = 2000;
    const steps = 50;
    const inc = target / steps;
    let current = 0;
    let step = 0;
    const timer = setInterval(() => {
      step++;
      current = Math.min(Math.round(inc * step), target);
      el.textContent = current;
      if (step >= steps) clearInterval(timer);
    }, duration / steps);
  });
}

// ===== SCROLL REVEAL =====
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
    }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('[data-reveal]').forEach((el, i) => {
  el.style.transitionDelay = `${(i % 3) * 100}ms`;
  revealObserver.observe(el);
});

// Trigger counter when hero is visible
const heroObserver = new IntersectionObserver(entries => {
  if (entries[0].isIntersecting) animateCounters();
}, { threshold: 0.3 });
const heroStats = document.querySelector('.hero-stats');
if (heroStats) heroObserver.observe(heroStats);

// ===== CONTACT FORM =====
const form = document.querySelector('.contact-form');
if (form) {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const btn = form.querySelector('button[type=submit]');
    const originalHTML = btn.innerHTML;
    btn.innerHTML = 'Anfrage gesendet!';
    btn.style.background = '#16a34a';
    btn.style.borderColor = '#16a34a';
    btn.disabled = true;
    setTimeout(() => {
      btn.innerHTML = originalHTML;
      btn.style.background = '';
      btn.style.borderColor = '';
      btn.disabled = false;
      form.reset();
    }, 3500);
  });
}

// ===== SPEEDOMETER INTERACTION =====
// Make speedometer respond to scroll speed
let lastScrollY = 0;
let scrollSpeed = 0;
window.addEventListener('scroll', () => {
  scrollSpeed = Math.abs(window.scrollY - lastScrollY);
  lastScrollY = window.scrollY;
  const needle = document.querySelector('.speedo-needle');
  if (needle) {
    const maxAngle = 80;
    const angle = Math.min(scrollSpeed * 3, maxAngle) - 30;
    needle.style.animationPlayState = scrollSpeed > 2 ? 'paused' : 'running';
    if (scrollSpeed > 2) {
      needle.style.transform = `rotate(${angle}deg)`;
    }
  }
}, { passive: true });

// ===== ROAD DIVIDER – trigger animation on view =====
const roadDividers = document.querySelectorAll('.road-divider');
const dividerObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const marks = entry.target.querySelectorAll('.road-mark');
    if (entry.isIntersecting) {
      marks.forEach(m => m.style.animationPlayState = 'running');
    } else {
      marks.forEach(m => m.style.animationPlayState = 'paused');
    }
  });
}, { threshold: 0.1 });
roadDividers.forEach(d => dividerObserver.observe(d));

// ===== PARALLAX HERO BG =====
window.addEventListener('scroll', () => {
  const hero = document.querySelector('.hero');
  if (!hero) return;
  const scrolled = window.scrollY;
  const speedometer = document.querySelector('.hero-speedometer');
  if (speedometer) {
    speedometer.style.transform = `translateY(${scrolled * 0.2}px)`;
  }
}, { passive: true });
