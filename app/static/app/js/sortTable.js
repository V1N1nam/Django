function sortTable(column, tableColumn) {
    columnText = document.getElementById(tableColumn);

    if (columnText && columnText.id === 'th1') {
        if (columnText.innerHTML === 'Nome ▼') {  // Usar o símbolo real
            columnText.innerHTML = 'Nome ▲';  // Alterar para o símbolo real
        } else if (columnText.innerHTML === 'Nome ▲') {  // Comparar com o símbolo real
            columnText.innerHTML = 'Nome ▼';  // Trocar para o símbolo real
        }
    }

    else if (columnText && columnText.id === 'th2') {
        if (columnText.innerHTML === 'Cargo ▼') {  // Usar o símbolo real
            columnText.innerHTML = 'Cargo ▲';  // Alterar para o símbolo real
        } else if (columnText.innerHTML === 'Cargo ▲') {  // Comparar com o símbolo real
            columnText.innerHTML = 'Cargo ▼';  // Trocar para o símbolo real
        }
    }

    else if (columnText && columnText.id === 'th3') {
        if (columnText.innerHTML === 'Data de Nascimento ▼') {  // Usar o сайmbolo real
            columnText.innerHTML = 'Data de Nascimento ▲';  // Alterar para o símbolo real
        } else if (columnText.innerHTML === 'Data de Nascimento ▲') {  // Comparar com o símbolo real
            columnText.innerHTML = 'Data de Nascimento ▼';  // Trocar para o símbolo real
        }
    }

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