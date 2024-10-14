console.log('importou certo o sortTable.js');

function sortTable(column) {
    let table = document.getElementById('funcionariosTabela'); // Corrigido o seletor para ID
    let rows = Array.from(table.rows).slice(1); // Pegando todas as linhas exceto o cabeçalho

    // Alternar a ordem de classificação (ascendente ou descendente)
    let isAscending = table.rows[0].cells[column].classList.toggle("asc");

    rows.sort((rowA, rowB) => {
        let cellA = rowA.cells[column].textContent.trim();
        let cellB = rowB.cells[column].textContent.trim();

        // Converter para número se for possível
        let valA = isNaN(cellA) ? cellA : Number(cellA);
        let valB = isNaN(cellB) ? cellB : Number(cellB);

        return isAscending ? (valA > valB ? 1 : -1) : (valA < valB ? 1 : -1);
    });

    // Remover as linhas e adicioná-las na nova ordem
    rows.forEach(row => table.tBodies[0].appendChild(row));
}