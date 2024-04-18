document.addEventListener('DOMContentLoaded', () => {

    const inputPasskeysButton = document.getElementById('entry-btn');
    const entryInput = document.getElementById('entry-input');
    const resultElement = document.getElementById('result');

    inputPasskeysButton.addEventListener('click', async () => {

        const entry_pass = entryInput.value;
        try {
            const response = await fetch('http://localhost:6002/auth-entry', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ entry_pass })
            });

            if (!response.ok) {
                throw new Error('Failed to validate passkey');
            }

            const responseData = await response.json();
            const result = responseData.success;
            const message = responseData.message;

            if (!result) {
                resultElement.textContent = `Result: ${message}`;
            }
            else {
                window.location.href = 'index.html';
            }
        } catch (error) {
            console.error('Error validating passkey:', error);
        }
    });
});
