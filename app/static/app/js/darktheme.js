let switchToggle = 0;

function toggle() {
    if (switchToggle === 0) {
        switchToggle = 1;
    }
    else {
        switchToggle = 0;
    }
    console.log(switchToggle);
}

function changeTheme(switchToggle) {
    if (switchToggle === 1) {
        document.body.style.backgroundColor = 'black';
        document.body.style.color = 'white';
        document.body.style.backgroundImage = 'linear-gradient(to left, rgba(49,0,8,1) 0%, rgba(14,14,14,1))';
    
        document.querySelectorAll('.titleRight').forEach(element => {
            element.style.color = 'black';
        });

        document.querySelectorAll('.subIndexContainer').forEach(element => {
            element.style.backgroundColor = 'black';
        });

        document.querySelectorAll('.subTitleRight').forEach(element => {
            element.style.color = 'black';
        });

        document.querySelectorAll('.signinBtn').forEach(element => {
            element.style.color = 'black';
        });

        document.querySelectorAll('.signupBtn').forEach(element => {
            element.style.color = 'black';
            element.style.border = '2px solid black';
        });
    }

    else {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'black';
        document.body.style.backgroundImage = 'linear-gradient(to right, rgb(235, 235, 235), rgb(225, 233, 241))';
        
        document.querySelectorAll('.titleRight').forEach(element => {
            element.style.color = '';
        });

        document.querySelectorAll('.subIndexContainer').forEach(element => {
            element.style.backgroundColor = 'white';
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
    }
}


const switchButton = document.querySelector('.darkthemeButton');
switchButton.addEventListener('click', () => {
    toggle(switchToggle);
    changeTheme(switchToggle);
});