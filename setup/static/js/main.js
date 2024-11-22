import { initAnimations } from './modules/animations.js';
import { initNavigation } from './modules/navigation.js';
import { initTerminal } from './modules/terminal.js';
import { levelSystem } from './modules/levelSystem.js';
import { initAbout } from './modules/about.js';

document.addEventListener('DOMContentLoaded', () => {
    initAnimations();
    initNavigation();
    initTerminal();
    levelSystem.init();
    initAbout();
});