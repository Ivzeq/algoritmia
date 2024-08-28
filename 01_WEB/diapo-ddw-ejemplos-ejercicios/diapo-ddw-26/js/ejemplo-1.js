const objeto = {
    nombre: 'Juan',
    apellido: 'Perez',
    edad: 33,
    materias: [
        {
            nombre: 'Diseño y Desarrollo Web',
            nota: 6,
        },
        {
            nombre: 'Programación 2',
            nota: 8,
        },
    ],
};

objetoCadenificado = JSON.stringify(objeto);
console.log(objetoCadenificado);

cadenificacionParseada = JSON.parse(objetoCadenificado);
console.log(cadenificacionParseada);
