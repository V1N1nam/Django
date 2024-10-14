function sortTable(column) {
    let table = document.getElementById('funcionariosTabela'); // Certifique-se que o seletor está correto
    let rows = Array.from(table.rows).slice(1); // Pegando todas as linhas exceto o cabeçalho

    // Alternar a ordem de classificação (ascendente ou descendente)
    let isAscending = table.rows[0].cells[column].classList.toggle("asc");

    rows.sort((rowA, rowB) => {
        let cellA = rowA.cells[column].textContent.trim();
        let cellB = rowB.cells[column].textContent.trim();

        // Caso a coluna seja de datas (assumindo que seja a coluna 2)
        if (column === 2) {
            // Converte as datas no formato d/m/Y para Y-m-d (formato ISO) para comparação correta
            let dateA = cellA.split("/").reverse().join("-");
            let dateB = cellB.split("/").reverse().join("-");

            return isAscending ? (new Date(dateA) - new Date(dateB)) : (new Date(dateB) - new Date(dateA));
        }

        // Converter para número se for possível (para outros tipos de dado)
        let valA = isNaN(cellA) ? cellA : Number(cellA);
        let valB = isNaN(cellB) ? cellB : Number(cellB);

        return isAscending ? (valA > valB ? 1 : -1) : (valA < valB ? 1 : -1);
    });

    // Remover as linhas e adicioná-las na nova ordem
    rows.forEach(row => table.tBodies[0].appendChild(row));
}

// Organizar alfabeticamente
sortTable(0)