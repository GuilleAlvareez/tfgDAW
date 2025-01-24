const subMenu = document.querySelector('.submenu');
const botonAbrir = document.querySelector('.open_submenu')

botonAbrir.addEventListener('click', (e) => {
    subMenu.classList.toggle('show')
})

document.addEventListener('click', (e) => {
    if (subMenu.classList.contains('show')
    && !subMenu.contains(e.target)
    && !botonAbrir.contains(e.target)) {

        subMenu.classList.remove('show')
    }
})