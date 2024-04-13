const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('uploadBtn');

uploadBtn.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', () => {
    const filePath = fileInput.files[0].path;

    // Send POST request using fetch API
    fetch('http://localhost:6002/upload/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ filePath }),
        mode: 'cors',
        credentials: 'same-origin'
    })
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log response from the Flask server
            if (data.success) {
                alert('CSV file uploaded successfully!');
            } else {
                alert('Error uploading file: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error uploading file');
        });
});