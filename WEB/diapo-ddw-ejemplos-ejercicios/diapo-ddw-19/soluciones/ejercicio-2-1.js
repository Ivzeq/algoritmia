'use strict';

// Variables:
let alumnos = [];

// Funciones:
const CargarAlumno = () => {
    // Variables:
    let nombre, apellido;

    // Nombre (ingreso y validación):
    do {
        nombre = prompt('Ingrese nombre del alumno');
    } while (!isNaN(nombre));

    // Apellido (ingreso y validación):
    do {
        apellido =  prompt('Ingrese apellido del alumno');
    } while (!isNaN(apellido));

    /* Array que irá guardando las notas del alumno */
    let notas = [];

    // Notas:
    do {
        let nota;
        // Nota (ingreso y validación):
        do {
            nota = parseInt(prompt('Ingrese nota del alumno'));
        } while (!(nota >= 1 && nota <= 10));
        
        // Cargo la nota al array de notas del alumno:
        notas.push(nota);
    } while (confirm('¿Ingresar otra nota?'));

    /* Array que irá guardando los datos del alumno, incluídas sus notas */
    let alumno = [];

    // Creo la info del alumno:
    alumno['Nombre'] = nombre;
    alumno['Apellido'] = apellido;
    alumno['Notas'] = notas;

    // Cargo el nuevo alumno al array global:
    alumnos.push(alumno);
}

const MostrarDatos = () => {
    // Variable que guarda el html generado:
    let html = '';

    // Armado:
    for (let alumno of alumnos) {
        // Datos del alumno:
        html += `<p>${alumno['Nombre']} ${alumno['Apellido']}</p>`;

        // Inicializo las variables para el promedio para cada alumno:
        let acum = 0, cont = 0;

        // Notas: recorrida de cada nota para acumular, contar y armar el mensaje:
        html += '<ul>';
            for (let nota of alumno['Notas']) {
                // Variables de promedio:
                acum += nota;
                cont++;
                // Destaco el tipo de nota por color:
                html += `<li style="color: ${nota >= 4 ? 'green' : 'red'}">${nota}</li>`;
            }
            html += `<li><strong>Promedio:</strong> ${acum / cont}</li>`;
        html += '</ul>';
    }

    // Ejecuto la función 'MostrarInfo':
    MostrarInfo(html);
}