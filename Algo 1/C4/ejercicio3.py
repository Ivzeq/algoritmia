'''
3.Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado.
Luego se solicita imprimir los últimos 10 valores de la lista utilizando segmentación de listas.
'''

def getListaCuadrados(numeroMax):
    return [elemento ** 2 for elemento in range(1,numeroMax + 1)]

def getLast10(lista):
    valorMax = 10
    
    if len(lista) < 10:
        valorMax = len(lista)
        
    return [lista[-elemento] for elemento in range(1,valorMax + 1)]
        

numero = int(input('Ingrese numero maximo \n'))
lista1 = getListaCuadrados(numero)


print(lista1)
print(getLast10(lista1))