'''
Crea una matriz con un tamaño que el usuario le indique por teclado (puede ser 6x4, 7x2, etc.) 
pero como máximo podrá contener 10x10 valores y como mínimo 2x2. 
Crear una función para la cargar de los valores y, por último, otro procedimiento para visualizar los resultados. 
Los valores para cargar deberán ser número positivos entre 0 y 100, siendo éstos generados al azar.
'''
from random import randint


def crearMatriz (filas,columnas):
    matriz = []

    for i in range(filas):
        listaF = []
        for j in range(columnas):
            listaF.append(randint(0,100))
        matriz.append(listaF)

    return matriz

filasMatriz = int(input('Ingrese filas\n'))
columnasMatriz = int(input('Ingrese columnas\n'))

print(crearMatriz(filasMatriz, columnasMatriz))