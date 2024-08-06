def InvertirElemento0N (lista):
    workingList = lista
    ultimoElemento = workingList.pop()
    primerElemento = workingList.pop(0)

    workingList.append(primerElemento)

    workingList = [ultimoElemento] + workingList

    return workingList

listaEvaluar = [0,2,3,64,3,4,2,3,4,22,34,2,1,3,3,3,4]

print(InvertirElemento0N(listaEvaluar))