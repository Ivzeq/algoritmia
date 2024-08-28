'use strict';

// Creo el objeto PersonaA:
let PersonaA = {
    Nombre: 'Alejandro',
    Apellido: 'Potente',
    Presentarse: function () {
        console.log(`Mi nombres es ${this.Nombre} ${this.Apellido}`);
    }
}

// Creo el objeto PersonaB:
let PersonaB = {
    Nombre: 'Marta',
    Apellido: 'Saffirio',
    Presentarse: function () {
        console.log(`Mi nombres es ${this.Nombre} ${this.Apellido}`);
    }
}

// Ejecuto los métodos:
PersonaA.Presentarse();
PersonaB.Presentarse();