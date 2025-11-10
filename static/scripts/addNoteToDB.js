const saveButton = document.getElementById('save-track');
const token = document.getElementById('csrfToken').value;

saveButton.addEventListener('click', () => {
    fetch('http://127.0.0.1:8000', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        },
        body: JSON.stringify({ action: 'save' })
    })
});