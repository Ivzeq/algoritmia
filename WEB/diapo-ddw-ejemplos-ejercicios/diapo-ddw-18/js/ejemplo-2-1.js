'use strict';

let materias = [
    'Análisis de Datos',
    'Diseño Gráfico para Web',
    'Diseño Vectorial',
    'Experiencia del Usuario',
    'Interacción con Dispositivos Móviles',
    'Programación I',
];

for (let i = 0; i < materias.length; i++) {
    console.log(i, materias[i]);
}

for (let indice in materias) {
    console.log(indice, materias[indice]);
}

for (let valor of materias) {
    console.log(valor);
}