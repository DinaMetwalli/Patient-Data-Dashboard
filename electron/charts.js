function calculateAverage(data) {
    const filteredData = data.filter(value => value !== null && !isNaN(value));
    const sum = filteredData.reduce((acc, curr) => acc + curr, 0);
    return sum / filteredData.length;
}

function calculateRespiratoryMeasurementsAverage(data) {
    console.log("Calculating Respiratory Measurements Average...");

    const averages = {
        "FiO2": calculateAverage(data.fio2),
        "FiO2 Ratio": calculateAverage(data.fio2_ratio),
        "Oxygen Flow Rate": calculateAverage(data.oxygen_flow_rate),
        "Respiratory Rate": calculateAverage(data.resp_rate),
        "SIP": calculateAverage(data.sip)
    };

    console.log('Respiratory Measurements Average:', averages);
    return averages;
}

function calculateMechanicalVentillationAverage(data) {
    console.log("Calculating Mechanical Ventillation Average...");

    const averages = {
        "ETCO2": calculateAverage(data.end_tidal_co2),
        "PEEP": calculateAverage(data.peep),
        "PIP": calculateAverage(data.pip),
        "Tidal Volume": calculateAverage(data.tidal_vol),
        "Actual Tidal Volume": calculateAverage(data.tidal_vol_actual),
        "Tidal Volume per kg": calculateAverage(data.tidal_vol_kg),
        "Spontaneous Tidal Volume": calculateAverage(data.tidal_vol_spon),
        "Inspiration Time": calculateAverage(data.insp_time)
    };

    console.log('Mechanical Ventillation Average:', averages);
    return averages;
}

function calculateDietaryRequirementsAverage(data) {
    console.log("Calculating Dietary Requirements Average...");

    const averages = {
        "FV": calculateAverage(data.feed_vol),
        "FV Administered": calculateAverage(data.feed_vol_adm),
        "BMI": calculateAverage(data.bmi)
    };

    console.log('Dietary Requirements Average:', averages);
    return averages;
}


function buildPieChart(referralData) {
    var referredCount = referralData.filter(value => value === 1 || isNaN(value)).length;
    var notReferredCount = referralData.filter(value => value === 0 || isNaN(value)).length;

    var pieChartData = {
        labels: ['Referred', 'Not Referred'],
        datasets: [{
            data: [referredCount, notReferredCount],
            backgroundColor: ['#1a2a6c', '#fdbb2d'], // Deep blues and golden yellow
            hoverBackgroundColor: ['#1a2a6c', '#fdbb2d']
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

function buildRespiratoryMeasurementsGraph(averages) {
    const labels = Object.keys(averages);
    const values = Object.values(averages);

    const ctx = document.getElementById('respiratoryMeasurementsChart').getContext('2d');
    const respiratoryMeasurementsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Respiratory Measurements Average',
                data: values,
                backgroundColor: [
                    '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d', '#1a2a6c' // Alternating deep blues and golden yellow
                ],
                borderColor: [
                    '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d', '#1a2a6c'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function buildMechanicalVentillationGraph(averages) {
    const labels = Object.keys(averages);
    const values = Object.values(averages);

    const ctx = document.getElementById('mechanicalVentillationChart').getContext('2d');
    const mechanicalVentillationChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Mechanical Ventillation Average',
                data: values,
                backgroundColor: [
                    '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d' // Alternating deep blues and golden yellow
                ],
                borderColor: [
                    '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d', '#1a2a6c', '#fdbb2d'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function buildDietaryRequirementsGraph(averages) {
    const labels = Object.keys(averages);
    const values = Object.values(averages);

    const ctx = document.getElementById('dietaryRequirementsChart').getContext('2d');
    const dietaryRequirementsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Dietary Requirements Average',
                data: values,
                backgroundColor: [
                    '#1a2a6c', '#fdbb2d', '#1a2a6c' // Deep blues and golden yellow
                ],
                borderColor: [
                    '#1a2a6c', '#fdbb2d', '#1a2a6c'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

async function importCSV() {
    try {
        const response = await fetch('http://localhost:6002/display_charts', {
            method: 'POST'
        });

        if (!response.ok) {
            throw new Error('Failed to fetch');
        }

        const data = await response.json();
        console.log("Data received:", data);

        if (data.success) {
            buildPieChart(data.data.referral);
            buildRespiratoryMeasurementsGraph(calculateRespiratoryMeasurementsAverage(data.data));
            buildMechanicalVentillationGraph(calculateMechanicalVentillationAverage(data.data));
            buildDietaryRequirementsGraph(calculateDietaryRequirementsAverage(data.data));
            showResult(`CSV Imported successfully.`);
        } else {
            console.error("Failed to import CSV:", data.message);
            showResult(`Failed to import CSV: ${data.message}`);
        }
    } catch (error) {
        console.error("An error occurred:", error);
        showResult(`An error occurred: ${error.message}`);
    }
}

function showResult(result) {
    const resultElement = document.getElementById("result");
    resultElement.textContent = `Result: ${result}`;
}

// Call the importCSV function when the page loads
document.addEventListener("DOMContentLoaded", function() {
    importCSV();
});