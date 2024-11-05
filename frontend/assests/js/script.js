document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:5000/api/themes')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(themes => {
            const themeSelect = document.getElementById('theme-select');
            themes.forEach(theme => {
                const option = document.createElement('option');
                option.value = theme.id;
                option.textContent = theme.name;
                themeSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching themes:', error));

    document.getElementById('terrain-button').addEventListener('click', () => {
        alert('Terrain size selection dialog will open here.');
    });

    document.getElementById('materials-button').addEventListener('click', () => {
        alert('Sports materials selection dialog will open here.');
    });

    document.getElementById('activity-form').addEventListener('submit', (event) => {
        event.preventDefault();
        alert('Form submitted!');
    });
});
