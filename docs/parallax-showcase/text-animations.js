/**
 * TEXT ANIMATIONS SHOWCASE - JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
    initCursorGlow();
    initTypewriter();
    initScrambleText();
    initShadowPop();
    initMatrixRain();
    initParticleText();
    initBackToTop();
    initScrollAnimations();
});

/**
 * Cursor Glow Effect
 */
function initCursorGlow() {
    const glow = document.getElementById('cursorGlow');
    if (!glow) return;

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let currentX = mouseX;
    let currentY = mouseY;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    function animate() {
        currentX += (mouseX - currentX) * 0.1;
        currentY += (mouseY - currentY) * 0.1;

        glow.style.left = `${currentX}px`;
        glow.style.top = `${currentY}px`;

        requestAnimationFrame(animate);
    }

    animate();
}

/**
 * Typewriter Effect
 */
function initTypewriter() {
    const element = document.querySelector('.typewriter-text');
    if (!element) return;

    const text = element.dataset.text || '';
    let index = 0;
    element.textContent = '';

    function type() {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(type, 100);
        } else {
            // Reset and restart after delay
            setTimeout(() => {
                index = 0;
                element.textContent = '';
                type();
            }, 3000);
        }
    }

    // Start after a short delay
    setTimeout(type, 500);
}

/**
 * Scramble Text Effect
 */
function initScrambleText() {
    const element = document.querySelector('.scramble-text');
    const button = document.querySelector('.scramble-btn');
    if (!element || !button) return;

    const finalText = element.dataset.final || 'DECRYPTED';
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*';
    let isAnimating = false;

    function scramble() {
        if (isAnimating) return;
        isAnimating = true;

        let iteration = 0;
        const interval = setInterval(() => {
            element.textContent = finalText
                .split('')
                .map((char, i) => {
                    if (i < iteration) {
                        return finalText[i];
                    }
                    return chars[Math.floor(Math.random() * chars.length)];
                })
                .join('');

            if (iteration >= finalText.length) {
                clearInterval(interval);
                isAnimating = false;
            }

            iteration += 1 / 3;
        }, 30);
    }

    function reset() {
        element.textContent = 'X'.repeat(finalText.length);
    }

    button.addEventListener('mouseenter', scramble);
    button.addEventListener('mouseleave', () => {
        setTimeout(reset, 500);
    });
}

/**
 * Shadow Pop Effect (follows mouse)
 */
function initShadowPop() {
    const element = document.querySelector('.shadow-pop-text');
    if (!element) return;

    element.addEventListener('mousemove', (e) => {
        const rect = element.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        const shadowX = -x / 10;
        const shadowY = -y / 10;

        element.style.textShadow = `
            ${shadowX}px ${shadowY}px 0 #667eea,
            ${shadowX * 2}px ${shadowY * 2}px 0 #764ba2,
            ${shadowX * 3}px ${shadowY * 3}px 0 #f093fb
        `;
        element.style.transform = `translate(${x / 20}px, ${y / 20}px)`;
    });

    element.addEventListener('mouseleave', () => {
        element.style.textShadow = '';
        element.style.transform = '';
    });
}

/**
 * Matrix Rain Effect
 */
function initMatrixRain() {
    const canvas = document.getElementById('matrixCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');

    // Set canvas size
    function resize() {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    const chars = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789';
    const charArray = chars.split('');
    const fontSize = 14;
    const columns = canvas.width / fontSize;
    const drops = Array(Math.floor(columns)).fill(1);

    function draw() {
        ctx.fillStyle = 'rgba(10, 10, 15, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = '#00ff00';
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < drops.length; i++) {
            const char = charArray[Math.floor(Math.random() * charArray.length)];
            ctx.fillText(char, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }

    setInterval(draw, 35);
}

/**
 * Particle Text Effect
 */
function initParticleText() {
    const canvas = document.getElementById('particleCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = canvas.offsetWidth * window.devicePixelRatio;
        canvas.height = canvas.offsetHeight * window.devicePixelRatio;
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }
    resize();
    window.addEventListener('resize', resize);

    const particles = [];
    const text = 'PARTICLES';
    const fontSize = Math.min(canvas.offsetWidth / 8, 80);

    // Draw text to get pixel data
    ctx.font = `bold ${fontSize}px Arial`;
    ctx.fillStyle = '#667eea';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    const textWidth = ctx.measureText(text).width;
    const startX = (canvas.offsetWidth - textWidth) / 2;
    const startY = canvas.offsetHeight / 2;

    ctx.fillText(text, canvas.offsetWidth / 2, canvas.offsetHeight / 2);

    // Get pixel data
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Create particles from text pixels
    const gap = 4;
    for (let y = 0; y < canvas.height; y += gap) {
        for (let x = 0; x < canvas.width; x += gap) {
            const index = (y * canvas.width + x) * 4;
            if (imageData.data[index + 3] > 128) {
                particles.push({
                    x: x / window.devicePixelRatio,
                    y: y / window.devicePixelRatio,
                    baseX: x / window.devicePixelRatio,
                    baseY: y / window.devicePixelRatio,
                    size: 2,
                    color: `rgb(${imageData.data[index]}, ${imageData.data[index + 1]}, ${imageData.data[index + 2]})`
                });
            }
        }
    }

    let mouseX = 0;
    let mouseY = 0;

    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouseX = e.clientX - rect.left;
        mouseY = e.clientY - rect.top;
    });

    canvas.addEventListener('mouseleave', () => {
        mouseX = -1000;
        mouseY = -1000;
    });

    function animate() {
        ctx.clearRect(0, 0, canvas.offsetWidth, canvas.offsetHeight);

        particles.forEach((p) => {
            const dx = mouseX - p.x;
            const dy = mouseY - p.y;
            const dist = Math.sqrt(dx * dx + dy * dy);
            const maxDist = 80;

            if (dist < maxDist) {
                const force = (maxDist - dist) / maxDist;
                const angle = Math.atan2(dy, dx);
                p.x -= Math.cos(angle) * force * 5;
                p.y -= Math.sin(angle) * force * 5;
            } else {
                p.x += (p.baseX - p.x) * 0.1;
                p.y += (p.baseY - p.y) * 0.1;
            }

            ctx.fillStyle = p.color;
            ctx.fillRect(p.x, p.y, p.size, p.size);
        });

        requestAnimationFrame(animate);
    }

    animate();
}

/**
 * Back to Top Button
 */
function initBackToTop() {
    const button = document.getElementById('backToTop');
    if (!button) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            button.classList.add('visible');
        } else {
            button.classList.remove('visible');
        }
    });

    button.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Scroll-triggered Animations
 */
function initScrollAnimations() {
    // Kinetic typography restart on scroll into view
    const kineticWords = document.querySelectorAll('.kinetic-word');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                // Reset animation
                entry.target.style.animation = 'none';
                entry.target.offsetHeight; // Trigger reflow
                entry.target.style.animation = '';
            }
        });
    }, { threshold: 0.5 });

    kineticWords.forEach((word) => observer.observe(word));

    // Stroke animation restart
    const strokeText = document.querySelector('.stroke-text');
    if (strokeText) {
        const strokeObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'none';
                    entry.target.offsetHeight;
                    entry.target.style.animation = 'strokeDraw 3s ease forwards infinite';
                }
            });
        }, { threshold: 0.5 });

        strokeObserver.observe(strokeText);
    }
}

/**
 * Add staggered animations for bounce text letters
 */
(function initBouncedelay() {
    const bounceText = document.querySelector('.bounce-text');
    if (!bounceText) return;

    const spans = bounceText.querySelectorAll('span');
    spans.forEach((span, index) => {
        span.style.transitionDelay = `${index * 0.05}s`;
    });
})();

/**
 * Flip text hover effect enhancement
 */
(function initFlipTextEffect() {
    const flipText = document.querySelector('.flip-text');
    if (!flipText) return;

    const spans = flipText.querySelectorAll('span');
    spans.forEach((span, index) => {
        span.style.transitionDelay = `${index * 0.1}s`;
    });
})();

/**
 * Elastic text stagger
 */
(function initElasticStagger() {
    const elasticText = document.querySelector('.elastic-text');
    if (!elasticText) return;

    const spans = elasticText.querySelectorAll('span');
    spans.forEach((span, index) => {
        span.style.transitionDelay = `${index * 0.05}s`;
    });
})();
