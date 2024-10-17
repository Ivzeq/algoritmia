'use strict';

// Declaración de variables globales:
let num;

// Creación de funciones:
const IngresarNumero = function() {
    num = ''
    while (!parseInt(num)){
        num = prompt('Ingrese un numero valido')
    }
}

const MostrarParidad = function() {
    if (num % 2 == 0){
        console.info('El numero es par')
    } else{
        console.info('El numero es impar')
    }
}