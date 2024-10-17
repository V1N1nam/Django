function sortTable(column) {
    let table = document.getElementById('funcionariosTabela');
    let rows = Array.from(table.rows).slice(1);

    let isAscending = table.rows[0].cells[column].classList.toggle("asc");

    // Reset the headers for all columns before sorting
    document.querySelectorAll('th').forEach((th) => {
        th.innerHTML = th.innerHTML.replace(' ▼', '').replace(' ▲', '');
    });

    rows.sort((rowA, rowB) => {
        let cellA = rowA.cells[column].textContent.trim();
        let cellB = rowB.cells[column].textContent.trim();

        if (column === 2) {
            let dateA = cellA.split("/").reverse().join("-");
            let dateB = cellB.split("/").reverse().join("-");

            let result = isAscending ? (new Date(dateA) - new Date(dateB)) : (new Date(dateB) - new Date(dateA));
            
            return result;
        }

        let valA = isNaN(cellA) ? cellA : Number(cellA);
        let valB = isNaN(cellB) ? cellB : Number(cellB);

        return isAscending ? (valA > valB ? 1 : -1) : (valA < valB ? 1 : -1);
    });

    // Update the header after sorting
    if (isAscending) {
        document.getElementById("th" + (column + 1)).innerHTML += " ▼";
    } else {
        document.getElementById("th" + (column + 1)).innerHTML += " ▲";
    }

    rows.forEach(row => table.tBodies[0].appendChild(row));
}

sortTable(0);
