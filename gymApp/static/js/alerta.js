const alerta = document.querySelector('.message-success');
const botonCerrar = document.getElementById('botonCerrar');

const tiempoAlerta = 2500;
const duracionAnimacion = 750;

function cerrarAlerta() {
    alerta.style.animation = `fadeOut ${duracionAnimacion}ms forwards`

    alerta.addEventListener('animationend', () => {
        alerta.remove();
    });
}

setTimeout(cerrarAlerta, tiempoAlerta);

botonCerrar.addEventListener('click', () => {
    cerrarAlerta()
});