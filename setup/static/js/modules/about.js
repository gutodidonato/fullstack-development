export const initAbout = () => {
    createMatrixRain();
    initStatsAnimation();
    initTypingEffect();
};

const createMatrixRain = () => {
    const canvas = document.createElement('canvas');
    const container = document.querySelector('.matrix-rain');
    if (!container) return;

    // Configurar o estilo para preencher a div completamente
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    container.appendChild(canvas);

    const ctx = canvas.getContext('2d');

    let fontSize = 14;
    let columns;
    let drops;

    const resizeCanvas = () => {
        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;
        columns = Math.floor(canvas.width / fontSize);
        drops = Array(columns).fill(1); 
    };

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const chars = '01';

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    
        ctx.fillStyle = '#00ff41';
        ctx.font = `${fontSize}px monospace`;
    
        drops.forEach((y, i) => {
            const char = chars[Math.floor(Math.random() * chars.length)];
            const x = i * fontSize;
            ctx.fillText(char, x, y * fontSize);
    
            if (y * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i] += 0.3; // Reduzir a velocidade
        });
    

        requestAnimationFrame(draw);
    }

    draw();
};

const initStatsAnimation = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statCard = entry.target;
                const value = parseInt(statCard.dataset.value);
                const valueDisplay = statCard.querySelector('.stat-value');
                
                animateValue(valueDisplay, 0, value, 2000);
                observer.unobserve(statCard);
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.stat-card').forEach(card => observer.observe(card));
};

const animateValue = (element, start, end, duration) => {
    let current = start;
    const increment = (end - start) / (duration / 16);
    const animate = () => {
        current += increment;
        element.textContent = Math.floor(current);
        
        if (current < end) {
            requestAnimationFrame(animate);
        } else {
            element.textContent = end;
        }
    };
    animate();
};



const initTypingEffect = () => {
    const text = document.querySelector('.typing-text');
    if (!text) return;

    const content = text.textContent;
    text.textContent = '';
    let index = 0;

    function type() {
        if (index < content.length) {
            text.textContent += content.charAt(index);
            index++;
            setTimeout(type, 50);
        }
    }

    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            type();
            observer.unobserve(text);
        }
    });

    observer.observe(text);
};


/*MODAL CONTATO*/
document.addEventListener('DOMContentLoaded', () => {
    const connectOptions = document.querySelectorAll('.connect-option');
    const modal = document.getElementById('connectModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalBody = document.getElementById('modalBody');
    const closeModal = document.querySelector('.close-modal');

    connectOptions.forEach(option => {
        option.addEventListener('click', () => {
            const platform = option.getAttribute('data-platform');
            openModal(platform);
        });
    });

    closeModal.addEventListener('click', () => {
        modal.classList.remove('active');
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    });

    function openModal(platform) {
        modalTitle.textContent = `Connect via ${platform.charAt(0).toUpperCase() + platform.slice(1)}`;
        
        switch(platform) {
            case 'github':
                modalBody.innerHTML = '<p>Check out my projects on GitHub:</p><a href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer">github.com/yourusername</a>';
                break;
            case 'linkedin':
                modalBody.innerHTML = '<p>Let\'s connect on LinkedIn:</p><a href="https://www.linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">linkedin.com/in/yourusername</a>';
                break;
            case 'email':
                modalBody.innerHTML = `
                    <form class="connect-form">
                        <input type="text" placeholder="Your Name" required>
                        <input type="email" placeholder="Your Email" required>
                        <textarea placeholder="Your Message" rows="4" required></textarea>
                        <button type="submit">Send Message</button>
                    </form>
                `;
                const form = modalBody.querySelector('form');
                form.addEventListener('submit', (e) => {
                    e.preventDefault();
                    alert('Message sent successfully!');
                    modal.classList.remove('active');
                });
                break;
        }

        modal.classList.add('active');
    }
});
document.addEventListener('DOMContentLoaded', () => {
    const techBackground = document.getElementById('background-footer');
    const numberOfLines = 15;
    const numberOfCircles = 20;

    for (let i = 0; i < numberOfLines; i++) {
        const line = document.createElement('div');
        line.classList.add('footer-tech-line');
        line.style.top = `${Math.random() * 100}%`;
        line.style.animationDelay = `${Math.random() * 8}s`;
        techBackground.appendChild(line);
    }

    // Create tech circles
    for (let i = 0; i < numberOfCircles; i++) {
        const circle = document.createElement('div');
        circle.classList.add('tech-circle');
        circle.style.width = circle.style.height = `${Math.random() * 50 + 10}px`;
        circle.style.left = `${Math.random() * 100}%`;
        circle.style.top = `${Math.random() * 100}%`;
        circle.style.animationDuration = `${Math.random() * 20 + 10}s`;
        techBackground.appendChild(circle);
    }

});