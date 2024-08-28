'''
Suma de Matrices: escribir una función que reciba dos matrices como entrada y devuelva la matriz resultante de su suma. 
Se asume que ambas matrices tienen las mismas dimensiones.
'''

def sumarMatriz (matriz1,matriz2):
    matriz = []

    for i in range(0,len(matriz1)):
        listaF = []
        for j in range(0,len(matriz1[i])):
            listaF.append(matriz1[i][j] + matriz2[i][j])
        matriz.append(listaF)

    return matriz

matriz1 = [[1, 31],[2, 28],[3, 31],[4, 30],[5, 31],[6, 30],[7, 31],[8, 31],[9, 30],[10, 31],[11, 30],[12, 31]]
matriz2 = [[1, 31],[2, 28],[3, 31],[4, 30],[5, 31],[6, 30],[7, 31],[8, 31],[9, 30],[10, 31],[11, 30],[12, 31]]


print(sumarMatriz(matriz1, matriz2))