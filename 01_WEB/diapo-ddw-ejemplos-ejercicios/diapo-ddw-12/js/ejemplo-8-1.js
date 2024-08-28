'use strict';


//Ejemplo:  Ingrese un valor numérico e informe si es cero, par o impar. 
let num 		= parseInt(prompt('Ingrese un valor numerico'))
let respuesta 	= ''; 
if (num == 0) 
{ 
	respuesta = 'El número es cero'; 
} 
else 
{ 
	if (num % 2 == 0) 
	{ 
		respuesta = 'El número es par'; 
	} 
	else 
	{ 
		respuesta = 'El número es impar'; 
	} 
} 
document.write(`<p><strong>${respuesta}</strong></p>`);


/*
// Realicemos la codificación a partir de aquí:
let resultado;

resultado	= ' Nombre: ' + prompt('Ingrese su nombre');
resultado   += ' Edad: ' + prompt('Ingrese su edad');
resultado  	+= ' Email: ' + prompt('Ingrese su email');
resultado 	+= ' Telefono: ' + prompt('Ingrese su telefono'); 
resultado	+= ' Estudiante: ' + confirm('¿Es estudiante?');

alert(resultado);
document.write(`<p><strong>${resultado}</strong></p>`);
console.log(resultado);*/

/*alert(`Nombre: ${nombre}
	   Edad: ${edad}
	   Email: ${email}
	   Telefono: ${telefono}
	   Estudiante: ${estudiante}`);

console.info(`Nombre: ${nombre}
	   Edad: ${edad}
	   Email: ${email}
	   Telefono: ${telefono}
	   Estudiante: ${estudiante}`);

document.write(`<ul><li>Nombre: ${nombre}</li>
	   <li>Edad: ${edad}</li>
	   <li>Email: ${email}</li>
	   <li>Telefono: ${telefono}</li>
	   <li>Estudiante: ${estudiante}</li></ul>`);*/



