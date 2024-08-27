function redirectWithDelay(url) {
    // Pré-carrega a página para cachear alguns recursos
    const preloader = document.createElement('link');
    preloader.rel = 'prefetch';
    preloader.href = url;
    document.head.appendChild(preloader);
    
    // Aplica o delay antes de redirecionar visualmente
    setTimeout(() => {
        window.location.href = url;
    }, 250);
}