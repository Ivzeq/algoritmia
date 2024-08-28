'use strict';

// Comencemos


//Declaro las variables
let nombre, edad, resultado = '';

//El algoritmo que resuelve mi problema
do {
	nombre = prompt('Ingrese el nombre.');
	edad   = prompt('Ingrese la edad.');
	
	resultado += `Nombre: ${nombre} y Edad: ${edad} <br>`;
		
} while(confirm('¿Desea seguir cargando personas?'))

//Muestra de datos
document.write(`<p>${ resultado }</p>`);