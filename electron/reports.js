document.addEventListener('DOMContentLoaded', () => {

    const generatePatientButton = document.getElementById('patient_report');
    const generateAverageButton = document.getElementById('average_report');

    const IDInput = document.getElementById('patient_id');
    const exportPatient = document.getElementById('export_patient');
    const exportAverage = document.getElementById('export_average');

    generatePatientButton.addEventListener('click', async () => {

        const patient_id = parseInt(IDInput.value);
        const export_name = exportPatient.value;

        try {
            const response = await fetch('http://localhost:6002/patient-report', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ patient_id, export_name })
            });

            if (!response.ok) {
                throw new Error('Failed to generate report');
            }

        } catch (error) {
            console.error('Error generating report:', error);
        }
    });

    generateAverageButton.addEventListener('click', async () => {

        const export_name = exportAverage.value;

        try {
            const response = await fetch('http://localhost:6002/average-report', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ export_name })
            });

            if (!response.ok) {
                throw new Error('Failed to generate report');
            }

        } catch (error) {
            console.error('Error generating report:', error);
        }
    });
});

