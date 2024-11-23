export const initNavigation = () => {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            mobileMenuBtn.classList.toggle('active');
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const section = document.querySelector(this.getAttribute('href'));
            if (section) {
                section.scrollIntoView({
                    behavior: 'smooth'
                });
                
                if (navLinks.classList.contains('active')) {
                    navLinks.classList.remove('active');
                    mobileMenuBtn.classList.remove('active');
                }
            }
        });
    });
};

document.addEventListener('DOMContentLoaded', () => {
    const techTags = document.querySelectorAll('.tech-tag');
    techTags.forEach((tag, index) => {
        tag.style.opacity = 0;
        tag.style.transform = 'translateY(10px)';
        tag.style.transition = `opacity 0.3s ease ${index * 0.1}s, transform 0.3s ease ${index * 0.1}s`;

        setTimeout(() => {
            tag.style.opacity = 1;
            tag.style.transform = 'translateY(0)';
        }, 500 + index * 100);
    });
});

/*DROPDOWN*/
document.addEventListener('DOMContentLoaded', function() {
    const userButton = document.querySelector('.user-button');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const chevron = document.querySelector('.chevron');

    function toggleDropdown() {
        dropdownMenu.classList.toggle('open');
        chevron.classList.toggle('open');
        userButton.setAttribute('aria-expanded', dropdownMenu.classList.contains('open'));
    }

    userButton.addEventListener('click', function(event) {
        event.stopPropagation();
        toggleDropdown();
    });

    document.addEventListener('click', function(event) {
        if (!userButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.classList.remove('open');
            chevron.classList.remove('open');
            userButton.setAttribute('aria-expanded', 'false');
        }
    });

    // Close dropdown when pressing Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && dropdownMenu.classList.contains('open')) {
            toggleDropdown();
        }
    });

    // Handle keyboard navigation within the dropdown
    dropdownMenu.addEventListener('keydown', function(event) {
        const items = Array.from(dropdownMenu.querySelectorAll('.dropdown-item'));
        const currentIndex = items.indexOf(document.activeElement);

        if (event.key === 'ArrowDown') {
            event.preventDefault();
            const nextIndex = (currentIndex + 1) % items.length;
            items[nextIndex].focus();
        } else if (event.key === 'ArrowUp') {
            event.preventDefault();
            const prevIndex = (currentIndex - 1 + items.length) % items.length;
            items[prevIndex].focus();
        }
    });
});

//Lazy loading images
const lazyLoadImages = () => {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
if (entry.isIntersecting) {
    const img = entry.target;
    img.src = img.dataset.src;
    img.classList.remove('lazy');
    observer.unobserve(img);
}
        });
    });

    const imgs = document.querySelectorAll('img.lazy');
    imgs.forEach(img => imageObserver.observe(img));
};

lazyLoadImages();

document.addEventListener('DOMContentLoaded', () => {
    const categoryButtons = document.querySelectorAll('.category-btn');
    const projectCards = document.querySelectorAll('.project-card');
    const loadingSpinner = document.getElementById('loadingSpinner');


    // Category filter functionality
    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            const category = button.textContent.trim();
            
            // Update aria-pressed attribute
            categoryButtons.forEach(btn => btn.setAttribute('aria-pressed', 'false'));
            button.setAttribute('aria-pressed', 'true');

            // Show loading spinner
            loadingSpinner.style.display = 'block';

            // Simulate loading delay
            setTimeout(() => {
                projectCards.forEach(card => {
                    const tags = card.querySelectorAll('.tag');
                    const shouldShow = category === 'Todos' || Array.from(tags).some(tag => tag.textContent === category);
                    card.style.display = shouldShow ? 'block' : 'none';
                });

                // Hide loading spinner
                loadingSpinner.style.display = 'none';
            }, 500);
        });
})
});