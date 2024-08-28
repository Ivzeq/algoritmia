'''
Crear una función que elimine los elementos de una lista que tengan un determinado valor.
'''
def EliminarValorEnLista (lista, valor):
    listaSinValor = lista
    isValorInLista = True

    while (isValorInLista):
        listaSinValor.remove(valor)
        if valor not in listaSinValor:
            isValorInLista = False

    return listaSinValor

listaEvaluar1 = [0,2,3,64,3,4,2,3,4,22,34,2,1,3,3,3,4]

print(EliminarValorEnLista(listaEvaluar1, 3))