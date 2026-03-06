// ===== PERSPECTIVE ROAD ANIMATION =====
(function () {
  const canvas = document.getElementById('roadCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width = canvas.parentElement.offsetWidth;
    canvas.height = canvas.parentElement.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  function draw(ts) {
    const W = canvas.width;
    const H = canvas.height;
    ctx.clearRect(0, 0, W, H);

    // Vanishing point: horizontally centered, 30% from top
    const vpX = W * 0.5;
    const vpY = H * 0.28;

    // Road edges at bottom of canvas
    const leftEdge  = W * 0.12;
    const rightEdge = W * 0.88;
    // Road edges at vanishing point (narrow)
    const vpLeft  = vpX - W * 0.03;
    const vpRight = vpX + W * 0.03;

    // Interpolate road x at depth t (0=vanishing, 1=bottom)
    function roadX(t, side) {
      const base = side === 'left' ? leftEdge : rightEdge;
      const top  = side === 'left' ? vpLeft   : vpRight;
      return top + (base - top) * t;
    }
    function roadY(t) {
      return vpY + (H - vpY) * t;
    }

    // --- Road surface ---
    const surfGrad = ctx.createLinearGradient(0, vpY, 0, H);
    surfGrad.addColorStop(0,   'rgba(10,10,20,0)');
    surfGrad.addColorStop(0.25,'rgba(12,12,22,0.55)');
    surfGrad.addColorStop(1,   'rgba(8,8,16,0.92)');

    ctx.beginPath();
    ctx.moveTo(vpLeft,  vpY);
    ctx.lineTo(vpRight, vpY);
    ctx.lineTo(rightEdge, H);
    ctx.lineTo(leftEdge,  H);
    ctx.closePath();
    ctx.fillStyle = surfGrad;
    ctx.fill();

    // --- Edge lines (white) ---
    ctx.strokeStyle = 'rgba(255,255,255,0.65)';
    ctx.lineWidth   = 2;
    ctx.beginPath();
    ctx.moveTo(vpLeft,   vpY);
    ctx.lineTo(leftEdge, H);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(vpRight,   vpY);
    ctx.lineTo(rightEdge, H);
    ctx.stroke();

    // Thin horizon glow
    const horizGrad = ctx.createLinearGradient(vpLeft, vpY, vpRight, vpY);
    horizGrad.addColorStop(0, 'transparent');
    horizGrad.addColorStop(0.5, 'rgba(212,0,116,0.6)');
    horizGrad.addColorStop(1, 'transparent');
    ctx.strokeStyle = horizGrad;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(vpLeft - 10, vpY);
    ctx.lineTo(vpRight + 10, vpY);
    ctx.stroke();

    // --- Animated center dashes ---
    // Speed: seconds per cycle-length
    const speed       = 0.55;
    const cycleLen    = 0.12;  // t-space per dash+gap
    const dashFrac    = 0.055; // how much of cycle is dash
    const animOffset  = ((ts / 1000) * speed) % cycleLen;

    for (let i = -1; i < 14; i++) {
      const tStart = i * cycleLen + animOffset;
      const tEnd   = tStart + cycleLen * dashFrac;
      if (tStart >= 1 || tEnd <= 0.01) continue;
      const t0 = Math.max(0.01, tStart);
      const t1 = Math.min(1.0, tEnd);

      // Width of dash based on perspective (wider = closer)
      const halfW0 = Math.max(1, (roadX(t0, 'right') - roadX(t0, 'left')) * 0.025);
      const halfW1 = Math.max(1, (roadX(t1, 'right') - roadX(t1, 'left')) * 0.025);

      // Fade near horizon
      const alpha = Math.min(1, t0 * 5) * 0.9;
      ctx.fillStyle = `rgba(255, 220, 50, ${alpha})`;

      ctx.beginPath();
      ctx.moveTo(vpX - halfW0, roadY(t0));
      ctx.lineTo(vpX + halfW0, roadY(t0));
      ctx.lineTo(vpX + halfW1, roadY(t1));
      ctx.lineTo(vpX - halfW1, roadY(t1));
      ctx.closePath();
      ctx.fill();
    }

    // --- Side lane markers (subtle white dashes on shoulders) ---
    [{ side: 'left', frac: 0.33 }, { side: 'right', frac: 0.67 }].forEach(({ frac }) => {
      for (let i = -1; i < 14; i++) {
        const tStart = i * cycleLen * 1.4 + animOffset * 0.9;
        const tEnd   = tStart + cycleLen * dashFrac * 0.8;
        if (tStart >= 1 || tEnd <= 0.01) continue;
        const t0 = Math.max(0.01, tStart);
        const t1 = Math.min(1.0, tEnd);

        const x0 = roadX(t0, 'left') + (roadX(t0, 'right') - roadX(t0, 'left')) * frac;
        const x1 = roadX(t1, 'left') + (roadX(t1, 'right') - roadX(t1, 'left')) * frac;
        const hw0 = Math.max(0.5, (roadX(t0, 'right') - roadX(t0, 'left')) * 0.01);
        const hw1 = Math.max(0.5, (roadX(t1, 'right') - roadX(t1, 'left')) * 0.01);
        const alpha = Math.min(1, t0 * 5) * 0.35;

        ctx.fillStyle = `rgba(255,255,255,${alpha})`;
        ctx.beginPath();
        ctx.moveTo(x0 - hw0, roadY(t0));
        ctx.lineTo(x0 + hw0, roadY(t0));
        ctx.lineTo(x1 + hw1, roadY(t1));
        ctx.lineTo(x1 - hw1, roadY(t1));
        ctx.closePath();
        ctx.fill();
      }
    });

    // Bottom glow (headlights feel)
    const glowGrad = ctx.createRadialGradient(vpX, H, 0, vpX, H, W * 0.4);
    glowGrad.addColorStop(0,   'rgba(212,0,116,0.12)');
    glowGrad.addColorStop(0.6, 'rgba(100,0,200,0.06)');
    glowGrad.addColorStop(1,   'transparent');
    ctx.fillStyle = glowGrad;
    ctx.fillRect(0, H * 0.6, W, H * 0.4);

    requestAnimationFrame(draw);
  }

  requestAnimationFrame(draw);
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
