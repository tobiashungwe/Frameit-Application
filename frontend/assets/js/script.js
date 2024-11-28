document.addEventListener('DOMContentLoaded', () => {
    // Fetch themes and populate the dropdown
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

    // Add click events for terrain and materials buttons
    document.getElementById('terrain-button').addEventListener('click', () => {
        alert('Terrain size selection dialog will open here.');
    });

    document.getElementById('materials-button').addEventListener('click', () => {
        alert('Sports materials selection dialog will open here.');
    });

    // File input and error message handling
    const pdfUpload = document.getElementById('pdf-upload');
    const fileError = document.getElementById('file-error');

    // Clear error message when a new file is selected
    pdfUpload.addEventListener('change', () => {
        fileError.textContent = ""; // Clear error message
    });

    // Add submit event listener with validation
    document.getElementById('activity-form').addEventListener('submit', (event) => {
        event.preventDefault();

        const file = pdfUpload.files[0];
        const validTypes = ["application/pdf"];
        const maxSize = 5 * 1024 * 1024; // 5 MB

        if (!file) {
            fileError.textContent = "Please select a file to upload.";
            return;
        }

        if (!validTypes.includes(file.type)) {
            fileError.textContent = "Invalid file type. Only PDF files are allowed.";
            return;
        }

        if (file.size > maxSize) {
            fileError.textContent = "File size exceeds the 5MB limit.";
            return;
        }

        // If validation passes
        fileError.textContent = ""; // Clear any residual error message
        alert('File is valid. Form submitted!');
        // Proceed with form submission logic (e.g., send file to server)
    });
});
