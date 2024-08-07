'''
Escriba una función, que dada una lista con notas entre 0 y 10, 
retorne otra lista indicando su resultado por cada posición; 
utilizando una función que al recibir una nota retorne:

0: Ausente
Entre 1 y 3: Desaprobado
Entre 4 y 6: Aprobado
Entre 7 y 10: Promocionado
'''

def CombinarListas (lista1, lista2):
    finalList = []
    if (len(lista1) == len(lista2)):
        for i in range(0, len(lista1)):
            finalList.append(lista1[i])
            finalList.append(lista2[i])
    elif(len(lista1) > len(lista2)):
        for i in range(0, len(lista2)):
            finalList.append(lista1[i])
            finalList.append(lista2[i])
        for i in range(len(lista2), len(lista1)):
            finalList.append(lista1[i])
    else:
        for i in range(0, len(lista1)):
            finalList.append(lista1[i])
            finalList.append(lista2[i])
        for i in range(len(lista1), len(lista2)):
            finalList.append(lista2[i])
    return finalList

listaEvaluar1 = ["Hola","nombre", "Juan"]
listaEvaluar2 = ["mi","es", "Perez", "y", "tengo", "25", "años"]

print(CombinarListas(listaEvaluar1,listaEvaluar2))