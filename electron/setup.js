document.addEventListener('DOMContentLoaded', () => {

    const setupPasskeysButton = document.getElementById('setup-btn');
    const resultElement = document.getElementById('result');

    const entryPass = document.getElementById('entry-pass');
    const importPass = document.getElementById('import-pass');
    const exportPass = document.getElementById('export-pass');

    setupPasskeysButton.addEventListener('click', async () => {

        const entry_pass = entryPass.value;
        const import_pass = importPass.value;
        const export_pass = exportPass.value;

        if (entry_pass == "" || import_pass == "" || export_pass == "") {
            resultElement.textContent = `All fields must be filled in before proceeding.`;
            return;
        }

        try {
            const response = await fetch('http://localhost:6002/setup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ entry_pass, import_pass, export_pass })
            });

            if (!response.ok) {
                throw new Error('Failed to setup passkeys');
            }
            // Parse the response JSON
            const data = await response.json();
            console.log('Response:', data);

            window.location.href = 'login.html';

        } catch (error) {
            console.error('Error setting up passkeys:', error);
        }
    });
});
