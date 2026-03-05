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

// ===== TACHOMETER ANIMATION =====
const tachoWraps = document.querySelectorAll('.tacho-wrap');
let tachosAnimated = false;

function animateTachos() {
  if (tachosAnimated) return;
  tachosAnimated = true;
  tachoWraps.forEach((wrap, i) => {
    const percent = parseFloat(wrap.dataset.percent) / 100;
    const maxDash = parseFloat(wrap.dataset.maxDash);
    const arc = wrap.querySelector('.tacho-arc');
    const needle = wrap.querySelector('.tacho-needle');
    const num = wrap.querySelector('.tacho-num');
    const delay = i * 150;

    setTimeout(() => {
      // Animate arc fill: 0% = left, 100% = right (counterclockwise over top)
      if (arc) arc.style.strokeDasharray = `${maxDash * percent} ${maxDash}`;
      // Animate needle: rotate(0deg) = pointing left, rotate(180deg) = pointing right
      if (needle) needle.style.transform = `rotate(${180 * percent}deg)`;
      // Animate counter
      if (num) {
        const target = parseInt(num.dataset.target);
        let current = 0;
        const steps = 40;
        const inc = target / steps;
        let step = 0;
        const timer = setInterval(() => {
          step++;
          current = Math.min(Math.round(inc * step), target);
          num.textContent = current;
          if (step >= steps) clearInterval(timer);
        }, 1600 / steps);
      }
    }, delay);
  });
}

// Legacy counter support (kept for other potential uses)
function animateCounters() {}

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

// Trigger tachometers when hero is visible
const heroObserver = new IntersectionObserver(entries => {
  if (entries[0].isIntersecting) animateTachos();
}, { threshold: 0.2 });
const tachoStats = document.querySelector('.hero-tacho-stats');
if (tachoStats) heroObserver.observe(tachoStats);

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
