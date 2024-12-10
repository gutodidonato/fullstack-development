export const initTerminal = () => {
    const terminalContent = document.querySelector('.typing-effect');
    if (terminalContent) {
        const text = `const developer = {
    name: "Luis Augusto Didonato",
    role: "Full Stack Developer",
    skills: ["Python", "Javascript", "Typescript", ...],
    passion: "Help peoples achieve their dreams"
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