const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const importPasskeysButton = document.getElementById('uploadBtn');
const importPass = document.getElementById('passkey');
const resultElement = document.getElementById('message');
let loadingModal;

if (window.opener && window.opener.loadingModal) {
    loadingModal = window.opener.loadingModal;
} else {
    loadingModal = document.getElementById('loadingModal');
}

uploadBtn.addEventListener('click', async () => {
    const import_pass = importPass.value;

    if (import_pass === "") {
        resultElement.textContent = `Please enter import passkey.`;
        return;
    }

    try {
        const authResponse = await fetch('http://localhost:6002/auth-import', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ import_pass })
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

    fileInput.click();
});

fileInput.addEventListener('change', async () => {
    if (loadingModal) {
        loadingModal.style.display = 'block';

        try {
            const filePath = fileInput.files[0].path;

            // Send POST request using fetch API
            const response = await fetch('http://localhost:6002/upload', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ filePath })
            });

            if (!response.ok) {
                throw new Error('Failed to upload file');
            }

            const data = await response.json();
            console.log(data); // Log response from the server

            if (data.success) {
                window.opener.alert('CSV file uploaded successfully!');
                location.reload();
            } else {
                alert('Error uploading file: ' + data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            window.opener.alert('Error uploading file');
        } finally {
            if (loadingModal) {
                loadingModal.style.display = 'none';
                document.body.removeChild(loadingModal);
            }
        }
    } else {
        console.error('Loading modal not found');
    }

    window.close();
});

function closeModal() {
    if (loadingModal) {
        loadingModal.style.display = 'none';
    }
}
