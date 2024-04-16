// Get a reference to the "auth-button"
const AuthButton = document.getElementById('auth-button');

// Add a click event listener to the button
AuthButton.addEventListener('click', () => {
    // Open the authentication page in a new window
    const authWindow = window.open('authentication.html', '_blank', 'width=400,height=300');
});