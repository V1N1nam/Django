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
    }
    else {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'black';
    }
}

const switchButton = document.querySelector('.darkthemeButton');
switchButton.addEventListener('click', () => {
    toggle(switchToggle);
    changeTheme(switchToggle);
});