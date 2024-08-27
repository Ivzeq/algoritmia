'''
1.	Desarrollar cada una de las siguientes funciones y
escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a.	Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
Realice la composición de la lista por comprensión y de la forma habitual (tendrá dos funciones distintas).
b.	Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c.	Eliminar todas las apariciones de un valor en la lista anterior.
El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro. Utilice comprensión de listas para resolverlo.
d.	Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50,17,91,17,50].

'''

from random import randint

def randomInt4 ():
    nElementos = randint(10,99)
    lista1 = []
    metodosEquivalentes = False
    
    for numero in range(nElementos):
        lista1.append(randint(1000,9999))
        
    lista2 = [randint(1000,9999) for numero in range(nElementos)]
    
    if (len(lista1) == len(lista2)):
        metodosEquivalentes = True
    
    return lista2

def sumarElementos (lista):
    return sum(lista)

def eliminarElemento (elemento, lista):
    return [ numero for numero in lista if numero != elemento]

def isCapicua (lista):     
    return lista == lista [::-1]

listaGenerada = randomInt4()

print(listaGenerada)
print('Sumatoria:',sumarElementos(randomInt4()))
print(eliminarElemento(int(input('Ingrese elemento a eliminar\n')),listaGenerada))
print(isCapicua([50,17,91,17,50]))

