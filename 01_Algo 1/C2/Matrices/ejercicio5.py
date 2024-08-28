'''
Suma de Filas y Columnas: crear una función que tome una matriz como entrada 
y devuelva una lista con la suma de cada fila y otra lista con la suma de cada columna.
'''

def sumaColumna (matriz1):
    listaF = []
    suma = 0

    for j in range(0,len(matriz1[i])):
        for i in range(0,len(matriz1)):
            suma += matriz1[i][j]

    return suma

def sumaFilaColumna (matriz1):
    suma = 0
    listaF = []
    listaC = []
    for i in range(0,len(matriz1)):
        for j in range(0,len(matriz1[i])):
            suma += matriz1[i][j]
        listaF.append(suma)
        suma = 0
    
    matrizFilaColumna = [listaF, listaC]
    return listaF

matriz1 = [[1, 31],[2, 28],[3, 31],[4, 30],[5, 31],[6, 30],[7, 31],[8, 31],[9, 30],[10, 31],[11, 30],[12, 31]]

print(sumaFilaColumna(matriz1))