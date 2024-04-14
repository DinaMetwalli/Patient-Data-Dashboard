document.addEventListener('DOMContentLoaded', () => {

    const setupPasskeysButton = document.getElementById('setup');
    const inputPasskeysButton = document.getElementById('entry');

    const entryPass = document.getElementById('entry-pass');
    const importPass = document.getElementById('import-pass');
    const exportPass = document.getElementById('export-pass');

    const entryInput = document.getElementById('entry-input');

    setupPasskeysButton.addEventListener('click', async () => {

        const entry_pass = entryPass.value;
        const import_pass = importPass.value;
        const export_pass = exportPass.value;

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

        } catch (error) {
            console.error('Error setting up passkeys:', error);
        }
    });

    inputPasskeysButton.addEventListener('click', async () => {

        const entry_password = entryInput.value;

        try {
            const response = await fetch('http://localhost:6002/auth-entry', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ entry_password })
            });

            if (!response.ok) {
                throw new Error('Failed to generate report');
            }

        } catch (error) {
            console.error('Error generating report:', error);
        }
    });
});
