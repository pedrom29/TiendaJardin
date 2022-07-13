const btnSwitch = document.querySelector('#modo');

btnSwitch.addEventListener('click', () => {
	document.body.classList.toggle('dark');
	btnSwitch.classList.toggle('active');


    if(document.body.classList.contains('dark')){
        localStorage.setItem('dark-mode', 'true');
    }else {
        localStorage.setItem('dark-mode', 'false');
    }
});


if(localStorage.getItem('dark-mode') === 'true' ) {
    document.body.classList.add('dark');
    btnSwitch.classList.add('active');
}else {
    document.body.classList.remove('dark');
    btnSwitch.classList.remove('active');
}  
  function checkInputs() {
    
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();
    
    if(usernameValue === '') {
      setErrorFor(username, 'El usuario no puede quedar en blanco');
    } else {
      setSuccessFor(username);
    }
    
    if(emailValue === '') {
      setErrorFor(email, ' El Email no puede quedar en blanco');
    } else if (!isEmail(emailValue)) {
      setErrorFor(email, 'Correo no valido');
    } else {
      setSuccessFor(email);
    }
    
    if(passwordValue === '') {
      setErrorFor(password, 'La contraseña no puede quedar en blanco');
    } else {
      setSuccessFor(password);
    }
    
    if(password2Value === '') {
      setErrorFor(password2, 'La contraseña no puede quedar en blanco');
    } else if(passwordValue !== password2Value) {
      setErrorFor(password2, 'Las contraseñas no coinciden');
    } else{
      setSuccessFor(password2);
    }
  }
  
  function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'form-control error';
    small.innerText = message;
  }
  
  function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control success';
  }
    
  function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
  }



function login() {
  var user, pass
}  


  
  
  
  
  
  
  
  
  
  
  