'''
2.Escribir funciones para:
a.Generar una lista de 50 números aleatorios del 1 al 100. Utilice comprensión de listas para generar el resultado.
b.Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.
c.Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
'''

from random import randint

def generarLista1to100():
    return [randint(1,100) for numero in range(50)]

def isElementoInListaRepetido(lista):
    elementoRepetido = False
    for elemento in lista:
        if lista.count(elemento) > 1:
            elementoRepetido = True
    return elementoRepetido 

def getElementosUnicos (lista):
    return [elemento for elemento in lista if lista.count(elemento) == 1]
    
lista1 = generarLista1to100()

print(lista1)
print(isElementoInListaRepetido(lista1))
print(getElementosUnicos(lista1))