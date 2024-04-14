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
            backgroundColor: ['#6a0dad', '#d670f4'], // Unique shades
            hoverBackgroundColor: ['#520b85', '#be4fd6'] // Darker shades for hover effect
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

    const backgroundColors = ['#6a0dad', '#d670f4', '#7c12b5', '#ea8cf9', '#843cc3']; // Unique shades of purple
    const borderColors = ['#520b85', '#be4fd6', '#5e118b', '#c66efc', '#6e3baf']; // Darker shades for borders

    const ctx = document.getElementById('respiratoryMeasurementsChart').getContext('2d');
    const respiratoryMeasurementsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Respiratory Measurements Average',
                data: values,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
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

    const backgroundColors = ['#6a0dad', '#d670f4', '#7c12b5', '#ea8cf9', '#843cc3']; // Unique shades of purple
    const borderColors = ['#520b85', '#be4fd6', '#5e118b', '#c66efc', '#6e3baf']; // Darker shades for borders

    const ctx = document.getElementById('mechanicalVentillationChart').getContext('2d');
    const mechanicalVentillationChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Mechanical Ventillation Average',
                data: values,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
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

    const backgroundColors = ['#6a0dad', '#d670f4', '#7c12b5', '#ea8cf9', '#843cc3']; // Unique shades of purple
    const borderColors = ['#520b85', '#be4fd6', '#5e118b', '#c66efc', '#6e3baf']; // Darker shades for borders

    const ctx = document.getElementById('dietaryRequirementsChart').getContext('2d');
    const dietaryRequirementsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Dietary Requirements Average',
                data: values,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
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
    hideLoader('pieChart');
    hideLoader('respiratoryMeasurementsChart');
    hideLoader('mechanicalVentillationChart');
    hideLoader('dietaryRequirementsChart');

}


let referralDataFromImportCSV = null;
let referralDataFromGetReferralData = null;

async function buildCharts() {
    try {
        const response = await fetch('http://localhost:6002/display_charts', {});

        if (!response.ok) {
            throw new Error('Failed to fetch');
        }

        const data = await response.json();

        if (data.success) {
            referralDataFromImportCSV = data.data.referral;
            countReferrals(referralDataFromImportCSV);

            buildPieChart(data.data.referral);

            buildRespiratoryMeasurementsGraph(calculateRespiratoryMeasurementsAverage(data.data));

            buildMechanicalVentillationGraph(calculateMechanicalVentillationAverage(data.data));

            buildDietaryRequirementsGraph(calculateDietaryRequirementsAverage(data.data));
            updatePatientData();

        } else {
            console.error("Failed to import CSV:", data.message);
            showResult(`Failed to import CSV: ${data.message}`);
        }
    } catch (error) {
        console.error("An error occurred:", error);
        showResult(`An error occurred: ${error.message}`);
    }
}

async function getReferralData() {
    try {
        const response = await fetch('http://localhost:6002/referal');
        if (!response.ok) {
            throw new Error('Failed to fetch referral data');
        }
        const data = await response.json();
        if (data.success) {
            referralDataFromGetReferralData = data.data.referral;

            updatePatientData();
        } else {
            console.error('Failed to fetch referral data:', data.message);
        }
    } catch (error) {
        console.error('An error occurred while fetching data:', error);
    }
}

function countReferrals(referralData) {
    // Count referrals with value 1 and 0
    const referralsWithOne = referralData.filter(value => value === 1).length;
    const referralsWithZero = referralData.filter(value => value === 0).length;

    document.getElementById('patientsNeedingReferral').textContent = referralsWithOne.toString();
    document.getElementById('patientsNotNeedingReferral').textContent = referralsWithZero.toString();
}


function updatePatientData() {
    const totalPatients = referralDataFromImportCSV.length;
    const referralsDifference = referralDataFromGetReferralData.filter(value => value === 1).length -
        referralDataFromImportCSV.filter(value => value === 1).length;

    document.getElementById('totalPatients').textContent = totalPatients.toString();
    document.getElementById('patientsReferred').textContent = referralsDifference.toString();
}

function showResult(result) {
    const resultElement = document.getElementById("result");
    resultElement.textContent = `Result: ${result}`;
}

function showLoader(chartId) {
    const loaderElement = document.getElementById(chartId + 'Loading');
    if (loaderElement) {
        loaderElement.style.display = 'block';
    }
}

function hideLoader(chartId) {
    const loaderElement = document.getElementById(chartId + 'Loading');
    if (loaderElement) {
        loaderElement.style.display = 'none';
        console.log(`Loader hidden for ${chartId}`);
    } else {
        console.warn(`Loader element not found for ${chartId}`);
    }
}



document.addEventListener("DOMContentLoaded", function() {

    showLoader('pieChart');
    showLoader('respiratoryMeasurementsChart');
    showLoader('mechanicalVentillationChart');
    showLoader('dietaryRequirementsChart');
    buildCharts();
    getReferralData();

});