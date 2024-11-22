export const initTerminal = () => {
    const terminalContent = document.querySelector('.typing-effect');
    if (terminalContent) {
        const text = `const developer = {
    name: "Your Name",
    role: "Full Stack Developer",
    skills: ["JavaScript", "React", "Node.js"],
    passion: "Building amazing web experiences"
};`;

        let index = 0;
        function typeText() {
            if (index < text.length) {
                terminalContent.textContent += text.charAt(index);
                index++;
                setTimeout(typeText, 50);
            }
        }

        typeText();
    }
};