'use strict';

class Alumno {
    // Estático:
    static cantidadAlumnos = 0;

    // Propiedades:
    nombre = 'Nombre alumno/a';
    materias = [];

    // Constructor:
    constructor() {
        console.log('Nuevo/a alumno/a creado');
        // Incremento por cada nuevo/a alumno:
    }

    // Métodos:
    ingresarNombre() {}

    guardarMateria(materia) {}

    calcularPromedio() {}

    armar() {
        // Armo la info de cada alumno:
        // Recorro cada una de las materias:
    }
}

class Materia {
    // Propiedades:
    nombre = 'Nombre materia';
    nota = 0;

    // Constructor:
    constructor() {
        console.log('Nueva materia creado');
    }

    // Métodos:
    ingresarNombre() {}

    ingresarNota() {}

    leerNota() {}

    armar() {}
}

// Todos los alumnos:
let alumnos = [];

// Funciones:
const Cargar = () => {
    // Variables:
    let alumno;

    // Creo el alumno:
    alumno = new Alumno();

    // Pido su nombre:

    // Materias:
    do {
        // Creo la materia:
        // Pido nombre y nota:
        // La guardo en el alumno:
    } while (confirm('Más materias?'));

    // Guardo al alumno en el array:
};

const Mostrar = () => {
    // Variable que guarda el html generado:
    let html = '';

    // Muestro el total de alumnos/as:

    // Recorro a los alumnos:
    for (let alumno of alumnos) {
        // Muestro cada alumno:
        html += alumno.armar();
        html += '<hr />';
    }

    // Llamo a la función 'Generar':
    document.getElementById('info').innerHTML = html;
};
