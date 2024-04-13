const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const resultElement = document.getElementById('result');

    try {
        const response = await fetch('http://localhost:5007/login', {
            method: 'POST',
            body: JSON.stringify({ username }),
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            // Handle successful login (e.g., redirect, update UI)
            const data = await response.json();
            console.log('Response:', data);

            // Extract the result from the response data
            const result = data.data.result;

            // Display the result in the HTML
            resultElement.textContent = `Result: ${result}`;
        } else {
            console.error('Login failed:', await response.text());
            // Handle login failure (e.g., display error message)
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
