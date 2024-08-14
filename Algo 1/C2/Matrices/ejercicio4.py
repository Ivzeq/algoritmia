'''
Producto Escalar: crear una función que tome una matriz y un número como entrada, 
y devuelva la matriz resultante de multiplicar cada elemento por el número dado.
'''

def sumarMatriz (matriz1,numero):
    matriz = []

    for i in range(0,len(matriz1)):
        listaF = []
        for j in range(0,len(matriz1[i])):
            listaF.append(matriz1[i][j] * numero)
        matriz.append(listaF)

    return matriz

matriz1 = [[1, 31],[2, 28],[3, 31],[4, 30],[5, 31],[6, 30],[7, 31],[8, 31],[9, 30],[10, 31],[11, 30],[12, 31]]
escalar = int(input('Ingrese un numero para el producto escalar\n'))

print(sumarMatriz(matriz1, escalar))