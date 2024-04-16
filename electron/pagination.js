document.addEventListener("DOMContentLoaded", function() {
    const itemsPerPage = 50;
    const tableBody = document.getElementById("patient-list");
    const pagination = document.getElementById("pagination");
    const rows = Array.from(tableBody.getElementsByTagName("tr"));

    async function displayPatients(pageNumber) {
        let data;
        try {
            const response = await fetch('http://127.0.0.1:6002/patient-all', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }

            data = await response.json();
            console.log(data); // Log response from the server

            if (!data || !data.result) {
                throw new Error('Response data does not contain the expected structure');
            }

            const patients = data.result; // Assuming data is an array of patient objects


            // Clear table body
            tableBody.innerHTML = "";

            // Calculate start and end index for pagination
            const startIndex = (pageNumber - 1) * itemsPerPage;
            const endIndex = Math.min(startIndex + itemsPerPage, patients.length);

            // Populate table with patient data
            for (let i = startIndex; i < endIndex; i++) {
                const patient = patients[i];
                const row = document.createElement("tr");
                const cell1 = document.createElement("td");
                const cell2 = document.createElement("td");
                const cell3 = document.createElement("td");
                const cell4 = document.createElement("td");
                const cell5 = document.createElement("td");
                const cell6 = document.createElement("td");
                const cell7 = document.createElement("td");
                const cell8 = document.createElement("td");
                const cell9 = document.createElement("td");
                const cell10 = document.createElement("td");
                const cell11 = document.createElement("td");
                const cell12 = document.createElement("td");
                const cell13 = document.createElement("td");
                const cell14 = document.createElement("td");
                const cell15 = document.createElement("td");
                const cell16 = document.createElement("td");
                // Add more cells as needed for additional patient properties

                cell1.textContent = patient.encounterId; // Assuming 'name' is a property of the patient object
                cell2.textContent = patient.end_tidal_co2;
                cell3.textContent = patient.feed_vol;
                cell4.textContent = patient.feed_vol_adm;
                cell5.textContent = patient.fio2;
                cell6.textContent = patient.fio2_ratio;
                cell7.textContent = patient.insp_time;
                cell8.textContent = patient.oxygen_flow_rate;
                cell9.textContent = patient.peep;
                cell10.textContent = patient.resp_rate;
                cell11.textContent = patient.tidal_vol;
                cell12.textContent = patient.tidal_vol_actual;
                cell13.textContent = patient.tidal_vol_kg;
                cell14.textContent = patient.tidal_vol_spon;
                cell15.textContent = patient.bmi;
                cell16.textContent = patient.referral;


                // Set additional cell content as needed

                row.appendChild(cell1);
                row.appendChild(cell2);
                row.appendChild(cell3);
                row.appendChild(cell4);
                row.appendChild(cell5);
                row.appendChild(cell6);
                row.appendChild(cell7);
                row.appendChild(cell8);
                row.appendChild(cell9);
                row.appendChild(cell10);
                row.appendChild(cell11);
                row.appendChild(cell12);
                row.appendChild(cell13);
                row.appendChild(cell14);
                row.appendChild(cell15);
                row.appendChild(cell16);

                // Append additional cells to the row

                tableBody.appendChild(row);
            }

            // Generate pagination links
            pagination.innerHTML = "";
            const totalPages = Math.ceil(patients.length / itemsPerPage);
            for (let i = 1; i <= totalPages; i++) {
                const link = document.createElement("a");
                link.href = "#";
                link.textContent = i;
                link.onclick = function() {
                    displayPatients(i);
                };
                pagination.appendChild(link);
            }
        } catch (error) {
            console.error('Error:', error);
            console.log('Response data:', data); // Log response data for further inspection
            alert('Please Upload a CSV file first');
        }

    }

    // Initial display of first page
    displayPatients(1);
});