
/* 
Ejercicio 1: Saludo personalizado
Escribe un programa que le pida al usuario ingresar su nombre y luego muestre un saludo personalizado en la consola. 
Utiliza una declaración if para verificar si se ingresó un nombre.
*/
const ejercicio1 = () => {
    const username = prompt('Ingrese su nombre')

    console.log('Hola ' + username +'!')
}
/* 
Ejercicio 2: Suma de números pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 50. 
Utiliza un bucle for para iterar a través de los números y una declaración if para verificar si un número es par.
*/

const ejercicio2 = () => {
    let sumaPar = 0
    let numerosPares = '2'

    for (let i = 1; i <= 50; i++) {
        if (i%2 === 0) {
            sumaPar += i
            if (i>2){
                numerosPares += ' + ' + i
            }
        }
    }

    console.log('La suma de todos los numeros pares del 1 al 50 es', sumaPar)
    console.log('Los numeros sumados son', numerosPares)
}

/* 
Ejercicio 3: Calculadora de promedio
Escribe un programa que le permita al usuario ingresar una serie de calificaciones. 
Luego, calcula y muestra el promedio de esas calificaciones. Utiliza un bucle for o while para permitir al usuario ingresar una cantidad variable de calificaciones.
*/

const ejercicio3 = () => {
    let notaInput = Number(prompt('Ingrese una nota. Para detener ingresar -1'))
    const notas = []
    let sumNotas = 0
    let promedio = 0

    while (notaInput != -1) {
        notas.push(notaInput)
        notaInput = Number(prompt('Ingrese una nota. Para detener ingresar -1'))
    }

    sumNotas = notas.reduce((suma, nota) => suma + nota)

    promedio = sumNotas/notas.length

    console.log('La cantidad de notas es', notas.length ,'y el promedio de las notas es', promedio)
} 

/* 
Ejercicio 4: Tabla de multiplicar

Escribe un programa que permita al usuario ingresar un número y luego muestre la tabla de multiplicar de ese número del 1 al 10. 
Utiliza un bucle for para generar la tabla.
*/

const ejercicio4 = () => {
    factor = Number(prompt('Ingrese un numero para ver su tabla del 1 al 10'))

    for (let i = 1; i <= 10; i++) {
        console.log(factor,'x',i,'=', factor*i)
    }
} 

/*
Ejercicio 5: Contador regresivo

Escribe un programa que cuente desde un número ingresado por el usuario hasta 1, mostrando cada número en la consola. 
Utiliza un bucle while para realizar el conteo regresivo.
*/

const ejercicio5 = () => {
    let numeroInicial = Number(prompt('Ingrese un numero para ver su cuenta regresiva hasta 1'))

    while (numeroInicial < 1 || !(Number.isInteger(numeroInicial))){
        numeroInicial = Number(prompt('Dato incorrecto. Ingrese un numero para ver su cuenta regresiva hasta 1'))
    }

    for (let i = numeroInicial; i >= 1; i--) {
        console.log(i)
    }
} 

/*
Ejercicio 6: Validación de contraseña

Escribe un programa que le pida al usuario que ingrese una contraseña. 
La contraseña debe tener al menos 8 caracteres, al menos una letra mayúscula, una letra minúscula y un número.
Utiliza un bucle while para asegurarte de que el usuario ingrese una contraseña válida. 
Si la contraseña es válida, muestra un mensaje de éxito; de lo contrario, pide al usuario que ingrese una contraseña nuevamente.
*/

const ejercicio6 = () => {
    let password = prompt('Ingrese una contraseña con al menos 8 caracteres, al menos una letra mayúscula, una letra minúscula y un número')
    let isCorrecta = false

    while(!isCorrecta){
        let is8Caracteres = password.length >= 8
        let hasUppercase = password !== password.toLowerCase
        let hasLowercase = password !== password.toUpperCase
        let hasNumber =  password.match(/\d+/) != null
        let hasLetter = password.match(/[a-zA-Z]/) != null

        if (is8Caracteres && hasUppercase && hasLowercase && hasNumber && hasLetter) {
            isCorrecta = true
        } else {
            password = prompt('Contraseña invalida. Ingrese una contraseña con al menos 8 caracteres, al menos una letra mayúscula, una letra minúscula y un número')
        }
    }

    console.log('Contraseña correcta')
} 

/*
Ejercicio 7: Adivinanza con do-while

Escribe un juego en el que el programa elija un número aleatorio entre 1 y 10, y el usuario tenga que adivinarlo. 
El programa debe proporcionar pistas (mayor/menor) hasta que el usuario adivine correctamente el número. 
Utiliza un bucle do-while para repetir la solicitud de adivinanza hasta que se adivine el número.

Como genero un número aleatorio:

const numeroAleatorio = Math.floor(Math.random() * 10) + 1;
*/

const ejercicio7 = () => {
    const numeroAleatorio = Math.floor(Math.random() * 10) + 1;
    console.log(numeroAleatorio)
    do {
        numeroInput = prompt('Ingrese un numero')
        if (numeroInput > numeroAleatorio) {
            console.log('El numero a adivinar es menor al ingresado')
        } else if (numeroInput < numeroAleatorio) {
            console.log('El numero a adivinar es mayor al ingresado')
        } else {
            console.log('Adivinaste correctamente el numero')
        }
    }
    while (numeroInput != numeroAleatorio) 
} 