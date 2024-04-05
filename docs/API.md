# Flask API and JS Communication
This guide defines how the communication between the Electron UI and the Python backend is done through JavaScript and the Flask API endpoints.

## JavaScript Requests
* Requests could be made to the endpoints using JS. These requests will contain the user input data from the UI, and are sent over to the endpoint in JSON format.

### Getting Data From UI

> Example of fetching inputs/data and sending them to the endpoint in `index-renderer.js`:

```javascript
document.addEventListener('DOMContentLoaded', () => {
    // Find the button element in the UI (HTML)
    const calculateButton = document.getElementById('calculateButton');
    // Get the user's enteries from the UI (HTML)
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultElement = document.getElementById('result');
```
* The elements in the HTML page are found by their associated ids

### Sending And Fetching Data

> Example of sending over parsed data to the endpoint:

```javascript
try {
    // Fetch processed data from the Flask API endpoint
    const response = await fetch('http://localhost:6002/calculate/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        // Send the retreived data to the API endpoint for processing by the python backend
        body: JSON.stringify({ num1, num2 })
    });

    if (!response.ok) {
        throw new Error('Failed to fetch data');
    }
```
* The user input is then sent to the desired endpoint.
* The response from the API is fetched.

### Displaying Fetched Data In UI

> Example of displaying fetched data in the UI:

```javascript
// Display the result in the HTML
resultElement.textContent = `Result: ${result}`;
```

* This will change the content of the `result` element in the HTML , which was fetched by its ID earlier.
