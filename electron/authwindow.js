// // Get a reference to the "auth-button"
// const AuthButton = document.getElementById('auth-button');

// // Add a click event listener to the button
// AuthButton.addEventListener('click', () => {
//     // Open the authentication page in a new window
//     const authWindow = window.open('authentication.html', '_blank', 'width=400,height=300');
// });
const authButton = document.querySelector('.auth-button');

// Add a click event listener to the button
authButton.addEventListener('click', () => {
    // Open the authentication page in a new window
    const authWindow = window.open('authentication.html', '_blank', 'width=400,height=300');
    // Pass the loading modal reference to the authentication window
    authWindow.loadingModal = window.loadingModal;
});

const exportBtn = document.getElementById('exportBtn')

exportBtn.addEventListener('click', () => {
    alert('CSV File Exported Successfully!');
});