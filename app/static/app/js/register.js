document.getElementById('abc').addEventListener('input', function() {
    let pin = this.value;
    let botao = document.querySelector('.signupBtn');
    
    if (pin === '12345') {
        botao.style.display = 'block';
    } else {
        botao.style.display = 'none';
    }
});