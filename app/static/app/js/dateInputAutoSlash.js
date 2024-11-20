document.getElementById('id_data_nascimento').addEventListener('input', function (e) {
    let input = e.target.value;
    // Remove qualquer caractere não numérico
    input = input.replace(/\D/g, '');

    // Adiciona as barras automaticamente
    if (input.length > 2 && input.length <= 4) {
        input = input.slice(0, 2) + '/' + input.slice(2);
    } else if (input.length > 4) {
        input = input.slice(0, 2) + '/' + input.slice(2, 4) + '/' + input.slice(4, 8);
    }

    e.target.value = input;
});