document.addEventListener('DOMContentLoaded', () => {
    const importPasskeysButton = document.getElementById('import-btn');

    const importPass = document.getElementById('passkey');
    const resultElement = document.getElementById('message');

    importPasskeysButton.addEventListener('click', async () => {

        const import_pass = importPass.value;

        if (import_pass == "") {
            resultElement.textContent = `Please enter import passkey.`;
            return;
        }

        try {
            const response = await fetch('http://localhost:6002/auth-import', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ import_pass })
            });

            if (!response.ok) {
                throw new Error('Failed to validate passkey');
            }
            // Parse the response JSON
            const responseData = await response.json();
            const result = responseData.success;
            const message = responseData.message;

            if (!result) {
                resultElement.textContent = `Result: ${message}`;
            }

        } catch (error) {
            console.error('Error validating passkey:', error);
        }
    });
});