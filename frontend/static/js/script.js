// script.js - Real-Time Frontend
document.addEventListener('DOMContentLoaded', () => {
    const themeSelect = document.getElementById('theme-select');
    const socket = io('http://localhost:3000');

    socket.on('updateThemes', (themes) => {
        themeSelect.innerHTML = '<option value="">Choose a theme...</option>';
        themes.forEach(theme => {
            const option = document.createElement('option');
            option.value = theme.id;
            option.textContent = theme.name;
            themeSelect.appendChild(option);
        });
    });

    document.getElementById('terrain-button').addEventListener('click', () => {
        alert('Terrain size selection dialog will open here.');
    });

    document.getElementById('materials-button').addEventListener('click', () => {
        alert('Sports materials selection dialog will open here.');
    });

    document.getElementById('complete-button').addEventListener('click', () => {
        alert('Form submission triggered!');
    });
});
