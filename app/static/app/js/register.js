document.getElementById('abc').addEventListener('input', function() {
    let pin = this.value;
    let cadastroBtn = document.querySelector('.signupBtn');
    
    if (pin === '12345') {
        cadastroBtn.style.backgroundColor = 'rgb(236, 43, 75)';
    } else {
        cadastroBtn.style.backgroundColor = 'rgba(255, 255, 255, 0.164)';
    }
});