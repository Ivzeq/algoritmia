'use strict';

//19. Se le solicita al usuario que ingrese dos números y un operador (+, -, *, /). 
//Realice el algoritmo
//para calcular e informar la operación solicitada entre ambos números.
/*
let numero1    = parseInt(prompt('Ingrese un numero'));
let numero2    = parseInt(prompt('Ingrese otro numero'));
let operador   = prompt("Ingrese un operador (+,-,*,/)");
let respuesta  = "";

switch(operador) {
    case "+":
    	respuesta = numero1 + numero2;
    break;
    case "-":
    	respuesta = numero1 - numero2;
    break;
    case "*":
    	respuesta = numero1 * numero2;
    break;
    case "/":
    	respuesta = numero1 / numero2;
    break;
    default:
    	respuesta = 'El operador ingresado no es válido.';
}
document.write("<p><strong>El resultado es:"+ respuesta+ " La operacion realizada fue una:"+ operador +" entre los valores: "+ numero1 +" y "+ numero2 +"</strong></p>");
*/
/*
let letra     = prompt('Ingrese una letra').toLowerCase();
let respuesta = "";

switch(letra) {
    case "a":
            respuesta = 'Es la primera Vocal';
    break;
    case "e":
            respuesta = 'Es la segunda Vocal';
    break;
    case "i":
            respuesta = 'Es la tercer Vocal';
    break;
    case "o":
            respuesta = 'Es la cuarta Vocal';
    break;
    case "u":
            respuesta = 'Es la quinta y última Vocal';
    break;
    default:
            respuesta = 'La letra ingresada no es una vocal';
}

document.write(`<p><strong>${respuesta}</strong></p>`)*/

/*20 - Se le solicita al usuario que ingrese los tres lados 
de un triángulo. Realice el algoritmo para
informar si el triángulo es equilátero, isósceles o escaleno.*/
/*
let lado1     = parseInt(prompt("ingrese el primer lado del triangulo"));
let lado2     = parseInt(prompt("ingrese el segundo lado del triangulo"));
let lado3     = parseInt(prompt("ingrese el tercer lado del triangulo"));

if(!isNaN(lado1) && !isNaN(lado2) && !isNaN(lado3)){
    if(lado1 == lado2 && lado1 == lado3){
        document.write("el triangulo es Equilatero");
    }else if(lado1 == lado2 || lado1 == lado3 || lado2 == lado3){
        document.write("El triangulo es Isosceles");
    }else{
        document.write("El triangulo es Escaleno");
    }
}else{
    document.write("Vuelva a intentarlo ingresando un numero");
}
*/
//isNaN is not a number