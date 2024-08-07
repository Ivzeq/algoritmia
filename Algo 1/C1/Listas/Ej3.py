'''
Crear un programa que combine dos listas en un recorrido sucesivo de sus índices en una tercera. 
Si las listas tienen diferentes longitudes, se debe notificar en pantalla que el proceso no se puede realizar.
'''

def CombinarListas (lista1, lista2):
    finalList = []
    if (len(lista1) == len(lista2)):
        for i in range(0, len(lista1)):
            finalList.append(lista1[i])
            finalList.append(lista2[i])
    else:
        return 'Las listas no tienen la misma longitud por lo que el proceso no se puede realizar'

    return finalList

listaEvaluar1 = [0,2,3,64,3,4,2,3,4,22,34,2,1,3,3,3,4]
listaEvaluar2 = [1,2,3,44,5,6,7,8,9,10,11,1,2,3,4,5,6]

print(CombinarListas(listaEvaluar1,listaEvaluar2))