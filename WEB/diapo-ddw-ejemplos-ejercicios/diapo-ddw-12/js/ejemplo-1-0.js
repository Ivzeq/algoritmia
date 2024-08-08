'use strict';

//Declaracion de Variables
let nombre, edad, email, telefono, esEstudiante;
let resultado;

//Pedir datos al usuario
nombre       = prompt('Ingrese su nombre');
edad   		 = parseInt(prompt('Ingrese su edad'));
email  		 = prompt('Ingrese su email');
telefono 	 = prompt('Ingrese su teléfono');
esEstudiante = confirm('Si es estudiante presiones Aceptar, sino Cancelar');

//Para mostrar con document.write
resultado = `<p>Nombre : <strong>${nombre}</strong></p>`;
resultado += `<p>Edad : <strong>${edad}</strong></p>`;
resultado += "<p>Email : <strong>"+email+"</strong></p>";
resultado += '<p>Teléfono : <strong>'+telefono+'</strong></p>';
resultado += `<p>Estudiante : <strong>${esEstudiante}</strong></p>`;

alert(resultado);

//Mostramos en consola
console.log(nombre, edad, email, telefono, esEstudiante);
