// Minimal - nur sanfte Einblend-Animation beim Scrollen
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.hero').forEach(hero => {
        hero.style.opacity = '0';
        hero.style.transform = 'translateY(20px)';
        hero.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(hero);
    });

    // Erste Sektion sofort sichtbar
    const firstHero = document.querySelector('.hero');
    if (firstHero) {
        firstHero.style.opacity = '1';
        firstHero.style.transform = 'translateY(0)';
    }
});
