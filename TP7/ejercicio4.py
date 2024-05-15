'''
Escribir una función para contar cuántas veces aparece un valor dentro de la
lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
un número entero.
'''

a = int(input('Ingrese un numero \n'))
b = int(input('Ingrese un numero \n'))
valorEvaluado = int(input('Ingrese valor a evaluar \n'))

def rangoLista(a,b):
    listaRango = []
    if (a<b):
        for i in range(a,b,1):
            listaRango.append(i)
    elif(b<a):
        for i in range(a,b,-1):
            listaRango.append(i)
    else:
        listaRango.append(a)
    return listaRango

def contarValor (lista, valor):
    contadorIgualdad = 0
    for i in range(len(lista)):
        if (lista[i]== valor):
            contadorIgualdad += 1
    return contadorIgualdad


listaParaEvaluacion = rangoLista(a,b)
nValoresEnLista = contarValor(listaParaEvaluacion,valorEvaluado)
print(nValoresEnLista)
