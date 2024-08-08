'use strict';

// Creación de la función:
const CalcularImpuesto = function (precio = null, impuesto = 21) {

}

// Generalmente se suele probar la función "a mano":

// No recibe argumento (no debería andar)
console.log(`1. CalcularImpuesto()`, CalcularImpuesto());

// Recebe un argumento para precio que no sirve (no debería andar)
console.log(`2. CalcularImpuesto(NaN)`, CalcularImpuesto(NaN));

// Recibe un argumento para precio que no sirve (no debería andar), no importa lo que reicba el parámetro impuesto
console.log(`3. CalcularImpuesto(NaN, NaN)`, CalcularImpuesto(NaN, NaN));

// Recibe un argumento para precio que no sirve (no debería andar), no importa lo que reicba el parámetro impuesto
console.log(`4. CalcularImpuesto(NaN, 30)`, CalcularImpuesto(NaN, 30));

// Recibe un argumento válido para precio (anda) y como el argumento para impuesto es inválido, debería quedar en 21 (valor por defecto)
console.log(`5. CalcularImpuesto(1000, NaN)`, CalcularImpuesto(1000, NaN));

// Recibe un argumento válido para precio (anda) y como el argumento para impuesto es inválido, debería quedar en 21 (valor por defecto)
console.log(`6. CalcularImpuesto(1000, 120)`, CalcularImpuesto(1000, 120));

// Recibe un argumento válido para precio (anda), impuesto queda con su valor por defecto (21)
console.log(`7. CalcularImpuesto(1000)`, CalcularImpuesto(1000));

// Recibe un argumento potencialmente válido para precio (para que ande nuestra función debería convertir a número el precio, ¿lo implementamos?), impuesto queda con su valor por defecto (21)
console.log(`8. CalcularImpuesto(' ')`, CalcularImpuesto(' '));

// Recibe un argumento potencialmente válido para precio (para que ande nuestra función debería convertir a número el precio, ¿lo implementamos?), impuesto queda con su valor por defecto (21)
console.log(`9. CalcularImpuesto('1000')`, CalcularImpuesto('1000'));

// Recibe dos argumentos válidos (anda)
console.log(`10. CalcularImpuesto(1000, 30)`, CalcularImpuesto(1000, 30));

