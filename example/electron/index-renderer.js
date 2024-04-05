// Wait for the DOM content to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Find the button element
    const calculateButton = document.getElementById('calculateButton');
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const resultElement = document.getElementById('result');

    // Add a click event listener to the button
    // for symbol in symbols:
    // generate password stuff.
    // and then like he had if conditions for everuthong
    // 
    calculateButton.addEventListener('click', async () => {
        const num1 = parseInt(num1Input.value);
        const num2 = parseInt(num2Input.value);

        try {
            // Fetch data from the Flask API endpoint
            const response = await fetch('http://localhost:6002/calculate/data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
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
