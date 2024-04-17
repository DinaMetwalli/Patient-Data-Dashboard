document.addEventListener("DOMContentLoaded", async function () {
    const patientId = document.getElementById("patientId");
    const table1Body = document.getElementById("table1Body");
    const table2Body = document.getElementById("table2Body");
    const table3Body = document.getElementById("table3Body");
    const loadingModal = document.getElementById('loadingModal');
    const fetchDataBtn = document.getElementById('fetchDataBtn');

    fetchDataBtn.addEventListener('click', async () => {
        const patient_id = parseInt(patientId.value);
        try {
            loadingModal.style.display = 'block';

            // Fetch data for table 1
            const response1 = await fetch('http://localhost:6002/patient-dietary', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ patient_id: patient_id })
            });

            if (!response1.ok) {
                throw new Error('Failed to fetch dietary data');
            }

            const data1 = await response1.json();
            console.log(data1);

            if (!data1 || !data1.data) {
                throw new Error('Response data does not contain the expected structure');
            }

            const dietaryData = data1.data;

            // Clear table 1 body
            table1Body.innerHTML = "";

            // Populate table 1 with dietary data
            const row1 = document.createElement("tr");
            const cell11 = document.createElement("td");
            const cell12 = document.createElement("td");
            const cell13 = document.createElement("td");
            const cell14 = document.createElement("td");

            cell11.textContent = dietaryData.patient_id;
            cell12.textContent = dietaryData.feed_vol;
            cell13.textContent = dietaryData.feed_vol_adm;
            cell14.textContent = dietaryData.bmi;

            row1.appendChild(cell11);
            row1.appendChild(cell12);
            row1.appendChild(cell13);
            row1.appendChild(cell14);

            table1Body.appendChild(row1);

            // Fetch data for table 2
            const response2 = await fetch('http://localhost:6002/patient-resp', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ patient_id: patient_id })
            });

            if (!response2.ok) {
                throw new Error('Failed to fetch respiratory data');
            }

            const data2 = await response2.json();
            console.log(data2);

            if (!data2 || !data2.data) {
                throw new Error('Response data does not contain the expected structure');
            }

            const respData = data2.data;

            // Clear table 2 body
            table2Body.innerHTML = "";

            // Populate table 2 with respiratory data
            const row2 = document.createElement("tr");
            const cell21 = document.createElement("td");
            const cell22 = document.createElement("td");
            const cell23 = document.createElement("td");
            const cell24 = document.createElement("td");
            const cell25 = document.createElement("td");
            const cell26 = document.createElement("td");

            cell21.textContent = respData.patient_id;
            cell22.textContent = respData.fio2;
            cell23.textContent = respData.fio2_ratio;
            cell24.textContent = respData.oxygen_flow_rate;
            cell25.textContent = respData.resp_rate;
            cell26.textContent = respData.sip;

            row2.appendChild(cell21);
            row2.appendChild(cell22);
            row2.appendChild(cell23);
            row2.appendChild(cell24);
            row2.appendChild(cell25);
            row2.appendChild(cell26);

            table2Body.appendChild(row2);

            // Fetch data for table 3
            const response3 = await fetch('http://localhost:6002/patient-mech', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ patient_id: patient_id })
            });

            if (!response3.ok) {
                throw new Error('Failed to fetch mechanical data');
            }

            const data3 = await response3.json();
            console.log(data3);

            if (!data3 || !data3.data) {
                throw new Error('Response data does not contain the expected structure');
            }

            const mechData = data3.data;

            // Clear table 3 body
            table3Body.innerHTML = "";

            // Populate table 3 with mechanical data
            const row3 = document.createElement("tr");
            const cell31 = document.createElement("td");
            const cell32 = document.createElement("td");
            const cell33 = document.createElement("td");
            const cell34 = document.createElement("td");
            const cell35 = document.createElement("td");
            const cell36 = document.createElement("td");
            const cell37 = document.createElement("td");
            const cell38 = document.createElement("td");
            const cell39 = document.createElement("td");

            cell31.textContent = mechData.patient_id;
            cell32.textContent = mechData.end_tidal_co2;
            cell33.textContent = mechData.peep;
            cell34.textContent = mechData.pip;
            cell35.textContent = mechData.tidal_vol;
            cell36.textContent = mechData.tidal_vol_actual;
            cell37.textContent = mechData.tidal_vol_kg;
            cell38.textContent = mechData.tidal_vol_spon;
            cell39.textContent = mechData.insp_time;

            row3.appendChild(cell31);
            row3.appendChild(cell32);
            row3.appendChild(cell33);
            row3.appendChild(cell34);
            row3.appendChild(cell35);
            row3.appendChild(cell36);
            row3.appendChild(cell37);
            row3.appendChild(cell38);
            row3.appendChild(cell39);

            table3Body.appendChild(row3);

        } catch (error) {
            console.error('Error:', error);
            alert('Patient ID does not exist!');
        } finally {
            loadingModal.style.display = 'none';
        }
    });
});
