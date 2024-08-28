'use strict';

respuesta 	= 'El número '; 
//Resuelto con if [elseif]
if (num == 0) { 
	respuesta += 'es cero'; 
} 
else if  (num % 2 ===0) {
		respuesta += 'es par'
} 
else {
	respuesta += 'es impar'; 
} 


document.write(`<p><strong>${respuesta}</strong></p>`); 