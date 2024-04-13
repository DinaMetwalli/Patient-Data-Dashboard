// Get a reference to the "Upload CSV" button
const authButton = document.querySelector('.auth-button');

// Add a click event listener to the button
authButton.addEventListener('click', () => {
    // Open the authentication page in a new window
    const authWindow = window.open('authentication.html', '_blank', 'width=400,height=300');
});

/* Charts */
document.addEventListener('DOMContentLoaded', function() {
    var data1 = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Chart 1',
            data: [120, 130, 125, 135, 130, 140, 138],
            borderColor: 'blue',
            borderWidth: 2,
            fill: false
        }]
    };

    var data2 = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Chart 2',
            data: [100, 110, 115, 120, 125, 130, 135],
            borderColor: 'red',
            borderWidth: 2,
            fill: false
        }]
    };

    var data3 = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Chart 3',
            data: [90, 95, 100, 105, 110, 115, 120],
            borderColor: 'green',
            borderWidth: 2,
            fill: false
        }]
    };

    var data4 = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Chart 4',
            data: [80, 85, 90, 95, 100, 105, 110],
            borderColor: 'orange',
            borderWidth: 2,
            fill: false
        }]
    };

    var config1 = {
        type: 'line',
        data: data1,
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Chart 1'
                }
            }
        }
    };

    var config2 = {
        type: 'line',
        data: data2,
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Chart 2'
                }
            }
        }
    };

    var config3 = {
        type: 'line',
        data: data3,
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Chart 3'
                }
            }
        }
    };

    var config4 = {
        type: 'line',
        data: data4,
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Chart 4'
                }
            }
        }
    };

    var ctx1 = document.getElementById('chart1').getContext('2d');
    var ctx2 = document.getElementById('chart2').getContext('2d');
    var ctx3 = document.getElementById('chart3').getContext('2d');
    var ctx4 = document.getElementById('chart4').getContext('2d');

    var myChart1 = new Chart(ctx1, config1);
    var myChart2 = new Chart(ctx2, config2);
    var myChart3 = new Chart(ctx3, config3);
    var myChart4 = new Chart(ctx4, config4);
});

/* inactive export button */
const uploadDataButton = document.getElementById('upload-data-button');
const exportDataButton = document.getElementById('export-data-button');

uploadDataButton.addEventListener('click', function() {
    // Simulate data upload process
    setTimeout(function() {
        // Enable export data button after upload
        exportDataButton.disabled = false;
    }, 2000); // Change to your actual upload process time
});

