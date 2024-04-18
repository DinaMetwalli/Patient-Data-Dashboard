const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');
let loadingModal;

// Check if the script is executing in the main window or in an authentication window
if (window.opener && window.opener.loadingModal) {
    loadingModal = window.opener.loadingModal; // Access the loading modal from the main window
} else {
    loadingModal = document.getElementById('loadingModal'); // Access the loading modal from the current window
}

uploadBtn.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', async () => {
    console.log("HI SISTERS!!!");
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
            // console.log(data); // Log response from the server

            if (data.success) {
                window.opener.alert('CSV file uploaded successfully!'); //check this!
                location.reload();
            } else {
                alert('Error uploading file: ' + data.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error uploading file');
        } finally {
            if (loadingModal) {
                // Detach the loading modal from the document body
                loadingModal.style.display = 'none';
                document.body.removeChild(loadingModal);
            }
        }
    } else {
        console.error('Loading modal not found');
    }

    // Close the window after detaching the loading modal
    window.close();
});

function closeModal() {
    if (loadingModal) {
        loadingModal.style.display = 'none';
    }
}
