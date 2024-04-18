const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
const loadingModal = document.getElementById('loadingModal');

uploadBtn.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', async () => {
    loadingModal.style.display = 'block';

    try {
        const filePath = fileInput.files[0].path;

        // Send POST request using fetch API
        const response = await fetch('http://127.0.0.1:6002/upload', {
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
            alert('CSV file uploaded successfully!');
            location.reload();
        } else {
            alert('Error uploading file: ' + data.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error uploading file');
    } finally {
        loadingModal.style.display = 'none';
    }
});

function closeModal() {
    loadingModal.style.display = 'none';
}