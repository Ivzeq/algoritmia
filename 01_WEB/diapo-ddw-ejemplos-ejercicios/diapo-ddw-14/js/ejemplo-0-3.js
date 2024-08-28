'use strict';

let resultado = 'Los numeros ingresados son:';
let numero    = 0;

for (let i=0; i<5; i++) {
	numero = parseInt(prompt('Ingrese un valor numérico.'));
	resultado += numero+ ' ';
}


document.write(`<p><strong>${resultado}</strong></p>`);
