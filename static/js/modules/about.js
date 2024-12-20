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

document.addEventListener('DOMContentLoaded', () => {
    const categoryButtons = document.querySelectorAll('.category-btn');
    const projectsGrid = document.getElementById('projectsGrid');
    const paginationContainer = document.getElementById('pagination');
    const loadingSpinner = document.getElementById('loadingSpinner');

    categoryButtons.forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();

            const categoryId = button.getAttribute('data-id'); // Obtém o ID da categoria
            loadingSpinner.style.display = 'block'; // Mostra o spinner de carregamento

            console.log(categoryId)
            console.log(`/projetos/${categoryId}}`)

            fetch(`/projetos/${categoryId ? categoryId + '/' : ''}`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest', // Necessário para a view reconhecer como AJAX
                    'Content-Type': 'application/json', // Indica que esperamos um JSON na resposta
                },
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(`Erro: ${response.status}`); // Captura o status HTTP (como 500)
                    }
                    return response.json(); // Tenta parsear a resposta como JSON
                })
                .then((data) => {
                    // Insere os projetos e a paginação no DOM
                    document.getElementById('projectsGrid').innerHTML = data.projects_html;
                    document.getElementById('pagination').innerHTML = data.pagination_html;
                })
                .catch((error) => {
                    console.error('Erro ao carregar os dados:', error); // Log do erro
                });
        });
    });
});
