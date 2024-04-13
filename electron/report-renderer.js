document.addEventListener('DOMContentLoaded', () => {

    const generateButton = document.getElementById('patient_report');

    const IDInput = document.getElementById('patient_id');
    const pathInput = document.getElementById('file_path');
    const exportInput = document.getElementById('export_name');

    generateButton.addEventListener('click', async () => {

        const patient_id = parseInt(IDInput.value);
        const export_name = exportInput.value;
        const csv_path = pathInput.value;

        try {
            const response = await fetch('http://localhost:6002/patient-report', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ patient_id, export_name, csv_path })
            });

            if (!response.ok) {
                throw new Error('Failed to generate report');
            }

        } catch (error) {
            console.error('Error generating report:', error);
        }
    });
});
