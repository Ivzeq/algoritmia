'use strict';
//Ingresar 5 números. Informar si cada número par o impar.

//Hacerlo con while.

let resultado = '';
let numero    = 0;
let cont	  = 0;

while (cont<5) {
	numero = parseInt(prompt('Ingrese un valor numérico.'));
	resultado +=`<br> El numero ${cont}: ${numero} es `;
	if (numero%2==0) {
		resultado += `par`;
	} else {
		resultado += `impar`;
	}
	cont++;
}
document.write(`<p><strong>${resultado}</strong></p>`);