// JavaScript file for frontend interactivity

document.addEventListener('DOMContentLoaded', function () {
    console.log('AgriP scripts loaded.');

    // Example: Handle form submissions via AJAX
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', async event => {
            event.preventDefault();
            const formData = new FormData(form);
            const action = form.getAttribute('action');
            const response = await fetch(action, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            console.log(data);

            // Example: Render results dynamically
            const resultContainer = document.querySelector('#results');
            if (resultContainer) {
                resultContainer.innerHTML = JSON.stringify(data, null, 2);
            }
        });
    });
});
