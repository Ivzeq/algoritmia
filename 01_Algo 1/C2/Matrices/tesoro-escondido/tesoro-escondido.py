from random import randint
\
def crearTablero(cantidad):
    tablero = []
    print('TESTING')
    for fila in range (0, cantidad - 1):
        for columna in range (0, cantidad -1):
            tablero[fila][columna]= 'O'
    return tablero

tablero = crearTablero(3)

print(tablero)