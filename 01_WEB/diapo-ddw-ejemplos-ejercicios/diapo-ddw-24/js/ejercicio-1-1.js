'use strict';

// Array de colores:
let colores = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta'];

// Obtengo el ul #elementos
let elementos = document.getElementById('elementos');

for (let hijo of elementos.children) {
    hijo.remove();
}

// Obtengo el div #colores
let divColores = document.getElementById('colores');

// Recorremos el array de colores
for (let color of colores) {
    let li = document.createElement('li');
    li.innerText = color;
    elementos.append(li);

    let div = document.createElement('div');
    div.style.width  = '60px';
    div.style.height = '60px';
    div.style.backgroundColor = color;
    div.style.display = 'inline-block';
    div.style.marginLeft = '10px';
    divColores.append(div);   
   
}

for (let div of divColores.children) {
    div.addEventListener('click', function () {
        for (let liItem of elementos.children) {
            liItem.style.color = div.style.backgroundColor;
        }
    });
} 