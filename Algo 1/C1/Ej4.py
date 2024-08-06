'''
Modifique el ejercicio anterior para que, 
en caso de que una de las listas tenga más elementos que la otra, 
se sumen dichos elementos al final de la nueva lista.
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