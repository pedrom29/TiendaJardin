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















if (valor=="true") {
    body.classList.add("dark")
} else {
    body.classList.remove("dark")
}