const exportBtn = document.getElementById('exportBtn');
const exportPass = document.getElementById('passkey');
const resultElement = document.getElementById('message');

exportBtn.addEventListener('click', async () => {
    const export_pass = exportPass.value;

    if (export_pass === "") {
        resultElement.textContent = `Please enter export passkey.`;
        return;
    }

    try {
        const authResponse = await fetch('http://localhost:6002/auth-export', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ export_pass })
        });

        if (!authResponse.ok) {
            throw new Error('Failed to validate passkey');
        }

        const authData = await authResponse.json();
        const authResult = authData.success;

        if (!authResult) {
            resultElement.textContent = `Result: ${authData.message}`;
            return;
        }
    } catch (error) {
        console.error('Error validating passkey:', error);
        return;
    }
});