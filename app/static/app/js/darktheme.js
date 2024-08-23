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
        document.body.style.color = 'white';
        document.body.style.backgroundImage = 'none';
        document.body.style.backgroundColor = 'rgb(30,33,36)';
    
        document.querySelectorAll('.titleRight').forEach(element => {
            element.style.color = 'rgb(236, 43, 75)';
        });

        document.querySelectorAll('.indexContainer').forEach(element => {
            element.style.border = '2px solid rgb(236, 43, 75)';
        });

        document.querySelectorAll('.subIndexContainer').forEach(element => {
            element.style.backgroundColor = 'transparent';
        });

        document.querySelectorAll('.subIndexContainer2').forEach(element => {
            element.style.backgroundImage = 'none';
            element.style.borderLeft = '2px solid rgb(236, 43, 75)';
        });

        document.querySelectorAll('.subTitleRight').forEach(element => {
            element.style.color = 'rgb(236, 43, 75)';
        });

        document.querySelectorAll('.signinBtn').forEach(element => {
            element.style.color = 'white';
        });

        document.querySelectorAll('.signupBtn').forEach(element => {
            element.style.color = 'rgb(236, 43, 75)';
            element.style.border = '2px solid rgb(236, 43, 75)';
        });
    }

    else {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'rgb(236, 43, 75)';
        document.body.style.backgroundImage = 'linear-gradient(to right, rgb(235, 235, 235), rgb(225, 233, 241))';
        
        document.querySelectorAll('.titleRight').forEach(element => {
            element.style.color = '';
        });

        document.querySelectorAll('.indexContainer').forEach(element => {
            element.style.border = 'none';
        });

        document.querySelectorAll('.subIndexContainer').forEach(element => {
            element.style.backgroundColor = 'white';
        });

        document.querySelectorAll('.subIndexContainer2').forEach(element => {
            element.style.backgroundColor = 'transparent';
            element.style.backgroundImage = 'linear-gradient(to top, rgb(182, 37, 37), rgb(236, 43, 75))';
            element.style.border = 'none';
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