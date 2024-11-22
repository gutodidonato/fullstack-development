export const initAnimations = () => {
    const observerOptions = {
        root: null,
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                if (entry.target.classList.contains('metric-value')) {
                    animateMetric(entry.target);
                }
                
                if (entry.target.classList.contains('progress')) {
                    const width = entry.target.getAttribute('data-width');
                    if (width) {
                        entry.target.style.width = width + '%';
                    }
                }
            }
        });
    }, observerOptions);

    document.querySelectorAll('.about, .skills-section, .projects, .contact, .metric-value, .progress')
        .forEach(element => observer.observe(element));
};

export const animateMetric = (element) => {
    const target = parseInt(element.getAttribute('data-count'), 10);
    let current = 0;
    const duration = 2000;
    const step = target / (duration / 16);

    function updateValue() {
        current = Math.min(current + step, target);
        element.textContent = Math.round(current);
        
        if (current < target) {
            requestAnimationFrame(updateValue);
        }
    }

    updateValue();
};
document.addEventListener('DOMContentLoaded', () => {
            const skillCards = document.querySelectorAll('.skill-card');

            skillCards.forEach(card => {
                const progressBar = card.querySelector('.skill-progress-bar');
                const progress = progressBar.getAttribute('data-progress');

                setTimeout(() => {
                    progressBar.style.width = `${progress}%`;
                }, 300);

                card.addEventListener('click', () => {
                    card.classList.toggle('active');
                });
            });

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate');
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.skills-category').forEach(category => {
                observer.observe(category);
            });
        });


        /*
        SKILLSS
        */

        document.addEventListener('DOMContentLoaded', () => {
            const skillCards = document.querySelectorAll('.skill-card');

            skillCards.forEach(card => {
                const progressBar = card.querySelector('.skill-progress-bar');
                const progress = progressBar.getAttribute('data-progress');

                setTimeout(() => {
                    progressBar.style.width = `${progress}%`;
                }, 300);

                card.addEventListener('click', () => {
                    card.classList.toggle('active');
                });
            });

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate');
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.skills-category').forEach(category => {
                observer.observe(category);
            });
        });