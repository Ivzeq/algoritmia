'''
Escribir una función para devolver una lista con todas las posiciones que ocupa un valor pasado como parámetro, utilizando búsqueda secuencial en una lista
desordenada. La función debe devolver una lista vacía si el elemento no se encuentra en la lista original.
'''
def rangoLista(a,b):
    listaValores = []
    inputValue = int(input('Ingrese un numero  \n'))

    while(inputValue!= -1):
        if (a<b):
            if(inputValue < b and inputValue > a):
                    listaValores.append(inputValue)
        elif(b<a):
            if(inputValue < a and inputValue > b):
                    listaValores.append(inputValue)
        else:
            if(a==inputValue):
                listaValores.append(inputValue)

        inputValue = int(input('Ingrese un numero \n'))
        
    return listaValores

def get_posiciones_listas (lista, valor):
    print(lista)
    posicionesValor = []
    for i in range(0,len(lista)):
        if (lista[i]== valor):
            posicionesValor.append(i)
    return posicionesValor


a = int(input('Ingrese un numero para limite 1 \n'))
b = int(input('Ingrese un numero para limite 2\n'))

listaParaEvaluacion = rangoLista(a,b)
posiciones_lista = get_posiciones_listas(listaParaEvaluacion,int(input('Ingrese valor a evaluar \n')))
print(posiciones_lista)
