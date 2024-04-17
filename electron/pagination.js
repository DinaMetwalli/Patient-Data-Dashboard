document.addEventListener("DOMContentLoaded", function () {
    const itemsPerPage = 50;
    const tableBody = document.getElementById("patient-list");
    const pagination = document.getElementById("pagination");
    const rows = Array.from(tableBody.getElementsByTagName("tr"));

    async function displayPatients(pageNumber) {
        let data;
        try {
            const response = await fetch('http://localhost:6002/patient-all', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }

            data = await response.json();
            console.log(data);

            if (!data || !data.result) {
                throw new Error('Response data does not contain the expected structure');
            }

            const patients = data.result;

            updateTable(patients, pageNumber); // Update table with patient data

        } catch (error) {
            console.error('Error:', error);
            alert('Error fetching patient data');
        }
    }

    async function filterByBMI(bmi) {
        try {
            const response = await fetch('http://localhost:6002/filter-by-bmi', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ bmi })
            });

            if (!response.ok) {
                throw new Error('Failed to fetch filtered data');
            }

            const data = await response.json();
            updateTable(data.data); // Update table with filtered data
        } catch (error) {
            console.error('Error:', error);
            alert('Error filtering patient data by BMI');
        }
    }

    async function filterByReferral(referral, pageNumber) {
        console.log("filter function referral stat:", referral)
        try {
            const response = await fetch('http://localhost:6002/filter-by-referral', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ referral })
            });

            if (!response.ok) {
                throw new Error('Failed to fetch filtered data');
            }

            const data = await response.json();
            updateTable(data.data, pageNumber, referral); // Update table with filtered data
        } catch (error) {
            console.error('Error:', error);
            alert('Error filtering patient data by referral status');
        }
    }

    function updateTable(data, pageNumber = 1, referral) {
        if (referral === undefined) {
            referral = null;
        }
        console.log("referall status:", referral);

        // Clear table body
        tableBody.innerHTML = "";

        // Calculate start and end index for pagination
        const startIndex = (pageNumber - 1) * itemsPerPage;
        const endIndex = Math.min(startIndex + itemsPerPage, data.length);

        // Populate table with patient data
        for (let i = startIndex; i < endIndex; i++) {
            const patient = data[i];
            console.log("Patient Data:", patient); // Log patient data
            const row = document.createElement("tr");
            const cells = [
                "encounterId", "end_tidal_co2", "feed_vol", "feed_vol_adm",
                "fio2", "fio2_ratio", "insp_time", "oxygen_flow_rate", "peep",
                "pip", "resp_rate", "sip", "tidal_vol", "tidal_vol_actual",
                "tidal_vol_kg", "tidal_vol_spon", "bmi", "referral"
            ];
            cells.forEach(cell => {
                const cellElement = document.createElement("td");
                cellElement.textContent = patient[cell] ?? "";
                console.log(`Cell (${cell}):`, patient[cell]); // Log cell value
                row.appendChild(cellElement);
            });

            tableBody.appendChild(row);
        }

        // Generate pagination links
        pagination.innerHTML = "";
        const totalPages = Math.ceil(data.length / itemsPerPage);
        const currentPage = pageNumber;
        const prevPage = currentPage > 1 ? currentPage - 1 : 1;
        const nextPage = currentPage < totalPages ? currentPage + 1 : totalPages;

        const prevLink = document.createElement("a");
        prevLink.href = "#";
        prevLink.textContent = "« Previous";
        prevLink.onclick = function () {
            if (referral == null) {
                displayPatients(prevPage);
            }
            else {
                filterByReferral(referral, prevPage);
            }
        };
        pagination.appendChild(prevLink);

        for (let i = Math.max(1, currentPage - 1); i <= Math.min(totalPages, currentPage + 1); i++) {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = i;
            link.onclick = function () {
                if (referral == null) {
                    displayPatients(i);
                }
                else {
                    filterByReferral(referral, i);
                }
            };
            pagination.appendChild(link);
        }

        const nextLink = document.createElement("a");
        nextLink.href = "#";
        nextLink.textContent = "Next »";
        nextLink.onclick = function () {
            if (referral == null) {
                displayPatients(nextPage);
            }
            else {
                filterByReferral(referral, nextPage);
            }
        };
        pagination.appendChild(nextLink);
    }

    // Event listeners for radio buttons
    document.querySelectorAll('input[name="filter"]').forEach(radio => {
        radio.addEventListener('change', function () {
            const filterValue = this.value;
            let referralValue;

            if (filterValue === 'all') {
                // Fetch all patient data
                displayPatients(1);
            } else if (filterValue === 'do-not-need-referral') {
                referralValue = false;
                console.log("update function referral stat:", referralValue)
            } else if (filterValue === 'need-referral') {
                referralValue = true;
            }

            // Filter patient data by referral status
            filterByReferral(referralValue, 1);
        });
    });


    // Event listener for the filter button
    document.getElementById('filter-button').addEventListener('click', function () {
        const bmiFilterValue = document.getElementById('bmi-filter').value;
        // Filter patient data by BMI
        filterByBMI(bmiFilterValue);
    });

    // Initial display of first page
    displayPatients(1);
});
