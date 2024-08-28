'use strict';

// Escape de caracteres y plantilla:
console.info('Mensaje con comillas \'simples\' dentro de comillas simples con \\\'.');
console.info("Mensaje con comillas \"dobles\" dentro de comillas dobles con \\\".");
console.info('Salto\nde línea.\nNo se requiere un espacio luego del \\n');

let dato = 'un string';
let suma = 1 + 1 + 2 + 3 + 5 + 8;

console.info(`Esto es
	una cadena que muestra 
	el contenido de las 
	variables ${dato} y ${suma} sin necesidad de concatenar`);