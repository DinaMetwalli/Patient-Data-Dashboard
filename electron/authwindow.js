const authButton = document.querySelector('.auth-button');
const exportAuthButton = document.querySelector('.exp-auth-button');

// Add a click event listener to the button
authButton.addEventListener('click', () => {
    // Open the authentication page in a new window
    const authWindow = window.open('authentication.html', '_blank', 'width=400,height=300');
    // Pass the loading modal reference to the authentication window
    authWindow.loadingModal = window.loadingModal;
});

exportAuthButton.addEventListener('click', () => {
    // Open the authentication page in a new window
    const authWindow = window.open('export-auth.html', '_blank', 'width=400,height=300');
});