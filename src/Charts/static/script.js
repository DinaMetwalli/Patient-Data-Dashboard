function importCSV() {
    fetch("/import-csv", {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {
        console.log("Data received:", data);
        if (data.success) {
            buildGraphs(data.data);
        } else {
            console.error("Failed to import CSV:", data.message);
        }
    })
    .catch(error => {
        console.error("An error occurred:", error);
    });
}

function buildGraphs(data) {
    console.log("Building graphs with data:", data);
    // Build the pie chart for referral statistics
    var referralData = data.referral;
    var referredCount = referralData.filter(value => value === 1 || isNaN(value)).length;
    var notReferredCount = referralData.filter(value => value === 0 || isNaN(value)).length;

    var pieChartData = {
        labels: ['Referred', 'Not Referred'],
        datasets: [{
            data: [referredCount, notReferredCount],
            backgroundColor: ['#36A2EB', '#FF6384'],
            hoverBackgroundColor: ['#36A2EB', '#FF6384']
        }]
    };

    var ctxPie = document.getElementById("pieChart").getContext('2d');
    var pieChart = new Chart(ctxPie, {
        type: 'pie',
        data: pieChartData,
        options: {
            title: {
                display: true,
                text: 'Percentage of People Referred or Not Referred',
                fontColor: '#333',
                fontSize: 18,
                padding: 20
            },
            legend: {
                display: true,
                position: 'bottom',
                labels: {
                    fontColor: '#333',
                    fontSize: 14
                }
            }
        }
    });
}

// Call the importCSV function when the page loads
document.addEventListener("DOMContentLoaded", function() {
    importCSV();
});
