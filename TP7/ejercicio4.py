'''
Escribir una función para contar cuántas veces aparece un valor dentro de la
lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
un número entero.
'''
def rangoLista(a,b):
    listaValores = []
    inputValue = int(input('Ingrese un numero \n'))

    while(inputValue!= -1):
        if (a<b):
            for i in range(a,b+1,1):
                if(i==inputValue):
                    listaValores.append(inputValue)
        elif(b<a):
            for i in range(a+1,b,-1):
                if(i==inputValue):
                    listaValores.append(inputValue)
        else:
            if(a==inputValue):
                listaValores.append(inputValue)

        inputValue = int(input('Ingrese un numero \n'))
        
    return listaValores

def contarValor (lista, valor):
    print(lista)
    contadorIgualdad = 0
    for i in range(0,len(lista)):
        if (lista[i]== valor):
            contadorIgualdad += 1
    return contadorIgualdad


a = int(input('Ingrese un numero \n'))
b = int(input('Ingrese un numero \n'))

listaParaEvaluacion = rangoLista(a,b)
nValoresEnLista = contarValor(listaParaEvaluacion,int(input('Ingrese valor a evaluar \n')))
print(nValoresEnLista)
