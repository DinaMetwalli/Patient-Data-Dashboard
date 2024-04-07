// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Find the button element in the UI (HTML)
    const calculateButton = document.getElementById('calculateButton');
    // Get the user's enteries from the UI (HTML)
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultElement = document.getElementById('result');

    /**
     * The following part is for communication between
     * the UI and the python backend through the API.
     * 
     * For every user input that needs processing, the user
     * would most likely press a button to trigger the
     * sending and processing of their request.
     * 
     * Another user request which belongs to the index page
     * could be processed as follows. Each HTML page will
     * have its own renderer.js file for clarity and less
     * clumpy code. Each renderer.js file will be for the
     * values in that specific HTML page.
     */

    // Add a click event listener to the button
    calculateButton.addEventListener('click', async () => {
        // Convert the user input values to integers
        const num1 = parseInt(num1Input.value);
        const num2 = parseInt(num2Input.value);

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

            // Parse the response JSON
            const data = await response.json();
            console.log('Response:', data);

            // Extract the result from the response data
            const { result } = data.data;

            // Display the result in the HTML
            resultElement.textContent = `Result: ${result}`;
        } catch (error) {
            // Handle any errors
            console.error('Error fetching data:', error);
        }
    });
});
