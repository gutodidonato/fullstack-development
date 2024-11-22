export const levelSystem = {
    currentXP: 0,
    currentLevel: 1,
    xpNeeded: 100,
    timeInterval: 1000,
    xpPerInterval: 1,

    init() {
        this.updateDisplay();
        this.startXPGain();
        this.setupMobileMenu();
    },

    gainXP(amount) {
        this.currentXP += amount;
        if (this.currentXP >= this.xpNeeded) {
            this.levelUp();
        }
        this.updateDisplay();
    },

    levelUp() {
        this.currentLevel++;
        this.currentXP = 0;
        this.xpNeeded = Math.floor(this.xpNeeded * 1.5);
        
        const notification = document.createElement('div');
        notification.className = 'level-up-notification';
        notification.textContent = `Level Up! You're now level ${this.currentLevel}`;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    },

    updateDisplay() {
        document.getElementById('current-level').textContent = this.currentLevel;
        document.getElementById('current-xp').textContent = this.currentXP;
        document.getElementById('xp-needed').textContent = this.xpNeeded;
        
        const progressPercentage = (this.currentXP / this.xpNeeded) * 100;
        const progressBar = document.getElementById('xp-progress');
        progressBar.style.width = `${progressPercentage}%`;
    },

    setupMobileMenu() {
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const navContent = document.querySelector('.nav-content');
        
        if (mobileMenuBtn && navContent) {
            mobileMenuBtn.addEventListener('click', () => {
                navContent.classList.toggle('active');
                mobileMenuBtn.classList.toggle('active');
            });
        }
    },

    startXPGain() {
        setInterval(() => {
            if (document.visibilityState === 'visible') {
                this.gainXP(this.xpPerInterval);
            }
        }, this.timeInterval);
    }
};