'''
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30). 
Debes usar una matriz para su parametrización y una función para la recuperación del dato.
'''
def getCantidadDias (mes, matriz):
    for fila in range(0, len(matriz)):
        if matriz[fila][0] == mes:
            return matriz [fila][1]

matriz=[[1,31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]
numeroDeMes = int(input('Ingrese mes\n'))

print(getCantidadDias(numeroDeMes, matriz))