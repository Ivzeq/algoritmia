'use strict';

// Declaración de variables globales:
let siglas;

// Creación de funciones:
const IngresarSigla = function() {
    siglas = ''
    while (siglas != 'dw' && siglas != 'dm' && siglas != 'dg'){
        siglas = prompt('Ingrese una de las siguientes siglas: dw, dm, dg')
        siglas = siglas.toLowerCase()
    }
}

const MostrarCarrera = function() {
    if (siglas == 'dw'){
        console.info('Diseño web')
    } else if (siglas == 'dm') {
        console.info('Diseño multimedial')
    } else if (siglas == 'dg') {
        console.info('Diseño gráfico')
    }
}