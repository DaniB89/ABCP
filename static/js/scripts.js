// static/js/scripts.js

function toggleForms() {
    var loginForm = document.getElementById('login-form');
    var registerForm = document.getElementById('register-form');
    var loginRadio = document.getElementById('login-radio');
    var registerRadio = document.getElementById('register-radio');

    if (loginRadio.checked) {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    } else if (registerRadio.checked) {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
    }
}
