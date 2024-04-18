const exportAuthButton = document.querySelector('.exp-auth-button');

exportAuthButton.addEventListener('click', () => {
    const authWindow = window.open('export-auth.html', '_blank', 'width=400,height=300');
});