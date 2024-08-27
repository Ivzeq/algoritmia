def productoEscalar (tupla1,tupla2):
    listaProductos = []
    for factor1 in tupla1:
        listaFactor = []
        for factor2 in tupla2:
            listaFactor.append((factor1*factor2))
        listaProductos.append(tuple(listaFactor))
    return tuple(listaProductos)

tupla1 = (1, 2, 3) 
tupla2 = (4, 5, 6)

tuplaFinal = productoEscalar(tupla1,tupla2)

print(tuplaFinal)

