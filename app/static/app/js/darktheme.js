let switchToggle = JSON.parse(localStorage.getItem('switchToggle')) || 0;

function toggle() {
    if (switchToggle === 0) {
        switchToggle = 1;
        localStorage.setItem('switchToggle', JSON.stringify(switchToggle));
    }
    else {
        switchToggle = 0;
        localStorage.setItem('switchToggle', JSON.stringify(switchToggle));
    }
}

function changeTheme(switchToggle) {
    if (window.location.pathname === '/register/') {
        if (switchToggle === 1) {
            document.body.style.backgroundImage = 'none';
            document.body.style.backgroundColor = 'rgb(30,33,36)';
            document.body.style.color = 'rgb(212, 212, 212)';

            document.querySelectorAll('.title').forEach(element => {
                element.style.color = 'rgb(212, 212, 212)';
            });

            document.querySelectorAll('.registerContainer').forEach(element => {
                element.style.backgroundColor = 'rgb(13, 14, 15)';
            });

            document.querySelectorAll('input[type="text"]').forEach(element => {
                element.style.backgroundColor = 'transparent';
                element.style.color = 'white';
            });
    
            document.querySelectorAll('input[type="password"]').forEach(element => {
                element.style.backgroundColor = 'transparent'
                element.style.color = 'white';;
            });
        }
        else {
            document.body.style.backgroundImage = 'linear-gradient(to right, rgb(235, 235, 235), rgb(225, 233, 241))';
            document.body.style.backgroundColor = 'transparent';
            document.body.style.color = 'black';

            document.querySelectorAll('.title').forEach(element => {
                element.style.color = 'black';
            });
            
            document.querySelectorAll('.registerContainer').forEach(element => {
                element.style.backgroundColor = 'white';
            });

            document.querySelectorAll('input[type="text"]').forEach(element => {
                element.style.backgroundColor = 'rgb(243, 243, 243)';
                element.style.color = 'rgb(73, 73, 73)';
            });
    
            document.querySelectorAll('input[type="password"]').forEach(element => {
                element.style.backgroundColor = 'rgb(243, 243, 243)'
                element.style.color = 'rgb(73, 73, 73)';;
            });
        }
    }
    

    else if (window.location.pathname === '/') {
        if (switchToggle === 1) {
            document.body.style.color = 'white';
            document.body.style.backgroundImage = 'none';
            document.body.style.backgroundColor = 'rgb(30,33,36)';
        
            document.querySelectorAll('.titleRight').forEach(element => {
                element.style.color = 'rgb(212, 212, 212)';
            });
    
            document.querySelectorAll('.indexContainer').forEach(element => {
                
            });
    
            document.querySelectorAll('.subIndexContainer').forEach(element => {
                element.style.backgroundColor = 'rgb(13, 14, 15)';
            });
    
            document.querySelectorAll('.subIndexContainer2').forEach(element => {
                element.style.backgroundImage = 'none';
                element.style.backgroundColor = 'rgb(13, 14, 15)';
            });
    
            document.querySelectorAll('.subTitleRight').forEach(element => {
                element.style.color = 'rgb(212, 212, 212)';
            });
    
            document.querySelectorAll('.signinBtn').forEach(element => {
                element.style.color = 'white';
            });
    
            document.querySelectorAll('.signupBtn').forEach(element => {
                element.style.color = 'rgb(212, 212, 212)';
                element.style.border = '2px solid rgb(212, 212, 212)';
            });
    
            document.querySelectorAll('input[type="text"]').forEach(element => {
                element.style.backgroundColor = 'transparent';
                element.style.color = 'white';
            });
    
            document.querySelectorAll('input[type="password"]').forEach(element => {
                element.style.backgroundColor = 'transparent';
                element.style.color = 'white';
            });
    
        }
    
        else {
            document.body.style.backgroundColor = 'transparent';
            document.body.style.color = 'rgb(236, 43, 75)';
            document.body.style.backgroundImage = 'linear-gradient(to right, rgb(235, 235, 235), rgb(225, 233, 241))';
            
            document.querySelectorAll('.titleRight').forEach(element => {
                element.style.color = '';
            });
    
            document.querySelectorAll('.indexContainer').forEach(element => {
                element.style.backgroundColor = 'transparent';
            });
    
            document.querySelectorAll('.subIndexContainer').forEach(element => {
                element.style.backgroundColor = 'white';
            });
    
            document.querySelectorAll('.subIndexContainer2').forEach(element => {
                element.style.backgroundColor = 'transparent';
                element.style.backgroundImage = 'linear-gradient(to top, rgb(182, 37, 37), rgb(236, 43, 75))';
            });
    
            document.querySelectorAll('.subTitleRight').forEach(element => {
                element.style.color = 'white';
            });
    
            document.querySelectorAll('.signinBtn').forEach(element => {
                element.style.color = 'white';
            });
            
            document.querySelectorAll('.signupBtn').forEach(element => {
                element.style.color = 'white';
                element.style.border = '2px solid white';
            });
    
            document.querySelectorAll('input[type="text"]').forEach(element => {
                element.style.backgroundColor = 'white';
                element.style.color = 'rgb(73, 73, 73)';
            });
    
            document.querySelectorAll('input[type="password"]').forEach(element => {
                element.style.backgroundColor = 'white';
                element.style.color = 'rgb(73, 73, 73)';
            });
        }
    }
}

const switchButton = document.querySelector('.darkthemeButton');
switchButton.addEventListener('click', () => {
    toggle(switchToggle);
    changeTheme(switchToggle);
});

console.log(window.location.pathname);

changeTheme(switchToggle);