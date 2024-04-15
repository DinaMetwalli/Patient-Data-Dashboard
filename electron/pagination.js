document.addEventListener("DOMContentLoaded", function () {
    const itemsPerPage = 1;
    const tableBody = document.getElementById("patient-list");
    const pagination = document.getElementById("pagination");
    const rows = Array.from(tableBody.getElementsByTagName("tr"));

    function displayPatients(pageNumber) {
        tableBody.innerHTML = "";
        const startIndex = (pageNumber - 1) * itemsPerPage;
        const endIndex = Math.min(startIndex + itemsPerPage, rows.length);

        for (let i = startIndex; i < endIndex; i++) {
            tableBody.appendChild(rows[i]);
        }

        // Generate pagination links
        pagination.innerHTML = "";
        const totalPages = Math.ceil(rows.length / itemsPerPage);
        for (let i = 1; i <= totalPages; i++) {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = i;
            link.onclick = function () {
                displayPatients(i);
            };
            pagination.appendChild(link);
        }
    }

    // Initial display of first page
    displayPatients(1);
});
