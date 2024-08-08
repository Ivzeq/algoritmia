'use strict';

let num 		= parseInt(prompt('Ingrese un valor numerico'))
let respuesta 	= 'El número '; 

//Resuelto con if [else]
if (num == 0) { 
	respuesta += 'es cero'; 
} 
else { 
	if (num % 2 ===0) {
		respuesta += 'es par'
	} 
	else {
		respuesta += 'es impar'; 
	} 
}


document.write(`<p><strong>${respuesta}</strong></p>`); 


// Comencemos